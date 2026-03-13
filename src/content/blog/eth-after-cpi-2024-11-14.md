---
title: "ETH CPI Win Rate (2024-11-14): Historical T+1/T+7 Probability"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-12"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-11-14"
asof_date: "2026-03-11"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -2.51
robust_score: -8.51
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 39
freshness_days: 482
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.23
hub_baseline_median_t7: -1.18
hub_baseline_std_t7: 9.719
hub_baseline_delta: 11.06
z_score_t7: 0.99
percentile_t7: 84.62
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:23+00:00"
event_direction: "up"
event_actual: 316.528
event_previous: 315.631
event_delta: 0.897
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 1.17
  mdd_t7: 0.0
  volatility: 8.44
  impact_t1_pct: 1.44
  impact_t7_pct: 9.88
probabilities:
  sample_size: 39
  t1:
    up: 58.97
    down: 41.03
    median: 0.94
    mean: 0.55
    sample: 39
  t7:
    up: 43.59
    down: 56.41
    median: -1.18
    mean: 0.23
    sample: 39
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.96
      mean: 0.64
      sample: 38
    t7:
      up: 44.74
      down: 55.26
      median: -1.52
      mean: 0.24
      sample: 38
related_events: [{"slug": "eth-after-cpi-2024-06-12", "title": "ETH Reaction to US CPI (2024-06-12): Quant Probability Breakdown", "event_date": "2024-06-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.22, "median_t7_pct": -1.18, "sample_size": 39}, {"slug": "eth-after-cpi-2026-02-12", "title": "ETH CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.18, "sample_size": 39}, {"slug": "eth-after-cpi-2026-01-12", "title": "2026-01-12 CPI Release: ETH Directional Probability Snapshot", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.18, "sample_size": 39}]
chartData: [{"time": "2024-11-11", "open": 3191.66, "high": 3389.53, "low": 3109.77, "close": 3374.81}, {"time": "2024-11-12", "open": 3375.15, "high": 3444.15, "low": 3211.2, "close": 3246.26}, {"time": "2024-11-13", "open": 3244.54, "high": 3337.88, "low": 3121.67, "close": 3192.6}, {"time": "2024-11-14", "open": 3192.52, "high": 3240.27, "low": 3032.97, "close": 3058.95}, {"time": "2024-11-15", "open": 3059.53, "high": 3130.7, "low": 3016.14, "close": 3103.04}, {"time": "2024-11-16", "open": 3089.74, "high": 3218.09, "low": 3073.29, "close": 3133.27}, {"time": "2024-11-17", "open": 3133.31, "high": 3160.15, "low": 3039.25, "close": 3075.66}, {"time": "2024-11-18", "open": 3075.72, "high": 3225.13, "low": 3052.49, "close": 3207.86}, {"time": "2024-11-19", "open": 3208.25, "high": 3222.0, "low": 3070.36, "close": 3111.38}, {"time": "2024-11-20", "open": 3111.12, "high": 3159.95, "low": 3032.6, "close": 3072.19}, {"time": "2024-11-21", "open": 3072.06, "high": 3388.54, "low": 3035.85, "close": 3361.05}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-11-14**
- As-of date (T-1): **2026-03-11**
- Freshness age: **482 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 316.528, Previous 315.631, Delta +0.8970)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.94% | 0.55% | 39 |
| T+7 | 43.59% | 56.41% | -1.18% | 0.23% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.96% | 0.64% | 38 |
| T+7 | 44.74% | 55.26% | -1.52% | 0.24% | 38 |

## Historical Distribution Summary

When CPI was **UP**, ETH T+1 up probability was **60.53%** (n=38).

When CPI was **UP**, ETH T+7 up probability was **44.74%** (n=38).

Same-direction T+7 median return: **-1.52%**.

For ETH, historical CPI windows show all-history T+1 up probability of 58.97% and T+7 up probability of 43.59%. When CPI printed Up versus previous, T+1 up probability was 60.53% and T+7 up probability was 44.74% across 38 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
