---
title: "ETH After CPI (2024-08-14): Historical T+1/T+7 Probability"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-08-14"
asof_date: "2025-02-12"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
confidence_level: "normal"
quality_score: 90
sample_size: 14
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -3.58
  mdd_t7: -3.49
  volatility: 0.0
  impact_t1_pct: -3.49
  impact_t7_pct: -1.18
probabilities:
  sample_size: 14
  t1:
    up: 50.0
    down: 50.0
    median: -0.22
    mean: -0.52
    sample: 14
  t7:
    up: 42.86
    down: 57.14
    median: -0.39
    mean: 0.26
    sample: 14
chartData: [{"time": "2024-08-11", "open": 2609.97, "high": 2718.8, "low": 2544.17, "close": 2553.25}, {"time": "2024-08-12", "open": 2553.5, "high": 2749.14, "low": 2513.39, "close": 2724.43}, {"time": "2024-08-13", "open": 2724.3, "high": 2737.99, "low": 2613.8, "close": 2703.67}, {"time": "2024-08-14", "open": 2703.59, "high": 2775.28, "low": 2636.71, "close": 2662.91}, {"time": "2024-08-15", "open": 2662.89, "high": 2675.31, "low": 2518.67, "close": 2570.09}, {"time": "2024-08-16", "open": 2570.09, "high": 2629.38, "low": 2553.07, "close": 2593.19}, {"time": "2024-08-17", "open": 2593.17, "high": 2626.67, "low": 2588.79, "close": 2614.55}, {"time": "2024-08-18", "open": 2614.11, "high": 2684.03, "low": 2596.74, "close": 2613.36}, {"time": "2024-08-19", "open": 2612.72, "high": 2648.28, "low": 2566.4, "close": 2637.31}, {"time": "2024-08-20", "open": 2637.31, "high": 2695.91, "low": 2556.75, "close": 2573.11}, {"time": "2024-08-21", "open": 2573.11, "high": 2662.95, "low": 2538.66, "close": 2631.4}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-08-14**
- As-of date (T-1): **2025-02-12**
- Sample size: **14**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.22% | -0.52% | 14 |
| T+7 | 42.86% | 57.14% | -0.39% | 0.26% | 14 |

## Historical Distribution Summary

T+1 Up Probability: **50.0%** (n=14)

T+7 Up Probability: **42.86%** (n=14)

T+7 Median Return: **-0.39%**

For ETH, historical CPI windows currently show a T+1 up probability of 50.0% and a T+7 up probability of 42.86%. Median T+7 return is -0.39% across 14 samples. Current classification is Neutral, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
