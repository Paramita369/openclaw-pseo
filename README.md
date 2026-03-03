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

## Python Dependencies
```bash
pip install -r requirements.txt
```

## Pipeline Steps
1. Fetch market snapshot
2. Copy DB to runtime workspace and compute risk metrics
3. Generate event pages + redirects + sitemap
4. Run strict quality gates
5. Run `astro build`
6. Generate KPI report
7. Commit/push only whitelisted paths

## Git Whitelist
- `src/content/blog/`
- `public/sitemap.xml`
- `src/daily_snapshot.json`
- `data/page_manifest.json`
- `data/slug_redirects.json`
- `vercel.json`

Runtime noisy paths are ignored during push checks:
- `data/macro_events.db` / `data/macro_events.db-journal`
- `node_modules/`, `.astro/`, `dist/`

## V2 Contracts
### CSV Contract (`data/verified_targets.csv`)
Required base columns:
- `asset,event_type,date,url_slug,title,impact_t1_pct,impact_t7_pct,volatility,sharpe_t7,mdd_t7,intent,source`

V2 extension columns:
- `event_label,event_slug,rise_prob_t1,fall_prob_t1,rise_prob_t7,fall_prob_t7,median_t1_pct,median_t7_pct,sample_size,asof_date,signal`

### Frontmatter Contract
Required fields include:
- `event_type,event_label,event_slug,event_date,asof_date`
- `signal,confidence_level,sample_size`
- `metrics` numeric block
- `probabilities` block (`t1`, `t7`, `sample_size`)

### Redirect Outputs
- `data/slug_redirects.json` (legacy slug -> new event slug)
- `vercel.json` `redirects` synced as 301

## Environment Variables
- `MINIMAX_API_KEY` (optional): LLM narrative enrichment.
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

## Notes
- `run_daily_ops` is the primary operation path; GitHub Actions is backup/manual.
- Educational content only, not investment advice.
