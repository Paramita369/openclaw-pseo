---
title: "BTC After FOMC (2024-04-30): Historical T+1/T+7 Probability"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-04-30"
asof_date: "2025-01-29"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
confidence_level: "normal"
quality_score: 80
sample_size: 9
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 5.37
  mdd_t7: -3.93
  volatility: 0.0
  impact_t1_pct: -3.93
  impact_t7_pct: 2.8
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 0.35
    mean: 0.19
    sample: 9
  t7:
    up: 55.56
    down: 44.44
    median: 0.31
    mean: 1.12
    sample: 9
chartData: [{"time": "2024-04-27", "open": 63750.99, "high": 63898.36, "low": 62424.72, "close": 63419.14}, {"time": "2024-04-28", "open": 63423.52, "high": 64321.48, "low": 62793.6, "close": 63113.23}, {"time": "2024-04-29", "open": 63106.36, "high": 64174.88, "low": 61795.46, "close": 63841.12}, {"time": "2024-04-30", "open": 63839.42, "high": 64703.33, "low": 59120.07, "close": 60636.86}, {"time": "2024-05-01", "open": 60609.5, "high": 60780.5, "low": 56555.29, "close": 58254.01}, {"time": "2024-05-02", "open": 58253.7, "high": 59602.3, "low": 56937.2, "close": 59123.43}, {"time": "2024-05-03", "open": 59122.3, "high": 63320.5, "low": 58848.31, "close": 62889.84}, {"time": "2024-05-04", "open": 62891.03, "high": 64494.96, "low": 62599.35, "close": 63891.47}, {"time": "2024-05-05", "open": 63892.45, "high": 64610.89, "low": 62955.3, "close": 64031.13}, {"time": "2024-05-06", "open": 64038.31, "high": 65494.9, "low": 62746.24, "close": 63161.95}, {"time": "2024-05-07", "open": 63162.76, "high": 64390.46, "low": 62285.98, "close": 62334.82}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2024-04-30**
- As-of date (T-1): **2025-01-29**
- Sample size: **9**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.35% | 0.19% | 9 |
| T+7 | 55.56% | 44.44% | 0.31% | 1.12% | 9 |

## Historical Distribution Summary

T+1 Up Probability: **55.56%** (n=9)

T+7 Up Probability: **55.56%** (n=9)

T+7 Median Return: **0.31%**

For BTC, historical FOMC windows currently show a T+1 up probability of 55.56% and a T+7 up probability of 55.56%. Median T+7 return is 0.31% across 9 samples. Current classification is Neutral, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
