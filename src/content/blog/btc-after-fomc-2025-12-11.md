---
title: "Historical Performance of BTC After FOMC (2025-12-11)"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-12-11"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -4.61
robust_score: -4.61
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 23
freshness_days: 82
freshness_status: "fresh"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 3.75
event_previous: 4.0
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.47
  mdd_t7: -7.62
  volatility: 5.2
  impact_t1_pct: -2.42
  impact_t7_pct: -7.62
probabilities:
  sample_size: 23
  t1:
    up: 52.17
    down: 47.83
    median: 0.27
    mean: -0.18
    sample: 23
  t7:
    up: 43.48
    down: 56.52
    median: -2.38
    mean: -0.7
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 6
    t1:
      up: 66.67
      down: 33.33
      median: 0.29
      mean: -0.25
      sample: 6
    t7:
      up: 33.33
      down: 66.67
      median: -4.1
      mean: -0.03
      sample: 6
related_events: [{"slug": "btc-after-fomc-2024-04-30", "title": "BTC After FOMC (2024-04-30): Historical T+1/T+7 Probability", "event_date": "2024-04-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 5.37, "median_t7_pct": 2.8, "sample_size": 0}, {"slug": "btc-after-fomc-2024-01-30", "title": "BTC After FOMC (2024-01-30): Historical T+1/T+7 Probability", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.97, "median_t7_pct": 0.31, "sample_size": 0}, {"slug": "btc-after-fomc-2026-01-28", "title": "BTC After FOMC (2026-01-28): Historical T+1/T+7 Probability", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -18.13, "sample_size": 0}]
chartData: [{"time": "2025-12-08", "open": 90424.59, "high": 92267.12, "low": 89644.89, "close": 90640.2}, {"time": "2025-12-09", "open": 90639.7, "high": 94601.57, "low": 89586.98, "close": 92691.71}, {"time": "2025-12-10", "open": 92695.23, "high": 94477.16, "low": 91640.13, "close": 92020.95}, {"time": "2025-12-11", "open": 92011.3, "high": 93554.27, "low": 89335.3, "close": 92511.34}, {"time": "2025-12-12", "open": 92513.66, "high": 92747.93, "low": 89532.6, "close": 90270.41}, {"time": "2025-12-13", "open": 90257.8, "high": 90647.57, "low": 89800.99, "close": 90298.71}, {"time": "2025-12-14", "open": 90296.44, "high": 90498.11, "low": 87634.94, "close": 88175.18}, {"time": "2025-12-15", "open": 88171.08, "high": 89983.92, "low": 85304.08, "close": 86419.78}, {"time": "2025-12-16", "open": 86424.41, "high": 88170.09, "low": 85381.69, "close": 87843.98}, {"time": "2025-12-17", "open": 87847.62, "high": 90264.57, "low": 85316.27, "close": 86143.76}, {"time": "2025-12-18", "open": 86144.37, "high": 89412.66, "low": 84436.31, "close": 85462.51}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2025-12-11**
- As-of date (T-1): **2026-03-03**
- Freshness age: **82 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 3.75, Previous 4.0, Delta -0.2500)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 52.17% | 47.83% | 0.27% | -0.18% | 23 |
| T+7 | 43.48% | 56.52% | -2.38% | -0.7% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 66.67% | 33.33% | 0.29% | -0.25% | 6 |
| T+7 | 33.33% | 66.67% | -4.1% | -0.03% | 6 |

## Historical Distribution Summary

When FOMC was **DOWN**, BTC T+1 up probability was **66.67%** (n=6).

When FOMC was **DOWN**, BTC T+7 up probability was **33.33%** (n=6).

Same-direction T+7 median return: **-4.1%**.

For BTC, historical FOMC windows show all-history T+1 up probability of 52.17% and T+7 up probability of 43.48%. When FOMC printed Down versus previous, T+1 up probability was 66.67% and T+7 up probability was 33.33% across 6 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
