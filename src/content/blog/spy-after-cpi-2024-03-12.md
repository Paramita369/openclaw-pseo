---
title: "SPY After CPI (2024-03-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
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
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 3.94
  mdd_t7: -0.16
  volatility: 0.0
  impact_t1_pct: -0.16
  impact_t7_pct: 0.1
probabilities:
  sample_size: 14
  t1:
    up: 64.29
    down: 35.71
    median: 0.15
    mean: 0.26
    sample: 14
  t7:
    up: 76.92
    down: 23.08
    median: 1.08
    mean: 0.51
    sample: 13
chartData: [{"time": "2024-03-11", "open": 498.16, "high": 499.53, "low": 496.23, "close": 498.95}, {"time": "2024-03-12", "open": 501.06, "high": 504.9, "low": 498.54, "close": 504.31}, {"time": "2024-03-13", "open": 504.63, "high": 504.81, "low": 502.08, "close": 503.52}, {"time": "2024-03-14", "open": 504.5, "high": 504.65, "low": 499.47, "close": 502.53}, {"time": "2024-03-15", "open": 499.45, "high": 500.91, "low": 497.4, "close": 499.08}, {"time": "2024-03-18", "open": 503.16, "high": 504.61, "low": 501.63, "close": 502.04}, {"time": "2024-03-19", "open": 501.35, "high": 505.12, "low": 500.34, "close": 504.83}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2024-03-12**
- As-of date (T-1): **2025-02-12**
- Sample size: **14**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 64.29% | 35.71% | 0.15% | 0.26% | 14 |
| T+7 | 76.92% | 23.08% | 1.08% | 0.51% | 13 |

## Historical Distribution Summary

T+1 Up Probability: **64.29%** (n=14)

T+7 Up Probability: **76.92%** (n=13)

T+7 Median Return: **1.08%**

For SPY, historical CPI windows currently show a T+1 up probability of 64.29% and a T+7 up probability of 76.92%. Median T+7 return is 1.08% across 14 samples. Current classification is Bullish, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
