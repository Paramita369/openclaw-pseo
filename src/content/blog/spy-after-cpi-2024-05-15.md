---
title: "Historical Performance of SPY After CPI (2024-05-15)"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-05-15"
asof_date: "2026-03-02"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 19.75
robust_score: 13.75
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 14
freshness_days: 656
freshness_status: "stale"
data_last_updated_at: "2026-03-03T14:52:49+00:00"
event_direction: "up"
event_actual: 313.175
event_previous: 313.023
event_delta: 0.152
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.37
  mdd_t7: -0.21
  volatility: 0.22
  impact_t1_pct: -0.21
  impact_t7_pct: 0.01
probabilities:
  sample_size: 14
  t1:
    up: 64.29
    down: 35.71
    median: 0.15
    mean: 0.26
    sample: 14
  t7:
    up: 76.92
    down: 23.08
    median: 1.08
    mean: 0.51
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 61.54
      down: 38.46
      median: 0.09
      mean: 0.26
      sample: 13
    t7:
      up: 76.92
      down: 23.08
      median: 1.08
      mean: 0.51
      sample: 13
related_events: [{"slug": "spy-after-cpi-2024-03-12", "title": "SPY After CPI (2024-03-12): Historical T+1/T+7 Probability", "event_date": "2024-03-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 3.94, "median_t7_pct": 0.1, "sample_size": 0}, {"slug": "spy-after-cpi-2024-11-14", "title": "SPY After CPI (2024-11-14): Historical T+1/T+7 Probability", "event_date": "2024-11-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.43, "median_t7_pct": 0.05, "sample_size": 0}, {"slug": "spy-after-cpi-2026-02-12", "title": "SPY After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.0, "sample_size": 0}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2024-05-15**
- As-of date (T-1): **2026-03-02**
- Freshness age: **656 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 313.175, Previous 313.023, Delta +0.1520)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 64.29% | 35.71% | 0.15% | 0.26% | 14 |
| T+7 | 76.92% | 23.08% | 1.08% | 0.51% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 61.54% | 38.46% | 0.09% | 0.26% | 13 |
| T+7 | 76.92% | 23.08% | 1.08% | 0.51% | 13 |

## Historical Distribution Summary

When CPI was **UP**, SPY T+1 up probability was **61.54%** (n=13).

When CPI was **UP**, SPY T+7 up probability was **76.92%** (n=13).

Same-direction T+7 median return: **1.08%**.

For SPY, historical CPI windows show all-history T+1 up probability of 64.29% and T+7 up probability of 76.92%. When CPI printed Up versus previous, T+1 up probability was 61.54% and T+7 up probability was 76.92% across 13 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
