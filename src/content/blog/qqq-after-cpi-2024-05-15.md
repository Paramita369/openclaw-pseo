---
title: "QQQ After CPI (2024-05-15): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-05-15"
asof_date: "2025-02-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
confidence_level: "normal"
quality_score: 90
sample_size: 14
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 9.6
  mdd_t7: -0.2
  volatility: 0.0
  impact_t1_pct: -0.2
  impact_t7_pct: 0.62
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
chartData: [{"time": "2024-05-13", "open": 439.72, "high": 439.82, "low": 437.4, "close": 438.82}, {"time": "2024-05-14", "open": 438.39, "high": 442.18, "low": 438.21, "close": 441.64}, {"time": "2024-05-15", "open": 444.12, "high": 448.79, "low": 442.6, "close": 448.54}, {"time": "2024-05-16", "open": 448.36, "high": 450.32, "low": 447.47, "close": 447.63}, {"time": "2024-05-17", "open": 447.76, "high": 448.37, "low": 445.22, "close": 447.42}, {"time": "2024-05-20", "open": 447.63, "high": 451.2, "low": 447.45, "close": 450.54}, {"time": "2024-05-21", "open": 448.68, "high": 451.61, "low": 448.49, "close": 451.42}, {"time": "2024-05-22", "open": 451.67, "high": 452.43, "low": 448.72, "close": 451.33}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2024-05-15**
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
