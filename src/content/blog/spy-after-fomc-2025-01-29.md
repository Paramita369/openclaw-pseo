---
title: "SPY After FOMC (2025-01-29): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around FOMC events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-01-29"
asof_date: "2025-01-29"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
confidence_level: "normal"
quality_score: 80
sample_size: 9
tags: ["spy", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 9.47
  mdd_t7: -0.14
  volatility: 0.0
  impact_t1_pct: 0.54
  impact_t7_pct: 0.4
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
chartData: [{"time": "2025-01-27", "open": 587.91, "high": 592.73, "low": 587.74, "close": 592.41}, {"time": "2025-01-28", "open": 593.65, "high": 598.34, "low": 590.32, "close": 597.5}, {"time": "2025-01-29", "open": 596.71, "high": 597.12, "low": 592.26, "close": 594.82}, {"time": "2025-01-30", "open": 596.95, "high": 599.56, "low": 593.75, "close": 598.02}, {"time": "2025-01-31", "open": 600.45, "high": 602.88, "low": 594.07, "close": 594.83}, {"time": "2025-02-03", "open": 585.79, "high": 593.32, "low": 583.64, "close": 590.83}, {"time": "2025-02-04", "open": 590.89, "high": 595.31, "low": 590.35, "close": 594.8}, {"time": "2025-02-05", "open": 593.67, "high": 597.36, "low": 591.63, "close": 597.21}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **SPY**
- Event date: **2025-01-29**
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
