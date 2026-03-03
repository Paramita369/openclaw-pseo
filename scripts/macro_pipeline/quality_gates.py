#!/usr/bin/env python3
"""Quality gates for generated blog content, matrix completeness, and sitemap integrity."""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sqlite3
from datetime import date, datetime, timezone
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run quality gates")
    parser.add_argument("--project-root", default=None, help="Repository root")
    parser.add_argument("--content-dir", default=None, help="Content directory")
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

    for field in ["quality_score", "sample_size", "event_actual", "event_previous", "event_delta"]:
        if field in fm and not is_finite_number(fm.get(field)):
            violations.append(f"non_numeric_{field}")

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


def validate_redirects(root: Path) -> Dict[str, object]:
    violations: List[str] = []

    slug_redirects_path = root / "data" / "slug_redirects.json"
    vercel_path = root / "vercel.json"

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


def validate_sitemap(root: Path) -> Dict[str, object]:
    violations: List[str] = []

    index_path = root / "public" / "sitemap-index.xml"
    core_path = root / "public" / "sitemap-core.xml"
    assets_path = root / "public" / "sitemap-assets.xml"
    events_path = root / "public" / "sitemap-events.xml"
    blog_paths = sorted((root / "public").glob("sitemap-blog-*.xml"))

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
    if assets_path.exists() and "/tags/" not in assets_path.read_text(encoding="utf-8"):
        violations.append("assets_sitemap_missing_tags")
    if events_path.exists() and "/events/" not in events_path.read_text(encoding="utf-8"):
        violations.append("events_sitemap_missing_event_routes")

    return {"violations": sorted(set(violations)), "count": len(sorted(set(violations)))}


def validate_filter_routes(root: Path) -> Dict[str, object]:
    violations: List[str] = []
    for path in list((root / "src" / "pages").rglob("*.astro")) + list((root / "src" / "layouts").rglob("*.astro")):
        text = path.read_text(encoding="utf-8")
        if "/blog?asset=" in text:
            violations.append(f"legacy_asset_query_filter:{path.relative_to(root)}")

    return {"violations": violations, "count": len(violations)}


def validate_target_matrix(root: Path, as_of_date: str) -> Dict[str, object]:
    violations: List[str] = []

    csv_path = root / "data" / "verified_targets.csv"
    db_path = root / "data" / "macro_events.db"

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

    if duplicate_count > 0:
        violations.append("duplicate_target_rows")

    as_of_cutoff = cutoff_date(as_of_date)
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        expected_dates: Dict[str, List[str]] = {}
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


def run_gates(root: Path, content_dir: Path, as_of_date: str) -> Dict[str, object]:
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

    redirect_result = validate_redirects(root)
    sitemap_result = validate_sitemap(root)
    route_filter_result = validate_filter_routes(root)
    matrix_result = validate_target_matrix(root, as_of_date)

    for scope in [redirect_result, sitemap_result, route_filter_result, matrix_result]:
        for issue in scope["violations"]:
            report["summary"][issue] = report["summary"].get(issue, 0) + 1

    report["violations"] = violations_by_file
    report["redirect_violations"] = redirect_result
    report["sitemap_violations"] = sitemap_result
    report["route_violations"] = route_filter_result
    report["matrix_violations"] = matrix_result

    content_violations = sum(len(v) for v in violations_by_file.values())
    total_violations = (
        content_violations
        + int(redirect_result["count"])
        + int(sitemap_result["count"])
        + int(route_filter_result["count"])
        + int(matrix_result["count"])
    )
    report["content_violations"] = content_violations
    report["total_violations"] = total_violations

    return report


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    content_dir = Path(args.content_dir).resolve() if args.content_dir else root / "src" / "content" / "blog"
    report_path = Path(args.report).resolve() if args.report else root / "logs" / "daily_ops" / "quality_gates.json"

    result = run_gates(root, content_dir, args.as_of_date)
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
