---
title: "QQQ After NFP (2024-02-02): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-02-02"
asof_date: "2025-01-10"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
confidence_level: "normal"
quality_score: 80
sample_size: 13
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -0.27
  mdd_t7: -2.68
  volatility: 0.0
  impact_t1_pct: 0.0
  impact_t7_pct: 1.87
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
chartData: [{"time": "2024-01-30", "open": 422.43, "high": 423.01, "low": 419.74, "close": 420.65}, {"time": "2024-01-31", "open": 416.25, "high": 418.25, "low": 412.24, "close": 412.42}, {"time": "2024-02-01", "open": 414.22, "high": 417.77, "low": 413.25, "close": 417.27}, {"time": "2024-02-02", "open": 419.17, "high": 425.54, "low": 418.17, "close": 424.32}, {"time": "2024-02-05", "open": 424.38, "high": 424.92, "low": 420.36, "close": 423.77}, {"time": "2024-02-06", "open": 424.92, "high": 425.52, "low": 420.58, "close": 422.92}, {"time": "2024-02-07", "open": 425.71, "high": 428.1, "low": 424.4, "close": 427.27}, {"time": "2024-02-08", "open": 427.39, "high": 428.82, "low": 426.71, "close": 428.06}, {"time": "2024-02-09", "open": 429.2, "high": 433.07, "low": 428.41, "close": 432.28}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2024-02-02**
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
