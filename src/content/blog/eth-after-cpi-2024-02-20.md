---
title: "ETH Reaction to US CPI (2024-02-20): Quant Probability Breakdown"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-02-20"
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
freshness_days: 744
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.26
hub_baseline_median_t7: -0.39
hub_baseline_std_t7: 11.002
hub_baseline_delta: 8.06
z_score_t7: 0.67
percentile_t7: 71.43
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 310.967
event_previous: 309.698
event_delta: 1.269
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.84
  mdd_t7: -1.43
  volatility: 9.1
  impact_t1_pct: -1.43
  impact_t7_pct: 7.67
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
chartData: [{"time": "2024-02-17", "open": 2803.74, "high": 2805.13, "low": 2724.39, "close": 2786.67}, {"time": "2024-02-18", "open": 2786.71, "high": 2892.84, "low": 2767.91, "close": 2879.0}, {"time": "2024-02-19", "open": 2881.3, "high": 2983.37, "low": 2860.26, "close": 2943.57}, {"time": "2024-02-20", "open": 2944.11, "high": 3031.52, "low": 2879.9, "close": 3013.5}, {"time": "2024-02-21", "open": 3015.65, "high": 3017.19, "low": 2875.42, "close": 2970.36}, {"time": "2024-02-22", "open": 2969.6, "high": 3030.67, "low": 2907.11, "close": 2971.01}, {"time": "2024-02-23", "open": 2970.14, "high": 2991.33, "low": 2906.58, "close": 2921.66}, {"time": "2024-02-24", "open": 2921.96, "high": 3003.2, "low": 2907.7, "close": 2992.39}, {"time": "2024-02-25", "open": 2992.37, "high": 3117.43, "low": 2984.39, "close": 3112.7}, {"time": "2024-02-26", "open": 3112.53, "high": 3197.38, "low": 3037.95, "close": 3178.99}, {"time": "2024-02-27", "open": 3178.41, "high": 3287.96, "low": 3167.83, "close": 3244.52}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-02-20**
- As-of date (T-1): **2026-03-05**
- Freshness age: **744 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 310.967, Previous 309.698, Delta +1.2690)
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
