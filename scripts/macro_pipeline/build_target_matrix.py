#!/usr/bin/env python3
"""Build full asset x event-date target matrix from macro_events DB."""

from __future__ import annotations

import argparse
import csv
import sqlite3
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from pipeline_utils import (
    ALLOWED_EVENT_TYPES,
    PRIMARY_ASSETS,
    canonical_slug,
    cutoff_date,
    event_filter_sql,
    parse_float,
    resolve_project_root,
)

FIELDNAMES = [
    "asset",
    "event_type",
    "date",
    "url_slug",
    "title",
    "impact_t1_pct",
    "impact_t7_pct",
    "volatility",
    "sharpe_t7",
    "mdd_t7",
    "intent",
    "source",
    "event_label",
    "event_slug",
    "rise_prob_t1",
    "fall_prob_t1",
    "rise_prob_t7",
    "fall_prob_t7",
    "median_t1_pct",
    "median_t7_pct",
    "sample_size",
    "asof_date",
    "signal",
    "event_direction",
    "event_actual",
    "event_previous",
    "event_delta",
    "direction_basis",
    "outcome_status",
]


@dataclass
class Outcome:
    direction: str
    actual: Optional[float]
    previous: Optional[float]
    delta: Optional[float]
    basis: str
    status: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build full target matrix")
    parser.add_argument("--project-root", default=".", help="Repository root")
    parser.add_argument("--db-path", default=None, help="Path to macro_events.db")
    parser.add_argument("--output", default=None, help="Path to verified_targets.csv")
    parser.add_argument("--as-of-date", default=date.today().isoformat(), help="Run date (YYYY-MM-DD)")
    parser.add_argument("--assets", nargs="*", default=list(PRIMARY_ASSETS), help="Assets to include")
    parser.add_argument("--strict", action="store_true", help="Fail if outcomes are missing")
    return parser.parse_args()


def to_text(value: Optional[float]) -> str:
    if value is None:
        return ""
    return str(round(float(value), 6))


def fetch_event_dates(conn: sqlite3.Connection, as_of_cutoff: str) -> Dict[str, List[str]]:
    cursor = conn.cursor()
    output: Dict[str, List[str]] = {}
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
        output[event_type] = [str(row[0]) for row in cursor.fetchall()]
    return output


def fetch_metrics(conn: sqlite3.Connection, asset: str, event_type: str, event_date: str) -> Dict[str, Optional[float]]:
    cursor = conn.cursor()
    cursor.execute(
        f"""
        SELECT
          AVG(a.impact_t1_pct) AS impact_t1_pct,
          AVG(a.impact_t7_pct) AS impact_t7_pct,
          AVG(a.volatility) AS volatility,
          AVG(a.sharpe_t7) AS sharpe_t7,
          AVG(a.mdd_t7) AS mdd_t7
        FROM asset_impact a
        JOIN macro_events m ON a.event_id = m.event_id
        WHERE a.ticker = ?
          AND m.date = ?
          AND {event_filter_sql(event_type)}
        """,
        (asset, event_date),
    )
    row = cursor.fetchone()
    if row is None:
        return {
            "impact_t1_pct": None,
            "impact_t7_pct": None,
            "volatility": None,
            "sharpe_t7": None,
            "mdd_t7": None,
        }

    return {
        "impact_t1_pct": parse_float(row[0]),
        "impact_t7_pct": parse_float(row[1]),
        "volatility": parse_float(row[2]),
        "sharpe_t7": parse_float(row[3]),
        "mdd_t7": parse_float(row[4]),
    }


def fetch_outcomes(conn: sqlite3.Connection) -> Dict[Tuple[str, str], Outcome]:
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT event_type, event_date, direction, actual_value, previous_value, delta_value, direction_basis, status
        FROM event_outcomes
        WHERE direction_basis = 'vs_previous'
        """
    )
    outcome_map: Dict[Tuple[str, str], Outcome] = {}
    for event_type, event_date, direction, actual_value, previous_value, delta_value, basis, status in cursor.fetchall():
        key = (str(event_type).upper(), str(event_date))
        outcome_map[key] = Outcome(
            direction=str(direction or "unknown").lower(),
            actual=parse_float(actual_value),
            previous=parse_float(previous_value),
            delta=parse_float(delta_value),
            basis=str(basis or "vs_previous"),
            status=str(status or "pending").lower(),
        )
    return outcome_map


def build_rows(
    *,
    event_dates: Dict[str, Sequence[str]],
    assets: Sequence[str],
    metrics_lookup,
    outcomes: Dict[Tuple[str, str], Outcome],
) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []

    for event_type in sorted(ALLOWED_EVENT_TYPES):
        dates = sorted(event_dates.get(event_type, []), reverse=True)
        for event_date in dates:
            for asset in assets:
                metrics = metrics_lookup(asset, event_type, event_date)
                outcome = outcomes.get((event_type, event_date))
                if outcome is None:
                    outcome = Outcome(
                        direction="unknown",
                        actual=None,
                        previous=None,
                        delta=None,
                        basis="vs_previous",
                        status="pending",
                    )

                slug = canonical_slug(asset=asset, event_type=event_type, event_date=event_date)
                rows.append(
                    {
                        "asset": asset,
                        "event_type": event_type,
                        "date": event_date,
                        "url_slug": slug,
                        "title": f"{asset} After {event_type} ({event_date}): Historical T+1/T+7 Probability",
                        "impact_t1_pct": to_text(metrics["impact_t1_pct"]),
                        "impact_t7_pct": to_text(metrics["impact_t7_pct"]),
                        "volatility": to_text(metrics["volatility"]),
                        "sharpe_t7": to_text(metrics["sharpe_t7"]),
                        "mdd_t7": to_text(metrics["mdd_t7"]),
                        "intent": "general",
                        "source": "verified_targets.csv",
                        "event_label": event_type,
                        "event_slug": event_type.lower(),
                        "rise_prob_t1": "",
                        "fall_prob_t1": "",
                        "rise_prob_t7": "",
                        "fall_prob_t7": "",
                        "median_t1_pct": "",
                        "median_t7_pct": "",
                        "sample_size": "",
                        "asof_date": "",
                        "signal": "",
                        "event_direction": outcome.direction,
                        "event_actual": to_text(outcome.actual),
                        "event_previous": to_text(outcome.previous),
                        "event_delta": to_text(outcome.delta),
                        "direction_basis": outcome.basis,
                        "outcome_status": outcome.status,
                    }
                )
    return rows


def write_csv(path: Path, rows: Iterable[Dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    db_path = Path(args.db_path).resolve() if args.db_path else root / "data" / "macro_events.db"
    output_path = Path(args.output).resolve() if args.output else root / "data" / "verified_targets.csv"

    as_of_cutoff = cutoff_date(args.as_of_date)
    assets = [asset.upper() for asset in args.assets if asset.strip()]

    conn = sqlite3.connect(db_path)
    try:
        event_dates = fetch_event_dates(conn, as_of_cutoff)
        outcomes = fetch_outcomes(conn)

        rows = build_rows(
            event_dates=event_dates,
            assets=assets,
            metrics_lookup=lambda asset, event_type, event_date: fetch_metrics(conn, asset, event_type, event_date),
            outcomes=outcomes,
        )
    finally:
        conn.close()

    write_csv(output_path, rows)

    expected = len(assets) * sum(len(values) for values in event_dates.values())
    pending = [row for row in rows if row.get("outcome_status") != "ok"]

    print(
        f"✅ Target matrix generated: rows={len(rows)} expected={expected} assets={len(assets)} cutoff={as_of_cutoff} pending_outcomes={len(pending)}"
    )

    if args.strict and len(rows) != expected:
        raise SystemExit(f"Target matrix mismatch: rows={len(rows)} expected={expected}")
    if args.strict and pending:
        sample = ", ".join(f"{r['asset']}:{r['event_type']}:{r['date']}" for r in pending[:5])
        raise SystemExit(f"Pending outcomes found in strict mode: {sample}")


if __name__ == "__main__":
    main()
