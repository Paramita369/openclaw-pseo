---
title: "GOLD After CPI (2024-06-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for GOLD around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-06-12"
asof_date: "2026-03-02"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
confidence_level: "normal"
quality_score: 50
sample_size: 14
event_direction: "down"
event_actual: 313.044
event_previous: 313.175
event_delta: -0.131
direction_basis: "vs_previous"
tags: ["gold", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.41
  mdd_t7: -1.53
  volatility: 2.6
  impact_t1_pct: -1.53
  impact_t7_pct: 1.07
probabilities:
  sample_size: 14
  t1:
    up: 50.0
    down: 50.0
    median: 0.27
    mean: 0.22
    sample: 14
  t7:
    up: 76.92
    down: 23.08
    median: 1.52
    mean: 1.07
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 0
    t1:
      up: 0.0
      down: 100.0
      median: -1.53
      mean: -1.53
      sample: 1
    t7:
      up: 0.0
      down: 100.0
      median: 0.0
      mean: 0.0
      sample: 0
---

## Event Snapshot

- Event: **CPI**
- Asset: **GOLD**
- Event date: **2024-06-12**
- As-of date (T-1): **2026-03-02**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **DOWN** (Actual 313.044, Previous 313.175, Delta -0.1310)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.27% | 0.22% | 14 |
| T+7 | 76.92% | 23.08% | 1.52% | 1.07% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | -1.53% | -1.53% | 1 |
| T+7 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |

## Historical Distribution Summary

When CPI was **DOWN**, GOLD T+1 up probability was **0.0%** (n=1).

When CPI was **DOWN**, GOLD T+7 up probability was **0.0%** (n=0).

Same-direction T+7 median return: **0.0%**.

For GOLD, historical CPI windows show all-history T+1 up probability of 50.0% and T+7 up probability of 76.92%. When CPI printed Down versus previous, T+1 up probability was 0.0% and T+7 up probability was 0.0% across 0 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
