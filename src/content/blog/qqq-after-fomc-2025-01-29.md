---
title: "Historical Performance of QQQ After FOMC (2025-01-29)"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-03"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-01-29"
asof_date: "2026-03-02"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 17.56
robust_score: 7.56
penalties:
  sample: 4.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 9
freshness_days: 397
freshness_status: "stale"
data_last_updated_at: "2026-03-03T14:52:49+00:00"
event_direction: "flat"
event_actual: 4.5
event_previous: 4.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 1.59
  mdd_t7: 0.0
  volatility: 0.73
  impact_t1_pct: 0.43
  impact_t7_pct: 1.16
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 0.43
    mean: 0.08
    sample: 9
  t7:
    up: 77.78
    down: 22.22
    median: 1.16
    mean: 1.03
    sample: 9
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 9
    t1:
      up: 55.56
      down: 44.44
      median: 0.43
      mean: 0.08
      sample: 9
    t7:
      up: 77.78
      down: 22.22
      median: 1.16
      mean: 1.03
      sample: 9
related_events: [{"slug": "qqq-after-fomc-2024-01-30", "title": "QQQ After FOMC (2024-01-30): Historical T+1/T+7 Probability", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.07, "median_t7_pct": 0.54, "sample_size": 0}, {"slug": "qqq-after-fomc-2026-01-28", "title": "QQQ After FOMC (2026-01-28): Historical T+1/T+7 Probability", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.0, "sample_size": 0}, {"slug": "qqq-after-fomc-2025-12-10", "title": "QQQ After FOMC (2025-12-10): Historical T+1/T+7 Probability", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.0, "sample_size": 0}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
- Event date: **2025-01-29**
- As-of date (T-1): **2026-03-02**
- Freshness age: **397 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.5, Previous 4.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.43% | 0.08% | 9 |
| T+7 | 77.78% | 22.22% | 1.16% | 1.03% | 9 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.43% | 0.08% | 9 |
| T+7 | 77.78% | 22.22% | 1.16% | 1.03% | 9 |

## Historical Distribution Summary

When FOMC was **FLAT**, QQQ T+1 up probability was **55.56%** (n=9).

When FOMC was **FLAT**, QQQ T+7 up probability was **77.78%** (n=9).

Same-direction T+7 median return: **1.16%**.

For QQQ, historical FOMC windows show all-history T+1 up probability of 55.56% and T+7 up probability of 77.78%. When FOMC printed Flat versus previous, T+1 up probability was 55.56% and T+7 up probability was 77.78% across 9 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
