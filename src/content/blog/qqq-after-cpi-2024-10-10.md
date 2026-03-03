---
title: "QQQ After CPI (2024-10-10): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-10-10"
asof_date: "2025-02-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
confidence_level: "normal"
quality_score: 90
sample_size: 14
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -7.38
  mdd_t7: -0.43
  volatility: 0.0
  impact_t1_pct: 0.16
  impact_t7_pct: -0.27
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
chartData: [{"time": "2024-10-07", "open": 482.16, "high": 483.34, "low": 477.67, "close": 478.9}, {"time": "2024-10-08", "open": 481.44, "high": 486.73, "low": 480.63, "close": 486.05}, {"time": "2024-10-09", "open": 485.75, "high": 490.45, "low": 484.71, "close": 489.87}, {"time": "2024-10-10", "open": 487.59, "high": 491.18, "low": 486.28, "close": 489.32}, {"time": "2024-10-11", "open": 487.48, "high": 491.1, "low": 486.91, "close": 490.08}, {"time": "2024-10-14", "open": 492.47, "high": 495.51, "low": 491.97, "close": 494.19}, {"time": "2024-10-15", "open": 494.52, "high": 495.19, "low": 485.43, "close": 487.59}, {"time": "2024-10-16", "open": 487.91, "high": 488.42, "low": 484.33, "close": 487.65}, {"time": "2024-10-17", "open": 493.14, "high": 493.19, "low": 487.92, "close": 487.98}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2024-10-10**
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
