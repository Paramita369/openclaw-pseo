# QuantMacro pSEO Platform (OpenClaw-First)

Static-first pSEO architecture on Vercel, with local daily automation driven by OpenClaw.

## Core Principles
- Static pages (`/blog/{slug}`) for low-cost SEO scale.
- Daily incremental generation (no noisy full rebuild by default).
- Strict quality gates (fail-fast, no push on critical issues).
- Monetization-first via affiliate links, tracked with GA4 events.

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
2. Copy DB to runtime workspace and compute risk metrics (no repo DB mutation)
3. Generate changed pages + sitemap
4. Run quality gates
5. Run `astro build`
6. Generate KPI report (GA4 + GSC)
7. Commit/push only whitelisted paths

## Git Whitelist
- `src/content/blog/`
- `public/sitemap.xml`
- `src/daily_snapshot.json`
- `data/page_manifest.json`

Runtime-only noisy paths are ignored by push checks:
- `data/macro_events.db` / `data/macro_events.db-journal`
- `node_modules/`, `.astro/`, `dist/`

## Configuration
- Affiliate offers: `config/offers.yaml`
- Frontend offer data mirror: `src/data/offers.json`
- Page increment state: `data/page_manifest.json`

## Environment Variables
- `MINIMAX_API_KEY` (optional): LLM enrichment in page generation.
- `PUBLIC_GA4_MEASUREMENT_ID` (optional): inject GA4 tag in layout.
- `GA4_PROPERTY_ID` (optional): KPI report for `affiliate_click`.
- `GOOGLE_APPLICATION_CREDENTIALS` + `GSC_SITE_URL` (optional): GSC KPI fetch.

## Quality Gates
Fails in strict mode when any rule is violated:
- `nan%` exists
- broken markdown table syntax
- legacy embedded CTA block appears in markdown
- duplicate CTA headings detected in markdown
- embedded affiliate URL appears in article markdown body
- generic `event_type: MACRO`
- missing required frontmatter fields

## Notes
- Content is educational and not investment advice.
- Keep GitHub Actions as manual backup only; OpenClaw is primary daily operator.
