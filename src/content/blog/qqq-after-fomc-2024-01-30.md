---
title: "QQQ After FOMC (2024-01-30): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-01-30"
asof_date: "2025-01-29"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
confidence_level: "normal"
quality_score: 80
sample_size: 9
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 2.07
  mdd_t7: -1.96
  volatility: 0.0
  impact_t1_pct: -1.96
  impact_t7_pct: 0.54
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 0.43
    mean: 0.08
    sample: 9
  t7:
    up: 77.78
    down: 22.22
    median: 1.16
    mean: 1.03
    sample: 9
chartData: [{"time": "2024-01-29", "open": 419.64, "high": 423.67, "low": 418.98, "close": 423.47}, {"time": "2024-01-30", "open": 422.43, "high": 423.01, "low": 419.74, "close": 420.65}, {"time": "2024-01-31", "open": 416.25, "high": 418.25, "low": 412.24, "close": 412.42}, {"time": "2024-02-01", "open": 414.22, "high": 417.77, "low": 413.25, "close": 417.27}, {"time": "2024-02-02", "open": 419.17, "high": 425.54, "low": 418.17, "close": 424.32}, {"time": "2024-02-05", "open": 424.38, "high": 424.92, "low": 420.36, "close": 423.77}, {"time": "2024-02-06", "open": 424.92, "high": 425.52, "low": 420.57, "close": 422.92}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
- Event date: **2024-01-30**
- As-of date (T-1): **2025-01-29**
- Sample size: **9**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.43% | 0.08% | 9 |
| T+7 | 77.78% | 22.22% | 1.16% | 1.03% | 9 |

## Historical Distribution Summary

T+1 Up Probability: **55.56%** (n=9)

T+7 Up Probability: **77.78%** (n=9)

T+7 Median Return: **1.16%**

For QQQ, historical FOMC windows currently show a T+1 up probability of 55.56% and a T+7 up probability of 77.78%. Median T+7 return is 1.16% across 9 samples. Current classification is Bullish, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
