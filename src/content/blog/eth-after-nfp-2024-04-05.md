---
title: "Historical Performance of ETH After NFP (2024-04-05)"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-04-05"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 4.94
robust_score: -1.06
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 34
freshness_days: 697
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 157530.0
event_previous: 157466.0
event_delta: 64.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -9.82
  mdd_t7: -3.31
  volatility: 3.35
  impact_t1_pct: 1.06
  impact_t7_pct: -2.29
probabilities:
  sample_size: 34
  t1:
    up: 50.0
    down: 50.0
    median: 0.0
    mean: -0.15
    sample: 34
  t7:
    up: 55.88
    down: 44.12
    median: 1.44
    mean: 2.65
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 30
    t1:
      up: 50.0
      down: 50.0
      median: 0.0
      mean: -0.14
      sample: 30
    t7:
      up: 53.33
      down: 46.67
      median: 0.79
      mean: 2.65
      sample: 30
related_events: [{"slug": "eth-after-nfp-2026-02-11", "title": "ETH After NFP (2026-02-11): Historical T+1/T+7 Probability", "event_date": "2026-02-11", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.69, "sample_size": 0}, {"slug": "eth-after-nfp-2026-02-06", "title": "ETH After NFP (2026-02-06): Historical T+1/T+7 Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.72, "sample_size": 0}, {"slug": "eth-after-nfp-2026-01-09", "title": "ETH After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 6.89, "sample_size": 0}]
chartData: [{"time": "2024-04-02", "open": 3504.82, "high": 3506.96, "low": 3215.99, "close": 3277.23}, {"time": "2024-04-03", "open": 3277.32, "high": 3368.11, "low": 3205.65, "close": 3311.44}, {"time": "2024-04-04", "open": 3311.5, "high": 3443.21, "low": 3253.32, "close": 3330.04}, {"time": "2024-04-05", "open": 3330.01, "high": 3345.67, "low": 3214.24, "close": 3318.89}, {"time": "2024-04-06", "open": 3318.86, "high": 3397.59, "low": 3308.98, "close": 3354.18}, {"time": "2024-04-07", "open": 3354.21, "high": 3458.51, "low": 3346.11, "close": 3453.49}, {"time": "2024-04-08", "open": 3453.5, "high": 3727.62, "low": 3409.51, "close": 3695.29}, {"time": "2024-04-09", "open": 3695.34, "high": 3724.92, "low": 3455.11, "close": 3505.16}, {"time": "2024-04-10", "open": 3505.16, "high": 3561.52, "low": 3415.18, "close": 3543.74}, {"time": "2024-04-11", "open": 3543.45, "high": 3616.19, "low": 3477.17, "close": 3505.25}, {"time": "2024-04-12", "open": 3505.33, "high": 3552.59, "low": 3103.43, "close": 3243.03}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2024-04-05**
- As-of date (T-1): **2026-03-03**
- Freshness age: **697 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157530.0, Previous 157466.0, Delta +64.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.15% | 34 |
| T+7 | 55.88% | 44.12% | 1.44% | 2.65% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.14% | 30 |
| T+7 | 53.33% | 46.67% | 0.79% | 2.65% | 30 |

## Historical Distribution Summary

When NFP was **UP**, ETH T+1 up probability was **50.0%** (n=30).

When NFP was **UP**, ETH T+7 up probability was **53.33%** (n=30).

Same-direction T+7 median return: **0.79%**.

For ETH, historical NFP windows show all-history T+1 up probability of 50.0% and T+7 up probability of 55.88%. When NFP printed Up versus previous, T+1 up probability was 50.0% and T+7 up probability was 53.33% across 30 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
