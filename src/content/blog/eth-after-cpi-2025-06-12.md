---
title: "ETH Reaction to US CPI (2025-06-12): Quant Probability Breakdown"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-06-12"
asof_date: "2026-03-10"
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
freshness_days: 271
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.23
hub_baseline_median_t7: -1.18
hub_baseline_std_t7: 9.719
hub_baseline_delta: -3.73
z_score_t7: -0.53
percentile_t7: 30.77
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 321.435
event_previous: 320.62
event_delta: 0.815
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -2.25
  mdd_t7: -4.91
  volatility: 2.18
  impact_t1_pct: -2.73
  impact_t7_pct: -4.91
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
chartData: [{"time": "2025-06-09", "open": 2510.84, "high": 2693.81, "low": 2479.87, "close": 2681.52}, {"time": "2025-06-10", "open": 2681.29, "high": 2824.81, "low": 2658.68, "close": 2813.52}, {"time": "2025-06-11", "open": 2813.74, "high": 2877.63, "low": 2746.46, "close": 2773.53}, {"time": "2025-06-12", "open": 2773.6, "high": 2784.26, "low": 2619.97, "close": 2651.8}, {"time": "2025-06-13", "open": 2651.92, "high": 2651.92, "low": 2443.96, "close": 2579.49}, {"time": "2025-06-14", "open": 2579.72, "high": 2580.16, "low": 2491.49, "close": 2533.44}, {"time": "2025-06-15", "open": 2533.18, "high": 2558.68, "low": 2493.2, "close": 2546.84}, {"time": "2025-06-16", "open": 2547.23, "high": 2680.09, "low": 2517.15, "close": 2540.6}, {"time": "2025-06-17", "open": 2540.31, "high": 2617.9, "low": 2456.65, "close": 2510.76}, {"time": "2025-06-18", "open": 2510.82, "high": 2546.63, "low": 2469.05, "close": 2524.3}, {"time": "2025-06-19", "open": 2524.4, "high": 2546.77, "low": 2486.1, "close": 2521.65}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2025-06-12**
- As-of date (T-1): **2026-03-10**
- Freshness age: **271 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 321.435, Previous 320.62, Delta +0.8150)
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
