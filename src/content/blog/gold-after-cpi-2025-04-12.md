---
title: "Historical Performance of GOLD After CPI (2025-04-12)"
description: "Historical probability profile for GOLD around CPI events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-04-12"
asof_date: "2026-03-02"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 15.46
robust_score: 9.46
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 70
sample_size: 14
freshness_days: 324
freshness_status: "stale"
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 320.302
event_previous: 319.785
event_delta: 0.517
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 1.26
  mdd_t7: 0.0
  volatility: 0.85
  impact_t1_pct: 0.22
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
    direction: "up"
    sample_size: 13
    t1:
      up: 53.85
      down: 46.15
      median: 0.56
      mean: 0.36
      sample: 13
    t7:
      up: 76.92
      down: 23.08
      median: 1.52
      mean: 1.07
      sample: 13
related_events: [{"slug": "gold-after-cpi-2025-02-12", "title": "GOLD After CPI (2025-02-12): Historical T+1/T+7 Probability", "event_date": "2025-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 7.09, "median_t7_pct": 0.36, "sample_size": 0}, {"slug": "gold-after-cpi-2024-02-20", "title": "GOLD After CPI (2024-02-20): Historical T+1/T+7 Probability", "event_date": "2024-02-20", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 6.12, "median_t7_pct": 0.32, "sample_size": 0}, {"slug": "gold-after-cpi-2024-05-15", "title": "GOLD After CPI (2024-05-15): Historical T+1/T+7 Probability", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.47, "median_t7_pct": 0.02, "sample_size": 0}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **GOLD**
- Event date: **2025-04-12**
- As-of date (T-1): **2026-03-02**
- Freshness age: **324 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 320.302, Previous 319.785, Delta +0.5170)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.27% | 0.22% | 14 |
| T+7 | 76.92% | 23.08% | 1.52% | 1.07% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.56% | 0.36% | 13 |
| T+7 | 76.92% | 23.08% | 1.52% | 1.07% | 13 |

## Historical Distribution Summary

When CPI was **UP**, GOLD T+1 up probability was **53.85%** (n=13).

When CPI was **UP**, GOLD T+7 up probability was **76.92%** (n=13).

Same-direction T+7 median return: **1.52%**.

For GOLD, historical CPI windows show all-history T+1 up probability of 50.0% and T+7 up probability of 76.92%. When CPI printed Up versus previous, T+1 up probability was 53.85% and T+7 up probability was 76.92% across 13 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
