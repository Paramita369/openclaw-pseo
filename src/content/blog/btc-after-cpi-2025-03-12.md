---
title: "BTC CPI Win Rate (2025-03-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-03-12"
asof_date: "2026-03-09"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 6.62
robust_score: 0.62
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 39
freshness_days: 362
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: 2.63
z_score_t7: 0.51
percentile_t7: 69.23
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 319.785
event_previous: 319.679
event_delta: 0.106
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.54
  mdd_t7: -3.17
  volatility: 6.91
  impact_t1_pct: -3.17
  impact_t7_pct: 3.74
probabilities:
  sample_size: 39
  t1:
    up: 58.97
    down: 41.03
    median: 0.51
    mean: 0.37
    sample: 39
  t7:
    up: 53.85
    down: 46.15
    median: 1.11
    mean: 0.44
    sample: 39
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.53
      mean: 0.44
      sample: 38
    t7:
      up: 55.26
      down: 44.74
      median: 1.26
      mean: 0.58
      sample: 38
related_events: [{"slug": "btc-after-cpi-2024-08-14", "title": "BTC Reaction to US CPI (2024-08-14): Quant Probability Breakdown", "event_date": "2024-08-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.86, "median_t7_pct": 1.11, "sample_size": 39}, {"slug": "btc-after-cpi-2026-02-12", "title": "BTC After CPI (2026-02-12): Up/Down Odds and Median Returns", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 39}, {"slug": "btc-after-cpi-2026-01-12", "title": "BTC CPI Win Rate (2026-01-12): Historical T+1/T+7 Probability", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 39}]
chartData: [{"time": "2025-03-09", "open": 86154.3, "high": 86471.13, "low": 80052.48, "close": 80601.04}, {"time": "2025-03-10", "open": 80597.15, "high": 83955.93, "low": 77420.59, "close": 78532.0}, {"time": "2025-03-11", "open": 78523.88, "high": 83577.76, "low": 76624.25, "close": 82862.21}, {"time": "2025-03-12", "open": 82857.38, "high": 84358.58, "low": 80635.25, "close": 83722.36}, {"time": "2025-03-13", "open": 83724.92, "high": 84301.7, "low": 79931.85, "close": 81066.7}, {"time": "2025-03-14", "open": 81066.99, "high": 85263.29, "low": 80797.56, "close": 83969.1}, {"time": "2025-03-15", "open": 83968.41, "high": 84672.67, "low": 83639.59, "close": 84343.11}, {"time": "2025-03-16", "open": 84333.32, "high": 85051.6, "low": 82017.91, "close": 82579.69}, {"time": "2025-03-17", "open": 82576.34, "high": 84725.33, "low": 82492.16, "close": 84075.69}, {"time": "2025-03-18", "open": 84075.72, "high": 84075.72, "low": 81179.99, "close": 82718.5}, {"time": "2025-03-19", "open": 82718.8, "high": 87021.19, "low": 82569.73, "close": 86854.23}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2025-03-12**
- As-of date (T-1): **2026-03-09**
- Freshness age: **362 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 319.785, Previous 319.679, Delta +0.1060)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.51% | 0.37% | 39 |
| T+7 | 53.85% | 46.15% | 1.11% | 0.44% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.53% | 0.44% | 38 |
| T+7 | 55.26% | 44.74% | 1.26% | 0.58% | 38 |

## Historical Distribution Summary

When CPI was **UP**, BTC T+1 up probability was **60.53%** (n=38).

When CPI was **UP**, BTC T+7 up probability was **55.26%** (n=38).

Same-direction T+7 median return: **1.26%**.

For BTC, historical CPI windows show all-history T+1 up probability of 58.97% and T+7 up probability of 53.85%. When CPI printed Up versus previous, T+1 up probability was 60.53% and T+7 up probability was 55.26% across 38 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
