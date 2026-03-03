---
title: "GOLD After FOMC (2024-09-17): Historical T+1/T+7 Probability"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-09-17"
asof_date: "2026-03-02"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
confidence_level: "normal"
quality_score: 80
sample_size: 9
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 1.08
  mdd_t7: 0.0
  volatility: 3.14
  impact_t1_pct: 0.25
  impact_t7_pct: 3.39
probabilities:
  sample_size: 9
  t1:
    up: 88.89
    down: 11.11
    median: 0.83
    mean: 0.72
    sample: 9
  t7:
    up: 66.67
    down: 33.33
    median: 0.9
    mean: 0.59
    sample: 9
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 9
    t1:
      up: 88.89
      down: 11.11
      median: 0.83
      mean: 0.72
      sample: 9
    t7:
      up: 66.67
      down: 33.33
      median: 0.9
      mean: 0.59
      sample: 9
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2024-09-17**
- As-of date (T-1): **2026-03-02**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.5, Previous 5.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 88.89% | 11.11% | 0.83% | 0.72% | 9 |
| T+7 | 66.67% | 33.33% | 0.9% | 0.59% | 9 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 88.89% | 11.11% | 0.83% | 0.72% | 9 |
| T+7 | 66.67% | 33.33% | 0.9% | 0.59% | 9 |

## Historical Distribution Summary

When FOMC was **FLAT**, GOLD T+1 up probability was **88.89%** (n=9).

When FOMC was **FLAT**, GOLD T+7 up probability was **66.67%** (n=9).

Same-direction T+7 median return: **0.9%**.

For GOLD, historical FOMC windows show all-history T+1 up probability of 88.89% and T+7 up probability of 66.67%. When FOMC printed Flat versus previous, T+1 up probability was 88.89% and T+7 up probability was 66.67% across 9 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
