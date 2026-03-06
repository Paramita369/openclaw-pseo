---
title: "US CPI (2025-02-12) and BTC: Event-Driven Return Odds"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-02-12"
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
quality_score: 90
sample_size: 14
freshness_days: 386
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 1.69
hub_baseline_median_t7: 3.64
hub_baseline_std_t7: 8.5155
hub_baseline_delta: -4.92
z_score_t7: -0.35
percentile_t7: 35.71
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 319.679
event_previous: 318.961
event_delta: 0.718
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -128.0
  mdd_t7: -1.29
  volatility: 0.01
  impact_t1_pct: -1.29
  impact_t7_pct: -1.28
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
chartData: [{"time": "2025-02-09", "open": 96481.31, "high": 97325.28, "low": 94745.26, "close": 96500.09}, {"time": "2025-02-10", "open": 96499.46, "high": 98333.22, "low": 95320.84, "close": 97437.55}, {"time": "2025-02-11", "open": 97438.13, "high": 98492.9, "low": 94875.04, "close": 95747.43}, {"time": "2025-02-12", "open": 95745.7, "high": 98151.02, "low": 94101.2, "close": 97885.86}, {"time": "2025-02-13", "open": 97888.75, "high": 98111.09, "low": 95269.71, "close": 96623.87}, {"time": "2025-02-14", "open": 96623.37, "high": 98819.47, "low": 96342.8, "close": 97508.97}, {"time": "2025-02-15", "open": 97508.38, "high": 97975.04, "low": 97240.2, "close": 97580.35}, {"time": "2025-02-16", "open": 97580.49, "high": 97725.59, "low": 96060.98, "close": 96175.03}, {"time": "2025-02-17", "open": 96179.01, "high": 97032.23, "low": 95243.55, "close": 95773.38}, {"time": "2025-02-18", "open": 95773.81, "high": 96695.38, "low": 93388.84, "close": 95539.55}, {"time": "2025-02-19", "open": 95532.53, "high": 96855.59, "low": 95011.97, "close": 96635.61}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2025-02-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **386 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 319.679, Previous 318.961, Delta +0.7180)
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
