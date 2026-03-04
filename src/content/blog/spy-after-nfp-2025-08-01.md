---
title: "Historical Performance of SPY After NFP (2025-08-01)"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-08-01"
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
quality_score: 60
sample_size: 34
freshness_days: 214
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 158472.0
event_previous: 158542.0
event_delta: -70.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 2.56
  mdd_t7: 0.0
  volatility: 0.97
  impact_t1_pct: 1.52
  impact_t7_pct: 2.49
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
    direction: "down"
    sample_size: 3
    t1:
      up: 100.0
      down: 0.0
      median: 0.36
      mean: 0.66
      sample: 3
    t7:
      up: 50.0
      down: 50.0
      median: 1.06
      mean: 0.66
      sample: 4
related_events: [{"slug": "spy-after-nfp-2024-07-05", "title": "SPY After NFP (2024-07-05): Historical T+1/T+7 Probability", "event_date": "2024-07-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.02, "median_t7_pct": 0.96, "sample_size": 0}, {"slug": "spy-after-nfp-2024-01-05", "title": "SPY After NFP (2024-01-05): Historical T+1/T+7 Probability", "event_date": "2024-01-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.04, "median_t7_pct": 1.87, "sample_size": 0}, {"slug": "spy-after-nfp-2024-10-04", "title": "SPY After NFP (2024-10-04): Historical T+1/T+7 Probability", "event_date": "2024-10-04", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.43, "median_t7_pct": 1.15, "sample_size": 0}]
chartData: [{"time": "2025-07-29", "open": 634.71, "high": 635.03, "low": 630.72, "close": 631.64}, {"time": "2025-07-30", "open": 632.29, "high": 634.04, "low": 627.94, "close": 630.84}, {"time": "2025-07-31", "open": 635.81, "high": 636.2, "low": 627.17, "close": 628.48}, {"time": "2025-08-01", "open": 622.73, "high": 622.77, "low": 615.76, "close": 618.17}, {"time": "2025-08-04", "open": 622.1, "high": 627.62, "low": 622.01, "close": 627.57}, {"time": "2025-08-05", "open": 628.19, "high": 629.0, "low": 623.46, "close": 624.39}, {"time": "2025-08-06", "open": 625.46, "high": 629.83, "low": 624.55, "close": 629.17}, {"time": "2025-08-07", "open": 632.61, "high": 633.35, "low": 625.52, "close": 628.64}, {"time": "2025-08-08", "open": 630.44, "high": 634.01, "low": 630.13, "close": 633.55}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2025-08-01**
- As-of date (T-1): **2026-03-03**
- Freshness age: **214 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158472.0, Previous 158542.0, Delta -70.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 47.62% | 52.38% | -0.04% | -0.1% | 21 |
| T+7 | 55.88% | 44.12% | 0.11% | 0.81% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 100.0% | 0.0% | 0.36% | 0.66% | 3 |
| T+7 | 50.0% | 50.0% | 1.06% | 0.66% | 4 |

## Historical Distribution Summary

When NFP was **DOWN**, SPY T+1 up probability was **100.0%** (n=3).

When NFP was **DOWN**, SPY T+7 up probability was **50.0%** (n=4).

Same-direction T+7 median return: **1.06%**.

For SPY, historical NFP windows show all-history T+1 up probability of 47.62% and T+7 up probability of 55.88%. When NFP printed Down versus previous, T+1 up probability was 100.0% and T+7 up probability was 50.0% across 3 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
