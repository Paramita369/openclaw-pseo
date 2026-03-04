---
title: "Historical Performance of ETH After CPI (2026-01-13)"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-01-13"
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
freshness_days: 49
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 326.588
event_previous: 326.031
event_delta: 0.557
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -0.92
  mdd_t7: -11.63
  volatility: 12.62
  impact_t1_pct: 0.98
  impact_t7_pct: -11.63
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
chartData: [{"time": "2026-01-10", "open": 3083.17, "high": 3099.17, "low": 3075.14, "close": 3082.4}, {"time": "2026-01-11", "open": 3082.41, "high": 3141.96, "low": 3080.75, "close": 3118.89}, {"time": "2026-01-12", "open": 3118.83, "high": 3166.22, "low": 3068.07, "close": 3092.33}, {"time": "2026-01-13", "open": 3092.01, "high": 3352.58, "low": 3088.51, "close": 3322.1}, {"time": "2026-01-14", "open": 3322.19, "high": 3397.9, "low": 3280.38, "close": 3354.72}, {"time": "2026-01-15", "open": 3354.77, "high": 3382.45, "low": 3276.82, "close": 3317.1}, {"time": "2026-01-16", "open": 3317.34, "high": 3325.25, "low": 3251.81, "close": 3295.48}, {"time": "2026-01-17", "open": 3295.48, "high": 3328.28, "low": 3282.66, "close": 3308.86}, {"time": "2026-01-18", "open": 3308.91, "high": 3367.17, "low": 3278.43, "close": 3281.16}, {"time": "2026-01-19", "open": 3282.2, "high": 3282.65, "low": 3166.02, "close": 3186.62}, {"time": "2026-01-20", "open": 3186.62, "high": 3197.39, "low": 2925.54, "close": 2935.61}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2026-01-13**
- As-of date (T-1): **2026-03-03**
- Freshness age: **49 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.588, Previous 326.031, Delta +0.5570)
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
