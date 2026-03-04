---
title: "Historical Performance of SPY After NFP (2024-05-03)"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-05-03"
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
quality_score: 80
sample_size: 34
freshness_days: 669
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 157608.0
event_previous: 157530.0
event_delta: 78.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.95
  mdd_t7: -0.1
  volatility: 1.97
  impact_t1_pct: -0.1
  impact_t7_pct: 1.87
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
chartData: [{"time": "2024-04-30", "open": 497.83, "high": 498.81, "low": 491.39, "close": 491.39}, {"time": "2024-05-01", "open": 490.8, "high": 497.47, "low": 489.33, "close": 489.8}, {"time": "2024-05-02", "open": 493.52, "high": 495.22, "low": 489.01, "close": 494.38}, {"time": "2024-05-03", "open": 500.38, "high": 501.74, "low": 497.83, "close": 500.51}, {"time": "2024-05-06", "open": 502.91, "high": 505.71, "low": 502.47, "close": 505.67}, {"time": "2024-05-07", "open": 506.64, "high": 507.63, "low": 505.56, "close": 506.23}, {"time": "2024-05-08", "open": 504.39, "high": 506.82, "low": 504.27, "close": 506.28}, {"time": "2024-05-09", "open": 506.47, "high": 509.24, "low": 505.81, "close": 509.2}, {"time": "2024-05-10", "open": 510.8, "high": 511.62, "low": 508.63, "close": 509.85}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2024-05-03**
- As-of date (T-1): **2026-03-03**
- Freshness age: **669 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157608.0, Previous 157530.0, Delta +78.0000)
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
