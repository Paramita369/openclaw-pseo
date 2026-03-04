# QuantMacro OpenClaw Daily SOP (V2.7R)

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
- [ ] Source DB exists or can be bootstrapped: `var/data/macro_events.db`
- [ ] Source DB health check:
  - `sqlite3 var/data/macro_events.db \"PRAGMA integrity_check;\"` -> `ok`
  - `sqlite3 var/data/macro_events.db \"SELECT COUNT(1) FROM event_outcomes;\"` -> non-error

## 4. Step A: Strict Dry Run (Required)
```bash
python3 scripts/macro_pipeline/run_daily_ops.py \
  --project-root . \
  --strict \
  --dry-run \
  --source-db-path var/data/macro_events.db \
  --bootstrap-if-missing \
  --seed-db-path data/macro_events.db
```

Pass criteria:
- Exit code `0`
- No pause contract output
- `logs/daily_ops/<YYYY-MM-DD>.json` status is `ok`
- `git status` remains clean (except ignored runtime files)

## 5. Step B: Strict Live Run (If A passed)
```bash
python3 scripts/macro_pipeline/run_daily_ops.py \
  --project-root . \
  --strict \
  --push \
  --source-db-path var/data/macro_events.db \
  --bootstrap-if-missing \
  --seed-db-path data/macro_events.db
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
- [ ] `snapshot_freshness_contract` passed (no stale false alarm on non-trading days)
- [ ] `conditional_sample_contract` passed (CSV/frontmatter aligned, not all zero)
- [ ] `title_diversity_contract` passed (>=3 templates/event, max share <=50%, LCS gate pass)
- [ ] `calendar_fetch_resilience_contract` passed (retry/backoff + evidence markers present)
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
- Action: inspect step stderr/stdout evidence logs; if FRED fetch failed, confirm fallback reuse and retry on next run.

3. `STEP=quality_gates`
- Meaning: one or more strict contracts failed.
- Action: open `quality_<date>.json`, resolve all violations.

4. `STEP=fetch_snapshot`
- Meaning: market snapshot source unavailable or stale logic contract broken.
- Action: validate `src/daily_snapshot.json` schema (`as_of_date/as_of_ts/asset_type/freshness_status`) and rerun.

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
