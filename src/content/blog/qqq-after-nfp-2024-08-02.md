---
title: "QQQ After NFP (2024-08-02): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-08-02"
asof_date: "2025-01-10"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
confidence_level: "normal"
quality_score: 80
sample_size: 13
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 3.35
  mdd_t7: -5.64
  volatility: 0.0
  impact_t1_pct: 0.0
  impact_t7_pct: 0.37
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
chartData: [{"time": "2024-07-30", "open": 462.1, "high": 462.81, "low": 450.5, "close": 453.85}, {"time": "2024-07-31", "open": 464.11, "high": 468.99, "low": 462.66, "close": 467.28}, {"time": "2024-08-01", "open": 467.97, "high": 471.73, "low": 452.31, "close": 455.96}, {"time": "2024-08-02", "open": 447.26, "high": 449.92, "low": 440.9, "close": 445.14}, {"time": "2024-08-05", "open": 421.29, "high": 438.73, "low": 420.04, "close": 431.87}, {"time": "2024-08-06", "open": 433.71, "high": 443.47, "low": 431.07, "close": 436.0}, {"time": "2024-08-07", "open": 442.9, "high": 445.39, "low": 430.88, "close": 431.27}, {"time": "2024-08-08", "open": 437.51, "high": 445.38, "low": 433.63, "close": 444.47}, {"time": "2024-08-09", "open": 443.15, "high": 448.42, "low": 442.03, "close": 446.79}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2024-08-02**
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
