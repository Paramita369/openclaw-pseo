#!/usr/bin/env python3
"""Single entrypoint for OpenClaw daily operations (fail-fast)."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Dict, List, Sequence

from pipeline_utils import ensure_dir, resolve_project_root


WHITELIST_PATHS = {
    "public/sitemap.xml",
    "src/daily_snapshot.json",
    "data/page_manifest.json",
    "data/slug_redirects.json",
    "vercel.json",
}
WHITELIST_PREFIXES = (
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run daily pSEO operations")
    parser.add_argument("--project-root", default=".", help="Repository root")
    parser.add_argument("--as-of-date", default=date.today().isoformat(), help="YYYY-MM-DD")
    parser.add_argument("--strict", action="store_true", help="Enable strict gates")
    parser.add_argument("--dry-run", action="store_true", help="Run without commit/push")
    parser.add_argument("--push", action="store_true", help="Commit and push if whitelist files changed")
    parser.add_argument("--max-pages", type=int, default=None, help="Max changed pages to regenerate")
    parser.add_argument("--with-backfill", action="store_true", help="Run history backfill step")
    parser.add_argument("--skip-build", action="store_true", help="Skip astro build")
    return parser.parse_args()


def run_step(name: str, cmd: Sequence[str], cwd: Path, required: bool = True) -> StepResult:
    start = utc_now()
    proc = subprocess.run(
        list(cmd),
        cwd=str(cwd),
        text=True,
        capture_output=True,
    )
    end = utc_now()

    result = StepResult(
        name=name,
        status="ok" if proc.returncode == 0 else ("failed" if required else "warn"),
        start_time=start.isoformat(),
        end_time=end.isoformat(),
        duration_ms=int((end - start).total_seconds() * 1000),
        command=list(cmd),
        returncode=proc.returncode,
        stdout=(proc.stdout or "")[-8000:],
        stderr=(proc.stderr or "")[-8000:],
    )

    if proc.returncode != 0 and required:
        raise RuntimeError(f"Step failed: {name} ({proc.returncode})")

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

    subprocess.run(
        [
            "git",
            "add",
            "src/content/blog",
            "public/sitemap.xml",
            "src/daily_snapshot.json",
            "data/page_manifest.json",
            "data/slug_redirects.json",
            "vercel.json",
        ],
        cwd=str(root),
        check=True,
    )
    staged_check = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=str(root))
    if staged_check.returncode == 0:
        return {"status": "nothing_staged", "changed": changed, "ignored_runtime_changes": ignored}

    message = f"chore: daily data sync {as_of_date}"
    subprocess.run(["git", "commit", "-m", message], cwd=str(root), check=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=str(root), check=True)

    return {"status": "pushed", "changed": changed, "ignored_runtime_changes": ignored, "message": message}


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)

    python = sys.executable
    log_dir = root / "logs" / "daily_ops"
    ensure_dir(log_dir)
    log_path = log_dir / f"{args.as_of_date}.json"

    run_log: Dict[str, object] = {
        "date": args.as_of_date,
        "generated_at": utc_now().isoformat(),
        "project_root": str(root),
        "strict": args.strict,
        "dry_run": args.dry_run,
        "push": args.push,
        "steps": [],
        "status": "running",
    }

    steps: List[StepResult] = []
    try:

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
                [python, "scripts/macro_pipeline/fetch_daily_snapshot.py", "--project-root", str(root)],
                cwd=root,
                required=True,
            )
        )

        source_db = root / "data" / "macro_events.db"
        runtime_db_dir = log_dir / "runtime"
        ensure_dir(runtime_db_dir)
        runtime_db = runtime_db_dir / "macro_events.runtime.db"
        if source_db.exists():
            shutil.copy2(source_db, runtime_db)
        else:
            raise RuntimeError(f"Missing source DB: {source_db}")

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
        ]
        if args.strict:
            build_cmd.append("--strict")
        if args.max_pages is not None:
            build_cmd.extend(["--max-pages", str(args.max_pages)])

        steps.append(run_step("generate_pages", build_cmd, cwd=root, required=True))

        gate_cmd = [
            python,
            "scripts/macro_pipeline/quality_gates.py",
            "--project-root",
            str(root),
            "--report",
            str(log_dir / f"quality_{args.as_of_date}.json"),
        ]
        if args.strict:
            gate_cmd.append("--strict")
        steps.append(run_step("quality_gates", gate_cmd, cwd=root, required=True))

        if not args.skip_build:
            steps.append(run_step("astro_build", ["npm", "run", "build"], cwd=root, required=True))

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

        if args.push:
            git_result = commit_and_push(root=root, as_of_date=args.as_of_date, dry_run=args.dry_run)
        else:
            git_result = {"status": "push_disabled"}

        run_log["git"] = git_result
        run_log["status"] = "ok"

    except Exception as exc:
        run_log["steps"] = [step.__dict__ for step in steps]
        run_log["status"] = "failed"
        run_log["error"] = str(exc)
    finally:
        if "steps" not in run_log or not run_log["steps"]:
            run_log["steps"] = [step.__dict__ for step in steps]
        run_log["finished_at"] = utc_now().isoformat()
        log_path.write_text(json.dumps(run_log, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"📝 Daily ops log: {log_path}")

    if run_log.get("status") != "ok":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
