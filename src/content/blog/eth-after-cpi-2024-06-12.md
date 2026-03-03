---
title: "ETH After CPI (2024-06-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-06-12"
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
quality_score: 60
sample_size: 14
freshness_days: 628
freshness_status: "stale"
data_last_updated_at: "2026-03-03T09:55:20+00:00"
event_direction: "down"
event_actual: 313.044
event_previous: 313.175
event_delta: -0.131
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.22
  mdd_t7: -2.54
  volatility: 2.53
  impact_t1_pct: -2.54
  impact_t7_pct: -0.01
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
    direction: "down"
    sample_size: 1
    t1:
      up: 0.0
      down: 100.0
      median: -2.54
      mean: -2.54
      sample: 1
    t7:
      up: 0.0
      down: 100.0
      median: -0.01
      mean: -0.01
      sample: 1
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-06-12**
- As-of date (T-1): **2026-03-02**
- Freshness age: **628 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **DOWN** (Actual 313.044, Previous 313.175, Delta -0.1310)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.22% | -0.52% | 14 |
| T+7 | 42.86% | 57.14% | -0.39% | 0.26% | 14 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | -2.54% | -2.54% | 1 |
| T+7 | 0.0% | 100.0% | -0.01% | -0.01% | 1 |

## Historical Distribution Summary

When CPI was **DOWN**, ETH T+1 up probability was **0.0%** (n=1).

When CPI was **DOWN**, ETH T+7 up probability was **0.0%** (n=1).

Same-direction T+7 median return: **-0.01%**.

For ETH, historical CPI windows show all-history T+1 up probability of 50.0% and T+7 up probability of 42.86%. When CPI printed Down versus previous, T+1 up probability was 0.0% and T+7 up probability was 0.0% across 1 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
