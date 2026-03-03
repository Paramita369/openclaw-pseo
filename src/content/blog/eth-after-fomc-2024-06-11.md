---
title: "ETH After FOMC (2024-06-11): Historical T+1/T+7 Probability"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-06-11"
asof_date: "2025-01-29"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
confidence_level: "normal"
quality_score: 80
sample_size: 9
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.88
  mdd_t7: -2.13
  volatility: 0.0
  impact_t1_pct: 1.75
  impact_t7_pct: -0.42
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 1.2
    mean: 1.38
    sample: 9
  t7:
    up: 44.44
    down: 55.56
    median: -0.19
    mean: -0.1
    sample: 9
chartData: [{"time": "2024-06-08", "open": 3677.4, "high": 3707.5, "low": 3669.64, "close": 3680.95}, {"time": "2024-06-09", "open": 3680.94, "high": 3719.37, "low": 3668.12, "close": 3705.9}, {"time": "2024-06-10", "open": 3705.88, "high": 3711.43, "low": 3648.16, "close": 3666.72}, {"time": "2024-06-11", "open": 3666.36, "high": 3669.89, "low": 3434.75, "close": 3498.33}, {"time": "2024-06-12", "open": 3497.9, "high": 3652.49, "low": 3463.78, "close": 3559.62}, {"time": "2024-06-13", "open": 3559.73, "high": 3559.73, "low": 3431.33, "close": 3469.28}, {"time": "2024-06-14", "open": 3467.97, "high": 3528.6, "low": 3366.22, "close": 3480.27}, {"time": "2024-06-15", "open": 3479.79, "high": 3589.89, "low": 3473.45, "close": 3565.55}, {"time": "2024-06-16", "open": 3566.76, "high": 3648.09, "low": 3541.53, "close": 3620.56}, {"time": "2024-06-17", "open": 3622.38, "high": 3634.29, "low": 3468.15, "close": 3511.38}, {"time": "2024-06-18", "open": 3510.57, "high": 3514.18, "low": 3371.59, "close": 3483.68}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2024-06-11**
- As-of date (T-1): **2025-01-29**
- Sample size: **9**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 1.2% | 1.38% | 9 |
| T+7 | 44.44% | 55.56% | -0.19% | -0.1% | 9 |

## Historical Distribution Summary

T+1 Up Probability: **55.56%** (n=9)

T+7 Up Probability: **44.44%** (n=9)

T+7 Median Return: **-0.19%**

For ETH, historical FOMC windows currently show a T+1 up probability of 55.56% and a T+7 up probability of 44.44%. Median T+7 return is -0.19% across 9 samples. Current classification is Neutral, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
