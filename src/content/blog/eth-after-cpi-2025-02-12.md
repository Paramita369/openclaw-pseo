---
title: "ETH After CPI (2025-02-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-02-12"
asof_date: "2025-02-12"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
confidence_level: "normal"
quality_score: 90
sample_size: 14
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -3.8
  mdd_t7: -2.23
  volatility: 0.0
  impact_t1_pct: -2.23
  impact_t7_pct: -0.77
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
chartData: [{"time": "2025-02-09", "open": 2632.58, "high": 2695.22, "low": 2530.44, "close": 2628.72}, {"time": "2025-02-10", "open": 2628.65, "high": 2692.81, "low": 2564.02, "close": 2661.17}, {"time": "2025-02-11", "open": 2661.32, "high": 2724.9, "low": 2565.4, "close": 2602.78}, {"time": "2025-02-12", "open": 2602.83, "high": 2794.87, "low": 2551.17, "close": 2736.9}, {"time": "2025-02-13", "open": 2737.03, "high": 2756.44, "low": 2615.67, "close": 2675.9}, {"time": "2025-02-14", "open": 2675.94, "high": 2790.02, "low": 2666.27, "close": 2726.09}, {"time": "2025-02-15", "open": 2726.07, "high": 2738.68, "low": 2668.53, "close": 2693.56}, {"time": "2025-02-16", "open": 2693.56, "high": 2724.1, "low": 2655.3, "close": 2663.32}, {"time": "2025-02-17", "open": 2663.23, "high": 2848.78, "low": 2640.18, "close": 2743.2}, {"time": "2025-02-18", "open": 2743.02, "high": 2754.68, "low": 2606.9, "close": 2669.34}, {"time": "2025-02-19", "open": 2669.21, "high": 2735.92, "low": 2656.38, "close": 2715.77}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2025-02-12**
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
