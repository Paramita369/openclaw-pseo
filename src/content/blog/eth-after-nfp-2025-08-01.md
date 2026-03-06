---
title: "ETH Post-NFP Setup (2025-08-01): Historical Probability Lens"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-08-01"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Bullish"
raw_signal_score: 8.93
robust_score: 2.93
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 40
sample_size: 13
freshness_days: 216
freshness_status: "stale"
index_tier: "C"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 3.32
hub_baseline_median_t7: 5.12
hub_baseline_std_t7: 8.5559
hub_baseline_delta: -1.8
z_score_t7: -0.0
percentile_t7: 46.15
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "none"
canonical_url: ""
robots_directive: "noindex,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "down"
event_actual: 158472.0
event_previous: 158542.0
event_delta: -70.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.03
  mdd_t7: 0.0
  volatility: 3.21
  impact_t1_pct: 0.11
  impact_t7_pct: 3.32
probabilities:
  sample_size: 13
  t1:
    up: 53.85
    down: 46.15
    median: 0.03
    mean: 0.11
    sample: 13
  t7:
    up: 61.54
    down: 38.46
    median: 5.12
    mean: 3.32
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 1
    t1:
      up: 100.0
      down: 0.0
      median: 0.45
      mean: 0.45
      sample: 1
    t7:
      up: 100.0
      down: 0.0
      median: 6.32
      mean: 6.32
      sample: 1
related_events: [{"slug": "eth-after-nfp-2026-02-06", "title": "ETH NFP Reaction (2026-02-06): T+1/T+7 Up Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 5.12, "sample_size": 13}, {"slug": "eth-after-nfp-2026-01-02", "title": "2026-01-02 Nonfarm Payrolls: ETH Historical Win Rate", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 5.12, "sample_size": 13}, {"slug": "eth-after-nfp-2025-12-05", "title": "ETH Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 5.12, "sample_size": 13}]
chartData: [{"time": "2025-07-29", "open": 3788.32, "high": 3884.0, "low": 3716.88, "close": 3793.45}, {"time": "2025-07-30", "open": 3793.58, "high": 3832.88, "low": 3683.14, "close": 3808.2}, {"time": "2025-07-31", "open": 3808.25, "high": 3877.47, "low": 3685.0, "close": 3696.71}, {"time": "2025-08-01", "open": 3696.14, "high": 3722.59, "low": 3432.38, "close": 3488.37}, {"time": "2025-08-02", "open": 3487.96, "high": 3535.56, "low": 3370.94, "close": 3392.74}, {"time": "2025-08-03", "open": 3392.74, "high": 3520.83, "low": 3357.94, "close": 3497.38}, {"time": "2025-08-04", "open": 3497.61, "high": 3734.98, "low": 3491.55, "close": 3718.99}, {"time": "2025-08-05", "open": 3719.82, "high": 3720.66, "low": 3547.62, "close": 3611.9}, {"time": "2025-08-06", "open": 3612.04, "high": 3698.12, "low": 3567.1, "close": 3683.92}, {"time": "2025-08-07", "open": 3684.06, "high": 3926.2, "low": 3650.37, "close": 3914.33}, {"time": "2025-08-08", "open": 3914.11, "high": 4068.85, "low": 3882.44, "close": 4009.85}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2025-08-01**
- As-of date (T-1): **2026-03-05**
- Freshness age: **216 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158472.0, Previous 158542.0, Delta -70.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.03% | 0.11% | 13 |
| T+7 | 61.54% | 38.46% | 5.12% | 3.32% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 100.0% | 0.0% | 0.45% | 0.45% | 1 |
| T+7 | 100.0% | 0.0% | 6.32% | 6.32% | 1 |

## Historical Distribution Summary

When NFP was **DOWN**, ETH T+1 up probability was **100.0%** (n=1).

When NFP was **DOWN**, ETH T+7 up probability was **100.0%** (n=1).

Same-direction T+7 median return: **6.32%**.

For ETH, historical NFP windows show all-history T+1 up probability of 53.85% and T+7 up probability of 61.54%. When NFP printed Down versus previous, T+1 up probability was 100.0% and T+7 up probability was 100.0% across 1 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
