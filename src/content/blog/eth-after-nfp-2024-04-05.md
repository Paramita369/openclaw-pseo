---
title: "ETH After NFP (2024-04-05): Historical T+1/T+7 Probability"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-04-05"
asof_date: "2025-01-10"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Bullish"
confidence_level: "normal"
quality_score: 90
sample_size: 13
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -9.82
  mdd_t7: -3.31
  volatility: 0.0
  impact_t1_pct: 1.06
  impact_t7_pct: -2.29
probabilities:
  sample_size: 13
  t1:
    up: 53.85
    down: 46.15
    median: 0.03
    mean: 0.11
    sample: 13
  t7:
    up: 61.54
    down: 38.46
    median: 5.12
    mean: 3.32
    sample: 13
chartData: [{"time": "2024-04-02", "open": 3504.82, "high": 3506.96, "low": 3215.99, "close": 3277.23}, {"time": "2024-04-03", "open": 3277.32, "high": 3368.11, "low": 3205.65, "close": 3311.44}, {"time": "2024-04-04", "open": 3311.5, "high": 3443.21, "low": 3253.32, "close": 3330.04}, {"time": "2024-04-05", "open": 3330.01, "high": 3345.67, "low": 3214.24, "close": 3318.89}, {"time": "2024-04-06", "open": 3318.86, "high": 3397.59, "low": 3308.98, "close": 3354.18}, {"time": "2024-04-07", "open": 3354.21, "high": 3458.51, "low": 3346.11, "close": 3453.49}, {"time": "2024-04-08", "open": 3453.5, "high": 3727.62, "low": 3409.51, "close": 3695.29}, {"time": "2024-04-09", "open": 3695.34, "high": 3724.92, "low": 3455.11, "close": 3505.16}, {"time": "2024-04-10", "open": 3505.16, "high": 3561.52, "low": 3415.18, "close": 3543.74}, {"time": "2024-04-11", "open": 3543.45, "high": 3616.19, "low": 3477.17, "close": 3505.25}, {"time": "2024-04-12", "open": 3505.33, "high": 3552.59, "low": 3103.43, "close": 3243.03}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2024-04-05**
- As-of date (T-1): **2025-01-10**
- Sample size: **13**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.03% | 0.11% | 13 |
| T+7 | 61.54% | 38.46% | 5.12% | 3.32% | 13 |

## Historical Distribution Summary

T+1 Up Probability: **53.85%** (n=13)

T+7 Up Probability: **61.54%** (n=13)

T+7 Median Return: **5.12%**

For ETH, historical NFP windows currently show a T+1 up probability of 53.85% and a T+7 up probability of 61.54%. Median T+7 return is 5.12% across 13 samples. Current classification is Bullish, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
