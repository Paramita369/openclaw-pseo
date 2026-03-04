---
title: "Historical Performance of GOLD After NFP (2024-12-06)"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-12-06"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 21.71
robust_score: 15.71
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 34
freshness_days: 452
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158316.0
event_previous: 158079.0
event_delta: 237.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 7.33
  mdd_t7: 0.0
  volatility: 0.09
  impact_t1_pct: 0.57
  impact_t7_pct: 0.66
probabilities:
  sample_size: 34
  t1:
    up: 66.67
    down: 33.33
    median: 0.5
    mean: 0.57
    sample: 21
  t7:
    up: 79.41
    down: 20.59
    median: 1.31
    mean: 1.61
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 18
    t1:
      up: 61.11
      down: 38.89
      median: 0.34
      mean: 0.51
      sample: 18
    t7:
      up: 76.67
      down: 23.33
      median: 1.1
      mean: 1.49
      sample: 30
related_events: [{"slug": "gold-after-nfp-2024-03-01", "title": "GOLD After NFP (2024-03-01): Historical T+1/T+7 Probability", "event_date": "2024-03-01", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.57, "median_t7_pct": 4.39, "sample_size": 0}, {"slug": "gold-after-nfp-2024-04-05", "title": "GOLD After NFP (2024-04-05): Historical T+1/T+7 Probability", "event_date": "2024-04-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 4.16, "median_t7_pct": 1.31, "sample_size": 0}, {"slug": "gold-after-nfp-2024-09-06", "title": "GOLD After NFP (2024-09-06): Historical T+1/T+7 Probability", "event_date": "2024-09-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 1.09, "median_t7_pct": 3.52, "sample_size": 0}]
chartData: [{"time": "2024-12-03", "open": 2639.0, "high": 2654.7, "low": 2636.0, "close": 2644.7}, {"time": "2024-12-04", "open": 2639.2, "high": 2658.3, "low": 2637.0, "close": 2653.8}, {"time": "2024-12-05", "open": 2652.4, "high": 2655.0, "low": 2625.7, "close": 2626.6}, {"time": "2024-12-06", "open": 2620.2, "high": 2643.1, "low": 2617.5, "close": 2638.6}, {"time": "2024-12-09", "open": 2632.1, "high": 2677.1, "low": 2630.8, "close": 2664.9}, {"time": "2024-12-10", "open": 2662.3, "high": 2698.2, "low": 2661.0, "close": 2697.6}, {"time": "2024-12-11", "open": 2701.8, "high": 2733.8, "low": 2693.1, "close": 2733.8}, {"time": "2024-12-12", "open": 2725.1, "high": 2725.1, "low": 2677.4, "close": 2687.5}, {"time": "2024-12-13", "open": 2688.2, "high": 2689.3, "low": 2647.9, "close": 2656.0}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
- Event date: **2024-12-06**
- As-of date (T-1): **2026-03-03**
- Freshness age: **452 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158316.0, Previous 158079.0, Delta +237.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 66.67% | 33.33% | 0.5% | 0.57% | 21 |
| T+7 | 79.41% | 20.59% | 1.31% | 1.61% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 61.11% | 38.89% | 0.34% | 0.51% | 18 |
| T+7 | 76.67% | 23.33% | 1.1% | 1.49% | 30 |

## Historical Distribution Summary

When NFP was **UP**, GOLD T+1 up probability was **61.11%** (n=18).

When NFP was **UP**, GOLD T+7 up probability was **76.67%** (n=30).

Same-direction T+7 median return: **1.1%**.

For GOLD, historical NFP windows show all-history T+1 up probability of 66.67% and T+7 up probability of 79.41%. When NFP printed Up versus previous, T+1 up probability was 61.11% and T+7 up probability was 76.67% across 18 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
