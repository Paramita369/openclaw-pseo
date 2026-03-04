#!/usr/bin/env python3
"""Bootstrap QuantMacro source DB with optional seed copy and schema guarantees."""

from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
import sys
from datetime import date
from pathlib import Path
from typing import Dict, List

try:
    from scripts.macro_pipeline.pipeline_utils import ensure_dir, resolve_project_root
except Exception:  # pragma: no cover
    CURRENT_FILE = Path(__file__).resolve()
    sys.path.insert(0, str(CURRENT_FILE.parents[1] / "macro_pipeline"))
    from pipeline_utils import ensure_dir, resolve_project_root


REQUIRED_TABLES = [
    "macro_events",
    "asset_impact",
    "event_calendar",
    "event_outcomes",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bootstrap source macro_events DB")
    parser.add_argument("--project-root", default=".", help="Repository root")
    parser.add_argument("--source-db-path", default=None, help="Source DB path (default: var/data/macro_events.db)")
    parser.add_argument("--seed-db-path", default=None, help="Optional seed DB to copy from")
    parser.add_argument("--as-of-date", default=date.today().isoformat(), help="Run date (YYYY-MM-DD)")
    parser.add_argument("--strict", action="store_true", help="Fail if required schema is missing")
    return parser.parse_args()


def table_exists(conn: sqlite3.Connection, table_name: str) -> bool:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name = ? LIMIT 1",
        (table_name,),
    )
    return bool(cursor.fetchone())


def ensure_schema(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS macro_events (
            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            domain TEXT NOT NULL,
            headline TEXT NOT NULL,
            summary TEXT,
            sentiment_score REAL,
            related_assets TEXT,
            embedding_id TEXT,
            metadata JSON,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS asset_impact (
            impact_id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER NOT NULL,
            ticker TEXT NOT NULL,
            asset_class TEXT NOT NULL,
            exchange TEXT,
            price_t0 REAL,
            price_t1 REAL,
            price_t3 REAL,
            price_t7 REAL,
            impact_t1_pct REAL,
            impact_t3_pct REAL,
            impact_t7_pct REAL,
            compound_return_pct REAL,
            volatility REAL,
            sharpe_t7 REAL,
            mdd_t7 REAL,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(event_id) REFERENCES macro_events(event_id)
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS vector_index (
            vector_id TEXT PRIMARY KEY,
            event_id INTEGER NOT NULL,
            vector_type TEXT,
            model_name TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(event_id) REFERENCES macro_events(event_id)
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS predictions (
            pred_id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_event_id INTEGER,
            query_headline TEXT,
            target_ticker TEXT,
            similar_event_ids TEXT,
            predicted_return_pct REAL,
            confidence_lower REAL,
            confidence_upper REAL,
            win_rate REAL,
            sample_size INTEGER,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS stock_assets (
            asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT UNIQUE NOT NULL,
            company_name TEXT,
            sector TEXT,
            market_cap REAL,
            country TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS event_calendar (
          event_type TEXT NOT NULL,
          event_date TEXT NOT NULL,
          source TEXT NOT NULL,
          status TEXT NOT NULL,
          release_ref TEXT,
          created_at TEXT DEFAULT CURRENT_TIMESTAMP,
          updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
          PRIMARY KEY(event_type, event_date)
        )
        """
    )

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

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_events_date ON macro_events(date)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_events_domain ON macro_events(domain)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_impact_event ON asset_impact(event_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_impact_ticker ON asset_impact(ticker)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_event_calendar_date ON event_calendar(event_date, event_type, status)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_event_outcomes_provider ON event_outcomes(provider, event_type, event_date)")
    conn.commit()


def summarize_counts(conn: sqlite3.Connection) -> Dict[str, int]:
    cursor = conn.cursor()
    out: Dict[str, int] = {}
    for table in ["macro_events", "asset_impact", "event_calendar", "event_outcomes"]:
        try:
            cursor.execute(f"SELECT COUNT(1) FROM {table}")
            out[table] = int(cursor.fetchone()[0])
        except Exception:
            out[table] = -1
    return out


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    source_db = Path(args.source_db_path).expanduser().resolve() if args.source_db_path else root / "var" / "data" / "macro_events.db"
    seed_db = Path(args.seed_db_path).expanduser().resolve() if args.seed_db_path else None

    ensure_dir(source_db.parent)

    status = "exists"
    used_seed = ""

    if not source_db.exists():
        status = "created"
        if seed_db is not None:
            if not seed_db.exists():
                raise SystemExit(f"Seed DB not found: {seed_db}")
            shutil.copy2(seed_db, source_db)
            used_seed = str(seed_db)
            status = "copied_from_seed"
        else:
            sqlite3.connect(source_db).close()

    conn = sqlite3.connect(source_db)
    try:
        ensure_schema(conn)
        missing_tables: List[str] = [name for name in REQUIRED_TABLES if not table_exists(conn, name)]
        counts = summarize_counts(conn)
        integrity = "unknown"
        try:
            cursor = conn.cursor()
            cursor.execute("PRAGMA integrity_check")
            row = cursor.fetchone()
            integrity = str(row[0]) if row else "unknown"
        except Exception:
            integrity = "unknown"
    finally:
        conn.close()

    payload = {
        "status": status,
        "source_db_path": str(source_db),
        "seed_db_path": used_seed,
        "as_of_date": args.as_of_date,
        "missing_tables": missing_tables,
        "counts": counts,
        "integrity_check": integrity,
    }
    print(json.dumps(payload, ensure_ascii=False))

    if args.strict:
        if missing_tables:
            raise SystemExit(f"Missing required tables after bootstrap: {missing_tables}")
        if integrity not in {"ok", "OK"}:
            raise SystemExit(f"SQLite integrity check failed: {integrity}")


if __name__ == "__main__":
    main()
