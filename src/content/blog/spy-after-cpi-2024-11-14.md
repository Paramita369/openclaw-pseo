---
title: "SPY After CPI (2024-11-14): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-11-14"
asof_date: "2025-02-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
confidence_level: "normal"
quality_score: 90
sample_size: 14
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.43
  mdd_t7: -1.28
  volatility: 0.0
  impact_t1_pct: -1.28
  impact_t7_pct: 0.05
probabilities:
  sample_size: 14
  t1:
    up: 64.29
    down: 35.71
    median: 0.15
    mean: 0.26
    sample: 14
  t7:
    up: 76.92
    down: 23.08
    median: 1.08
    mean: 0.51
    sample: 13
chartData: [{"time": "2024-11-11", "open": 590.86, "high": 591.21, "low": 588.09, "close": 589.83}, {"time": "2024-11-12", "open": 589.75, "high": 590.35, "low": 585.5, "close": 587.99}, {"time": "2024-11-13", "open": 588.46, "high": 590.29, "low": 586.08, "close": 588.28}, {"time": "2024-11-14", "open": 588.41, "high": 588.89, "low": 583.81, "close": 584.5}, {"time": "2024-11-15", "open": 580.92, "high": 581.39, "low": 575.15, "close": 577.01}, {"time": "2024-11-18", "open": 577.47, "high": 580.69, "low": 576.61, "close": 579.37}, {"time": "2024-11-19", "open": 575.98, "high": 582.22, "low": 575.31, "close": 581.49}, {"time": "2024-11-20", "open": 581.57, "high": 581.97, "low": 575.91, "close": 581.69}, {"time": "2024-11-21", "open": 584.55, "high": 586.24, "low": 578.68, "close": 584.81}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2024-11-14**
- As-of date (T-1): **2025-02-12**
- Sample size: **14**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 64.29% | 35.71% | 0.15% | 0.26% | 14 |
| T+7 | 76.92% | 23.08% | 1.08% | 0.51% | 13 |

## Historical Distribution Summary

T+1 Up Probability: **64.29%** (n=14)

T+7 Up Probability: **76.92%** (n=13)

T+7 Median Return: **1.08%**

For SPY, historical CPI windows currently show a T+1 up probability of 64.29% and a T+7 up probability of 76.92%. Median T+7 return is 1.08% across 14 samples. Current classification is Bullish, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
