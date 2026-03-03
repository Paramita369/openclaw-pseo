---
title: "SPY After CPI (2024-07-11): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-07-11"
asof_date: "2025-02-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
confidence_level: "normal"
quality_score: 90
sample_size: 14
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -5.55
  mdd_t7: -1.31
  volatility: 0.0
  impact_t1_pct: 0.63
  impact_t7_pct: -0.69
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
chartData: [{"time": "2024-07-08", "open": 545.48, "high": 546.27, "low": 544.25, "close": 545.32}, {"time": "2024-07-09", "open": 546.28, "high": 547.19, "low": 545.56, "close": 545.85}, {"time": "2024-07-10", "open": 547.08, "high": 551.6, "low": 546.78, "close": 551.25}, {"time": "2024-07-11", "open": 551.37, "high": 552.24, "low": 545.86, "close": 546.5}, {"time": "2024-07-12", "open": 547.63, "high": 553.56, "low": 547.16, "close": 549.95}, {"time": "2024-07-15", "open": 551.95, "high": 554.71, "low": 549.59, "close": 551.46}, {"time": "2024-07-16", "open": 552.78, "high": 555.02, "low": 552.02, "close": 554.73}, {"time": "2024-07-17", "open": 548.78, "high": 550.46, "low": 546.63, "close": 546.95}, {"time": "2024-07-18", "open": 548.49, "high": 549.49, "low": 540.56, "close": 542.75}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2024-07-11**
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
