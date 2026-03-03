---
title: "ETH After NFP (2025-01-10): Historical T+1/T+7 Probability"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-01-10"
asof_date: "2026-03-02"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Bullish"
raw_signal_score: 8.93
robust_score: 2.93
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 60
sample_size: 13
freshness_days: 416
freshness_status: "stale"
data_last_updated_at: "2026-03-03T09:55:20+00:00"
event_direction: "down"
event_actual: 158268.0
event_previous: 158316.0
event_delta: -48.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.08
  mdd_t7: 0.0
  volatility: 5.87
  impact_t1_pct: 0.45
  impact_t7_pct: 6.32
probabilities:
  sample_size: 13
  t1:
    up: 53.85
    down: 46.15
    median: 0.03
    mean: 0.11
    sample: 13
  t7:
    up: 61.54
    down: 38.46
    median: 5.12
    mean: 3.32
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 1
    t1:
      up: 100.0
      down: 0.0
      median: 0.45
      mean: 0.45
      sample: 1
    t7:
      up: 100.0
      down: 0.0
      median: 6.32
      mean: 6.32
      sample: 1
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2025-01-10**
- As-of date (T-1): **2026-03-02**
- Freshness age: **416 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158268.0, Previous 158316.0, Delta -48.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.03% | 0.11% | 13 |
| T+7 | 61.54% | 38.46% | 5.12% | 3.32% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 100.0% | 0.0% | 0.45% | 0.45% | 1 |
| T+7 | 100.0% | 0.0% | 6.32% | 6.32% | 1 |

## Historical Distribution Summary

When NFP was **DOWN**, ETH T+1 up probability was **100.0%** (n=1).

When NFP was **DOWN**, ETH T+7 up probability was **100.0%** (n=1).

Same-direction T+7 median return: **6.32%**.

For ETH, historical NFP windows show all-history T+1 up probability of 53.85% and T+7 up probability of 61.54%. When NFP printed Down versus previous, T+1 up probability was 100.0% and T+7 up probability was 100.0% across 1 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
