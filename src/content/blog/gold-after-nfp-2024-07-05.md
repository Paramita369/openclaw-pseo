---
title: "GOLD After NFP (2024-07-05): Historical T+1/T+7 Probability"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-07-05"
asof_date: "2026-03-02"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 4.31
robust_score: -1.69
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 50
sample_size: 13
freshness_days: 605
freshness_status: "stale"
data_last_updated_at: "2026-03-03T09:55:20+00:00"
event_direction: "up"
event_actual: 157748.0
event_previous: 157695.0
event_delta: 53.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.0
  mdd_t7: 0.0
  volatility: 1.07
  impact_t1_pct: 0.0
  impact_t7_pct: 1.07
probabilities:
  sample_size: 13
  t1:
    up: 0.0
    down: 100.0
    median: 0.0
    mean: 0.0
    sample: 0
  t7:
    up: 84.62
    down: 15.38
    median: 1.07
    mean: 1.14
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 0
    t1:
      up: 0.0
      down: 100.0
      median: 0.0
      mean: 0.0
      sample: 0
    t7:
      up: 83.33
      down: 16.67
      median: 0.86
      mean: 1.12
      sample: 12
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
- Event date: **2024-07-05**
- As-of date (T-1): **2026-03-02**
- Freshness age: **605 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 157748.0, Previous 157695.0, Delta +53.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 84.62% | 15.38% | 1.07% | 1.14% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 83.33% | 16.67% | 0.86% | 1.12% | 12 |

## Historical Distribution Summary

When NFP was **UP**, GOLD T+1 up probability was **0.0%** (n=0).

When NFP was **UP**, GOLD T+7 up probability was **83.33%** (n=12).

Same-direction T+7 median return: **0.86%**.

For GOLD, historical NFP windows show all-history T+1 up probability of 0.0% and T+7 up probability of 84.62%. When NFP printed Up versus previous, T+1 up probability was 0.0% and T+7 up probability was 83.33% across 0 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
