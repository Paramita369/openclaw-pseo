---
title: "Historical Performance of BTC After CPI (2025-12-18)"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-12-18"
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
freshness_days: 75
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 326.031
event_previous: 325.063
event_delta: 0.968
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 2.03
  mdd_t7: 0.0
  volatility: 1.02
  impact_t1_pct: 3.09
  impact_t7_pct: 2.07
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
chartData: [{"time": "2025-12-15", "open": 88171.08, "high": 89983.92, "low": 85304.08, "close": 86419.78}, {"time": "2025-12-16", "open": 86424.41, "high": 88170.09, "low": 85381.69, "close": 87843.98}, {"time": "2025-12-17", "open": 87847.62, "high": 90264.57, "low": 85316.27, "close": 86143.76}, {"time": "2025-12-18", "open": 86144.37, "high": 89412.66, "low": 84436.31, "close": 85462.51}, {"time": "2025-12-19", "open": 85476.13, "high": 89339.12, "low": 85107.66, "close": 88103.38}, {"time": "2025-12-20", "open": 88101.67, "high": 88497.2, "low": 87924.88, "close": 88344.0}, {"time": "2025-12-21", "open": 88344.7, "high": 89027.95, "low": 87613.2, "close": 88621.75}, {"time": "2025-12-22", "open": 88621.4, "high": 90501.93, "low": 87908.07, "close": 88490.02}, {"time": "2025-12-23", "open": 88490.03, "high": 88898.38, "low": 86606.98, "close": 87414.0}, {"time": "2025-12-24", "open": 87404.32, "high": 87956.88, "low": 86411.8, "close": 87611.96}, {"time": "2025-12-25", "open": 87608.32, "high": 88501.79, "low": 86949.26, "close": 87234.74}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2025-12-18**
- As-of date (T-1): **2026-03-03**
- Freshness age: **75 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.031, Previous 325.063, Delta +0.9680)
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
