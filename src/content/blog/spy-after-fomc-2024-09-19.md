---
title: "Historical Performance of SPY After FOMC (2024-09-19)"
description: "Historical probability profile for SPY around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-09-19"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 5.91
robust_score: -0.09
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 23
freshness_days: 530
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 5.0
event_previous: 5.5
event_delta: -0.5
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 0.76
  mdd_t7: -0.17
  volatility: 0.71
  impact_t1_pct: -0.17
  impact_t7_pct: 0.54
probabilities:
  sample_size: 23
  t1:
    up: 52.17
    down: 47.83
    median: 0.1
    mean: -0.02
    sample: 23
  t7:
    up: 56.52
    down: 43.48
    median: 0.54
    mean: 0.26
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 6
    t1:
      up: 66.67
      down: 33.33
      median: 0.21
      mean: 0.15
      sample: 6
    t7:
      up: 33.33
      down: 66.67
      median: -0.88
      mean: -0.37
      sample: 6
related_events: [{"slug": "spy-after-fomc-2025-01-29", "title": "SPY After FOMC (2025-01-29): Historical T+1/T+7 Probability", "event_date": "2025-01-29", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 9.47, "median_t7_pct": 0.4, "sample_size": 0}, {"slug": "spy-after-fomc-2024-03-19", "title": "SPY After FOMC (2024-03-19): Historical T+1/T+7 Probability", "event_date": "2024-03-19", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 7.7, "median_t7_pct": 0.6, "sample_size": 0}, {"slug": "spy-after-fomc-2024-01-30", "title": "SPY After FOMC (2024-01-30): Historical T+1/T+7 Probability", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.69, "median_t7_pct": 0.63, "sample_size": 0}]
chartData: [{"time": "2024-09-16", "open": 551.67, "high": 553.01, "low": 549.86, "close": 552.75}, {"time": "2024-09-17", "open": 554.97, "high": 556.42, "low": 550.73, "close": 552.97}, {"time": "2024-09-18", "open": 553.63, "high": 558.49, "low": 550.77, "close": 551.33}, {"time": "2024-09-19", "open": 560.77, "high": 562.61, "low": 557.89, "close": 560.74}, {"time": "2024-09-20", "open": 559.37, "high": 560.81, "low": 556.74, "close": 559.77}, {"time": "2024-09-23", "open": 560.84, "high": 561.82, "low": 559.62, "close": 561.17}, {"time": "2024-09-24", "open": 561.97, "high": 562.83, "low": 559.13, "close": 562.77}, {"time": "2024-09-25", "open": 562.62, "high": 563.36, "low": 560.42, "close": 561.53}, {"time": "2024-09-26", "open": 565.81, "high": 566.13, "low": 561.4, "close": 563.76}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **SPY**
- Event date: **2024-09-19**
- As-of date (T-1): **2026-03-03**
- Freshness age: **530 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 5.0, Previous 5.5, Delta -0.5000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 52.17% | 47.83% | 0.1% | -0.02% | 23 |
| T+7 | 56.52% | 43.48% | 0.54% | 0.26% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 66.67% | 33.33% | 0.21% | 0.15% | 6 |
| T+7 | 33.33% | 66.67% | -0.88% | -0.37% | 6 |

## Historical Distribution Summary

When FOMC was **DOWN**, SPY T+1 up probability was **66.67%** (n=6).

When FOMC was **DOWN**, SPY T+7 up probability was **33.33%** (n=6).

Same-direction T+7 median return: **-0.88%**.

For SPY, historical FOMC windows show all-history T+1 up probability of 52.17% and T+7 up probability of 56.52%. When FOMC printed Down versus previous, T+1 up probability was 66.67% and T+7 up probability was 33.33% across 6 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
