---
title: "Historical Performance of ETH After NFP (2026-02-11)"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-02-11"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 4.94
robust_score: 4.94
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 34
freshness_days: 20
freshness_status: "fresh"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158627.0
event_previous: 158497.0
event_delta: 130.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.91
  mdd_t7: 0.0
  volatility: 0.36
  impact_t1_pct: 0.33
  impact_t7_pct: 0.69
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
related_events: [{"slug": "eth-after-nfp-2026-02-06", "title": "ETH After NFP (2026-02-06): Historical T+1/T+7 Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.72, "sample_size": 0}, {"slug": "eth-after-nfp-2026-01-09", "title": "ETH After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 6.89, "sample_size": 0}, {"slug": "eth-after-nfp-2026-01-02", "title": "ETH After NFP (2026-01-02): Historical T+1/T+7 Probability", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.32, "sample_size": 0}]
chartData: [{"time": "2026-02-08", "open": 2090.63, "high": 2148.12, "low": 2066.38, "close": 2088.76}, {"time": "2026-02-09", "open": 2087.92, "high": 2144.98, "low": 2008.36, "close": 2103.57}, {"time": "2026-02-10", "open": 2104.18, "high": 2122.02, "low": 1990.14, "close": 2019.5}, {"time": "2026-02-11", "open": 2019.58, "high": 2030.41, "low": 1903.69, "close": 1940.62}, {"time": "2026-02-12", "open": 1940.84, "high": 1999.5, "low": 1897.33, "close": 1946.94}, {"time": "2026-02-13", "open": 1946.61, "high": 2069.46, "low": 1924.14, "close": 2048.53}, {"time": "2026-02-14", "open": 2048.33, "high": 2105.07, "low": 2042.64, "close": 2086.01}, {"time": "2026-02-15", "open": 2085.95, "high": 2100.48, "low": 1929.39, "close": 1966.04}, {"time": "2026-02-16", "open": 1965.92, "high": 2021.08, "low": 1938.55, "close": 1997.92}, {"time": "2026-02-17", "open": 1997.92, "high": 2013.86, "low": 1941.78, "close": 1992.19}, {"time": "2026-02-18", "open": 1992.2, "high": 2037.16, "low": 1923.81, "close": 1953.97}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2026-02-11**
- As-of date (T-1): **2026-03-03**
- Freshness age: **20 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158627.0, Previous 158497.0, Delta +130.0000)
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
