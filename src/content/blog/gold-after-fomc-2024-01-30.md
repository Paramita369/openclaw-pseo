---
title: "GOLD After FOMC (2024-01-30): Historical T+1/T+7 Probability"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
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
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 1.61
  mdd_t7: -0.68
  volatility: 0.0
  impact_t1_pct: 0.83
  impact_t7_pct: 0.15
probabilities:
  sample_size: 9
  t1:
    up: 88.89
    down: 11.11
    median: 0.83
    mean: 0.72
    sample: 9
  t7:
    up: 66.67
    down: 33.33
    median: 0.9
    mean: 0.59
    sample: 9
chartData: [{"time": "2024-01-29", "open": 2025.2, "high": 2025.2, "low": 2025.2, "close": 2025.2}, {"time": "2024-01-30", "open": 2032.5, "high": 2048.5, "low": 2028.1, "close": 2031.5}, {"time": "2024-01-31", "open": 2035.4, "high": 2055.0, "low": 2030.0, "close": 2048.4}, {"time": "2024-02-01", "open": 2040.2, "high": 2064.5, "low": 2029.0, "close": 2053.0}, {"time": "2024-02-02", "open": 2054.8, "high": 2055.9, "low": 2027.7, "close": 2036.1}, {"time": "2024-02-05", "open": 2038.9, "high": 2040.8, "low": 2013.8, "close": 2025.7}, {"time": "2024-02-06", "open": 2025.9, "high": 2037.3, "low": 2025.9, "close": 2034.5}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2024-01-30**
- As-of date (T-1): **2025-01-29**
- Sample size: **9**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 88.89% | 11.11% | 0.83% | 0.72% | 9 |
| T+7 | 66.67% | 33.33% | 0.9% | 0.59% | 9 |

## Historical Distribution Summary

T+1 Up Probability: **88.89%** (n=9)

T+7 Up Probability: **66.67%** (n=9)

T+7 Median Return: **0.9%**

For GOLD, historical FOMC windows currently show a T+1 up probability of 88.89% and a T+7 up probability of 66.67%. Median T+7 return is 0.9% across 9 samples. Current classification is Bullish, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
