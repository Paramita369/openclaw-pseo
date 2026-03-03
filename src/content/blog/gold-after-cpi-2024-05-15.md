---
title: "GOLD After CPI (2024-05-15): Historical T+1/T+7 Probability"
description: "Historical probability profile for GOLD around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-05-15"
asof_date: "2025-02-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
confidence_level: "normal"
quality_score: 90
sample_size: 14
tags: ["gold", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.47
  mdd_t7: -0.36
  volatility: 0.0
  impact_t1_pct: -0.36
  impact_t7_pct: 0.02
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
chartData: [{"time": "2024-05-13", "open": 2358.3, "high": 2358.3, "low": 2336.1, "close": 2336.1}, {"time": "2024-05-14", "open": 2336.0, "high": 2358.0, "low": 2336.0, "close": 2353.4}, {"time": "2024-05-15", "open": 2361.6, "high": 2388.7, "low": 2356.0, "close": 2388.7}, {"time": "2024-05-16", "open": 2389.5, "high": 2392.2, "low": 2380.0, "close": 2380.0}, {"time": "2024-05-17", "open": 2380.7, "high": 2415.8, "low": 2380.7, "close": 2412.2}, {"time": "2024-05-20", "open": 2415.8, "high": 2435.8, "low": 2409.7, "close": 2433.9}, {"time": "2024-05-21", "open": 2429.5, "high": 2429.5, "low": 2421.0, "close": 2421.7}, {"time": "2024-05-22", "open": 2417.5, "high": 2417.6, "low": 2375.8, "close": 2389.2}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **GOLD**
- Event date: **2024-05-15**
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
