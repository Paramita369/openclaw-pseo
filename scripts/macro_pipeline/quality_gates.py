#!/usr/bin/env python3
"""Quality gates for generated blog content, matrix completeness, and sitemap integrity."""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sqlite3
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

from pipeline_utils import ALLOWED_EVENT_TYPES, PRIMARY_ASSETS, cutoff_date, event_filter_sql, resolve_project_root
from content_features import (
    CORE_WINDOW_DAYS,
    FEATURE_EPSILON,
    compute_statistical_features,
    is_core_page_for_window,
    narrative_direction_band,
    narrative_rank_band,
    resolve_narrative_trigger,
)

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None

REQUIRED_FRONTMATTER_KEYS = [
    "title_variant_id",
    "title_template_key",
    "event_type",
    "event_label",
    "event_slug",
    "event_date",
    "asof_date",
    "source",
    "offer_key",
    "signal",
    "confidence_level",
    "quality_score",
    "sample_size",
    "freshness_days",
    "freshness_status",
    "index_tier",
    "is_recent_90d",
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
    "narrative_rank_band",
    "narrative_direction_band",
    "canonical_target",
    "canonical_url",
    "robots_directive",
    "in_blog_sitemap",
    "raw_signal_score",
    "robust_score",
    "penalties",
    "metrics",
    "probabilities",
    "event_direction",
    "event_actual",
    "event_previous",
    "event_delta",
    "direction_basis",
    "outcome_status",
]

EXPECTED_CSV_COLUMNS = {
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
    "canonical_target",
    "canonical_url",
    "robots_directive",
    "in_blog_sitemap",
    "event_direction",
    "event_actual",
    "event_previous",
    "event_delta",
    "direction_basis",
    "outcome_status",
}

EMBEDDED_AFFILIATE_PATTERN = re.compile(
    r"(binance\.com/referral|ibkr\.com/referral|invest\.futuhk\.com/invite-centre_share)",
    flags=re.IGNORECASE,
)

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

EXPECTED_ROBUST_PENALTIES = {
    "freshness_stale": 6.0,
    "freshness_fresh": 0.0,
    "confidence_low": 4.0,
    "confidence_normal": 0.0,
    "outcome_ok": 0.0,
    "outcome_pending": 12.0,
}


def hub_content_depth_passes(item: object) -> bool:
    if not isinstance(item, dict):
        return False
    thesis = str(item.get("thesis", "")).strip()
    changed = str(item.get("what_changed_recently", "")).strip()
    risk = str(item.get("risk_watchouts", "")).strip()
    checklist = item.get("execution_checklist")
    if len(thesis) < HUB_MIN_THESIS_LEN:
        return False
    if len(changed) < HUB_MIN_CHANGED_LEN:
        return False
    if len(risk) < HUB_MIN_RISK_LEN:
        return False
    if not isinstance(checklist, list) or len(checklist) < HUB_MIN_CHECKLIST_ITEMS:
        return False
    for value in checklist:
        if len(str(value or "").strip()) < HUB_MIN_CHECKLIST_ITEM_LEN:
            return False
    return True


def load_hub_briefs_payload(path: Path) -> object:
    raw_content = path.read_text(encoding="utf-8")
    if yaml is not None:
        try:
            return yaml.safe_load(raw_content)
        except Exception:
            return parse_hub_briefs_fallback(raw_content)
    return parse_hub_briefs_fallback(raw_content)


def table_exists(conn: sqlite3.Connection, table_name: str) -> bool:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name = ? LIMIT 1",
        (table_name,),
    )
    return cursor.fetchone() is not None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run quality gates")
    parser.add_argument("--project-root", default=None, help="Repository root")
    parser.add_argument("--content-dir", default=None, help="Content directory")
    parser.add_argument("--manifest-path", default=None, help="Manifest path override")
    parser.add_argument("--public-dir", default=None, help="Public directory override")
    parser.add_argument("--slug-redirects-path", default=None, help="slug_redirects.json override")
    parser.add_argument("--vercel-config-path", default=None, help="vercel.json override")
    parser.add_argument("--offers-path", default=None, help="offers.json override")
    parser.add_argument("--csv-path", default=None, help="verified_targets.csv override")
    parser.add_argument("--db-path", default=None, help="macro_events.db override")
    parser.add_argument("--index-path", default=None, help="index.astro override")
    parser.add_argument("--snapshot-path", default=None, help="daily_snapshot.json override")
    parser.add_argument("--strict", action="store_true", help="Fail on any violations")
    parser.add_argument("--report", default=None, help="Output report path")
    parser.add_argument("--as-of-date", default=date.today().isoformat(), help="Run date (YYYY-MM-DD)")
    return parser.parse_args()


def parse_scalar(value: str) -> object:
    text = value.strip()
    if text == "":
        return ""
    if text[0] in {'"', "'"} and text[-1] == text[0]:
        return text[1:-1]
    if text.startswith("[") or text.startswith("{"):
        try:
            return json.loads(text)
        except Exception:
            return text
    lowered = text.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    try:
        if "." in text:
            return float(text)
        return int(text)
    except Exception:
        return text


def parse_frontmatter_fallback(frontmatter_text: str) -> Dict[str, object]:
    root: Dict[str, object] = {}
    stack: List[Tuple[int, Dict[str, object]]] = [(-1, root)]

    for raw in frontmatter_text.splitlines():
        if not raw.strip():
            continue
        if raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        stripped = raw.strip()
        if ":" not in stripped:
            continue

        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()

        while len(stack) > 1 and indent <= stack[-1][0]:
            stack.pop()
        current = stack[-1][1]

        if value == "":
            nested: Dict[str, object] = {}
            current[key] = nested
            stack.append((indent, nested))
            continue

        current[key] = parse_scalar(value)

    return root


def extract_frontmatter(content: str) -> Dict[str, object]:
    match = re.match(r"^---\n(.*?)\n---\n", content, flags=re.DOTALL)
    if not match:
        return {}

    frontmatter_text = match.group(1)
    if yaml is not None:
        try:
            loaded = yaml.safe_load(frontmatter_text)
            if isinstance(loaded, dict):
                return loaded
        except Exception:
            pass

    fallback = parse_frontmatter_fallback(frontmatter_text)
    return fallback if isinstance(fallback, dict) else {}


def extract_markdown_body(content: str) -> str:
    match = re.match(r"^---\n.*?\n---\n", content, flags=re.DOTALL)
    if not match:
        return content
    return content[match.end():]


def compute_core_page_flag(frontmatter: Dict[str, object], as_of_date: str) -> bool:
    return is_core_page_for_window(
        event_date=str(frontmatter.get("event_date", "")),
        as_of_date=as_of_date,
        canonical_target=str(frontmatter.get("canonical_target", "")).lower(),
        robots_directive=str(frontmatter.get("robots_directive", "")).lower(),
        in_blog_sitemap=bool(frontmatter.get("in_blog_sitemap")),
        window_days=CORE_WINDOW_DAYS,
    )


def extract_section_text(body: str, heading: str) -> str:
    match = re.search(
        rf"{re.escape(heading)}\n\n(.+?)(?=\n## |\Z)",
        body,
        flags=re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def first_sentence(text: str) -> str:
    match = re.search(r"(.+?)(?:[.!?])(?:\s|$)", text.strip(), flags=re.DOTALL)
    return match.group(1).strip() if match else text.strip()


def load_core_page_entries(content_dir: Path, as_of_date: str) -> List[Tuple[str, Dict[str, object], str]]:
    entries: List[Tuple[str, Dict[str, object], str]] = []
    for path in sorted(content_dir.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        fm = extract_frontmatter(content)
        if not compute_core_page_flag(fm, as_of_date):
            continue
        body = extract_markdown_body(content)
        body_before_methodology = body.split("## Methodology", 1)[0]
        entries.append((path.stem, fm, body_before_methodology))
    return entries


def is_finite_number(value: object) -> bool:
    try:
        number = float(value)
        return math.isfinite(number)
    except Exception:
        return False


def to_float(value: object) -> float | None:
    try:
        number = float(value)
        if not math.isfinite(number):
            return None
        return number
    except Exception:
        return None


def expected_sample_penalty(sample_size: float) -> float:
    if sample_size < 5:
        return 10.0
    if sample_size < 10:
        return 4.0
    return 0.0


def validate_probability_window(window: object, prefix: str) -> List[str]:
    if not isinstance(window, dict):
        return [f"missing_{prefix}_window"]

    violations: List[str] = []
    for field in ["up", "down", "median", "mean", "sample"]:
        if field not in window:
            violations.append(f"missing_{prefix}_{field}")

    up = window.get("up")
    down = window.get("down")
    if not is_finite_number(up) or not is_finite_number(down):
        violations.append(f"non_numeric_{prefix}_up_down")
    else:
        total = float(up) + float(down)
        if abs(total - 100.0) > 0.01:
            violations.append(f"probability_sum_not_100_{prefix}")

    for field in ["median", "mean", "sample"]:
        if field in window and not is_finite_number(window.get(field)):
            violations.append(f"non_numeric_{prefix}_{field}")

    return violations


def validate_probability_block(block: object) -> Tuple[bool, List[str]]:
    if not isinstance(block, dict):
        return False, ["invalid_probabilities_object"]

    violations: List[str] = []
    sample_size = block.get("sample_size")
    if not isinstance(sample_size, int) or sample_size < 0:
        violations.append("invalid_probabilities_sample_size")

    violations.extend(validate_probability_window(block.get("t1"), "probabilities_t1"))
    violations.extend(validate_probability_window(block.get("t7"), "probabilities_t7"))

    conditional = block.get("conditional")
    if not isinstance(conditional, dict):
        violations.append("missing_probabilities_conditional")
    else:
        direction = str(conditional.get("direction", "")).lower()
        if direction not in {"up", "down", "flat"}:
            violations.append("invalid_conditional_direction")
        basis = str(conditional.get("basis", "")).lower()
        if basis != "event_direction":
            violations.append("invalid_conditional_basis")
        conditional_size = conditional.get("sample_size")
        if not isinstance(conditional_size, int) or conditional_size < 0:
            violations.append("invalid_conditional_sample_size")
        violations.extend(validate_probability_window(conditional.get("t1"), "conditional_t1"))
        violations.extend(validate_probability_window(conditional.get("t7"), "conditional_t7"))

    return len(violations) == 0, sorted(set(violations))


def scan_file(path: Path) -> List[str]:
    content = path.read_text(encoding="utf-8")
    violations: List[str] = []

    lowered = content.lower()
    if "nan%" in lowered or " nan" in lowered:
        violations.append("contains_nan")
    if "|--------|-------||" in content:
        violations.append("broken_markdown_table")
    if "After Macro Events" in content:
        violations.append("contains_after_macro_events_literal")
    if EMBEDDED_AFFILIATE_PATTERN.search(content):
        violations.append("embedded_affiliate_link")

    fm = extract_frontmatter(content)
    if not fm:
        violations.append("missing_frontmatter")
        return sorted(set(violations))

    for key in REQUIRED_FRONTMATTER_KEYS:
        if key not in fm:
            violations.append(f"missing_{key}")

    event_type = str(fm.get("event_type", "")).upper()
    if event_type not in ALLOWED_EVENT_TYPES:
        violations.append("event_type_not_allowed")

    event_direction = str(fm.get("event_direction", "")).lower()
    if event_direction not in {"up", "down", "flat"}:
        violations.append("invalid_event_direction")

    direction_basis = str(fm.get("direction_basis", "")).lower()
    if direction_basis != "vs_previous":
        violations.append("invalid_direction_basis")

    outcome_status = str(fm.get("outcome_status", "")).lower()
    if outcome_status not in {"ok", "pending"}:
        violations.append("invalid_outcome_status")

    for field in ["quality_score", "sample_size", "freshness_days", "event_actual", "event_previous", "event_delta"]:
        if field in fm and not is_finite_number(fm.get(field)):
            violations.append(f"non_numeric_{field}")

    freshness_state = str(fm.get("freshness_status", "")).lower()
    if freshness_state not in {"fresh", "stale"}:
        violations.append("invalid_freshness_status")

    if "is_core_page" not in fm or not isinstance(fm.get("is_core_page"), bool):
        violations.append("invalid_is_core_page")
    if "core_window_days" not in fm or not is_finite_number(fm.get("core_window_days")):
        violations.append("invalid_core_window_days")
    elif int(float(fm.get("core_window_days", 0))) != CORE_WINDOW_DAYS:
        violations.append("core_window_days_mismatch")
    if not str(fm.get("body_variant_family", "")).strip():
        violations.append("invalid_body_variant_family")
    if str(fm.get("narrative_trigger", "")).strip() not in {
        "extreme_outperformance",
        "moderate_outperformance",
        "strict_median_norm",
        "moderate_underperformance",
        "extreme_underperformance",
        "low_context",
    }:
        violations.append("invalid_narrative_trigger")
    if str(fm.get("narrative_rank_band", "")).strip() not in {"extreme", "moderate", "median", "low_context"}:
        violations.append("invalid_narrative_rank_band")
    if str(fm.get("narrative_direction_band", "")).strip() not in {"positive", "negative", "neutral", "unknown"}:
        violations.append("invalid_narrative_direction_band")
    for field in [
        "hub_baseline_mean_t7",
        "hub_baseline_median_t7",
        "hub_baseline_std_t7",
        "hub_baseline_delta",
        "z_score_t7",
        "percentile_t7",
    ]:
        if field in fm and not is_finite_number(fm.get(field)):
            violations.append(f"non_numeric_{field}")
    percentile = to_float(fm.get("percentile_t7"))
    if percentile is not None and not (0.0 <= percentile <= 100.0):
        violations.append("percentile_out_of_range")

    metrics = fm.get("metrics")
    if not isinstance(metrics, dict):
        violations.append("invalid_metrics_object")
    else:
        for field in ["sharpe_t7", "mdd_t7", "volatility", "impact_t1_pct", "impact_t7_pct"]:
            if field not in metrics or not is_finite_number(metrics.get(field)):
                violations.append(f"invalid_metric_{field}")

    ok_prob, prob_violations = validate_probability_block(fm.get("probabilities"))
    if not ok_prob:
        violations.extend(prob_violations)

    sample_size = fm.get("sample_size")
    confidence_level = str(fm.get("confidence_level", "")).lower()
    if is_finite_number(sample_size):
        sample_size_num = float(sample_size)
        if sample_size_num < 5 and confidence_level != "low":
            violations.append("confidence_level_should_be_low")
        if sample_size_num >= 5 and confidence_level != "normal":
            violations.append("confidence_level_should_be_normal")
    else:
        sample_size_num = -1.0

    penalties = fm.get("penalties")
    if not isinstance(penalties, dict):
        violations.append("invalid_penalties_object")
    else:
        for field in ["sample", "freshness", "confidence", "outcome"]:
            value = penalties.get(field)
            if not is_finite_number(value):
                violations.append(f"invalid_penalty_{field}")
                continue
            if float(value) < 0:
                violations.append(f"negative_penalty_{field}")

    raw_score = fm.get("raw_signal_score")
    robust_score = fm.get("robust_score")
    if not is_finite_number(raw_score):
        violations.append("invalid_raw_signal_score")
    if not is_finite_number(robust_score):
        violations.append("invalid_robust_score")

    if (
        isinstance(penalties, dict)
        and is_finite_number(raw_score)
        and is_finite_number(robust_score)
        and sample_size_num >= 0
    ):
        sample_penalty = float(penalties.get("sample", 0.0))
        freshness_penalty = float(penalties.get("freshness", 0.0))
        confidence_penalty = float(penalties.get("confidence", 0.0))
        outcome_penalty = float(penalties.get("outcome", 0.0))

        expected_sample = expected_sample_penalty(sample_size_num)
        if abs(sample_penalty - expected_sample) > 0.01:
            violations.append("penalty_sample_mismatch")

        expected_freshness = (
            EXPECTED_ROBUST_PENALTIES["freshness_stale"]
            if freshness_state == "stale"
            else EXPECTED_ROBUST_PENALTIES["freshness_fresh"]
        )
        if abs(freshness_penalty - expected_freshness) > 0.01:
            violations.append("penalty_freshness_mismatch")

        expected_confidence = (
            EXPECTED_ROBUST_PENALTIES["confidence_low"]
            if confidence_level == "low"
            else EXPECTED_ROBUST_PENALTIES["confidence_normal"]
        )
        if abs(confidence_penalty - expected_confidence) > 0.01:
            violations.append("penalty_confidence_mismatch")

        expected_outcome = (
            EXPECTED_ROBUST_PENALTIES["outcome_pending"]
            if outcome_status == "pending"
            else EXPECTED_ROBUST_PENALTIES["outcome_ok"]
        )
        if abs(outcome_penalty - expected_outcome) > 0.01:
            violations.append("penalty_outcome_mismatch")

        reconstructed = float(raw_score) - (sample_penalty + freshness_penalty + confidence_penalty + outcome_penalty)
        if abs(reconstructed - float(robust_score)) > 0.01:
            violations.append("robust_score_formula_mismatch")

    index_tier = str(fm.get("index_tier", "")).upper()
    if index_tier not in {"A", "B", "C"}:
        violations.append("invalid_index_tier")
    is_recent_90d = fm.get("is_recent_90d")
    if not isinstance(is_recent_90d, bool):
        violations.append("invalid_is_recent_90d")
    canonical_target = str(fm.get("canonical_target", "")).lower()
    if canonical_target not in {"self", "hub", "none"}:
        violations.append("invalid_canonical_target")
    canonical_url = str(fm.get("canonical_url", "")).strip()
    robots_directive = str(fm.get("robots_directive", "")).strip().lower()
    if robots_directive not in {"index,follow", "noindex,follow"}:
        violations.append("invalid_robots_directive")
    in_blog_sitemap = fm.get("in_blog_sitemap")
    if not isinstance(in_blog_sitemap, bool):
        violations.append("invalid_in_blog_sitemap")

    if robots_directive == "noindex,follow" and canonical_target == "hub":
        violations.append("seo_signal_conflict_noindex_with_hub_canonical")
    if canonical_target == "none" and canonical_url:
        violations.append("canonical_none_must_not_have_url")
    if canonical_target in {"self", "hub"} and not canonical_url:
        violations.append("canonical_target_missing_url")
    if canonical_target == "hub" and "/playbooks/" not in canonical_url:
        violations.append("canonical_hub_url_invalid")
    if canonical_target == "self" and "/blog/" not in canonical_url:
        violations.append("canonical_self_url_invalid")

    if index_tier == "C":
        if robots_directive != "noindex,follow":
            violations.append("tier_c_requires_noindex")
        if canonical_target != "none":
            violations.append("tier_c_requires_canonical_none")
        if in_blog_sitemap is True:
            violations.append("tier_c_must_not_be_in_blog_sitemap")
    elif index_tier in {"A", "B"}:
        if robots_directive != "index,follow":
            violations.append("tier_ab_requires_index")
        if isinstance(is_recent_90d, bool):
            expected_canonical = "self" if is_recent_90d else "hub"
            if canonical_target != expected_canonical:
                violations.append("tier_ab_canonical_target_mismatch")
            if is_recent_90d and in_blog_sitemap is not True:
                violations.append("recent_ab_requires_blog_sitemap")
            if (not is_recent_90d) and in_blog_sitemap is not False:
                violations.append("old_ab_must_not_be_in_blog_sitemap")

    return sorted(set(violations))


def validate_redirects(
    root: Path,
    slug_redirects_path: Path | None = None,
    vercel_path: Path | None = None,
) -> Dict[str, object]:
    violations: List[str] = []

    slug_redirects_path = slug_redirects_path or (root / "data" / "slug_redirects.json")
    vercel_path = vercel_path or (root / "vercel.json")

    slug_redirects: Dict[str, str] = {}
    if slug_redirects_path.exists():
        try:
            payload = json.loads(slug_redirects_path.read_text(encoding="utf-8"))
            for item in payload.get("redirects", []):
                source = str(item.get("source", "")).strip()
                destination = str(item.get("destination", "")).strip()
                if source and destination:
                    slug_redirects[source] = destination
        except Exception:
            violations.append("invalid_slug_redirects_json")
    else:
        violations.append("missing_slug_redirects_json")

    vercel_redirects: List[Dict[str, str]] = []
    if vercel_path.exists():
        try:
            vercel_payload = json.loads(vercel_path.read_text(encoding="utf-8"))
            vercel_redirects = vercel_payload.get("redirects", []) or []
        except Exception:
            violations.append("invalid_vercel_json")
    else:
        violations.append("missing_vercel_json")

    source_map: Dict[str, str] = {}
    for item in vercel_redirects:
        source = str(item.get("source", "")).strip()
        destination = str(item.get("destination", "")).strip()
        if not source:
            continue
        if source in source_map and source_map[source] != destination:
            violations.append("duplicate_redirect_source_conflict")
        source_map[source] = destination

    for source, destination in slug_redirects.items():
        if source_map.get(source) != destination:
            violations.append("slug_redirect_missing_in_vercel")
            break

    next_map = {k: v for k, v in source_map.items() if k.startswith("/blog/") and v.startswith("/blog/")}
    for start in next_map:
        seen = set()
        cur = start
        while cur in next_map:
            if cur in seen:
                violations.append("redirect_cycle_detected")
                break
            seen.add(cur)
            cur = next_map[cur]

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_sitemap(
    root: Path,
    public_dir: Path | None = None,
    manifest_path: Path | None = None,
) -> Dict[str, object]:
    violations: List[str] = []
    public_dir = public_dir or (root / "public")

    index_path = public_dir / "sitemap-index.xml"
    core_path = public_dir / "sitemap-core.xml"
    assets_path = public_dir / "sitemap-assets.xml"
    events_path = public_dir / "sitemap-events.xml"
    playbooks_path = public_dir / "sitemap-playbooks.xml"
    blog_paths = sorted(public_dir.glob("sitemap-blog-*.xml"))

    if not index_path.exists():
        violations.append("missing_sitemap_index")
        return {"violations": violations, "count": len(violations)}

    if not core_path.exists():
        violations.append("missing_sitemap_core")
    if not assets_path.exists():
        violations.append("missing_sitemap_assets")
    if not events_path.exists():
        violations.append("missing_sitemap_events")
    if not playbooks_path.exists():
        violations.append("missing_sitemap_playbooks")
    if not blog_paths:
        violations.append("missing_sitemap_blog")

    index_content = index_path.read_text(encoding="utf-8")
    for name in ["sitemap-core.xml", "sitemap-assets.xml", "sitemap-events.xml", "sitemap-playbooks.xml"]:
        if name not in index_content:
            violations.append(f"sitemap_index_missing_{name.replace('.xml', '')}")
    if "sitemap-blog-" not in index_content:
        violations.append("sitemap_index_missing_blog_chunk")

    for sitemap_file in [index_path, core_path, assets_path, events_path, playbooks_path, *blog_paths]:
        if not sitemap_file.exists():
            continue
        content = sitemap_file.read_text(encoding="utf-8")
        if re.search(r"/blog/[a-z0-9-]*after-macro-[0-9]{4}-[0-9]{2}-[0-9]{2}", content):
            violations.append("sitemap_contains_legacy_macro_slug")

    if core_path.exists():
        core_content = core_path.read_text(encoding="utf-8")
        if "/events" not in core_content:
            violations.append("core_sitemap_missing_events_route")
        expected_priorities = {
            "/": "1.0",
            "/leaderboard": "0.95",
            "/events": "0.9",
            "/playbooks": "0.88",
            "/blog": "0.85",
            "/about": "0.82",
        }
        for route, priority in expected_priorities.items():
            loc_pattern = (
                r"<loc>https?://[^<]+/</loc>"
                if route == "/"
                else rf"<loc>[^<]*{re.escape(route)}</loc>"
            )
            pattern = rf"{loc_pattern}[\s\S]*?<priority>{re.escape(priority)}</priority>"
            if not re.search(pattern, core_content):
                violations.append(f"core_priority_mismatch_{route.strip('/').replace('/', '_') or 'home'}")
    if assets_path.exists() and "/tags/" not in assets_path.read_text(encoding="utf-8"):
        violations.append("assets_sitemap_missing_tags")
    if events_path.exists() and "/events/" not in events_path.read_text(encoding="utf-8"):
        violations.append("events_sitemap_missing_event_routes")
    if playbooks_path.exists():
        playbooks_content = playbooks_path.read_text(encoding="utf-8")
        if "/playbooks/" not in playbooks_content:
            expected_indexable = 0
            hub_briefs_path = root / "data" / "hub_briefs.yaml"
            if hub_briefs_path.exists():
                try:
                    raw = hub_briefs_path.read_text(encoding="utf-8")
                    payload = yaml.safe_load(raw) if yaml is not None else parse_hub_briefs_fallback(raw)
                except Exception:
                    payload = parse_hub_briefs_fallback(raw)
                if isinstance(payload, dict):
                    for asset in HUB_ASSETS:
                        for event in HUB_EVENTS:
                            key = f"{asset}_{event}"
                            item = payload.get(key) if isinstance(payload.get(key), dict) else {}
                            status = str(item.get("status", "")).lower()
                            indexing = str(item.get("indexing", "")).lower()
                            if indexing not in {"index", "noindex"}:
                                indexing = "index" if status == "approved" else "noindex"
                            content_depth_ok = hub_content_depth_passes(item)
                            if indexing == "index" and content_depth_ok:
                                expected_indexable += 1
            if expected_indexable > 0:
                violations.append("playbooks_sitemap_missing_playbook_routes")

    blog_lastmods: List[str] = []
    for blog_sitemap in blog_paths:
        content = blog_sitemap.read_text(encoding="utf-8")
        blog_lastmods.extend(re.findall(r"<lastmod>([^<]+)</lastmod>", content))
    if len(blog_lastmods) >= 50 and len(set(blog_lastmods)) == 1:
        local_manifest_path = manifest_path or (root / "data" / "page_manifest.json")
        allow_uniform = False
        if local_manifest_path.exists():
            try:
                payload = json.loads(local_manifest_path.read_text(encoding="utf-8"))
                allow_uniform = bool(payload.get("allow_uniform_lastmod_once"))
            except Exception:
                allow_uniform = False
        if not allow_uniform:
            violations.append("sitemap_blog_lastmod_uniform")

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_filter_routes(root: Path) -> Dict[str, object]:
    violations: List[str] = []
    for path in list((root / "src" / "pages").rglob("*.astro")) + list((root / "src" / "layouts").rglob("*.astro")):
        text = path.read_text(encoding="utf-8")
        if "/blog?asset=" in text:
            violations.append(f"legacy_asset_query_filter:{path.relative_to(root)}")

    return {"violations": violations, "count": len(violations)}


def validate_target_matrix(
    root: Path,
    as_of_date: str,
    csv_path: Path | None = None,
    db_path: Path | None = None,
) -> Dict[str, object]:
    violations: List[str] = []

    csv_path = csv_path or (root / "data" / "verified_targets.csv")
    db_path = db_path or (root / "data" / "macro_events.db")

    if not csv_path.exists():
        return {"violations": ["missing_verified_targets_csv"], "count": 1}
    if not db_path.exists():
        return {"violations": ["missing_macro_events_db"], "count": 1}

    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = set(reader.fieldnames or [])
        missing_cols = sorted(EXPECTED_CSV_COLUMNS - headers)
        if missing_cols:
            violations.append("missing_csv_columns:" + ",".join(missing_cols))

        rows = list(reader)

    combos = set()
    duplicate_count = 0
    for row in rows:
        key = (row.get("asset", "").upper(), row.get("event_type", "").upper(), row.get("date", ""))
        if key in combos:
            duplicate_count += 1
        combos.add(key)

        direction = str(row.get("event_direction", "")).lower()
        status = str(row.get("outcome_status", "")).lower()
        basis = str(row.get("direction_basis", "")).lower()

        if direction not in {"up", "down", "flat"}:
            violations.append("invalid_csv_event_direction")
            break
        if status != "ok":
            violations.append("csv_outcome_not_ok")
            break
        if basis != "vs_previous":
            violations.append("invalid_csv_direction_basis")
            break

        for field in ["event_actual", "event_previous", "event_delta"]:
            value = row.get(field)
            if value is None or value == "" or not is_finite_number(value):
                violations.append(f"invalid_csv_{field}")
                break
        freshness_value = row.get("freshness_days")
        if freshness_value is None or freshness_value == "" or not is_finite_number(freshness_value):
            violations.append("invalid_csv_freshness_days")
            break
        if float(freshness_value) < 0:
            violations.append("negative_csv_freshness_days")
            break

    if duplicate_count > 0:
        violations.append("duplicate_target_rows")

    as_of_cutoff = cutoff_date(as_of_date)
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        expected_dates: Dict[str, List[str]] = {}
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
                expected_dates[event_type] = [str(row[0]) for row in cursor.fetchall()]
        else:
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
                expected_dates[event_type] = [str(row[0]) for row in cursor.fetchall()]
    finally:
        conn.close()

    expected = {
        (asset, event_type, event_date)
        for asset in PRIMARY_ASSETS
        for event_type, dates in expected_dates.items()
        for event_date in dates
    }

    missing = expected - combos
    extra = combos - expected

    if missing:
        violations.append(f"matrix_missing_combos:{len(missing)}")
    if extra:
        violations.append(f"matrix_extra_combos:{len(extra)}")

    expected_count = len(expected)
    if len(rows) != expected_count:
        violations.append(f"matrix_count_mismatch:{len(rows)}_expected_{expected_count}")

    return {
        "violations": sorted(set(violations)),
        "count": len(sorted(set(violations))),
        "row_count": len(rows),
        "expected_count": expected_count,
    }


def validate_event_pool(root: Path, as_of_date: str, db_path: Path | None = None) -> Dict[str, object]:
    violations: List[str] = []
    db_path = db_path or (root / "data" / "macro_events.db")
    if not db_path.exists():
        return {"violations": ["missing_macro_events_db"], "count": 1}

    as_of_cutoff = datetime.strptime(cutoff_date(as_of_date), "%Y-%m-%d").date()
    threshold = as_of_cutoff - timedelta(days=90)

    conn = sqlite3.connect(db_path)
    try:
        if not table_exists(conn, "event_calendar"):
            return {"violations": ["missing_event_calendar_table"], "count": 1}
        cursor = conn.cursor()
        latest_by_event: Dict[str, str] = {}
        for event_type in sorted(ALLOWED_EVENT_TYPES):
            cursor.execute(
                """
                SELECT MAX(ec.event_date)
                FROM event_calendar ec
                WHERE ec.event_type = ?
                  AND ec.event_date <= ?
                  AND LOWER(COALESCE(ec.status, 'confirmed')) NOT IN ('disabled', 'skip')
                """,
                (event_type, as_of_cutoff.isoformat()),
            )
            result = cursor.fetchone()
            latest = str(result[0]) if result and result[0] else ""
            latest_by_event[event_type] = latest
            if not latest:
                violations.append(f"event_pool_missing_{event_type.lower()}")
                continue
            latest_dt = datetime.strptime(latest, "%Y-%m-%d").date()
            if latest_dt < threshold:
                violations.append(f"event_pool_stale_{event_type.lower()}_{latest}")
    finally:
        conn.close()

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_cta_routes(root: Path, offers_path: Path | None = None) -> Dict[str, object]:
    violations: List[str] = []
    warnings: List[str] = []
    offers_path = offers_path or (root / "src" / "data" / "offers.json")
    if not offers_path.exists():
        return {"violations": ["missing_offers_json"], "warnings": [], "count": 1}

    try:
        payload = json.loads(offers_path.read_text(encoding="utf-8"))
    except Exception:
        return {"violations": ["invalid_offers_json"], "warnings": [], "count": 1}

    primary_map = payload.get("primary_offer_keys", {}) or {}
    secondary_map = payload.get("secondary_offer_keys", {}) or {}
    offers = payload.get("offers", {}) or {}

    for asset in ["QQQ", "SPY", "NVDA"]:
        primary = str(primary_map.get(asset) or primary_map.get("DEFAULT") or "").lower()
        if primary != "ibkr":
            violations.append(f"invalid_primary_offer_{asset.lower()}")
        secondary = [str(item).lower() for item in (secondary_map.get(asset) or [])]
        if "futu" not in secondary:
            violations.append(f"missing_secondary_futu_{asset.lower()}")

    for key in ["ibkr", "futu"]:
        if key not in offers:
            violations.append(f"missing_offer_definition_{key}")

    dynamic_cta = root / "src" / "components" / "DynamicCta.astro"
    index_cta = root / "src" / "pages" / "index.astro"
    for path in [dynamic_cta, index_cta]:
        if not path.exists():
            violations.append(f"missing_cta_file:{path}")
            continue
        source = path.read_text(encoding="utf-8")
        if 'data-cta-role="secondary"' in source and "btn-secondary-muted" not in source:
            violations.append(f"missing_secondary_muted_style:{path.name}")
        if re.search(r'data-cta-role="secondary"[\s\S]{0,280}class="[^"]*btn-primary', source):
            violations.append(f"secondary_uses_primary_class:{path.name}")

    if "NVDA" in primary_map or "NVDA" in secondary_map:
        index_source = index_cta.read_text(encoding="utf-8") if index_cta.exists() else ""
        has_nvda_carrier = "NVDA" in index_source
        if not has_nvda_carrier:
            warnings.append("nvda_cta_configured_without_visible_carrier")

    return {
        "violations": sorted(set(violations)),
        "warnings": sorted(set(warnings)),
        "count": len(sorted(set(violations))),
    }


def validate_freshness_semantics(
    root: Path,
    as_of_date: str,
    csv_path: Path | None = None,
    index_path: Path | None = None,
    content_dir: Path | None = None,
) -> Dict[str, object]:
    violations: List[str] = []
    csv_path = csv_path or (root / "data" / "verified_targets.csv")
    index_path = index_path or (root / "src" / "pages" / "index.astro")
    content_dir = content_dir or (root / "src" / "content" / "blog")
    if not csv_path.exists() or not index_path.exists():
        return {"violations": ["missing_freshness_inputs"], "count": 1}

    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = [
            (str(row.get("date", "")).strip(), str(row.get("event_type", "")).strip().upper())
            for row in reader
            if str(row.get("date", "")).strip()
        ]
    if not rows:
        return {"violations": ["missing_target_dates"], "count": 1}

    latest_date = max(item[0] for item in rows)
    latest_types = {event_type for dt, event_type in rows if dt == latest_date and event_type in EVENT_FRESHNESS_THRESHOLDS}
    if not latest_types:
        latest_types = {"CPI"}
    threshold = min(EVENT_FRESHNESS_THRESHOLDS[event_type] for event_type in latest_types)
    as_of_cutoff = datetime.strptime(cutoff_date(as_of_date), "%Y-%m-%d").date()
    latest_dt = datetime.strptime(latest_date, "%Y-%m-%d").date()
    age_days = (as_of_cutoff - latest_dt).days

    source = index_path.read_text(encoding="utf-8")
    if "Today's Event Playbook" in source:
        violations.append("freshness_forbidden_today_heading")
    if "Current Event Playbook" not in source and "Latest Event Playbook" not in source:
        violations.append("freshness_missing_supported_heading")

    if age_days > threshold:
        if "Latest Event Playbook" not in source:
            violations.append("freshness_missing_latest_heading")
        if "Last event:" not in source:
            violations.append("freshness_missing_last_event_note")
        if "Stale Data" not in source:
            violations.append("freshness_missing_stale_badge")
    else:
        if "Current Event Playbook" not in source:
            violations.append("freshness_missing_current_heading")

    if content_dir.exists():
        for md_file in content_dir.glob("*.md"):
            frontmatter = extract_frontmatter(md_file.read_text(encoding="utf-8"))
            event_type = str(frontmatter.get("event_type", "")).upper()
            freshness_value = frontmatter.get("freshness_days")
            freshness_state = str(frontmatter.get("freshness_status", "")).lower()
            if event_type not in EVENT_FRESHNESS_THRESHOLDS or not is_finite_number(freshness_value):
                continue
            expected = "stale" if float(freshness_value) > EVENT_FRESHNESS_THRESHOLDS[event_type] else "fresh"
            if freshness_state != expected:
                violations.append("frontmatter_freshness_status_mismatch")
                break

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_snapshot_freshness_contract(
    root: Path,
    snapshot_path: Path | None = None,
    index_path: Path | None = None,
) -> Dict[str, object]:
    violations: List[str] = []
    snapshot_path = snapshot_path or (root / "src" / "daily_snapshot.json")
    index_path = index_path or (root / "src" / "pages" / "index.astro")
    allowed_statuses = {"fresh", "stale", "fallback", "calendar_unknown"}
    allowed_source_quality = {"live", "fallback", "calendar_unknown"}
    allowed_display_modes = {"live", "delayed", "fallback", "calendar_unknown"}
    allowed_asset_types = {"crypto", "us_session"}

    if not snapshot_path.exists():
        return {"violations": ["missing_daily_snapshot_json"], "count": 1}

    try:
        payload = json.loads(snapshot_path.read_text(encoding="utf-8"))
    except Exception:
        return {"violations": ["invalid_daily_snapshot_json"], "count": 1}

    if not isinstance(payload, dict):
        return {"violations": ["daily_snapshot_not_object"], "count": 1}
    if not re.match(r"^\d{4}-\d{2}-\d{2}T", str(payload.get("timestamp", ""))):
        violations.append("daily_snapshot_missing_timestamp")

    markets = payload.get("markets")
    if not isinstance(markets, dict) or not markets:
        violations.append("daily_snapshot_missing_markets")
        return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}

    has_crypto = False
    has_us_session = False
    for asset, item in markets.items():
        if not isinstance(item, dict):
            violations.append(f"snapshot_market_not_object:{asset}")
            continue

        asset_type = str(item.get("asset_type", "")).strip().lower()
        freshness = str(item.get("freshness_status", "")).strip().lower()
        as_of_date = str(item.get("as_of_date", "")).strip()
        as_of_ts = str(item.get("as_of_ts", "")).strip()
        source = str(item.get("source", "")).strip()
        source_quality = str(item.get("source_quality", "")).strip().lower()
        display_mode = str(item.get("display_mode", "")).strip().lower()
        data_age_hours = item.get("data_age_hours")

        if asset_type not in allowed_asset_types:
            violations.append(f"snapshot_invalid_asset_type:{asset}")
        if asset_type == "crypto":
            has_crypto = True
        if asset_type == "us_session":
            has_us_session = True

        if freshness not in allowed_statuses:
            violations.append(f"snapshot_invalid_freshness_status:{asset}")
        if source_quality not in allowed_source_quality:
            violations.append(f"snapshot_invalid_source_quality:{asset}")
        if display_mode not in allowed_display_modes:
            violations.append(f"snapshot_invalid_display_mode:{asset}")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", as_of_date):
            violations.append(f"snapshot_invalid_as_of_date:{asset}")
        if not re.match(r"^\d{4}-\d{2}-\d{2}T", as_of_ts):
            violations.append(f"snapshot_invalid_as_of_ts:{asset}")
        if not source:
            violations.append(f"snapshot_missing_source:{asset}")
        if data_age_hours is not None and not is_finite_number(data_age_hours):
            violations.append(f"snapshot_invalid_data_age_hours:{asset}")

        for field in ["price", "change", "high", "low"]:
            if field not in item or not is_finite_number(item.get(field)):
                violations.append(f"snapshot_invalid_{field}:{asset}")

    if not has_crypto:
        violations.append("snapshot_missing_crypto_assets")
    if not has_us_session:
        violations.append("snapshot_missing_us_session_assets")

    if not index_path.exists():
        violations.append("missing_index_astro_for_snapshot_contract")
    else:
        index_source = index_path.read_text(encoding="utf-8")
        if "As-of:" not in index_source:
            violations.append("snapshot_ui_missing_asof_label")
        if "freshnessLabel" not in index_source:
            violations.append("snapshot_ui_missing_freshness_badge")
        if "source_quality" not in index_source:
            violations.append("snapshot_ui_missing_source_quality_usage")
        if "24/7 Data Updates" in index_source:
            violations.append("snapshot_ui_contains_misleading_24_7_claim")

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_conditional_sample_contract(content_dir: Path, csv_path: Path) -> Dict[str, object]:
    violations: List[str] = []
    if not content_dir.exists():
        return {"violations": ["missing_content_dir"], "count": 1}
    if not csv_path.exists():
        return {"violations": ["missing_verified_targets_csv"], "count": 1}

    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        csv_map: Dict[str, Dict[str, str]] = {}
        positive_rows = 0
        valid_rows = 0
        for row in reader:
            slug = str(row.get("url_slug", "")).strip()
            if not slug:
                continue
            csv_map[slug] = row
            value = to_float(row.get("conditional_sample_size"))
            if value is not None:
                valid_rows += 1
                if value > 0:
                    positive_rows += 1

    if valid_rows == 0:
        violations.append("conditional_sample_missing_or_non_numeric_in_csv")
        return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}
    if positive_rows == 0:
        violations.append("conditional_sample_all_zero")

    for path in sorted(content_dir.glob("*.md")):
        slug = path.stem
        row = csv_map.get(slug)
        if row is None:
            violations.append("conditional_sample_csv_row_missing")
            break

        fm = extract_frontmatter(path.read_text(encoding="utf-8"))
        probabilities = fm.get("probabilities")
        conditional = probabilities.get("conditional") if isinstance(probabilities, dict) else None
        fm_size = to_float(conditional.get("sample_size") if isinstance(conditional, dict) else None)
        csv_size = to_float(row.get("conditional_sample_size"))
        if fm_size is None or csv_size is None:
            violations.append("conditional_sample_non_numeric")
            break
        if abs(fm_size - csv_size) > 0.01:
            violations.append("conditional_sample_csv_frontmatter_mismatch")
            break

    return {
        "violations": sorted(set(violations)),
        "count": len(sorted(set(violations))),
        "valid_rows": valid_rows,
        "positive_rows": positive_rows,
    }


def validate_csv_contract_backfill(csv_path: Path) -> Dict[str, object]:
    violations: List[str] = []
    if not csv_path.exists():
        return {"violations": ["missing_verified_targets_csv"], "count": 1}
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = set(reader.fieldnames or [])
        required = {"conditional_sample_size", "title_variant_id", "title_template_key"}
        missing = sorted(required - headers)
        if missing:
            violations.append("csv_contract_missing_backfill_columns:" + ",".join(missing))
    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_seo_signal_conflict_contract(content_dir: Path) -> Dict[str, object]:
    violations: List[str] = []
    if not content_dir.exists():
        return {"violations": ["missing_content_dir"], "count": 1}
    for path in sorted(content_dir.glob("*.md")):
        fm = extract_frontmatter(path.read_text(encoding="utf-8"))
        robots_directive = str(fm.get("robots_directive", "")).lower()
        canonical_target = str(fm.get("canonical_target", "")).lower()
        if "noindex" in robots_directive and canonical_target not in {"none", "self"}:
            violations.append("seo_signal_conflict_noindex_with_nonself_canonical")
            break
    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_sitemap_canonical_contract(content_dir: Path, public_dir: Path) -> Dict[str, object]:
    violations: List[str] = []
    if not content_dir.exists():
        return {"violations": ["missing_content_dir"], "count": 1}

    blog_paths = sorted(public_dir.glob("sitemap-blog-*.xml"))
    indexed_slugs: set[str] = set()
    for path in blog_paths:
        content = path.read_text(encoding="utf-8")
        for slug in re.findall(r"/blog/([a-z0-9-]+)</loc>", content):
            indexed_slugs.add(slug)

    for path in sorted(content_dir.glob("*.md")):
        slug = path.stem
        fm = extract_frontmatter(path.read_text(encoding="utf-8"))
        canonical_target = str(fm.get("canonical_target", "")).lower()
        in_blog_sitemap = fm.get("in_blog_sitemap")
        if canonical_target != "self":
            if slug in indexed_slugs:
                violations.append("sitemap_contains_nonself_canonical_page")
                break
            if in_blog_sitemap is True:
                violations.append("frontmatter_nonself_canonical_marked_in_blog_sitemap")
                break
    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_tier_contract(content_dir: Path) -> Dict[str, object]:
    violations: List[str] = []
    if not content_dir.exists():
        return {"violations": ["missing_content_dir"], "count": 1}

    for path in sorted(content_dir.glob("*.md")):
        fm = extract_frontmatter(path.read_text(encoding="utf-8"))
        tier = str(fm.get("index_tier", "")).upper()
        robots_directive = str(fm.get("robots_directive", "")).lower()
        canonical_target = str(fm.get("canonical_target", "")).lower()
        is_recent_90d = fm.get("is_recent_90d")
        in_blog_sitemap = fm.get("in_blog_sitemap")

        if tier == "C":
            if robots_directive != "noindex,follow" or canonical_target != "none" or in_blog_sitemap is True:
                violations.append("tier_contract_c_mismatch")
                break
        elif tier in {"A", "B"}:
            if robots_directive != "index,follow":
                violations.append("tier_contract_ab_requires_index")
                break
            if isinstance(is_recent_90d, bool):
                expected = "self" if is_recent_90d else "hub"
                if canonical_target != expected:
                    violations.append("tier_contract_ab_canonical_mismatch")
                    break
        else:
            violations.append("tier_contract_invalid_tier")
            break

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_snapshot_single_source_contract(root: Path) -> Dict[str, object]:
    violations: List[str] = []
    legacy_snapshot = root / "src" / "data" / "daily_snapshot.json"
    if legacy_snapshot.exists():
        violations.append("legacy_snapshot_file_still_exists")

    for path in list((root / "src").rglob("*.astro")) + list((root / "src").rglob("*.ts")):
        text = path.read_text(encoding="utf-8")
        if "data/daily_snapshot.json" in text:
            violations.append(f"legacy_snapshot_import:{path.relative_to(root)}")
            break

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_hub_loader_strict_contract(root: Path) -> Dict[str, object]:
    violations: List[str] = []
    hub_briefs_path = root / "data" / "hub_briefs.yaml"
    if not hub_briefs_path.exists():
        return {"violations": ["missing_hub_briefs_yaml"], "count": 1}

    payload = load_hub_briefs_payload(hub_briefs_path)
    if not isinstance(payload, dict):
        return {"violations": ["invalid_hub_briefs_payload"], "count": 1}

    for asset in HUB_ASSETS:
        for event in HUB_EVENTS:
            key = f"{asset}_{event}"
            item = payload.get(key) if isinstance(payload.get(key), dict) else {}
            status = str(item.get("status", "")).lower()
            indexing = str(item.get("indexing", "")).lower()
            if indexing not in {"index", "noindex"}:
                indexing = "index" if status == "approved" else "noindex"
            if status == "approved" and indexing == "index" and not hub_content_depth_passes(item):
                violations.append(f"approved_index_hub_depth_fail:{key}")

    for relative_path in [
        Path("src/pages/playbooks/[asset]/[event].astro"),
        Path("src/pages/playbooks/index.astro"),
        Path("src/pages/blog/[slug].astro"),
    ]:
        full_path = root / relative_path
        if not full_path.exists():
            violations.append(f"missing_loader_consumer:{relative_path}")
            continue
        text = full_path.read_text(encoding="utf-8")
        if "loadHubBriefs({ strict: true" not in text and "loadHubBriefs({strict: true" not in text:
            violations.append(f"missing_strict_hub_loader:{relative_path}")

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_statistical_feature_safety_contract(content_dir: Path, as_of_date: str) -> Dict[str, object]:
    violations: List[str] = []
    if not content_dir.exists():
        return {"violations": ["missing_content_dir"], "count": 1}

    for path in sorted(content_dir.glob("*.md")):
        fm = extract_frontmatter(path.read_text(encoding="utf-8"))
        percentile = to_float(fm.get("percentile_t7"))
        z_score = to_float(fm.get("z_score_t7"))
        std_value = to_float(fm.get("hub_baseline_std_t7"))
        trigger = str(fm.get("narrative_trigger", "")).strip()
        is_core_page = compute_core_page_flag(fm, as_of_date)
        if percentile is None or z_score is None or std_value is None:
            violations.append("missing_statistical_feature")
            break
        if not (0.0 <= percentile <= 100.0):
            violations.append("percentile_out_of_range")
            break
        if std_value < FEATURE_EPSILON and abs(z_score) > 0.0:
            violations.append("z_score_nonzero_when_std_zero")
            break
        if is_core_page and trigger == "low_context" and abs(z_score) > 0.0:
            violations.append("low_context_should_zero_z_score")
            break
        if not math.isfinite(percentile) or not math.isfinite(z_score):
            violations.append("non_finite_statistical_feature")
            break

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_core_content_depth_contract(content_dir: Path, as_of_date: str) -> Dict[str, object]:
    violations: List[str] = []
    warnings: List[str] = []
    required_headings = [
        "## Distribution Position",
        "## Comparison vs Hub Baseline",
        "## Failure Modes",
        "## Execution Relevance",
    ]

    core_pages: List[Path] = []
    for path in sorted(content_dir.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        fm = extract_frontmatter(content)
        computed_is_core = compute_core_page_flag(fm, as_of_date)
        if isinstance(fm.get("is_core_page"), bool) and fm.get("is_core_page") is not computed_is_core:
            violations.append(f"is_core_page_mismatch:{path.stem}")
        if computed_is_core:
            core_pages.append(path)
            body = extract_markdown_body(content)
            for heading in required_headings:
                if heading not in body:
                    violations.append(f"missing_core_heading:{path.stem}:{heading}")
                    break

    if not core_pages:
        warnings.append("no_core_pages_in_recent_window")
    elif len(core_pages) < 10:
        warnings.append(f"low_core_page_count:{len(core_pages)}")

    return {
        "violations": sorted(set(violations)),
        "count": len(sorted(set(violations))),
        "warnings": warnings,
        "core_pages": len(core_pages),
    }


def validate_content_uniqueness_contract(content_dir: Path, as_of_date: str) -> Dict[str, object]:
    violations: List[str] = []
    warnings: List[str] = []
    core_pages = load_core_page_entries(content_dir, as_of_date)

    if not core_pages:
        warnings.append("no_core_pages_in_recent_window")
        return {"violations": [], "count": 0, "warnings": warnings, "core_pages": 0}
    if len(core_pages) < 10:
        warnings.append(f"low_core_page_count:{len(core_pages)}")

    for slug, fm, body in core_pages:
        word_count = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]*", body))
        if word_count < 450:
            violations.append(f"core_page_word_count_below_min:{slug}:{word_count}")
        if not str(fm.get("narrative_trigger", "")).strip():
            violations.append(f"core_page_missing_narrative_trigger:{slug}")
        for field in [
            "narrative_rank_band",
            "narrative_direction_band",
            "hub_baseline_delta",
            "z_score_t7",
            "percentile_t7",
        ]:
            value = fm.get(field)
            if field.startswith("narrative_"):
                if not str(value or "").strip():
                    violations.append(f"core_page_missing_{field}:{slug}")
            elif not is_finite_number(value):
                violations.append(f"core_page_missing_{field}:{slug}")

    return {
        "violations": sorted(set(violations)),
        "count": len(sorted(set(violations))),
        "warnings": warnings,
        "core_pages": len(core_pages),
    }


def validate_narrative_distribution_contract(content_dir: Path, as_of_date: str) -> Dict[str, object]:
    warnings: List[str] = []
    core_pages = load_core_page_entries(content_dir, as_of_date)
    trigger_counts: Dict[str, int] = {}
    for _slug, fm, _body in core_pages:
        trigger = str(fm.get("narrative_trigger", "")).strip() or "missing"
        trigger_counts[trigger] = trigger_counts.get(trigger, 0) + 1

    core_count = len(core_pages)
    strict_median_share = 0.0
    if core_count > 0:
        strict_median_share = float(trigger_counts.get("strict_median_norm", 0)) / float(core_count)

    trigger_types_present = sorted(name for name, count in trigger_counts.items() if count > 0)
    if core_count >= 12 and strict_median_share > 0.70:
        warnings.append(f"strict_median_norm_share_high:{strict_median_share:.2f}")
    if core_count >= 12 and len(trigger_types_present) == 1:
        warnings.append("single_trigger_type_across_core_pages")
    if core_count >= 20:
        non_median_types = [
            name for name in trigger_types_present if name.startswith("moderate_") or name.startswith("extreme_")
        ]
        if not non_median_types:
            warnings.append("no_moderate_or_extreme_core_pages")

    return {
        "violations": [],
        "count": 0,
        "warnings": warnings,
        "core_pages": core_count,
        "core_page_trigger_counts": trigger_counts,
        "strict_median_norm_share": round(strict_median_share, 4),
        "trigger_types_present": trigger_types_present,
    }


def validate_narrative_text_divergence_contract(content_dir: Path, as_of_date: str) -> Dict[str, object]:
    violations: List[str] = []
    core_pages = load_core_page_entries(content_dir, as_of_date)
    if not core_pages:
        return {"violations": [], "count": 0, "warnings": ["no_core_pages_in_recent_window"], "core_pages": 0}

    required_patterns = {
        "extreme_outperformance": {
            "distribution": [r"\btail\b", r"\bupper decile\b", r"\bextreme positive deviation\b"],
            "execution": [r"\breversion risk\b", r"\bdo not extrapolate\b", r"\bhigher confirmation burden\b"],
        },
        "moderate_outperformance": {
            "distribution": [r"\babove baseline\b", r"\bconstructive\b", r"\bpositive but not extreme\b"],
            "execution": [r"\bconfirmation is still required\b", r"\bconstructive but not extreme\b", r"\babove-baseline\b"],
        },
        "strict_median_norm": {
            "distribution": [r"\bmedian band\b", r"\bcalibration\b", r"\bdo not overstate\b"],
            "execution": [r"\bcalibration\b", r"\bdo not overstate\b", r"\bkeep sizing conservative\b"],
        },
        "moderate_underperformance": {
            "distribution": [r"\bbelow baseline\b", r"\bfragile\b", r"\bbounce risk\b"],
            "execution": [r"\bbounce risk\b", r"\bbelow-baseline\b", r"\btighter invalidation\b"],
        },
        "extreme_underperformance": {
            "distribution": [r"\bweak tail\b", r"\bdownside tail\b", r"\bhigher invalidation burden\b"],
            "execution": [r"\bdownside tail\b", r"\bhigher invalidation burden\b", r"\bwait for confirmation\b"],
        },
        "low_context": {
            "distribution": [r"\binsufficient sample\b", r"\blow context\b", r"\bresearch breadcrumb\b"],
            "execution": [r"\binsufficient sample\b", r"\blow context\b", r"\bresearch breadcrumb\b"],
        },
    }
    forbidden_patterns = {
        "strict_median_norm": [r"\btail\b"],
    }
    shared_first_sentences: Dict[Tuple[str, str], set[str]] = {}

    for slug, fm, body in core_pages:
        trigger = str(fm.get("narrative_trigger", "")).strip()
        distribution_text = extract_section_text(body, "## Distribution Position").lower()
        execution_text = extract_section_text(body, "## Execution Relevance").lower()
        distribution_first = first_sentence(distribution_text)
        execution_first = first_sentence(execution_text)

        if distribution_first:
            shared_first_sentences.setdefault(("distribution", distribution_first), set()).add(trigger)
        if execution_first:
            shared_first_sentences.setdefault(("execution", execution_first), set()).add(trigger)

        patterns = required_patterns.get(trigger, {})
        for scope, pattern_list in patterns.items():
            haystack = distribution_text if scope == "distribution" else execution_text
            if not any(re.search(pattern, haystack) for pattern in pattern_list):
                violations.append(f"missing_{scope}_anchor:{slug}:{trigger}")
        for scope, pattern_list in forbidden_patterns.items():
            if trigger != scope:
                continue
            for pattern in pattern_list:
                if re.search(pattern, distribution_text) or re.search(pattern, execution_text):
                    violations.append(f"forbidden_trigger_anchor:{slug}:{trigger}:{pattern}")
                    break

    for (scope, sentence), triggers in shared_first_sentences.items():
        if len(triggers) > 1 and sentence:
            violations.append(f"shared_{scope}_first_sentence_across_triggers:{sentence[:80]}")

    return {
        "violations": sorted(set(violations)),
        "count": len(sorted(set(violations))),
        "warnings": [],
        "core_pages": len(core_pages),
    }


def validate_core_page_trigger_coverage_contract(content_dir: Path, as_of_date: str) -> Dict[str, object]:
    violations: List[str] = []
    core_pages = load_core_page_entries(content_dir, as_of_date)
    if not core_pages:
        return {"violations": [], "count": 0, "warnings": ["no_core_pages_in_recent_window"], "core_pages": 0}

    for slug, fm, _body in core_pages:
        trigger = str(fm.get("narrative_trigger", "")).strip()
        rank_band = str(fm.get("narrative_rank_band", "")).strip()
        direction_band = str(fm.get("narrative_direction_band", "")).strip()
        sample_size = int(float(fm.get("sample_size", 0) or 0))
        z_score = to_float(fm.get("z_score_t7"))
        percentile = to_float(fm.get("percentile_t7"))
        hub_delta = to_float(fm.get("hub_baseline_delta"))
        if not trigger:
            violations.append(f"missing_narrative_trigger:{slug}")
            continue
        if z_score is None or percentile is None or hub_delta is None:
            violations.append(f"missing_narrative_metrics:{slug}")
            continue
        expected_trigger = resolve_narrative_trigger(z_score, percentile, sample_size)
        if trigger != expected_trigger:
            violations.append(f"trigger_resolution_mismatch:{slug}:{trigger}:{expected_trigger}")
        expected_rank_band = narrative_rank_band(trigger)
        expected_direction_band = narrative_direction_band(trigger)
        if rank_band != expected_rank_band:
            violations.append(f"rank_band_mismatch:{slug}:{rank_band}:{expected_rank_band}")
        if direction_band != expected_direction_band:
            violations.append(f"direction_band_mismatch:{slug}:{direction_band}:{expected_direction_band}")

    return {
        "violations": sorted(set(violations)),
        "count": len(sorted(set(violations))),
        "warnings": [],
        "core_pages": len(core_pages),
    }


def validate_core_page_trigger_telemetry_contract(content_dir: Path, as_of_date: str) -> Dict[str, object]:
    warnings: List[str] = []
    core_pages = load_core_page_entries(content_dir, as_of_date)
    trigger_counts: Dict[str, int] = {}
    trigger_slugs: Dict[str, List[str]] = {}
    for slug, fm, _body in core_pages:
        trigger = str(fm.get("narrative_trigger", "")).strip() or "missing"
        trigger_counts[trigger] = trigger_counts.get(trigger, 0) + 1
        trigger_slugs.setdefault(trigger, []).append(slug)

    if len(core_pages) >= 12 and len([name for name, count in trigger_counts.items() if count > 0]) == 1:
        warnings.append("all_core_pages_share_one_trigger")

    return {
        "violations": [],
        "count": 0,
        "warnings": warnings,
        "core_pages": len(core_pages),
        "trigger_counts": trigger_counts,
        "trigger_slugs": {key: value[:10] for key, value in sorted(trigger_slugs.items())},
    }


def token_lcs_ratio(left: Sequence[str], right: Sequence[str]) -> float:
    if not left or not right:
        return 0.0
    rows = len(left) + 1
    cols = len(right) + 1
    dp = [[0] * cols for _ in range(rows)]
    for i in range(1, rows):
        for j in range(1, cols):
            if left[i - 1] == right[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs = dp[-1][-1]
    return float(lcs) / float(max(len(left), len(right)))


def normalize_title_template(title: str) -> str:
    text = str(title or "").strip().lower()
    text = re.sub(r"\b\d{4}-\d{2}-\d{2}\b", "{date}", text)
    text = re.sub(r"\b(btc|eth|gold|qqq|spy)\b", "{asset}", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def validate_title_diversity_contract(content_dir: Path) -> Dict[str, object]:
    violations: List[str] = []
    if not content_dir.exists():
        return {"violations": ["missing_content_dir"], "count": 1}

    per_event_counts: Dict[str, Dict[str, int]] = {}
    per_event_templates: Dict[str, Dict[str, str]] = {}

    for path in sorted(content_dir.glob("*.md")):
        fm = extract_frontmatter(path.read_text(encoding="utf-8"))
        event_type = str(fm.get("event_type", "")).upper().strip()
        if event_type not in ALLOWED_EVENT_TYPES:
            continue
        template_key = str(fm.get("title_template_key", "")).strip()
        title = str(fm.get("title", "")).strip()
        if not template_key or not title:
            violations.append("title_diversity_missing_template_metadata")
            continue

        per_event_counts.setdefault(event_type, {})
        per_event_templates.setdefault(event_type, {})
        per_event_counts[event_type][template_key] = per_event_counts[event_type].get(template_key, 0) + 1
        per_event_templates[event_type].setdefault(template_key, normalize_title_template(title))

    for event_type in sorted(ALLOWED_EVENT_TYPES):
        counts = per_event_counts.get(event_type, {})
        templates = per_event_templates.get(event_type, {})
        total = sum(counts.values())
        if total == 0:
            violations.append(f"title_diversity_missing_event_titles:{event_type.lower()}")
            continue

        unique_count = len(counts)
        if unique_count < 3:
            violations.append(f"title_diversity_min_templates_fail:{event_type.lower()}")

        max_share = max(counts.values()) / float(total)
        if max_share > 0.50:
            violations.append(f"title_diversity_max_share_fail:{event_type.lower()}")

        template_keys = sorted(templates.keys())
        for idx, left_key in enumerate(template_keys):
            left_tokens = templates[left_key].split()
            for right_key in template_keys[idx + 1 :]:
                right_tokens = templates[right_key].split()
                ratio = token_lcs_ratio(left_tokens, right_tokens)
                if ratio >= 0.60:
                    violations.append(f"title_diversity_lcs_fail:{event_type.lower()}:{left_key}:{right_key}")
                    break
            if any(v.startswith(f"title_diversity_lcs_fail:{event_type.lower()}") for v in violations):
                break

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_calendar_fetch_resilience_contract(root: Path) -> Dict[str, object]:
    violations: List[str] = []
    sync_path = root / "scripts" / "macro_pipeline" / "sync_event_calendar.py"
    ops_path = root / "scripts" / "macro_pipeline" / "run_daily_ops.py"

    if not sync_path.exists():
        return {"violations": ["missing_sync_event_calendar_script"], "count": 1}
    if not ops_path.exists():
        return {"violations": ["missing_run_daily_ops_script"], "count": 1}

    sync_text = sync_path.read_text(encoding="utf-8")
    ops_text = ops_path.read_text(encoding="utf-8")

    required_sync_markers = [
        "requests.Session()",
        "Retry(",
        "status_forcelist=[429, 500, 502, 503, 504]",
        "backoff_factor=1",
        "record_fetch_issue",
        "FETCH_DIAGNOSTICS",
        "parse_fred_csv",
    ]
    for marker in required_sync_markers:
        if marker not in sync_text:
            violations.append(f"calendar_fetch_missing_marker:{marker}")

    if "fetch_diagnostics_count" not in sync_text or "fetch_diagnostics" not in sync_text:
        violations.append("calendar_fetch_missing_diagnostics_summary")

    required_ops_markers = [
        "CURRENT_STEP_LOGS_DIR",
        "stdout_path",
        "stderr_path",
        "EVIDENCE=",
        "evidence_paths",
    ]
    for marker in required_ops_markers:
        if marker not in ops_text:
            violations.append(f"calendar_fetch_missing_ops_evidence_marker:{marker}")

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_schema_graph_and_breadcrumbs(root: Path) -> Dict[str, object]:
    violations: List[str] = []

    layout_path = root / "src" / "layouts" / "Layout.astro"
    breadcrumbs_component = root / "src" / "components" / "Breadcrumbs.astro"
    required_pages = [
        root / "src" / "pages" / "blog" / "[slug].astro",
        root / "src" / "pages" / "events" / "[event].astro",
        root / "src" / "pages" / "tags" / "[tag].astro",
        root / "src" / "pages" / "leaderboard.astro",
        root / "src" / "pages" / "about.astro",
        root / "src" / "pages" / "playbooks" / "index.astro",
        root / "src" / "pages" / "playbooks" / "[asset]" / "[event].astro",
    ]

    if not layout_path.exists():
        return {"violations": ["missing_layout_astro"], "count": 1}

    layout_text = layout_path.read_text(encoding="utf-8")
    jsonld_count = len(re.findall(r'type="application/ld\+json"', layout_text))
    if jsonld_count != 1:
        violations.append("schema_graph_single_script_required")
    if '"@graph"' not in layout_text and "'@graph'" not in layout_text:
        violations.append("schema_graph_missing_at_graph")
    if "BreadcrumbList" not in layout_text:
        violations.append("schema_graph_missing_breadcrumb_list")
    if "breadcrumbs" not in layout_text:
        violations.append("layout_missing_breadcrumb_prop")

    if not breadcrumbs_component.exists():
        violations.append("missing_breadcrumbs_component")
    else:
        component_text = breadcrumbs_component.read_text(encoding="utf-8")
        if "aria-label=\"Breadcrumb\"" not in component_text:
            violations.append("breadcrumbs_component_missing_aria")

    for page_path in required_pages:
        if not page_path.exists():
            violations.append(f"missing_breadcrumb_page:{page_path.relative_to(root)}")
            continue
        source = page_path.read_text(encoding="utf-8")
        if "Breadcrumbs" not in source:
            violations.append(f"page_missing_breadcrumb_component:{page_path.relative_to(root)}")
        if "breadcrumbs" not in source:
            violations.append(f"page_missing_breadcrumb_data:{page_path.relative_to(root)}")

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_related_events_integrity(content_dir: Path) -> Dict[str, object]:
    violations: List[str] = []
    if not content_dir.exists():
        return {"violations": ["missing_content_dir"], "count": 1}

    files = sorted(content_dir.glob("*.md"))
    slug_set = {path.stem for path in files}

    for path in files:
        fm = extract_frontmatter(path.read_text(encoding="utf-8"))
        related = fm.get("related_events")
        if related is None:
            continue
        if not isinstance(related, list):
            violations.append("related_events_not_list")
            continue
        if len(related) > 3:
            violations.append("related_events_overflow")
            continue

        for item in related:
            if not isinstance(item, dict):
                violations.append("related_event_item_not_object")
                break
            for key in ["slug", "title", "event_date", "event_type", "signal", "sharpe_t7", "median_t7_pct", "sample_size"]:
                if key not in item:
                    violations.append(f"related_event_missing_{key}")
                    break

            slug = str(item.get("slug", "")).strip()
            if not slug:
                violations.append("related_event_empty_slug")
                continue
            if slug == path.stem:
                violations.append("related_event_self_link")
            if slug not in slug_set:
                violations.append("related_event_slug_not_found")

            if str(item.get("event_type", "")).upper() not in ALLOWED_EVENT_TYPES:
                violations.append("related_event_invalid_event_type")
            if str(item.get("signal", "")) not in {"Bullish", "Neutral", "Bearish"}:
                violations.append("related_event_invalid_signal")
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(item.get("event_date", ""))):
                violations.append("related_event_invalid_event_date")

            for numeric_field in ["sharpe_t7", "median_t7_pct", "sample_size"]:
                if not is_finite_number(item.get(numeric_field)):
                    violations.append(f"related_event_invalid_{numeric_field}")
            if is_finite_number(item.get("sample_size")) and float(item.get("sample_size")) < 0:
                violations.append("related_event_negative_sample_size")

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_trust_layer(root: Path) -> Dict[str, object]:
    violations: List[str] = []
    trust_component = root / "src" / "components" / "TrustSignals.astro"
    blog_page = root / "src" / "pages" / "blog" / "[slug].astro"
    hub_page = root / "src" / "pages" / "playbooks" / "[asset]" / "[event].astro"

    if not trust_component.exists():
        return {"violations": ["missing_trust_signals_component"], "count": 1}
    trust_text = trust_component.read_text(encoding="utf-8")
    required_markers = [
        "not investment advice",
        "FRED",
        "yfinance",
        "Methodology",
        "dataLastUpdatedAt",
    ]
    for marker in required_markers:
        if marker not in trust_text:
            violations.append(f"trust_component_missing_{marker.lower().replace(' ', '_')}")

    if not blog_page.exists():
        violations.append("missing_blog_slug_page")
    else:
        blog_text = blog_page.read_text(encoding="utf-8")
        if "TrustSignals" not in blog_text:
            violations.append("blog_page_missing_trust_signals")
        if "data_last_updated_at" not in blog_text:
            violations.append("blog_page_missing_data_last_updated_at_binding")

    if not hub_page.exists():
        violations.append("missing_playbook_hub_page")
    else:
        hub_text = hub_page.read_text(encoding="utf-8")
        if "TrustSignals" not in hub_text:
            violations.append("playbook_hub_missing_trust_signals")
        if "reviewedAt" not in hub_text:
            violations.append("playbook_hub_missing_reviewed_at_binding")

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def parse_hub_briefs_fallback(content: str) -> Dict[str, object]:
    payload: Dict[str, object] = {}
    current_key: str | None = None
    current_item: Dict[str, object] | None = None
    in_checklist = False

    for raw_line in content.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if not line.startswith(" ") and stripped.endswith(":"):
            current_key = stripped[:-1].strip()
            if not current_key:
                continue
            current_item = {}
            payload[current_key] = current_item
            in_checklist = False
            continue

        if current_item is None:
            continue

        if in_checklist and stripped.startswith("- "):
            current_item.setdefault("execution_checklist", [])
            if isinstance(current_item["execution_checklist"], list):
                current_item["execution_checklist"].append(parse_scalar(stripped[2:].strip()))
            continue

        if line.startswith("  ") and ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key == "execution_checklist":
                current_item[key] = []
                in_checklist = True
            else:
                current_item[key] = parse_scalar(value)
                in_checklist = False

    return payload


def validate_hub_briefs_contract(root: Path) -> Dict[str, object]:
    violations: List[str] = []
    path = root / "data" / "hub_briefs.yaml"
    if not path.exists():
        return {"violations": ["missing_hub_briefs_yaml"], "count": 1}

    payload = load_hub_briefs_payload(path)

    if not isinstance(payload, dict):
        return {"violations": ["hub_briefs_not_object"], "count": 1}

    expected_keys = {f"{asset}_{event}" for asset in HUB_ASSETS for event in HUB_EVENTS}
    actual_keys = set(payload.keys())
    missing_keys = sorted(expected_keys - actual_keys)
    if missing_keys:
        violations.append(f"hub_briefs_missing_keys:{','.join(missing_keys)}")

    for key in sorted(expected_keys & actual_keys):
        item = payload.get(key)
        if not isinstance(item, dict):
            violations.append(f"hub_brief_not_object:{key}")
            continue
        required_fields = [
            "asset",
            "event_type",
            "thesis",
            "what_changed_recently",
            "risk_watchouts",
            "execution_checklist",
            "reviewed_at",
            "status",
            "indexing",
        ]
        for field in required_fields:
            value = item.get(field)
            if value is None or (isinstance(value, str) and not value.strip()):
                violations.append(f"hub_brief_missing_{field}:{key}")
        if str(item.get("asset", "")).upper() not in HUB_ASSETS:
            violations.append(f"hub_brief_invalid_asset:{key}")
        if str(item.get("event_type", "")).upper() not in HUB_EVENTS:
            violations.append(f"hub_brief_invalid_event_type:{key}")
        checklist = item.get("execution_checklist")
        if not isinstance(checklist, list) or len(checklist) < 3:
            violations.append(f"hub_brief_invalid_checklist:{key}")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(item.get("reviewed_at", ""))):
            violations.append(f"hub_brief_invalid_reviewed_at:{key}")
        status = str(item.get("status", "")).lower()
        indexing = str(item.get("indexing", "")).lower()
        if status not in {"draft", "approved"}:
            violations.append(f"hub_brief_invalid_status:{key}")
        if indexing not in {"index", "noindex"}:
            violations.append(f"hub_brief_invalid_indexing:{key}")
        if status == "draft" and indexing == "index":
            violations.append(f"hub_brief_draft_must_be_noindex:{key}")

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_author_entity_contract(root: Path) -> Dict[str, object]:
    violations: List[str] = []
    layout_path = root / "src" / "layouts" / "Layout.astro"
    authors_path = root / "src" / "data" / "authors.json"
    if not layout_path.exists():
        return {"violations": ["missing_layout_astro"], "count": 1}
    if not authors_path.exists():
        return {"violations": ["missing_authors_json"], "count": 1}

    layout_text = layout_path.read_text(encoding="utf-8")
    if "'@type': 'Person'" not in layout_text:
        violations.append("schema_missing_person_entity")
    if "author: { '@id': authorId }" not in layout_text and 'author: {"@id": authorId}' not in layout_text:
        violations.append("article_author_not_linked_to_person")
    if "authorConfig" not in layout_text:
        violations.append("layout_missing_author_config_binding")

    try:
        payload = json.loads(authors_path.read_text(encoding="utf-8"))
    except Exception:
        return {"violations": ["invalid_authors_json"], "count": 1}
    if not isinstance(payload, dict):
        return {"violations": ["authors_json_not_object"], "count": 1}

    default_key = str(payload.get("defaultAuthorKey", "")).strip()
    authors = payload.get("authors")
    if not default_key:
        violations.append("authors_missing_default_key")
    if not isinstance(authors, list) or not authors:
        violations.append("authors_missing_authors_array")
    else:
        key_set = set()
        for item in authors:
            if not isinstance(item, dict):
                violations.append("authors_item_not_object")
                continue
            key = str(item.get("key", "")).strip()
            if not key:
                violations.append("authors_item_missing_key")
                continue
            key_set.add(key)
            required_fields = ["name", "jobTitle", "url", "sameAs", "description", "credentials"]
            for field in required_fields:
                value = item.get(field)
                if value is None or (isinstance(value, str) and not value.strip()):
                    violations.append(f"authors_item_missing_{field}")
            same_as = item.get("sameAs")
            if not isinstance(same_as, list) or not same_as:
                violations.append("authors_item_invalid_sameAs")
            credentials = item.get("credentials")
            if not isinstance(credentials, list) or not credentials:
                violations.append("authors_item_invalid_credentials")
        if default_key and default_key not in key_set:
            violations.append("authors_default_key_not_found")

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_about_page_contract(root: Path, public_dir: Path | None = None) -> Dict[str, object]:
    violations: List[str] = []
    public_dir = public_dir or (root / "public")
    about_page = root / "src" / "pages" / "about.astro"
    if not about_page.exists():
        return {"violations": ["missing_about_page"], "count": 1}

    text = about_page.read_text(encoding="utf-8")
    required_terms = [
        "The Analyst",
        "Infrastructure",
        "Methodology",
        "Transparency & Disclaimer",
        "FRED",
        "yfinance",
        "OpenClaw daily primary",
        "GitHub Actions manual backup only",
        "Not investment advice",
    ]
    for term in required_terms:
        if term not in text:
            violations.append(f"about_missing_{term.lower().replace(' ', '_').replace('&', 'and')}")

    if "Breadcrumbs" not in text or "breadcrumbs" not in text:
        violations.append("about_missing_breadcrumbs")

    core_sitemap = public_dir / "sitemap-core.xml"
    if not core_sitemap.exists():
        violations.append("missing_sitemap_core")
    else:
        core_text = core_sitemap.read_text(encoding="utf-8")
        if "/about" not in core_text:
            violations.append("about_not_in_core_sitemap")

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_hub_content_depth_contract(root: Path) -> Dict[str, object]:
    violations: List[str] = []
    path = root / "data" / "hub_briefs.yaml"
    if not path.exists():
        return {"violations": ["missing_hub_briefs_yaml"], "count": 1}
    payload = load_hub_briefs_payload(path)
    if not isinstance(payload, dict):
        return {"violations": ["hub_briefs_not_object"], "count": 1}

    for asset in HUB_ASSETS:
        for event in HUB_EVENTS:
            key = f"{asset}_{event}"
            item = payload.get(key)
            if not isinstance(item, dict):
                violations.append(f"hub_content_missing_item:{key}")
                continue
            status = str(item.get("status", "")).lower()
            indexing = str(item.get("indexing", "")).lower()
            if indexing not in {"index", "noindex"}:
                indexing = "index" if status == "approved" else "noindex"
            if status == "approved" and indexing == "index" and not hub_content_depth_passes(item):
                violations.append(f"hub_content_depth_fail:{key}")

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_approved_hub_minimum_contract(root: Path) -> Dict[str, object]:
    warnings: List[str] = []
    path = root / "data" / "hub_briefs.yaml"
    if not path.exists():
        return {"violations": [], "warnings": ["missing_hub_briefs_yaml"], "count": 0}
    payload = load_hub_briefs_payload(path)
    if not isinstance(payload, dict):
        return {"violations": [], "warnings": ["hub_briefs_not_object"], "count": 0}

    indexable_count = 0
    for asset in HUB_ASSETS:
        for event in HUB_EVENTS:
            key = f"{asset}_{event}"
            item = payload.get(key)
            if not isinstance(item, dict):
                continue
            status = str(item.get("status", "")).lower()
            indexing = str(item.get("indexing", "")).lower()
            if indexing not in {"index", "noindex"}:
                indexing = "index" if status == "approved" else "noindex"
            if status == "approved" and indexing == "index" and hub_content_depth_passes(item):
                indexable_count += 1
    if indexable_count < 6:
        warnings.append(f"approved_hub_count_low:{indexable_count}")

    return {"violations": [], "warnings": warnings, "count": 0}


def validate_crawl_policy_contract(
    root: Path,
    public_dir: Path | None = None,
    vercel_path: Path | None = None,
) -> Dict[str, object]:
    violations: List[str] = []
    public_dir = public_dir or (root / "public")
    vercel_path = vercel_path or (root / "vercel.json")
    robots_path = public_dir / "robots.txt"
    crawl_script = root / "scripts" / "ops" / "crawl_access_check.py"

    if not crawl_script.exists():
        violations.append("missing_crawl_access_check_script")

    if not robots_path.exists():
        violations.append("missing_robots_txt")
    else:
        robots_text = robots_path.read_text(encoding="utf-8")
        lowered = robots_text.lower()
        if "user-agent: *" not in lowered:
            violations.append("robots_missing_user_agent_all")
        if "allow: /" not in lowered:
            violations.append("robots_missing_allow_all")
        if "sitemap: https://quantmacro.vercel.app/sitemap.xml" not in lowered:
            violations.append("robots_missing_primary_sitemap")
        if "sitemap: https://quantmacro.vercel.app/sitemap-index.xml" not in lowered:
            violations.append("robots_missing_sitemap_index")
        if re.search(r"user-agent:\s*google-extended[\s\S]*?disallow:\s*/", lowered):
            violations.append("robots_disallow_google_extended")

    if not vercel_path.exists():
        violations.append("missing_vercel_json")
    else:
        try:
            payload = json.loads(vercel_path.read_text(encoding="utf-8"))
        except Exception:
            payload = {}
            violations.append("invalid_vercel_json_for_crawl_policy")
        headers = payload.get("headers", []) if isinstance(payload, dict) else []
        for header_rule in headers:
            for header in header_rule.get("headers", []) if isinstance(header_rule, dict) else []:
                key = str(header.get("key", "")).lower()
                value = str(header.get("value", "")).lower()
                if key == "x-robots-tag":
                    if any(token in value for token in ["noindex", "noai", "nosnippet", "none"]):
                        violations.append("vercel_blocks_index_or_ai_crawlers")
                        break

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_hub_route_contract(root: Path, public_dir: Path | None = None) -> Dict[str, object]:
    violations: List[str] = []
    warnings: List[str] = []
    public_dir = public_dir or (root / "public")

    index_page = root / "src" / "pages" / "playbooks" / "index.astro"
    detail_page = root / "src" / "pages" / "playbooks" / "[asset]" / "[event].astro"
    trust_component = root / "src" / "components" / "TrustSignals.astro"

    if not index_page.exists():
        violations.append("missing_playbooks_index_page")
    if not detail_page.exists():
        violations.append("missing_playbooks_detail_page")
    if not trust_component.exists():
        violations.append("missing_trust_signals_component")

    if detail_page.exists():
        source = detail_page.read_text(encoding="utf-8")
        if "TrustSignals" not in source:
            violations.append("playbook_detail_missing_trust_signals")
        if "Breadcrumbs" not in source:
            violations.append("playbook_detail_missing_breadcrumbs")

    playbooks_sitemap = public_dir / "sitemap-playbooks.xml"
    if not playbooks_sitemap.exists():
        violations.append("missing_playbooks_sitemap")
    else:
        content = playbooks_sitemap.read_text(encoding="utf-8")
        url_count = len(re.findall(r"<url>", content))
        hub_briefs_path = root / "data" / "hub_briefs.yaml"
        expected_indexable_routes: List[str] = []
        draft_routes: List[str] = []
        if hub_briefs_path.exists():
            payload = load_hub_briefs_payload(hub_briefs_path)

            if isinstance(payload, dict):
                for asset in HUB_ASSETS:
                    for event in HUB_EVENTS:
                        key = f"{asset}_{event}"
                        item = payload.get(key)
                        status = str(item.get("status", "")).lower() if isinstance(item, dict) else "draft"
                        indexing = str(item.get("indexing", "")).lower() if isinstance(item, dict) else ""
                        if indexing not in {"index", "noindex"}:
                            indexing = "index" if status == "approved" else "noindex"
                        route = f"/playbooks/{asset.lower()}/{event.lower()}"
                        content_depth_ok = hub_content_depth_passes(item)
                        if indexing == "index" and content_depth_ok:
                            expected_indexable_routes.append(route)
                        else:
                            draft_routes.append(route)

        if len(expected_indexable_routes) < 6:
            warnings.append("approved_hub_count_low")

        if url_count != len(expected_indexable_routes):
            violations.append("playbooks_sitemap_indexable_count_mismatch")

        for route in expected_indexable_routes:
            if route not in content:
                violations.append("playbooks_sitemap_missing_indexable_route")
                break
        for route in draft_routes:
            if route in content:
                violations.append("playbooks_sitemap_contains_noindex_route")
                break

    return {
        "violations": sorted(set(violations)),
        "warnings": sorted(set(warnings)),
        "count": len(sorted(set(violations))),
    }


def validate_hub_draft_noindex_contract(root: Path, public_dir: Path | None = None) -> Dict[str, object]:
    violations: List[str] = []
    public_dir = public_dir or (root / "public")

    playbook_page = root / "src" / "pages" / "playbooks" / "[asset]" / "[event].astro"
    if not playbook_page.exists():
        return {"violations": ["missing_playbook_detail_page"], "count": 1}

    source = playbook_page.read_text(encoding="utf-8")
    required_markers = ["robotsDirective", "noindex,follow", "index,follow", "indexing"]
    for marker in required_markers:
        if marker not in source:
            violations.append(f"playbook_detail_missing_{marker.replace(',', '_')}")

    playbooks_sitemap = public_dir / "sitemap-playbooks.xml"
    if not playbooks_sitemap.exists():
        violations.append("missing_playbooks_sitemap")
        return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}

    sitemap_text = playbooks_sitemap.read_text(encoding="utf-8")
    hub_briefs_path = root / "data" / "hub_briefs.yaml"
    if not hub_briefs_path.exists():
        violations.append("missing_hub_briefs_yaml")
        return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}

    payload = load_hub_briefs_payload(hub_briefs_path)

    if not isinstance(payload, dict):
        violations.append("hub_briefs_not_object")
        return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}

    for asset in HUB_ASSETS:
        for event in HUB_EVENTS:
            key = f"{asset}_{event}"
            item = payload.get(key) if isinstance(payload.get(key), dict) else {}
            status = str(item.get("status", "")).lower()
            indexing = str(item.get("indexing", "")).lower()
            if indexing not in {"index", "noindex"}:
                indexing = "index" if status == "approved" else "noindex"
            route = f"/playbooks/{asset.lower()}/{event.lower()}"
            content_depth_ok = hub_content_depth_passes(item)
            if (indexing == "noindex" or not content_depth_ok) and route in sitemap_text:
                violations.append("draft_or_noindex_hub_present_in_sitemap")
                break
        if "draft_or_noindex_hub_present_in_sitemap" in violations:
            break

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_blog_hub_link_contract(root: Path) -> Dict[str, object]:
    violations: List[str] = []
    blog_page = root / "src" / "pages" / "blog" / "[slug].astro"
    if not blog_page.exists():
        return {"violations": ["missing_blog_slug_page"], "count": 1}

    source = blog_page.read_text(encoding="utf-8")
    required_markers = [
        "hubIsIndexable",
        "hubPrimaryHref",
        "/playbooks/",
        "/events/",
    ]
    for marker in required_markers:
        if marker not in source:
            violations.append(f"blog_hub_link_missing_{marker.strip('/').replace('/', '_')}")
    if "hub.status === 'approved'" not in source or "hub.indexing === 'index'" not in source:
        violations.append("blog_hub_link_missing_approved_index_gate")

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_lastmod_threshold_contract(manifest_path: Path) -> Dict[str, object]:
    violations: List[str] = []
    if not manifest_path.exists():
        return {"violations": ["missing_page_manifest"], "count": 1}

    try:
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception:
        return {"violations": ["invalid_page_manifest_json"], "count": 1}

    pages = payload.get("pages", {}) if isinstance(payload, dict) else {}
    if not isinstance(pages, dict):
        return {"violations": ["manifest_pages_not_object"], "count": 1}

    required_signature_keys = {
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
    }

    for slug, page in pages.items():
        if not isinstance(page, dict):
            continue
        signature = page.get("lastmod_metric_signature")
        decision_reason = str(page.get("lastmod_decision_reason", "")).strip()
        if not isinstance(signature, dict):
            violations.append("manifest_missing_lastmod_metric_signature")
            break
        if not required_signature_keys.issubset(set(signature.keys())):
            violations.append("manifest_lastmod_signature_incomplete")
            break
        if not decision_reason:
            violations.append("manifest_missing_lastmod_decision_reason")
            break
        if decision_reason == "threshold_not_met" and not str(page.get("sitemap_lastmod", "")).strip():
            violations.append(f"manifest_invalid_sitemap_lastmod:{slug}")
            break

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_ymyl_regex_contract(root: Path, content_dir: Path) -> Dict[str, object]:
    violations: List[str] = []
    trust_component = root / "src" / "components" / "TrustSignals.astro"
    if not trust_component.exists():
        return {"violations": ["missing_trust_signals_component"], "count": 1}

    trust_text = trust_component.read_text(encoding="utf-8")
    trust_patterns = [
        r"(?i)Methodology",
        r"(?i)Not investment advice",
        r"(?i)FRED",
        r"(?i)yfinance",
    ]
    for pattern in trust_patterns:
        if not re.search(pattern, trust_text):
            violations.append(f"ymyl_missing_trust_pattern:{pattern}")

    files = sorted(content_dir.glob("*.md"))
    if not files:
        violations.append("ymyl_missing_blog_markdown_files")
        return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}

    for path in files[:50]:
        content = path.read_text(encoding="utf-8")
        if not re.search(r"(?i)Methodology", content):
            violations.append("ymyl_missing_methodology_in_blog")
            break
        if not re.search(r"\d{4}-\d{2}-\d{2}", content):
            violations.append("ymyl_missing_date_stamp_in_blog")
            break

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def run_gates(
    root: Path,
    content_dir: Path,
    as_of_date: str,
    manifest_path: Path,
    public_dir: Path,
    slug_redirects_path: Path,
    vercel_config_path: Path,
    offers_path: Path,
    csv_path: Path,
    db_path: Path,
    index_path: Path,
    snapshot_path: Path,
) -> Dict[str, object]:
    files = sorted(content_dir.glob("*.md"))

    report: Dict[str, object] = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_files": len(files),
        "violations": {},
        "summary": {},
    }

    violations_by_file: Dict[str, List[str]] = {}
    for path in files:
        file_violations = scan_file(path)
        if not file_violations:
            continue
        violations_by_file[path.name] = file_violations
        for issue in file_violations:
            report["summary"][issue] = report["summary"].get(issue, 0) + 1

    redirect_result = validate_redirects(root, slug_redirects_path=slug_redirects_path, vercel_path=vercel_config_path)
    sitemap_result = validate_sitemap(root, public_dir=public_dir, manifest_path=manifest_path)
    route_filter_result = validate_filter_routes(root)
    matrix_result = validate_target_matrix(root, as_of_date, csv_path=csv_path, db_path=db_path)
    event_pool_result = validate_event_pool(root, as_of_date, db_path=db_path)
    cta_result = validate_cta_routes(root, offers_path=offers_path)
    freshness_result = validate_freshness_semantics(
        root,
        as_of_date,
        csv_path=csv_path,
        index_path=index_path,
        content_dir=content_dir,
    )
    snapshot_freshness_result = validate_snapshot_freshness_contract(
        root,
        snapshot_path=snapshot_path,
        index_path=index_path,
    )
    conditional_sample_result = validate_conditional_sample_contract(content_dir, csv_path)
    csv_contract_backfill_result = validate_csv_contract_backfill(csv_path)
    title_diversity_result = validate_title_diversity_contract(content_dir)
    calendar_fetch_resilience_result = validate_calendar_fetch_resilience_contract(root)
    schema_breadcrumb_result = validate_schema_graph_and_breadcrumbs(root)
    related_events_result = validate_related_events_integrity(content_dir)
    trust_layer_result = validate_trust_layer(root)
    hub_briefs_result = validate_hub_briefs_contract(root)
    crawl_policy_result = validate_crawl_policy_contract(root, public_dir=public_dir, vercel_path=vercel_config_path)
    hub_route_result = validate_hub_route_contract(root, public_dir=public_dir)
    hub_draft_noindex_result = validate_hub_draft_noindex_contract(root, public_dir=public_dir)
    blog_hub_link_result = validate_blog_hub_link_contract(root)
    lastmod_threshold_result = validate_lastmod_threshold_contract(manifest_path)
    ymyl_regex_result = validate_ymyl_regex_contract(root, content_dir)
    author_entity_result = validate_author_entity_contract(root)
    about_page_result = validate_about_page_contract(root, public_dir=public_dir)
    hub_depth_result = validate_hub_content_depth_contract(root)
    approved_hub_minimum_result = validate_approved_hub_minimum_contract(root)
    seo_signal_conflict_result = validate_seo_signal_conflict_contract(content_dir)
    sitemap_canonical_result = validate_sitemap_canonical_contract(content_dir, public_dir)
    tier_contract_result = validate_tier_contract(content_dir)
    snapshot_single_source_result = validate_snapshot_single_source_contract(root)
    hub_loader_strict_result = validate_hub_loader_strict_contract(root)
    core_content_depth_result = validate_core_content_depth_contract(content_dir, as_of_date)
    statistical_feature_safety_result = validate_statistical_feature_safety_contract(content_dir, as_of_date)
    content_uniqueness_result = validate_content_uniqueness_contract(content_dir, as_of_date)
    narrative_distribution_result = validate_narrative_distribution_contract(content_dir, as_of_date)
    narrative_text_divergence_result = validate_narrative_text_divergence_contract(content_dir, as_of_date)
    core_page_trigger_coverage_result = validate_core_page_trigger_coverage_contract(content_dir, as_of_date)
    core_page_trigger_telemetry_result = validate_core_page_trigger_telemetry_contract(content_dir, as_of_date)

    for scope in [
        redirect_result,
        sitemap_result,
        route_filter_result,
        matrix_result,
        event_pool_result,
        cta_result,
        freshness_result,
        snapshot_freshness_result,
        conditional_sample_result,
        csv_contract_backfill_result,
        title_diversity_result,
        calendar_fetch_resilience_result,
        schema_breadcrumb_result,
        related_events_result,
        trust_layer_result,
        hub_briefs_result,
        crawl_policy_result,
        hub_route_result,
        hub_draft_noindex_result,
        blog_hub_link_result,
        lastmod_threshold_result,
        ymyl_regex_result,
        author_entity_result,
        about_page_result,
        hub_depth_result,
        seo_signal_conflict_result,
        sitemap_canonical_result,
        tier_contract_result,
        snapshot_single_source_result,
        hub_loader_strict_result,
        core_content_depth_result,
        statistical_feature_safety_result,
        content_uniqueness_result,
        narrative_text_divergence_result,
        core_page_trigger_coverage_result,
    ]:
        for issue in scope["violations"]:
            report["summary"][issue] = report["summary"].get(issue, 0) + 1

    report["violations"] = violations_by_file
    report["redirect_violations"] = redirect_result
    report["sitemap_violations"] = sitemap_result
    report["route_violations"] = route_filter_result
    report["matrix_violations"] = matrix_result
    report["event_pool_violations"] = event_pool_result
    report["cta_violations"] = cta_result
    report["freshness_violations"] = freshness_result
    report["snapshot_freshness_violations"] = snapshot_freshness_result
    report["conditional_sample_violations"] = conditional_sample_result
    report["csv_contract_backfill_violations"] = csv_contract_backfill_result
    report["title_diversity_violations"] = title_diversity_result
    report["calendar_fetch_resilience_violations"] = calendar_fetch_resilience_result
    report["schema_breadcrumb_violations"] = schema_breadcrumb_result
    report["related_events_violations"] = related_events_result
    report["trust_layer_violations"] = trust_layer_result
    report["hub_briefs_violations"] = hub_briefs_result
    report["crawl_policy_violations"] = crawl_policy_result
    report["hub_route_violations"] = hub_route_result
    report["hub_draft_noindex_violations"] = hub_draft_noindex_result
    report["blog_hub_link_violations"] = blog_hub_link_result
    report["lastmod_threshold_violations"] = lastmod_threshold_result
    report["ymyl_regex_violations"] = ymyl_regex_result
    report["author_entity_violations"] = author_entity_result
    report["about_page_violations"] = about_page_result
    report["hub_content_depth_violations"] = hub_depth_result
    report["seo_signal_conflict_violations"] = seo_signal_conflict_result
    report["sitemap_canonical_violations"] = sitemap_canonical_result
    report["tier_contract_violations"] = tier_contract_result
    report["snapshot_single_source_violations"] = snapshot_single_source_result
    report["hub_loader_strict_violations"] = hub_loader_strict_result
    report["core_content_depth_violations"] = core_content_depth_result
    report["statistical_feature_safety_violations"] = statistical_feature_safety_result
    report["content_uniqueness_violations"] = content_uniqueness_result
    report["narrative_distribution_violations"] = narrative_distribution_result
    report["narrative_text_divergence_violations"] = narrative_text_divergence_result
    report["core_page_trigger_coverage_violations"] = core_page_trigger_coverage_result
    report["core_page_trigger_telemetry_violations"] = core_page_trigger_telemetry_result
    report["approved_hub_minimum_contract"] = approved_hub_minimum_result
    report["warnings"] = {
        "cta": cta_result.get("warnings", []),
        "hub_route": hub_route_result.get("warnings", []),
        "approved_hub_minimum": approved_hub_minimum_result.get("warnings", []),
        "core_content_depth": core_content_depth_result.get("warnings", []),
        "content_uniqueness": content_uniqueness_result.get("warnings", []),
        "narrative_distribution": narrative_distribution_result.get("warnings", []),
        "core_page_trigger_telemetry": core_page_trigger_telemetry_result.get("warnings", []),
    }

    content_violations = sum(len(v) for v in violations_by_file.values())
    total_violations = (
        content_violations
        + int(redirect_result["count"])
        + int(sitemap_result["count"])
        + int(route_filter_result["count"])
        + int(matrix_result["count"])
        + int(event_pool_result["count"])
        + int(cta_result["count"])
        + int(freshness_result["count"])
        + int(snapshot_freshness_result["count"])
        + int(conditional_sample_result["count"])
        + int(csv_contract_backfill_result["count"])
        + int(title_diversity_result["count"])
        + int(calendar_fetch_resilience_result["count"])
        + int(schema_breadcrumb_result["count"])
        + int(related_events_result["count"])
        + int(trust_layer_result["count"])
        + int(hub_briefs_result["count"])
        + int(crawl_policy_result["count"])
        + int(hub_route_result["count"])
        + int(hub_draft_noindex_result["count"])
        + int(blog_hub_link_result["count"])
        + int(lastmod_threshold_result["count"])
        + int(ymyl_regex_result["count"])
        + int(author_entity_result["count"])
        + int(about_page_result["count"])
        + int(hub_depth_result["count"])
        + int(seo_signal_conflict_result["count"])
        + int(sitemap_canonical_result["count"])
        + int(tier_contract_result["count"])
        + int(snapshot_single_source_result["count"])
        + int(hub_loader_strict_result["count"])
        + int(core_content_depth_result["count"])
        + int(statistical_feature_safety_result["count"])
        + int(content_uniqueness_result["count"])
        + int(narrative_text_divergence_result["count"])
        + int(core_page_trigger_coverage_result["count"])
    )
    report["content_violations"] = content_violations
    report["total_violations"] = total_violations

    return report


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    content_dir = Path(args.content_dir).resolve() if args.content_dir else root / "src" / "content" / "blog"
    manifest_path = Path(args.manifest_path).resolve() if args.manifest_path else root / "data" / "page_manifest.json"
    public_dir = Path(args.public_dir).resolve() if args.public_dir else root / "public"
    slug_redirects_path = (
        Path(args.slug_redirects_path).resolve() if args.slug_redirects_path else root / "data" / "slug_redirects.json"
    )
    vercel_config_path = Path(args.vercel_config_path).resolve() if args.vercel_config_path else root / "vercel.json"
    offers_path = Path(args.offers_path).resolve() if args.offers_path else root / "src" / "data" / "offers.json"
    csv_path = Path(args.csv_path).resolve() if args.csv_path else root / "data" / "verified_targets.csv"
    db_path = Path(args.db_path).resolve() if args.db_path else root / "data" / "macro_events.db"
    index_path = Path(args.index_path).resolve() if args.index_path else root / "src" / "pages" / "index.astro"
    snapshot_path = Path(args.snapshot_path).resolve() if args.snapshot_path else root / "src" / "daily_snapshot.json"
    report_path = Path(args.report).resolve() if args.report else root / "logs" / "daily_ops" / "quality_gates.json"

    result = run_gates(
        root=root,
        content_dir=content_dir,
        as_of_date=args.as_of_date,
        manifest_path=manifest_path,
        public_dir=public_dir,
        slug_redirects_path=slug_redirects_path,
        vercel_config_path=vercel_config_path,
        offers_path=offers_path,
        csv_path=csv_path,
        db_path=db_path,
        index_path=index_path,
        snapshot_path=snapshot_path,
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    print(
        json.dumps(
            {
                "total_files": result["total_files"],
                "content_violations": result["content_violations"],
                "total_violations": result["total_violations"],
            },
            ensure_ascii=False,
        )
    )

    if args.strict and int(result["total_violations"]) > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
