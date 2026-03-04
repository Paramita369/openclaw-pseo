# QuantMacro V2 (OpenClaw-First)

QuantMacro is a static-first pSEO system on Vercel focused on event-driven probabilities for `CPI`, `NFP`, and `FOMC`.

## Core Positioning
- Visual-first dashboard with clear 3-step operating flow.
- Article first fold is probability-first (`P(up)`, `P(down)`, median return, sample size).
- Daily OpenClaw operations with fail-fast gates and controlled push.
- Monetization via config-driven affiliate CTA (no hardcoded links in markdown body).

## Daily Command (OpenClaw)
```bash
python3 scripts/macro_pipeline/run_daily_ops.py --project-root . --strict --push
```

Skip remote crawler contract check when needed:
```bash
python3 scripts/macro_pipeline/run_daily_ops.py --project-root . --strict --push --skip-crawl-check
```

Skip content accuracy contract only for emergency debugging (not daily standard):
```bash
python3 scripts/macro_pipeline/run_daily_ops.py --project-root . --strict --push --skip-accuracy-check
```

## Daily SOP / SKILL
- Human SOP: `ops/openclaw_daily_sop.md`
- OpenClaw Skill: `ops/skills/openclaw-daily-ops/SKILL.md`

## GitHub Actions Backup (Manual Only)
- Workflow: `Daily QuantMacro Update`
- Trigger: `Actions -> Daily QuantMacro Update -> Run workflow`
- Schedule: disabled (no daily cron)
- Command executed by workflow:
```bash
python3 scripts/macro_pipeline/run_daily_ops.py --project-root . --strict --push
```
- Expected behavior:
  - If whitelisted files changed, workflow commits and pushes.
  - If no whitelisted change, workflow exits cleanly without push.

## Python Dependencies
```bash
pip install -r requirements.txt
```

## Pipeline Steps
1. Fetch market snapshot
2. Sync event calendar (`FRED + override`) and backfill missing macro event rows
3. Copy DB to runtime workspace
4. Fetch event outcomes (`vs_previous`) from FRED
5. Build full target matrix (`5 assets × all CPI/NFP/FOMC dates`)
6. Compute risk metrics
7. Generate event pages + redirects + segmented sitemaps (core/assets/events/playbooks/blog)
8. Run strict quality gates
9. Run full content accuracy audit (`content_accuracy_check`, strict = full sweep)
10. Run `astro build`
11. Run crawler access contract check (`Googlebot` + `Google-Extended`)
12. Generate KPI report
13. Commit/push only whitelisted paths

## Git Whitelist
- `src/content/blog/`
- `public/robots.txt`
- `public/sitemap*.xml`
- `src/daily_snapshot.json`
- `data/page_manifest.json`
- `data/slug_redirects.json`
- `data/verified_targets.csv`
- `data/event_overrides.csv`
- `vercel.json`

Runtime noisy paths are ignored during push checks:
- `data/macro_events.db` / `data/macro_events.db-journal`
- `node_modules/`, `.astro/`, `dist/`

## V2 Contracts
### CSV Contract (`data/verified_targets.csv`)
Required base columns:
- `asset,event_type,date,url_slug,title,impact_t1_pct,impact_t7_pct,volatility,sharpe_t7,mdd_t7,intent,source`

V2 extension columns:
- `event_label,event_slug,rise_prob_t1,fall_prob_t1,rise_prob_t7,fall_prob_t7,median_t1_pct,median_t7_pct,sample_size,asof_date,freshness_days,signal`
- `conditional_sample_size,title_variant_id,title_template_key`
- `event_direction,event_actual,event_previous,event_delta,direction_basis,outcome_status`

### Frontmatter Contract
Required fields include:
- `event_type,event_label,event_slug,event_date,asof_date`
- `event_direction,event_actual,event_previous,event_delta,direction_basis`
- `signal,confidence_level,sample_size`
- `title_variant_id,title_template_key`
- `freshness_days`
- `metrics` numeric block
- `probabilities` block (`t1`, `t7`, `conditional`, `sample_size`)

### Snapshot Contract (`src/daily_snapshot.json`)
Per-asset required fields:
- `asset_type` (`crypto|us_session`)
- `as_of_date`
- `as_of_ts`
- `freshness_status` (`fresh|stale|fallback|calendar_unknown`)
- `data_age_hours`
- `source`

### Redirect Outputs
- `data/slug_redirects.json` (legacy slug -> new event slug)
- `vercel.json` `redirects` synced as 301

## Environment Variables
- `MINIMAX_API_KEY` (optional): LLM narrative enrichment.
- `FRED_API_KEY` (optional): preferred for outcome fetch quota.
- `PUBLIC_GA4_MEASUREMENT_ID` (optional): frontend GA4 events.
- `GA4_PROPERTY_ID` (optional): KPI report (`affiliate_click`).
- `GOOGLE_APPLICATION_CREDENTIALS` + `GSC_SITE_URL` (optional): GSC metrics.

## Quality Gates (strict)
Run with:
```bash
python3 scripts/macro_pipeline/quality_gates.py --project-root . --strict
```

Strict failures include:
- `After Macro Events` literal still present
- invalid `event_type` (must be `CPI/NFP/FOMC`)
- missing frontmatter v2 fields
- probability sum mismatch (`up + down != 100 ± 0.01`)
- confidence/sample mismatch (`sample_size < 5` must be `low`)
- embedded affiliate URL in markdown body
- redirect map integrity issues
- sitemap containing legacy macro slugs
- missing segmented sitemap index (`sitemap-index.xml` + sub-sitemaps)
- missing playbook sitemap chunk (`sitemap-playbooks.xml`)
- non-full target matrix coverage (must match DB event-date matrix)
- missing/invalid event outcome direction fields
- stale event pool (`event_calendar`) for CPI/NFP/FOMC (>90 days)
- missing QQQ/SPY CTA route contract (`primary=IBKR`, `secondary includes Futu`)
- stale semantic mismatch (homepage should switch to `Latest Event Playbook` when data is old)
- crawler policy mismatch (`robots.txt`/`vercel.json` blocks `Google-Extended` or sets global blocking `X-Robots-Tag`)
- missing Hub route contract (`/playbooks/{asset}/{event}` + trust layer + sitemap coverage)
- snapshot freshness contract failure (schema/status/UI as-of mismatch)
- conditional sample contract failure (CSV/frontmatter mismatch or all-zero anomaly)
- title diversity contract failure (per-event template spread + LCS similarity)
- calendar fetch resilience contract failure (retry/backoff/evidence markers missing)

## Accuracy Audit (strict full sweep)
Run directly:
```bash
python3 scripts/ops/content_accuracy_check.py --project-root . --as-of-date 2026-03-03 --strict --full-sweep
```

Report output:
- `logs/daily_ops/content_accuracy_<YYYY-MM-DD>.json`

## Notes
- `run_daily_ops` is the primary operation path; GitHub Actions is manual backup only.
- Educational content only, not investment advice.

## Search Console Operations
- Submit only `https://quantmacro.vercel.app/sitemap.xml` (index entrypoint).
- Remove duplicate failed sitemap submissions before re-submit.
- Use URL Inspection -> Test live URL for:
  - `/`
  - `/leaderboard`
  - one representative `/blog/{slug}`
