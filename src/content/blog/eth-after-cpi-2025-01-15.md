---
title: "ETH Reaction to US CPI (2025-01-15): Quant Probability Breakdown"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-01-15"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -5.57
robust_score: -11.57
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 14
freshness_days: 414
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 0.26
hub_baseline_median_t7: -0.39
hub_baseline_std_t7: 11.002
hub_baseline_delta: -5.71
z_score_t7: -0.58
percentile_t7: 28.57
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 318.961
event_previous: 317.604
event_delta: 1.357
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -3.08
  mdd_t7: -6.1
  volatility: 1.98
  impact_t1_pct: -4.12
  impact_t7_pct: -6.1
probabilities:
  sample_size: 14
  t1:
    up: 50.0
    down: 50.0
    median: -0.22
    mean: -0.52
    sample: 14
  t7:
    up: 42.86
    down: 57.14
    median: -0.39
    mean: 0.26
    sample: 14
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 53.85
      down: 46.15
      median: 0.66
      mean: -0.36
      sample: 13
    t7:
      up: 46.15
      down: 53.85
      median: -0.77
      mean: 0.28
      sample: 13
related_events: [{"slug": "eth-after-cpi-2024-06-12", "title": "ETH Reaction to US CPI (2024-06-12): Quant Probability Breakdown", "event_date": "2024-06-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.22, "median_t7_pct": -0.39, "sample_size": 14}, {"slug": "eth-after-cpi-2026-02-12", "title": "ETH CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.39, "sample_size": 14}, {"slug": "eth-after-cpi-2026-01-12", "title": "2026-01-12 CPI Release: ETH Directional Probability Snapshot", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.39, "sample_size": 14}]
chartData: [{"time": "2025-01-12", "open": 3282.15, "high": 3298.02, "low": 3224.51, "close": 3265.95}, {"time": "2025-01-13", "open": 3266.1, "high": 3335.19, "low": 2920.59, "close": 3135.5}, {"time": "2025-01-14", "open": 3135.67, "high": 3254.75, "low": 3126.81, "close": 3223.68}, {"time": "2025-01-15", "open": 3223.68, "high": 3473.1, "low": 3186.14, "close": 3450.54}, {"time": "2025-01-16", "open": 3450.31, "high": 3458.18, "low": 3265.68, "close": 3308.35}, {"time": "2025-01-17", "open": 3308.19, "high": 3525.54, "low": 3307.31, "close": 3474.11}, {"time": "2025-01-18", "open": 3473.56, "high": 3493.06, "low": 3228.33, "close": 3305.79}, {"time": "2025-01-19", "open": 3305.4, "high": 3444.21, "low": 3127.62, "close": 3208.96}, {"time": "2025-01-20", "open": 3208.93, "high": 3444.28, "low": 3147.52, "close": 3278.04}, {"time": "2025-01-21", "open": 3278.44, "high": 3365.78, "low": 3202.49, "close": 3327.41}, {"time": "2025-01-22", "open": 3327.24, "high": 3364.75, "low": 3223.39, "close": 3240.22}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2025-01-15**
- As-of date (T-1): **2026-03-05**
- Freshness age: **414 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 318.961, Previous 317.604, Delta +1.3570)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.22% | -0.52% | 14 |
| T+7 | 42.86% | 57.14% | -0.39% | 0.26% | 14 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.66% | -0.36% | 13 |
| T+7 | 46.15% | 53.85% | -0.77% | 0.28% | 13 |

## Historical Distribution Summary

When CPI was **UP**, ETH T+1 up probability was **53.85%** (n=13).

When CPI was **UP**, ETH T+7 up probability was **46.15%** (n=13).

Same-direction T+7 median return: **-0.77%**.

For ETH, historical CPI windows show all-history T+1 up probability of 50.0% and T+7 up probability of 42.86%. When CPI printed Up versus previous, T+1 up probability was 53.85% and T+7 up probability was 46.15% across 13 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
