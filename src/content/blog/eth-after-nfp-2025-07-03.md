---
title: "Historical Performance of ETH After NFP (2025-07-03)"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-07-03"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 4.94
robust_score: -1.06
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 34
freshness_days: 243
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158542.0
event_previous: 158478.0
event_delta: 64.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.81
  mdd_t7: -3.18
  volatility: 17.23
  impact_t1_pct: -3.18
  impact_t7_pct: 14.04
probabilities:
  sample_size: 34
  t1:
    up: 50.0
    down: 50.0
    median: 0.0
    mean: -0.15
    sample: 34
  t7:
    up: 55.88
    down: 44.12
    median: 1.44
    mean: 2.65
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 30
    t1:
      up: 50.0
      down: 50.0
      median: 0.0
      mean: -0.14
      sample: 30
    t7:
      up: 53.33
      down: 46.67
      median: 0.79
      mean: 2.65
      sample: 30
related_events: [{"slug": "eth-after-nfp-2026-02-11", "title": "ETH After NFP (2026-02-11): Historical T+1/T+7 Probability", "event_date": "2026-02-11", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.69, "sample_size": 0}, {"slug": "eth-after-nfp-2026-02-06", "title": "ETH After NFP (2026-02-06): Historical T+1/T+7 Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.72, "sample_size": 0}, {"slug": "eth-after-nfp-2026-01-09", "title": "ETH After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 6.89, "sample_size": 0}]
chartData: [{"time": "2025-06-30", "open": 2500.61, "high": 2521.72, "low": 2438.05, "close": 2486.46}, {"time": "2025-07-01", "open": 2486.43, "high": 2500.59, "low": 2389.82, "close": 2405.79}, {"time": "2025-07-02", "open": 2405.86, "high": 2616.78, "low": 2378.39, "close": 2571.34}, {"time": "2025-07-03", "open": 2570.8, "high": 2635.19, "low": 2558.58, "close": 2591.01}, {"time": "2025-07-04", "open": 2590.85, "high": 2601.12, "low": 2475.75, "close": 2508.52}, {"time": "2025-07-05", "open": 2508.1, "high": 2529.84, "low": 2489.0, "close": 2517.28}, {"time": "2025-07-06", "open": 2517.28, "high": 2603.06, "low": 2505.37, "close": 2571.24}, {"time": "2025-07-07", "open": 2571.4, "high": 2589.32, "low": 2517.9, "close": 2543.01}, {"time": "2025-07-08", "open": 2542.97, "high": 2626.66, "low": 2525.44, "close": 2615.51}, {"time": "2025-07-09", "open": 2615.51, "high": 2794.52, "low": 2591.95, "close": 2770.78}, {"time": "2025-07-10", "open": 2770.74, "high": 2995.15, "low": 2757.27, "close": 2954.85}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2025-07-03**
- As-of date (T-1): **2026-03-03**
- Freshness age: **243 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158542.0, Previous 158478.0, Delta +64.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.15% | 34 |
| T+7 | 55.88% | 44.12% | 1.44% | 2.65% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.14% | 30 |
| T+7 | 53.33% | 46.67% | 0.79% | 2.65% | 30 |

## Historical Distribution Summary

When NFP was **UP**, ETH T+1 up probability was **50.0%** (n=30).

When NFP was **UP**, ETH T+7 up probability was **53.33%** (n=30).

Same-direction T+7 median return: **0.79%**.

For ETH, historical NFP windows show all-history T+1 up probability of 50.0% and T+7 up probability of 55.88%. When NFP printed Up versus previous, T+1 up probability was 50.0% and T+7 up probability was 53.33% across 30 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
