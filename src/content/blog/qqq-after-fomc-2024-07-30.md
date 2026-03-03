---
title: "QQQ After FOMC (2024-07-30): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-07-30"
asof_date: "2025-01-29"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
confidence_level: "normal"
quality_score: 80
sample_size: 9
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -6.14
  mdd_t7: -6.7
  volatility: 0.0
  impact_t1_pct: 2.96
  impact_t7_pct: -3.93
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
chartData: [{"time": "2024-07-29", "open": 461.96, "high": 464.15, "low": 457.91, "close": 460.17}, {"time": "2024-07-30", "open": 462.1, "high": 462.81, "low": 450.5, "close": 453.85}, {"time": "2024-07-31", "open": 464.11, "high": 468.99, "low": 462.66, "close": 467.28}, {"time": "2024-08-01", "open": 467.97, "high": 471.73, "low": 452.31, "close": 455.96}, {"time": "2024-08-02", "open": 447.26, "high": 449.92, "low": 440.9, "close": 445.14}, {"time": "2024-08-05", "open": 421.29, "high": 438.73, "low": 420.04, "close": 431.87}, {"time": "2024-08-06", "open": 433.71, "high": 443.47, "low": 431.07, "close": 436.0}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
- Event date: **2024-07-30**
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
