#!/usr/bin/env python3
"""Generate event-driven Astro markdown pages with strict quality controls."""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import re
import sqlite3
import statistics
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

try:
    import requests
except Exception:  # pragma: no cover
    requests = None
try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None

from pipeline_utils import (
    ALLOWED_EVENT_TYPES,
    canonical_slug,
    cutoff_date,
    ensure_dir,
    event_filter_sql,
    load_config,
    load_manifest,
    normalize_event_type,
    parse_float,
    resolve_project_root,
    save_manifest,
    stable_hash,
    to_offer_key,
)
from content_features import CORE_WINDOW_DAYS, FEATURE_EPSILON, compute_statistical_features, is_core_page_for_window

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
    "event_direction",
    "event_actual",
    "event_previous",
    "event_delta",
    "direction_basis",
    "outcome_status",
    "freshness_days",
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
    "conditional_sample_size",
    "asof_date",
    "freshness_days",
    "signal",
    "raw_signal_score",
    "robust_score",
    "title_variant_id",
    "title_template_key",
    "index_tier",
    "is_recent_90d",
    "canonical_target",
    "canonical_url",
    "robots_directive",
    "in_blog_sitemap",
    "confidence_level",
    "is_core_page",
    "core_window_days",
    "body_variant_family",
    "hub_baseline_mean_t7",
    "hub_baseline_median_t7",
    "hub_baseline_std_t7",
    "hub_baseline_delta",
    "z_score_t7",
    "percentile_t7",
    "narrative_trigger",
    "event_direction",
    "event_actual",
    "event_previous",
    "event_delta",
    "direction_basis",
    "outcome_status",
]

EVENT_FRESHNESS_THRESHOLDS = {
    "CPI": 45,
    "NFP": 45,
    "FOMC": 90,
}

HUB_ASSETS = ["BTC", "ETH", "GOLD", "QQQ", "SPY"]
HUB_EVENTS = ["CPI", "NFP", "FOMC"]
HUB_MIN_THESIS_LEN = 180
HUB_MIN_CHANGED_LEN = 120
HUB_MIN_RISK_LEN = 120
HUB_MIN_CHECKLIST_ITEMS = 3
HUB_MIN_CHECKLIST_ITEM_LEN = 12
BODY_VARIANT_FAMILIES = ("analyst", "distribution", "risk-first", "checklist")
TITLE_TEMPLATE_POOLS: Dict[str, List[str]] = {
    "CPI": [
        "{ASSET} CPI Win Rate ({DATE}): Historical T+1/T+7 Probability",
        "{ASSET} Reaction to US CPI ({DATE}): Quant Probability Breakdown",
        "US CPI ({DATE}) and {ASSET}: Event-Driven Return Odds",
        "{DATE} CPI Release: {ASSET} Directional Probability Snapshot",
        "{ASSET} After CPI ({DATE}): Up/Down Odds and Median Returns",
    ],
    "NFP": [
        "{ASSET} NFP Reaction ({DATE}): T+1/T+7 Up Probability",
        "{DATE} Nonfarm Payrolls: {ASSET} Historical Win Rate",
        "{ASSET} After NFP ({DATE}): Event Probability and Median Return",
        "NFP Print ({DATE}) vs {ASSET}: Quantified Directional Odds",
        "{ASSET} Post-NFP Setup ({DATE}): Historical Probability Lens",
    ],
    "FOMC": [
        "{ASSET} After FOMC ({DATE}): Historical Signal & Probability",
        "Fed Decision ({DATE}) and {ASSET}: Event-Driven Odds",
        "{DATE} FOMC Meeting: {ASSET} T+1/T+7 Probability Profile",
        "{ASSET} Post-FOMC Reaction ({DATE}): Quant Backtest Snapshot",
        "FOMC Outcome ({DATE}) for {ASSET}: Up/Down Probability View",
    ],
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
    hub_briefs: Dict[str, Dict[str, Any]]
    as_of_date: str
    llm_enabled: bool
    llm_api_key: str
    strict: bool
    full: bool
    max_pages: Optional[int]
    slug_redirects_path: Path
    vercel_config_path: Path
    skip_vercel_sync: bool
    build_timestamp: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Astro markdown pages with strict quality gates")
    parser.add_argument("--project-root", default=None, help="Repository root path")
    parser.add_argument("--db-path", default=None, help="Path to macro_events.db")
    parser.add_argument("--csv-path", default=None, help="Path to verified_targets.csv")
    parser.add_argument("--output-dir", default=None, help="Path to src/content/blog")
    parser.add_argument("--public-dir", default=None, help="Path to public output directory")
    parser.add_argument("--slug-redirects-path", default=None, help="Path to slug_redirects.json")
    parser.add_argument("--vercel-config-path", default=None, help="Path to vercel.json")
    parser.add_argument("--manifest-path", default=None, help="Path to page_manifest.json")
    parser.add_argument("--offers-config", default=None, help="Path to config/offers.yaml")
    parser.add_argument("--as-of-date", default=date.today().isoformat(), help="Pipeline run date (YYYY-MM-DD)")
    parser.add_argument("--max-pages", type=int, default=None, help="Maximum changed pages to generate")
    parser.add_argument("--full", action="store_true", help="Ignore manifest and regenerate all pages")
    parser.add_argument("--strict", action="store_true", help="Enable strict mode for malformed input")
    parser.add_argument("--no-llm", action="store_true", help="Disable LLM analysis generation")
    parser.add_argument("--skip-vercel-sync", action="store_true", help="Do not mutate vercel.json redirects")
    return parser.parse_args()


def build_context(args: argparse.Namespace) -> BuildContext:
    root = resolve_project_root(args.project_root)
    csv_path = Path(args.csv_path).resolve() if args.csv_path else root / "data" / "verified_targets.csv"
    db_path = Path(args.db_path).resolve() if args.db_path else root / "data" / "macro_events.db"
    output_dir = Path(args.output_dir).resolve() if args.output_dir else root / "src" / "content" / "blog"
    public_dir = Path(args.public_dir).resolve() if args.public_dir else root / "public"
    manifest_path = Path(args.manifest_path).resolve() if args.manifest_path else root / "data" / "page_manifest.json"
    offers_path = Path(args.offers_config).resolve() if args.offers_config else root / "config" / "offers.yaml"
    slug_redirects_path = (
        Path(args.slug_redirects_path).resolve()
        if args.slug_redirects_path
        else root / "data" / "slug_redirects.json"
    )
    vercel_config_path = (
        Path(args.vercel_config_path).resolve() if args.vercel_config_path else root / "vercel.json"
    )

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")
    if not offers_path.exists():
        raise FileNotFoundError(f"Offers config not found: {offers_path}")

    offers_config = load_config(offers_path)
    hub_briefs = load_hub_brief_map(root)

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
        hub_briefs=hub_briefs,
        as_of_date=args.as_of_date,
        llm_enabled=llm_enabled,
        llm_api_key=llm_key,
        strict=args.strict,
        full=args.full,
        max_pages=args.max_pages,
        slug_redirects_path=slug_redirects_path,
        vercel_config_path=vercel_config_path,
        skip_vercel_sync=args.skip_vercel_sync,
        build_timestamp=datetime.now(timezone.utc).isoformat(),
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

            row.setdefault("source", "verified_targets.csv")
            row.setdefault("intent", "general")
            row.setdefault("event_label", row.get("event_type", ""))
            row.setdefault("event_slug", str(row.get("event_type", "")).lower())
            row.setdefault("direction_basis", "vs_previous")
            row.setdefault("outcome_status", "pending")
            row.setdefault("freshness_days", "")
            rows.append(row)

    ensure_csv_contract(csv_path, rows)
    rows.sort(key=lambda item: item.get("date", ""), reverse=True)
    return rows


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
              AVG(a.impact_t7_pct) AS impact_t7_pct,
              MAX(eo.direction) AS event_direction,
              MAX(eo.actual_value) AS event_actual,
              MAX(eo.previous_value) AS event_previous,
              MAX(eo.delta_value) AS event_delta,
              MAX(eo.status) AS outcome_status
            FROM asset_impact a
            JOIN macro_events m ON a.event_id = m.event_id
            LEFT JOIN event_outcomes eo
              ON eo.event_type = ?
             AND eo.event_date = m.date
             AND eo.direction_basis = 'vs_previous'
            WHERE a.ticker = ?
              AND m.date <= ?
              AND {event_filter_sql(event_type)}
            GROUP BY m.date
            ORDER BY m.date ASC
            """,
            (event_type.upper(), ticker.upper(), asof_date),
        )
        fetched = cursor.fetchall()
    finally:
        conn.close()

    rows = []
    by_date: Dict[str, Dict[str, Any]] = {}
    for event_date, impact_t1, impact_t7, event_direction, event_actual, event_previous, event_delta, outcome_status in fetched:
        direction = str(event_direction or "unknown").lower()
        item = {
            "event_date": event_date,
            "impact_t1_pct": parse_float(impact_t1),
            "impact_t7_pct": parse_float(impact_t7),
            "event_direction": direction,
            "event_actual": parse_float(event_actual),
            "event_previous": parse_float(event_previous),
            "event_delta": parse_float(event_delta),
            "outcome_status": str(outcome_status or "pending").lower(),
        }
        rows.append(item)
        by_date[event_date] = item

    latest = rows[-1]["event_date"] if rows else asof_date

    return {
        "rows": rows,
        "sample_size": len(rows),
        "latest_event_date": latest,
        "by_date": by_date,
    }


def freshness_threshold(event_type: str) -> int:
    return int(EVENT_FRESHNESS_THRESHOLDS.get(event_type.upper(), 45))


def freshness_status(event_type: str, age_days: int) -> str:
    return "stale" if age_days > freshness_threshold(event_type) else "fresh"


def normalize_db_timestamp(value: object) -> Optional[str]:
    text = str(value or "").strip()
    if not text:
        return None
    parsed: Optional[datetime] = None
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d %H:%M:%S"):
        try:
            parsed = datetime.strptime(text, fmt)
            break
        except ValueError:
            continue
    if parsed is None:
        try:
            parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
        except Exception:
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).isoformat()


def pick_max_timestamp(*values: object) -> Optional[str]:
    candidates: List[datetime] = []
    for value in values:
        normalized = normalize_db_timestamp(value)
        if not normalized:
            continue
        try:
            candidates.append(datetime.fromisoformat(normalized))
        except ValueError:
            continue
    if not candidates:
        return None
    return max(candidates).astimezone(timezone.utc).isoformat()


def fetch_data_last_updated_at(db_path: Path, ticker: str, event_type: str, event_date: str) -> Optional[str]:
    if not db_path.exists():
        return None

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='event_outcomes' LIMIT 1"
        )
        has_event_outcomes = bool(cursor.fetchone())
        if has_event_outcomes:
            cursor.execute(
                f"""
                SELECT
                  MAX(a.updated_at) AS asset_updated_at,
                  MAX(eo.updated_at) AS outcome_updated_at
                FROM asset_impact a
                JOIN macro_events m ON a.event_id = m.event_id
                LEFT JOIN event_outcomes eo
                  ON eo.event_type = ?
                 AND eo.event_date = m.date
                 AND eo.direction_basis = 'vs_previous'
                WHERE a.ticker = ?
                  AND m.date = ?
                  AND {event_filter_sql(event_type)}
                """,
                (event_type.upper(), ticker.upper(), event_date),
            )
        else:
            cursor.execute(
                f"""
                SELECT MAX(a.updated_at) AS asset_updated_at, NULL
                FROM asset_impact a
                JOIN macro_events m ON a.event_id = m.event_id
                WHERE a.ticker = ?
                  AND m.date = ?
                  AND {event_filter_sql(event_type)}
                """,
                (ticker.upper(), event_date),
            )
        row = cursor.fetchone()
    finally:
        conn.close()

    if not row:
        return None
    return pick_max_timestamp(row[0], row[1])


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


def robust_penalty_breakdown(
    *,
    sample_size: int,
    freshness_status: str,
    confidence_level: str,
    outcome_status: str,
) -> Tuple[Dict[str, float], float]:
    if sample_size < 5:
        sample_penalty = 10.0
    elif sample_size < 10:
        sample_penalty = 4.0
    else:
        sample_penalty = 0.0

    freshness_penalty = 6.0 if str(freshness_status).lower() == "stale" else 0.0
    confidence_penalty = 4.0 if str(confidence_level).lower() == "low" else 0.0
    outcome_penalty = 12.0 if str(outcome_status).lower() != "ok" else 0.0

    breakdown = {
        "sample": sample_penalty,
        "freshness": freshness_penalty,
        "confidence": confidence_penalty,
        "outcome": outcome_penalty,
    }
    total = round(sum(breakdown.values()), 2)
    return breakdown, total


def resolve_index_tier(*, sample_size: int, freshness_status_value: str, quality: int) -> str:
    if sample_size >= 20 and freshness_status_value == "fresh" and quality >= 80:
        return "A"
    if sample_size >= 8 and quality >= 60:
        return "B"
    return "C"


def parse_int(value: object, fallback: int = 0) -> int:
    number = parse_float(value)
    if number is None:
        return fallback
    return int(round(number))


def deterministic_title(
    *,
    slug: str,
    asset: str,
    event_type: str,
    event_date: str,
) -> Tuple[str, int, str]:
    templates = TITLE_TEMPLATE_POOLS.get(event_type, ["Historical Performance of {ASSET} After {EVENT} ({DATE})"])
    payload = {"slug": slug, "event_type": event_type}
    digest = stable_hash(payload)
    variant_index = int(digest[:8], 16) % max(len(templates), 1)
    template = templates[variant_index]
    title = template.format(ASSET=asset, EVENT=event_type, DATE=event_date)
    return title, variant_index + 1, f"{event_type.lower()}_{variant_index + 1}"


def sort_date_rank(value: str) -> int:
    text = str(value or "").strip()
    if re.match(r"^\d{4}-\d{2}-\d{2}$", text):
        return int(text.replace("-", ""))
    return 0


def derive_signal_from_row(row: Dict[str, Any]) -> str:
    signal = str(row.get("signal", "")).strip()
    if signal in {"Bullish", "Neutral", "Bearish"}:
        return signal

    raw_score = parse_float(row.get("raw_signal_score"))
    if raw_score is None:
        t1_up = parse_float(row.get("rise_prob_t1"), 50.0)
        t7_up = parse_float(row.get("rise_prob_t7"), 50.0)
        median_t7 = parse_float(row.get("median_t7_pct"), parse_float(row.get("impact_t7_pct"), 0.0))
        _, raw_score = signal_from_probabilities(float(t1_up or 50.0), float(t7_up or 50.0), float(median_t7 or 0.0))

    if float(raw_score) >= 8:
        return "Bullish"
    if float(raw_score) <= -8:
        return "Bearish"
    return "Neutral"


def build_related_lookup(rows: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    by_slug: Dict[str, Dict[str, Any]] = {}
    by_asset_event: Dict[Tuple[str, str], List[Dict[str, Any]]] = {}
    by_asset: Dict[str, List[Dict[str, Any]]] = {}

    for row in rows:
        asset = str(row.get("asset", "")).upper().strip()
        event_date = str(row.get("date", "")).strip()
        event_type = normalize_event_type(str(row.get("event_type", "")), event_date)
        if not asset or event_type not in ALLOWED_EVENT_TYPES:
            continue

        slug = str(row.get("url_slug", "")).strip() or canonical_slug(asset, event_type, event_date)
        if not slug:
            continue

        title = str(row.get("title", "")).strip() or f"{asset} After {event_type} ({event_date}): Historical T+1/T+7 Probability"
        sharpe_t7 = round(float(parse_float(row.get("sharpe_t7"), 0.0) or 0.0), 2)
        median_t7_pct = round(
            float(parse_float(row.get("median_t7_pct"), parse_float(row.get("impact_t7_pct"), 0.0)) or 0.0), 2
        )
        sample_size = max(parse_int(row.get("sample_size"), 0), 0)

        candidate = {
            "slug": slug,
            "asset": asset,
            "event_type": event_type,
            "event_date": event_date,
            "title": title,
            "signal": derive_signal_from_row(row),
            "sharpe_t7": sharpe_t7,
            "median_t7_pct": median_t7_pct,
            "sample_size": sample_size,
        }

        existing = by_slug.get(slug)
        if existing:
            old_key = (-float(existing["sharpe_t7"]), -sort_date_rank(existing["event_date"]), str(existing["slug"]))
            new_key = (-float(candidate["sharpe_t7"]), -sort_date_rank(candidate["event_date"]), str(candidate["slug"]))
            if new_key < old_key:
                by_slug[slug] = candidate
        else:
            by_slug[slug] = candidate

    for candidate in by_slug.values():
        asset = str(candidate["asset"])
        event_type = str(candidate["event_type"])
        by_asset_event.setdefault((asset, event_type), []).append(candidate)
        by_asset.setdefault(asset, []).append(candidate)

    sort_key = lambda item: (
        -float(item.get("sharpe_t7", 0.0)),
        -sort_date_rank(str(item.get("event_date", ""))),
        str(item.get("slug", "")),
    )
    for key in list(by_asset_event.keys()):
        by_asset_event[key] = sorted(by_asset_event[key], key=sort_key)
    for key in list(by_asset.keys()):
        by_asset[key] = sorted(by_asset[key], key=sort_key)

    lookup: Dict[str, List[Dict[str, Any]]] = {}
    for slug, candidate in by_slug.items():
        asset = str(candidate["asset"])
        event_type = str(candidate["event_type"])
        preferred = [item for item in by_asset_event.get((asset, event_type), []) if item["slug"] != slug]
        fallback = [
            item
            for item in by_asset.get(asset, [])
            if item["slug"] != slug and str(item.get("event_type")) != event_type
        ]

        merged: List[Dict[str, Any]] = []
        seen: set[str] = set()
        for item in [*preferred, *fallback]:
            item_slug = str(item.get("slug", ""))
            if not item_slug or item_slug in seen:
                continue
            seen.add(item_slug)
            merged.append(
                {
                    "slug": item_slug,
                    "title": str(item.get("title", "")).strip(),
                    "event_date": str(item.get("event_date", "")).strip(),
                    "event_type": str(item.get("event_type", "")).upper(),
                    "signal": str(item.get("signal", "Neutral")),
                    "sharpe_t7": round(float(parse_float(item.get("sharpe_t7"), 0.0) or 0.0), 2),
                    "median_t7_pct": round(float(parse_float(item.get("median_t7_pct"), 0.0) or 0.0), 2),
                    "sample_size": max(parse_int(item.get("sample_size"), 0), 0),
                }
            )
            if len(merged) >= 3:
                break
        lookup[slug] = merged

    return lookup


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


def generate_llm_analysis(asset: str, event_type: str, event_direction: str, probabilities: Dict[str, Any], context: BuildContext) -> Optional[str]:
    if not context.llm_enabled or requests is None:
        return None

    prompt = f"""Write a concise quantitative analysis in English.
Asset: {asset}
Event: {event_type}
Event Direction (vs previous): {event_direction}
All-history T+1 Up Probability: {probabilities['t1']['up']}%
All-history T+7 Up Probability: {probabilities['t7']['up']}%
Same-direction T+1 Up Probability: {probabilities['conditional']['t1']['up']}%
Same-direction T+7 Up Probability: {probabilities['conditional']['t7']['up']}%
Same-direction T+7 Median Return: {probabilities['conditional']['t7']['median']}%
Same-direction Sample Size: {probabilities['conditional']['sample_size']}

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


def fallback_analysis(asset: str, event_type: str, event_direction: str, probabilities: Dict[str, Any], signal: str) -> str:
    direction_text = event_direction.capitalize()
    return (
        f"For {asset}, historical {event_type} windows show all-history T+1 up probability of "
        f"{probabilities['t1']['up']}% and T+7 up probability of {probabilities['t7']['up']}%. "
        f"When {event_type} printed {direction_text} versus previous, T+1 up probability was "
        f"{probabilities['conditional']['t1']['up']}% and T+7 up probability was {probabilities['conditional']['t7']['up']}% "
        f"across {probabilities['conditional']['sample_size']} matched cases. "
        f"Current classification is {signal}; this remains an educational probability lens, not investment advice."
    )


def body_variant_family_for_slug(slug: str) -> str:
    digest = stable_hash({"slug": slug, "scope": "body_variant"})
    index = int(digest[:8], 16) % max(len(BODY_VARIANT_FAMILIES), 1)
    return BODY_VARIANT_FAMILIES[index]


def format_pct(value: object, signed: bool = False) -> str:
    number = parse_float(value, 0.0) or 0.0
    return f"{number:+.2f}%" if signed else f"{number:.2f}%"


def format_basis_points(value: object) -> str:
    number = parse_float(value, 0.0) or 0.0
    return f"{number * 100:.0f} bps"


def direction_phrase(event_direction: str) -> str:
    mapping = {
        "up": "higher than the previous release",
        "down": "lower than the previous release",
        "flat": "unchanged versus the previous release",
    }
    return mapping.get(str(event_direction).lower(), "mixed versus the previous release")


def narrative_trigger_text(trigger: str) -> str:
    mapping = {
        "significant_outperformance": "the upper end of its historical distribution",
        "significant_underperformance": "the weak tail of its historical distribution",
        "within_historical_norm": "the middle of its historical distribution",
        "low_context": "a low-context sample bucket",
    }
    return mapping.get(trigger, "its historical distribution")


def percentile_band_text(percentile: float) -> str:
    if percentile >= 90:
        return "the top decile of observed windows"
    if percentile >= 75:
        return "the upper quartile of observed windows"
    if percentile <= 10:
        return "the weakest decile of observed windows"
    if percentile <= 25:
        return "the lower quartile of observed windows"
    return "the central band of observed windows"


def brief_snippet(value: object, fallback: str, max_chars: int = 220) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if not text:
        text = fallback
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1].rstrip(" ,;:.") + "..."


def compose_core_body(
    *,
    slug: str,
    asset: str,
    event_label: str,
    event_direction: str,
    event_actual: float,
    event_previous: float,
    event_delta: float,
    probabilities: Dict[str, Any],
    metrics: Dict[str, float],
    signal: str,
    features: Dict[str, Any],
    brief: Dict[str, Any],
) -> str:
    family = body_variant_family_for_slug(slug)
    trigger = str(features.get("narrative_trigger", "low_context"))
    t7_up = probabilities["t7"]["up"]
    t7_down = probabilities["t7"]["down"]
    t7_median = probabilities["t7"]["median"]
    conditional_sample = probabilities["conditional"]["sample_size"]
    conditional_t7_up = probabilities["conditional"]["t7"]["up"]
    conditional_t7_median = probabilities["conditional"]["t7"]["median"]
    z_score = features["z_score_t7"]
    percentile = features["percentile_t7"]
    baseline_mean = features["hub_baseline_mean_t7"]
    baseline_median = features["hub_baseline_median_t7"]
    baseline_std = features["hub_baseline_std_t7"]
    baseline_delta = features["hub_baseline_delta"]
    same_direction_gap = round(conditional_t7_up - t7_up, 2)
    same_direction_median_gap = round(conditional_t7_median - t7_median, 2)
    percentile_band = percentile_band_text(percentile)
    thesis_context = brief_snippet(
        brief.get("thesis"),
        f"{asset} around {event_label} should be handled as a macro response distribution, not a headline-only trade.",
    )
    changed_context = brief_snippet(
        brief.get("what_changed_recently"),
        f"Recent positioning and cross-asset confirmation still matter more than the first reaction bar after {event_label}.",
    )
    failure_modes = str(brief.get("risk_watchouts", "")).strip() or (
        "Liquidity shocks, rate repricing, and cross-asset confirmation failures remain the main reasons this setup can break."
    )
    checklist = brief.get("execution_checklist") if isinstance(brief.get("execution_checklist"), list) else []
    checklist_text = "; ".join(str(item).strip() for item in checklist[:3] if str(item).strip())
    if not checklist_text:
        checklist_text = "wait for confirmation, scale entries, and define invalidation before execution"

    intros = {
        "analyst": "This event should be read as a distribution problem, not a headline-only trade.",
        "distribution": "The useful signal is where this release sits inside the historical range, not the headline in isolation.",
        "risk-first": "The main mistake after macro releases is to treat every surprise as a regime break.",
        "checklist": "Execution quality here comes from context discipline rather than reacting to the first candle.",
    }
    comparison_intros = {
        "analyst": "Against the hub baseline for this asset-event pair, the current print is measurable rather than anecdotal.",
        "distribution": "Relative to the hub baseline, this release can be located with a concrete distance from normal behavior.",
        "risk-first": "The baseline comparison matters because most false positives come from overreacting to ordinary noise.",
        "checklist": "The baseline comparison is what turns this page from observation into a repeatable checklist.",
    }
    distribution_explanations = {
        "analyst": "That keeps the interpretation anchored in the shape of the historical sample rather than the release headline.",
        "distribution": "That framing matters because it separates ordinary event noise from true tail behavior inside the same distribution.",
        "risk-first": "That is the difference between a manageable macro impulse and a tail event that can invalidate prior playbooks.",
        "checklist": "That distinction is what tells an operator whether to slow down, confirm, or stand aside.",
    }
    comparison_explanations = {
        "analyst": "The classification is therefore tied to a measurable gap versus baseline, not to narrative convenience.",
        "distribution": "In other words, the baseline gap decides the narrative, not a cosmetic change in wording.",
        "risk-first": "That distance from baseline is what determines whether this is noise, pressure, or a real outlier worth extra caution.",
        "checklist": "That baseline gap is what turns the page into an action filter instead of a generic macro recap.",
    }
    failure_intros = {
        "analyst": "The main failure mode is misreading a statistically ordinary move as a structural break.",
        "distribution": "The main failure mode is forgetting that distributions absorb a lot of noise before they change shape.",
        "risk-first": "The main failure mode is assuming the first interpretation of the release will survive cross-asset confirmation.",
        "checklist": "The main failure mode is skipping confirmation steps because the headline seems obvious.",
    }
    execution_intros = {
        "analyst": "Use this page as an educational operating lens, not a trading instruction.",
        "distribution": "Use this page as a distribution map, not a shortcut to conviction.",
        "risk-first": "Treat this as an educational risk framework, not investment advice.",
        "checklist": "Treat this page as an execution checklist input, not a buy or sell signal.",
    }

    outcome_paragraph = (
        f"{intros[family]} {asset} around {event_label} is best framed through how the release landed "
        f"{direction_phrase(event_direction)}. The current observation shows actual value {event_actual:.4f} versus "
        f"previous {event_previous:.4f}, a delta of {event_delta:+.4f}. Across the full history, {asset} has a "
        f"T+7 up probability of {t7_up:.2f}% versus {t7_down:.2f}% down, with a median return of {t7_median:.2f}%. "
        f"When only matching the same event direction, the T+7 up probability shifts to {conditional_t7_up:.2f}% "
        f"across {conditional_sample} comparable releases, with a same-direction median of {conditional_t7_median:.2f}%. "
        f"That is the immediate context behind the current {signal.lower()} classification. The standing hub thesis for this "
        f"asset-event pair is: {thesis_context}"
    )

    if trigger == "low_context":
        distribution_paragraph = (
            f"## Distribution Position\n\n"
            f"This page currently falls into a low-context bucket because the valid baseline sample is below the minimum "
            f"needed for a stable distribution read. Z-score is held at {z_score:.2f} and percentile at {percentile:.2f} "
            f"by contract, which means the system is intentionally refusing to overstate confidence. In practical terms, "
            f"that means the observed T+7 move of {metrics['impact_t7_pct']:.2f}% should be treated as descriptive evidence "
            f"rather than a statistically strong signal. In this regime the safer interpretation is to treat the page as a "
            f"research breadcrumb that should be subordinated to the broader {asset} {event_label} hub, not as a self-contained setup."
        )
    elif trigger == "significant_outperformance":
        distribution_paragraph = (
            f"## Distribution Position\n\n"
            f"The current T+7 reaction of {metrics['impact_t7_pct']:.2f}% sits in {narrative_trigger_text(trigger)} for "
            f"{asset} after {event_label}. Its z-score is {z_score:.2f}, meaning the window is more than a standard deviation "
            f"above the mean response, and its percentile rank is {percentile:.2f}, placing it in {percentile_band}. "
            f"{distribution_explanations[family]} This is not just a positive reading; it is a stronger-than-typical response "
            f"relative to the same asset-event history, so the operator should assume reversion risk rises if confirmation from rates, "
            f"the dollar, or index breadth fails to hold."
        )
    elif trigger == "significant_underperformance":
        distribution_paragraph = (
            f"## Distribution Position\n\n"
            f"The current T+7 reaction of {metrics['impact_t7_pct']:.2f}% sits in {narrative_trigger_text(trigger)} for "
            f"{asset} after {event_label}. Its z-score is {z_score:.2f}, which places the move materially below the historical mean, "
            f"and its percentile rank is {percentile:.2f}, leaving it in {percentile_band}. {distribution_explanations[family]} "
            f"That makes the current release a weaker-than-normal outcome rather than routine variance, so downside follow-through and "
            f"false-positive bounce risk both matter more than in a median event window."
        )
    else:
        distribution_paragraph = (
            f"## Distribution Position\n\n"
            f"The current T+7 reaction of {metrics['impact_t7_pct']:.2f}% sits in {narrative_trigger_text(trigger)} for "
            f"{asset} after {event_label}. Its z-score is {z_score:.2f}, which measures distance from the historical mean, "
            f"and its percentile rank is {percentile:.2f}, which shows how often prior releases were weaker than this one. "
            f"That places the observation inside {percentile_band}, not in an obvious tail bucket. {distribution_explanations[family]} "
            f"In practice this means the page is useful for calibration, but it does not justify upgrading a routine macro response "
            f"into a regime-break narrative."
        )

    comparison_paragraph = (
        f"## Comparison vs Hub Baseline\n\n"
        f"{comparison_intros[family]} The hub baseline median T+7 return for {asset} after {event_label} is "
        f"{baseline_median:.2f}%, while the baseline mean is {baseline_mean:.2f}% and the baseline standard deviation is "
        f"{baseline_std:.4f}. The current event is running at {format_pct(baseline_delta, signed=True)} versus the baseline median. "
        f"Same-direction probability is {format_pct(same_direction_gap, signed=True)} versus the all-history T+7 up rate, and the "
        f"same-direction median differs by {format_pct(same_direction_median_gap, signed=True)}. "
        f"{comparison_explanations[family]} This release is classified as {trigger.replace('_', ' ')} rather than handled as a generic macro template. "
        f"If the current move only differed by a few basis points, the narrative would collapse back toward historical norm. "
        f"The current regime context also matters: {changed_context}"
    )

    failure_paragraph = (
        f"## Failure Modes\n\n"
        f"{failure_intros[family]} "
        f"{failure_modes} This matters because the historical distribution is built on end-of-window outcomes, not the first minute of "
        f"price discovery. A release can look constructive initially, then fail once rates, the dollar, and sector breadth reprice in a "
        f"different direction. That is also why low sample environments and mixed reaction functions should be handled as weaker evidence."
    )

    execution_paragraph = (
        f"## Execution Relevance\n\n"
        f"{execution_intros[family]} The practical takeaway is to use the current page as a "
        f"decision filter: read the release, compare it with the hub baseline, then decide whether the event is behaving like a normal "
        f"{event_label} setup or a tail observation. For this asset-event pair, the operational checklist is: {checklist_text}. "
        f"When the page is marked {trigger.replace('_', ' ')}, the right response is not automatically to trade more aggressively; "
        f"it is to decide whether confirmation quality is strong enough to justify action."
    )

    return (
        "## Event Outcome Interpretation\n\n"
        + outcome_paragraph
        + "\n\n"
        + distribution_paragraph
        + "\n\n"
        + comparison_paragraph
        + "\n\n"
        + failure_paragraph
        + "\n\n"
        + execution_paragraph
    )


def build_markdown(
    *,
    slug: str,
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
    raw_signal_score: float,
    robust_score: float,
    title_variant_id: int,
    title_template_key: str,
    penalty_breakdown: Dict[str, float],
    confidence_level: str,
    quality: int,
    sample_size: int,
    freshness_days: int,
    freshness_status_value: str,
    index_tier: str,
    is_recent_90d: bool,
    canonical_target: str,
    canonical_url: str,
    robots_directive: str,
    in_blog_sitemap: bool,
    is_core_page: bool,
    core_window_days: int,
    body_variant_family: str,
    hub_baseline_mean_t7: float,
    hub_baseline_median_t7: float,
    hub_baseline_std_t7: float,
    hub_baseline_delta: float,
    z_score_t7: float,
    percentile_t7: float,
    narrative_trigger: str,
    data_last_updated_at: str,
    metrics: Dict[str, float],
    probabilities: Dict[str, Any],
    related_events: List[Dict[str, Any]],
    analysis: str,
    chart_data: List[Dict[str, Any]],
    event_direction: str,
    event_actual: float,
    event_previous: float,
    event_delta: float,
    direction_basis: str,
    outcome_status: str,
    brief: Dict[str, Any],
) -> str:
    tags = [asset.lower(), event_type.lower(), "event-probability", intent.replace(" ", "-").lower()]

    chart_line = f"chartData: {json.dumps(chart_data)}\n" if chart_data else ""

    outcome_sentence = (
        f"{event_label} Outcome: **{event_direction.upper()}** "
        f"(Actual {event_actual}, Previous {event_previous}, Delta {event_delta:+.4f})"
    )

    return f"""---
title: "{title}"
description: "Historical probability profile for {asset} around {event_type} events (T+1/T+7)."
pubDate: "{publish_date}"
title_variant_id: {title_variant_id}
title_template_key: "{title_template_key}"
event_type: "{event_type}"
event_label: "{event_label}"
event_slug: "{event_slug}"
event_date: "{event_date}"
asof_date: "{asof_date}"
source: "{source}"
offer_key: "{offer_key}"
signal: "{signal}"
raw_signal_score: {raw_signal_score}
robust_score: {robust_score}
penalties:
  sample: {penalty_breakdown['sample']}
  freshness: {penalty_breakdown['freshness']}
  confidence: {penalty_breakdown['confidence']}
  outcome: {penalty_breakdown['outcome']}
confidence_level: "{confidence_level}"
quality_score: {quality}
sample_size: {sample_size}
freshness_days: {freshness_days}
freshness_status: "{freshness_status_value}"
index_tier: "{index_tier}"
is_recent_90d: {str(bool(is_recent_90d)).lower()}
is_core_page: {str(bool(is_core_page)).lower()}
core_window_days: {core_window_days}
body_variant_family: "{body_variant_family}"
hub_baseline_mean_t7: {hub_baseline_mean_t7}
hub_baseline_median_t7: {hub_baseline_median_t7}
hub_baseline_std_t7: {hub_baseline_std_t7}
hub_baseline_delta: {hub_baseline_delta}
z_score_t7: {z_score_t7}
percentile_t7: {percentile_t7}
narrative_trigger: "{narrative_trigger}"
canonical_target: "{canonical_target}"
canonical_url: "{canonical_url}"
robots_directive: "{robots_directive}"
in_blog_sitemap: {str(bool(in_blog_sitemap)).lower()}
data_last_updated_at: "{data_last_updated_at}"
event_direction: "{event_direction}"
event_actual: {event_actual}
event_previous: {event_previous}
event_delta: {event_delta}
direction_basis: "{direction_basis}"
outcome_status: "{outcome_status}"
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
  conditional:
    basis: "event_direction"
    direction: "{event_direction}"
    sample_size: {probabilities['conditional']['sample_size']}
    t1:
      up: {probabilities['conditional']['t1']['up']}
      down: {probabilities['conditional']['t1']['down']}
      median: {probabilities['conditional']['t1']['median']}
      mean: {probabilities['conditional']['t1']['mean']}
      sample: {probabilities['conditional']['t1']['sample']}
    t7:
      up: {probabilities['conditional']['t7']['up']}
      down: {probabilities['conditional']['t7']['down']}
      median: {probabilities['conditional']['t7']['median']}
      mean: {probabilities['conditional']['t7']['mean']}
      sample: {probabilities['conditional']['t7']['sample']}
related_events: {json.dumps(related_events)}
{chart_line}---

## Event Snapshot

- Event: **{event_label}**
- Asset: **{asset}**
- Event date: **{event_date}**
- As-of date (T-1): **{asof_date}**
- Freshness age: **{freshness_days} days**
- Sample size (all-history): **{sample_size}**

## Event Outcome

- {outcome_sentence}
- Direction basis: **{direction_basis}**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | {probabilities['t1']['up']}% | {probabilities['t1']['down']}% | {probabilities['t1']['median']}% | {probabilities['t1']['mean']}% | {probabilities['t1']['sample']} |
| T+7 | {probabilities['t7']['up']}% | {probabilities['t7']['down']}% | {probabilities['t7']['median']}% | {probabilities['t7']['mean']}% | {probabilities['t7']['sample']} |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | {probabilities['conditional']['t1']['up']}% | {probabilities['conditional']['t1']['down']}% | {probabilities['conditional']['t1']['median']}% | {probabilities['conditional']['t1']['mean']}% | {probabilities['conditional']['t1']['sample']} |
| T+7 | {probabilities['conditional']['t7']['up']}% | {probabilities['conditional']['t7']['down']}% | {probabilities['conditional']['t7']['median']}% | {probabilities['conditional']['t7']['mean']}% | {probabilities['conditional']['t7']['sample']} |

{compose_core_body(
    slug=slug,
    asset=asset,
    event_label=event_label,
    event_direction=event_direction,
    event_actual=event_actual,
    event_previous=event_previous,
    event_delta=event_delta,
    probabilities=probabilities,
    metrics=metrics,
    signal=signal,
    features={
        "hub_baseline_mean_t7": hub_baseline_mean_t7,
        "hub_baseline_median_t7": hub_baseline_median_t7,
        "hub_baseline_std_t7": hub_baseline_std_t7,
        "hub_baseline_delta": hub_baseline_delta,
        "z_score_t7": z_score_t7,
        "percentile_t7": percentile_t7,
        "narrative_trigger": narrative_trigger,
    },
    brief=brief,
) if is_core_page else f'''## Historical Distribution Summary

When {event_label} was **{event_direction.upper()}**, {asset} T+1 up probability was **{probabilities['conditional']['t1']['up']}%** (n={probabilities['conditional']['t1']['sample']}).

When {event_label} was **{event_direction.upper()}**, {asset} T+7 up probability was **{probabilities['conditional']['t7']['up']}%** (n={probabilities['conditional']['t7']['sample']}).

Same-direction T+7 median return: **{probabilities['conditional']['t7']['median']}%**.

{analysis}'''}

## Methodology

This page aggregates historical windows for the same event type ({event_label}) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
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


def build_lastmod_metric_signature(probabilities: Dict[str, Any]) -> Dict[str, float]:
    t1 = probabilities.get("t1", {}) if isinstance(probabilities, dict) else {}
    t7 = probabilities.get("t7", {}) if isinstance(probabilities, dict) else {}
    conditional = probabilities.get("conditional", {}) if isinstance(probabilities, dict) else {}
    c1 = conditional.get("t1", {}) if isinstance(conditional, dict) else {}
    c7 = conditional.get("t7", {}) if isinstance(conditional, dict) else {}

    return {
        "all_t1_up": round(float(parse_float(t1.get("up"), 0.0) or 0.0), 2),
        "all_t1_down": round(float(parse_float(t1.get("down"), 0.0) or 0.0), 2),
        "all_t7_up": round(float(parse_float(t7.get("up"), 0.0) or 0.0), 2),
        "all_t7_down": round(float(parse_float(t7.get("down"), 0.0) or 0.0), 2),
        "same_t1_up": round(float(parse_float(c1.get("up"), 0.0) or 0.0), 2),
        "same_t1_down": round(float(parse_float(c1.get("down"), 0.0) or 0.0), 2),
        "same_t7_up": round(float(parse_float(c7.get("up"), 0.0) or 0.0), 2),
        "same_t7_down": round(float(parse_float(c7.get("down"), 0.0) or 0.0), 2),
        "sample_size": float(parse_int(probabilities.get("sample_size"), 0)),
        "conditional_sample_size": float(parse_int(conditional.get("sample_size"), 0)),
    }


def parse_lastmod_metric_signature(value: object) -> Dict[str, float]:
    if isinstance(value, dict):
        payload = value
    elif isinstance(value, str):
        text = value.strip()
        if not text:
            return {}
        try:
            parsed = json.loads(text)
        except Exception:
            return {}
        if not isinstance(parsed, dict):
            return {}
        payload = parsed
    else:
        return {}

    normalized: Dict[str, float] = {}
    for key in [
        "all_t1_up",
        "all_t1_down",
        "all_t7_up",
        "all_t7_down",
        "same_t1_up",
        "same_t1_down",
        "same_t7_up",
        "same_t7_down",
        "sample_size",
        "conditional_sample_size",
    ]:
        parsed_value = parse_float(payload.get(key))
        if parsed_value is not None:
            normalized[key] = round(float(parsed_value), 2)
    return normalized


def lastmod_threshold_decision(
    previous_signature: Dict[str, float],
    current_signature: Dict[str, float],
) -> Tuple[bool, str]:
    if not previous_signature:
        return True, "initial_signature"

    probability_fields = [
        "all_t1_up",
        "all_t1_down",
        "all_t7_up",
        "all_t7_down",
        "same_t1_up",
        "same_t1_down",
        "same_t7_up",
        "same_t7_down",
    ]
    for field in probability_fields:
        old = previous_signature.get(field)
        new = current_signature.get(field)
        if old is None or new is None:
            return True, f"signature_missing_{field}"
        if abs(float(new) - float(old)) > 5.0:
            return True, f"probability_delta_gt_5:{field}"

    sample_fields = ["sample_size", "conditional_sample_size"]
    for field in sample_fields:
        old = previous_signature.get(field, 0.0)
        new = current_signature.get(field, 0.0)
        if float(new) > float(old):
            return True, f"sample_increase:{field}"

    return False, "threshold_not_met"


def write_urlset(path: Path, entries: Sequence[Dict[str, str]]) -> None:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for entry in entries:
        lines.extend(
            [
                "  <url>",
                f"    <loc>{entry['loc']}</loc>",
                f"    <lastmod>{entry['lastmod']}</lastmod>",
                f"    <changefreq>{entry['changefreq']}</changefreq>",
                f"    <priority>{entry['priority']}</priority>",
                "  </url>",
            ]
        )

    lines.append("</urlset>")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_sitemap_index(
    path: Path,
    domain: str,
    files: Sequence[str],
    file_lastmods: Dict[str, str],
    fallback_lastmod: str,
) -> None:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for filename in files:
        lastmod = file_lastmods.get(filename) or fallback_lastmod
        lines.extend(
            [
                "  <sitemap>",
                f"    <loc>{domain}/{filename}</loc>",
                f"    <lastmod>{lastmod}</lastmod>",
                "  </sitemap>",
            ]
        )
    lines.append("</sitemapindex>")
    payload = "\n".join(lines)
    path.write_text(payload, encoding="utf-8")


def parse_yaml_scalar(value: str) -> str:
    text = str(value or "").strip()
    if (text.startswith('"') and text.endswith('"')) or (text.startswith("'") and text.endswith("'")):
        return text[1:-1]
    return text


def parse_hub_briefs_fallback(content: str) -> Dict[str, Dict[str, Any]]:
    payload: Dict[str, Dict[str, Any]] = {}
    current_key: Optional[str] = None
    in_checklist = False

    for raw_line in content.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if not line.startswith(" ") and stripped.endswith(":"):
            key = stripped[:-1].strip()
            if not key:
                continue
            payload[key] = {}
            current_key = key
            in_checklist = False
            continue

        if not current_key or current_key not in payload:
            continue

        if in_checklist and stripped.startswith("- "):
            payload[current_key].setdefault("execution_checklist", [])
            if isinstance(payload[current_key]["execution_checklist"], list):
                payload[current_key]["execution_checklist"].append(parse_yaml_scalar(stripped[2:]))
            continue

        if line.startswith("  ") and ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key == "execution_checklist":
                payload[current_key]["execution_checklist"] = []
                in_checklist = True
            else:
                payload[current_key][key] = parse_yaml_scalar(value)
                in_checklist = False

    return payload


def normalize_hub_status(value: object) -> str:
    status = str(value or "").strip().lower()
    return status if status in {"draft", "approved"} else "draft"


def normalize_hub_indexing(status: str, value: object) -> str:
    indexing = str(value or "").strip().lower()
    if indexing in {"index", "noindex"}:
        return indexing
    return "index" if status == "approved" else "noindex"


def is_hub_content_strong(brief: Dict[str, Any]) -> bool:
    thesis = str(brief.get("thesis", "")).strip()
    changed = str(brief.get("what_changed_recently", "")).strip()
    risk = str(brief.get("risk_watchouts", "")).strip()
    checklist_raw = brief.get("execution_checklist")
    checklist = checklist_raw if isinstance(checklist_raw, list) else []

    if len(thesis) < HUB_MIN_THESIS_LEN:
        return False
    if len(changed) < HUB_MIN_CHANGED_LEN:
        return False
    if len(risk) < HUB_MIN_RISK_LEN:
        return False
    if len(checklist) < HUB_MIN_CHECKLIST_ITEMS:
        return False
    for item in checklist:
        if len(str(item or "").strip()) < HUB_MIN_CHECKLIST_ITEM_LEN:
            return False
    return True


def load_hub_brief_map(project_root: Path) -> Dict[str, Dict[str, Any]]:
    path = project_root / "data" / "hub_briefs.yaml"
    if not path.exists():
        return {}

    raw = path.read_text(encoding="utf-8")
    payload: Any
    if yaml is not None:
        try:
            payload = yaml.safe_load(raw)
        except Exception:
            payload = parse_hub_briefs_fallback(raw)
    else:
        payload = parse_hub_briefs_fallback(raw)

    if not isinstance(payload, dict):
        return {}

    normalized: Dict[str, Dict[str, Any]] = {}
    for asset in HUB_ASSETS:
        for event in HUB_EVENTS:
            key = f"{asset}_{event}"
            brief = payload.get(key)
            normalized[key] = brief if isinstance(brief, dict) else {}
    return normalized


def load_playbook_hubs(project_root: Path, default_date: str) -> List[Dict[str, str]]:
    fallback = [
        {
            "asset": asset,
            "event": event,
            "lastmod": default_date,
            "status": "draft",
            "indexing": "noindex",
            "content_depth_pass": "false",
        }
        for asset in HUB_ASSETS
        for event in HUB_EVENTS
    ]
    path = project_root / "data" / "hub_briefs.yaml"
    if not path.exists():
        return fallback

    raw = path.read_text(encoding="utf-8")
    payload: Any
    if yaml is not None:
        try:
            payload = yaml.safe_load(raw)
        except Exception:
            payload = parse_hub_briefs_fallback(raw)
    else:
        payload = parse_hub_briefs_fallback(raw)

    if not isinstance(payload, dict):
        return fallback

    items: List[Dict[str, str]] = []
    for asset in HUB_ASSETS:
        for event in HUB_EVENTS:
            key = f"{asset}_{event}"
            brief = payload.get(key) if isinstance(payload.get(key), dict) else {}
            reviewed = str(brief.get("reviewed_at", "")).strip() if isinstance(brief, dict) else ""
            reviewed_norm = reviewed if re.match(r"^\d{4}-\d{2}-\d{2}$", reviewed) else default_date
            status = normalize_hub_status(brief.get("status") if isinstance(brief, dict) else None)
            indexing = normalize_hub_indexing(status, brief.get("indexing") if isinstance(brief, dict) else None)
            content_depth_pass = is_hub_content_strong(brief) if isinstance(brief, dict) else False
            items.append(
                {
                    "asset": asset,
                    "event": event,
                    "lastmod": reviewed_norm,
                    "status": status,
                    "indexing": indexing,
                    "content_depth_pass": "true" if content_depth_pass else "false",
                }
            )
    return items


def generate_dynamic_sitemaps(
    public_dir: Path,
    output_dir: Path,
    domain: str,
    manifest: Dict[str, Any],
    build_timestamp: str,
    project_root: Path,
) -> None:
    ensure_dir(public_dir)
    today = (normalize_db_timestamp(build_timestamp) or datetime.now(timezone.utc).isoformat())[:10]
    playbook_hubs = load_playbook_hubs(project_root=project_root, default_date=today)
    indexable_playbook_hubs = [
        item
        for item in playbook_hubs
        if str(item.get("indexing", "")).lower() == "index" and str(item.get("content_depth_pass", "")).lower() == "true"
    ]
    pages_manifest = manifest.get("pages", {}) if isinstance(manifest.get("pages"), dict) else {}
    slugs = sorted(path.stem for path in output_dir.glob("*.md"))
    sitemap_blog_slugs = [
        slug
        for slug in slugs
        if bool((pages_manifest.get(slug) or {}).get("in_blog_sitemap", False))
    ]

    def slug_lastmod(slug: str) -> str:
        page = pages_manifest.get(slug) or {}
        value = (
            str(page.get("sitemap_lastmod", "")).strip()
            or str(page.get("last_content_change_at", "")).strip()
            or str(page.get("data_last_updated_at", "")).strip()
            or str(page.get("last_generated", "")).strip()
            or build_timestamp
        )
        normalized = normalize_db_timestamp(value)
        if normalized:
            return normalized[:10]
        return today

    slug_lastmods: Dict[str, str] = {slug: slug_lastmod(slug) for slug in slugs}

    def max_lastmod(items: Sequence[str]) -> str:
        if not items:
            return today
        return max(slug_lastmods.get(item, today) for item in items)

    assets = sorted({slug.split("-after-")[0] for slug in slugs if "-after-" in slug})
    events = sorted({slug.split("-after-")[1].split("-")[0] for slug in slugs if "-after-" in slug})
    slugs_by_asset: Dict[str, List[str]] = {asset: [] for asset in assets}
    slugs_by_event: Dict[str, List[str]] = {event: [] for event in events}
    for slug in slugs:
        if "-after-" not in slug:
            continue
        asset = slug.split("-after-")[0]
        event = slug.split("-after-")[1].split("-")[0]
        if asset in slugs_by_asset:
            slugs_by_asset[asset].append(slug)
        if event in slugs_by_event:
            slugs_by_event[event].append(slug)

    blog_root_lastmod = max_lastmod(sitemap_blog_slugs or slugs)
    events_root_lastmod = max([max_lastmod(slugs_by_event[event]) for event in events], default=today)
    playbooks_root_lastmod = max((item["lastmod"] for item in indexable_playbook_hubs), default=today)
    home_lastmod = max(blog_root_lastmod, events_root_lastmod, playbooks_root_lastmod)

    core_entries = [
        {"loc": f"{domain}/", "lastmod": home_lastmod, "changefreq": "daily", "priority": "1.0"},
        {"loc": f"{domain}/leaderboard", "lastmod": blog_root_lastmod, "changefreq": "daily", "priority": "0.95"},
        {"loc": f"{domain}/events", "lastmod": events_root_lastmod, "changefreq": "daily", "priority": "0.9"},
        {"loc": f"{domain}/playbooks", "lastmod": playbooks_root_lastmod, "changefreq": "daily", "priority": "0.88"},
        {"loc": f"{domain}/blog", "lastmod": blog_root_lastmod, "changefreq": "daily", "priority": "0.85"},
        {"loc": f"{domain}/about", "lastmod": today, "changefreq": "weekly", "priority": "0.82"},
    ]
    write_urlset(public_dir / "sitemap-core.xml", core_entries)

    asset_entries = [
        {
            "loc": f"{domain}/tags/{asset}",
            "lastmod": max_lastmod(slugs_by_asset.get(asset, [])),
            "changefreq": "daily",
            "priority": "0.8",
        }
        for asset in assets
    ]
    write_urlset(public_dir / "sitemap-assets.xml", asset_entries)

    event_entries = [
        {
            "loc": f"{domain}/events/{event}",
            "lastmod": max_lastmod(slugs_by_event.get(event, [])),
            "changefreq": "daily",
            "priority": "0.8",
        }
        for event in events
    ]
    write_urlset(public_dir / "sitemap-events.xml", event_entries)

    playbook_entries = [
        {
            "loc": f"{domain}/playbooks/{item['asset'].lower()}/{item['event'].lower()}",
            "lastmod": item["lastmod"],
            "changefreq": "weekly",
            "priority": "0.78",
        }
        for item in indexable_playbook_hubs
    ]
    write_urlset(public_dir / "sitemap-playbooks.xml", playbook_entries)

    chunk_size = 1000
    blog_files: List[str] = []
    file_lastmods: Dict[str, str] = {}
    for idx in range(0, len(sitemap_blog_slugs), chunk_size):
        chunk = sitemap_blog_slugs[idx : idx + chunk_size]
        file_index = idx // chunk_size + 1
        filename = f"sitemap-blog-{file_index}.xml"
        blog_files.append(filename)
        entries = [
            {
                "loc": f"{domain}/blog/{slug}",
                "lastmod": slug_lastmod(slug),
                "changefreq": "weekly",
                "priority": "0.7",
            }
            for slug in chunk
        ]
        write_urlset(public_dir / filename, entries)
        file_lastmods[filename] = max([entry["lastmod"] for entry in entries], default=today)

    file_lastmods["sitemap-core.xml"] = max([entry["lastmod"] for entry in core_entries], default=today)
    file_lastmods["sitemap-assets.xml"] = max([entry["lastmod"] for entry in asset_entries], default=today)
    file_lastmods["sitemap-events.xml"] = max([entry["lastmod"] for entry in event_entries], default=today)
    file_lastmods["sitemap-playbooks.xml"] = max([entry["lastmod"] for entry in playbook_entries], default=today)

    index_files = ["sitemap-core.xml", "sitemap-assets.xml", "sitemap-events.xml", "sitemap-playbooks.xml", *blog_files]
    write_sitemap_index(public_dir / "sitemap-index.xml", domain, index_files, file_lastmods, today)
    write_sitemap_index(public_dir / "sitemap.xml", domain, index_files, file_lastmods, today)

    robots = "\n".join(
        [
            "User-agent: *",
            "Allow: /",
            "",
            # Keep /sitemap.xml as primary entry for Search Console compatibility,
            # and keep /sitemap-index.xml as an explicit secondary index endpoint.
            f"Sitemap: {domain}/sitemap.xml",
            f"Sitemap: {domain}/sitemap-index.xml",
            "",
        ]
    )
    (public_dir / "robots.txt").write_text(robots, encoding="utf-8")


def write_slug_redirects(path: Path, slug_redirects: Dict[str, str]) -> None:
    ensure_dir(path.parent)
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
    ensure_dir(vercel_config_path.parent)
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


def process_row(
    row: Dict[str, Any],
    context: BuildContext,
    manifest: Dict[str, Any],
    related_lookup: Dict[str, List[Dict[str, Any]]],
) -> Dict[str, Any]:
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
    intent = str(row.get("intent", "general")).strip() or "general"

    asof_cutoff = cutoff_date(context.as_of_date)
    try:
        freshness_days = max(
            (
                datetime.strptime(asof_cutoff, "%Y-%m-%d").date()
                - datetime.strptime(event_date, "%Y-%m-%d").date()
            ).days,
            0,
        )
    except ValueError:
        freshness_days = 0

    freshness_status_value = freshness_status(event_type, freshness_days)

    summary = fetch_event_distribution(
        db_path=context.db_path,
        ticker=asset,
        event_type=event_type,
        asof_date=asof_cutoff,
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

    event_direction = str(row.get("event_direction") or current_event.get("event_direction") or "unknown").lower()
    event_actual = parse_float(row.get("event_actual"), parse_float(current_event.get("event_actual")))
    event_previous = parse_float(row.get("event_previous"), parse_float(current_event.get("event_previous")))
    event_delta = parse_float(row.get("event_delta"), parse_float(current_event.get("event_delta")))
    direction_basis = str(row.get("direction_basis") or "vs_previous").lower()
    outcome_status = str(row.get("outcome_status") or current_event.get("outcome_status") or "pending").lower()

    if context.strict:
        if event_direction not in {"up", "down", "flat"}:
            raise ValueError(f"Invalid event_direction for {asset} {event_type} {event_date}: {event_direction}")
        if direction_basis != "vs_previous":
            raise ValueError(f"Invalid direction_basis for {asset} {event_type} {event_date}: {direction_basis}")
        if outcome_status != "ok":
            raise ValueError(f"Outcome pending for {asset} {event_type} {event_date}")
        for val_name, val in [
            ("event_actual", event_actual),
            ("event_previous", event_previous),
            ("event_delta", event_delta),
        ]:
            if val is None:
                raise ValueError(f"Missing {val_name} for {asset} {event_type} {event_date}")

    if event_direction not in {"up", "down", "flat"}:
        event_direction = "flat"
    if direction_basis != "vs_previous":
        direction_basis = "vs_previous"
    if outcome_status not in {"ok", "pending"}:
        outcome_status = "pending"

    t1_values = [float(r["impact_t1_pct"]) for r in summary["rows"] if r["impact_t1_pct"] is not None]
    t7_values = [float(r["impact_t7_pct"]) for r in summary["rows"] if r["impact_t7_pct"] is not None]

    conditional_t1_values = [
        float(r["impact_t1_pct"])
        for r in summary["rows"]
        if r["impact_t1_pct"] is not None and str(r.get("event_direction", "")).lower() == event_direction
    ]
    conditional_t7_values = [
        float(r["impact_t7_pct"])
        for r in summary["rows"]
        if r["impact_t7_pct"] is not None and str(r.get("event_direction", "")).lower() == event_direction
    ]

    t1_window = probability_window(t1_values)
    t7_window = probability_window(t7_values)
    conditional_t1_window = probability_window(conditional_t1_values)
    conditional_t7_window = probability_window(conditional_t7_values)

    probabilities = {
        "sample_size": int(summary.get("sample_size", 0)),
        "t1": t1_window,
        "t7": t7_window,
        "conditional": {
            "basis": "event_direction",
            "direction": event_direction,
            "sample_size": int(
                min(
                    conditional_t1_window.get("sample", 0),
                    conditional_t7_window.get("sample", 0),
                )
            ),
            "t1": conditional_t1_window,
            "t7": conditional_t7_window,
        },
    }

    signal, raw_signal_score = signal_from_probabilities(t1_window["up"], t7_window["up"], t7_window["median"])
    confidence_level = "normal" if probabilities["sample_size"] >= 5 else "low"
    penalty_breakdown, total_penalty = robust_penalty_breakdown(
        sample_size=probabilities["sample_size"],
        freshness_status=freshness_status_value,
        confidence_level=confidence_level,
        outcome_status=outcome_status,
    )
    robust_score = round(raw_signal_score - total_penalty, 2)

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

    quality = quality_score(raw_t1, raw_t7, raw_vol, probabilities["conditional"]["sample_size"])
    offer_key = to_offer_key(asset, context.offers_config)
    index_tier = resolve_index_tier(
        sample_size=probabilities["sample_size"],
        freshness_status_value=freshness_status_value,
        quality=quality,
    )
    is_recent_90d = freshness_days <= 90
    default_domain = str(context.offers_config.get("default_domain", "quantmacro.vercel.app")).strip() or "quantmacro.vercel.app"
    site_domain = default_domain if default_domain.startswith("http") else f"https://{default_domain}"
    canonical_self_url = f"{site_domain}/blog/{slug}"
    canonical_hub_url = f"{site_domain}/playbooks/{asset.lower()}/{event_type.lower()}"
    if index_tier == "C":
        canonical_target = "none"
        canonical_url = ""
        robots_directive = "noindex,follow"
        in_blog_sitemap = False
    elif is_recent_90d:
        canonical_target = "self"
        canonical_url = canonical_self_url
        robots_directive = "index,follow"
        in_blog_sitemap = True
    else:
        canonical_target = "hub"
        canonical_url = canonical_hub_url
        robots_directive = "index,follow"
        in_blog_sitemap = False
    is_core_page = is_core_page_for_window(
        event_date=event_date,
        as_of_date=context.as_of_date,
        canonical_target=canonical_target,
        robots_directive=robots_directive,
        in_blog_sitemap=in_blog_sitemap,
        window_days=CORE_WINDOW_DAYS,
    )
    body_variant_family = body_variant_family_for_slug(slug)
    baseline_t7_values = [r.get("impact_t7_pct") for r in summary["rows"] if r.get("impact_t7_pct") is not None]
    statistical_features = compute_statistical_features(metrics["impact_t7_pct"], baseline_t7_values, epsilon=FEATURE_EPSILON)
    if context.strict:
        for field_name, field_value in [
            ("hub_baseline_mean_t7", statistical_features.baseline_mean_t7),
            ("hub_baseline_median_t7", statistical_features.baseline_median_t7),
            ("hub_baseline_std_t7", statistical_features.baseline_std_t7),
            ("hub_baseline_delta", statistical_features.hub_baseline_delta),
            ("z_score_t7", statistical_features.z_score_t7),
            ("percentile_t7", statistical_features.percentile_t7),
        ]:
            if not isinstance(field_value, float) or not math.isfinite(field_value):
                raise ValueError(f"Non-finite statistical feature for {slug}: {field_name}={field_value}")
    brief = context.hub_briefs.get(f"{asset}_{event_type}", {})

    title, title_variant_id, title_template_key = deterministic_title(
        slug=slug,
        asset=asset,
        event_type=event_type,
        event_date=event_date,
    )
    event_label = event_type
    event_slug = event_type.lower()
    asof_date = asof_cutoff

    if is_core_page:
        analysis = ""
    else:
        llm_text = generate_llm_analysis(asset, event_type, event_direction, probabilities, context)
        analysis = llm_text or fallback_analysis(asset, event_type, event_direction, probabilities, signal)

    previous = manifest.get("pages", {}).get(slug, {})
    related_events = related_lookup.get(slug, [])
    chart_data = fetch_chart_data(asset, event_date)
    data_last_updated_at = (
        fetch_data_last_updated_at(context.db_path, asset, event_type, event_date)
        or str(previous.get("data_last_updated_at", "")).strip()
    )
    if not data_last_updated_at:
        data_last_updated_at = context.build_timestamp
    normalized_data_last_updated_at = normalize_db_timestamp(data_last_updated_at) or context.build_timestamp

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
        "related_events": related_events,
        "signal": signal,
        "raw_signal_score": raw_signal_score,
        "robust_score": robust_score,
        "title_variant_id": title_variant_id,
        "title_template_key": title_template_key,
        "penalty_breakdown": penalty_breakdown,
        "confidence_level": confidence_level,
        "quality": quality,
        "offer_key": offer_key,
        "index_tier": index_tier,
        "is_recent_90d": is_recent_90d,
        "is_core_page": is_core_page,
        "core_window_days": CORE_WINDOW_DAYS,
        "body_variant_family": body_variant_family,
        "hub_baseline_mean_t7": statistical_features.baseline_mean_t7,
        "hub_baseline_median_t7": statistical_features.baseline_median_t7,
        "hub_baseline_std_t7": statistical_features.baseline_std_t7,
        "hub_baseline_delta": statistical_features.hub_baseline_delta,
        "z_score_t7": statistical_features.z_score_t7,
        "percentile_t7": statistical_features.percentile_t7,
        "narrative_trigger": statistical_features.narrative_trigger,
        "canonical_target": canonical_target,
        "canonical_url": canonical_url,
        "robots_directive": robots_directive,
        "in_blog_sitemap": in_blog_sitemap,
        "asof_date": asof_date,
        "event_direction": event_direction,
        "event_actual": event_actual,
        "event_previous": event_previous,
        "event_delta": event_delta,
        "direction_basis": direction_basis,
        "freshness_days": freshness_days,
        "freshness_status": freshness_status_value,
        "data_last_updated_at": normalized_data_last_updated_at,
    }
    fingerprint = row_fingerprint(fingerprint_payload)

    target_file = context.output_dir / f"{slug}.md"

    need_generate = context.full or previous.get("hash") != fingerprint or (not target_file.exists())

    if need_generate:
        content = build_markdown(
            slug=slug,
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
            raw_signal_score=raw_signal_score,
            robust_score=robust_score,
            title_variant_id=title_variant_id,
            title_template_key=title_template_key,
            penalty_breakdown=penalty_breakdown,
            confidence_level=confidence_level,
            quality=quality,
            sample_size=probabilities["sample_size"],
            freshness_days=freshness_days,
            freshness_status_value=freshness_status_value,
            index_tier=index_tier,
            is_recent_90d=is_recent_90d,
            is_core_page=is_core_page,
            core_window_days=CORE_WINDOW_DAYS,
            body_variant_family=body_variant_family,
            hub_baseline_mean_t7=statistical_features.baseline_mean_t7,
            hub_baseline_median_t7=statistical_features.baseline_median_t7,
            hub_baseline_std_t7=statistical_features.baseline_std_t7,
            hub_baseline_delta=statistical_features.hub_baseline_delta,
            z_score_t7=statistical_features.z_score_t7,
            percentile_t7=statistical_features.percentile_t7,
            narrative_trigger=statistical_features.narrative_trigger,
            canonical_target=canonical_target,
            canonical_url=canonical_url,
            robots_directive=robots_directive,
            in_blog_sitemap=in_blog_sitemap,
            data_last_updated_at=normalized_data_last_updated_at,
            metrics=metrics,
            probabilities=probabilities,
            related_events=related_events,
            analysis=analysis,
            chart_data=chart_data,
            event_direction=event_direction,
            event_actual=float(event_actual or 0.0),
            event_previous=float(event_previous or 0.0),
            event_delta=float(event_delta or 0.0),
            direction_basis=direction_basis,
            outcome_status=outcome_status,
            brief=brief if isinstance(brief, dict) else {},
        )

        ensure_dir(context.output_dir)
        target_file.write_text(content, encoding="utf-8")

    now_iso = datetime.now(timezone.utc).isoformat()
    previous_last_change = previous.get("last_content_change_at")
    if not previous_last_change:
        previous_last_change = previous.get("created_at") or previous.get("last_generated")
    last_content_change_at = now_iso if need_generate else (str(previous_last_change) if previous_last_change else context.build_timestamp)
    created_at = str(previous.get("created_at", "")).strip() or now_iso
    current_metric_signature = build_lastmod_metric_signature(probabilities)
    previous_metric_signature = parse_lastmod_metric_signature(previous.get("lastmod_metric_signature"))
    should_update_lastmod, lastmod_decision_reason = lastmod_threshold_decision(
        previous_signature=previous_metric_signature,
        current_signature=current_metric_signature,
    )
    previous_sitemap_lastmod = normalize_db_timestamp(previous.get("sitemap_lastmod"))
    if should_update_lastmod or not previous_sitemap_lastmod:
        sitemap_lastmod = (
            pick_max_timestamp(last_content_change_at, normalized_data_last_updated_at, context.build_timestamp)
            or context.build_timestamp
        )
    else:
        sitemap_lastmod = previous_sitemap_lastmod

    manifest.setdefault("pages", {})[slug] = {
        "hash": fingerprint,
        "source_event": event_type,
        "event_date": event_date,
        "last_generated": now_iso,
        "last_content_change_at": last_content_change_at,
        "data_last_updated_at": normalized_data_last_updated_at,
        "sitemap_lastmod": sitemap_lastmod,
        "lastmod_metric_signature": current_metric_signature,
        "lastmod_decision_reason": lastmod_decision_reason,
        "freshness_status": freshness_status_value,
        "index_tier": index_tier,
        "is_recent_90d": is_recent_90d,
        "is_core_page": is_core_page,
        "core_window_days": CORE_WINDOW_DAYS,
        "body_variant_family": body_variant_family,
        "hub_baseline_mean_t7": statistical_features.baseline_mean_t7,
        "hub_baseline_median_t7": statistical_features.baseline_median_t7,
        "hub_baseline_std_t7": statistical_features.baseline_std_t7,
        "hub_baseline_delta": statistical_features.hub_baseline_delta,
        "z_score_t7": statistical_features.z_score_t7,
        "percentile_t7": statistical_features.percentile_t7,
        "narrative_trigger": statistical_features.narrative_trigger,
        "canonical_target": canonical_target,
        "canonical_url": canonical_url,
        "robots_directive": robots_directive,
        "in_blog_sitemap": in_blog_sitemap,
        "created_at": created_at,
        "quality_score": quality,
        "offer_key": offer_key,
        "signal": signal,
        "signal_score": raw_signal_score,
        "raw_signal_score": raw_signal_score,
        "robust_score": robust_score,
        "title_variant_id": title_variant_id,
        "title_template_key": title_template_key,
        "penalty_breakdown": penalty_breakdown,
        "sample_size": probabilities["sample_size"],
        "related_count": len(related_events),
        "asof_date": asof_date,
        "event_direction": event_direction,
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
    row["conditional_sample_size"] = str(probabilities["conditional"]["sample_size"])
    row["asof_date"] = asof_date
    row["freshness_days"] = str(freshness_days)
    row["signal"] = signal
    row["raw_signal_score"] = str(raw_signal_score)
    row["robust_score"] = str(robust_score)
    row["title_variant_id"] = str(title_variant_id)
    row["title_template_key"] = title_template_key
    row["index_tier"] = index_tier
    row["is_recent_90d"] = "true" if is_recent_90d else "false"
    row["is_core_page"] = "true" if is_core_page else "false"
    row["core_window_days"] = str(CORE_WINDOW_DAYS)
    row["body_variant_family"] = body_variant_family
    row["hub_baseline_mean_t7"] = str(statistical_features.baseline_mean_t7)
    row["hub_baseline_median_t7"] = str(statistical_features.baseline_median_t7)
    row["hub_baseline_std_t7"] = str(statistical_features.baseline_std_t7)
    row["hub_baseline_delta"] = str(statistical_features.hub_baseline_delta)
    row["z_score_t7"] = str(statistical_features.z_score_t7)
    row["percentile_t7"] = str(statistical_features.percentile_t7)
    row["narrative_trigger"] = statistical_features.narrative_trigger
    row["canonical_target"] = canonical_target
    row["canonical_url"] = canonical_url
    row["robots_directive"] = robots_directive
    row["in_blog_sitemap"] = "true" if in_blog_sitemap else "false"
    row["confidence_level"] = confidence_level
    row["event_direction"] = event_direction
    row["event_actual"] = str(event_actual if event_actual is not None else "")
    row["event_previous"] = str(event_previous if event_previous is not None else "")
    row["event_delta"] = str(event_delta if event_delta is not None else "")
    row["direction_basis"] = direction_basis
    row["outcome_status"] = outcome_status

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

    related_lookup = build_related_lookup(targets)

    print(f"📄 Total targets: {len(targets)}")
    print(f"🧩 Candidate targets: {len(changed_targets)}")

    generated = 0
    skipped = 0
    errors = 0

    for row in changed_targets:
        try:
            result = process_row(row, context, manifest, related_lookup)
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

    for old_slug, new_slug in list(manifest.get("slug_redirects", {}).items()):
        old_file = context.output_dir / f"{old_slug}.md"
        if old_file.exists() and old_slug != new_slug:
            old_file.unlink()

    page_entries = manifest.get("pages", {}) if isinstance(manifest.get("pages"), dict) else {}
    content_lastmods = [
        str(page.get("last_content_change_at", "")).strip()[:10]
        for page in page_entries.values()
        if isinstance(page, dict) and str(page.get("last_content_change_at", "")).strip()
    ]
    unique_content_dates = len(set(content_lastmods))
    if unique_content_dates > 1:
        manifest["allow_uniform_lastmod_once"] = False
    elif generated > 0 and unique_content_dates <= 1:
        manifest["allow_uniform_lastmod_once"] = True
    elif unique_content_dates <= 1 and manifest.get("allow_uniform_lastmod_once") is None:
        manifest["allow_uniform_lastmod_once"] = True

    generate_dynamic_sitemaps(
        public_dir=context.public_dir,
        output_dir=context.output_dir,
        domain=f"https://{context.offers_config.get('default_domain', 'quantmacro.vercel.app')}",
        manifest=manifest,
        build_timestamp=context.build_timestamp,
        project_root=context.project_root,
    )

    write_slug_redirects(context.slug_redirects_path, manifest.get("slug_redirects", {}))
    if not context.skip_vercel_sync:
        sync_vercel_redirects(context.vercel_config_path, manifest.get("slug_redirects", {}))
    save_manifest(context.manifest_path, manifest)
    write_targets_csv(context.csv_path, targets)

    print(f"✅ Generated: {generated}, Skipped: {skipped}, Errors: {errors}")
    if errors > 0 and context.strict:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
