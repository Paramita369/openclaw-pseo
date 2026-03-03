---
title: "Historical Performance of GOLD After NFP (2025-08-01)"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-08-01"
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
quality_score: 40
sample_size: 13
freshness_days: 213
freshness_status: "stale"
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "down"
event_actual: 158472.0
event_previous: 158542.0
event_delta: -70.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.0
  mdd_t7: 0.0
  volatility: 1.14
  impact_t1_pct: 0.0
  impact_t7_pct: 1.14
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
      median: 1.32
      mean: 1.32
      sample: 1
related_events: [{"slug": "gold-after-nfp-2024-03-01", "title": "GOLD After NFP (2024-03-01): Historical T+1/T+7 Probability", "event_date": "2024-03-01", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.57, "median_t7_pct": 4.39, "sample_size": 0}, {"slug": "gold-after-nfp-2024-04-05", "title": "GOLD After NFP (2024-04-05): Historical T+1/T+7 Probability", "event_date": "2024-04-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 4.16, "median_t7_pct": 1.31, "sample_size": 0}, {"slug": "gold-after-nfp-2024-09-06", "title": "GOLD After NFP (2024-09-06): Historical T+1/T+7 Probability", "event_date": "2024-09-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 1.09, "median_t7_pct": 3.52, "sample_size": 0}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
- Event date: **2025-08-01**
- As-of date (T-1): **2026-03-02**
- Freshness age: **213 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158472.0, Previous 158542.0, Delta -70.0000)
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
| T+7 | 100.0% | 0.0% | 1.32% | 1.32% | 1 |

## Historical Distribution Summary

When NFP was **DOWN**, GOLD T+1 up probability was **0.0%** (n=0).

When NFP was **DOWN**, GOLD T+7 up probability was **100.0%** (n=1).

Same-direction T+7 median return: **1.32%**.

For GOLD, historical NFP windows show all-history T+1 up probability of 0.0% and T+7 up probability of 84.62%. When NFP printed Down versus previous, T+1 up probability was 0.0% and T+7 up probability was 100.0% across 0 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
