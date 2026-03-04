---
title: "Historical Performance of ETH After CPI (2025-08-12)"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-08-12"
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
freshness_days: 203
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 323.291
event_previous: 322.169
event_delta: 1.122
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -0.76
  mdd_t7: -11.27
  volatility: 14.87
  impact_t1_pct: 3.6
  impact_t7_pct: -11.27
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
chartData: [{"time": "2025-08-09", "open": 4009.15, "high": 4323.76, "low": 4007.71, "close": 4263.6}, {"time": "2025-08-10", "open": 4263.55, "high": 4332.21, "low": 4163.94, "close": 4254.22}, {"time": "2025-08-11", "open": 4254.23, "high": 4362.09, "low": 4168.88, "close": 4226.97}, {"time": "2025-08-12", "open": 4227.21, "high": 4634.06, "low": 4222.36, "close": 4590.92}, {"time": "2025-08-13", "open": 4590.66, "high": 4784.67, "low": 4566.24, "close": 4756.28}, {"time": "2025-08-14", "open": 4756.04, "high": 4788.55, "low": 4461.28, "close": 4548.17}, {"time": "2025-08-15", "open": 4549.08, "high": 4667.73, "low": 4375.55, "close": 4439.99}, {"time": "2025-08-16", "open": 4440.0, "high": 4493.15, "low": 4379.16, "close": 4426.18}, {"time": "2025-08-17", "open": 4426.26, "high": 4575.88, "low": 4400.71, "close": 4473.27}, {"time": "2025-08-18", "open": 4473.33, "high": 4484.01, "low": 4229.38, "close": 4312.5}, {"time": "2025-08-19", "open": 4312.53, "high": 4355.08, "low": 4070.54, "close": 4073.46}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2025-08-12**
- As-of date (T-1): **2026-03-03**
- Freshness age: **203 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 323.291, Previous 322.169, Delta +1.1220)
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
