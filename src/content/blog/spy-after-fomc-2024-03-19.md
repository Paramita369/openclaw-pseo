---
title: "SPY After FOMC (2024-03-19): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around FOMC events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-03-19"
asof_date: "2025-01-29"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
confidence_level: "normal"
quality_score: 80
sample_size: 9
tags: ["spy", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 7.7
  mdd_t7: -0.32
  volatility: 0.0
  impact_t1_pct: 0.92
  impact_t7_pct: 0.6
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 0.54
    mean: -0.06
    sample: 9
  t7:
    up: 77.78
    down: 22.22
    median: 0.63
    mean: 0.64
    sample: 9
chartData: [{"time": "2024-03-18", "open": 503.16, "high": 504.61, "low": 501.63, "close": 502.04}, {"time": "2024-03-19", "open": 501.35, "high": 505.12, "low": 500.34, "close": 504.83}, {"time": "2024-03-20", "open": 504.89, "high": 509.64, "low": 504.22, "close": 509.5}, {"time": "2024-03-21", "open": 512.35, "high": 513.06, "low": 510.9, "close": 511.19}, {"time": "2024-03-22", "open": 511.1, "high": 511.59, "low": 509.98, "close": 510.22}, {"time": "2024-03-25", "open": 508.84, "high": 509.96, "low": 508.65, "close": 508.81}, {"time": "2024-03-26", "open": 510.24, "high": 510.58, "low": 507.47, "close": 507.87}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **SPY**
- Event date: **2024-03-19**
- As-of date (T-1): **2025-01-29**
- Sample size: **9**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.54% | -0.06% | 9 |
| T+7 | 77.78% | 22.22% | 0.63% | 0.64% | 9 |

## Historical Distribution Summary

T+1 Up Probability: **55.56%** (n=9)

T+7 Up Probability: **77.78%** (n=9)

T+7 Median Return: **0.63%**

For SPY, historical FOMC windows currently show a T+1 up probability of 55.56% and a T+7 up probability of 77.78%. Median T+7 return is 0.63% across 9 samples. Current classification is Bullish, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
