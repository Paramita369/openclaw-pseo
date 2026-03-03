#!/usr/bin/env python3
"""Backfill macro events and historical impacts with idempotent inserts."""

from __future__ import annotations

import argparse
import sqlite3
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Tuple

import pandas as pd

from pipeline_utils import resolve_project_root


MACRO_EVENTS_2024 = [
    {"date": "2024-01-15", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-02-20", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-03-12", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-04-10", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-05-15", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-06-12", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-07-11", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-08-14", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-09-11", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-10-10", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-11-14", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-12-11", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-01-05", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-02-02", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-03-01", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-04-05", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-05-03", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-06-07", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-07-05", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-08-02", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-09-06", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-10-04", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-11-01", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-12-06", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-01-30", "event": "FOMC", "headline": "FOMC Rate Decision", "domain": "Macro"},
    {"date": "2024-03-19", "event": "FOMC", "headline": "FOMC Rate Decision", "domain": "Macro"},
    {"date": "2024-04-30", "event": "FOMC", "headline": "FOMC Rate Decision", "domain": "Macro"},
    {"date": "2024-06-11", "event": "FOMC", "headline": "FOMC Rate Decision", "domain": "Macro"},
    {"date": "2024-07-30", "event": "FOMC", "headline": "FOMC Rate Decision", "domain": "Macro"},
    {"date": "2024-09-17", "event": "FOMC", "headline": "FOMC Rate Decision", "domain": "Macro"},
    {"date": "2024-11-06", "event": "FOMC", "headline": "FOMC Rate Decision", "domain": "Macro"},
    {"date": "2024-12-17", "event": "FOMC", "headline": "FOMC Rate Decision", "domain": "Macro"},
]

MACRO_EVENTS_2025 = [
    {"date": "2025-01-15", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2025-02-12", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2025-01-10", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2025-01-29", "event": "FOMC", "headline": "FOMC Rate Decision", "domain": "Macro"},
]

ASSETS = ["BTC", "ETH", "GOLD", "SPY", "QQQ"]
TICKER_MAP = {
    "BTC": "BTC-USD",
    "ETH": "ETH-USD",
    "GOLD": "GC=F",
    "SPY": "SPY",
    "QQQ": "QQQ",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Historical backfill")
    parser.add_argument("--project-root", default=None, help="Repository root")
    parser.add_argument("--db-path", default=None, help="Database path")
    parser.add_argument("--max-events", type=int, default=None, help="Limit events to process")
    return parser.parse_args()


def get_historical_price(ticker: str, date_str: str) -> Tuple[Optional[float], Optional[float], Optional[float]]:
    try:
        import yfinance as yf

        stock = yf.Ticker(TICKER_MAP.get(ticker, ticker))
        target_date = datetime.strptime(date_str, "%Y-%m-%d")
        start = (target_date - timedelta(days=7)).strftime("%Y-%m-%d")
        end = (target_date + timedelta(days=14)).strftime("%Y-%m-%d")
        hist = stock.history(start=start, end=end)
        if hist.empty:
            return None, None, None

        hist = hist.reset_index()
        hist["date"] = pd.to_datetime(hist["Date"]).dt.date

        def close_on(day: datetime) -> Optional[float]:
            if day.date() in hist["date"].values:
                return float(hist[hist["date"] == day.date()].iloc[0]["Close"])
            return None

        t0 = close_on(target_date) or float(hist.iloc[0]["Close"])
        t1 = close_on(target_date + timedelta(days=1))
        t7 = close_on(target_date + timedelta(days=7))
        return t0, t1, t7
    except Exception as exc:
        print(f"⚠️ Price fetch failed for {ticker} @ {date_str}: {exc}")
        return None, None, None


def ensure_indexes(cursor: sqlite3.Cursor) -> None:
    cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS uniq_macro_event ON macro_events(date, headline)")
    cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS uniq_impact_event_ticker ON asset_impact(event_id, ticker)")


def insert_events_and_prices(db_path: Path, max_events: Optional[int]) -> int:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    ensure_indexes(cursor)

    all_events = MACRO_EVENTS_2024 + MACRO_EVENTS_2025
    if max_events is not None:
        all_events = all_events[:max_events]

    total_inserted = 0
    for event in all_events:
        event_date = event["date"]
        headline = event["headline"]

        cursor.execute("SELECT event_id FROM macro_events WHERE date = ? AND headline = ?", (event_date, headline))
        row = cursor.fetchone()
        if row:
            event_id = row[0]
        else:
            cursor.execute(
                """
                INSERT INTO macro_events (date, domain, headline, summary, sentiment_score, related_assets)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    event_date,
                    event["domain"],
                    headline,
                    f"{event['event']} historical data point for backtesting",
                    0.0,
                    ",".join(ASSETS),
                ),
            )
            event_id = cursor.lastrowid

        for asset in ASSETS:
            cursor.execute("SELECT impact_id FROM asset_impact WHERE event_id = ? AND ticker = ?", (event_id, asset))
            if cursor.fetchone():
                continue

            t0, t1, t7 = get_historical_price(asset, event_date)
            if t0 is None:
                continue

            impact_t1 = ((t1 - t0) / t0 * 100) if t1 is not None else None
            impact_t7 = ((t7 - t0) / t0 * 100) if t7 is not None else None

            cursor.execute(
                """
                INSERT INTO asset_impact
                (event_id, ticker, asset_class, exchange, price_t0, price_t1, price_t7, impact_t1_pct, impact_t7_pct)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    event_id,
                    asset,
                    "Crypto" if asset in {"BTC", "ETH"} else "Stock",
                    "BINANCE" if asset in {"BTC", "ETH"} else "NYSE",
                    t0,
                    t1,
                    t7,
                    round(impact_t1, 2) if impact_t1 is not None else None,
                    round(impact_t7, 2) if impact_t7 is not None else None,
                ),
            )
            total_inserted += 1
            time.sleep(0.2)

    conn.commit()
    conn.close()
    return total_inserted


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    db_path = Path(args.db_path).resolve() if args.db_path else root / "data" / "macro_events.db"

    inserted = insert_events_and_prices(db_path, args.max_events)
    print(f"✅ Backfill complete. New impact rows: {inserted}")


if __name__ == "__main__":
    main()
