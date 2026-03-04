---
title: "Historical Performance of SPY After CPI (2025-11-12)"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-11-12"
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
quality_score: 90
sample_size: 39
freshness_days: 111
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 325.063
event_previous: 324.245
event_delta: 0.818
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -2.2
  mdd_t7: -3.04
  volatility: 1.38
  impact_t1_pct: -1.66
  impact_t7_pct: -3.04
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
    direction: "up"
    sample_size: 38
    t1:
      up: 63.16
      down: 36.84
      median: 0.14
      mean: 0.21
      sample: 38
    t7:
      up: 68.42
      down: 31.58
      median: 0.51
      mean: 0.21
      sample: 38
related_events: [{"slug": "spy-after-cpi-2024-03-12", "title": "SPY After CPI (2024-03-12): Historical T+1/T+7 Probability", "event_date": "2024-03-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 3.94, "median_t7_pct": 0.1, "sample_size": 0}, {"slug": "spy-after-cpi-2024-11-14", "title": "SPY After CPI (2024-11-14): Historical T+1/T+7 Probability", "event_date": "2024-11-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.43, "median_t7_pct": 0.05, "sample_size": 0}, {"slug": "spy-after-cpi-2024-05-15", "title": "SPY After CPI (2024-05-15): Historical T+1/T+7 Probability", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.37, "median_t7_pct": 0.01, "sample_size": 0}]
chartData: [{"time": "2025-11-10", "open": 675.24, "high": 680.17, "low": 673.04, "close": 679.43}, {"time": "2025-11-11", "open": 677.95, "high": 681.56, "low": 676.73, "close": 680.99}, {"time": "2025-11-12", "open": 682.77, "high": 682.94, "low": 678.94, "close": 681.37}, {"time": "2025-11-13", "open": 678.5, "high": 678.85, "low": 668.54, "close": 670.06}, {"time": "2025-11-14", "open": 663.42, "high": 673.67, "low": 661.32, "close": 669.95}, {"time": "2025-11-17", "open": 667.73, "high": 671.73, "low": 660.22, "close": 663.71}, {"time": "2025-11-18", "open": 660.15, "high": 663.16, "low": 653.93, "close": 658.14}, {"time": "2025-11-19", "open": 658.83, "high": 665.37, "low": 656.81, "close": 660.68}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2025-11-12**
- As-of date (T-1): **2026-03-03**
- Freshness age: **111 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 325.063, Previous 324.245, Delta +0.8180)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 64.1% | 35.9% | 0.16% | 0.21% | 39 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 63.16% | 36.84% | 0.14% | 0.21% | 38 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Historical Distribution Summary

When CPI was **UP**, SPY T+1 up probability was **63.16%** (n=38).

When CPI was **UP**, SPY T+7 up probability was **68.42%** (n=38).

Same-direction T+7 median return: **0.51%**.

For SPY, historical CPI windows show all-history T+1 up probability of 64.1% and T+7 up probability of 68.42%. When CPI printed Up versus previous, T+1 up probability was 63.16% and T+7 up probability was 68.42% across 38 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
