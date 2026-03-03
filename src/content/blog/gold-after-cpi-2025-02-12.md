---
title: "GOLD After CPI (2025-02-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for GOLD around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-02-12"
asof_date: "2025-02-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
confidence_level: "normal"
quality_score: 90
sample_size: 14
tags: ["gold", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 7.09
  mdd_t7: -0.22
  volatility: 0.0
  impact_t1_pct: 0.58
  impact_t7_pct: 0.36
probabilities:
  sample_size: 14
  t1:
    up: 50.0
    down: 50.0
    median: 0.27
    mean: 0.22
    sample: 14
  t7:
    up: 76.92
    down: 23.08
    median: 1.52
    mean: 1.07
    sample: 13
chartData: [{"time": "2025-02-10", "open": 2864.2, "high": 2916.1, "low": 2863.8, "close": 2914.3}, {"time": "2025-02-11", "open": 2925.5, "high": 2945.4, "low": 2890.0, "close": 2912.5}, {"time": "2025-02-12", "open": 2902.0, "high": 2912.3, "low": 2868.6, "close": 2909.0}, {"time": "2025-02-13", "open": 2911.3, "high": 2937.7, "low": 2910.6, "close": 2925.9}, {"time": "2025-02-14", "open": 2937.3, "high": 2944.4, "low": 2874.8, "close": 2883.6}, {"time": "2025-02-18", "open": 2879.2, "high": 2936.4, "low": 2873.8, "close": 2931.6}, {"time": "2025-02-19", "open": 2938.7, "high": 2946.0, "low": 2917.1, "close": 2919.4}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **GOLD**
- Event date: **2025-02-12**
- As-of date (T-1): **2025-02-12**
- Sample size: **14**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.27% | 0.22% | 14 |
| T+7 | 76.92% | 23.08% | 1.52% | 1.07% | 13 |

## Historical Distribution Summary

T+1 Up Probability: **50.0%** (n=14)

T+7 Up Probability: **76.92%** (n=13)

T+7 Median Return: **1.52%**

For GOLD, historical CPI windows currently show a T+1 up probability of 50.0% and a T+7 up probability of 76.92%. Median T+7 return is 1.52% across 14 samples. Current classification is Bullish, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
