---
title: "SPY After FOMC (2024-01-30): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around FOMC events (T+1/T+7)."
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
tags: ["spy", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 2.69
  mdd_t7: -1.63
  volatility: 0.0
  impact_t1_pct: -1.63
  impact_t7_pct: 0.63
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 0.54
    mean: -0.06
    sample: 9
  t7:
    up: 77.78
    down: 22.22
    median: 0.63
    mean: 0.64
    sample: 9
chartData: [{"time": "2024-01-29", "open": 475.96, "high": 479.56, "low": 475.42, "close": 479.42}, {"time": "2024-01-30", "open": 478.73, "high": 479.76, "low": 478.29, "close": 479.05}, {"time": "2024-01-31", "open": 476.83, "high": 477.28, "low": 471.21, "close": 471.23}, {"time": "2024-02-01", "open": 472.94, "high": 477.43, "low": 472.13, "close": 477.4}, {"time": "2024-02-02", "open": 477.84, "high": 484.08, "low": 477.5, "close": 482.42}, {"time": "2024-02-05", "open": 481.79, "high": 482.45, "low": 478.4, "close": 480.67}, {"time": "2024-02-06", "open": 481.61, "high": 482.39, "low": 480.18, "close": 482.06}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **SPY**
- Event date: **2024-01-30**
- As-of date (T-1): **2025-01-29**
- Sample size: **9**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.54% | -0.06% | 9 |
| T+7 | 77.78% | 22.22% | 0.63% | 0.64% | 9 |

## Historical Distribution Summary

T+1 Up Probability: **55.56%** (n=9)

T+7 Up Probability: **77.78%** (n=9)

T+7 Median Return: **0.63%**

For SPY, historical FOMC windows currently show a T+1 up probability of 55.56% and a T+7 up probability of 77.78%. Median T+7 return is 0.63% across 9 samples. Current classification is Bullish, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
