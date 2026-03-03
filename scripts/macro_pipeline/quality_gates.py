#!/usr/bin/env python3
"""Quality gates for generated blog content and redirect integrity."""

from __future__ import annotations

import argparse
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

from pipeline_utils import ALLOWED_EVENT_TYPES, resolve_project_root

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
]

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
    return parser.parse_args()


def extract_frontmatter(content: str) -> Dict[str, object]:
    match = re.match(r"^---\n(.*?)\n---\n", content, flags=re.DOTALL)
    if not match:
        return {}
    if yaml is None:
        return {}
    try:
        loaded = yaml.safe_load(match.group(1))
    except Exception:
        return {}
    return loaded if isinstance(loaded, dict) else {}


def is_finite_number(value: object) -> bool:
    try:
        number = float(value)
        return math.isfinite(number)
    except Exception:
        return False


def validate_probability_block(block: object) -> Tuple[bool, List[str]]:
    if not isinstance(block, dict):
        return False, ["invalid_probabilities_object"]

    violations: List[str] = []
    sample_size = block.get("sample_size")
    if not isinstance(sample_size, int) or sample_size < 0:
        violations.append("invalid_probabilities_sample_size")

    for key in ["t1", "t7"]:
        window = block.get(key)
        if not isinstance(window, dict):
            violations.append(f"missing_probabilities_{key}")
            continue

        for field in ["up", "down", "median", "mean", "sample"]:
            if field not in window:
                violations.append(f"missing_probabilities_{key}_{field}")

        up = window.get("up")
        down = window.get("down")
        if not is_finite_number(up) or not is_finite_number(down):
            violations.append(f"non_numeric_probabilities_{key}_up_down")
        else:
            total = float(up) + float(down)
            if abs(total - 100.0) > 0.01:
                violations.append(f"probability_sum_not_100_{key}")

        for field in ["median", "mean", "sample"]:
            if field in window and not is_finite_number(window.get(field)):
                violations.append(f"non_numeric_probabilities_{key}_{field}")

    return len(violations) == 0, violations


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
        return violations

    for key in REQUIRED_FRONTMATTER_KEYS:
        if key not in fm:
            violations.append(f"missing_{key}")

    event_type = str(fm.get("event_type", "")).upper()
    if event_type not in ALLOWED_EVENT_TYPES:
        violations.append("event_type_not_allowed")

    for field in ["quality_score", "sample_size"]:
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

    # cycle detection on blog redirects
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

    return {
        "violations": sorted(set(violations)),
        "count": len(sorted(set(violations))),
    }


def validate_sitemap(root: Path) -> Dict[str, object]:
    violations: List[str] = []
    sitemap_path = root / "public" / "sitemap.xml"

    if not sitemap_path.exists():
        violations.append("missing_sitemap")
        return {"violations": violations, "count": len(violations)}

    content = sitemap_path.read_text(encoding="utf-8")
    if re.search(r"/blog/[a-z0-9-]*after-macro-[0-9]{4}-[0-9]{2}-[0-9]{2}", content):
        violations.append("sitemap_contains_legacy_macro_slug")

    return {"violations": violations, "count": len(violations)}


def run_gates(root: Path, content_dir: Path) -> Dict[str, object]:
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

    for issue in redirect_result["violations"]:
        report["summary"][issue] = report["summary"].get(issue, 0) + 1
    for issue in sitemap_result["violations"]:
        report["summary"][issue] = report["summary"].get(issue, 0) + 1

    report["violations"] = violations_by_file
    report["redirect_violations"] = redirect_result
    report["sitemap_violations"] = sitemap_result

    content_violations = sum(len(v) for v in violations_by_file.values())
    total_violations = content_violations + int(redirect_result["count"]) + int(sitemap_result["count"])
    report["content_violations"] = content_violations
    report["total_violations"] = total_violations

    return report


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    content_dir = Path(args.content_dir).resolve() if args.content_dir else root / "src" / "content" / "blog"
    report_path = Path(args.report).resolve() if args.report else root / "logs" / "daily_ops" / "quality_gates.json"

    result = run_gates(root, content_dir)
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
