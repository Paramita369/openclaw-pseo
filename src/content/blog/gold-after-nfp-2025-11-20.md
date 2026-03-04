---
title: "Historical Performance of GOLD After NFP (2025-11-20)"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-11-20"
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
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.14
  mdd_t7: 0.0
  volatility: 3.49
  impact_t1_pct: 0.5
  impact_t7_pct: 3.99
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
chartData: [{"time": "2025-11-17", "open": 4070.0, "high": 4099.5, "low": 4019.4, "close": 4068.3}, {"time": "2025-11-18", "open": 4037.4, "high": 4063.4, "low": 4035.6, "close": 4061.3}, {"time": "2025-11-19", "open": 4086.1, "high": 4122.7, "low": 4072.0, "close": 4077.7}, {"time": "2025-11-20", "open": 4045.0, "high": 4090.4, "low": 4040.2, "close": 4056.5}, {"time": "2025-11-21", "open": 4031.8, "high": 4085.2, "low": 4031.8, "close": 4076.7}, {"time": "2025-11-24", "open": 4060.5, "high": 4091.9, "low": 4060.5, "close": 4091.9}, {"time": "2025-11-25", "open": 4139.2, "high": 4139.2, "low": 4139.2, "close": 4139.2}, {"time": "2025-11-26", "open": 4128.6, "high": 4171.0, "low": 4127.5, "close": 4165.2}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
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
