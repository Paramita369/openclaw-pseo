---
title: "BTC After NFP (2024-04-05): Historical T+1/T+7 Probability"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-04-05"
asof_date: "2025-01-10"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
confidence_level: "normal"
quality_score: 90
sample_size: 13
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -4.3
  mdd_t7: -2.47
  volatility: 0.0
  impact_t1_pct: 1.56
  impact_t7_pct: -0.95
probabilities:
  sample_size: 13
  t1:
    up: 38.46
    down: 61.54
    median: -0.05
    mean: 0.25
    sample: 13
  t7:
    up: 61.54
    down: 38.46
    median: 1.54
    mean: 3.29
    sample: 13
chartData: [{"time": "2024-04-02", "open": 69705.02, "high": 69708.38, "low": 64586.59, "close": 65446.97}, {"time": "2024-04-03", "open": 65446.67, "high": 66914.32, "low": 64559.9, "close": 65980.81}, {"time": "2024-04-04", "open": 65975.7, "high": 69291.26, "low": 65113.8, "close": 68508.84}, {"time": "2024-04-05", "open": 68515.76, "high": 68725.76, "low": 66011.48, "close": 67837.64}, {"time": "2024-04-06", "open": 67840.57, "high": 69629.6, "low": 67491.72, "close": 68896.11}, {"time": "2024-04-07", "open": 68897.11, "high": 70284.43, "low": 68851.63, "close": 69362.55}, {"time": "2024-04-08", "open": 69362.55, "high": 72715.36, "low": 69064.24, "close": 71631.36}, {"time": "2024-04-09", "open": 71632.5, "high": 71742.51, "low": 68212.92, "close": 69139.02}, {"time": "2024-04-10", "open": 69140.24, "high": 71093.43, "low": 67503.56, "close": 70587.88}, {"time": "2024-04-11", "open": 70575.73, "high": 71256.23, "low": 69571.81, "close": 70060.61}, {"time": "2024-04-12", "open": 70061.38, "high": 71222.74, "low": 65254.84, "close": 67195.87}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2024-04-05**
- As-of date (T-1): **2025-01-10**
- Sample size: **13**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 38.46% | 61.54% | -0.05% | 0.25% | 13 |
| T+7 | 61.54% | 38.46% | 1.54% | 3.29% | 13 |

## Historical Distribution Summary

T+1 Up Probability: **38.46%** (n=13)

T+7 Up Probability: **61.54%** (n=13)

T+7 Median Return: **1.54%**

For BTC, historical NFP windows currently show a T+1 up probability of 38.46% and a T+7 up probability of 61.54%. Median T+7 return is 1.54% across 13 samples. Current classification is Neutral, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
