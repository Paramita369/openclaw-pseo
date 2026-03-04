---
title: "Historical Performance of ETH After FOMC (2025-12-11)"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-12-11"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Bearish"
raw_signal_score: -13.74
robust_score: -13.74
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 23
freshness_days: 82
freshness_status: "fresh"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 3.75
event_previous: 4.0
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.6
  mdd_t7: -12.67
  volatility: 7.94
  impact_t1_pct: -4.72
  impact_t7_pct: -12.67
probabilities:
  sample_size: 23
  t1:
    up: 43.48
    down: 56.52
    median: -0.1
    mean: 0.91
    sample: 23
  t7:
    up: 30.43
    down: 69.57
    median: -3.26
    mean: -2.8
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 6
    t1:
      up: 66.67
      down: 33.33
      median: 1.36
      mean: 0.84
      sample: 6
    t7:
      up: 33.33
      down: 66.67
      median: -7.6
      mean: -5.39
      sample: 6
related_events: [{"slug": "eth-after-fomc-2024-01-30", "title": "ETH After FOMC (2024-01-30): Historical T+1/T+7 Probability", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 3.74, "median_t7_pct": 1.18, "sample_size": 0}, {"slug": "eth-after-fomc-2026-01-28", "title": "ETH After FOMC (2026-01-28): Historical T+1/T+7 Probability", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -28.71, "sample_size": 0}, {"slug": "eth-after-fomc-2025-12-10", "title": "ETH After FOMC (2025-12-10): Historical T+1/T+7 Probability", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -14.86, "sample_size": 0}]
chartData: [{"time": "2025-12-08", "open": 3061.01, "high": 3177.87, "low": 3043.7, "close": 3125.2}, {"time": "2025-12-09", "open": 3124.94, "high": 3395.84, "low": 3092.88, "close": 3321.11}, {"time": "2025-12-10", "open": 3321.2, "high": 3446.62, "low": 3290.15, "close": 3325.39}, {"time": "2025-12-11", "open": 3324.39, "high": 3327.34, "low": 3149.03, "close": 3237.06}, {"time": "2025-12-12", "open": 3237.03, "high": 3265.37, "low": 3050.27, "close": 3084.17}, {"time": "2025-12-13", "open": 3084.13, "high": 3134.85, "low": 3080.08, "close": 3116.7}, {"time": "2025-12-14", "open": 3116.74, "high": 3128.62, "low": 3034.69, "close": 3060.59}, {"time": "2025-12-15", "open": 3060.48, "high": 3175.12, "low": 2899.69, "close": 2964.18}, {"time": "2025-12-16", "open": 2964.38, "high": 2978.92, "low": 2890.01, "close": 2964.18}, {"time": "2025-12-17", "open": 2964.02, "high": 3025.82, "low": 2791.33, "close": 2831.4}, {"time": "2025-12-18", "open": 2831.49, "high": 2994.55, "low": 2777.12, "close": 2827.07}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2025-12-11**
- As-of date (T-1): **2026-03-03**
- Freshness age: **82 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 3.75, Previous 4.0, Delta -0.2500)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 43.48% | 56.52% | -0.1% | 0.91% | 23 |
| T+7 | 30.43% | 69.57% | -3.26% | -2.8% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 66.67% | 33.33% | 1.36% | 0.84% | 6 |
| T+7 | 33.33% | 66.67% | -7.6% | -5.39% | 6 |

## Historical Distribution Summary

When FOMC was **DOWN**, ETH T+1 up probability was **66.67%** (n=6).

When FOMC was **DOWN**, ETH T+7 up probability was **33.33%** (n=6).

Same-direction T+7 median return: **-7.6%**.

For ETH, historical FOMC windows show all-history T+1 up probability of 43.48% and T+7 up probability of 30.43%. When FOMC printed Down versus previous, T+1 up probability was 66.67% and T+7 up probability was 33.33% across 6 matched cases. Current classification is Bearish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
