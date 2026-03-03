---
title: "QQQ After NFP (2024-10-04): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-10-04"
asof_date: "2025-01-10"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
confidence_level: "normal"
quality_score: 80
sample_size: 13
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.58
  mdd_t7: -1.77
  volatility: 0.0
  impact_t1_pct: 0.0
  impact_t7_pct: 1.24
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
chartData: [{"time": "2024-10-01", "open": 484.46, "high": 484.76, "low": 474.23, "close": 478.07}, {"time": "2024-10-02", "open": 477.17, "high": 480.66, "low": 474.54, "close": 478.75}, {"time": "2024-10-03", "open": 476.55, "high": 481.33, "low": 475.81, "close": 478.39}, {"time": "2024-10-04", "open": 484.21, "high": 484.64, "low": 479.18, "close": 484.08}, {"time": "2024-10-07", "open": 482.16, "high": 483.34, "low": 477.67, "close": 478.9}, {"time": "2024-10-08", "open": 481.44, "high": 486.73, "low": 480.63, "close": 486.05}, {"time": "2024-10-09", "open": 485.75, "high": 490.45, "low": 484.71, "close": 489.87}, {"time": "2024-10-10", "open": 487.59, "high": 491.18, "low": 486.28, "close": 489.32}, {"time": "2024-10-11", "open": 487.48, "high": 491.1, "low": 486.91, "close": 490.08}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2024-10-04**
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
