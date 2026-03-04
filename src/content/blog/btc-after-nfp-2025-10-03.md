---
title: "Historical Performance of BTC After NFP (2025-10-03)"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-10-03"
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
freshness_days: 151
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 158408.0
event_previous: 158548.0
event_delta: -140.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -0.98
  mdd_t7: -7.4
  volatility: 7.53
  impact_t1_pct: 0.13
  impact_t7_pct: -7.4
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
chartData: [{"time": "2025-09-30", "open": 114396.52, "high": 114836.62, "low": 112740.56, "close": 114056.09}, {"time": "2025-10-01", "open": 114057.59, "high": 118648.93, "low": 113981.4, "close": 118648.93}, {"time": "2025-10-02", "open": 118652.38, "high": 121086.41, "low": 118383.16, "close": 120681.26}, {"time": "2025-10-03", "open": 120656.98, "high": 123944.7, "low": 119344.31, "close": 122266.53}, {"time": "2025-10-04", "open": 122267.47, "high": 122857.64, "low": 121577.57, "close": 122425.43}, {"time": "2025-10-05", "open": 122419.67, "high": 125559.21, "low": 122191.96, "close": 123513.48}, {"time": "2025-10-06", "open": 123510.45, "high": 126198.07, "low": 123196.05, "close": 124752.53}, {"time": "2025-10-07", "open": 124752.14, "high": 125184.02, "low": 120681.97, "close": 121451.38}, {"time": "2025-10-08", "open": 121448.35, "high": 124167.09, "low": 121119.18, "close": 123354.87}, {"time": "2025-10-09", "open": 123337.07, "high": 123739.34, "low": 119812.03, "close": 121705.59}, {"time": "2025-10-10", "open": 121704.74, "high": 122509.66, "low": 104582.41, "close": 113214.37}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-10-03**
- As-of date (T-1): **2026-03-03**
- Freshness age: **151 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158408.0, Previous 158548.0, Delta -140.0000)
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
