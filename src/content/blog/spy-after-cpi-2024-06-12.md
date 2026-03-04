---
title: "Historical Performance of SPY After CPI (2024-06-12)"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-06-12"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 15.44
robust_score: 9.44
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 50
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
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 21.0
  mdd_t7: 0.0
  volatility: 0.01
  impact_t1_pct: 0.2
  impact_t7_pct: 0.21
probabilities:
  sample_size: 39
  t1:
    up: 64.1
    down: 35.9
    median: 0.16
    mean: 0.21
    sample: 39
  t7:
    up: 68.42
    down: 31.58
    median: 0.51
    mean: 0.21
    sample: 38
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 0
    t1:
      up: 100.0
      down: 0.0
      median: 0.2
      mean: 0.2
      sample: 1
    t7:
      up: 0.0
      down: 100.0
      median: 0.0
      mean: 0.0
      sample: 0
related_events: [{"slug": "spy-after-cpi-2024-03-12", "title": "SPY After CPI (2024-03-12): Historical T+1/T+7 Probability", "event_date": "2024-03-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 3.94, "median_t7_pct": 0.1, "sample_size": 0}, {"slug": "spy-after-cpi-2024-11-14", "title": "SPY After CPI (2024-11-14): Historical T+1/T+7 Probability", "event_date": "2024-11-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.43, "median_t7_pct": 0.05, "sample_size": 0}, {"slug": "spy-after-cpi-2024-05-15", "title": "SPY After CPI (2024-05-15): Historical T+1/T+7 Probability", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.37, "median_t7_pct": 0.01, "sample_size": 0}]
chartData: [{"time": "2024-06-10", "open": 521.93, "high": 524.68, "low": 521.34, "close": 524.36}, {"time": "2024-06-11", "open": 522.8, "high": 525.68, "low": 520.83, "close": 525.62}, {"time": "2024-06-12", "open": 530.21, "high": 532.64, "low": 528.9, "close": 529.94}, {"time": "2024-06-13", "open": 531.69, "high": 531.87, "low": 528.21, "close": 531.01}, {"time": "2024-06-14", "open": 529.47, "high": 531.36, "low": 528.46, "close": 531.33}, {"time": "2024-06-17", "open": 530.65, "high": 536.96, "low": 530.19, "close": 535.56}, {"time": "2024-06-18", "open": 535.62, "high": 537.05, "low": 535.2, "close": 536.92}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
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
| T+1 | 64.1% | 35.9% | 0.16% | 0.21% | 39 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 100.0% | 0.0% | 0.2% | 0.2% | 1 |
| T+7 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |

## Historical Distribution Summary

When CPI was **DOWN**, SPY T+1 up probability was **100.0%** (n=1).

When CPI was **DOWN**, SPY T+7 up probability was **0.0%** (n=0).

Same-direction T+7 median return: **0.0%**.

For SPY, historical CPI windows show all-history T+1 up probability of 64.1% and T+7 up probability of 68.42%. When CPI printed Down versus previous, T+1 up probability was 100.0% and T+7 up probability was 0.0% across 0 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
