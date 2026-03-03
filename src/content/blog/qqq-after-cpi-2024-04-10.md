---
title: "QQQ After CPI (2024-04-10): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-04-10"
asof_date: "2025-02-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
confidence_level: "normal"
quality_score: 90
sample_size: 14
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -7.4
  mdd_t7: -4.39
  volatility: 0.0
  impact_t1_pct: 1.6
  impact_t7_pct: -2.86
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
chartData: [{"time": "2024-04-08", "open": 437.17, "high": 438.24, "low": 434.98, "close": 436.36}, {"time": "2024-04-09", "open": 438.7, "high": 438.98, "low": 433.23, "close": 437.98}, {"time": "2024-04-10", "open": 432.8, "high": 435.02, "low": 432.08, "close": 434.15}, {"time": "2024-04-11", "open": 436.03, "high": 442.04, "low": 433.75, "close": 441.09}, {"time": "2024-04-12", "open": 436.86, "high": 437.99, "low": 432.68, "close": 434.06}, {"time": "2024-04-15", "open": 437.81, "high": 437.9, "low": 426.07, "close": 426.91}, {"time": "2024-04-16", "open": 426.76, "high": 429.59, "low": 425.57, "close": 426.95}, {"time": "2024-04-17", "open": 428.94, "high": 428.96, "low": 420.81, "close": 421.75}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2024-04-10**
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
