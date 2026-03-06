#!/usr/bin/env python3
"""Full-sweep content accuracy audit for generated blog pages."""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sqlite3
import statistics
import sys
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None

try:
    from scripts.macro_pipeline.pipeline_utils import cutoff_date, event_filter_sql, parse_float, resolve_project_root
    from scripts.macro_pipeline.content_features import CORE_WINDOW_DAYS, compute_statistical_features, is_core_page_for_window
except Exception:  # pragma: no cover
    CURRENT_FILE = Path(__file__).resolve()
    sys.path.insert(0, str(CURRENT_FILE.parents[1] / "macro_pipeline"))
    from pipeline_utils import cutoff_date, event_filter_sql, parse_float, resolve_project_root
    from content_features import CORE_WINDOW_DAYS, compute_statistical_features, is_core_page_for_window

EVENT_FRESHNESS_THRESHOLDS = {
    "CPI": 45,
    "NFP": 45,
    "FOMC": 90,
}

FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


@dataclass
class DistributionRow:
    event_date: str
    impact_t1_pct: Optional[float]
    impact_t7_pct: Optional[float]
    event_direction: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate generated blog accuracy against DB and CSV contracts")
    parser.add_argument("--project-root", default=".", help="Repository root")
    parser.add_argument("--as-of-date", default=date.today().isoformat(), help="Run date (YYYY-MM-DD)")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when mismatches exist")
    parser.add_argument("--full-sweep", action="store_true", help="Check all pages")
    parser.add_argument("--sample-size", type=int, default=20, help="Pages checked when not full sweep")
    parser.add_argument("--report", default=None, help="Report JSON path")
    parser.add_argument("--content-dir", default=None, help="Override blog content directory")
    parser.add_argument("--csv-path", default=None, help="Override verified_targets.csv path")
    parser.add_argument("--db-path", default=None, help="Override macro_events.db path")
    return parser.parse_args()


def read_frontmatter(path: Path) -> Dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(raw)
    if not match:
        return {}
    if yaml is not None:
        loaded = yaml.safe_load(match.group(1))
        if isinstance(loaded, dict):
            return loaded
    fallback = parse_frontmatter_fallback(match.group(1))
    if isinstance(fallback, dict):
        return fallback
    return {}


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


def parse_frontmatter_fallback(frontmatter_text: str) -> Dict[str, Any]:
    root: Dict[str, Any] = {}
    stack: List[Tuple[int, Dict[str, Any]]] = [(-1, root)]

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
            nested: Dict[str, Any] = {}
            current[key] = nested
            stack.append((indent, nested))
            continue

        current[key] = parse_scalar(value)

    return root


def table_exists(conn: sqlite3.Connection, table_name: str) -> bool:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name = ? LIMIT 1",
        (table_name,),
    )
    return bool(cursor.fetchone())


def probability_window(values: Sequence[float]) -> Dict[str, float]:
    if not values:
        return {"up": 0.0, "down": 100.0, "median": 0.0, "mean": 0.0, "sample": 0}

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


def as_float(value: Any, default: Optional[float] = None) -> Optional[float]:
    return parse_float(value, default)


def is_close(a: Any, b: Any, tolerance: float = 0.01) -> bool:
    left = as_float(a)
    right = as_float(b)
    if left is None or right is None:
        return left is None and right is None
    return math.isfinite(left) and math.isfinite(right) and abs(left - right) <= tolerance


def load_csv_index(csv_path: Path) -> Dict[str, Dict[str, str]]:
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        index: Dict[str, Dict[str, str]] = {}
        for row in reader:
            slug = str(row.get("url_slug") or "").strip()
            if slug:
                index[slug] = row
    return index


def fetch_distribution(
    conn: sqlite3.Connection,
    *,
    asset: str,
    event_type: str,
    asof_date: str,
    has_outcomes: bool,
) -> List[DistributionRow]:
    cursor = conn.cursor()
    if has_outcomes:
        cursor.execute(
            f"""
            SELECT
              m.date AS event_date,
              AVG(a.impact_t1_pct) AS impact_t1_pct,
              AVG(a.impact_t7_pct) AS impact_t7_pct,
              MAX(eo.direction) AS event_direction
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
            (event_type.upper(), asset.upper(), asof_date),
        )
        fetched = cursor.fetchall()
    else:
        cursor.execute(
            f"""
            SELECT
              m.date AS event_date,
              AVG(a.impact_t1_pct) AS impact_t1_pct,
              AVG(a.impact_t7_pct) AS impact_t7_pct,
              'unknown' AS event_direction
            FROM asset_impact a
            JOIN macro_events m ON a.event_id = m.event_id
            WHERE a.ticker = ?
              AND m.date <= ?
              AND {event_filter_sql(event_type)}
            GROUP BY m.date
            ORDER BY m.date ASC
            """,
            (asset.upper(), asof_date),
        )
        fetched = cursor.fetchall()

    rows: List[DistributionRow] = []
    for event_date, impact_t1, impact_t7, event_direction in fetched:
        rows.append(
            DistributionRow(
                event_date=str(event_date),
                impact_t1_pct=parse_float(impact_t1),
                impact_t7_pct=parse_float(impact_t7),
                event_direction=str(event_direction or "unknown").lower(),
            )
        )
    return rows


def expected_freshness_status(event_type: str, freshness_days: int) -> str:
    threshold = int(EVENT_FRESHNESS_THRESHOLDS.get(event_type.upper(), 45))
    return "stale" if freshness_days > threshold else "fresh"


def add_mismatch(mismatches: List[Dict[str, Any]], slug: str, code: str, details: str) -> None:
    mismatches.append({"slug": slug, "code": code, "details": details})


def validate_page(
    *,
    path: Path,
    frontmatter: Dict[str, Any],
    csv_row: Optional[Dict[str, str]],
    conn: sqlite3.Connection,
    has_outcomes: bool,
    default_asof_cutoff: str,
    run_as_of_date: str,
    known_slugs: Sequence[str],
) -> List[Dict[str, Any]]:
    slug = path.stem
    mismatches: List[Dict[str, Any]] = []
    event_type = str(frontmatter.get("event_type") or "").strip().upper()
    event_date = str(frontmatter.get("event_date") or "").strip()
    asof_date = str(frontmatter.get("asof_date") or default_asof_cutoff).strip()
    asset = slug.split("-after-", 1)[0].upper()

    if not event_type:
        add_mismatch(mismatches, slug, "missing_event_type", "frontmatter.event_type is missing")
        return mismatches
    if not event_date:
        add_mismatch(mismatches, slug, "missing_event_date", "frontmatter.event_date is missing")
        return mismatches

    if csv_row is None:
        add_mismatch(mismatches, slug, "missing_csv_row", "No row found in verified_targets.csv")
        csv_conditional_size = None
    else:
        csv_event_type = str(csv_row.get("event_type") or "").strip().upper()
        csv_date = str(csv_row.get("date") or "").strip()
        csv_slug = str(csv_row.get("url_slug") or "").strip()
        csv_conditional_size = parse_float(csv_row.get("conditional_sample_size"))
        if csv_slug != slug:
            add_mismatch(mismatches, slug, "csv_slug_mismatch", f"csv={csv_slug} page={slug}")
        if csv_event_type != event_type:
            add_mismatch(mismatches, slug, "csv_event_type_mismatch", f"csv={csv_event_type} fm={event_type}")
        if csv_date != event_date:
            add_mismatch(mismatches, slug, "csv_event_date_mismatch", f"csv={csv_date} fm={event_date}")
        if csv_conditional_size is None:
            add_mismatch(
                mismatches,
                slug,
                "csv_conditional_sample_invalid",
                f"conditional_sample_size={csv_row.get('conditional_sample_size')}",
            )

    probabilities = frontmatter.get("probabilities")
    if not isinstance(probabilities, dict):
        add_mismatch(mismatches, slug, "missing_probabilities", "frontmatter.probabilities is missing or invalid")
        return mismatches

    for key in ("t1", "t7"):
        window = probabilities.get(key)
        if not isinstance(window, dict):
            add_mismatch(mismatches, slug, f"missing_{key}_window", f"probabilities.{key} missing")
            continue
        up = parse_float(window.get("up"))
        down = parse_float(window.get("down"))
        if up is None or down is None:
            add_mismatch(mismatches, slug, f"non_numeric_{key}", f"probabilities.{key}.up/down not numeric")
            continue
        if abs((up + down) - 100.0) > 0.01:
            add_mismatch(
                mismatches,
                slug,
                f"probability_sum_mismatch_{key}",
                f"probabilities.{key} up+down={up + down:.4f}",
            )

    distribution_rows = fetch_distribution(
        conn,
        asset=asset,
        event_type=event_type,
        asof_date=asof_date,
        has_outcomes=has_outcomes,
    )
    t1_values = [float(row.impact_t1_pct) for row in distribution_rows if row.impact_t1_pct is not None]
    t7_values = [float(row.impact_t7_pct) for row in distribution_rows if row.impact_t7_pct is not None]
    t1_expected = probability_window(t1_values)
    t7_expected = probability_window(t7_values)

    for metric_key in ("up", "down", "median"):
        actual_t1 = ((probabilities.get("t1") or {}) if isinstance(probabilities.get("t1"), dict) else {}).get(metric_key)
        actual_t7 = ((probabilities.get("t7") or {}) if isinstance(probabilities.get("t7"), dict) else {}).get(metric_key)
        if not is_close(actual_t1, t1_expected[metric_key]):
            add_mismatch(
                mismatches,
                slug,
                f"db_t1_{metric_key}_mismatch",
                f"expected={t1_expected[metric_key]} actual={actual_t1}",
            )
        if not is_close(actual_t7, t7_expected[metric_key]):
            add_mismatch(
                mismatches,
                slug,
                f"db_t7_{metric_key}_mismatch",
                f"expected={t7_expected[metric_key]} actual={actual_t7}",
            )

    event_direction = str(frontmatter.get("event_direction") or "").strip().lower()
    conditional_block = probabilities.get("conditional")
    fm_conditional_size = (
        parse_float(conditional_block.get("sample_size"))
        if isinstance(conditional_block, dict)
        else None
    )
    if fm_conditional_size is None:
        add_mismatch(mismatches, slug, "frontmatter_conditional_sample_invalid", "probabilities.conditional.sample_size")
    if csv_conditional_size is not None and fm_conditional_size is not None:
        if abs(float(csv_conditional_size) - float(fm_conditional_size)) > 0.01:
            add_mismatch(
                mismatches,
                slug,
                "csv_frontmatter_conditional_sample_mismatch",
                f"csv={csv_conditional_size} fm={fm_conditional_size}",
            )

    if has_outcomes and event_direction in {"up", "down", "flat"}:
        conditional_t1_values = [
            float(row.impact_t1_pct)
            for row in distribution_rows
            if row.impact_t1_pct is not None and row.event_direction == event_direction
        ]
        conditional_t7_values = [
            float(row.impact_t7_pct)
            for row in distribution_rows
            if row.impact_t7_pct is not None and row.event_direction == event_direction
        ]
        conditional_expected_t1 = probability_window(conditional_t1_values)
        conditional_expected_t7 = probability_window(conditional_t7_values)
        conditional = conditional_block
        if isinstance(conditional, dict):
            for metric_key in ("up", "down", "median"):
                actual_c_t1 = (
                    (conditional.get("t1") or {}) if isinstance(conditional.get("t1"), dict) else {}
                ).get(metric_key)
                actual_c_t7 = (
                    (conditional.get("t7") or {}) if isinstance(conditional.get("t7"), dict) else {}
                ).get(metric_key)
                if not is_close(actual_c_t1, conditional_expected_t1[metric_key]):
                    add_mismatch(
                        mismatches,
                        slug,
                        f"db_conditional_t1_{metric_key}_mismatch",
                        f"expected={conditional_expected_t1[metric_key]} actual={actual_c_t1}",
                    )
                if not is_close(actual_c_t7, conditional_expected_t7[metric_key]):
                    add_mismatch(
                        mismatches,
                        slug,
                        f"db_conditional_t7_{metric_key}_mismatch",
                        f"expected={conditional_expected_t7[metric_key]} actual={actual_c_t7}",
                    )
            expected_conditional_size = float(
                min(conditional_expected_t1["sample"], conditional_expected_t7["sample"])
            )
            if fm_conditional_size is not None and abs(float(fm_conditional_size) - expected_conditional_size) > 0.01:
                add_mismatch(
                    mismatches,
                    slug,
                    "db_conditional_sample_size_mismatch",
                    f"expected={expected_conditional_size} actual={fm_conditional_size}",
                )
            if csv_conditional_size is not None and abs(float(csv_conditional_size) - expected_conditional_size) > 0.01:
                add_mismatch(
                    mismatches,
                    slug,
                    "db_csv_conditional_sample_size_mismatch",
                    f"expected={expected_conditional_size} csv={csv_conditional_size}",
                )

    baseline_t7_values = [row.impact_t7_pct for row in distribution_rows if row.impact_t7_pct is not None]
    metrics_block = frontmatter.get("metrics") if isinstance(frontmatter.get("metrics"), dict) else {}
    expected_features = compute_statistical_features(metrics_block.get("impact_t7_pct"), baseline_t7_values)
    fm_is_core_page = frontmatter.get("is_core_page")
    expected_is_core_page = is_core_page_for_window(
        event_date=event_date,
        as_of_date=run_as_of_date,
        canonical_target=str(frontmatter.get("canonical_target", "")).lower(),
        robots_directive=str(frontmatter.get("robots_directive", "")).lower(),
        in_blog_sitemap=bool(frontmatter.get("in_blog_sitemap")),
        window_days=CORE_WINDOW_DAYS,
    )
    if not isinstance(fm_is_core_page, bool) or fm_is_core_page != expected_is_core_page:
        add_mismatch(
            mismatches,
            slug,
            "core_page_flag_mismatch",
            f"expected={expected_is_core_page} actual={fm_is_core_page}",
        )
    core_window_days = frontmatter.get("core_window_days")
    try:
        parsed_core_window = int(float(core_window_days or 0))
    except Exception:
        parsed_core_window = 0
    if parsed_core_window != CORE_WINDOW_DAYS:
        add_mismatch(
            mismatches,
            slug,
            "core_window_days_mismatch",
            f"expected={CORE_WINDOW_DAYS} actual={core_window_days}",
        )
    for field_name, expected_value in [
        ("hub_baseline_mean_t7", expected_features.baseline_mean_t7),
        ("hub_baseline_median_t7", expected_features.baseline_median_t7),
        ("hub_baseline_std_t7", expected_features.baseline_std_t7),
        ("hub_baseline_delta", expected_features.hub_baseline_delta),
        ("z_score_t7", expected_features.z_score_t7),
        ("percentile_t7", expected_features.percentile_t7),
    ]:
        if not is_close(frontmatter.get(field_name), expected_value):
            add_mismatch(
                mismatches,
                slug,
                f"{field_name}_mismatch",
                f"expected={expected_value} actual={frontmatter.get(field_name)}",
            )
    if str(frontmatter.get("narrative_trigger") or "").strip() != expected_features.narrative_trigger:
        add_mismatch(
            mismatches,
            slug,
            "narrative_trigger_mismatch",
            f"expected={expected_features.narrative_trigger} actual={frontmatter.get('narrative_trigger')}",
        )

    try:
        asof_dt = datetime.strptime(asof_date, "%Y-%m-%d").date()
        event_dt = datetime.strptime(event_date, "%Y-%m-%d").date()
        expected_freshness_days = max((asof_dt - event_dt).days, 0)
        fm_freshness_days = int(float(frontmatter.get("freshness_days", 0)))
        if fm_freshness_days != expected_freshness_days:
            add_mismatch(
                mismatches,
                slug,
                "freshness_days_mismatch",
                f"expected={expected_freshness_days} actual={fm_freshness_days}",
            )
        expected_status = expected_freshness_status(event_type, expected_freshness_days)
        actual_status = str(frontmatter.get("freshness_status") or "").strip().lower()
        if actual_status != expected_status:
            add_mismatch(
                mismatches,
                slug,
                "freshness_status_mismatch",
                f"expected={expected_status} actual={actual_status}",
            )
    except Exception as exc:
        add_mismatch(mismatches, slug, "freshness_parse_error", str(exc))

    related_events = frontmatter.get("related_events")
    if related_events is None:
        related_events = []
    if not isinstance(related_events, list):
        add_mismatch(mismatches, slug, "related_events_invalid_type", "related_events should be an array")
    else:
        if len(related_events) > 3:
            add_mismatch(mismatches, slug, "related_events_too_many", f"count={len(related_events)}")
        known_slug_set = set(known_slugs)
        for item in related_events:
            if not isinstance(item, dict):
                add_mismatch(mismatches, slug, "related_events_item_invalid", f"item={item}")
                continue
            related_slug = str(item.get("slug") or "").strip()
            if not related_slug:
                add_mismatch(mismatches, slug, "related_events_missing_slug", "related event missing slug")
                continue
            if related_slug == slug:
                add_mismatch(mismatches, slug, "related_events_self_link", related_slug)
            if related_slug not in known_slug_set:
                add_mismatch(mismatches, slug, "related_events_slug_not_found", related_slug)

    return mismatches


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    content_dir = Path(args.content_dir).resolve() if args.content_dir else root / "src" / "content" / "blog"
    csv_path = Path(args.csv_path).resolve() if args.csv_path else root / "data" / "verified_targets.csv"
    db_path = Path(args.db_path).resolve() if args.db_path else root / "data" / "macro_events.db"

    if args.strict and not args.full_sweep:
        args.full_sweep = True

    report_path = (
        Path(args.report).resolve()
        if args.report
        else (root / "logs" / "daily_ops" / f"content_accuracy_{args.as_of_date}.json")
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)

    if not content_dir.exists():
        raise SystemExit(f"Content directory not found: {content_dir}")
    if not csv_path.exists():
        raise SystemExit(f"CSV path not found: {csv_path}")
    if not db_path.exists():
        raise SystemExit(f"DB path not found: {db_path}")

    csv_index = load_csv_index(csv_path)
    all_files = sorted(content_dir.glob("*.md"))
    selected_files = all_files if args.full_sweep else all_files[: max(args.sample_size, 0)]
    known_slugs = [path.stem for path in all_files]
    default_asof_cutoff = cutoff_date(args.as_of_date)

    conn = sqlite3.connect(db_path)
    has_outcomes = table_exists(conn, "event_outcomes")

    mismatches: List[Dict[str, Any]] = []
    checked_pages = 0
    try:
        for path in selected_files:
            frontmatter = read_frontmatter(path)
            page_mismatches = validate_page(
                path=path,
                frontmatter=frontmatter,
                csv_row=csv_index.get(path.stem),
                conn=conn,
                has_outcomes=has_outcomes,
                default_asof_cutoff=default_asof_cutoff,
                run_as_of_date=args.as_of_date,
                known_slugs=known_slugs,
            )
            checked_pages += 1
            mismatches.extend(page_mismatches)
    finally:
        conn.close()

    unique_slugs = sorted({item["slug"] for item in mismatches})
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "as_of_date": args.as_of_date,
        "strict": bool(args.strict),
        "full_sweep": bool(args.full_sweep),
        "db_path": str(db_path),
        "csv_path": str(csv_path),
        "content_dir": str(content_dir),
        "total_pages": len(all_files),
        "checked_pages": checked_pages,
        "mismatch_count": len(mismatches),
        "pages_with_mismatch": len(unique_slugs),
        "top_mismatches": mismatches[:100],
        "fatal": bool(args.strict and mismatches),
    }
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print(
        json.dumps(
            {
                "checked_pages": checked_pages,
                "mismatch_count": len(mismatches),
                "pages_with_mismatch": len(unique_slugs),
                "report": str(report_path),
            },
            ensure_ascii=False,
        )
    )

    if args.strict and mismatches:
        raise SystemExit(f"content accuracy mismatches detected: {len(mismatches)}")


if __name__ == "__main__":
    main()
