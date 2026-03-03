---
title: "QQQ After NFP (2025-01-10): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-01-10"
asof_date: "2026-03-02"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 0.46
robust_score: -5.54
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 50
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
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 7.64
  mdd_t7: -1.65
  volatility: 2.87
  impact_t1_pct: 0.0
  impact_t7_pct: 2.87
probabilities:
  sample_size: 13
  t1:
    up: 0.0
    down: 100.0
    median: 0.0
    mean: 0.0
    sample: 0
  t7:
    up: 76.92
    down: 23.08
    median: 1.51
    mean: 1.89
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 0
    t1:
      up: 0.0
      down: 100.0
      median: 0.0
      mean: 0.0
      sample: 0
    t7:
      up: 100.0
      down: 0.0
      median: 2.87
      mean: 2.87
      sample: 1
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
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
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 76.92% | 23.08% | 1.51% | 1.89% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 100.0% | 0.0% | 2.87% | 2.87% | 1 |

## Historical Distribution Summary

When NFP was **DOWN**, QQQ T+1 up probability was **0.0%** (n=0).

When NFP was **DOWN**, QQQ T+7 up probability was **100.0%** (n=1).

Same-direction T+7 median return: **2.87%**.

For QQQ, historical NFP windows show all-history T+1 up probability of 0.0% and T+7 up probability of 76.92%. When NFP printed Down versus previous, T+1 up probability was 0.0% and T+7 up probability was 100.0% across 0 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
