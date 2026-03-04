---
title: "Historical Performance of BTC After NFP (2024-11-01)"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-11-01"
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
freshness_days: 487
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158079.0
event_previous: 157945.0
event_delta: 134.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.97
  mdd_t7: -0.28
  volatility: 10.45
  impact_t1_pct: -0.28
  impact_t7_pct: 10.17
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
chartData: [{"time": "2024-10-29", "open": 69910.05, "high": 73577.21, "low": 69729.91, "close": 72720.49}, {"time": "2024-10-30", "open": 72715.37, "high": 72905.3, "low": 71411.73, "close": 72339.54}, {"time": "2024-10-31", "open": 72335.05, "high": 72662.31, "low": 69590.5, "close": 70215.19}, {"time": "2024-11-01", "open": 70216.9, "high": 71559.02, "low": 68779.7, "close": 69482.47}, {"time": "2024-11-02", "open": 69486.02, "high": 69867.35, "low": 69033.72, "close": 69289.27}, {"time": "2024-11-03", "open": 69296.38, "high": 69361.66, "low": 67482.52, "close": 68741.12}, {"time": "2024-11-04", "open": 68742.13, "high": 69433.18, "low": 66803.65, "close": 67811.51}, {"time": "2024-11-05", "open": 67811.17, "high": 70522.79, "low": 67458.87, "close": 69359.56}, {"time": "2024-11-06", "open": 69358.5, "high": 76460.16, "low": 69322.03, "close": 75639.08}, {"time": "2024-11-07", "open": 75637.09, "high": 76943.12, "low": 74480.42, "close": 75904.86}, {"time": "2024-11-08", "open": 75902.84, "high": 77252.75, "low": 75648.74, "close": 76545.48}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2024-11-01**
- As-of date (T-1): **2026-03-03**
- Freshness age: **487 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158079.0, Previous 157945.0, Delta +134.0000)
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
