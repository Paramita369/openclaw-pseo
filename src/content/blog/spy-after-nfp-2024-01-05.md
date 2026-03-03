---
title: "SPY After NFP (2024-01-05): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-01-05"
asof_date: "2025-01-10"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
confidence_level: "normal"
quality_score: 80
sample_size: 13
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 6.04
  mdd_t7: -1.33
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
    median: 1.39
    mean: 1.41
    sample: 13
chartData: [{"time": "2024-01-02", "open": 460.77, "high": 462.24, "low": 459.14, "close": 461.25}, {"time": "2024-01-03", "open": 459.08, "high": 459.82, "low": 456.88, "close": 457.48}, {"time": "2024-01-04", "open": 457.0, "high": 459.6, "low": 455.78, "close": 456.01}, {"time": "2024-01-05", "open": 456.21, "high": 459.09, "low": 455.18, "close": 456.63}, {"time": "2024-01-08", "open": 457.13, "high": 463.3, "low": 457.0, "close": 463.15}, {"time": "2024-01-09", "open": 460.49, "high": 463.47, "low": 459.98, "close": 462.45}, {"time": "2024-01-10", "open": 462.72, "high": 465.93, "low": 462.44, "close": 465.06}, {"time": "2024-01-11", "open": 466.07, "high": 466.59, "low": 460.87, "close": 464.86}, {"time": "2024-01-12", "open": 466.31, "high": 467.05, "low": 463.77, "close": 465.18}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2024-01-05**
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
