---
title: "BTC After NFP (2024-05-03): Historical T+1/T+7 Probability"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-05-03"
asof_date: "2025-01-10"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
confidence_level: "normal"
quality_score: 90
sample_size: 13
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -9.66
  mdd_t7: -4.85
  volatility: 0.0
  impact_t1_pct: 1.59
  impact_t7_pct: -3.33
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
chartData: [{"time": "2024-04-30", "open": 63839.42, "high": 64703.33, "low": 59120.07, "close": 60636.86}, {"time": "2024-05-01", "open": 60609.5, "high": 60780.5, "low": 56555.29, "close": 58254.01}, {"time": "2024-05-02", "open": 58253.7, "high": 59602.3, "low": 56937.2, "close": 59123.43}, {"time": "2024-05-03", "open": 59122.3, "high": 63320.5, "low": 58848.31, "close": 62889.84}, {"time": "2024-05-04", "open": 62891.03, "high": 64494.96, "low": 62599.35, "close": 63891.47}, {"time": "2024-05-05", "open": 63892.45, "high": 64610.89, "low": 62955.3, "close": 64031.13}, {"time": "2024-05-06", "open": 64038.31, "high": 65494.9, "low": 62746.24, "close": 63161.95}, {"time": "2024-05-07", "open": 63162.76, "high": 64390.46, "low": 62285.98, "close": 62334.82}, {"time": "2024-05-08", "open": 62332.64, "high": 62986.09, "low": 60877.13, "close": 61187.94}, {"time": "2024-05-09", "open": 61191.2, "high": 63404.91, "low": 60648.07, "close": 63049.96}, {"time": "2024-05-10", "open": 63055.19, "high": 63446.74, "low": 60208.78, "close": 60792.78}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2024-05-03**
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
