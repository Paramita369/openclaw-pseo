---
title: "Historical Performance of BTC After NFP (2026-01-09)"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-01-09"
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
freshness_days: 53
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
  sharpe_t7: 0.97
  mdd_t7: -0.14
  volatility: 5.68
  impact_t1_pct: -0.14
  impact_t7_pct: 5.54
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
related_events: [{"slug": "btc-after-nfp-2026-02-11", "title": "BTC After NFP (2026-02-11): Historical T+1/T+7 Probability", "event_date": "2026-02-11", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.85, "sample_size": 0}, {"slug": "btc-after-nfp-2026-02-06", "title": "BTC After NFP (2026-02-06): Historical T+1/T+7 Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -2.41, "sample_size": 0}, {"slug": "btc-after-nfp-2026-01-02", "title": "BTC After NFP (2026-01-02): Historical T+1/T+7 Probability", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.63, "sample_size": 0}]
chartData: [{"time": "2026-01-06", "open": 93876.95, "high": 94395.3, "low": 91286.55, "close": 93729.03}, {"time": "2026-01-07", "open": 93727.47, "high": 93738.79, "low": 90601.8, "close": 91308.05}, {"time": "2026-01-08", "open": 91309.64, "high": 91485.85, "low": 89233.88, "close": 91027.12}, {"time": "2026-01-09", "open": 91026.27, "high": 91910.67, "low": 89625.38, "close": 90513.1}, {"time": "2026-01-10", "open": 90510.1, "high": 90713.03, "low": 90283.4, "close": 90386.65}, {"time": "2026-01-11", "open": 90385.36, "high": 91155.23, "low": 90212.02, "close": 90827.46}, {"time": "2026-01-12", "open": 90825.86, "high": 92395.52, "low": 90055.02, "close": 91192.99}, {"time": "2026-01-13", "open": 91185.34, "high": 96011.62, "low": 90941.93, "close": 95321.78}, {"time": "2026-01-14", "open": 95322.91, "high": 97860.6, "low": 94583.05, "close": 96929.33}, {"time": "2026-01-15", "open": 96931.29, "high": 97150.17, "low": 95103.24, "close": 95551.19}, {"time": "2026-01-16", "open": 95554.1, "high": 95801.89, "low": 94259.27, "close": 95525.12}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2026-01-09**
- As-of date (T-1): **2026-03-03**
- Freshness age: **53 days**
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
