---
title: "Historical Performance of GOLD After NFP (2024-10-04)"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-10-04"
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
freshness_days: 515
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 157945.0
event_previous: 157912.0
event_delta: 33.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -6.49
  mdd_t7: -8.11
  volatility: 0.12
  impact_t1_pct: 0.57
  impact_t7_pct: 0.45
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
chartData: [{"time": "2024-10-01", "open": 2631.4, "high": 2670.9, "low": 2631.4, "close": 2667.3}, {"time": "2024-10-02", "open": 2650.6, "high": 2657.2, "low": 2640.0, "close": 2647.1}, {"time": "2024-10-03", "open": 2642.8, "high": 2657.1, "low": 2640.0, "close": 2657.1}, {"time": "2024-10-04", "open": 2656.0, "high": 2667.0, "low": 2639.0, "close": 2645.8}, {"time": "2024-10-07", "open": 2648.7, "high": 2657.4, "low": 2639.0, "close": 2644.8}, {"time": "2024-10-08", "open": 2639.0, "high": 2639.0, "low": 2609.3, "close": 2615.0}, {"time": "2024-10-09", "open": 2603.0, "high": 2607.7, "low": 2603.0, "close": 2606.0}, {"time": "2024-10-10", "open": 2602.5, "high": 2628.3, "low": 2602.5, "close": 2620.6}, {"time": "2024-10-11", "open": 2638.3, "high": 2658.1, "low": 2638.2, "close": 2657.6}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
- Event date: **2024-10-04**
- As-of date (T-1): **2026-03-03**
- Freshness age: **515 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157945.0, Previous 157912.0, Delta +33.0000)
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
