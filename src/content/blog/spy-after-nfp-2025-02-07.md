---
title: "Historical Performance of SPY After NFP (2025-02-07)"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-02-07"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 4.23
robust_score: -1.77
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 34
freshness_days: 389
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158310.0
event_previous: 158268.0
event_delta: 42.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.84
  mdd_t7: 0.0
  volatility: 0.81
  impact_t1_pct: 0.68
  impact_t7_pct: 1.49
probabilities:
  sample_size: 34
  t1:
    up: 47.62
    down: 52.38
    median: -0.04
    mean: -0.1
    sample: 21
  t7:
    up: 55.88
    down: 44.12
    median: 0.11
    mean: 0.81
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 18
    t1:
      up: 38.89
      down: 61.11
      median: -0.13
      mean: -0.22
      sample: 18
    t7:
      up: 56.67
      down: 43.33
      median: 0.11
      mean: 0.83
      sample: 30
related_events: [{"slug": "spy-after-nfp-2024-07-05", "title": "SPY After NFP (2024-07-05): Historical T+1/T+7 Probability", "event_date": "2024-07-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.02, "median_t7_pct": 0.96, "sample_size": 0}, {"slug": "spy-after-nfp-2024-01-05", "title": "SPY After NFP (2024-01-05): Historical T+1/T+7 Probability", "event_date": "2024-01-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.04, "median_t7_pct": 1.87, "sample_size": 0}, {"slug": "spy-after-nfp-2024-10-04", "title": "SPY After NFP (2024-10-04): Historical T+1/T+7 Probability", "event_date": "2024-10-04", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.43, "median_t7_pct": 1.15, "sample_size": 0}]
chartData: [{"time": "2025-02-04", "open": 590.89, "high": 595.31, "low": 590.35, "close": 594.8}, {"time": "2025-02-05", "open": 593.67, "high": 597.36, "low": 591.63, "close": 597.21}, {"time": "2025-02-06", "open": 598.96, "high": 599.41, "low": 595.64, "close": 599.28}, {"time": "2025-02-07", "open": 599.85, "high": 601.07, "low": 593.09, "close": 593.8}, {"time": "2025-02-10", "open": 597.02, "high": 598.47, "low": 595.74, "close": 597.83}, {"time": "2025-02-11", "open": 595.56, "high": 598.83, "low": 595.44, "close": 598.28}, {"time": "2025-02-12", "open": 592.25, "high": 597.53, "low": 591.56, "close": 596.36}, {"time": "2025-02-13", "open": 597.46, "high": 602.86, "low": 596.2, "close": 602.65}, {"time": "2025-02-14", "open": 602.86, "high": 603.9, "low": 602.0, "close": 602.62}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2025-02-07**
- As-of date (T-1): **2026-03-03**
- Freshness age: **389 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158310.0, Previous 158268.0, Delta +42.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 47.62% | 52.38% | -0.04% | -0.1% | 21 |
| T+7 | 55.88% | 44.12% | 0.11% | 0.81% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 38.89% | 61.11% | -0.13% | -0.22% | 18 |
| T+7 | 56.67% | 43.33% | 0.11% | 0.83% | 30 |

## Historical Distribution Summary

When NFP was **UP**, SPY T+1 up probability was **38.89%** (n=18).

When NFP was **UP**, SPY T+7 up probability was **56.67%** (n=30).

Same-direction T+7 median return: **0.11%**.

For SPY, historical NFP windows show all-history T+1 up probability of 47.62% and T+7 up probability of 55.88%. When NFP printed Up versus previous, T+1 up probability was 38.89% and T+7 up probability was 56.67% across 18 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
