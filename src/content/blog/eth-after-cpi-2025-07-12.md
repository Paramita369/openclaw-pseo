---
title: "US CPI (2025-07-12) and ETH: Event-Driven Return Odds"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-07-12"
asof_date: "2026-03-05"
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
quality_score: 100
sample_size: 39
freshness_days: 236
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 322.169
event_previous: 321.435
event_delta: 0.734
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 106.85
  impact_t1_pct: 1.03
  impact_t7_pct: 22.17
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
related_events: [{"slug": "eth-after-cpi-2025-07-15", "title": "ETH After CPI (2025-07-15): Historical T+1/T+7 Probability", "event_date": "2025-07-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 19.4, "sample_size": 0}, {"slug": "eth-after-cpi-2025-04-10", "title": "ETH After CPI (2025-04-10): Historical T+1/T+7 Probability", "event_date": "2025-04-10", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.94, "sample_size": 0}, {"slug": "eth-after-cpi-2025-03-12", "title": "ETH After CPI (2025-03-12): Historical T+1/T+7 Probability", "event_date": "2025-03-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 7.79, "sample_size": 0}]
chartData: [{"time": "2025-07-09", "open": 2615.51, "high": 2794.52, "low": 2591.95, "close": 2770.78}, {"time": "2025-07-10", "open": 2770.74, "high": 2995.15, "low": 2757.27, "close": 2954.85}, {"time": "2025-07-11", "open": 2954.83, "high": 3038.14, "low": 2916.96, "close": 2957.89}, {"time": "2025-07-12", "open": 2958.33, "high": 2979.78, "low": 2907.19, "close": 2942.91}, {"time": "2025-07-13", "open": 2942.85, "high": 3016.39, "low": 2938.74, "close": 2973.36}, {"time": "2025-07-14", "open": 2973.23, "high": 3079.99, "low": 2965.32, "close": 3013.35}, {"time": "2025-07-15", "open": 3013.29, "high": 3142.43, "low": 2934.37, "close": 3139.89}, {"time": "2025-07-16", "open": 3139.89, "high": 3422.6, "low": 3102.48, "close": 3371.51}, {"time": "2025-07-17", "open": 3371.51, "high": 3521.69, "low": 3316.0, "close": 3476.78}, {"time": "2025-07-18", "open": 3476.12, "high": 3674.86, "low": 3463.39, "close": 3549.02}, {"time": "2025-07-19", "open": 3548.93, "high": 3608.28, "low": 3512.97, "close": 3595.27}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2025-07-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **236 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 322.169, Previous 321.435, Delta +0.7340)
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
