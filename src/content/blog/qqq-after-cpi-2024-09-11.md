---
title: "QQQ After CPI (2024-09-11): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-09-11"
asof_date: "2025-02-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
confidence_level: "normal"
quality_score: 90
sample_size: 14
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 7.08
  mdd_t7: -0.38
  volatility: 0.0
  impact_t1_pct: 0.98
  impact_t7_pct: 0.6
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
chartData: [{"time": "2024-09-09", "open": 449.42, "high": 451.8, "low": 446.2, "close": 450.81}, {"time": "2024-09-10", "open": 452.57, "high": 455.48, "low": 448.59, "close": 454.97}, {"time": "2024-09-11", "open": 456.21, "high": 465.6, "low": 447.65, "close": 464.85}, {"time": "2024-09-12", "open": 464.88, "high": 470.23, "low": 463.1, "close": 469.41}, {"time": "2024-09-13", "open": 468.68, "high": 472.7, "low": 468.45, "close": 471.52}, {"time": "2024-09-16", "open": 469.38, "high": 470.05, "low": 466.11, "close": 469.43}, {"time": "2024-09-17", "open": 472.46, "high": 473.76, "low": 467.18, "close": 469.68}, {"time": "2024-09-18", "open": 470.88, "high": 474.98, "low": 467.04, "close": 467.65}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2024-09-11**
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
