---
title: "ETH Post-NFP Setup (2025-08-01): Historical Probability Lens"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-08-01"
asof_date: "2026-03-09"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 4.94
robust_score: -1.06
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 60
sample_size: 34
freshness_days: 220
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 2.65
hub_baseline_median_t7: 1.44
hub_baseline_std_t7: 9.723
hub_baseline_delta: 13.51
z_score_t7: 1.27
percentile_t7: 91.18
narrative_trigger: "extreme_outperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 158472.0
event_previous: 158542.0
event_delta: -70.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.85
  mdd_t7: -2.74
  volatility: 17.69
  impact_t1_pct: -2.74
  impact_t7_pct: 14.95
probabilities:
  sample_size: 34
  t1:
    up: 50.0
    down: 50.0
    median: 0.0
    mean: -0.15
    sample: 34
  t7:
    up: 55.88
    down: 44.12
    median: 1.44
    mean: 2.65
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 4
    t1:
      up: 50.0
      down: 50.0
      median: -0.06
      mean: -0.22
      sample: 4
    t7:
      up: 75.0
      down: 25.0
      median: 5.22
      mean: 2.63
      sample: 4
related_events: [{"slug": "eth-after-nfp-2026-02-06", "title": "ETH NFP Reaction (2026-02-06): T+1/T+7 Up Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}, {"slug": "eth-after-nfp-2026-01-02", "title": "2026-01-02 Nonfarm Payrolls: ETH Historical Win Rate", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}, {"slug": "eth-after-nfp-2025-12-05", "title": "ETH Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}]
chartData: [{"time": "2025-07-29", "open": 3788.32, "high": 3884.0, "low": 3716.88, "close": 3793.45}, {"time": "2025-07-30", "open": 3793.58, "high": 3832.88, "low": 3683.14, "close": 3808.2}, {"time": "2025-07-31", "open": 3808.25, "high": 3877.47, "low": 3685.0, "close": 3696.71}, {"time": "2025-08-01", "open": 3696.14, "high": 3722.59, "low": 3432.38, "close": 3488.37}, {"time": "2025-08-02", "open": 3487.96, "high": 3535.56, "low": 3370.94, "close": 3392.74}, {"time": "2025-08-03", "open": 3392.74, "high": 3520.83, "low": 3357.94, "close": 3497.38}, {"time": "2025-08-04", "open": 3497.61, "high": 3734.98, "low": 3491.55, "close": 3718.99}, {"time": "2025-08-05", "open": 3719.82, "high": 3720.66, "low": 3547.62, "close": 3611.9}, {"time": "2025-08-06", "open": 3612.04, "high": 3698.12, "low": 3567.1, "close": 3683.92}, {"time": "2025-08-07", "open": 3684.06, "high": 3926.2, "low": 3650.37, "close": 3914.33}, {"time": "2025-08-08", "open": 3914.11, "high": 4068.85, "low": 3882.44, "close": 4009.85}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2025-08-01**
- As-of date (T-1): **2026-03-09**
- Freshness age: **220 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158472.0, Previous 158542.0, Delta -70.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.15% | 34 |
| T+7 | 55.88% | 44.12% | 1.44% | 2.65% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.06% | -0.22% | 4 |
| T+7 | 75.0% | 25.0% | 5.22% | 2.63% | 4 |

## Historical Distribution Summary

When NFP was **DOWN**, ETH T+1 up probability was **50.0%** (n=4).

When NFP was **DOWN**, ETH T+7 up probability was **75.0%** (n=4).

Same-direction T+7 median return: **5.22%**.

For ETH, historical NFP windows show all-history T+1 up probability of 50.0% and T+7 up probability of 55.88%. When NFP printed Down versus previous, T+1 up probability was 50.0% and T+7 up probability was 75.0% across 4 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
