#!/usr/bin/env python3
"""Single entrypoint for OpenClaw daily operations (fail-fast)."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Sequence

from pipeline_utils import ensure_dir, resolve_project_root


WHITELIST_PATHS = {
    "public/robots.txt",
    "src/daily_snapshot.json",
    "data/page_manifest.json",
    "data/slug_redirects.json",
    "data/verified_targets.csv",
    "data/event_overrides.csv",
    "vercel.json",
}
WHITELIST_PREFIXES = (
    "public/sitemap",
    "src/content/blog/",
)
IGNORED_RUNTIME_PATHS = {
    "data/macro_events.db",
    "data/macro_events.db-journal",
}
IGNORED_RUNTIME_PREFIXES = (
    "node_modules/",
    ".astro/",
    "dist/",
)
CURRENT_STEP_LOGS_DIR: Optional[Path] = None


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class StepResult:
    name: str
    status: str
    start_time: str
    end_time: str
    duration_ms: int
    command: List[str]
    returncode: int
    stdout: str
    stderr: str
    stdout_path: Optional[str] = None
    stderr_path: Optional[str] = None


class StepExecutionError(RuntimeError):
    def __init__(self, result: StepResult):
        self.result = result
        super().__init__(f"Step failed: {result.name} ({result.returncode})")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run daily pSEO operations")
    parser.add_argument("--project-root", default=".", help="Repository root")
    parser.add_argument("--as-of-date", default=date.today().isoformat(), help="YYYY-MM-DD")
    parser.add_argument("--strict", action="store_true", help="Enable strict gates")
    parser.add_argument("--dry-run", action="store_true", help="Run without commit/push")
    parser.add_argument("--push", action="store_true", help="Commit and push if whitelist files changed")
    parser.add_argument("--max-pages", type=int, default=None, help="Max changed pages to regenerate")
    parser.add_argument("--full", action="store_true", help="Force full content regeneration")
    parser.add_argument("--with-backfill", action="store_true", help="Run history backfill step")
    parser.add_argument("--skip-build", action="store_true", help="Skip astro build")
    parser.add_argument("--skip-crawl-check", action="store_true", help="Skip remote crawler accessibility check")
    parser.add_argument("--skip-accuracy-check", action="store_true", help="Skip content accuracy contract check")
    parser.add_argument("--runtime-root", default=None, help="Override runtime output root for dry-run")
    return parser.parse_args()


def run_step(name: str, cmd: Sequence[str], cwd: Path, required: bool = True) -> StepResult:
    global CURRENT_STEP_LOGS_DIR
    start = utc_now()
    proc = subprocess.run(
        list(cmd),
        cwd=str(cwd),
        text=True,
        capture_output=True,
    )
    end = utc_now()
    stdout_text = proc.stdout or ""
    stderr_text = proc.stderr or ""
    stdout_path: Optional[str] = None
    stderr_path: Optional[str] = None
    if CURRENT_STEP_LOGS_DIR is not None:
        ensure_dir(CURRENT_STEP_LOGS_DIR)
        safe_name = re.sub(r"[^a-zA-Z0-9_.-]+", "_", name).strip("_") or "step"
        stdout_file = CURRENT_STEP_LOGS_DIR / f"{safe_name}.stdout.log"
        stderr_file = CURRENT_STEP_LOGS_DIR / f"{safe_name}.stderr.log"
        stdout_file.write_text(stdout_text, encoding="utf-8")
        stderr_file.write_text(stderr_text, encoding="utf-8")
        stdout_path = str(stdout_file)
        stderr_path = str(stderr_file)

    result = StepResult(
        name=name,
        status="ok" if proc.returncode == 0 else ("failed" if required else "warn"),
        start_time=start.isoformat(),
        end_time=end.isoformat(),
        duration_ms=int((end - start).total_seconds() * 1000),
        command=list(cmd),
        returncode=proc.returncode,
        stdout=stdout_text[-8000:],
        stderr=stderr_text[-8000:],
        stdout_path=stdout_path,
        stderr_path=stderr_path,
    )

    if proc.returncode != 0 and required:
        raise StepExecutionError(result)

    return result


def list_changed_files(root: Path) -> List[str]:
    proc = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=str(root),
        text=True,
        capture_output=True,
        check=True,
    )
    files: List[str] = []
    for line in proc.stdout.splitlines():
        if not line:
            continue
        # porcelain: XY <path>
        path = line[3:].strip()
        if " -> " in path:
            path = path.split(" -> ", 1)[1].strip()
        files.append(path)
    return files


def is_whitelisted(path: str) -> bool:
    if path in WHITELIST_PATHS:
        return True
    return any(path.startswith(prefix) for prefix in WHITELIST_PREFIXES)


def is_ignored_runtime_change(path: str) -> bool:
    if path in IGNORED_RUNTIME_PATHS:
        return True
    return any(path.startswith(prefix) for prefix in IGNORED_RUNTIME_PREFIXES)


def assert_no_tracked_changes(root: Path, baseline: Sequence[str]) -> None:
    baseline_set = {path for path in baseline if not is_ignored_runtime_change(path)}
    changed = [path for path in list_changed_files(root) if not is_ignored_runtime_change(path)]
    introduced = sorted(path for path in changed if path not in baseline_set)
    if introduced:
        raise RuntimeError(f"Dry-run produced tracked changes: {introduced}")


def commit_and_push(root: Path, as_of_date: str, dry_run: bool) -> Dict[str, object]:
    all_changed = list_changed_files(root)
    ignored = [path for path in all_changed if is_ignored_runtime_change(path)]
    changed = [path for path in all_changed if not is_ignored_runtime_change(path)]
    if not changed:
        return {"status": "no_changes", "changed": [], "ignored_runtime_changes": ignored}

    outside = [path for path in changed if not is_whitelisted(path)]
    if outside:
        raise RuntimeError(f"Detected non-whitelisted changes: {outside}")

    if dry_run:
        return {"status": "dry_run", "changed": changed, "ignored_runtime_changes": ignored}

    staged_paths = [path for path in changed if is_whitelisted(path)]
    if not staged_paths:
        return {"status": "nothing_whitelisted", "changed": changed, "ignored_runtime_changes": ignored}

    subprocess.run(["git", "add", *staged_paths], cwd=str(root), check=True)
    staged_check = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=str(root))
    if staged_check.returncode == 0:
        return {"status": "nothing_staged", "changed": changed, "ignored_runtime_changes": ignored}

    message = f"chore: daily data sync {as_of_date}"
    subprocess.run(["git", "commit", "-m", message], cwd=str(root), check=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=str(root), check=True)

    return {"status": "pushed", "changed": changed, "ignored_runtime_changes": ignored, "message": message}


def validate_playbooks_sitemap(public_dir: Path) -> None:
    sitemap_path = public_dir / "sitemap-playbooks.xml"
    if not sitemap_path.exists():
        raise RuntimeError(f"Post-build gate failed: missing {sitemap_path}")
    content = sitemap_path.read_text(encoding="utf-8").strip()
    if "<urlset" not in content or "</urlset>" not in content:
        raise RuntimeError("Post-build gate failed: sitemap-playbooks.xml malformed envelope")
    try:
        ET.fromstring(content)
    except Exception as exc:
        raise RuntimeError(f"Post-build gate failed: invalid sitemap-playbooks.xml ({exc})") from exc


def classify_error_code(step_name: str) -> str:
    mapping = {
        "content_accuracy_check": "ACCURACY_MISMATCH",
        "fetch_event_outcomes": "OUTCOMES_SYNC_FAILED",
        "quality_gates": "QUALITY_GATES_FAILED",
    }
    return mapping.get(step_name, "PIPELINE_STEP_FAILED")


def recommended_action(step_name: str) -> str:
    mapping = {
        "content_accuracy_check": (
            "Inspect content_accuracy report mismatches, regenerate affected pages, and rerun strict dry-run."
        ),
        "fetch_event_outcomes": (
            "Check source/runtime DB write consistency for event_outcomes and resolve transaction failure."
        ),
        "quality_gates": "Resolve strict quality gate violations before rerunning live ops.",
    }
    return mapping.get(step_name, "Inspect failing step stderr and rerun from strict dry-run.")


def build_incident(
    *,
    step_name: str,
    error_text: str,
    evidence_candidates: Sequence[Optional[Path]],
) -> Dict[str, object]:
    evidence_paths = [str(path) for path in evidence_candidates if path and path.exists()]
    return {
        "failure_step": step_name,
        "error_code": classify_error_code(step_name),
        "evidence_paths": evidence_paths,
        "recommended_action": recommended_action(step_name),
        "error": error_text,
    }


def main() -> None:
    global CURRENT_STEP_LOGS_DIR
    args = parse_args()
    root = resolve_project_root(args.project_root)
    if args.push and args.dry_run:
        raise SystemExit("--push cannot be used together with --dry-run")
    baseline_changes = list_changed_files(root) if args.dry_run else []

    python = sys.executable
    log_dir = root / "logs" / "daily_ops"
    ensure_dir(log_dir)
    log_path = log_dir / f"{args.as_of_date}.json"
    runtime_root = (
        Path(args.runtime_root).expanduser().resolve()
        if args.runtime_root
        else (log_dir / "runtime" / f"{args.as_of_date}_{utc_now().strftime('%H%M%S')}")
    )
    run_id = f"{args.as_of_date}_{utc_now().strftime('%H%M%S')}"
    if args.dry_run:
        ensure_dir(runtime_root)
        step_logs_dir = runtime_root / "steps"
    else:
        step_logs_dir = log_dir / "runtime" / run_id / "steps"
    ensure_dir(step_logs_dir)
    CURRENT_STEP_LOGS_DIR = step_logs_dir

    run_log: Dict[str, object] = {
        "date": args.as_of_date,
        "generated_at": utc_now().isoformat(),
        "project_root": str(root),
        "runtime_root": str(runtime_root if args.dry_run else root),
        "strict": args.strict,
        "dry_run": args.dry_run,
        "push": args.push,
        "steps": [],
        "status": "running",
        "git": {"status": "not_started"},
    }

    steps: List[StepResult] = []
    quality_report_path: Optional[Path] = None
    crawl_report_path: Optional[Path] = None
    accuracy_report_path: Optional[Path] = None
    try:
        source_db = root / "data" / "macro_events.db"
        if not source_db.exists():
            raise RuntimeError(f"Missing source DB: {source_db}")

        if args.dry_run:
            runtime_db = runtime_root / "data" / "macro_events.runtime.db"
            ensure_dir(runtime_db.parent)
            shutil.copy2(source_db, runtime_db)
            sync_db = runtime_db
            snapshot_output = runtime_root / "src" / "daily_snapshot.json"
            targets_output = runtime_root / "data" / "verified_targets.csv"
            content_output = runtime_root / "src" / "content" / "blog"
            manifest_output = runtime_root / "data" / "page_manifest.json"
            public_output = runtime_root / "public"
            slug_redirects_output = runtime_root / "data" / "slug_redirects.json"
            vercel_output = runtime_root / "vercel.json"
            quality_report_path = runtime_root / "logs" / f"quality_{args.as_of_date}.json"
            crawl_report_path = runtime_root / "logs" / f"crawl_access_{args.as_of_date}.json"
            accuracy_report_path = runtime_root / "logs" / f"content_accuracy_{args.as_of_date}.json"
            if (root / "vercel.json").exists():
                ensure_dir(vercel_output.parent)
                shutil.copy2(root / "vercel.json", vercel_output)
            source_snapshot = root / "src" / "daily_snapshot.json"
            if source_snapshot.exists():
                ensure_dir(snapshot_output.parent)
                shutil.copy2(source_snapshot, snapshot_output)
        else:
            sync_db = source_db
            runtime_db_dir = log_dir / "runtime"
            ensure_dir(runtime_db_dir)
            runtime_db = runtime_db_dir / f"macro_events.{run_id}.runtime.db"
            snapshot_output = root / "src" / "daily_snapshot.json"
            targets_output = root / "data" / "verified_targets.csv"
            content_output = root / "src" / "content" / "blog"
            manifest_output = root / "data" / "page_manifest.json"
            public_output = root / "public"
            slug_redirects_output = root / "data" / "slug_redirects.json"
            vercel_output = root / "vercel.json"
            quality_report_path = log_dir / f"quality_{args.as_of_date}.json"
            crawl_report_path = log_dir / f"crawl_access_{args.as_of_date}.json"
            accuracy_report_path = log_dir / f"content_accuracy_{args.as_of_date}.json"

        if args.with_backfill:
            steps.append(
                run_step(
                    "history_backfill",
                    [python, "scripts/macro_pipeline/history_backfill.py", "--project-root", str(root)],
                    cwd=root,
                    required=False,
                )
            )

        steps.append(
            run_step(
                "fetch_snapshot",
                [
                    python,
                    "scripts/macro_pipeline/fetch_daily_snapshot.py",
                    "--project-root",
                    str(root),
                    "--output-path",
                    str(snapshot_output),
                ],
                cwd=root,
                required=True,
            )
        )

        steps.append(
            run_step(
                "sync_event_calendar",
                [
                    python,
                    "scripts/macro_pipeline/sync_event_calendar.py",
                    "--project-root",
                    str(root),
                    "--db-path",
                    str(sync_db),
                    "--as-of-date",
                    args.as_of_date,
                    "--override-file",
                    str(root / "data" / "event_overrides.csv"),
                    *(["--strict"] if args.strict else []),
                ],
                cwd=root,
                required=True,
            )
        )

        if not args.dry_run:
            shutil.copy2(source_db, runtime_db)

        steps.append(
            run_step(
                "fetch_event_outcomes",
                [
                    python,
                    "scripts/macro_pipeline/fetch_event_outcomes.py",
                    "--project-root",
                    str(root),
                    "--db-path",
                    str(runtime_db),
                    "--source-db-path",
                    str(runtime_db if args.dry_run else source_db),
                    "--as-of-date",
                    args.as_of_date,
                    *(["--strict"] if args.strict else []),
                ],
                cwd=root,
                required=True,
            )
        )

        steps.append(
            run_step(
                "build_target_matrix",
                [
                    python,
                    "scripts/macro_pipeline/build_target_matrix.py",
                    "--project-root",
                    str(root),
                    "--db-path",
                    str(runtime_db),
                    "--output",
                    str(targets_output),
                    "--as-of-date",
                    args.as_of_date,
                    *(["--strict"] if args.strict else []),
                ],
                cwd=root,
                required=True,
            )
        )

        steps.append(
            run_step(
                "risk_metrics",
                [
                    python,
                    "scripts/macro_pipeline/risk_metrics_calculator.py",
                    "--project-root",
                    str(root),
                    "--db-path",
                    str(runtime_db),
                ],
                cwd=root,
                required=True,
            )
        )

        build_cmd = [
            python,
            "scripts/macro_pipeline/astro_page_builder.py",
            "--project-root",
            str(root),
            "--as-of-date",
            args.as_of_date,
            "--db-path",
            str(runtime_db),
            "--csv-path",
            str(targets_output),
            "--output-dir",
            str(content_output),
            "--manifest-path",
            str(manifest_output),
            "--public-dir",
            str(public_output),
            "--slug-redirects-path",
            str(slug_redirects_output),
            "--vercel-config-path",
            str(vercel_output),
        ]
        if args.strict:
            build_cmd.append("--strict")
        if args.full:
            build_cmd.append("--full")
        if args.max_pages is not None:
            build_cmd.extend(["--max-pages", str(args.max_pages)])

        steps.append(run_step("generate_pages", build_cmd, cwd=root, required=True))

        gate_cmd = [
            python,
            "scripts/macro_pipeline/quality_gates.py",
            "--project-root",
            str(root),
            "--content-dir",
            str(content_output),
            "--report",
            str(quality_report_path),
            "--as-of-date",
            args.as_of_date,
            "--manifest-path",
            str(manifest_output),
            "--public-dir",
            str(public_output),
            "--slug-redirects-path",
            str(slug_redirects_output),
            "--vercel-config-path",
            str(vercel_output),
            "--csv-path",
            str(targets_output),
            "--db-path",
            str(runtime_db),
            "--snapshot-path",
            str(snapshot_output),
        ]
        if args.strict:
            gate_cmd.append("--strict")
        steps.append(run_step("quality_gates", gate_cmd, cwd=root, required=True))

        if not args.skip_accuracy_check:
            accuracy_cmd = [
                python,
                "scripts/ops/content_accuracy_check.py",
                "--project-root",
                str(root),
                "--as-of-date",
                args.as_of_date,
                "--db-path",
                str(runtime_db),
                "--csv-path",
                str(targets_output),
                "--content-dir",
                str(content_output),
                "--report",
                str(accuracy_report_path),
            ]
            if args.strict:
                accuracy_cmd.append("--strict")
            steps.append(run_step("content_accuracy_check", accuracy_cmd, cwd=root, required=True))

        if not args.skip_build:
            steps.append(run_step("astro_build", ["npm", "run", "build"], cwd=root, required=True))
            validate_playbooks_sitemap(public_output)
            steps.append(
                StepResult(
                    name="post_build_sitemap_playbooks_gate",
                    status="ok",
                    start_time=utc_now().isoformat(),
                    end_time=utc_now().isoformat(),
                    duration_ms=0,
                    command=["internal:validate_playbooks_sitemap", str(public_output / "sitemap-playbooks.xml")],
                    returncode=0,
                    stdout="validated sitemap-playbooks.xml",
                    stderr="",
                    stdout_path=None,
                    stderr_path=None,
                )
            )

        if not args.skip_crawl_check:
            crawl_cmd = [
                python,
                "scripts/ops/crawl_access_check.py",
                "--base-url",
                "https://quantmacro.vercel.app",
                "--report",
                str(crawl_report_path),
            ]
            if args.strict:
                crawl_cmd.append("--strict")
            steps.append(
                run_step(
                    "crawl_access_check",
                    crawl_cmd,
                    cwd=root,
                    required=bool(args.strict),
                )
            )

        steps.append(
            run_step(
                "kpi_report",
                [
                    python,
                    "scripts/macro_pipeline/kpi_report.py",
                    "--project-root",
                    str(root),
                    "--report-date",
                    args.as_of_date,
                ],
                cwd=root,
                required=False,
            )
        )

        if args.dry_run:
            assert_no_tracked_changes(root, baseline_changes)
            git_result = {"status": "dry_run_clean", "runtime_root": str(runtime_root)}
        elif args.push:
            git_result = commit_and_push(root=root, as_of_date=args.as_of_date, dry_run=args.dry_run)
        else:
            git_result = {"status": "push_disabled"}

        run_log["git"] = git_result
        run_log["status"] = "ok"

    except StepExecutionError as exc:
        steps.append(exc.result)
        incident = build_incident(
            step_name=exc.result.name,
            error_text=str(exc),
            evidence_candidates=[
                Path(exc.result.stderr_path) if exc.result.stderr_path else None,
                Path(exc.result.stdout_path) if exc.result.stdout_path else None,
                quality_report_path,
                accuracy_report_path,
                crawl_report_path,
            ],
        )
        run_log["incident"] = incident
        run_log["steps"] = [step.__dict__ for step in steps]
        run_log["status"] = "failed"
        run_log["error"] = str(exc)
        if exc.result.name == "content_accuracy_check":
            run_log["git"] = {"status": "blocked_by_accuracy"}
        else:
            run_log["git"] = {"status": "blocked"}
        evidence = ",".join(incident["evidence_paths"]) if incident["evidence_paths"] else "none"
        print("PAUSE_CONTRACT_TRIGGERED")
        print(f"STEP={incident['failure_step']}")
        print(f"EVIDENCE={evidence}")
    except Exception as exc:
        incident = build_incident(
            step_name="runtime_precheck",
            error_text=str(exc),
            evidence_candidates=[quality_report_path, accuracy_report_path, crawl_report_path],
        )
        run_log["incident"] = incident
        run_log["steps"] = [step.__dict__ for step in steps]
        run_log["status"] = "failed"
        run_log["error"] = str(exc)
        run_log["git"] = {"status": "blocked"}
        evidence = ",".join(incident["evidence_paths"]) if incident["evidence_paths"] else "none"
        print("PAUSE_CONTRACT_TRIGGERED")
        print("STEP=runtime_precheck")
        print(f"EVIDENCE={evidence}")
    finally:
        if "steps" not in run_log or not run_log["steps"]:
            run_log["steps"] = [step.__dict__ for step in steps]
        run_log["finished_at"] = utc_now().isoformat()
        log_path.write_text(json.dumps(run_log, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"📝 Daily ops log: {log_path}")
        CURRENT_STEP_LOGS_DIR = None

    if run_log.get("status") != "ok":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
