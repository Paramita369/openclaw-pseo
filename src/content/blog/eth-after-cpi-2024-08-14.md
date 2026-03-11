---
title: "2024-08-14 CPI Release: ETH Directional Probability Snapshot"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 4
title_template_key: "cpi_4"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-08-14"
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
freshness_days: 573
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.23
hub_baseline_median_t7: -1.18
hub_baseline_std_t7: 9.719
hub_baseline_delta: 0.0
z_score_t7: -0.15
percentile_t7: 51.28
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 314.062
event_previous: 313.569
event_delta: 0.493
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -3.58
  mdd_t7: -3.49
  volatility: 2.31
  impact_t1_pct: -3.49
  impact_t7_pct: -1.18
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
chartData: [{"time": "2024-08-11", "open": 2609.97, "high": 2718.8, "low": 2544.17, "close": 2553.25}, {"time": "2024-08-12", "open": 2553.5, "high": 2749.14, "low": 2513.39, "close": 2724.43}, {"time": "2024-08-13", "open": 2724.3, "high": 2737.99, "low": 2613.8, "close": 2703.67}, {"time": "2024-08-14", "open": 2703.59, "high": 2775.28, "low": 2636.71, "close": 2662.91}, {"time": "2024-08-15", "open": 2662.89, "high": 2675.31, "low": 2518.67, "close": 2570.09}, {"time": "2024-08-16", "open": 2570.09, "high": 2629.38, "low": 2553.07, "close": 2593.19}, {"time": "2024-08-17", "open": 2593.17, "high": 2626.67, "low": 2588.79, "close": 2614.55}, {"time": "2024-08-18", "open": 2614.11, "high": 2684.03, "low": 2596.74, "close": 2613.36}, {"time": "2024-08-19", "open": 2612.72, "high": 2648.28, "low": 2566.4, "close": 2637.31}, {"time": "2024-08-20", "open": 2637.31, "high": 2695.91, "low": 2556.75, "close": 2573.11}, {"time": "2024-08-21", "open": 2573.11, "high": 2662.95, "low": 2538.66, "close": 2631.4}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-08-14**
- As-of date (T-1): **2026-03-10**
- Freshness age: **573 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 314.062, Previous 313.569, Delta +0.4930)
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
