---
title: "SPY After CPI (2024-05-15): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
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
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.37
  mdd_t7: -0.21
  volatility: 0.0
  impact_t1_pct: -0.21
  impact_t7_pct: 0.01
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
chartData: [{"time": "2024-05-13", "open": 511.54, "high": 511.65, "low": 508.78, "close": 509.92}, {"time": "2024-05-14", "open": 510.12, "high": 512.78, "low": 509.58, "close": 512.26}, {"time": "2024-05-15", "open": 514.74, "high": 518.9, "low": 514.1, "close": 518.61}, {"time": "2024-05-16", "open": 518.7, "high": 520.31, "low": 517.39, "close": 517.54}, {"time": "2024-05-17", "open": 517.66, "high": 518.35, "low": 516.2, "close": 518.28}, {"time": "2024-05-20", "open": 518.4, "high": 520.35, "low": 518.01, "close": 518.88}, {"time": "2024-05-21", "open": 518.12, "high": 520.31, "low": 517.91, "close": 520.15}, {"time": "2024-05-22", "open": 519.46, "high": 520.17, "low": 516.47, "close": 518.65}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2024-05-15**
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
