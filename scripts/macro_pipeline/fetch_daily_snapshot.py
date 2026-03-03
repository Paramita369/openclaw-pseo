#!/usr/bin/env python3
"""Fetch daily market snapshot for homepage widgets."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict

from pipeline_utils import ensure_dir, resolve_project_root

try:
    import yfinance as yf
except ImportError:  # pragma: no cover
    yf = None


ASSETS = {
    "BTC": "BTC-USD",
    "ETH": "ETH-USD",
    "SOL": "SOL-USD",
    "GOLD": "GC=F",
    "SPY": "SPY",
    "QQQ": "QQQ",
    "DXY": "DX-Y.NYB",
    "VIX": "^VIX",
    "TNX": "^TNX",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch daily snapshot")
    parser.add_argument("--project-root", default=None, help="Repository root")
    parser.add_argument("--output", default=None, help="Deprecated output json path (use --output-path)")
    parser.add_argument("--output-path", default=None, help="Override output json path")
    return parser.parse_args()


def fetch_snapshot(previous: Dict[str, object] | None = None) -> Dict[str, object]:
    results: Dict[str, Dict[str, float]] = {}
    if yf is None:
        previous_markets = (previous or {}).get("markets", {})
        return {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "markets": previous_markets if isinstance(previous_markets, dict) else {},
            "macro": {},
        }

    for name, ticker in ASSETS.items():
        data = yf.Ticker(ticker).history(period="5d")
        if len(data) < 2:
            continue
        latest = data.iloc[-1]
        prev = data.iloc[-2]
        prev_close = float(prev["Close"]) if float(prev["Close"]) != 0 else 1.0
        pct_change = ((float(latest["Close"]) - prev_close) / prev_close) * 100
        results[name] = {
            "price": round(float(latest["Close"]), 2),
            "change": round(pct_change, 2),
            "volume": int(latest.get("Volume", 0)),
            "high": round(float(latest["High"]), 2),
            "low": round(float(latest["Low"]), 2),
        }

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "markets": results,
        "macro": {},
    }


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    output_override = args.output_path or args.output
    output = Path(output_override).resolve() if output_override else root / "src" / "daily_snapshot.json"

    previous = None
    if output.exists():
        try:
            previous = json.loads(output.read_text(encoding="utf-8"))
        except Exception:
            previous = None

    snapshot = fetch_snapshot(previous=previous)
    ensure_dir(output.parent)
    output.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"✅ Daily snapshot saved: {output}")


if __name__ == "__main__":
    main()
