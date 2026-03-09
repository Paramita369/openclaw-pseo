---
title: "US CPI (2024-01-15) and ETH: Event-Driven Return Odds"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-01-15"
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
freshness_days: 783
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.23
hub_baseline_median_t7: -1.18
hub_baseline_std_t7: 9.719
hub_baseline_delta: -6.81
z_score_t7: -0.85
percentile_t7: 17.95
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:02+00:00"
event_direction: "up"
event_actual: 309.698
event_previous: 308.741
event_delta: 0.957
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -0.72
  mdd_t7: -7.99
  volatility: 11.03
  impact_t1_pct: 3.04
  impact_t7_pct: -7.99
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
chartData: [{"time": "2024-01-12", "open": 2619.18, "high": 2710.42, "low": 2460.93, "close": 2524.46}, {"time": "2024-01-13", "open": 2522.93, "high": 2589.08, "low": 2498.59, "close": 2576.6}, {"time": "2024-01-14", "open": 2578.0, "high": 2578.33, "low": 2470.42, "close": 2472.24}, {"time": "2024-01-15", "open": 2471.67, "high": 2550.77, "low": 2470.82, "close": 2511.36}, {"time": "2024-01-16", "open": 2510.63, "high": 2613.57, "low": 2500.0, "close": 2587.69}, {"time": "2024-01-17", "open": 2587.04, "high": 2592.74, "low": 2508.43, "close": 2528.37}, {"time": "2024-01-18", "open": 2528.59, "high": 2546.26, "low": 2426.14, "close": 2467.02}, {"time": "2024-01-19", "open": 2468.69, "high": 2501.31, "low": 2414.71, "close": 2489.5}, {"time": "2024-01-20", "open": 2489.85, "high": 2489.85, "low": 2456.1, "close": 2469.59}, {"time": "2024-01-21", "open": 2469.8, "high": 2479.76, "low": 2452.38, "close": 2453.91}, {"time": "2024-01-22", "open": 2454.99, "high": 2463.45, "low": 2303.5, "close": 2310.83}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-01-15**
- As-of date (T-1): **2026-03-08**
- Freshness age: **783 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 309.698, Previous 308.741, Delta +0.9570)
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
