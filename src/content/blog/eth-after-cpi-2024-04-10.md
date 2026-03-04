---
title: "Historical Performance of ETH After CPI (2024-04-10)"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-04-10"
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
freshness_days: 692
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 313.023
event_previous: 312.345
event_delta: 0.678
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -1.07
  mdd_t7: -15.77
  volatility: 14.68
  impact_t1_pct: -1.09
  impact_t7_pct: -15.77
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
chartData: [{"time": "2024-04-07", "open": 3354.21, "high": 3458.51, "low": 3346.11, "close": 3453.49}, {"time": "2024-04-08", "open": 3453.5, "high": 3727.62, "low": 3409.51, "close": 3695.29}, {"time": "2024-04-09", "open": 3695.34, "high": 3724.92, "low": 3455.11, "close": 3505.16}, {"time": "2024-04-10", "open": 3505.16, "high": 3561.52, "low": 3415.18, "close": 3543.74}, {"time": "2024-04-11", "open": 3543.45, "high": 3616.19, "low": 3477.17, "close": 3505.25}, {"time": "2024-04-12", "open": 3505.33, "high": 3552.59, "low": 3103.43, "close": 3243.03}, {"time": "2024-04-13", "open": 3242.94, "high": 3299.66, "low": 2862.39, "close": 3004.9}, {"time": "2024-04-14", "open": 3005.55, "high": 3174.67, "low": 2914.42, "close": 3156.94}, {"time": "2024-04-15", "open": 3156.83, "high": 3277.56, "low": 3026.54, "close": 3101.6}, {"time": "2024-04-16", "open": 3101.14, "high": 3127.16, "low": 2997.75, "close": 3084.92}, {"time": "2024-04-17", "open": 3084.92, "high": 3123.67, "low": 2918.55, "close": 2984.73}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-04-10**
- As-of date (T-1): **2026-03-03**
- Freshness age: **692 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 313.023, Previous 312.345, Delta +0.6780)
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
