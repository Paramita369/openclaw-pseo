---
title: "BTC After FOMC (2024-01-30): Historical T+1/T+7 Probability"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-01-30"
asof_date: "2025-01-29"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
confidence_level: "normal"
quality_score: 80
sample_size: 9
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 2.97
  mdd_t7: -0.86
  volatility: 0.0
  impact_t1_pct: -0.86
  impact_t7_pct: 0.31
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
chartData: [{"time": "2024-01-27", "open": 41815.62, "high": 42195.63, "low": 41431.28, "close": 42120.05}, {"time": "2024-01-28", "open": 42126.12, "high": 42797.18, "low": 41696.91, "close": 42035.59}, {"time": "2024-01-29", "open": 42030.91, "high": 43305.87, "low": 41818.33, "close": 43288.25}, {"time": "2024-01-30", "open": 43300.23, "high": 43838.95, "low": 42711.37, "close": 42952.61}, {"time": "2024-01-31", "open": 42946.25, "high": 43717.41, "low": 42298.95, "close": 42582.61}, {"time": "2024-02-01", "open": 42569.76, "high": 43243.17, "low": 41879.19, "close": 43075.77}, {"time": "2024-02-02", "open": 43077.64, "high": 43422.49, "low": 42584.34, "close": 43185.86}, {"time": "2024-02-03", "open": 43184.96, "high": 43359.94, "low": 42890.81, "close": 42992.25}, {"time": "2024-02-04", "open": 42994.94, "high": 43097.64, "low": 42374.83, "close": 42583.58}, {"time": "2024-02-05", "open": 42577.62, "high": 43494.25, "low": 42264.82, "close": 42658.67}, {"time": "2024-02-06", "open": 42657.39, "high": 43344.15, "low": 42529.02, "close": 43084.67}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2024-01-30**
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
