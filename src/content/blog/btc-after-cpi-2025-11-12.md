---
title: "BTC Reaction to US CPI (2025-11-12): Quant Probability Breakdown"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-11-12"
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
freshness_days: 118
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: -11.14
z_score_t7: -1.61
percentile_t7: 10.26
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 325.063
event_previous: 324.245
event_delta: 0.818
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -1.24
  mdd_t7: -10.03
  volatility: 8.1
  impact_t1_pct: -1.93
  impact_t7_pct: -10.03
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
chartData: [{"time": "2025-11-09", "open": 102278.98, "high": 105418.37, "low": 101468.88, "close": 104719.64}, {"time": "2025-11-10", "open": 104723.77, "high": 106564.7, "low": 104350.65, "close": 105996.59}, {"time": "2025-11-11", "open": 105996.86, "high": 107428.26, "low": 102457.33, "close": 102997.47}, {"time": "2025-11-12", "open": 103011.44, "high": 105297.23, "low": 100836.62, "close": 101663.19}, {"time": "2025-11-13", "open": 101674.15, "high": 104005.49, "low": 97988.72, "close": 99697.49}, {"time": "2025-11-14", "open": 99694.7, "high": 99804.43, "low": 94000.73, "close": 94397.79}, {"time": "2025-11-15", "open": 94420.47, "high": 96728.47, "low": 94420.47, "close": 95549.15}, {"time": "2025-11-16", "open": 95556.87, "high": 96564.19, "low": 92971.16, "close": 94177.08}, {"time": "2025-11-17", "open": 94180.88, "high": 95928.37, "low": 91214.76, "close": 92093.88}, {"time": "2025-11-18", "open": 92094.53, "high": 93745.08, "low": 89300.46, "close": 92948.88}, {"time": "2025-11-19", "open": 92946.16, "high": 92946.16, "low": 88526.83, "close": 91465.99}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2025-11-12**
- As-of date (T-1): **2026-03-10**
- Freshness age: **118 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 325.063, Previous 324.245, Delta +0.8180)
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
