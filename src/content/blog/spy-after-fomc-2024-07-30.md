---
title: "SPY After FOMC (2024-07-30): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around FOMC events (T+1/T+7)."
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
tags: ["spy", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -8.32
  mdd_t7: -5.2
  volatility: 0.0
  impact_t1_pct: 1.63
  impact_t7_pct: -3.66
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
chartData: [{"time": "2024-07-29", "open": 536.23, "high": 537.24, "low": 532.99, "close": 534.99}, {"time": "2024-07-30", "open": 536.46, "high": 537.52, "low": 528.86, "close": 532.28}, {"time": "2024-07-31", "open": 539.13, "high": 543.57, "low": 537.76, "close": 540.93}, {"time": "2024-08-01", "open": 542.66, "high": 544.92, "low": 529.76, "close": 533.27}, {"time": "2024-08-02", "open": 526.14, "high": 527.36, "low": 519.12, "close": 523.34}, {"time": "2024-08-05", "open": 502.46, "high": 514.19, "low": 501.12, "close": 508.1}, {"time": "2024-08-06", "open": 509.91, "high": 520.25, "low": 508.58, "close": 512.79}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **SPY**
- Event date: **2024-07-30**
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
