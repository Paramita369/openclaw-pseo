---
title: "2024-02-20 CPI Release: BTC Directional Probability Snapshot"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 4
title_template_key: "cpi_4"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-02-20"
asof_date: "2026-03-10"
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
freshness_days: 749
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: 8.07
z_score_t7: 1.34
percentile_t7: 89.74
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:05+00:00"
event_direction: "up"
event_actual: 310.967
event_previous: 309.698
event_delta: 1.269
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.92
  mdd_t7: -0.85
  volatility: 10.03
  impact_t1_pct: -0.85
  impact_t7_pct: 9.18
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
chartData: [{"time": "2024-02-17", "open": 52161.68, "high": 52191.91, "low": 50669.67, "close": 51663.0}, {"time": "2024-02-18", "open": 51661.97, "high": 52356.96, "low": 51233.71, "close": 52122.55}, {"time": "2024-02-19", "open": 52134.81, "high": 52483.32, "low": 51711.82, "close": 51779.14}, {"time": "2024-02-20", "open": 51777.73, "high": 52945.05, "low": 50792.31, "close": 52284.88}, {"time": "2024-02-21", "open": 52273.54, "high": 52368.82, "low": 50671.76, "close": 51839.18}, {"time": "2024-02-22", "open": 51854.64, "high": 52009.61, "low": 50926.29, "close": 51304.97}, {"time": "2024-02-23", "open": 51283.91, "high": 51497.93, "low": 50561.78, "close": 50731.95}, {"time": "2024-02-24", "open": 50736.37, "high": 51684.2, "low": 50585.45, "close": 51571.1}, {"time": "2024-02-25", "open": 51565.21, "high": 51950.03, "low": 51306.17, "close": 51733.24}, {"time": "2024-02-26", "open": 51730.54, "high": 54938.18, "low": 50931.03, "close": 54522.4}, {"time": "2024-02-27", "open": 54519.36, "high": 57537.84, "low": 54484.2, "close": 57085.37}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2024-02-20**
- As-of date (T-1): **2026-03-10**
- Freshness age: **749 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 310.967, Previous 309.698, Delta +1.2690)
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
