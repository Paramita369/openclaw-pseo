# QuantMacro OpenClaw Daily SOP (V2.6R)

## 1. Purpose
Daily fail-fast operations for QuantMacro with audit evidence.  
Primary path: OpenClaw local run.  
Backup path: manual GitHub workflow dispatch only.

## 2. Daily SLA
- Target completion window: <= 20 minutes
- If failed: publish incident summary within 30 minutes

## 3. Preflight Checklist (Required)
- [ ] Current branch is `main`
- [ ] `git status` has no unexpected tracked changes
- [ ] Python dependencies installed: `pip install -r requirements.txt`
- [ ] Node dependencies installed: `npm ci`
- [ ] Network reachable (FRED + site domain)
- [ ] Disk has free space for runtime logs/build artifacts

## 4. Step A: Strict Dry Run (Required)
```bash
python3 scripts/macro_pipeline/run_daily_ops.py --project-root . --strict --dry-run
```

Pass criteria:
- Exit code `0`
- No pause contract output
- `logs/daily_ops/<YYYY-MM-DD>.json` status is `ok`
- `git status` remains clean (except ignored runtime files)

## 5. Step B: Strict Live Run (If A passed)
```bash
python3 scripts/macro_pipeline/run_daily_ops.py --project-root . --strict --push
```

Pass criteria:
- Exit code `0`
- `git.status` in run log is `pushed`, `no_changes`, or `push_disabled`
- No `PAUSE_CONTRACT_TRIGGERED`

## 6. Mandatory Post-Checks
- [ ] `quality_total_violations == 0`  
  Check file: `logs/daily_ops/quality_<YYYY-MM-DD>.json`
- [ ] `accuracy_mismatch_count == 0`  
  Check file: `logs/daily_ops/content_accuracy_<YYYY-MM-DD>.json`
- [ ] Crawl contract is healthy  
  Check file: `logs/daily_ops/crawl_access_<YYYY-MM-DD>.json`
- [ ] `public/sitemap.xml` includes `sitemap-playbooks.xml`
- [ ] Spot check 2 draft hubs show `noindex,follow`

## 7. Incident Playbook (Pause Contract)
If terminal shows:
- `PAUSE_CONTRACT_TRIGGERED`
- `STEP=<...>`
- `EVIDENCE=<...>`

Then do all actions below:
1. Stop pipeline immediately (no retries with `--push`).
2. Open evidence JSON files from `EVIDENCE`.
3. Record incident block fields:
   - `failure_step`
   - `error_code`
   - `recommended_action`
4. Fix root cause.
5. Re-run strict dry-run first.
6. Only run live push after dry-run is green.

## 8. Frequent Failure Modes
1. `STEP=content_accuracy_check`
- Meaning: generated content does not match DB/CSV contracts.
- Action: open `content_accuracy_<date>.json`, fix mismatched pages/data, rerun.

2. `STEP=fetch_event_outcomes`
- Meaning: source/runtime `event_outcomes` sync inconsistency or write failure.
- Action: inspect DB paths and consistency stats in step output; rerun after DB fix.

3. `STEP=quality_gates`
- Meaning: one or more strict contracts failed.
- Action: open `quality_<date>.json`, resolve all violations.

## 9. Standard Daily Summary Template
```text
Run Status: OK|FAILED
Date: YYYY-MM-DD
Quality Violations: <n>
Accuracy Mismatches: <n>
Crawl Contract: OK|FAILED
Push Result: pushed|no_changes|blocked
Next Action: <one-line action>
```
