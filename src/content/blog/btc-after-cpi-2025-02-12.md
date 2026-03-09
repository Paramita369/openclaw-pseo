---
title: "US CPI (2025-02-12) and BTC: Event-Driven Return Odds"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-02-12"
asof_date: "2026-03-08"
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
freshness_days: 389
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: -2.39
z_score_t7: -0.26
percentile_t7: 33.33
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:04:06+00:00"
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
related_events: [{"slug": "btc-after-cpi-2024-08-14", "title": "BTC Reaction to US CPI (2024-08-14): Quant Probability Breakdown", "event_date": "2024-08-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.86, "median_t7_pct": 3.64, "sample_size": 14}, {"slug": "btc-after-cpi-2026-02-12", "title": "BTC After CPI (2026-02-12): Up/Down Odds and Median Returns", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 39}, {"slug": "btc-after-cpi-2026-01-12", "title": "BTC CPI Win Rate (2026-01-12): Historical T+1/T+7 Probability", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 39}]
chartData: [{"time": "2025-02-09", "open": 96481.31, "high": 97325.28, "low": 94745.26, "close": 96500.09}, {"time": "2025-02-10", "open": 96499.46, "high": 98333.22, "low": 95320.84, "close": 97437.55}, {"time": "2025-02-11", "open": 97438.13, "high": 98492.9, "low": 94875.04, "close": 95747.43}, {"time": "2025-02-12", "open": 95745.7, "high": 98151.02, "low": 94101.2, "close": 97885.86}, {"time": "2025-02-13", "open": 97888.75, "high": 98111.09, "low": 95269.71, "close": 96623.87}, {"time": "2025-02-14", "open": 96623.37, "high": 98819.47, "low": 96342.8, "close": 97508.97}, {"time": "2025-02-15", "open": 97508.38, "high": 97975.04, "low": 97240.2, "close": 97580.35}, {"time": "2025-02-16", "open": 97580.49, "high": 97725.59, "low": 96060.98, "close": 96175.03}, {"time": "2025-02-17", "open": 96179.01, "high": 97032.23, "low": 95243.55, "close": 95773.38}, {"time": "2025-02-18", "open": 95773.81, "high": 96695.38, "low": 93388.84, "close": 95539.55}, {"time": "2025-02-19", "open": 95532.53, "high": 96855.59, "low": 95011.97, "close": 96635.61}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2025-02-12**
- As-of date (T-1): **2026-03-08**
- Freshness age: **389 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 319.679, Previous 318.961, Delta +0.7180)
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
