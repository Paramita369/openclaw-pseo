---
title: "Historical Performance of ETH After FOMC (2025-09-17)"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-09-17"
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
freshness_days: 167
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "flat"
event_actual: 4.5
event_previous: 4.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.01
  mdd_t7: -9.56
  volatility: 9.5
  impact_t1_pct: -0.06
  impact_t7_pct: -9.56
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
chartData: [{"time": "2025-09-14", "open": 4668.17, "high": 4690.64, "low": 4581.85, "close": 4609.6}, {"time": "2025-09-15", "open": 4609.72, "high": 4670.53, "low": 4469.86, "close": 4526.82}, {"time": "2025-09-16", "open": 4526.08, "high": 4537.6, "low": 4428.33, "close": 4503.56}, {"time": "2025-09-17", "open": 4503.64, "high": 4617.23, "low": 4429.64, "close": 4592.73}, {"time": "2025-09-18", "open": 4592.44, "high": 4643.97, "low": 4556.27, "close": 4589.92}, {"time": "2025-09-19", "open": 4589.51, "high": 4620.79, "low": 4443.26, "close": 4470.92}, {"time": "2025-09-20", "open": 4470.98, "high": 4509.81, "low": 4459.16, "close": 4482.27}, {"time": "2025-09-21", "open": 4482.58, "high": 4499.39, "low": 4447.12, "close": 4451.33}, {"time": "2025-09-22", "open": 4451.58, "high": 4457.08, "low": 4092.4, "close": 4202.88}, {"time": "2025-09-23", "open": 4203.02, "high": 4227.73, "low": 4120.82, "close": 4165.5}, {"time": "2025-09-24", "open": 4165.41, "high": 4206.9, "low": 4081.35, "close": 4153.47}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2025-09-17**
- As-of date (T-1): **2026-03-03**
- Freshness age: **167 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.5, Previous 4.5, Delta +0.0000)
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
