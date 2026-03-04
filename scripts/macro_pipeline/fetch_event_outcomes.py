#!/usr/bin/env python3
"""Fetch CPI/NFP/FOMC outcomes and persist event direction metadata."""

from __future__ import annotations

import argparse
import csv
import json
import os
import sqlite3
from bisect import bisect_right
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except Exception:  # pragma: no cover
    requests = None  # type: ignore
    HTTPAdapter = None  # type: ignore
    Retry = None  # type: ignore

from pipeline_utils import ALLOWED_EVENT_TYPES, cutoff_date, event_filter_sql, parse_float, resolve_project_root

FRED_SERIES = {
    "CPI": {"series_id": "CPIAUCSL", "unit": "index"},
    "NFP": {"series_id": "PAYEMS", "unit": "thousands"},
    "FOMC": {"series_id": "DFEDTARU", "unit": "percent"},
}


@dataclass
class OutcomeRow:
    event_type: str
    event_date: str
    actual_value: Optional[float]
    previous_value: Optional[float]
    delta_value: Optional[float]
    direction: str
    direction_basis: str
    unit: str
    provider: str
    status: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch macro event outcomes")
    parser.add_argument("--project-root", default=".", help="Repository root")
    parser.add_argument("--db-path", default=None, help="Path to macro_events.db")
    parser.add_argument("--source-db-path", default=None, help="Path to source macro_events.db for consistency sync")
    parser.add_argument("--as-of-date", default=date.today().isoformat(), help="Run date (YYYY-MM-DD)")
    parser.add_argument("--provider", default="fred", choices=["fred"], help="Outcome provider")
    parser.add_argument("--strict", action="store_true", help="Fail if any outcome is missing")
    return parser.parse_args()


def ensure_table(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS event_outcomes (
          event_type TEXT NOT NULL,
          event_date TEXT NOT NULL,
          actual_value REAL,
          previous_value REAL,
          delta_value REAL,
          direction TEXT NOT NULL,
          direction_basis TEXT NOT NULL,
          unit TEXT,
          provider TEXT NOT NULL,
          status TEXT NOT NULL,
          updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
          PRIMARY KEY(event_type, event_date, direction_basis)
        )
        """
    )
    cursor.execute(
        "CREATE INDEX IF NOT EXISTS idx_event_outcomes_provider ON event_outcomes(provider, event_type, event_date)"
    )
    conn.commit()


def table_exists(conn: sqlite3.Connection, table_name: str) -> bool:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name = ? LIMIT 1",
        (table_name,),
    )
    return cursor.fetchone() is not None


def fetch_event_dates(conn: sqlite3.Connection, as_of_cutoff: str) -> Dict[str, List[str]]:
    cursor = conn.cursor()
    grouped: Dict[str, List[str]] = {}
    if table_exists(conn, "event_calendar"):
        for event_type in sorted(ALLOWED_EVENT_TYPES):
            cursor.execute(
                """
                SELECT DISTINCT ec.event_date
                FROM event_calendar ec
                WHERE ec.event_type = ?
                  AND ec.event_date <= ?
                  AND LOWER(COALESCE(ec.status, 'confirmed')) NOT IN ('disabled', 'skip')
                ORDER BY ec.event_date ASC
                """,
                (event_type, as_of_cutoff),
            )
            grouped[event_type] = [str(row[0]) for row in cursor.fetchall()]
        return grouped

    for event_type in sorted(ALLOWED_EVENT_TYPES):
        cursor.execute(
            f"""
            SELECT DISTINCT m.date
            FROM macro_events m
            WHERE m.date <= ?
              AND {event_filter_sql(event_type)}
            ORDER BY m.date ASC
            """,
            (as_of_cutoff,),
        )
        grouped[event_type] = [str(row[0]) for row in cursor.fetchall()]
    return grouped


def get_fred_session():
    if requests is None:
        return None
    session = requests.Session()
    if Retry is not None and HTTPAdapter is not None:
        retries = Retry(
            total=3,
            connect=3,
            read=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods={"GET"},
            raise_on_status=False,
        )
        session.mount("https://", HTTPAdapter(max_retries=retries))
    return session


def fetch_fred_series_csv(series_id: str) -> List[Tuple[str, float]]:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    session = get_fred_session()
    if session is None:
        return []
    response = session.get(url, timeout=30)
    response.raise_for_status()
    raw = response.text

    rows: List[Tuple[str, float]] = []
    reader = csv.DictReader(raw.splitlines())
    for item in reader:
        observation_date = str(item.get("DATE") or item.get("date") or item.get("observation_date") or "").strip()
        value = parse_float(item.get(series_id))
        if not observation_date or value is None:
            continue
        rows.append((observation_date, float(value)))
    return rows


def fetch_fred_series(series_id: str, api_key: str) -> Tuple[List[Tuple[str, float]], str]:
    session = get_fred_session()
    if session is None:
        return [], "error"

    params = {
        "series_id": series_id,
        "file_type": "json",
        "sort_order": "asc",
        "observation_start": "2010-01-01",
    }
    if api_key:
        params["api_key"] = api_key

    payload: Dict[str, object] = {}
    try:
        response = session.get("https://api.stlouisfed.org/fred/series/observations", params=params, timeout=30)
        response.raise_for_status()
        parsed = response.json()
        if isinstance(parsed, dict):
            payload = parsed
    except Exception:
        try:
            return fetch_fred_series_csv(series_id), "csv"
        except Exception:
            return [], "error"

    rows: List[Tuple[str, float]] = []
    for item in payload.get("observations", []):
        observation_date = str(item.get("date", "")).strip()
        value = parse_float(item.get("value"))
        if not observation_date or value is None:
            continue
        rows.append((observation_date, float(value)))
    if not rows:
        try:
            return fetch_fred_series_csv(series_id), "csv"
        except Exception:
            return [], "error"
    return rows, "api"


def compute_outcome(
    *,
    event_type: str,
    event_date: str,
    observations: Sequence[Tuple[str, float]],
    unit: str,
    provider: str,
) -> OutcomeRow:
    dates = [item[0] for item in observations]
    values = [item[1] for item in observations]

    idx = bisect_right(dates, event_date) - 1
    if idx < 0:
        return OutcomeRow(
            event_type=event_type,
            event_date=event_date,
            actual_value=None,
            previous_value=None,
            delta_value=None,
            direction="unknown",
            direction_basis="vs_previous",
            unit=unit,
            provider=provider,
            status="pending",
        )

    actual_value = values[idx]
    previous_value = values[idx - 1] if idx - 1 >= 0 else None

    if previous_value is None:
        return OutcomeRow(
            event_type=event_type,
            event_date=event_date,
            actual_value=round(actual_value, 6),
            previous_value=None,
            delta_value=None,
            direction="unknown",
            direction_basis="vs_previous",
            unit=unit,
            provider=provider,
            status="pending",
        )

    delta = actual_value - previous_value
    if delta > 0:
        direction = "up"
    elif delta < 0:
        direction = "down"
    else:
        direction = "flat"

    return OutcomeRow(
        event_type=event_type,
        event_date=event_date,
        actual_value=round(actual_value, 6),
        previous_value=round(previous_value, 6),
        delta_value=round(delta, 6),
        direction=direction,
        direction_basis="vs_previous",
        unit=unit,
        provider=provider,
        status="ok",
    )


def upsert_outcomes(conn: sqlite3.Connection, outcomes: Sequence[OutcomeRow]) -> None:
    cursor = conn.cursor()
    for row in outcomes:
        cursor.execute(
            """
            INSERT INTO event_outcomes (
              event_type,
              event_date,
              actual_value,
              previous_value,
              delta_value,
              direction,
              direction_basis,
              unit,
              provider,
              status,
              updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(event_type, event_date, direction_basis)
            DO UPDATE SET
              actual_value = excluded.actual_value,
              previous_value = excluded.previous_value,
              delta_value = excluded.delta_value,
              direction = excluded.direction,
              unit = excluded.unit,
              provider = excluded.provider,
              status = excluded.status,
              updated_at = CURRENT_TIMESTAMP
            """,
            (
                row.event_type,
                row.event_date,
                row.actual_value,
                row.previous_value,
                row.delta_value,
                row.direction,
                row.direction_basis,
                row.unit,
                row.provider,
                row.status,
            ),
        )


def fetch_outcome_stats(conn: sqlite3.Connection) -> Dict[str, object]:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(1), MAX(event_date) FROM event_outcomes")
    row = cursor.fetchone() or (0, None)
    cursor.execute(
        """
        SELECT status, COUNT(1)
        FROM event_outcomes
        GROUP BY status
        ORDER BY status
        """
    )
    status_counts = {str(status or "unknown"): int(count) for status, count in cursor.fetchall()}
    return {
        "row_count": int(row[0] or 0),
        "max_event_date": str(row[1] or ""),
        "status_counts": status_counts,
    }


def compare_stats(runtime_stats: Dict[str, object], source_stats: Dict[str, object]) -> List[str]:
    violations: List[str] = []
    if runtime_stats.get("row_count") != source_stats.get("row_count"):
        violations.append(
            f"row_count_mismatch:runtime={runtime_stats.get('row_count')} source={source_stats.get('row_count')}"
        )
    if str(runtime_stats.get("max_event_date") or "") != str(source_stats.get("max_event_date") or ""):
        violations.append(
            "max_event_date_mismatch:"
            f"runtime={runtime_stats.get('max_event_date')} source={source_stats.get('max_event_date')}"
        )
    if runtime_stats.get("status_counts") != source_stats.get("status_counts"):
        violations.append(
            "status_counts_mismatch:"
            f"runtime={runtime_stats.get('status_counts')} source={source_stats.get('status_counts')}"
        )
    return violations


def load_existing_outcomes(conn: sqlite3.Connection) -> Dict[Tuple[str, str], OutcomeRow]:
    if not table_exists(conn, "event_outcomes"):
        return {}
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT
          event_type,
          event_date,
          actual_value,
          previous_value,
          delta_value,
          direction,
          direction_basis,
          unit,
          provider,
          status
        FROM event_outcomes
        WHERE direction_basis = 'vs_previous'
        """
    )
    rows = cursor.fetchall()
    mapping: Dict[Tuple[str, str], OutcomeRow] = {}
    for (
        event_type,
        event_date,
        actual_value,
        previous_value,
        delta_value,
        direction,
        direction_basis,
        unit,
        provider,
        status,
    ) in rows:
        key = (str(event_type or "").upper(), str(event_date or ""))
        mapping[key] = OutcomeRow(
            event_type=str(event_type or "").upper(),
            event_date=str(event_date or ""),
            actual_value=parse_float(actual_value),
            previous_value=parse_float(previous_value),
            delta_value=parse_float(delta_value),
            direction=str(direction or "unknown").lower(),
            direction_basis=str(direction_basis or "vs_previous"),
            unit=str(unit or ""),
            provider=str(provider or "fred"),
            status=str(status or "pending").lower(),
        )
    return mapping


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    runtime_db_path = Path(args.db_path).resolve() if args.db_path else root / "data" / "macro_events.db"
    source_db_path = Path(args.source_db_path).resolve() if args.source_db_path else runtime_db_path

    if args.provider != "fred":
        raise SystemExit(f"Unsupported provider: {args.provider}")
    if not runtime_db_path.exists():
        raise SystemExit(f"Runtime DB not found: {runtime_db_path}")
    if not source_db_path.exists():
        raise SystemExit(f"Source DB not found: {source_db_path}")

    fred_api_key = os.getenv("FRED_API_KEY", "").strip()
    as_of_cutoff = cutoff_date(args.as_of_date)
    same_db = runtime_db_path == source_db_path

    runtime_conn = sqlite3.connect(runtime_db_path)
    source_conn = runtime_conn if same_db else sqlite3.connect(source_db_path)
    output_rows: List[OutcomeRow] = []
    runtime_stats: Dict[str, object] = {"row_count": 0, "max_event_date": "", "status_counts": {}}
    source_stats: Dict[str, object] = {"row_count": 0, "max_event_date": "", "status_counts": {}}
    source_sync_status = "pending"
    runtime_sync_status = "pending"
    consistency_violations: List[str] = []
    fallback_reused_rows = 0
    fetch_statuses: Dict[str, str] = {}
    try:
        ensure_table(runtime_conn)
        if not same_db:
            ensure_table(source_conn)
        event_dates = fetch_event_dates(runtime_conn, as_of_cutoff)
        existing_outcomes = load_existing_outcomes(runtime_conn)

        by_type_observations: Dict[str, List[Tuple[str, float]]] = {}
        for event_type, spec in FRED_SERIES.items():
            observations, fetch_status = fetch_fred_series(spec["series_id"], fred_api_key)
            by_type_observations[event_type] = observations
            fetch_statuses[event_type] = fetch_status

        for event_type in sorted(ALLOWED_EVENT_TYPES):
            unit = FRED_SERIES[event_type]["unit"]
            observations = by_type_observations.get(event_type, [])
            fetch_status = fetch_statuses.get(event_type, "error")
            for event_date in event_dates.get(event_type, []):
                if fetch_status == "error":
                    existing = existing_outcomes.get((event_type, event_date))
                    if existing is not None:
                        output_rows.append(existing)
                        fallback_reused_rows += 1
                        continue

                computed = compute_outcome(
                    event_type=event_type,
                    event_date=event_date,
                    observations=observations,
                    unit=unit,
                    provider="fred",
                )
                output_rows.append(computed)

        if same_db:
            runtime_conn.execute("BEGIN")
            try:
                upsert_outcomes(runtime_conn, output_rows)
                runtime_conn.commit()
                runtime_sync_status = "ok"
                source_sync_status = "same_db"
            except Exception:
                runtime_conn.rollback()
                runtime_sync_status = "rollback"
                source_sync_status = "rollback"
                raise
        else:
            runtime_conn.execute("BEGIN")
            source_conn.execute("BEGIN")
            try:
                upsert_outcomes(runtime_conn, output_rows)
                upsert_outcomes(source_conn, output_rows)
                runtime_conn.commit()
                source_conn.commit()
                runtime_sync_status = "ok"
                source_sync_status = "ok"
            except Exception:
                runtime_conn.rollback()
                source_conn.rollback()
                runtime_sync_status = "rollback"
                source_sync_status = "rollback"
                raise

        runtime_stats = fetch_outcome_stats(runtime_conn)
        source_stats = runtime_stats if same_db else fetch_outcome_stats(source_conn)
        consistency_violations = compare_stats(runtime_stats, source_stats)
    finally:
        runtime_conn.close()
        if not same_db:
            source_conn.close()

    pending = [row for row in output_rows if row.status != "ok"]
    payload = {
        "total_rows": len(output_rows),
        "ok_rows": len(output_rows) - len(pending),
        "pending_rows": len(pending),
        "cutoff": as_of_cutoff,
        "runtime_db_path": str(runtime_db_path),
        "source_db_path": str(source_db_path),
        "runtime_sync_status": runtime_sync_status,
        "source_sync_status": source_sync_status,
        "runtime_stats": runtime_stats,
        "source_stats": source_stats,
        "consistency_violations": consistency_violations,
        "fetch_statuses": fetch_statuses,
        "fallback_reused_rows": fallback_reused_rows,
    }
    print(json.dumps(payload, ensure_ascii=False))

    if args.strict and pending:
        preview = ", ".join(f"{row.event_type}:{row.event_date}" for row in pending[:5])
        raise SystemExit(f"Missing event outcomes for strict run: {preview}")
    if args.strict and consistency_violations:
        raise SystemExit(f"event_outcomes consistency check failed: {consistency_violations[:3]}")


if __name__ == "__main__":
    main()
