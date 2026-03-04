---
title: "Historical Performance of ETH After FOMC (2024-11-06)"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-11-06"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Bearish"
raw_signal_score: -13.74
robust_score: -19.74
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 23
freshness_days: 482
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "flat"
event_actual: 5.0
event_previous: 5.0
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 1.58
  mdd_t7: 0.0
  volatility: 10.91
  impact_t1_pct: 6.29
  impact_t7_pct: 17.2
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
    direction: "flat"
    sample_size: 17
    t1:
      up: 35.29
      down: 64.71
      median: -1.41
      mean: 0.94
      sample: 17
    t7:
      up: 29.41
      down: 70.59
      median: -3.26
      mean: -1.88
      sample: 17
related_events: [{"slug": "eth-after-fomc-2024-01-30", "title": "ETH After FOMC (2024-01-30): Historical T+1/T+7 Probability", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 3.74, "median_t7_pct": 1.18, "sample_size": 0}, {"slug": "eth-after-fomc-2026-01-28", "title": "ETH After FOMC (2026-01-28): Historical T+1/T+7 Probability", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -28.71, "sample_size": 0}, {"slug": "eth-after-fomc-2025-12-11", "title": "ETH After FOMC (2025-12-11): Historical T+1/T+7 Probability", "event_date": "2025-12-11", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -12.67, "sample_size": 0}]
chartData: [{"time": "2024-11-03", "open": 2491.09, "high": 2495.44, "low": 2411.4, "close": 2456.43}, {"time": "2024-11-04", "open": 2456.1, "high": 2488.35, "low": 2359.58, "close": 2397.03}, {"time": "2024-11-05", "open": 2397.04, "high": 2478.62, "low": 2380.6, "close": 2422.65}, {"time": "2024-11-06", "open": 2422.54, "high": 2743.96, "low": 2421.81, "close": 2724.17}, {"time": "2024-11-07", "open": 2724.01, "high": 2918.74, "low": 2701.59, "close": 2895.59}, {"time": "2024-11-08", "open": 2895.6, "high": 2983.74, "low": 2889.48, "close": 2962.3}, {"time": "2024-11-09", "open": 2962.79, "high": 3156.37, "low": 2957.18, "close": 3131.14}, {"time": "2024-11-10", "open": 3130.73, "high": 3249.91, "low": 3073.25, "close": 3191.33}, {"time": "2024-11-11", "open": 3191.66, "high": 3389.53, "low": 3109.77, "close": 3374.81}, {"time": "2024-11-12", "open": 3375.15, "high": 3444.15, "low": 3211.2, "close": 3246.26}, {"time": "2024-11-13", "open": 3244.54, "high": 3337.88, "low": 3121.67, "close": 3192.6}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2024-11-06**
- As-of date (T-1): **2026-03-03**
- Freshness age: **482 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.0, Previous 5.0, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 43.48% | 56.52% | -0.1% | 0.91% | 23 |
| T+7 | 30.43% | 69.57% | -3.26% | -2.8% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 35.29% | 64.71% | -1.41% | 0.94% | 17 |
| T+7 | 29.41% | 70.59% | -3.26% | -1.88% | 17 |

## Historical Distribution Summary

When FOMC was **FLAT**, ETH T+1 up probability was **35.29%** (n=17).

When FOMC was **FLAT**, ETH T+7 up probability was **29.41%** (n=17).

Same-direction T+7 median return: **-3.26%**.

For ETH, historical FOMC windows show all-history T+1 up probability of 43.48% and T+7 up probability of 30.43%. When FOMC printed Flat versus previous, T+1 up probability was 35.29% and T+7 up probability was 29.41% across 17 matched cases. Current classification is Bearish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
