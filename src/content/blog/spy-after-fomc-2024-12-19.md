---
title: "Historical Performance of SPY After FOMC (2024-12-19)"
description: "Historical probability profile for SPY around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-12-19"
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
freshness_days: 439
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 4.5
event_previous: 4.75
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 1.69
  mdd_t7: 0.0
  volatility: 1.74
  impact_t1_pct: 1.2
  impact_t7_pct: 2.95
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
chartData: [{"time": "2024-12-16", "open": 596.96, "high": 598.71, "low": 596.18, "close": 597.74}, {"time": "2024-12-17", "open": 595.17, "high": 596.14, "low": 593.89, "close": 595.27}, {"time": "2024-12-18", "open": 594.97, "high": 597.36, "low": 577.15, "close": 577.53}, {"time": "2024-12-19", "open": 582.54, "high": 584.15, "low": 577.11, "close": 577.35}, {"time": "2024-12-20", "open": 575.02, "high": 588.84, "low": 574.17, "close": 584.29}, {"time": "2024-12-23", "open": 584.03, "high": 588.39, "low": 580.84, "close": 587.79}, {"time": "2024-12-24", "open": 589.14, "high": 594.36, "low": 588.56, "close": 594.32}, {"time": "2024-12-26", "open": 592.54, "high": 595.49, "low": 591.14, "close": 594.36}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **SPY**
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
