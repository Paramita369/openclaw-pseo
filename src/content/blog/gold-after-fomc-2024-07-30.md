---
title: "GOLD After FOMC (2024-07-30): Historical T+1/T+7 Probability"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
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
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -4.22
  mdd_t7: -1.54
  volatility: 0.0
  impact_t1_pct: 0.89
  impact_t7_pct: -0.66
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
chartData: [{"time": "2024-07-29", "open": 2377.3, "high": 2377.3, "low": 2377.3, "close": 2377.3}, {"time": "2024-07-30", "open": 2380.9, "high": 2409.3, "low": 2373.8, "close": 2405.0}, {"time": "2024-07-31", "open": 2407.1, "high": 2447.6, "low": 2402.8, "close": 2426.5}, {"time": "2024-08-01", "open": 2446.7, "high": 2455.1, "low": 2430.4, "close": 2435.0}, {"time": "2024-08-02", "open": 2444.0, "high": 2477.0, "low": 2416.0, "close": 2425.7}, {"time": "2024-08-05", "open": 2442.0, "high": 2449.8, "low": 2367.4, "close": 2401.7}, {"time": "2024-08-06", "open": 2414.5, "high": 2421.8, "low": 2380.0, "close": 2389.1}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2024-07-30**
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
