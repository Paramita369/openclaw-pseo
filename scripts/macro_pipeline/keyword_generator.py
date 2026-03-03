#!/usr/bin/env python3
"""Generate pSEO target matrix compatible with the strict CSV contract."""

from __future__ import annotations

import argparse
import csv
import itertools
from pathlib import Path
from typing import Iterable, List

from pipeline_utils import ensure_dir, normalize_event_type, resolve_project_root

ASSETS = ["BTC", "ETH", "GOLD", "SPY", "QQQ", "SOL"]
INTENTS = ["analysis", "historical-performance", "volatility", "correlation"]
EVENT_TYPES = ["CPI", "NFP", "FOMC"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Keyword matrix generator")
    parser.add_argument("--project-root", default=None, help="Repository root")
    parser.add_argument("--output", default=None, help="CSV output path")
    parser.add_argument("--assets", nargs="*", default=None, help="Override assets")
    parser.add_argument("--intents", nargs="*", default=None, help="Override intents")
    parser.add_argument("--events", nargs="*", default=None, help="Override event types")
    return parser.parse_args()


def slugify(parts: Iterable[str]) -> str:
    return "-".join(str(part).strip().lower().replace(" ", "-") for part in parts if str(part).strip())


def generate_rows(assets: List[str], intents: List[str], events: List[str]) -> List[dict]:
    rows: List[dict] = []
    for asset, intent, event_type in itertools.product(assets, intents, events):
        normalized_event = normalize_event_type(event_type, "")
        slug = slugify([asset, "after", normalized_event, intent])
        title = f"Historical {intent.replace('-', ' ').title()} of {asset} After {normalized_event} Events"
        rows.append(
            {
                "asset": asset,
                "event_type": normalized_event,
                "date": "",
                "url_slug": slug,
                "title": title,
                "impact_t1_pct": "",
                "impact_t7_pct": "",
                "volatility": "",
                "sharpe_t7": "",
                "mdd_t7": "",
                "intent": intent,
                "source": "keyword_generator",
            }
        )
    return rows


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    output = Path(args.output).resolve() if args.output else root / "data" / "verified_targets.csv"

    assets = [a.upper() for a in (args.assets or ASSETS)]
    intents = [i.lower() for i in (args.intents or INTENTS)]
    events = [e.upper() for e in (args.events or EVENT_TYPES)]

    rows = generate_rows(assets, intents, events)
    ensure_dir(output.parent)

    columns = [
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
    ]

    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Generated {len(rows)} keyword rows -> {output}")


if __name__ == "__main__":
    main()
