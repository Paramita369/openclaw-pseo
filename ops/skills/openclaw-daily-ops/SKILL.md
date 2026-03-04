# OpenClaw Daily Ops Skill (QuantMacro V2.7R)

## Skill Intent
Execute daily QuantMacro operations in fail-fast mode with evidence-first reporting.

## Required Inputs
- `as_of_date` (YYYY-MM-DD)
- `strict` (default `true`)
- `push` (`true` for live, `false` for dry-run)

## Safety Contracts
1. If `--dry-run` and `--push` are both requested: hard fail.
2. If git has non-whitelist tracked changes: stop and report.
3. If pause contract triggers: stop immediately and report evidence paths.

## Execution Flow
1. Preflight
- Validate current branch and `git status`
- Confirm dependencies (`pip`, `npm`)

2. Dry-run (always first)
```bash
python3 scripts/macro_pipeline/run_daily_ops.py --project-root . --as-of-date <as_of_date> --strict --dry-run
```

3. Live-run (only if dry-run passed and `push=true`)
```bash
python3 scripts/macro_pipeline/run_daily_ops.py --project-root . --as-of-date <as_of_date> --strict --push
```

4. Post-check
- Read latest:
  - `logs/daily_ops/<as_of_date>.json`
  - `logs/daily_ops/quality_<as_of_date>.json`
  - `logs/daily_ops/content_accuracy_<as_of_date>.json`
  - `logs/daily_ops/crawl_access_<as_of_date>.json` (if enabled)
- Confirm:
  - quality violations `0`
  - accuracy mismatches `0`
  - snapshot freshness contract passed
  - conditional sample contract passed
  - title diversity contract passed
  - calendar fetch resilience contract passed
  - crawl check `0` violations
  - sitemap entrypoint remains healthy

## Output Template
```text
Run Status: OK|FAILED
Data Freshness: <fresh|latest/stale summary>
Accuracy Result: mismatches=<n>, checked_pages=<n>
SEO Crawlability Result: violations=<n>
Push Result: pushed|no_changes|blocked|dry_run_clean
Next Action: <one line>
```

## Pause Contract Handling
When output contains `PAUSE_CONTRACT_TRIGGERED`:
- Report:
  - `STEP=<failure_step>`
  - `EVIDENCE=<comma-separated paths>`
- Do not continue to push.
- Recommend rerunning strict dry-run after fix.
