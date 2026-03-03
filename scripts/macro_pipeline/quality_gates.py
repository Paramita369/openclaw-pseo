#!/usr/bin/env python3
"""Quality gates for generated blog content."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

from pipeline_utils import resolve_project_root


REQUIRED_FRONTMATTER_KEYS = [
    "event_type",
    "source",
    "offer_key",
    "quality_score",
    "metrics:",
]

CTA_HEADING_PATTERN = re.compile(r"^##\s+(Quantitative Action Plan|Actionable Insight)", flags=re.MULTILINE | re.IGNORECASE)
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


def frontmatter_block(content: str) -> str:
    match = re.match(r"^---\n(.*?)\n---\n", content, flags=re.DOTALL)
    return match.group(1) if match else ""


def scan_file(path: Path) -> List[str]:
    content = path.read_text(encoding="utf-8")
    violations: List[str] = []

    if "nan%" in content.lower() or " nan" in content.lower():
        violations.append("contains_nan")
    if "|--------|-------||" in content:
        violations.append("broken_markdown_table")
    if "💡 Actionable Insight" in content:
        violations.append("legacy_embedded_cta")
    if "reacting to **Macro** macro events" in content:
        violations.append("legacy_macro_literal")
    if len(CTA_HEADING_PATTERN.findall(content)) > 1:
        violations.append("duplicate_cta")
    if EMBEDDED_AFFILIATE_PATTERN.search(content):
        violations.append("embedded_affiliate_link")

    fm = frontmatter_block(content)
    if not fm:
        violations.append("missing_frontmatter")
        return violations

    for key in REQUIRED_FRONTMATTER_KEYS:
        if key not in fm:
            violations.append(f"missing_{key.rstrip(':')}")

    if re.search(r"event_type:\s*\"?MACRO\"?", fm):
        violations.append("event_type_generic_macro")

    # numeric metric fields must be concrete values (no null/string)
    for field in ["sharpe_t7", "mdd_t7", "volatility", "impact_t1_pct", "impact_t7_pct", "quality_score"]:
        matcher = re.search(rf"{field}:\s*([^\n]+)", fm)
        if not matcher:
            continue
        value = matcher.group(1).strip().strip('"').strip("'")
        try:
            float(value)
        except ValueError:
            violations.append(f"non_numeric_{field}")

    return violations


def run_gates(content_dir: Path) -> Dict[str, object]:
    files = sorted(content_dir.glob("*.md"))
    report: Dict[str, object] = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_files": len(files),
        "violations": {},
        "summary": {
            "contains_nan": 0,
            "broken_markdown_table": 0,
            "legacy_embedded_cta": 0,
            "legacy_macro_literal": 0,
            "duplicate_cta": 0,
            "embedded_affiliate_link": 0,
            "missing_frontmatter": 0,
            "event_type_generic_macro": 0,
        },
    }

    violations: Dict[str, List[str]] = {}
    for path in files:
        file_violations = scan_file(path)
        if not file_violations:
            continue
        violations[path.name] = file_violations
        for issue in file_violations:
            report["summary"][issue] = report["summary"].get(issue, 0) + 1

    report["violations"] = violations
    report["total_violations"] = sum(len(v) for v in violations.values())
    return report


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    content_dir = Path(args.content_dir).resolve() if args.content_dir else root / "src" / "content" / "blog"
    report_path = Path(args.report).resolve() if args.report else root / "logs" / "daily_ops" / "quality_gates.json"

    result = run_gates(content_dir)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    print(json.dumps({"total_files": result["total_files"], "total_violations": result["total_violations"]}, ensure_ascii=False))

    if args.strict and result["total_violations"] > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
