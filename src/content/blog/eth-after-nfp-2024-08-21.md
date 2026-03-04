---
title: "Historical Performance of ETH After NFP (2024-08-21)"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-08-21"
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
freshness_days: 559
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 157757.0
event_previous: 157748.0
event_delta: 9.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -1.09
  mdd_t7: -3.91
  volatility: 3.59
  impact_t1_pct: -0.32
  impact_t7_pct: -3.91
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
chartData: [{"time": "2024-08-18", "open": 2614.11, "high": 2684.03, "low": 2596.74, "close": 2613.36}, {"time": "2024-08-19", "open": 2612.72, "high": 2648.28, "low": 2566.4, "close": 2637.31}, {"time": "2024-08-20", "open": 2637.31, "high": 2695.91, "low": 2556.75, "close": 2573.11}, {"time": "2024-08-21", "open": 2573.11, "high": 2662.95, "low": 2538.66, "close": 2631.4}, {"time": "2024-08-22", "open": 2630.86, "high": 2644.82, "low": 2587.11, "close": 2622.95}, {"time": "2024-08-23", "open": 2622.92, "high": 2799.33, "low": 2622.58, "close": 2764.45}, {"time": "2024-08-24", "open": 2765.48, "high": 2820.02, "low": 2737.78, "close": 2769.39}, {"time": "2024-08-25", "open": 2769.1, "high": 2793.01, "low": 2736.09, "close": 2749.16}, {"time": "2024-08-26", "open": 2749.25, "high": 2763.0, "low": 2668.89, "close": 2681.34}, {"time": "2024-08-27", "open": 2681.62, "high": 2700.15, "low": 2401.18, "close": 2458.73}, {"time": "2024-08-28", "open": 2458.9, "high": 2553.82, "low": 2422.29, "close": 2528.42}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
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
