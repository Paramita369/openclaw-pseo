---
title: "ETH After FOMC (2024-01-30): Historical T+1/T+7 Probability"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
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
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 3.74
  mdd_t7: -2.64
  volatility: 0.0
  impact_t1_pct: -2.64
  impact_t7_pct: 1.18
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
chartData: [{"time": "2024-01-27", "open": 2267.32, "high": 2282.54, "low": 2252.39, "close": 2267.89}, {"time": "2024-01-28", "open": 2268.19, "high": 2306.9, "low": 2242.68, "close": 2257.21}, {"time": "2024-01-29", "open": 2257.0, "high": 2320.03, "low": 2237.71, "close": 2317.06}, {"time": "2024-01-30", "open": 2317.44, "high": 2388.87, "low": 2298.28, "close": 2344.49}, {"time": "2024-01-31", "open": 2343.56, "high": 2349.61, "low": 2264.44, "close": 2282.54}, {"time": "2024-02-01", "open": 2282.18, "high": 2309.84, "low": 2243.57, "close": 2303.82}, {"time": "2024-02-02", "open": 2303.71, "high": 2323.05, "low": 2282.23, "close": 2308.04}, {"time": "2024-02-03", "open": 2307.98, "high": 2327.35, "low": 2293.54, "close": 2296.04}, {"time": "2024-02-04", "open": 2296.12, "high": 2309.01, "low": 2272.3, "close": 2289.55}, {"time": "2024-02-05", "open": 2289.21, "high": 2334.68, "low": 2270.07, "close": 2298.89}, {"time": "2024-02-06", "open": 2298.96, "high": 2389.83, "low": 2296.79, "close": 2372.2}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2024-01-30**
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
