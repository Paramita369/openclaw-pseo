---
title: "QQQ After CPI (2024-11-14): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-11-14"
asof_date: "2025-02-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
confidence_level: "normal"
quality_score: 90
sample_size: 14
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -2.68
  mdd_t7: -2.38
  volatility: 0.0
  impact_t1_pct: -2.38
  impact_t7_pct: -0.73
probabilities:
  sample_size: 14
  t1:
    up: 57.14
    down: 42.86
    median: 0.35
    mean: 0.28
    sample: 14
  t7:
    up: 53.85
    down: 46.15
    median: 0.6
    mean: 0.54
    sample: 13
chartData: [{"time": "2024-11-11", "open": 511.94, "high": 512.15, "low": 507.52, "close": 510.42}, {"time": "2024-11-12", "open": 510.35, "high": 511.24, "low": 506.44, "close": 509.5}, {"time": "2024-11-13", "open": 508.99, "high": 511.56, "low": 506.56, "close": 508.84}, {"time": "2024-11-14", "open": 508.51, "high": 509.38, "low": 504.39, "close": 505.31}, {"time": "2024-11-15", "open": 499.6, "high": 499.98, "low": 491.2, "close": 493.27}, {"time": "2024-11-18", "open": 494.82, "high": 498.8, "low": 493.43, "close": 496.7}, {"time": "2024-11-19", "open": 494.11, "high": 500.6, "low": 493.78, "close": 500.11}, {"time": "2024-11-20", "open": 499.82, "high": 500.13, "low": 493.26, "close": 499.83}, {"time": "2024-11-21", "open": 502.87, "high": 503.59, "low": 494.25, "close": 501.62}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2024-11-14**
- As-of date (T-1): **2025-02-12**
- Sample size: **14**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 57.14% | 42.86% | 0.35% | 0.28% | 14 |
| T+7 | 53.85% | 46.15% | 0.6% | 0.54% | 13 |

## Historical Distribution Summary

T+1 Up Probability: **57.14%** (n=14)

T+7 Up Probability: **53.85%** (n=13)

T+7 Median Return: **0.6%**

For QQQ, historical CPI windows currently show a T+1 up probability of 57.14% and a T+7 up probability of 53.85%. Median T+7 return is 0.6% across 14 samples. Current classification is Neutral, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
