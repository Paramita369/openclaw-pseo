---
title: "Historical Performance of GOLD After FOMC (2024-12-19)"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-12-19"
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
freshness_days: 439
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 4.5
event_previous: 4.75
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 4.61
  mdd_t7: 0.0
  volatility: 0.39
  impact_t1_pct: 1.41
  impact_t7_pct: 1.8
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
chartData: [{"time": "2024-12-16", "open": 2658.3, "high": 2663.3, "low": 2651.0, "close": 2651.4}, {"time": "2024-12-17", "open": 2651.8, "high": 2652.3, "low": 2632.5, "close": 2644.4}, {"time": "2024-12-18", "open": 2644.3, "high": 2647.1, "low": 2590.2, "close": 2636.5}, {"time": "2024-12-19", "open": 2582.1, "high": 2610.3, "low": 2582.1, "close": 2592.2}, {"time": "2024-12-20", "open": 2605.3, "high": 2631.6, "low": 2604.9, "close": 2628.7}, {"time": "2024-12-23", "open": 2620.0, "high": 2627.7, "low": 2611.1, "close": 2612.3}, {"time": "2024-12-24", "open": 2613.0, "high": 2620.0, "low": 2609.5, "close": 2620.0}, {"time": "2024-12-26", "open": 2628.5, "high": 2638.8, "low": 2627.9, "close": 2638.8}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2024-12-19**
- As-of date (T-1): **2026-03-03**
- Freshness age: **439 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 4.5, Previous 4.75, Delta -0.2500)
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
