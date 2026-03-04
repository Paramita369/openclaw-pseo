---
title: "Historical Performance of GOLD After CPI (2025-06-11)"
description: "Historical probability profile for GOLD around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-06-11"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 18.4
robust_score: 12.4
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 39
freshness_days: 265
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 321.435
event_previous: 320.62
event_delta: 0.815
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 7.64
  mdd_t7: 0.0
  volatility: 0.27
  impact_t1_pct: 1.79
  impact_t7_pct: 2.06
probabilities:
  sample_size: 39
  t1:
    up: 56.41
    down: 43.59
    median: 0.34
    mean: 0.3
    sample: 39
  t7:
    up: 78.95
    down: 21.05
    median: 1.4
    mean: 1.49
    sample: 38
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 57.89
      down: 42.11
      median: 0.42
      mean: 0.35
      sample: 38
    t7:
      up: 78.95
      down: 21.05
      median: 1.4
      mean: 1.49
      sample: 38
related_events: [{"slug": "gold-after-cpi-2025-02-12", "title": "GOLD After CPI (2025-02-12): Historical T+1/T+7 Probability", "event_date": "2025-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 7.09, "median_t7_pct": 0.36, "sample_size": 0}, {"slug": "gold-after-cpi-2024-02-20", "title": "GOLD After CPI (2024-02-20): Historical T+1/T+7 Probability", "event_date": "2024-02-20", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 6.12, "median_t7_pct": 0.32, "sample_size": 0}, {"slug": "gold-after-cpi-2024-05-15", "title": "GOLD After CPI (2024-05-15): Historical T+1/T+7 Probability", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.47, "median_t7_pct": 0.02, "sample_size": 0}]
chartData: [{"time": "2025-06-09", "open": 3315.6, "high": 3334.6, "low": 3290.0, "close": 3332.1}, {"time": "2025-06-10", "open": 3302.0, "high": 3344.3, "low": 3302.0, "close": 3320.9}, {"time": "2025-06-11", "open": 3328.0, "high": 3356.0, "low": 3321.3, "close": 3321.3}, {"time": "2025-06-12", "open": 3363.0, "high": 3395.9, "low": 3353.4, "close": 3380.9}, {"time": "2025-06-13", "open": 3407.3, "high": 3444.0, "low": 3407.3, "close": 3431.2}, {"time": "2025-06-16", "open": 3442.0, "high": 3442.0, "low": 3385.4, "close": 3396.4}, {"time": "2025-06-17", "open": 3398.3, "high": 3398.3, "low": 3376.1, "close": 3386.6}, {"time": "2025-06-18", "open": 3385.3, "high": 3391.9, "low": 3365.1, "close": 3389.8}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **GOLD**
- Event date: **2025-06-11**
- As-of date (T-1): **2026-03-03**
- Freshness age: **265 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 321.435, Previous 320.62, Delta +0.8150)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 56.41% | 43.59% | 0.34% | 0.3% | 39 |
| T+7 | 78.95% | 21.05% | 1.4% | 1.49% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 57.89% | 42.11% | 0.42% | 0.35% | 38 |
| T+7 | 78.95% | 21.05% | 1.4% | 1.49% | 38 |

## Historical Distribution Summary

When CPI was **UP**, GOLD T+1 up probability was **57.89%** (n=38).

When CPI was **UP**, GOLD T+7 up probability was **78.95%** (n=38).

Same-direction T+7 median return: **1.4%**.

For GOLD, historical CPI windows show all-history T+1 up probability of 56.41% and T+7 up probability of 78.95%. When CPI printed Up versus previous, T+1 up probability was 57.89% and T+7 up probability was 78.95% across 38 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
