---
title: "ETH After FOMC (2024-04-30): Historical T+1/T+7 Probability"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
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
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.24
  mdd_t7: -1.41
  volatility: 0.0
  impact_t1_pct: -1.41
  impact_t7_pct: -0.19
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 1.2
    mean: 1.38
    sample: 9
  t7:
    up: 44.44
    down: 55.56
    median: -0.19
    mean: -0.1
    sample: 9
chartData: [{"time": "2024-04-27", "open": 3129.73, "high": 3279.45, "low": 3071.34, "close": 3252.17}, {"time": "2024-04-28", "open": 3252.25, "high": 3351.18, "low": 3249.15, "close": 3262.77}, {"time": "2024-04-29", "open": 3262.34, "high": 3285.47, "low": 3116.2, "close": 3215.43}, {"time": "2024-04-30", "open": 3215.38, "high": 3249.38, "low": 2918.23, "close": 3012.29}, {"time": "2024-05-01", "open": 3011.02, "high": 3020.17, "low": 2815.92, "close": 2969.78}, {"time": "2024-05-02", "open": 2969.79, "high": 3015.05, "low": 2894.33, "close": 2988.17}, {"time": "2024-05-03", "open": 2988.13, "high": 3127.16, "low": 2960.18, "close": 3103.54}, {"time": "2024-05-04", "open": 3103.62, "high": 3167.54, "low": 3096.27, "close": 3117.58}, {"time": "2024-05-05", "open": 3117.64, "high": 3170.06, "low": 3075.59, "close": 3137.25}, {"time": "2024-05-06", "open": 3137.51, "high": 3220.15, "low": 3048.24, "close": 3062.73}, {"time": "2024-05-07", "open": 3062.75, "high": 3129.08, "low": 3003.01, "close": 3006.58}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2024-04-30**
- As-of date (T-1): **2025-01-29**
- Sample size: **9**

## Probability Table

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 1.2% | 1.38% | 9 |
| T+7 | 44.44% | 55.56% | -0.19% | -0.1% | 9 |

## Historical Distribution Summary

T+1 Up Probability: **55.56%** (n=9)

T+7 Up Probability: **44.44%** (n=9)

T+7 Median Return: **-0.19%**

For ETH, historical FOMC windows currently show a T+1 up probability of 55.56% and a T+7 up probability of 44.44%. Median T+7 return is -0.19% across 9 samples. Current classification is Neutral, which should be treated as an educational probability view, not a trade instruction.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports directional probabilities and return distribution summaries for educational use only.
