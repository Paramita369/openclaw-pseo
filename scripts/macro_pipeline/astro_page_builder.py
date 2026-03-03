#!/usr/bin/env python3
"""Generate blog markdown pages from verified target rows with strict quality controls."""

from __future__ import annotations

import argparse
import csv
import json
import os
import sqlite3
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

from pipeline_utils import (
    ensure_dir,
    load_config,
    load_manifest,
    normalize_event_type,
    parse_float,
    resolve_project_root,
    save_manifest,
    stable_hash,
    to_offer_key,
)


REQUIRED_CSV_COLUMNS = {
    "asset",
    "date",
    "url_slug",
    "title",
    "impact_t1_pct",
    "impact_t7_pct",
    "volatility",
    "sharpe_t7",
    "mdd_t7",
    "intent",
    "event_type",
    "source",
}


@dataclass
class BuildContext:
    project_root: Path
    csv_path: Path
    db_path: Path
    output_dir: Path
    public_dir: Path
    manifest_path: Path
    offers_config: Dict[str, Any]
    as_of_date: str
    llm_enabled: bool
    llm_api_key: str
    strict: bool
    full: bool
    max_pages: Optional[int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Astro markdown pages with strict quality gates")
    parser.add_argument("--project-root", default=None, help="Repository root path")
    parser.add_argument("--db-path", default=None, help="Path to macro_events.db")
    parser.add_argument("--csv-path", default=None, help="Path to verified_targets.csv")
    parser.add_argument("--output-dir", default=None, help="Path to src/content/blog")
    parser.add_argument("--manifest-path", default=None, help="Path to page_manifest.json")
    parser.add_argument("--offers-config", default=None, help="Path to config/offers.yaml")
    parser.add_argument("--as-of-date", default=date.today().isoformat(), help="Publish date (YYYY-MM-DD)")
    parser.add_argument("--max-pages", type=int, default=None, help="Maximum changed pages to generate")
    parser.add_argument("--full", action="store_true", help="Ignore manifest and regenerate all pages")
    parser.add_argument("--strict", action="store_true", help="Enable strict mode for malformed input")
    parser.add_argument("--no-llm", action="store_true", help="Disable LLM analysis generation")
    return parser.parse_args()


def build_context(args: argparse.Namespace) -> BuildContext:
    root = resolve_project_root(args.project_root)
    csv_path = Path(args.csv_path).resolve() if args.csv_path else root / "data" / "verified_targets.csv"
    db_path = Path(args.db_path).resolve() if args.db_path else root / "data" / "macro_events.db"
    output_dir = Path(args.output_dir).resolve() if args.output_dir else root / "src" / "content" / "blog"
    public_dir = root / "public"
    manifest_path = Path(args.manifest_path).resolve() if args.manifest_path else root / "data" / "page_manifest.json"
    offers_path = Path(args.offers_config).resolve() if args.offers_config else root / "config" / "offers.yaml"

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")
    if not offers_path.exists():
        raise FileNotFoundError(f"Offers config not found: {offers_path}")

    offers_config = load_config(offers_path)

    llm_key = os.environ.get("MINIMAX_API_KEY", "")
    llm_enabled = bool(llm_key) and (not args.no_llm)

    return BuildContext(
        project_root=root,
        csv_path=csv_path,
        db_path=db_path,
        output_dir=output_dir,
        public_dir=public_dir,
        manifest_path=manifest_path,
        offers_config=offers_config,
        as_of_date=args.as_of_date,
        llm_enabled=llm_enabled,
        llm_api_key=llm_key,
        strict=args.strict,
        full=args.full,
        max_pages=args.max_pages,
    )


def load_targets(csv_path: Path, strict: bool) -> List[Dict[str, Any]]:
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = set(reader.fieldnames or [])

        missing = REQUIRED_CSV_COLUMNS - headers
        if missing:
            message = f"Missing required CSV columns: {sorted(missing)}"
            if strict:
                raise ValueError(message)
            print(f"⚠️ {message}. Falling back to legacy column mapping.")

        rows = []
        for row in reader:
            if not row.get("url_slug"):
                if strict:
                    raise ValueError(f"Row missing url_slug: {row}")
                continue

            if not row.get("title") and row.get("h1_title"):
                row["title"] = row.get("h1_title")
            if not row.get("event_type"):
                row["event_type"] = row.get("macro_event", "")
            if not row.get("source"):
                row["source"] = "verified_targets.csv"
            if not row.get("intent"):
                row["intent"] = "analysis"

            rows.append(row)

    rows.sort(key=lambda item: item.get("date", ""), reverse=True)
    return rows


def row_fingerprint(row: Dict[str, Any], event_type: str) -> str:
    return stable_hash(
        {
            "asset": str(row.get("asset", "")).upper().strip(),
            "slug": str(row.get("url_slug", "")).strip(),
            "event_date": str(row.get("date", "")).strip(),
            "event_type": event_type,
            "source": str(row.get("source", "verified_targets.csv")).strip() or "verified_targets.csv",
            "intent": str(row.get("intent", "analysis")).strip() or "analysis",
            "impact_t1_pct": parse_float(row.get("impact_t1_pct"), 0.0),
            "impact_t7_pct": parse_float(row.get("impact_t7_pct"), 0.0),
            "volatility": parse_float(row.get("volatility"), 0.0),
            "sharpe_t7": parse_float(row.get("sharpe_t7"), 0.0),
            "mdd_t7": parse_float(row.get("mdd_t7"), 0.0),
        }
    )


def fetch_historical_summary(db_path: Path, ticker: str, event_type: str) -> Optional[Dict[str, Any]]:
    if not db_path.exists():
        return None

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT impact_t1_pct, impact_t7_pct
            FROM asset_impact a
            JOIN macro_events m ON a.event_id = m.event_id
            WHERE a.ticker = ? AND UPPER(m.headline) LIKE ?
            """,
            (ticker.upper(), f"%{event_type.upper()}%"),
        )
        rows = cursor.fetchall()
    finally:
        conn.close()

    if not rows:
        return None

    t1 = [parse_float(r[0]) for r in rows if parse_float(r[0]) is not None]
    t7 = [parse_float(r[1]) for r in rows if parse_float(r[1]) is not None]
    if not t1 and not t7:
        return None

    def avg(values: List[float]) -> float:
        return round(sum(values) / len(values), 2)

    result: Dict[str, Any] = {
        "sample_size": len(rows),
        "avg_t1": avg(t1) if t1 else 0.0,
        "avg_t7": avg(t7) if t7 else 0.0,
        "win_rate": round((sum(1 for x in t1 if x > 0) / len(t1)) * 100, 2) if t1 else 0.0,
    }
    if t7:
        mean_t7 = sum(t7) / len(t7)
        variance = sum((x - mean_t7) ** 2 for x in t7) / len(t7)
        result["std_t7"] = round(variance ** 0.5, 4)
    return result


def fetch_chart_data(asset: str, event_date: str) -> List[Dict[str, Any]]:
    try:
        import yfinance as yf
    except ImportError:
        return []

    ticker_map = {
        "BTC": "BTC-USD",
        "ETH": "ETH-USD",
        "SOL": "SOL-USD",
        "GOLD": "GC=F",
        "SPY": "SPY",
        "QQQ": "QQQ",
    }
    yf_ticker = ticker_map.get(asset.upper(), asset.upper())

    try:
        event_dt = datetime.strptime(event_date, "%Y-%m-%d")
        start = (event_dt - timedelta(days=3)).strftime("%Y-%m-%d")
        end = (event_dt + timedelta(days=8)).strftime("%Y-%m-%d")
        hist = yf.Ticker(yf_ticker).history(start=start, end=end)
    except Exception:
        return []

    if hist.empty:
        return []

    data = []
    for idx, row in hist.iterrows():
        data.append(
            {
                "time": idx.strftime("%Y-%m-%d"),
                "open": round(float(row["Open"]), 2),
                "high": round(float(row["High"]), 2),
                "low": round(float(row["Low"]), 2),
                "close": round(float(row["Close"]), 2),
            }
        )
    return data


def generate_llm_analysis(asset: str, event_type: str, metrics: Dict[str, float], context: BuildContext) -> Optional[str]:
    if not context.llm_enabled:
        return None

    prompt = f"""Write a concise quantitative market analysis in English.
Asset: {asset}
Event type: {event_type}
T+1: {metrics['impact_t1_pct']}%
T+7: {metrics['impact_t7_pct']}%
Sharpe: {metrics['sharpe_t7']}
MDD: {metrics['mdd_t7']}%
Volatility: {metrics['volatility']}%

Rules:
- 120-180 words
- Data-driven and educational
- No investment advice
- No markdown headings
"""

    url = "https://api.minimax.chat/v1/text/chatcompletion_pro"
    headers = {
        "Authorization": f"Bearer {context.llm_api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "abab6.5s-chat",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 300,
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        if response.status_code != 200:
            return None
        body = response.json()
        text = body.get("choices", [{}])[0].get("message", {}).get("content", "")
        text = (text or "").strip()
        return text or None
    except Exception:
        return None


def fallback_analysis(asset: str, event_type: str, summary: Optional[Dict[str, Any]], metrics: Dict[str, float]) -> str:
    if summary:
        return (
            f"Historical data indicates that {asset} reacts to {event_type} releases with a "
            f"T+1 average move of {summary.get('avg_t1', 0.0)}% and a T+7 average move of {summary.get('avg_t7', 0.0)}%. "
            f"Across {summary.get('sample_size', 0)} comparable events, short-horizon win rate is {summary.get('win_rate', 0.0)}%. "
            f"Current risk metrics for this page show Sharpe {metrics['sharpe_t7']} and max drawdown {metrics['mdd_t7']}%. "
            "Use this as an educational reference for event-driven volatility behavior."
        )

    return (
        f"This page tracks {asset} behavior around {event_type} events with quantitative metrics "
        "for educational research. Current sample density is still limited, so interpretation should "
        "focus on directional context rather than deterministic forecasting."
    )


def quality_score(
    raw_t1: Optional[float],
    raw_t7: Optional[float],
    raw_vol: Optional[float],
    event_type: str,
    summary: Optional[Dict[str, Any]],
    llm_used: bool,
) -> int:
    score = 100
    if raw_t1 is None:
        score -= 15
    if raw_t7 is None:
        score -= 15
    if raw_vol is None or raw_vol == 0:
        score -= 20
    if event_type == "MACRO":
        score -= 15
    if (summary or {}).get("sample_size", 0) < 3:
        score -= 10
    if not llm_used:
        score -= 5
    return max(0, min(100, score))


def build_markdown(
    *,
    asset: str,
    title: str,
    publish_date: str,
    event_date: str,
    event_type: str,
    source: str,
    intent: str,
    offer_key: str,
    quality: int,
    metrics: Dict[str, float],
    analysis: str,
    chart_data: List[Dict[str, Any]],
) -> str:
    tags = [asset.lower(), event_type.lower(), "backtest", intent.replace(" ", "-").lower()]

    chart_line = f"chartData: {json.dumps(chart_data)}\n" if chart_data else ""

    recommendation = "Neutral"
    if metrics["impact_t7_pct"] > 2:
        recommendation = "Bullish bias"
    elif metrics["impact_t7_pct"] < -2:
        recommendation = "Bearish bias"

    return f"""---
title: "{title}"
description: "Quantitative analysis of {asset} around {event_type} events based on historical backtesting."
pubDate: "{publish_date}"
event_type: "{event_type}"
source: "{source}"
offer_key: "{offer_key}"
quality_score: {quality}
tags: {json.dumps(tags)}
metrics:
  sharpe_t7: {metrics['sharpe_t7']}
  mdd_t7: {metrics['mdd_t7']}
  volatility: {metrics['volatility']}
  impact_t1_pct: {metrics['impact_t1_pct']}
  impact_t7_pct: {metrics['impact_t7_pct']}
{chart_line}---

# {title}

**Event Date:** {event_date}  
**Asset:** {asset}  
**Event Type:** {event_type}

## Historical Performance Data

| Metric | T+1 (24h) | T+7 (1 Week) |
| :--- | :---: | :---: |
| Average Return | {metrics['impact_t1_pct']}% | {metrics['impact_t7_pct']}% |
| Sharpe Ratio | {metrics['sharpe_t7']} | - |
| Max Drawdown | - | {metrics['mdd_t7']}% |
| Volatility | - | {metrics['volatility']}% |

## Trading Context (Educational)

**{recommendation}:** This page is informational and should not be treated as investment advice.

## Quantitative Analysis

{analysis}

## Methodology

Metrics are generated from historical event windows and normalized into T+1/T+7 returns. Past performance does not guarantee future results.
"""


def generate_dynamic_sitemap(public_dir: Path, output_dir: Path, domain: str) -> None:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    slugs = sorted(path.stem for path in output_dir.glob("*.md"))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]

    core_routes = [
        (f"{domain}/", "1.0", "daily"),
        (f"{domain}/blog", "0.9", "daily"),
        (f"{domain}/leaderboard", "0.8", "daily"),
    ]

    for loc, priority, freq in core_routes:
        lines.extend(
            [
                "  <url>",
                f"    <loc>{loc}</loc>",
                f"    <lastmod>{today}</lastmod>",
                f"    <changefreq>{freq}</changefreq>",
                f"    <priority>{priority}</priority>",
                "  </url>",
            ]
        )

    for slug in slugs:
        lines.extend(
            [
                "  <url>",
                f"    <loc>{domain}/blog/{slug}</loc>",
                f"    <lastmod>{today}</lastmod>",
                "    <changefreq>weekly</changefreq>",
                "    <priority>0.7</priority>",
                "  </url>",
            ]
        )

    lines.append("</urlset>")
    ensure_dir(public_dir)
    (public_dir / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")


def process_row(row: Dict[str, Any], context: BuildContext, manifest: Dict[str, Any]) -> Dict[str, Any]:
    asset = str(row.get("asset", "")).upper().strip()
    slug = str(row.get("url_slug", "")).strip()
    event_date = str(row.get("date", "")).strip()
    title = str(row.get("title", "")).strip() or f"{asset} after macro event on {event_date}"
    event_type = normalize_event_type(str(row.get("event_type", "")), event_date)
    source = str(row.get("source", "verified_targets.csv")).strip() or "verified_targets.csv"
    intent = str(row.get("intent", "analysis")).strip() or "analysis"

    if not asset or not slug or not event_date:
        raise ValueError(f"Invalid row: missing asset/slug/date => {row}")

    raw_t1 = parse_float(row.get("impact_t1_pct"))
    raw_t7 = parse_float(row.get("impact_t7_pct"))
    raw_vol = parse_float(row.get("volatility"))
    raw_sharpe = parse_float(row.get("sharpe_t7"))
    raw_mdd = parse_float(row.get("mdd_t7"))

    summary = fetch_historical_summary(context.db_path, asset, event_type)

    impact_t1 = raw_t1 if raw_t1 is not None else parse_float((summary or {}).get("avg_t1"), 0.0)
    impact_t7 = raw_t7 if raw_t7 is not None else parse_float((summary or {}).get("avg_t7"), 0.0)

    volatility = raw_vol
    if volatility is None:
        volatility = parse_float((summary or {}).get("std_t7"), None)
    if volatility is None:
        volatility = round(abs((impact_t7 or 0.0) - (impact_t1 or 0.0)), 2)

    sharpe = raw_sharpe
    if sharpe is None:
        sharpe = round((impact_t7 or 0.0) / (volatility or 1.0), 2)

    mdd = raw_mdd
    if mdd is None:
        mdd = round(min(0.0, impact_t1 or 0.0, impact_t7 or 0.0), 2)

    metrics = {
        "impact_t1_pct": round(float(impact_t1 or 0.0), 2),
        "impact_t7_pct": round(float(impact_t7 or 0.0), 2),
        "volatility": round(float(volatility or 0.0), 2),
        "sharpe_t7": round(float(sharpe or 0.0), 2),
        "mdd_t7": round(float(mdd or 0.0), 2),
    }

    llm_text = generate_llm_analysis(asset, event_type, metrics, context)
    analysis = llm_text or fallback_analysis(asset, event_type, summary, metrics)

    quality = quality_score(raw_t1, raw_t7, raw_vol, event_type, summary, bool(llm_text))
    offer_key = to_offer_key(asset, context.offers_config)

    chart_data = fetch_chart_data(asset, event_date)

    fingerprint = row_fingerprint(row, event_type)

    previous = manifest.get("pages", {}).get(slug, {})
    target_file = context.output_dir / f"{slug}.md"
    if (not context.full) and previous.get("hash") == fingerprint and target_file.exists():
        return {"status": "skipped", "slug": slug}

    content = build_markdown(
        asset=asset,
        title=title,
        publish_date=context.as_of_date,
        event_date=event_date,
        event_type=event_type,
        source=source,
        intent=intent,
        offer_key=offer_key,
        quality=quality,
        metrics=metrics,
        analysis=analysis,
        chart_data=chart_data,
    )

    ensure_dir(context.output_dir)
    target_file.write_text(content, encoding="utf-8")

    manifest.setdefault("pages", {})[slug] = {
        "hash": fingerprint,
        "source_event": event_type,
        "event_date": event_date,
        "last_generated": datetime.now(timezone.utc).isoformat(),
        "quality_score": quality,
        "offer_key": offer_key,
    }
    return {"status": "generated", "slug": slug}


def main() -> None:
    args = parse_args()
    context = build_context(args)

    targets = load_targets(context.csv_path, context.strict)
    manifest = load_manifest(context.manifest_path)

    changed_targets: List[Dict[str, Any]] = []
    for row in targets:
        asset = str(row.get("asset", "")).upper().strip()
        slug = str(row.get("url_slug", "")).strip()
        event_date = str(row.get("date", "")).strip()
        event_type = normalize_event_type(str(row.get("event_type", "")), event_date)

        fingerprint = row_fingerprint(row, event_type)
        prev = manifest.get("pages", {}).get(slug, {})
        file_exists = (context.output_dir / f"{slug}.md").exists()

        if context.full or (prev.get("hash") != fingerprint) or (not file_exists):
            changed_targets.append(row)

    if context.max_pages is not None:
        changed_targets = changed_targets[: context.max_pages]

    print(f"📄 Total targets: {len(targets)}")
    print(f"🧩 Changed targets: {len(changed_targets)}")

    generated = 0
    skipped = 0
    errors = 0

    for row in changed_targets:
        try:
            result = process_row(row, context, manifest)
            if result["status"] == "generated":
                generated += 1
            else:
                skipped += 1
        except Exception as exc:
            errors += 1
            slug = row.get("url_slug", "unknown")
            print(f"❌ Failed {slug}: {exc}")
            if context.strict:
                raise

    generate_dynamic_sitemap(
        public_dir=context.public_dir,
        output_dir=context.output_dir,
        domain=f"https://{context.offers_config.get('default_domain', 'quantmacro.vercel.app')}",
    )

    save_manifest(context.manifest_path, manifest)

    print(f"✅ Generated: {generated}, Skipped: {skipped}, Errors: {errors}")
    if errors > 0 and context.strict:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
