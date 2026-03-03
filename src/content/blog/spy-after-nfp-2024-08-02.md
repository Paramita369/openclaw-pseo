---
title: "SPY After NFP (2024-08-02): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
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
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 2.25
  mdd_t7: -4.25
  volatility: 0.0
  impact_t1_pct: 0.0
  impact_t7_pct: 0.02
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
chartData: [{"time": "2024-07-30", "open": 536.46, "high": 537.52, "low": 528.86, "close": 532.28}, {"time": "2024-07-31", "open": 539.13, "high": 543.57, "low": 537.76, "close": 540.93}, {"time": "2024-08-01", "open": 542.66, "high": 544.92, "low": 529.76, "close": 533.27}, {"time": "2024-08-02", "open": 526.14, "high": 527.36, "low": 519.12, "close": 523.34}, {"time": "2024-08-05", "open": 502.46, "high": 514.19, "low": 501.12, "close": 508.1}, {"time": "2024-08-06", "open": 509.91, "high": 520.25, "low": 508.58, "close": 512.79}, {"time": "2024-08-07", "open": 518.99, "high": 522.06, "low": 508.76, "close": 509.36}, {"time": "2024-08-08", "open": 514.51, "high": 521.76, "low": 512.48, "close": 521.13}, {"time": "2024-08-09", "open": 520.31, "high": 524.92, "low": 519.08, "close": 523.43}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2024-08-02**
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
