---
title: "SPY After FOMC (2024-12-17): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around FOMC events (T+1/T+7)."
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
tags: ["spy", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -0.2
  mdd_t7: -2.98
  volatility: 0.0
  impact_t1_pct: -2.98
  impact_t7_pct: -0.16
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
chartData: [{"time": "2024-12-16", "open": 596.96, "high": 598.71, "low": 596.18, "close": 597.74}, {"time": "2024-12-17", "open": 595.17, "high": 596.14, "low": 593.89, "close": 595.27}, {"time": "2024-12-18", "open": 594.97, "high": 597.36, "low": 577.15, "close": 577.53}, {"time": "2024-12-19", "open": 582.54, "high": 584.15, "low": 577.11, "close": 577.35}, {"time": "2024-12-20", "open": 575.02, "high": 588.84, "low": 574.17, "close": 584.29}, {"time": "2024-12-23", "open": 584.03, "high": 588.39, "low": 580.84, "close": 587.79}, {"time": "2024-12-24", "open": 589.14, "high": 594.36, "low": 588.56, "close": 594.32}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **SPY**
- Event date: **2024-12-17**
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
