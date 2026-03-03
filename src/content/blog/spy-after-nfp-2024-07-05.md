---
title: "SPY After NFP (2024-07-05): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-07-05"
asof_date: "2025-01-10"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
confidence_level: "normal"
quality_score: 80
sample_size: 13
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 7.02
  mdd_t7: -0.98
  volatility: 0.0
  impact_t1_pct: 0.0
  impact_t7_pct: 0.96
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
chartData: [{"time": "2024-07-02", "open": 533.95, "high": 539.16, "low": 533.9, "close": 539.16}, {"time": "2024-07-03", "open": 538.85, "high": 541.93, "low": 538.81, "close": 541.57}, {"time": "2024-07-05", "open": 541.87, "high": 545.1, "low": 541.24, "close": 544.69}, {"time": "2024-07-08", "open": 545.48, "high": 546.27, "low": 544.25, "close": 545.32}, {"time": "2024-07-09", "open": 546.28, "high": 547.19, "low": 545.56, "close": 545.85}, {"time": "2024-07-10", "open": 547.08, "high": 551.6, "low": 546.78, "close": 551.25}, {"time": "2024-07-11", "open": 551.37, "high": 552.24, "low": 545.86, "close": 546.5}, {"time": "2024-07-12", "open": 547.63, "high": 553.56, "low": 547.16, "close": 549.95}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2024-07-05**
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
