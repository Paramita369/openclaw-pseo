---
title: "ETH Post-NFP Setup (2024-07-05): Historical Probability Lens"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-07-05"
asof_date: "2026-03-08"
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
quality_score: 90
sample_size: 34
freshness_days: 611
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 2.65
hub_baseline_median_t7: 1.44
hub_baseline_std_t7: 9.723
hub_baseline_delta: 3.68
z_score_t7: 0.25
percentile_t7: 61.76
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:38+00:00"
event_direction: "up"
event_actual: 157748.0
event_previous: 157695.0
event_delta: 53.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 2.35
  mdd_t7: 0.0
  volatility: 2.18
  impact_t1_pct: 2.94
  impact_t7_pct: 5.12
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
    direction: "up"
    sample_size: 30
    t1:
      up: 50.0
      down: 50.0
      median: 0.0
      mean: -0.14
      sample: 30
    t7:
      up: 53.33
      down: 46.67
      median: 0.79
      mean: 2.65
      sample: 30
related_events: [{"slug": "eth-after-nfp-2026-02-06", "title": "ETH NFP Reaction (2026-02-06): T+1/T+7 Up Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}, {"slug": "eth-after-nfp-2026-01-02", "title": "2026-01-02 Nonfarm Payrolls: ETH Historical Win Rate", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}, {"slug": "eth-after-nfp-2025-12-05", "title": "ETH Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}]
chartData: [{"time": "2024-07-02", "open": 3439.38, "high": 3459.76, "low": 3399.03, "close": 3416.35}, {"time": "2024-07-03", "open": 3416.25, "high": 3426.33, "low": 3254.52, "close": 3292.92}, {"time": "2024-07-04", "open": 3291.82, "high": 3309.2, "low": 3054.52, "close": 3054.52}, {"time": "2024-07-05", "open": 3057.83, "high": 3106.15, "low": 2826.01, "close": 2981.6}, {"time": "2024-07-06", "open": 2981.99, "high": 3080.11, "low": 2957.4, "close": 3069.38}, {"time": "2024-07-07", "open": 3067.41, "high": 3072.81, "low": 2923.96, "close": 2929.39}, {"time": "2024-07-08", "open": 2929.86, "high": 3090.66, "low": 2826.48, "close": 3018.73}, {"time": "2024-07-09", "open": 3018.8, "high": 3105.8, "low": 3005.52, "close": 3064.03}, {"time": "2024-07-10", "open": 3066.14, "high": 3148.41, "low": 3026.61, "close": 3102.22}, {"time": "2024-07-11", "open": 3101.34, "high": 3208.94, "low": 3057.22, "close": 3100.33}, {"time": "2024-07-12", "open": 3099.99, "high": 3154.6, "low": 3048.51, "close": 3134.16}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2024-07-05**
- As-of date (T-1): **2026-03-08**
- Freshness age: **611 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157748.0, Previous 157695.0, Delta +53.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.15% | 34 |
| T+7 | 55.88% | 44.12% | 1.44% | 2.65% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.14% | 30 |
| T+7 | 53.33% | 46.67% | 0.79% | 2.65% | 30 |

## Historical Distribution Summary

When NFP was **UP**, ETH T+1 up probability was **50.0%** (n=30).

When NFP was **UP**, ETH T+7 up probability was **53.33%** (n=30).

Same-direction T+7 median return: **0.79%**.

For ETH, historical NFP windows show all-history T+1 up probability of 50.0% and T+7 up probability of 55.88%. When NFP printed Up versus previous, T+1 up probability was 50.0% and T+7 up probability was 53.33% across 30 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
