---
title: "Historical Performance of QQQ After CPI (2025-03-12)"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-03-12"
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
freshness_days: 356
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 319.785
event_previous: 319.679
event_delta: 0.106
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.32
  mdd_t7: -1.8
  volatility: 2.63
  impact_t1_pct: -1.8
  impact_t7_pct: 0.83
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
chartData: [{"time": "2025-03-10", "open": 481.01, "high": 481.53, "low": 466.3, "close": 470.34}, {"time": "2025-03-11", "open": 469.97, "high": 476.39, "low": 464.65, "close": 469.22}, {"time": "2025-03-12", "open": 476.74, "high": 478.63, "low": 469.41, "close": 474.51}, {"time": "2025-03-13", "open": 473.85, "high": 473.88, "low": 464.08, "close": 465.98}, {"time": "2025-03-14", "open": 471.34, "high": 478.14, "low": 470.73, "close": 477.24}, {"time": "2025-03-17", "open": 477.19, "high": 483.39, "low": 475.39, "close": 480.33}, {"time": "2025-03-18", "open": 476.99, "high": 477.19, "low": 470.03, "close": 472.15}, {"time": "2025-03-19", "open": 474.4, "high": 482.88, "low": 472.47, "close": 478.46}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2025-03-12**
- As-of date (T-1): **2026-03-03**
- Freshness age: **356 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 319.785, Previous 319.679, Delta +0.1060)
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
