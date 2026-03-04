---
title: "Historical Performance of BTC After NFP (2025-01-10)"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-01-10"
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
quality_score: 60
sample_size: 34
freshness_days: 417
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 158268.0
event_previous: 158316.0
event_delta: -48.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.99
  mdd_t7: -0.14
  volatility: 10.45
  impact_t1_pct: -0.14
  impact_t7_pct: 10.31
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
    direction: "down"
    sample_size: 4
    t1:
      up: 50.0
      down: 50.0
      median: -0.01
      mean: 0.12
      sample: 4
    t7:
      up: 75.0
      down: 25.0
      median: 2.3
      mean: 1.88
      sample: 4
related_events: [{"slug": "btc-after-nfp-2026-02-11", "title": "BTC After NFP (2026-02-11): Historical T+1/T+7 Probability", "event_date": "2026-02-11", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.85, "sample_size": 0}, {"slug": "btc-after-nfp-2026-02-06", "title": "BTC After NFP (2026-02-06): Historical T+1/T+7 Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -2.41, "sample_size": 0}, {"slug": "btc-after-nfp-2026-01-09", "title": "BTC After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 5.54, "sample_size": 0}]
chartData: [{"time": "2025-01-07", "open": 102248.85, "high": 102712.48, "low": 96132.88, "close": 96922.7}, {"time": "2025-01-08", "open": 96924.16, "high": 97258.32, "low": 92525.84, "close": 95043.52}, {"time": "2025-01-09", "open": 95043.48, "high": 95349.72, "low": 91220.84, "close": 92484.04}, {"time": "2025-01-10", "open": 92494.49, "high": 95770.61, "low": 92250.09, "close": 94701.45}, {"time": "2025-01-11", "open": 94700.84, "high": 94977.69, "low": 93840.05, "close": 94566.59}, {"time": "2025-01-12", "open": 94565.73, "high": 95367.54, "low": 93712.51, "close": 94488.44}, {"time": "2025-01-13", "open": 94488.89, "high": 95837.0, "low": 89260.1, "close": 94516.52}, {"time": "2025-01-14", "open": 94519.01, "high": 97352.66, "low": 94322.16, "close": 96534.05}, {"time": "2025-01-15", "open": 96534.05, "high": 100697.23, "low": 96501.64, "close": 100504.49}, {"time": "2025-01-16", "open": 100505.3, "high": 100781.59, "low": 97364.45, "close": 99756.91}, {"time": "2025-01-17", "open": 100025.77, "high": 105884.23, "low": 99948.91, "close": 104462.04}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-01-10**
- As-of date (T-1): **2026-03-03**
- Freshness age: **417 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158268.0, Previous 158316.0, Delta -48.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 29.41% | 70.59% | -0.33% | -0.26% | 34 |
| T+7 | 58.82% | 41.18% | 1.0% | 1.55% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.01% | 0.12% | 4 |
| T+7 | 75.0% | 25.0% | 2.3% | 1.88% | 4 |

## Historical Distribution Summary

When NFP was **DOWN**, BTC T+1 up probability was **50.0%** (n=4).

When NFP was **DOWN**, BTC T+7 up probability was **75.0%** (n=4).

Same-direction T+7 median return: **2.3%**.

For BTC, historical NFP windows show all-history T+1 up probability of 29.41% and T+7 up probability of 58.82%. When NFP printed Down versus previous, T+1 up probability was 50.0% and T+7 up probability was 75.0% across 4 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
