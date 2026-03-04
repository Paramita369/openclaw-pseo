---
title: "Historical Performance of ETH After CPI (2025-10-24)"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-10-24"
asof_date: "2026-03-03"
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
freshness_days: 130
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 324.245
event_previous: 323.291
event_delta: 0.954
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -0.82
  mdd_t7: -2.22
  volatility: 2.7
  impact_t1_pct: 0.48
  impact_t7_pct: -2.22
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
related_events: [{"slug": "eth-after-cpi-2024-06-12", "title": "ETH After CPI (2024-06-12): Historical T+1/T+7 Probability", "event_date": "2024-06-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.22, "median_t7_pct": -0.01, "sample_size": 0}, {"slug": "eth-after-cpi-2026-02-13", "title": "ETH After CPI (2026-02-13): Historical T+1/T+7 Probability", "event_date": "2026-02-13", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -3.88, "sample_size": 0}, {"slug": "eth-after-cpi-2026-02-12", "title": "ETH After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.06, "sample_size": 0}]
chartData: [{"time": "2025-10-21", "open": 3980.74, "high": 4109.53, "low": 3843.23, "close": 3876.76}, {"time": "2025-10-22", "open": 3877.36, "high": 3890.63, "low": 3718.08, "close": 3808.12}, {"time": "2025-10-23", "open": 3808.08, "high": 3930.97, "low": 3801.24, "close": 3856.03}, {"time": "2025-10-24", "open": 3856.03, "high": 4002.56, "low": 3849.72, "close": 3934.57}, {"time": "2025-10-25", "open": 3934.49, "high": 3967.65, "low": 3914.64, "close": 3953.47}, {"time": "2025-10-26", "open": 3953.44, "high": 4177.31, "low": 3923.19, "close": 4157.99}, {"time": "2025-10-27", "open": 4158.01, "high": 4250.67, "low": 4099.57, "close": 4120.12}, {"time": "2025-10-28", "open": 4120.27, "high": 4173.51, "low": 3940.83, "close": 3982.26}, {"time": "2025-10-29", "open": 3980.76, "high": 4036.35, "low": 3849.54, "close": 3903.35}, {"time": "2025-10-30", "open": 3903.32, "high": 3948.22, "low": 3681.91, "close": 3804.38}, {"time": "2025-10-31", "open": 3805.08, "high": 3900.58, "low": 3797.67, "close": 3847.08}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2025-10-24**
- As-of date (T-1): **2026-03-03**
- Freshness age: **130 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 324.245, Previous 323.291, Delta +0.9540)
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
