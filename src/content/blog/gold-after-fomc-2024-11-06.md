---
title: "GOLD After FOMC (2024-11-06): Historical T+1/T+7 Probability"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-11-06"
asof_date: "2025-01-29"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
confidence_level: "normal"
quality_score: 80
sample_size: 9
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -9.22
  mdd_t7: -4.36
  volatility: 0.0
  impact_t1_pct: 1.15
  impact_t7_pct: -3.25
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
chartData: [{"time": "2024-11-04", "open": 2736.5, "high": 2737.1, "low": 2736.1, "close": 2736.1}, {"time": "2024-11-05", "open": 2743.0, "high": 2743.9, "low": 2740.3, "close": 2740.3}, {"time": "2024-11-06", "open": 2734.5, "high": 2734.5, "low": 2659.4, "close": 2667.6}, {"time": "2024-11-07", "open": 2662.5, "high": 2699.1, "low": 2662.5, "close": 2698.4}, {"time": "2024-11-08", "open": 2688.5, "high": 2694.6, "low": 2682.9, "close": 2687.5}, {"time": "2024-11-11", "open": 2671.7, "high": 2671.7, "low": 2611.2, "close": 2611.2}, {"time": "2024-11-12", "open": 2605.5, "high": 2605.5, "low": 2592.8, "close": 2600.0}, {"time": "2024-11-13", "open": 2611.1, "high": 2611.8, "low": 2580.8, "close": 2580.8}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2024-11-06**
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
