---
title: "Historical Performance of ETH After CPI (2026-02-13)"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-02-13"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -2.51
robust_score: -2.51
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 39
freshness_days: 18
freshness_status: "fresh"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 326.588
event_previous: 326.031
event_delta: 0.557
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -0.68
  mdd_t7: -3.88
  volatility: 5.71
  impact_t1_pct: 1.83
  impact_t7_pct: -3.88
probabilities:
  sample_size: 39
  t1:
    up: 58.97
    down: 41.03
    median: 0.94
    mean: 0.55
    sample: 39
  t7:
    up: 43.59
    down: 56.41
    median: -1.18
    mean: 0.23
    sample: 39
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.96
      mean: 0.64
      sample: 38
    t7:
      up: 44.74
      down: 55.26
      median: -1.52
      mean: 0.24
      sample: 38
related_events: [{"slug": "eth-after-cpi-2024-06-12", "title": "ETH After CPI (2024-06-12): Historical T+1/T+7 Probability", "event_date": "2024-06-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.22, "median_t7_pct": -0.01, "sample_size": 0}, {"slug": "eth-after-cpi-2026-02-12", "title": "ETH After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.06, "sample_size": 0}, {"slug": "eth-after-cpi-2026-01-13", "title": "ETH After CPI (2026-01-13): Historical T+1/T+7 Probability", "event_date": "2026-01-13", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -11.63, "sample_size": 0}]
chartData: [{"time": "2026-02-10", "open": 2104.18, "high": 2122.02, "low": 1990.14, "close": 2019.5}, {"time": "2026-02-11", "open": 2019.58, "high": 2030.41, "low": 1903.69, "close": 1940.62}, {"time": "2026-02-12", "open": 1940.84, "high": 1999.5, "low": 1897.33, "close": 1946.94}, {"time": "2026-02-13", "open": 1946.61, "high": 2069.46, "low": 1924.14, "close": 2048.53}, {"time": "2026-02-14", "open": 2048.33, "high": 2105.07, "low": 2042.64, "close": 2086.01}, {"time": "2026-02-15", "open": 2085.95, "high": 2100.48, "low": 1929.39, "close": 1966.04}, {"time": "2026-02-16", "open": 1965.92, "high": 2021.08, "low": 1938.55, "close": 1997.92}, {"time": "2026-02-17", "open": 1997.92, "high": 2013.86, "low": 1941.78, "close": 1992.19}, {"time": "2026-02-18", "open": 1992.2, "high": 2037.16, "low": 1923.81, "close": 1953.97}, {"time": "2026-02-19", "open": 1953.99, "high": 1985.81, "low": 1906.82, "close": 1948.2}, {"time": "2026-02-20", "open": 1948.27, "high": 1980.24, "low": 1923.62, "close": 1969.02}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2026-02-13**
- As-of date (T-1): **2026-03-03**
- Freshness age: **18 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.588, Previous 326.031, Delta +0.5570)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.94% | 0.55% | 39 |
| T+7 | 43.59% | 56.41% | -1.18% | 0.23% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.96% | 0.64% | 38 |
| T+7 | 44.74% | 55.26% | -1.52% | 0.24% | 38 |

## Historical Distribution Summary

When CPI was **UP**, ETH T+1 up probability was **60.53%** (n=38).

When CPI was **UP**, ETH T+7 up probability was **44.74%** (n=38).

Same-direction T+7 median return: **-1.52%**.

For ETH, historical CPI windows show all-history T+1 up probability of 58.97% and T+7 up probability of 43.59%. When CPI printed Up versus previous, T+1 up probability was 60.53% and T+7 up probability was 44.74% across 38 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
