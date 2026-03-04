---
title: "Historical Performance of BTC After NFP (2026-01-02)"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-01-02"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 0.23
robust_score: -5.77
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 34
freshness_days: 60
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158627.0
event_previous: 158497.0
event_delta: 130.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 6.32
  mdd_t7: 0.0
  volatility: 0.1
  impact_t1_pct: 0.73
  impact_t7_pct: 0.63
probabilities:
  sample_size: 34
  t1:
    up: 29.41
    down: 70.59
    median: -0.33
    mean: -0.26
    sample: 34
  t7:
    up: 58.82
    down: 41.18
    median: 1.0
    mean: 1.55
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 30
    t1:
      up: 26.67
      down: 73.33
      median: -0.39
      mean: -0.31
      sample: 30
    t7:
      up: 56.67
      down: 43.33
      median: 0.81
      mean: 1.51
      sample: 30
related_events: [{"slug": "btc-after-nfp-2026-02-11", "title": "BTC After NFP (2026-02-11): Historical T+1/T+7 Probability", "event_date": "2026-02-11", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.85, "sample_size": 0}, {"slug": "btc-after-nfp-2026-02-06", "title": "BTC After NFP (2026-02-06): Historical T+1/T+7 Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -2.41, "sample_size": 0}, {"slug": "btc-after-nfp-2026-01-09", "title": "BTC After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 5.54, "sample_size": 0}]
chartData: [{"time": "2025-12-30", "open": 87134.35, "high": 89297.94, "low": 86735.55, "close": 88430.13}, {"time": "2025-12-31", "open": 88429.59, "high": 89080.29, "low": 87130.56, "close": 87508.83}, {"time": "2026-01-01", "open": 87508.05, "high": 88803.23, "low": 87399.41, "close": 88731.98}, {"time": "2026-01-02", "open": 88733.06, "high": 90884.46, "low": 88298.62, "close": 89944.7}, {"time": "2026-01-03", "open": 89945.05, "high": 90679.57, "low": 89328.07, "close": 90603.19}, {"time": "2026-01-04", "open": 90603.0, "high": 91712.59, "low": 90595.1, "close": 91413.49}, {"time": "2026-01-05", "open": 91414.62, "high": 94762.07, "low": 91414.62, "close": 93882.55}, {"time": "2026-01-06", "open": 93876.95, "high": 94395.3, "low": 91286.55, "close": 93729.03}, {"time": "2026-01-07", "open": 93727.47, "high": 93738.79, "low": 90601.8, "close": 91308.05}, {"time": "2026-01-08", "open": 91309.64, "high": 91485.85, "low": 89233.88, "close": 91027.12}, {"time": "2026-01-09", "open": 91026.27, "high": 91910.67, "low": 89625.38, "close": 90513.1}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2026-01-02**
- As-of date (T-1): **2026-03-03**
- Freshness age: **60 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158627.0, Previous 158497.0, Delta +130.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 29.41% | 70.59% | -0.33% | -0.26% | 34 |
| T+7 | 58.82% | 41.18% | 1.0% | 1.55% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 26.67% | 73.33% | -0.39% | -0.31% | 30 |
| T+7 | 56.67% | 43.33% | 0.81% | 1.51% | 30 |

## Historical Distribution Summary

When NFP was **UP**, BTC T+1 up probability was **26.67%** (n=30).

When NFP was **UP**, BTC T+7 up probability was **56.67%** (n=30).

Same-direction T+7 median return: **0.81%**.

For BTC, historical NFP windows show all-history T+1 up probability of 29.41% and T+7 up probability of 58.82%. When NFP printed Up versus previous, T+1 up probability was 26.67% and T+7 up probability was 56.67% across 30 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
