#!/usr/bin/env python3
"""Compute risk metrics (volatility, Sharpe, MDD) for asset impacts."""

from __future__ import annotations

import argparse
import math
import sqlite3
from pathlib import Path

from pipeline_utils import resolve_project_root


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Risk metrics calculator")
    parser.add_argument("--project-root", default=None, help="Repository root")
    parser.add_argument("--db-path", default=None, help="Database path")
    return parser.parse_args()


def ensure_columns(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(asset_impact)")
    columns = {row[1] for row in cursor.fetchall()}

    required = {
        "sharpe_t7": "REAL",
        "mdd_t7": "REAL",
        "volatility": "REAL",
    }
    for name, col_type in required.items():
        if name not in columns:
            cursor.execute(f"ALTER TABLE asset_impact ADD COLUMN {name} {col_type}")

    conn.commit()


def calculate_metrics(db_path: Path) -> None:
    conn = sqlite3.connect(db_path)
    ensure_columns(conn)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT impact_id, ticker, price_t0, price_t1, price_t3, price_t7
        FROM asset_impact
        WHERE price_t0 IS NOT NULL
        """
    )
    records = cursor.fetchall()

    processed = 0
    for impact_id, ticker, p0, p1, p3, p7 in records:
        prices = [p for p in [p0, p1, p3, p7] if p is not None and p > 0]
        if len(prices) < 3:
            continue

        returns = []
        for idx in range(1, len(prices)):
            prev = float(prices[idx - 1])
            curr = float(prices[idx])
            if prev == 0:
                continue
            returns.append((curr - prev) / prev)

        if len(returns) == 0:
            continue

        annual_factor = 365 if ticker in {"BTC", "ETH", "SOL"} else 252
        mean_return = sum(returns) / len(returns)
        variance = sum((ret - mean_return) ** 2 for ret in returns) / len(returns)
        std_daily = variance ** 0.5
        volatility_pct = round(std_daily * math.sqrt(annual_factor) * 100, 2)

        if std_daily == 0:
            sharpe = 0.0
        else:
            sharpe = float(mean_return / std_daily * math.sqrt(annual_factor))
        sharpe = round(max(-10.0, min(10.0, sharpe)), 2)

        cumulative_max = []
        current_max = float(prices[0])
        for price in prices:
            if price > current_max:
                current_max = float(price)
            cumulative_max.append(current_max)

        drawdowns = []
        for price, peak in zip(prices, cumulative_max):
            if peak == 0:
                continue
            drawdowns.append((float(price) - float(peak)) / float(peak))
        mdd_pct = round(float(min(drawdowns) * 100), 2) if drawdowns else 0.0

        cursor.execute(
            """
            UPDATE asset_impact
            SET sharpe_t7 = ?, mdd_t7 = ?, volatility = ?, updated_at = CURRENT_TIMESTAMP
            WHERE impact_id = ?
            """,
            (sharpe, mdd_pct, volatility_pct, impact_id),
        )
        processed += 1

    conn.commit()
    conn.close()
    print(f"✅ Risk metrics updated for {processed} records")


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    db_path = Path(args.db_path).resolve() if args.db_path else root / "data" / "macro_events.db"
    calculate_metrics(db_path)


if __name__ == "__main__":
    main()
