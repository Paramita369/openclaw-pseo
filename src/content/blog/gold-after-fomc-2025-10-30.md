---
title: "Historical Performance of GOLD After FOMC (2025-10-30)"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-10-30"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 11.13
robust_score: 5.13
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 23
freshness_days: 124
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 4.0
event_previous: 4.25
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -8.91
  mdd_t7: -0.53
  volatility: 0.06
  impact_t1_pct: -0.48
  impact_t7_pct: -0.53
probabilities:
  sample_size: 23
  t1:
    up: 69.57
    down: 30.43
    median: 0.34
    mean: 0.24
    sample: 23
  t7:
    up: 56.52
    down: 43.48
    median: 0.9
    mean: 0.05
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 6
    t1:
      up: 66.67
      down: 33.33
      median: 0.55
      mean: 0.07
      sample: 6
    t7:
      up: 66.67
      down: 33.33
      median: 1.53
      mean: 0.62
      sample: 6
related_events: [{"slug": "gold-after-fomc-2024-01-30", "title": "GOLD After FOMC (2024-01-30): Historical T+1/T+7 Probability", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 1.61, "median_t7_pct": 0.15, "sample_size": 0}, {"slug": "gold-after-fomc-2026-01-28", "title": "GOLD After FOMC (2026-01-28): Historical T+1/T+7 Probability", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -7.19, "sample_size": 0}, {"slug": "gold-after-fomc-2025-12-11", "title": "GOLD After FOMC (2025-12-11): Historical T+1/T+7 Probability", "event_date": "2025-12-11", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.26, "sample_size": 0}]
chartData: [{"time": "2025-10-27", "open": 4060.0, "high": 4078.6, "low": 3971.3, "close": 4001.9}, {"time": "2025-10-28", "open": 3929.7, "high": 3966.2, "low": 3923.6, "close": 3966.2}, {"time": "2025-10-29", "open": 3983.7, "high": 3983.7, "low": 3983.7, "close": 3983.7}, {"time": "2025-10-30", "open": 3960.0, "high": 4027.2, "low": 3913.7, "close": 4001.3}, {"time": "2025-10-31", "open": 4034.5, "high": 4034.5, "low": 3976.6, "close": 3982.2}, {"time": "2025-11-03", "open": 3976.2, "high": 4020.0, "low": 3959.0, "close": 4000.3}, {"time": "2025-11-04", "open": 3994.2, "high": 3995.4, "low": 3927.4, "close": 3947.7}, {"time": "2025-11-05", "open": 3929.9, "high": 3983.5, "low": 3929.9, "close": 3980.3}, {"time": "2025-11-06", "open": 4004.0, "high": 4007.5, "low": 3979.9, "close": 3979.9}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2025-10-30**
- As-of date (T-1): **2026-03-03**
- Freshness age: **124 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 4.0, Previous 4.25, Delta -0.2500)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 69.57% | 30.43% | 0.34% | 0.24% | 23 |
| T+7 | 56.52% | 43.48% | 0.9% | 0.05% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 66.67% | 33.33% | 0.55% | 0.07% | 6 |
| T+7 | 66.67% | 33.33% | 1.53% | 0.62% | 6 |

## Historical Distribution Summary

When FOMC was **DOWN**, GOLD T+1 up probability was **66.67%** (n=6).

When FOMC was **DOWN**, GOLD T+7 up probability was **66.67%** (n=6).

Same-direction T+7 median return: **1.53%**.

For GOLD, historical FOMC windows show all-history T+1 up probability of 69.57% and T+7 up probability of 56.52%. When FOMC printed Down versus previous, T+1 up probability was 66.67% and T+7 up probability was 66.67% across 6 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
