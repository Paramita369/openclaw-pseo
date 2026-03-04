---
title: "Historical Performance of BTC After NFP (2025-11-20)"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-11-20"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 0.23
robust_score: -5.77
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 34
freshness_days: 103
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158449.0
event_previous: 158408.0
event_delta: 41.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.75
  mdd_t7: -1.78
  volatility: 7.15
  impact_t1_pct: -1.78
  impact_t7_pct: 5.37
probabilities:
  sample_size: 34
  t1:
    up: 29.41
    down: 70.59
    median: -0.33
    mean: -0.26
    sample: 34
  t7:
    up: 58.82
    down: 41.18
    median: 1.0
    mean: 1.55
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 30
    t1:
      up: 26.67
      down: 73.33
      median: -0.39
      mean: -0.31
      sample: 30
    t7:
      up: 56.67
      down: 43.33
      median: 0.81
      mean: 1.51
      sample: 30
related_events: [{"slug": "btc-after-nfp-2026-02-11", "title": "BTC After NFP (2026-02-11): Historical T+1/T+7 Probability", "event_date": "2026-02-11", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.85, "sample_size": 0}, {"slug": "btc-after-nfp-2026-02-06", "title": "BTC After NFP (2026-02-06): Historical T+1/T+7 Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -2.41, "sample_size": 0}, {"slug": "btc-after-nfp-2026-01-09", "title": "BTC After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 5.54, "sample_size": 0}]
chartData: [{"time": "2025-11-17", "open": 94180.88, "high": 95928.37, "low": 91214.76, "close": 92093.88}, {"time": "2025-11-18", "open": 92094.53, "high": 93745.08, "low": 89300.46, "close": 92948.88}, {"time": "2025-11-19", "open": 92946.16, "high": 92946.16, "low": 88526.83, "close": 91465.99}, {"time": "2025-11-20", "open": 91459.35, "high": 93025.07, "low": 86040.8, "close": 86631.9}, {"time": "2025-11-21", "open": 86528.77, "high": 87380.8, "low": 80659.81, "close": 85090.69}, {"time": "2025-11-22", "open": 85098.56, "high": 85503.01, "low": 83490.9, "close": 84648.36}, {"time": "2025-11-23", "open": 84648.61, "high": 88038.47, "low": 84641.77, "close": 86805.01}, {"time": "2025-11-24", "open": 86798.77, "high": 89206.34, "low": 85272.2, "close": 88270.56}, {"time": "2025-11-25", "open": 88269.96, "high": 88457.34, "low": 86131.43, "close": 87341.89}, {"time": "2025-11-26", "open": 87345.59, "high": 90581.16, "low": 86316.9, "close": 90518.37}, {"time": "2025-11-27", "open": 90517.77, "high": 91897.58, "low": 90089.52, "close": 91285.38}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-11-20**
- As-of date (T-1): **2026-03-03**
- Freshness age: **103 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158449.0, Previous 158408.0, Delta +41.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 29.41% | 70.59% | -0.33% | -0.26% | 34 |
| T+7 | 58.82% | 41.18% | 1.0% | 1.55% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 26.67% | 73.33% | -0.39% | -0.31% | 30 |
| T+7 | 56.67% | 43.33% | 0.81% | 1.51% | 30 |

## Historical Distribution Summary

When NFP was **UP**, BTC T+1 up probability was **26.67%** (n=30).

When NFP was **UP**, BTC T+7 up probability was **56.67%** (n=30).

Same-direction T+7 median return: **0.81%**.

For BTC, historical NFP windows show all-history T+1 up probability of 29.41% and T+7 up probability of 58.82%. When NFP printed Up versus previous, T+1 up probability was 26.67% and T+7 up probability was 56.67% across 30 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
