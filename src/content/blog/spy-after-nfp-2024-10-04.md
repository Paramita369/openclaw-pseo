---
title: "SPY After NFP (2024-10-04): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
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
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 3.43
  mdd_t7: -1.11
  volatility: 0.0
  impact_t1_pct: 0.0
  impact_t7_pct: 1.15
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
chartData: [{"time": "2024-10-01", "open": 564.84, "high": 565.49, "low": 557.55, "close": 560.13}, {"time": "2024-10-02", "open": 559.24, "high": 561.4, "low": 556.83, "close": 560.37}, {"time": "2024-10-03", "open": 558.89, "high": 561.3, "low": 557.05, "close": 559.35}, {"time": "2024-10-04", "open": 563.81, "high": 564.8, "low": 559.62, "close": 564.43}, {"time": "2024-10-07", "open": 562.77, "high": 563.42, "low": 558.17, "close": 559.33}, {"time": "2024-10-08", "open": 561.91, "high": 565.22, "low": 561.03, "close": 564.62}, {"time": "2024-10-09", "open": 564.61, "high": 569.09, "low": 564.01, "close": 568.53}, {"time": "2024-10-10", "open": 567.18, "high": 568.96, "low": 565.92, "close": 567.53}, {"time": "2024-10-11", "open": 567.45, "high": 571.67, "low": 567.32, "close": 570.93}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2024-10-04**
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
