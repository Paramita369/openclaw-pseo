---
title: "Historical Performance of BTC After NFP (2024-08-21)"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-08-21"
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
freshness_days: 559
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 157757.0
event_previous: 157748.0
event_delta: 9.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -1.59
  mdd_t7: -3.51
  volatility: 2.21
  impact_t1_pct: -1.3
  impact_t7_pct: -3.51
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
chartData: [{"time": "2024-08-18", "open": 59468.13, "high": 60262.72, "low": 58445.4, "close": 58483.96}, {"time": "2024-08-19", "open": 58480.71, "high": 59612.66, "low": 57864.71, "close": 59493.45}, {"time": "2024-08-20", "open": 59493.45, "high": 61396.33, "low": 58610.88, "close": 59012.79}, {"time": "2024-08-21", "open": 59014.99, "high": 61834.35, "low": 58823.45, "close": 61175.19}, {"time": "2024-08-22", "open": 61168.32, "high": 61408.11, "low": 59815.25, "close": 60381.91}, {"time": "2024-08-23", "open": 60380.95, "high": 64947.06, "low": 60372.05, "close": 64094.36}, {"time": "2024-08-24", "open": 64103.87, "high": 64513.79, "low": 63619.92, "close": 64178.99}, {"time": "2024-08-25", "open": 64176.37, "high": 64996.42, "low": 63833.52, "close": 64333.54}, {"time": "2024-08-26", "open": 64342.23, "high": 64489.71, "low": 62849.56, "close": 62880.66}, {"time": "2024-08-27", "open": 62879.71, "high": 63210.8, "low": 58116.75, "close": 59504.13}, {"time": "2024-08-28", "open": 59507.93, "high": 60236.45, "low": 57890.68, "close": 59027.62}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
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
