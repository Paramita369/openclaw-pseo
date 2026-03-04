---
title: "Historical Performance of QQQ After FOMC (2024-12-19)"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-12-19"
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
freshness_days: 439
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 4.5
event_previous: 4.75
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 1.38
  mdd_t7: 0.0
  volatility: 2.29
  impact_t1_pct: 0.87
  impact_t7_pct: 3.17
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
chartData: [{"time": "2024-12-16", "open": 529.54, "high": 535.57, "low": 529.46, "close": 534.59}, {"time": "2024-12-17", "open": 532.79, "high": 533.91, "low": 530.58, "close": 532.24}, {"time": "2024-12-18", "open": 531.59, "high": 533.31, "low": 511.59, "close": 513.04}, {"time": "2024-12-19", "open": 517.73, "high": 518.29, "low": 510.41, "close": 510.75}, {"time": "2024-12-20", "open": 507.05, "high": 521.33, "low": 505.9, "close": 515.21}, {"time": "2024-12-23", "open": 516.93, "high": 520.61, "low": 513.53, "close": 520.23}, {"time": "2024-12-24", "open": 522.18, "high": 527.38, "low": 521.54, "close": 527.29}, {"time": "2024-12-26", "open": 525.65, "high": 528.56, "low": 523.65, "close": 526.93}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
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
