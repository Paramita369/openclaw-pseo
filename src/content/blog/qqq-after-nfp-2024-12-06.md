---
title: "QQQ After NFP (2024-12-06): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-12-06"
asof_date: "2025-01-10"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
confidence_level: "normal"
quality_score: 80
sample_size: 13
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 3.77
  mdd_t7: -1.39
  volatility: 0.0
  impact_t1_pct: 0.0
  impact_t7_pct: 0.77
probabilities:
  sample_size: 13
  t1:
    up: 0.0
    down: 100.0
    median: 0.0
    mean: 0.0
    sample: 0
  t7:
    up: 76.92
    down: 23.08
    median: 1.51
    mean: 1.89
    sample: 13
chartData: [{"time": "2024-12-03", "open": 510.53, "high": 513.71, "low": 509.96, "close": 513.43}, {"time": "2024-12-04", "open": 516.86, "high": 520.04, "low": 516.15, "close": 519.78}, {"time": "2024-12-05", "open": 519.83, "high": 520.56, "low": 517.95, "close": 518.34}, {"time": "2024-12-06", "open": 519.01, "high": 523.22, "low": 518.88, "close": 522.98}, {"time": "2024-12-09", "open": 522.06, "high": 522.85, "low": 517.76, "close": 518.91}, {"time": "2024-12-10", "open": 520.14, "high": 521.89, "low": 515.71, "close": 517.14}, {"time": "2024-12-11", "open": 521.51, "high": 527.08, "low": 521.1, "close": 526.4}, {"time": "2024-12-12", "open": 524.17, "high": 525.44, "low": 522.52, "close": 523.0}, {"time": "2024-12-13", "open": 526.93, "high": 529.63, "low": 523.79, "close": 527.0}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2024-12-06**
- As-of date (T-1): **2025-01-10**
- Sample size: **13**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 76.92% | 23.08% | 1.51% | 1.89% | 13 |

## Historical Distribution Summary

T+1 Up Probability: **0.0%** (n=0)

T+7 Up Probability: **76.92%** (n=13)

T+7 Median Return: **1.51%**

For QQQ, historical NFP windows currently show a T+1 up probability of 0.0% and a T+7 up probability of 76.92%. Median T+7 return is 1.51% across 13 samples. Current classification is Neutral, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
