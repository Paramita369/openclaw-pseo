---
title: "Historical Performance of QQQ After FOMC (2025-10-30)"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-10-30"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 3.3
robust_score: -2.7
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
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -0.83
  mdd_t7: -2.3
  volatility: 2.78
  impact_t1_pct: 0.48
  impact_t7_pct: -2.3
probabilities:
  sample_size: 23
  t1:
    up: 43.48
    down: 56.52
    median: -0.19
    mean: -0.05
    sample: 23
  t7:
    up: 56.52
    down: 43.48
    median: 0.88
    mean: 0.27
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 6
    t1:
      up: 50.0
      down: 50.0
      median: 0.21
      mean: -0.02
      sample: 6
    t7:
      up: 33.33
      down: 66.67
      median: -1.24
      mean: -0.66
      sample: 6
related_events: [{"slug": "qqq-after-fomc-2024-01-30", "title": "QQQ After FOMC (2024-01-30): Historical T+1/T+7 Probability", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.07, "median_t7_pct": 0.54, "sample_size": 0}, {"slug": "qqq-after-fomc-2026-01-28", "title": "QQQ After FOMC (2026-01-28): Historical T+1/T+7 Probability", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -4.34, "sample_size": 0}, {"slug": "qqq-after-fomc-2025-12-11", "title": "QQQ After FOMC (2025-12-11): Historical T+1/T+7 Probability", "event_date": "2025-12-11", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -2.63, "sample_size": 0}]
chartData: [{"time": "2025-10-27", "open": 623.72, "high": 627.74, "low": 623.23, "close": 627.28}, {"time": "2025-10-28", "open": 629.55, "high": 633.86, "low": 628.44, "close": 632.11}, {"time": "2025-10-29", "open": 634.77, "high": 636.19, "low": 629.44, "close": 634.95}, {"time": "2025-10-30", "open": 631.36, "high": 632.68, "low": 625.13, "close": 625.24}, {"time": "2025-10-31", "open": 633.35, "high": 633.38, "low": 625.88, "close": 628.26}, {"time": "2025-11-03", "open": 634.29, "high": 635.0, "low": 629.04, "close": 631.27}, {"time": "2025-11-04", "open": 622.48, "high": 626.14, "low": 617.66, "close": 618.45}, {"time": "2025-11-05", "open": 617.69, "high": 625.79, "low": 616.42, "close": 622.48}, {"time": "2025-11-06", "open": 620.99, "high": 621.24, "low": 609.51, "close": 610.88}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
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
| T+1 | 43.48% | 56.52% | -0.19% | -0.05% | 23 |
| T+7 | 56.52% | 43.48% | 0.88% | 0.27% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.21% | -0.02% | 6 |
| T+7 | 33.33% | 66.67% | -1.24% | -0.66% | 6 |

## Historical Distribution Summary

When FOMC was **DOWN**, QQQ T+1 up probability was **50.0%** (n=6).

When FOMC was **DOWN**, QQQ T+7 up probability was **33.33%** (n=6).

Same-direction T+7 median return: **-1.24%**.

For QQQ, historical FOMC windows show all-history T+1 up probability of 43.48% and T+7 up probability of 56.52%. When FOMC printed Down versus previous, T+1 up probability was 50.0% and T+7 up probability was 33.33% across 6 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
