---
title: "Historical Performance of QQQ After CPI (2024-07-11)"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-07-11"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 8.09
robust_score: 2.09
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
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -0.81
  mdd_t7: -2.53
  volatility: 3.12
  impact_t1_pct: 0.59
  impact_t7_pct: -2.53
probabilities:
  sample_size: 39
  t1:
    up: 61.54
    down: 38.46
    median: 0.21
    mean: 0.23
    sample: 39
  t7:
    up: 55.26
    down: 44.74
    median: 0.58
    mean: 0.2
    sample: 38
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.19
      mean: 0.23
      sample: 38
    t7:
      up: 55.26
      down: 44.74
      median: 0.58
      mean: 0.2
      sample: 38
related_events: [{"slug": "qqq-after-cpi-2024-05-15", "title": "QQQ After CPI (2024-05-15): Historical T+1/T+7 Probability", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.6, "median_t7_pct": 0.62, "sample_size": 0}, {"slug": "qqq-after-cpi-2024-09-11", "title": "QQQ After CPI (2024-09-11): Historical T+1/T+7 Probability", "event_date": "2024-09-11", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 7.08, "median_t7_pct": 0.6, "sample_size": 0}, {"slug": "qqq-after-cpi-2026-02-13", "title": "QQQ After CPI (2026-02-13): Historical T+1/T+7 Probability", "event_date": "2026-02-13", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.14, "sample_size": 0}]
chartData: [{"time": "2024-07-08", "open": 492.54, "high": 493.9, "low": 491.52, "close": 493.34}, {"time": "2024-07-09", "open": 494.86, "high": 495.98, "low": 492.25, "close": 493.77}, {"time": "2024-07-10", "open": 495.69, "high": 499.47, "low": 494.38, "close": 498.92}, {"time": "2024-07-11", "open": 499.02, "high": 499.23, "low": 486.78, "close": 487.97}, {"time": "2024-07-12", "open": 488.55, "high": 495.6, "low": 488.08, "close": 490.84}, {"time": "2024-07-15", "open": 492.62, "high": 496.98, "low": 490.12, "close": 492.16}, {"time": "2024-07-16", "open": 493.62, "high": 494.43, "low": 489.18, "close": 492.35}, {"time": "2024-07-17", "open": 484.35, "high": 484.87, "low": 477.83, "close": 477.9}, {"time": "2024-07-18", "open": 481.63, "high": 481.8, "low": 472.44, "close": 475.63}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
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
| T+1 | 61.54% | 38.46% | 0.21% | 0.23% | 39 |
| T+7 | 55.26% | 44.74% | 0.58% | 0.2% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.19% | 0.23% | 38 |
| T+7 | 55.26% | 44.74% | 0.58% | 0.2% | 38 |

## Historical Distribution Summary

When CPI was **UP**, QQQ T+1 up probability was **60.53%** (n=38).

When CPI was **UP**, QQQ T+7 up probability was **55.26%** (n=38).

Same-direction T+7 median return: **0.58%**.

For QQQ, historical CPI windows show all-history T+1 up probability of 61.54% and T+7 up probability of 55.26%. When CPI printed Up versus previous, T+1 up probability was 60.53% and T+7 up probability was 55.26% across 38 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
