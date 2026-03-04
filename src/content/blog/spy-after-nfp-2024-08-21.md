---
title: "Historical Performance of SPY After NFP (2024-08-21)"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-08-21"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 4.23
robust_score: -1.77
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 34
freshness_days: 559
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 157757.0
event_previous: 157748.0
event_delta: 9.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -1.12
  mdd_t7: -0.78
  volatility: 0.37
  impact_t1_pct: -0.78
  impact_t7_pct: -0.41
probabilities:
  sample_size: 34
  t1:
    up: 47.62
    down: 52.38
    median: -0.04
    mean: -0.1
    sample: 21
  t7:
    up: 55.88
    down: 44.12
    median: 0.11
    mean: 0.81
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 18
    t1:
      up: 38.89
      down: 61.11
      median: -0.13
      mean: -0.22
      sample: 18
    t7:
      up: 56.67
      down: 43.33
      median: 0.11
      mean: 0.83
      sample: 30
related_events: [{"slug": "spy-after-nfp-2024-07-05", "title": "SPY After NFP (2024-07-05): Historical T+1/T+7 Probability", "event_date": "2024-07-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.02, "median_t7_pct": 0.96, "sample_size": 0}, {"slug": "spy-after-nfp-2024-01-05", "title": "SPY After NFP (2024-01-05): Historical T+1/T+7 Probability", "event_date": "2024-01-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.04, "median_t7_pct": 1.87, "sample_size": 0}, {"slug": "spy-after-nfp-2024-10-04", "title": "SPY After NFP (2024-10-04): Historical T+1/T+7 Probability", "event_date": "2024-10-04", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.43, "median_t7_pct": 1.15, "sample_size": 0}]
chartData: [{"time": "2024-08-19", "open": 544.78, "high": 549.57, "low": 543.93, "close": 549.57}, {"time": "2024-08-20", "open": 549.12, "high": 550.78, "low": 547.33, "close": 548.68}, {"time": "2024-08-21", "open": 549.73, "high": 552.03, "low": 544.78, "close": 550.57}, {"time": "2024-08-22", "open": 552.47, "high": 553.08, "low": 545.03, "close": 546.24}, {"time": "2024-08-23", "open": 549.5, "high": 552.99, "low": 547.3, "close": 552.05}, {"time": "2024-08-26", "open": 553.08, "high": 553.8, "low": 549.02, "close": 550.73}, {"time": "2024-08-27", "open": 549.46, "high": 551.98, "low": 548.31, "close": 551.49}, {"time": "2024-08-28", "open": 551.14, "high": 551.58, "low": 545.09, "close": 548.29}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2024-08-21**
- As-of date (T-1): **2026-03-03**
- Freshness age: **559 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157757.0, Previous 157748.0, Delta +9.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 47.62% | 52.38% | -0.04% | -0.1% | 21 |
| T+7 | 55.88% | 44.12% | 0.11% | 0.81% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 38.89% | 61.11% | -0.13% | -0.22% | 18 |
| T+7 | 56.67% | 43.33% | 0.11% | 0.83% | 30 |

## Historical Distribution Summary

When NFP was **UP**, SPY T+1 up probability was **38.89%** (n=18).

When NFP was **UP**, SPY T+7 up probability was **56.67%** (n=30).

Same-direction T+7 median return: **0.11%**.

For SPY, historical NFP windows show all-history T+1 up probability of 47.62% and T+7 up probability of 55.88%. When NFP printed Up versus previous, T+1 up probability was 38.89% and T+7 up probability was 56.67% across 18 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
