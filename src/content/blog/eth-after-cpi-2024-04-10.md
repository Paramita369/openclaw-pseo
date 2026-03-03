---
title: "Historical Performance of ETH After CPI (2024-04-10)"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-04-10"
asof_date: "2026-03-02"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -5.57
robust_score: -11.57
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 14
freshness_days: 691
freshness_status: "stale"
data_last_updated_at: "2026-03-03T14:52:49+00:00"
event_direction: "up"
event_actual: 313.023
event_previous: 312.345
event_delta: 0.678
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -1.07
  mdd_t7: -15.77
  volatility: 14.68
  impact_t1_pct: -1.09
  impact_t7_pct: -15.77
probabilities:
  sample_size: 14
  t1:
    up: 50.0
    down: 50.0
    median: -0.22
    mean: -0.52
    sample: 14
  t7:
    up: 42.86
    down: 57.14
    median: -0.39
    mean: 0.26
    sample: 14
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 53.85
      down: 46.15
      median: 0.66
      mean: -0.36
      sample: 13
    t7:
      up: 46.15
      down: 53.85
      median: -0.77
      mean: 0.28
      sample: 13
related_events: [{"slug": "eth-after-cpi-2024-06-12", "title": "ETH After CPI (2024-06-12): Historical T+1/T+7 Probability", "event_date": "2024-06-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.22, "median_t7_pct": -0.01, "sample_size": 0}, {"slug": "eth-after-cpi-2026-02-12", "title": "ETH After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.0, "sample_size": 0}, {"slug": "eth-after-cpi-2026-01-12", "title": "ETH After CPI (2026-01-12): Historical T+1/T+7 Probability", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.0, "sample_size": 0}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-04-10**
- As-of date (T-1): **2026-03-02**
- Freshness age: **691 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 313.023, Previous 312.345, Delta +0.6780)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.22% | -0.52% | 14 |
| T+7 | 42.86% | 57.14% | -0.39% | 0.26% | 14 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.66% | -0.36% | 13 |
| T+7 | 46.15% | 53.85% | -0.77% | 0.28% | 13 |

## Historical Distribution Summary

When CPI was **UP**, ETH T+1 up probability was **53.85%** (n=13).

When CPI was **UP**, ETH T+7 up probability was **46.15%** (n=13).

Same-direction T+7 median return: **-0.77%**.

For ETH, historical CPI windows show all-history T+1 up probability of 50.0% and T+7 up probability of 42.86%. When CPI printed Up versus previous, T+1 up probability was 53.85% and T+7 up probability was 46.15% across 13 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
