---
title: "BTC CPI Win Rate (2025-03-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-03-12"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 3.43
robust_score: -2.57
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 70
sample_size: 14
freshness_days: 358
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 1.69
hub_baseline_median_t7: 3.64
hub_baseline_std_t7: 8.5155
hub_baseline_delta: -1.95
z_score_t7: -0.0
percentile_t7: 42.86
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 319.785
event_previous: 319.679
event_delta: 0.106
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 1.18
  mdd_t7: 0.0
  volatility: 1.43
  impact_t1_pct: 0.26
  impact_t7_pct: 1.69
probabilities:
  sample_size: 14
  t1:
    up: 42.86
    down: 57.14
    median: -0.74
    mean: 0.26
    sample: 14
  t7:
    up: 57.14
    down: 42.86
    median: 3.64
    mean: 1.69
    sample: 14
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 46.15
      down: 53.85
      median: -0.74
      mean: 0.44
      sample: 13
    t7:
      up: 61.54
      down: 38.46
      median: 4.15
      mean: 2.19
      sample: 13
related_events: [{"slug": "btc-after-cpi-2024-08-14", "title": "BTC Reaction to US CPI (2024-08-14): Quant Probability Breakdown", "event_date": "2024-08-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.86, "median_t7_pct": 3.64, "sample_size": 14}, {"slug": "btc-after-cpi-2026-02-12", "title": "BTC After CPI (2026-02-12): Up/Down Odds and Median Returns", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 3.64, "sample_size": 14}, {"slug": "btc-after-cpi-2026-01-12", "title": "BTC CPI Win Rate (2026-01-12): Historical T+1/T+7 Probability", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 3.64, "sample_size": 14}]
chartData: [{"time": "2025-03-09", "open": 86154.3, "high": 86471.13, "low": 80052.48, "close": 80601.04}, {"time": "2025-03-10", "open": 80597.15, "high": 83955.93, "low": 77420.59, "close": 78532.0}, {"time": "2025-03-11", "open": 78523.88, "high": 83577.76, "low": 76624.25, "close": 82862.21}, {"time": "2025-03-12", "open": 82857.38, "high": 84358.58, "low": 80635.25, "close": 83722.36}, {"time": "2025-03-13", "open": 83724.92, "high": 84301.7, "low": 79931.85, "close": 81066.7}, {"time": "2025-03-14", "open": 81066.99, "high": 85263.29, "low": 80797.56, "close": 83969.1}, {"time": "2025-03-15", "open": 83968.41, "high": 84672.67, "low": 83639.59, "close": 84343.11}, {"time": "2025-03-16", "open": 84333.32, "high": 85051.6, "low": 82017.91, "close": 82579.69}, {"time": "2025-03-17", "open": 82576.34, "high": 84725.33, "low": 82492.16, "close": 84075.69}, {"time": "2025-03-18", "open": 84075.72, "high": 84075.72, "low": 81179.99, "close": 82718.5}, {"time": "2025-03-19", "open": 82718.8, "high": 87021.19, "low": 82569.73, "close": 86854.23}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2025-03-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **358 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 319.785, Previous 319.679, Delta +0.1060)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 42.86% | 57.14% | -0.74% | 0.26% | 14 |
| T+7 | 57.14% | 42.86% | 3.64% | 1.69% | 14 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 46.15% | 53.85% | -0.74% | 0.44% | 13 |
| T+7 | 61.54% | 38.46% | 4.15% | 2.19% | 13 |

## Historical Distribution Summary

When CPI was **UP**, BTC T+1 up probability was **46.15%** (n=13).

When CPI was **UP**, BTC T+7 up probability was **61.54%** (n=13).

Same-direction T+7 median return: **4.15%**.

For BTC, historical CPI windows show all-history T+1 up probability of 42.86% and T+7 up probability of 57.14%. When CPI printed Up versus previous, T+1 up probability was 46.15% and T+7 up probability was 61.54% across 13 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
