---
title: "BTC CPI Win Rate (2024-03-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-03-12"
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
freshness_days: 727
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: -14.5
z_score_t7: -2.12
percentile_t7: 2.56
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:07+00:00"
event_direction: "up"
event_actual: 312.345
event_previous: 310.967
event_delta: 1.378
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -0.86
  mdd_t7: -13.39
  volatility: 15.63
  impact_t1_pct: 2.24
  impact_t7_pct: -13.39
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
chartData: [{"time": "2024-03-09", "open": 68299.26, "high": 68673.05, "low": 68053.12, "close": 68498.88}, {"time": "2024-03-10", "open": 68500.26, "high": 70005.2, "low": 68239.98, "close": 69019.79}, {"time": "2024-03-11", "open": 69020.55, "high": 72850.71, "low": 67194.88, "close": 72123.91}, {"time": "2024-03-12", "open": 72125.12, "high": 72825.66, "low": 68728.85, "close": 71481.29}, {"time": "2024-03-13", "open": 71482.12, "high": 73637.48, "low": 71334.09, "close": 73083.5}, {"time": "2024-03-14", "open": 73079.38, "high": 73750.07, "low": 68563.02, "close": 71396.59}, {"time": "2024-03-15", "open": 71387.88, "high": 72357.13, "low": 65630.7, "close": 69403.77}, {"time": "2024-03-16", "open": 69392.48, "high": 70046.27, "low": 64801.39, "close": 65315.12}, {"time": "2024-03-17", "open": 65316.34, "high": 68845.72, "low": 64545.32, "close": 68390.62}, {"time": "2024-03-18", "open": 68371.3, "high": 68897.13, "low": 66594.23, "close": 67548.59}, {"time": "2024-03-19", "open": 67556.13, "high": 68106.93, "low": 61536.18, "close": 61912.77}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2024-03-12**
- As-of date (T-1): **2026-03-09**
- Freshness age: **727 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 312.345, Previous 310.967, Delta +1.3780)
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
