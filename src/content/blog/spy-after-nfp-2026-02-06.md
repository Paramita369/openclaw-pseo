---
title: "SPY NFP Reaction (2026-02-06): T+1/T+7 Up Probability"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 1
title_template_key: "nfp_1"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-02-06"
asof_date: "2026-03-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 4.94
robust_score: 4.94
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 35
freshness_days: 34
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.81
hub_baseline_median_t7: 0.11
hub_baseline_std_t7: 1.9337
hub_baseline_delta: -1.39
z_score_t7: -1.08
percentile_t7: 11.76
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/spy-after-nfp-2026-02-06"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "down"
event_actual: 158466.0
event_previous: 158558.0
event_delta: -92.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -7.01
  mdd_t7: -1.76
  volatility: 15.28
  impact_t1_pct: 0.48
  impact_t7_pct: -1.28
probabilities:
  sample_size: 35
  t1:
    up: 50.0
    down: 50.0
    median: 0.02
    mean: -0.05
    sample: 22
  t7:
    up: 55.88
    down: 44.12
    median: 0.11
    mean: 0.81
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 8
    t1:
      up: 62.5
      down: 37.5
      median: 0.22
      mean: 0.05
      sample: 8
    t7:
      up: 37.5
      down: 62.5
      median: -0.47
      mean: 0.2
      sample: 8
related_events: [{"slug": "spy-after-nfp-2026-01-02", "title": "SPY After NFP (2026-01-02): Historical T+1/T+7 Probability", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.6, "sample_size": 0}, {"slug": "spy-after-nfp-2025-11-20", "title": "SPY After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.73, "sample_size": 0}, {"slug": "spy-after-nfp-2025-09-05", "title": "SPY After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.57, "sample_size": 0}]
chartData: [{"time": "2026-02-03", "open": 696.21, "high": 696.96, "low": 684.03, "close": 689.53}, {"time": "2026-02-04", "open": 690.35, "high": 691.45, "low": 681.76, "close": 686.19}, {"time": "2026-02-05", "open": 680.94, "high": 683.69, "low": 675.79, "close": 677.62}, {"time": "2026-02-06", "open": 681.46, "high": 692.31, "low": 680.85, "close": 690.62}, {"time": "2026-02-09", "open": 689.42, "high": 695.87, "low": 688.34, "close": 693.95}, {"time": "2026-02-10", "open": 694.95, "high": 696.54, "low": 691.66, "close": 692.12}, {"time": "2026-02-11", "open": 696.39, "high": 697.14, "low": 689.18, "close": 691.96}, {"time": "2026-02-12", "open": 694.24, "high": 695.35, "low": 680.37, "close": 681.27}, {"time": "2026-02-13", "open": 681.69, "high": 686.28, "low": 677.52, "close": 681.75}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2026-02-06**
- As-of date (T-1): **2026-03-12**
- Freshness age: **34 days**
- Sample size (all-history): **35**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158466.0, Previous 158558.0, Delta -92.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.02% | -0.05% | 22 |
| T+7 | 55.88% | 44.12% | 0.11% | 0.81% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 62.5% | 37.5% | 0.22% | 0.05% | 8 |
| T+7 | 37.5% | 62.5% | -0.47% | 0.2% | 8 |

## Event Outcome Interpretation

The main mistake after macro releases is to treat every surprise as a regime break. SPY around NFP is best framed through how the release landed lower than the previous release. The current observation shows actual value 158466.0000 versus previous 158558.0000, a delta of -92.0000. Across the full history, SPY has a T+7 up probability of 55.88% versus 44.12% down, with a median return of 0.11%. When only matching the same event direction, the T+7 up probability shifts to 37.50% across 8 comparable releases, with a same-direction median of -0.47%. The current release therefore reads as a below-baseline and fragile response rather than a collapse. The standing hub thesis for this asset-event pair is: SPY's payroll reaction depends on whether labor strength implies growth support or renewed rate pressure; context from wages and revisions is critical.

## Distribution Position

This window is below baseline and looks fragile rather than structurally broken. The current T+7 move of -1.28% carries a z-score of -1.08 and a percentile rank of 11.76, leaving the release in the lower quartile of observed windows. That puts the event on the weak side of normal without forcing it into a full downside tail label. The important distinction is that fragile reactions can still bounce, which is why a mild underperformance should not be confused with regime failure.

## Comparison vs Hub Baseline

This comparison is below baseline, but it is still better read as fragile than catastrophic. The baseline comparison matters because most false positives come from overreacting to ordinary noise. The hub baseline median T+7 return is 0.11% and the current gap is -1.39%. Same-direction probability differs by -18.38% and the same-direction median differs by -0.58%. The baseline gap is large enough to matter, but not large enough to imply that the broader playbook is broken. The current regime context also matters: Market has priced labor resilience with tighter tolerance for inflation reacceleration.

## Failure Modes

The failure mode here is reading a fragile window as proof of permanent weakness. The main failure mode is assuming the first interpretation will survive cross-asset confirmation. False trend starts are common before cash-session participation increases. Moderate underperformance often creates bounce risk, especially if rates or the dollar stop reinforcing the weak read.

## Execution Relevance

Treat this as an educational risk framework, not investment advice. The operational takeaway is to respect the below-baseline read without assuming collapse. The checklist is Read payroll, wages, and revisions as a package.; Wait for cash equity open confirmation.; Scale out into intraday volatility spikes.. Fragile setups demand tighter invalidation and more patience because bounce risk is often highest when traders treat every weak release as a one-way trend.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
