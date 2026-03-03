---
title: "QQQ After FOMC (2024-12-17): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-12-17"
asof_date: "2025-01-29"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
confidence_level: "normal"
quality_score: 80
sample_size: 9
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -2.06
  mdd_t7: -3.61
  volatility: 0.0
  impact_t1_pct: -3.61
  impact_t7_pct: -0.93
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
chartData: [{"time": "2024-12-16", "open": 529.54, "high": 535.57, "low": 529.46, "close": 534.59}, {"time": "2024-12-17", "open": 532.79, "high": 533.91, "low": 530.58, "close": 532.24}, {"time": "2024-12-18", "open": 531.59, "high": 533.31, "low": 511.59, "close": 513.04}, {"time": "2024-12-19", "open": 517.73, "high": 518.29, "low": 510.41, "close": 510.75}, {"time": "2024-12-20", "open": 507.05, "high": 521.33, "low": 505.9, "close": 515.21}, {"time": "2024-12-23", "open": 516.93, "high": 520.61, "low": 513.53, "close": 520.23}, {"time": "2024-12-24", "open": 522.18, "high": 527.38, "low": 521.54, "close": 527.29}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
- Event date: **2024-12-17**
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
