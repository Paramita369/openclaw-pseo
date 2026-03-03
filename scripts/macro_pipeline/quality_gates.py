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

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None

REQUIRED_FRONTMATTER_KEYS = [
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
    "metrics",
    "probabilities",
    "event_direction",
    "event_actual",
    "event_previous",
    "event_delta",
    "direction_basis",
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
    "asof_date",
    "freshness_days",
    "signal",
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


def is_finite_number(value: object) -> bool:
    try:
        number = float(value)
        return math.isfinite(number)
    except Exception:
        return False


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

    for field in ["quality_score", "sample_size", "freshness_days", "event_actual", "event_previous", "event_delta"]:
        if field in fm and not is_finite_number(fm.get(field)):
            violations.append(f"non_numeric_{field}")

    freshness_state = str(fm.get("freshness_status", "")).lower()
    if freshness_state not in {"fresh", "stale"}:
        violations.append("invalid_freshness_status")

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
    if not blog_paths:
        violations.append("missing_sitemap_blog")

    index_content = index_path.read_text(encoding="utf-8")
    for name in ["sitemap-core.xml", "sitemap-assets.xml", "sitemap-events.xml"]:
        if name not in index_content:
            violations.append(f"sitemap_index_missing_{name.replace('.xml', '')}")
    if "sitemap-blog-" not in index_content:
        violations.append("sitemap_index_missing_blog_chunk")

    for sitemap_file in [index_path, core_path, assets_path, events_path, *blog_paths]:
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
            "/blog": "0.85",
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

    for scope in [
        redirect_result,
        sitemap_result,
        route_filter_result,
        matrix_result,
        event_pool_result,
        cta_result,
        freshness_result,
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
    report["warnings"] = {"cta": cta_result.get("warnings", [])}

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
