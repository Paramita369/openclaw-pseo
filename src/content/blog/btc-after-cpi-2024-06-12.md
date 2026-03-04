---
title: "Historical Performance of BTC After CPI (2024-06-12)"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-06-12"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 6.62
robust_score: 0.62
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 60
sample_size: 39
freshness_days: 629
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 313.044
event_previous: 313.175
event_delta: -0.131
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -1.83
  mdd_t7: -4.81
  volatility: 2.63
  impact_t1_pct: -2.18
  impact_t7_pct: -4.81
probabilities:
  sample_size: 39
  t1:
    up: 58.97
    down: 41.03
    median: 0.51
    mean: 0.37
    sample: 39
  t7:
    up: 53.85
    down: 46.15
    median: 1.11
    mean: 0.44
    sample: 39
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 1
    t1:
      up: 0.0
      down: 100.0
      median: -2.18
      mean: -2.18
      sample: 1
    t7:
      up: 0.0
      down: 100.0
      median: -4.81
      mean: -4.81
      sample: 1
related_events: [{"slug": "btc-after-cpi-2024-08-14", "title": "BTC After CPI (2024-08-14): Historical T+1/T+7 Probability", "event_date": "2024-08-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.86, "median_t7_pct": 4.15, "sample_size": 0}, {"slug": "btc-after-cpi-2026-02-13", "title": "BTC After CPI (2026-02-13): Historical T+1/T+7 Probability", "event_date": "2026-02-13", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.24, "sample_size": 0}, {"slug": "btc-after-cpi-2026-02-12", "title": "BTC After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 0}]
chartData: [{"time": "2024-06-09", "open": 69297.49, "high": 69817.52, "low": 69160.84, "close": 69647.99}, {"time": "2024-06-10", "open": 69644.31, "high": 70146.07, "low": 69232.42, "close": 69512.28}, {"time": "2024-06-11", "open": 69508.08, "high": 69549.41, "low": 66123.6, "close": 67332.03}, {"time": "2024-06-12", "open": 67321.38, "high": 69977.89, "low": 66902.45, "close": 68241.19}, {"time": "2024-06-13", "open": 68243.1, "high": 68365.78, "low": 66304.56, "close": 66756.4}, {"time": "2024-06-14", "open": 66747.57, "high": 67294.65, "low": 65056.89, "close": 66011.09}, {"time": "2024-06-15", "open": 66006.74, "high": 66402.19, "low": 65871.77, "close": 66191.0}, {"time": "2024-06-16", "open": 66189.36, "high": 66894.84, "low": 66018.25, "close": 66639.05}, {"time": "2024-06-17", "open": 66636.52, "high": 67188.32, "low": 65094.96, "close": 66490.3}, {"time": "2024-06-18", "open": 66490.98, "high": 66556.7, "low": 64066.96, "close": 65140.75}, {"time": "2024-06-19", "open": 65146.66, "high": 65695.35, "low": 64693.3, "close": 64960.3}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2024-06-12**
- As-of date (T-1): **2026-03-03**
- Freshness age: **629 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **DOWN** (Actual 313.044, Previous 313.175, Delta -0.1310)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.51% | 0.37% | 39 |
| T+7 | 53.85% | 46.15% | 1.11% | 0.44% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | -2.18% | -2.18% | 1 |
| T+7 | 0.0% | 100.0% | -4.81% | -4.81% | 1 |

## Historical Distribution Summary

When CPI was **DOWN**, BTC T+1 up probability was **0.0%** (n=1).

When CPI was **DOWN**, BTC T+7 up probability was **0.0%** (n=1).

Same-direction T+7 median return: **-4.81%**.

For BTC, historical CPI windows show all-history T+1 up probability of 58.97% and T+7 up probability of 53.85%. When CPI printed Down versus previous, T+1 up probability was 0.0% and T+7 up probability was 0.0% across 1 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
