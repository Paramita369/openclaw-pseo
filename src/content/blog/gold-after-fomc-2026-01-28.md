---
title: "Historical Performance of GOLD After FOMC (2026-01-28)"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2026-01-28"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 11.13
robust_score: 11.13
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
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -0.96
  mdd_t7: -7.19
  volatility: 7.51
  impact_t1_pct: 0.32
  impact_t7_pct: -7.19
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
    direction: "flat"
    sample_size: 17
    t1:
      up: 70.59
      down: 29.41
      median: 0.32
      mean: 0.31
      sample: 17
    t7:
      up: 52.94
      down: 47.06
      median: 0.15
      mean: -0.16
      sample: 17
related_events: [{"slug": "gold-after-fomc-2024-01-30", "title": "GOLD After FOMC (2024-01-30): Historical T+1/T+7 Probability", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 1.61, "median_t7_pct": 0.15, "sample_size": 0}, {"slug": "gold-after-fomc-2025-12-11", "title": "GOLD After FOMC (2025-12-11): Historical T+1/T+7 Probability", "event_date": "2025-12-11", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.26, "sample_size": 0}, {"slug": "gold-after-fomc-2025-12-10", "title": "GOLD After FOMC (2025-12-10): Historical T+1/T+7 Probability", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 3.6, "sample_size": 0}]
chartData: [{"time": "2026-01-26", "open": 5081.5, "high": 5095.6, "low": 5052.2, "close": 5079.7}, {"time": "2026-01-27", "open": 5079.9, "high": 5079.9, "low": 5079.9, "close": 5079.9}, {"time": "2026-01-28", "open": 5301.6, "high": 5301.6, "low": 5301.6, "close": 5301.6}, {"time": "2026-01-29", "open": 5415.7, "high": 5586.2, "low": 5097.5, "close": 5318.4}, {"time": "2026-01-30", "open": 5376.4, "high": 5440.5, "low": 4700.0, "close": 4713.9}, {"time": "2026-02-02", "open": 4807.7, "high": 4855.8, "low": 4400.0, "close": 4622.5}, {"time": "2026-02-03", "open": 4680.0, "high": 4984.6, "low": 4674.3, "close": 4903.7}, {"time": "2026-02-04", "open": 4923.3, "high": 5082.2, "low": 4897.9, "close": 4920.4}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
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
| T+1 | 69.57% | 30.43% | 0.34% | 0.24% | 23 |
| T+7 | 56.52% | 43.48% | 0.9% | 0.05% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 70.59% | 29.41% | 0.32% | 0.31% | 17 |
| T+7 | 52.94% | 47.06% | 0.15% | -0.16% | 17 |

## Historical Distribution Summary

When FOMC was **FLAT**, GOLD T+1 up probability was **70.59%** (n=17).

When FOMC was **FLAT**, GOLD T+7 up probability was **52.94%** (n=17).

Same-direction T+7 median return: **0.15%**.

For GOLD, historical FOMC windows show all-history T+1 up probability of 69.57% and T+7 up probability of 56.52%. When FOMC printed Flat versus previous, T+1 up probability was 70.59% and T+7 up probability was 52.94% across 17 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
