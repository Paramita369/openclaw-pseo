#!/usr/bin/env python3
"""Fetch CPI/NFP/FOMC outcomes and persist event direction metadata."""

from __future__ import annotations

import argparse
import csv
import json
import os
import sqlite3
import urllib.parse
import urllib.request
from bisect import bisect_right
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

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


def fetch_fred_series_csv(series_id: str) -> List[Tuple[str, float]]:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    with urllib.request.urlopen(url, timeout=30) as response:
        raw = response.read().decode("utf-8")

    rows: List[Tuple[str, float]] = []
    reader = csv.DictReader(raw.splitlines())
    for item in reader:
        observation_date = str(item.get("DATE") or item.get("date") or item.get("observation_date") or "").strip()
        value = parse_float(item.get(series_id))
        if not observation_date or value is None:
            continue
        rows.append((observation_date, float(value)))
    return rows


def fetch_fred_series(series_id: str, api_key: str) -> List[Tuple[str, float]]:
    params = {
        "series_id": series_id,
        "file_type": "json",
        "sort_order": "asc",
        "observation_start": "2010-01-01",
    }
    if api_key:
        params["api_key"] = api_key

    payload = None
    if api_key:
        query = urllib.parse.urlencode(params)
        url = f"https://api.stlouisfed.org/fred/series/observations?{query}"
        with urllib.request.urlopen(url, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
    else:
        try:
            query = urllib.parse.urlencode(params)
            url = f"https://api.stlouisfed.org/fred/series/observations?{query}"
            with urllib.request.urlopen(url, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except Exception:
            return fetch_fred_series_csv(series_id)

    rows: List[Tuple[str, float]] = []
    for item in (payload or {}).get("observations", []):
        observation_date = str(item.get("date", "")).strip()
        value = parse_float(item.get("value"))
        if not observation_date or value is None:
            continue
        rows.append((observation_date, float(value)))
    if not rows:
        return fetch_fred_series_csv(series_id)
    return rows


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
    conn.commit()


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    db_path = Path(args.db_path).resolve() if args.db_path else root / "data" / "macro_events.db"

    if args.provider != "fred":
        raise SystemExit(f"Unsupported provider: {args.provider}")

    fred_api_key = os.getenv("FRED_API_KEY", "").strip()
    as_of_cutoff = cutoff_date(args.as_of_date)

    conn = sqlite3.connect(db_path)
    try:
        ensure_table(conn)
        event_dates = fetch_event_dates(conn, as_of_cutoff)

        by_type_observations: Dict[str, List[Tuple[str, float]]] = {}
        for event_type, spec in FRED_SERIES.items():
            by_type_observations[event_type] = fetch_fred_series(spec["series_id"], fred_api_key)

        output_rows: List[OutcomeRow] = []
        for event_type in sorted(ALLOWED_EVENT_TYPES):
            unit = FRED_SERIES[event_type]["unit"]
            observations = by_type_observations.get(event_type, [])
            for event_date in event_dates.get(event_type, []):
                output_rows.append(
                    compute_outcome(
                        event_type=event_type,
                        event_date=event_date,
                        observations=observations,
                        unit=unit,
                        provider="fred",
                    )
                )

        upsert_outcomes(conn, output_rows)
    finally:
        conn.close()

    pending = [row for row in output_rows if row.status != "ok"]
    print(
        f"✅ Event outcomes updated: total={len(output_rows)} ok={len(output_rows) - len(pending)} pending={len(pending)} cutoff={as_of_cutoff}"
    )

    if args.strict and pending:
        preview = ", ".join(f"{row.event_type}:{row.event_date}" for row in pending[:5])
        raise SystemExit(f"Missing event outcomes for strict run: {preview}")


if __name__ == "__main__":
    main()
