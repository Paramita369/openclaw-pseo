---
title: "Historical Performance of BTC After CPI (2024-02-13)"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-02-13"
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
quality_score: 90
sample_size: 39
freshness_days: 749
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 310.967
event_previous: 309.698
event_delta: 1.269
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 5.56
  mdd_t7: 0.0
  volatility: 0.92
  impact_t1_pct: 4.19
  impact_t7_pct: 5.11
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
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.53
      mean: 0.44
      sample: 38
    t7:
      up: 55.26
      down: 44.74
      median: 1.26
      mean: 0.58
      sample: 38
related_events: [{"slug": "btc-after-cpi-2024-08-14", "title": "BTC After CPI (2024-08-14): Historical T+1/T+7 Probability", "event_date": "2024-08-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.86, "median_t7_pct": 4.15, "sample_size": 0}, {"slug": "btc-after-cpi-2026-02-13", "title": "BTC After CPI (2026-02-13): Historical T+1/T+7 Probability", "event_date": "2026-02-13", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.24, "sample_size": 0}, {"slug": "btc-after-cpi-2026-02-12", "title": "BTC After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 0}]
chartData: [{"time": "2024-02-10", "open": 47153.53, "high": 48146.17, "low": 46905.32, "close": 47771.28}, {"time": "2024-02-11", "open": 47768.97, "high": 48535.94, "low": 47617.41, "close": 48293.92}, {"time": "2024-02-12", "open": 48296.39, "high": 50280.48, "low": 47745.76, "close": 49958.22}, {"time": "2024-02-13", "open": 49941.36, "high": 50358.39, "low": 48406.5, "close": 49742.44}, {"time": "2024-02-14", "open": 49733.45, "high": 52021.37, "low": 49296.83, "close": 51826.7}, {"time": "2024-02-15", "open": 51836.79, "high": 52820.07, "low": 51371.63, "close": 51938.55}, {"time": "2024-02-16", "open": 51937.73, "high": 52537.97, "low": 51641.37, "close": 52160.2}, {"time": "2024-02-17", "open": 52161.68, "high": 52191.91, "low": 50669.67, "close": 51663.0}, {"time": "2024-02-18", "open": 51661.97, "high": 52356.96, "low": 51233.71, "close": 52122.55}, {"time": "2024-02-19", "open": 52134.81, "high": 52483.32, "low": 51711.82, "close": 51779.14}, {"time": "2024-02-20", "open": 51777.73, "high": 52945.05, "low": 50792.31, "close": 52284.88}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2024-02-13**
- As-of date (T-1): **2026-03-03**
- Freshness age: **749 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 310.967, Previous 309.698, Delta +1.2690)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.51% | 0.37% | 39 |
| T+7 | 53.85% | 46.15% | 1.11% | 0.44% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.53% | 0.44% | 38 |
| T+7 | 55.26% | 44.74% | 1.26% | 0.58% | 38 |

## Historical Distribution Summary

When CPI was **UP**, BTC T+1 up probability was **60.53%** (n=38).

When CPI was **UP**, BTC T+7 up probability was **55.26%** (n=38).

Same-direction T+7 median return: **1.26%**.

For BTC, historical CPI windows show all-history T+1 up probability of 58.97% and T+7 up probability of 53.85%. When CPI printed Up versus previous, T+1 up probability was 60.53% and T+7 up probability was 55.26% across 38 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
