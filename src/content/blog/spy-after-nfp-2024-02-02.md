---
title: "SPY After NFP (2024-02-02): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
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
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -0.17
  mdd_t7: -2.09
  volatility: 0.0
  impact_t1_pct: 0.0
  impact_t7_pct: 1.39
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
    median: 1.39
    mean: 1.41
    sample: 13
chartData: [{"time": "2024-01-30", "open": 478.73, "high": 479.76, "low": 478.29, "close": 479.05}, {"time": "2024-01-31", "open": 476.83, "high": 477.28, "low": 471.21, "close": 471.23}, {"time": "2024-02-01", "open": 472.94, "high": 477.43, "low": 472.13, "close": 477.4}, {"time": "2024-02-02", "open": 477.84, "high": 484.08, "low": 477.5, "close": 482.42}, {"time": "2024-02-05", "open": 481.79, "high": 482.45, "low": 478.4, "close": 480.67}, {"time": "2024-02-06", "open": 481.61, "high": 482.39, "low": 480.18, "close": 482.06}, {"time": "2024-02-07", "open": 484.32, "high": 486.5, "low": 483.41, "close": 486.08}, {"time": "2024-02-08", "open": 486.08, "high": 486.68, "low": 485.26, "close": 486.3}, {"time": "2024-02-09", "open": 486.81, "high": 489.55, "low": 486.46, "close": 489.11}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2024-02-02**
- As-of date (T-1): **2025-01-10**
- Sample size: **13**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 76.92% | 23.08% | 1.39% | 1.41% | 13 |

## Historical Distribution Summary

T+1 Up Probability: **0.0%** (n=0)

T+7 Up Probability: **76.92%** (n=13)

T+7 Median Return: **1.39%**

For SPY, historical NFP windows currently show a T+1 up probability of 0.0% and a T+7 up probability of 76.92%. Median T+7 return is 1.39% across 13 samples. Current classification is Neutral, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
