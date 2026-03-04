---
title: "Historical Performance of ETH After FOMC (2024-12-17)"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-12-17"
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
freshness_days: 441
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "flat"
event_actual: 4.75
event_previous: 4.75
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -3.11
  mdd_t7: -10.16
  volatility: 3.27
  impact_t1_pct: -6.89
  impact_t7_pct: -10.16
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
chartData: [{"time": "2024-12-14", "open": 3910.85, "high": 3943.28, "low": 3826.76, "close": 3868.41}, {"time": "2024-12-15", "open": 3868.44, "high": 3971.5, "low": 3832.1, "close": 3951.94}, {"time": "2024-12-16", "open": 3951.65, "high": 4106.96, "low": 3882.71, "close": 3987.48}, {"time": "2024-12-17", "open": 3987.33, "high": 4040.34, "low": 3849.29, "close": 3886.77}, {"time": "2024-12-18", "open": 3886.89, "high": 3902.72, "low": 3617.84, "close": 3618.79}, {"time": "2024-12-19", "open": 3619.58, "high": 3717.66, "low": 3330.87, "close": 3417.93}, {"time": "2024-12-20", "open": 3417.93, "high": 3496.33, "low": 3098.2, "close": 3472.55}, {"time": "2024-12-21", "open": 3472.59, "high": 3552.92, "low": 3293.51, "close": 3337.22}, {"time": "2024-12-22", "open": 3337.0, "high": 3398.66, "low": 3219.29, "close": 3277.54}, {"time": "2024-12-23", "open": 3277.51, "high": 3461.53, "low": 3217.37, "close": 3415.79}, {"time": "2024-12-24", "open": 3415.74, "high": 3535.86, "low": 3355.61, "close": 3492.05}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2024-12-17**
- As-of date (T-1): **2026-03-03**
- Freshness age: **441 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.75, Previous 4.75, Delta +0.0000)
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
