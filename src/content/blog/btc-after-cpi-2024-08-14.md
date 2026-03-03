---
title: "BTC After CPI (2024-08-14): Historical T+1/T+7 Probability"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-08-14"
asof_date: "2025-02-12"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
confidence_level: "normal"
quality_score: 90
sample_size: 14
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 9.86
  mdd_t7: -2.0
  volatility: 0.0
  impact_t1_pct: -2.0
  impact_t7_pct: 4.15
probabilities:
  sample_size: 14
  t1:
    up: 42.86
    down: 57.14
    median: -0.74
    mean: 0.26
    sample: 14
  t7:
    up: 57.14
    down: 42.86
    median: 3.64
    mean: 1.69
    sample: 14
chartData: [{"time": "2024-08-11", "open": 60944.89, "high": 61778.66, "low": 58348.82, "close": 58719.48}, {"time": "2024-08-12", "open": 58719.39, "high": 60680.33, "low": 57688.9, "close": 59354.52}, {"time": "2024-08-13", "open": 59356.21, "high": 61572.4, "low": 58506.25, "close": 60609.57}, {"time": "2024-08-14", "open": 60611.05, "high": 61687.76, "low": 58472.88, "close": 58737.27}, {"time": "2024-08-15", "open": 58733.26, "high": 59838.65, "low": 56161.59, "close": 57560.1}, {"time": "2024-08-16", "open": 57560.27, "high": 59847.36, "low": 57110.02, "close": 58894.11}, {"time": "2024-08-17", "open": 58893.53, "high": 59694.67, "low": 58814.83, "close": 59478.97}, {"time": "2024-08-18", "open": 59468.13, "high": 60262.72, "low": 58445.4, "close": 58483.96}, {"time": "2024-08-19", "open": 58480.71, "high": 59612.66, "low": 57864.71, "close": 59493.45}, {"time": "2024-08-20", "open": 59493.45, "high": 61396.33, "low": 58610.88, "close": 59012.79}, {"time": "2024-08-21", "open": 59014.99, "high": 61834.35, "low": 58823.45, "close": 61175.19}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2024-08-14**
- As-of date (T-1): **2025-02-12**
- Sample size: **14**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 42.86% | 57.14% | -0.74% | 0.26% | 14 |
| T+7 | 57.14% | 42.86% | 3.64% | 1.69% | 14 |

## Historical Distribution Summary

T+1 Up Probability: **42.86%** (n=14)

T+7 Up Probability: **57.14%** (n=14)

T+7 Median Return: **3.64%**

For BTC, historical CPI windows currently show a T+1 up probability of 42.86% and a T+7 up probability of 57.14%. Median T+7 return is 3.64% across 14 samples. Current classification is Neutral, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
