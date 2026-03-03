---
title: "Historical Performance of QQQ After CPI (2025-06-12)"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-06-12"
asof_date: "2026-03-02"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 6.07
robust_score: 0.07
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 70
sample_size: 14
freshness_days: 263
freshness_status: "stale"
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 321.435
event_previous: 320.62
event_delta: 0.815
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 2.08
  mdd_t7: 0.0
  volatility: 0.26
  impact_t1_pct: 0.28
  impact_t7_pct: 0.54
probabilities:
  sample_size: 14
  t1:
    up: 57.14
    down: 42.86
    median: 0.35
    mean: 0.28
    sample: 14
  t7:
    up: 53.85
    down: 46.15
    median: 0.6
    mean: 0.54
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 53.85
      down: 46.15
      median: 0.16
      mean: 0.26
      sample: 13
    t7:
      up: 53.85
      down: 46.15
      median: 0.6
      mean: 0.54
      sample: 13
related_events: [{"slug": "qqq-after-cpi-2024-05-15", "title": "QQQ After CPI (2024-05-15): Historical T+1/T+7 Probability", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.6, "median_t7_pct": 0.62, "sample_size": 0}, {"slug": "qqq-after-cpi-2024-09-11", "title": "QQQ After CPI (2024-09-11): Historical T+1/T+7 Probability", "event_date": "2024-09-11", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 7.08, "median_t7_pct": 0.6, "sample_size": 0}, {"slug": "qqq-after-cpi-2026-02-12", "title": "QQQ After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.0, "sample_size": 0}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2025-06-12**
- As-of date (T-1): **2026-03-02**
- Freshness age: **263 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 321.435, Previous 320.62, Delta +0.8150)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 57.14% | 42.86% | 0.35% | 0.28% | 14 |
| T+7 | 53.85% | 46.15% | 0.6% | 0.54% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.16% | 0.26% | 13 |
| T+7 | 53.85% | 46.15% | 0.6% | 0.54% | 13 |

## Historical Distribution Summary

When CPI was **UP**, QQQ T+1 up probability was **53.85%** (n=13).

When CPI was **UP**, QQQ T+7 up probability was **53.85%** (n=13).

Same-direction T+7 median return: **0.6%**.

For QQQ, historical CPI windows show all-history T+1 up probability of 57.14% and T+7 up probability of 53.85%. When CPI printed Up versus previous, T+1 up probability was 53.85% and T+7 up probability was 53.85% across 13 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
