---
title: "Historical Performance of SPY After NFP (2025-03-07)"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-03-07"
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
quality_score: 40
sample_size: 13
freshness_days: 360
freshness_status: "stale"
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 158377.0
event_previous: 158310.0
event_delta: 67.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.0
  mdd_t7: 0.0
  volatility: 1.41
  impact_t1_pct: 0.0
  impact_t7_pct: 1.41
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
    median: 1.39
    mean: 1.41
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
      up: 75.0
      down: 25.0
      median: 1.27
      mean: 1.28
      sample: 12
related_events: [{"slug": "spy-after-nfp-2024-07-05", "title": "SPY After NFP (2024-07-05): Historical T+1/T+7 Probability", "event_date": "2024-07-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.02, "median_t7_pct": 0.96, "sample_size": 0}, {"slug": "spy-after-nfp-2024-01-05", "title": "SPY After NFP (2024-01-05): Historical T+1/T+7 Probability", "event_date": "2024-01-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.04, "median_t7_pct": 1.87, "sample_size": 0}, {"slug": "spy-after-nfp-2024-10-04", "title": "SPY After NFP (2024-10-04): Historical T+1/T+7 Probability", "event_date": "2024-10-04", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.43, "median_t7_pct": 1.15, "sample_size": 0}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2025-03-07**
- As-of date (T-1): **2026-03-02**
- Freshness age: **360 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 158377.0, Previous 158310.0, Delta +67.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 76.92% | 23.08% | 1.39% | 1.41% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 75.0% | 25.0% | 1.27% | 1.28% | 12 |

## Historical Distribution Summary

When NFP was **UP**, SPY T+1 up probability was **0.0%** (n=0).

When NFP was **UP**, SPY T+7 up probability was **75.0%** (n=12).

Same-direction T+7 median return: **1.27%**.

For SPY, historical NFP windows show all-history T+1 up probability of 0.0% and T+7 up probability of 76.92%. When NFP printed Up versus previous, T+1 up probability was 0.0% and T+7 up probability was 75.0% across 0 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
