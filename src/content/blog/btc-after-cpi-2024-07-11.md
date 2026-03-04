---
title: "Historical Performance of BTC After CPI (2024-07-11)"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-07-11"
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
freshness_days: 600
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 313.569
event_previous: 313.044
event_delta: 0.525
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 1.09
  mdd_t7: 0.0
  volatility: 10.59
  impact_t1_pct: 0.97
  impact_t7_pct: 11.56
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
chartData: [{"time": "2024-07-08", "open": 55849.57, "high": 58131.34, "low": 54321.02, "close": 56705.1}, {"time": "2024-07-09", "open": 56704.6, "high": 58239.2, "low": 56316.88, "close": 58009.23}, {"time": "2024-07-10", "open": 58033.88, "high": 59359.43, "low": 57178.41, "close": 57742.5}, {"time": "2024-07-11", "open": 57729.89, "high": 59299.43, "low": 57120.38, "close": 57344.91}, {"time": "2024-07-12", "open": 57341.2, "high": 58532.55, "low": 56590.18, "close": 57899.46}, {"time": "2024-07-13", "open": 57908.74, "high": 59787.08, "low": 57796.44, "close": 59231.95}, {"time": "2024-07-14", "open": 59225.25, "high": 61329.53, "low": 59225.25, "close": 60787.79}, {"time": "2024-07-15", "open": 60815.46, "high": 64870.15, "low": 60704.93, "close": 64870.15}, {"time": "2024-07-16", "open": 64784.42, "high": 65354.34, "low": 62487.97, "close": 65097.15}, {"time": "2024-07-17", "open": 65091.83, "high": 66066.73, "low": 63896.09, "close": 64118.79}, {"time": "2024-07-18", "open": 64104.74, "high": 65104.66, "low": 63246.16, "close": 63974.07}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2024-07-11**
- As-of date (T-1): **2026-03-03**
- Freshness age: **600 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 313.569, Previous 313.044, Delta +0.5250)
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
