#!/usr/bin/env python3
"""Generate event-driven Astro markdown pages with strict quality controls."""

from __future__ import annotations

import argparse
import csv
import json
import os
import sqlite3
import statistics
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

from pipeline_utils import (
    ALLOWED_EVENT_TYPES,
    canonical_slug,
    cutoff_date,
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

CSV_EXTRA_COLUMNS = [
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
]


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
    slug_redirects_path: Path
    vercel_config_path: Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Astro markdown pages with strict quality gates")
    parser.add_argument("--project-root", default=None, help="Repository root path")
    parser.add_argument("--db-path", default=None, help="Path to macro_events.db")
    parser.add_argument("--csv-path", default=None, help="Path to verified_targets.csv")
    parser.add_argument("--output-dir", default=None, help="Path to src/content/blog")
    parser.add_argument("--manifest-path", default=None, help="Path to page_manifest.json")
    parser.add_argument("--offers-config", default=None, help="Path to config/offers.yaml")
    parser.add_argument("--as-of-date", default=date.today().isoformat(), help="Pipeline run date (YYYY-MM-DD)")
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
        slug_redirects_path=root / "data" / "slug_redirects.json",
        vercel_config_path=root / "vercel.json",
    )


def ensure_csv_contract(csv_path: Path, rows: List[Dict[str, Any]]) -> None:
    if not rows:
        return

    headers = list(rows[0].keys())
    missing = [column for column in CSV_EXTRA_COLUMNS if column not in headers]
    if not missing:
        return

    fieldnames = headers + missing
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            for key in missing:
                row.setdefault(key, "")
            writer.writerow(row)


def load_targets(csv_path: Path, strict: bool) -> List[Dict[str, Any]]:
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = set(reader.fieldnames or [])

        missing = REQUIRED_CSV_COLUMNS - headers
        if missing:
            message = f"Missing required CSV columns: {sorted(missing)}"
            if strict:
                raise ValueError(message)
            print(f"⚠️ {message}. Falling back to legacy mapping.")

        rows: List[Dict[str, Any]] = []
        for row in reader:
            if not row.get("url_slug") and not row.get("date"):
                if strict:
                    raise ValueError(f"Row missing url_slug/date: {row}")
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

    ensure_csv_contract(csv_path, rows)

    rows.sort(key=lambda item: item.get("date", ""), reverse=True)
    return rows


def event_filter_sql(event_type: str) -> str:
    if event_type == "CPI":
        return "UPPER(m.headline) LIKE '%CPI%'"
    if event_type == "NFP":
        return "UPPER(m.headline) LIKE '%NFP%'"
    if event_type == "FOMC":
        return "UPPER(m.headline) LIKE '%FOMC%'"
    return "1=0"


def fetch_event_distribution(db_path: Path, ticker: str, event_type: str, asof_date: str) -> Dict[str, Any]:
    if not db_path.exists():
        return {
            "rows": [],
            "sample_size": 0,
            "latest_event_date": asof_date,
            "by_date": {},
        }

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(
            f"""
            SELECT
              m.date AS event_date,
              AVG(a.impact_t1_pct) AS impact_t1_pct,
              AVG(a.impact_t7_pct) AS impact_t7_pct
            FROM asset_impact a
            JOIN macro_events m ON a.event_id = m.event_id
            WHERE a.ticker = ?
              AND m.date <= ?
              AND {event_filter_sql(event_type)}
            GROUP BY m.date
            ORDER BY m.date ASC
            """,
            (ticker.upper(), asof_date),
        )
        fetched = cursor.fetchall()
    finally:
        conn.close()

    rows = []
    by_date: Dict[str, Dict[str, Optional[float]]] = {}
    for event_date, impact_t1, impact_t7 in fetched:
        item = {
            "event_date": event_date,
            "impact_t1_pct": parse_float(impact_t1),
            "impact_t7_pct": parse_float(impact_t7),
        }
        rows.append(item)
        by_date[event_date] = {
            "impact_t1_pct": item["impact_t1_pct"],
            "impact_t7_pct": item["impact_t7_pct"],
        }

    latest = rows[-1]["event_date"] if rows else asof_date

    return {
        "rows": rows,
        "sample_size": len(rows),
        "latest_event_date": latest,
        "by_date": by_date,
    }


def probability_window(values: List[float]) -> Dict[str, float]:
    if not values:
        return {
            "up": 0.0,
            "down": 100.0,
            "median": 0.0,
            "mean": 0.0,
            "sample": 0,
        }

    sample = len(values)
    up_ratio = sum(1 for value in values if value > 0) / sample
    up = round(up_ratio * 100, 2)
    down = round(100 - up, 2)

    return {
        "up": up,
        "down": down,
        "median": round(float(statistics.median(values)), 2),
        "mean": round(float(statistics.mean(values)), 2),
        "sample": sample,
    }


def signal_from_probabilities(t1_up: float, t7_up: float, median_t7: float) -> Tuple[str, float]:
    signal_score = 0.5 * (t7_up - 50) + 0.3 * (t1_up - 50) + 0.2 * (float((median_t7 > 0) - (median_t7 < 0)) * 10)

    if signal_score >= 8:
        return "Bullish", round(signal_score, 2)
    if signal_score <= -8:
        return "Bearish", round(signal_score, 2)
    return "Neutral", round(signal_score, 2)


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


def generate_llm_analysis(asset: str, event_type: str, probabilities: Dict[str, Any], context: BuildContext) -> Optional[str]:
    if not context.llm_enabled:
        return None

    prompt = f"""Write a concise quantitative analysis in English.
Asset: {asset}
Event: {event_type}
T+1 Up Probability: {probabilities['t1']['up']}%
T+7 Up Probability: {probabilities['t7']['up']}%
T+7 Median Return: {probabilities['t7']['median']}%
Sample Size: {probabilities['sample_size']}

Rules:
- 90-130 words
- Educational and data-driven
- No investment advice
- No markdown heading
"""

    url = "https://api.minimax.chat/v1/text/chatcompletion_pro"
    headers = {
        "Authorization": f"Bearer {context.llm_api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "abab6.5s-chat",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 220,
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


def fallback_analysis(asset: str, event_type: str, probabilities: Dict[str, Any], signal: str) -> str:
    return (
        f"For {asset}, historical {event_type} windows currently show a T+1 up probability of "
        f"{probabilities['t1']['up']}% and a T+7 up probability of {probabilities['t7']['up']}%. "
        f"Median T+7 return is {probabilities['t7']['median']}% across {probabilities['sample_size']} samples. "
        f"Current classification is {signal}, which should be treated as an educational probability view, not a trade instruction."
    )


def build_markdown(
    *,
    asset: str,
    title: str,
    publish_date: str,
    event_date: str,
    event_type: str,
    event_label: str,
    event_slug: str,
    asof_date: str,
    source: str,
    intent: str,
    offer_key: str,
    signal: str,
    confidence_level: str,
    quality: int,
    sample_size: int,
    metrics: Dict[str, float],
    probabilities: Dict[str, Any],
    analysis: str,
    chart_data: List[Dict[str, Any]],
) -> str:
    tags = [asset.lower(), event_type.lower(), "event-probability", intent.replace(" ", "-").lower()]

    chart_line = f"chartData: {json.dumps(chart_data)}\n" if chart_data else ""

    return f"""---
title: "{title}"
description: "Historical probability profile for {asset} around {event_type} events (T+1/T+7)."
pubDate: "{publish_date}"
event_type: "{event_type}"
event_label: "{event_label}"
event_slug: "{event_slug}"
event_date: "{event_date}"
asof_date: "{asof_date}"
source: "{source}"
offer_key: "{offer_key}"
signal: "{signal}"
confidence_level: "{confidence_level}"
quality_score: {quality}
sample_size: {sample_size}
tags: {json.dumps(tags)}
metrics:
  sharpe_t7: {metrics['sharpe_t7']}
  mdd_t7: {metrics['mdd_t7']}
  volatility: {metrics['volatility']}
  impact_t1_pct: {metrics['impact_t1_pct']}
  impact_t7_pct: {metrics['impact_t7_pct']}
probabilities:
  sample_size: {probabilities['sample_size']}
  t1:
    up: {probabilities['t1']['up']}
    down: {probabilities['t1']['down']}
    median: {probabilities['t1']['median']}
    mean: {probabilities['t1']['mean']}
    sample: {probabilities['t1']['sample']}
  t7:
    up: {probabilities['t7']['up']}
    down: {probabilities['t7']['down']}
    median: {probabilities['t7']['median']}
    mean: {probabilities['t7']['mean']}
    sample: {probabilities['t7']['sample']}
{chart_line}---

## Event Snapshot

- Event: **{event_label}**
- Asset: **{asset}**
- Event date: **{event_date}**
- As-of date (T-1): **{asof_date}**
- Sample size: **{sample_size}**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | {probabilities['t1']['up']}% | {probabilities['t1']['down']}% | {probabilities['t1']['median']}% | {probabilities['t1']['mean']}% | {probabilities['t1']['sample']} |
| T+7 | {probabilities['t7']['up']}% | {probabilities['t7']['down']}% | {probabilities['t7']['median']}% | {probabilities['t7']['mean']}% | {probabilities['t7']['sample']} |

## Historical Distribution Summary

T+1 Up Probability: **{probabilities['t1']['up']}%** (n={probabilities['t1']['sample']})

T+7 Up Probability: **{probabilities['t7']['up']}%** (n={probabilities['t7']['sample']})

T+7 Median Return: **{probabilities['t7']['median']}%**

{analysis}

## Methodology

This page aggregates historical windows for the same event type ({event_label}) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
"""


def quality_score(raw_t1: Optional[float], raw_t7: Optional[float], raw_vol: Optional[float], sample_size: int) -> int:
    score = 100
    if raw_t1 is None:
        score -= 10
    if raw_t7 is None:
        score -= 10
    if raw_vol is None or raw_vol == 0:
        score -= 10
    if sample_size < 5:
        score -= 20
    if sample_size < 10:
        score -= 10
    return max(0, min(100, score))


def row_fingerprint(payload: Dict[str, Any]) -> str:
    return stable_hash(payload)


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


def write_slug_redirects(path: Path, slug_redirects: Dict[str, str]) -> None:
    redirects = [
        {
            "source": f"/blog/{source}",
            "destination": f"/blog/{destination}",
            "permanent": True,
        }
        for source, destination in sorted(slug_redirects.items())
        if source != destination
    ]

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(redirects),
        "redirects": redirects,
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def sync_vercel_redirects(vercel_config_path: Path, slug_redirects: Dict[str, str]) -> None:
    if vercel_config_path.exists():
        try:
            config = json.loads(vercel_config_path.read_text(encoding="utf-8"))
        except Exception:
            config = {}
    else:
        config = {}

    existing = config.get("redirects", [])
    redirect_map: Dict[str, Dict[str, Any]] = {}
    for item in existing:
        source = item.get("source")
        if isinstance(source, str) and source:
            redirect_map[source] = item

    for source, destination in slug_redirects.items():
        if source == destination:
            continue
        source_path = f"/blog/{source}"
        destination_path = f"/blog/{destination}"
        redirect_map[source_path] = {
            "source": source_path,
            "destination": destination_path,
            "permanent": True,
        }

    config["redirects"] = [redirect_map[key] for key in sorted(redirect_map.keys())]
    vercel_config_path.write_text(json.dumps(config, indent=2, ensure_ascii=False), encoding="utf-8")


def process_row(row: Dict[str, Any], context: BuildContext, manifest: Dict[str, Any]) -> Dict[str, Any]:
    asset = str(row.get("asset", "")).upper().strip()
    event_date = str(row.get("date", "")).strip()
    event_type = normalize_event_type(str(row.get("event_type", "")), event_date)
    if event_type not in ALLOWED_EVENT_TYPES:
        if context.strict:
            raise ValueError(f"Unsupported event type for row: {row}")
        return {"status": "skipped", "slug": row.get("url_slug", "unknown")}

    slug = canonical_slug(asset, event_type, event_date)
    legacy_slug = str(row.get("url_slug", "")).strip()

    source = str(row.get("source", "verified_targets.csv")).strip() or "verified_targets.csv"
    intent = str(row.get("intent", "analysis")).strip() or "analysis"

    summary = fetch_event_distribution(
        db_path=context.db_path,
        ticker=asset,
        event_type=event_type,
        asof_date=cutoff_date(context.as_of_date),
    )
    by_date = summary.get("by_date", {})
    current_event = by_date.get(event_date, {})

    raw_t1 = parse_float(row.get("impact_t1_pct"))
    raw_t7 = parse_float(row.get("impact_t7_pct"))
    raw_vol = parse_float(row.get("volatility"))
    raw_sharpe = parse_float(row.get("sharpe_t7"))
    raw_mdd = parse_float(row.get("mdd_t7"))

    if raw_t1 is None:
        raw_t1 = parse_float(current_event.get("impact_t1_pct"))
    if raw_t7 is None:
        raw_t7 = parse_float(current_event.get("impact_t7_pct"))

    t1_values = [r["impact_t1_pct"] for r in summary["rows"] if r["impact_t1_pct"] is not None]
    t7_values = [r["impact_t7_pct"] for r in summary["rows"] if r["impact_t7_pct"] is not None]

    t1_window = probability_window([float(v) for v in t1_values])
    t7_window = probability_window([float(v) for v in t7_values])

    probabilities = {
        "sample_size": int(summary.get("sample_size", 0)),
        "t1": t1_window,
        "t7": t7_window,
    }

    signal, signal_score = signal_from_probabilities(t1_window["up"], t7_window["up"], t7_window["median"])
    confidence_level = "normal" if probabilities["sample_size"] >= 5 else "low"

    impact_t1 = raw_t1 if raw_t1 is not None else t1_window["mean"]
    impact_t7 = raw_t7 if raw_t7 is not None else t7_window["mean"]

    volatility = raw_vol
    if volatility is None:
        volatility = round(abs((impact_t7 or 0.0) - (impact_t1 or 0.0)), 2)

    sharpe = raw_sharpe
    if sharpe is None:
        denominator = volatility if volatility not in (None, 0) else 1.0
        sharpe = round((impact_t7 or 0.0) / denominator, 2)

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

    quality = quality_score(raw_t1, raw_t7, raw_vol, probabilities["sample_size"])
    offer_key = to_offer_key(asset, context.offers_config)

    title = f"{asset} After {event_type} ({event_date}): Historical T+1/T+7 Probability"
    event_label = event_type
    event_slug = event_type.lower()
    asof_date = summary.get("latest_event_date") or cutoff_date(context.as_of_date)

    llm_text = generate_llm_analysis(asset, event_type, probabilities, context)
    analysis = llm_text or fallback_analysis(asset, event_type, probabilities, signal)

    chart_data = fetch_chart_data(asset, event_date)

    fingerprint_payload = {
        "asset": asset,
        "slug": slug,
        "legacy_slug": legacy_slug,
        "event_date": event_date,
        "event_type": event_type,
        "source": source,
        "intent": intent,
        "metrics": metrics,
        "probabilities": probabilities,
        "signal": signal,
        "confidence_level": confidence_level,
        "quality": quality,
        "offer_key": offer_key,
        "asof_date": asof_date,
    }
    fingerprint = row_fingerprint(fingerprint_payload)

    previous = manifest.get("pages", {}).get(slug, {})
    target_file = context.output_dir / f"{slug}.md"

    need_generate = context.full or previous.get("hash") != fingerprint or (not target_file.exists())

    content = ""
    if need_generate:
        content = build_markdown(
            asset=asset,
            title=title,
            publish_date=context.as_of_date,
            event_date=event_date,
            event_type=event_type,
            event_label=event_label,
            event_slug=event_slug,
            asof_date=asof_date,
            source=source,
            intent=intent,
            offer_key=offer_key,
            signal=signal,
            confidence_level=confidence_level,
            quality=quality,
            sample_size=probabilities["sample_size"],
            metrics=metrics,
            probabilities=probabilities,
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
        "signal": signal,
        "signal_score": signal_score,
        "sample_size": probabilities["sample_size"],
        "asof_date": asof_date,
        "legacy_slugs": [legacy_slug] if legacy_slug and legacy_slug != slug else [],
    }

    if legacy_slug and legacy_slug != slug:
        manifest.setdefault("slug_redirects", {})[legacy_slug] = slug
        manifest.setdefault("legacy_slugs", {}).setdefault(slug, [])
        if legacy_slug not in manifest["legacy_slugs"][slug]:
            manifest["legacy_slugs"][slug].append(legacy_slug)
        if legacy_slug in manifest.get("pages", {}):
            del manifest["pages"][legacy_slug]

        legacy_file = context.output_dir / f"{legacy_slug}.md"
        if legacy_file.exists():
            legacy_file.unlink()

    # enrich row with new contract fields
    row["url_slug"] = slug
    row["title"] = title
    row["event_label"] = event_label
    row["event_slug"] = event_slug
    row["rise_prob_t1"] = str(t1_window["up"])
    row["fall_prob_t1"] = str(t1_window["down"])
    row["rise_prob_t7"] = str(t7_window["up"])
    row["fall_prob_t7"] = str(t7_window["down"])
    row["median_t1_pct"] = str(t1_window["median"])
    row["median_t7_pct"] = str(t7_window["median"])
    row["sample_size"] = str(probabilities["sample_size"])
    row["asof_date"] = asof_date
    row["signal"] = signal

    return {"status": "generated" if need_generate else "skipped", "slug": slug}


def write_targets_csv(csv_path: Path, rows: List[Dict[str, Any]]) -> None:
    if not rows:
        return

    base_fields = [
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
    fieldnames = base_fields + CSV_EXTRA_COLUMNS

    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def main() -> None:
    args = parse_args()
    context = build_context(args)

    targets = load_targets(context.csv_path, context.strict)
    manifest = load_manifest(context.manifest_path)

    changed_targets: List[Dict[str, Any]] = [
        row
        for row in targets
        if normalize_event_type(str(row.get("event_type", "")), str(row.get("date", "")).strip()) in ALLOWED_EVENT_TYPES
    ]

    if context.strict and len(changed_targets) != len(targets):
        invalid_rows = [row for row in targets if row not in changed_targets]
        raise ValueError(f"Found rows with unsupported event_type. examples={invalid_rows[:2]}")

    if context.max_pages is not None:
        changed_targets = changed_targets[: context.max_pages]

    print(f"📄 Total targets: {len(targets)}")
    print(f"🧩 Candidate targets: {len(changed_targets)}")

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

    # remove stale macro slugs that were migrated
    for old_slug, new_slug in list(manifest.get("slug_redirects", {}).items()):
        old_file = context.output_dir / f"{old_slug}.md"
        if old_file.exists() and old_slug != new_slug:
            old_file.unlink()

    generate_dynamic_sitemap(
        public_dir=context.public_dir,
        output_dir=context.output_dir,
        domain=f"https://{context.offers_config.get('default_domain', 'quantmacro.vercel.app')}",
    )

    write_slug_redirects(context.slug_redirects_path, manifest.get("slug_redirects", {}))
    sync_vercel_redirects(context.vercel_config_path, manifest.get("slug_redirects", {}))
    save_manifest(context.manifest_path, manifest)
    write_targets_csv(context.csv_path, targets)

    print(f"✅ Generated: {generated}, Skipped: {skipped}, Errors: {errors}")
    if errors > 0 and context.strict:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
