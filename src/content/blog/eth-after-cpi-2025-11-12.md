---
title: "ETH CPI Win Rate (2025-11-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-11-12"
asof_date: "2026-03-08"
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
freshness_days: 116
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 0.23
hub_baseline_median_t7: -1.18
hub_baseline_std_t7: 9.719
hub_baseline_delta: -10.25
z_score_t7: -1.2
percentile_t7: 7.69
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 325.063
event_previous: 324.245
event_delta: 0.818
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -1.86
  mdd_t7: -11.43
  volatility: 6.14
  impact_t1_pct: -5.28
  impact_t7_pct: -11.43
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
related_events: [{"slug": "eth-after-cpi-2024-06-12", "title": "ETH Reaction to US CPI (2024-06-12): Quant Probability Breakdown", "event_date": "2024-06-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.22, "median_t7_pct": -0.39, "sample_size": 14}, {"slug": "eth-after-cpi-2026-02-12", "title": "ETH CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.18, "sample_size": 39}, {"slug": "eth-after-cpi-2026-01-12", "title": "2026-01-12 CPI Release: ETH Directional Probability Snapshot", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.18, "sample_size": 39}]
chartData: [{"time": "2025-11-09", "open": 3400.1, "high": 3616.44, "low": 3359.72, "close": 3582.62}, {"time": "2025-11-10", "open": 3583.44, "high": 3656.15, "low": 3508.99, "close": 3568.46}, {"time": "2025-11-11", "open": 3568.47, "high": 3644.53, "low": 3404.86, "close": 3415.28}, {"time": "2025-11-12", "open": 3415.8, "high": 3586.01, "low": 3373.71, "close": 3413.09}, {"time": "2025-11-13", "open": 3412.99, "high": 3561.86, "low": 3156.03, "close": 3232.76}, {"time": "2025-11-14", "open": 3232.3, "high": 3252.66, "low": 3071.97, "close": 3103.79}, {"time": "2025-11-15", "open": 3104.23, "high": 3227.69, "low": 3104.23, "close": 3166.63}, {"time": "2025-11-16", "open": 3166.79, "high": 3244.84, "low": 3007.07, "close": 3092.85}, {"time": "2025-11-17", "open": 3092.94, "high": 3218.13, "low": 2957.31, "close": 3024.54}, {"time": "2025-11-18", "open": 3024.41, "high": 3167.93, "low": 2948.33, "close": 3122.98}, {"time": "2025-11-19", "open": 3122.65, "high": 3122.65, "low": 2871.23, "close": 3023.07}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2025-11-12**
- As-of date (T-1): **2026-03-08**
- Freshness age: **116 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 325.063, Previous 324.245, Delta +0.8180)
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
