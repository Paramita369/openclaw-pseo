---
title: "GOLD After CPI (2024-03-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for GOLD around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-03-12"
asof_date: "2025-02-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
confidence_level: "normal"
quality_score: 90
sample_size: 14
tags: ["gold", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -1.85
  mdd_t7: -0.88
  volatility: 0.0
  impact_t1_pct: 0.69
  impact_t7_pct: -0.19
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
chartData: [{"time": "2024-03-11", "open": 2181.0, "high": 2184.0, "low": 2177.2, "close": 2182.5}, {"time": "2024-03-12", "open": 2182.5, "high": 2182.7, "low": 2160.4, "close": 2160.4}, {"time": "2024-03-13", "open": 2162.5, "high": 2175.4, "low": 2162.5, "close": 2175.4}, {"time": "2024-03-14", "open": 2163.0, "high": 2163.0, "low": 2162.3, "close": 2163.0}, {"time": "2024-03-15", "open": 2161.7, "high": 2161.7, "low": 2157.3, "close": 2157.3}, {"time": "2024-03-18", "open": 2146.2, "high": 2160.7, "low": 2146.2, "close": 2160.7}, {"time": "2024-03-19", "open": 2156.1, "high": 2156.3, "low": 2156.1, "close": 2156.3}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **GOLD**
- Event date: **2024-03-12**
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
