---
title: "ETH After CPI (2024-06-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-06-12"
asof_date: "2025-02-12"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
confidence_level: "normal"
quality_score: 90
sample_size: 14
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.22
  mdd_t7: -2.54
  volatility: 0.0
  impact_t1_pct: -2.54
  impact_t7_pct: -0.01
probabilities:
  sample_size: 14
  t1:
    up: 50.0
    down: 50.0
    median: -0.22
    mean: -0.52
    sample: 14
  t7:
    up: 42.86
    down: 57.14
    median: -0.39
    mean: 0.26
    sample: 14
chartData: [{"time": "2024-06-09", "open": 3680.94, "high": 3719.37, "low": 3668.12, "close": 3705.9}, {"time": "2024-06-10", "open": 3705.88, "high": 3711.43, "low": 3648.16, "close": 3666.72}, {"time": "2024-06-11", "open": 3666.36, "high": 3669.89, "low": 3434.75, "close": 3498.33}, {"time": "2024-06-12", "open": 3497.9, "high": 3652.49, "low": 3463.78, "close": 3559.62}, {"time": "2024-06-13", "open": 3559.73, "high": 3559.73, "low": 3431.33, "close": 3469.28}, {"time": "2024-06-14", "open": 3467.97, "high": 3528.6, "low": 3366.22, "close": 3480.27}, {"time": "2024-06-15", "open": 3479.79, "high": 3589.89, "low": 3473.45, "close": 3565.55}, {"time": "2024-06-16", "open": 3566.76, "high": 3648.09, "low": 3541.53, "close": 3620.56}, {"time": "2024-06-17", "open": 3622.38, "high": 3634.29, "low": 3468.15, "close": 3511.38}, {"time": "2024-06-18", "open": 3510.57, "high": 3514.18, "low": 3371.59, "close": 3483.68}, {"time": "2024-06-19", "open": 3482.35, "high": 3583.32, "low": 3466.48, "close": 3559.35}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-06-12**
- As-of date (T-1): **2025-02-12**
- Sample size: **14**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.22% | -0.52% | 14 |
| T+7 | 42.86% | 57.14% | -0.39% | 0.26% | 14 |

## Historical Distribution Summary

T+1 Up Probability: **50.0%** (n=14)

T+7 Up Probability: **42.86%** (n=14)

T+7 Median Return: **-0.39%**

For ETH, historical CPI windows currently show a T+1 up probability of 50.0% and a T+7 up probability of 42.86%. Median T+7 return is -0.39% across 14 samples. Current classification is Neutral, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
