---
title: "BTC After NFP (2025-01-10): Historical T+1/T+7 Probability"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-01-10"
asof_date: "2026-03-02"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
confidence_level: "normal"
quality_score: 60
sample_size: 13
event_direction: "down"
event_actual: 158268.0
event_previous: 158316.0
event_delta: -48.0
direction_basis: "vs_previous"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.99
  mdd_t7: -0.14
  volatility: 10.45
  impact_t1_pct: -0.14
  impact_t7_pct: 10.31
probabilities:
  sample_size: 13
  t1:
    up: 38.46
    down: 61.54
    median: -0.05
    mean: 0.25
    sample: 13
  t7:
    up: 61.54
    down: 38.46
    median: 1.54
    mean: 3.29
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 1
    t1:
      up: 0.0
      down: 100.0
      median: -0.14
      mean: -0.14
      sample: 1
    t7:
      up: 100.0
      down: 0.0
      median: 10.31
      mean: 10.31
      sample: 1
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-01-10**
- As-of date (T-1): **2026-03-02**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158268.0, Previous 158316.0, Delta -48.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 38.46% | 61.54% | -0.05% | 0.25% | 13 |
| T+7 | 61.54% | 38.46% | 1.54% | 3.29% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | -0.14% | -0.14% | 1 |
| T+7 | 100.0% | 0.0% | 10.31% | 10.31% | 1 |

## Historical Distribution Summary

When NFP was **DOWN**, BTC T+1 up probability was **0.0%** (n=1).

When NFP was **DOWN**, BTC T+7 up probability was **100.0%** (n=1).

Same-direction T+7 median return: **10.31%**.

For BTC, historical NFP windows show all-history T+1 up probability of 38.46% and T+7 up probability of 61.54%. When NFP printed Down versus previous, T+1 up probability was 0.0% and T+7 up probability was 100.0% across 1 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
