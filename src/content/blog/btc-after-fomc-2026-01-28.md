---
title: "Historical Performance of BTC After FOMC (2026-01-28)"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2026-01-28"
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
quality_score: 90
sample_size: 23
freshness_days: 34
freshness_status: "fresh"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "flat"
event_actual: 3.75
event_previous: 3.75
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.4
  mdd_t7: -18.13
  volatility: 12.94
  impact_t1_pct: -5.18
  impact_t7_pct: -18.13
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
    direction: "flat"
    sample_size: 17
    t1:
      up: 47.06
      down: 52.94
      median: -0.19
      mean: -0.15
      sample: 17
    t7:
      up: 47.06
      down: 52.94
      median: -2.38
      mean: -0.94
      sample: 17
related_events: [{"slug": "btc-after-fomc-2024-04-30", "title": "BTC After FOMC (2024-04-30): Historical T+1/T+7 Probability", "event_date": "2024-04-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 5.37, "median_t7_pct": 2.8, "sample_size": 0}, {"slug": "btc-after-fomc-2024-01-30", "title": "BTC After FOMC (2024-01-30): Historical T+1/T+7 Probability", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.97, "median_t7_pct": 0.31, "sample_size": 0}, {"slug": "btc-after-fomc-2025-12-11", "title": "BTC After FOMC (2025-12-11): Historical T+1/T+7 Probability", "event_date": "2025-12-11", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -7.62, "sample_size": 0}]
chartData: [{"time": "2026-01-25", "open": 89104.77, "high": 89193.15, "low": 86003.71, "close": 86572.22}, {"time": "2026-01-26", "open": 86566.52, "high": 88743.07, "low": 86429.29, "close": 88267.14}, {"time": "2026-01-27", "open": 88257.48, "high": 89427.12, "low": 87228.92, "close": 89102.57}, {"time": "2026-01-28", "open": 89104.05, "high": 90439.29, "low": 88721.46, "close": 89184.57}, {"time": "2026-01-29", "open": 89169.85, "high": 89200.78, "low": 83250.6, "close": 84561.59}, {"time": "2026-01-30", "open": 84562.73, "high": 84602.16, "low": 81071.48, "close": 84128.66}, {"time": "2026-01-31", "open": 84126.5, "high": 84136.92, "low": 75815.88, "close": 78621.12}, {"time": "2026-02-01", "open": 78626.12, "high": 79322.61, "low": 75698.9, "close": 76974.45}, {"time": "2026-02-02", "open": 76968.88, "high": 79258.61, "low": 74551.34, "close": 78688.77}, {"time": "2026-02-03", "open": 78693.51, "high": 79118.85, "low": 72897.14, "close": 75633.55}, {"time": "2026-02-04", "open": 75640.09, "high": 76864.66, "low": 71779.93, "close": 73019.7}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2026-01-28**
- As-of date (T-1): **2026-03-03**
- Freshness age: **34 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 3.75, Previous 3.75, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 52.17% | 47.83% | 0.27% | -0.18% | 23 |
| T+7 | 43.48% | 56.52% | -2.38% | -0.7% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 47.06% | 52.94% | -0.19% | -0.15% | 17 |
| T+7 | 47.06% | 52.94% | -2.38% | -0.94% | 17 |

## Historical Distribution Summary

When FOMC was **FLAT**, BTC T+1 up probability was **47.06%** (n=17).

When FOMC was **FLAT**, BTC T+7 up probability was **47.06%** (n=17).

Same-direction T+7 median return: **-2.38%**.

For BTC, historical FOMC windows show all-history T+1 up probability of 52.17% and T+7 up probability of 43.48%. When FOMC printed Flat versus previous, T+1 up probability was 47.06% and T+7 up probability was 47.06% across 17 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
