---
title: "GOLD After FOMC (2025-09-18): Historical Signal & Probability"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 1
title_template_key: "fomc_1"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-09-18"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 11.13
robust_score: 5.13
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 23
freshness_days: 166
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/gold/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "down"
event_actual: 4.25
event_previous: 4.5
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: -0.1
  volatility: 12.91
  impact_t1_pct: 0.76
  impact_t7_pct: 2.56
probabilities:
  sample_size: 23
  t1:
    up: 69.57
    down: 30.43
    median: 0.34
    mean: 0.24
    sample: 23
  t7:
    up: 56.52
    down: 43.48
    median: 0.9
    mean: 0.05
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 6
    t1:
      up: 66.67
      down: 33.33
      median: 0.55
      mean: 0.07
      sample: 6
    t7:
      up: 66.67
      down: 33.33
      median: 1.53
      mean: 0.62
      sample: 6
related_events: [{"slug": "gold-after-fomc-2025-12-11", "title": "GOLD After FOMC (2025-12-11): Historical T+1/T+7 Probability", "event_date": "2025-12-11", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.26, "sample_size": 0}, {"slug": "gold-after-fomc-2025-12-10", "title": "GOLD After FOMC (2025-12-10): Historical T+1/T+7 Probability", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.6, "sample_size": 0}, {"slug": "gold-after-fomc-2025-07-30", "title": "GOLD After FOMC (2025-07-30): Historical T+1/T+7 Probability", "event_date": "2025-07-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.55, "sample_size": 0}]
chartData: [{"time": "2025-09-15", "open": 3640.0, "high": 3686.4, "low": 3635.1, "close": 3682.2}, {"time": "2025-09-16", "open": 3681.4, "high": 3698.6, "low": 3681.4, "close": 3688.9}, {"time": "2025-09-17", "open": 3669.0, "high": 3685.2, "low": 3661.6, "close": 3681.8}, {"time": "2025-09-18", "open": 3654.6, "high": 3667.4, "low": 3637.0, "close": 3643.7}, {"time": "2025-09-19", "open": 3659.0, "high": 3685.9, "low": 3658.2, "close": 3671.5}, {"time": "2025-09-22", "open": 3688.2, "high": 3748.2, "low": 3688.0, "close": 3740.7}, {"time": "2025-09-23", "open": 3747.0, "high": 3786.0, "low": 3740.0, "close": 3780.6}, {"time": "2025-09-24", "open": 3769.8, "high": 3772.5, "low": 3732.1, "close": 3732.1}, {"time": "2025-09-25", "open": 3742.8, "high": 3756.0, "low": 3724.7, "close": 3736.9}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2025-09-18**
- As-of date (T-1): **2026-03-03**
- Freshness age: **166 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 4.25, Previous 4.5, Delta -0.2500)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 69.57% | 30.43% | 0.34% | 0.24% | 23 |
| T+7 | 56.52% | 43.48% | 0.9% | 0.05% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 66.67% | 33.33% | 0.55% | 0.07% | 6 |
| T+7 | 66.67% | 33.33% | 1.53% | 0.62% | 6 |

## Historical Distribution Summary

When FOMC was **DOWN**, GOLD T+1 up probability was **66.67%** (n=6).

When FOMC was **DOWN**, GOLD T+7 up probability was **66.67%** (n=6).

Same-direction T+7 median return: **1.53%**.

For GOLD, historical FOMC windows show all-history T+1 up probability of 69.57% and T+7 up probability of 56.52%. When FOMC printed Down versus previous, T+1 up probability was 66.67% and T+7 up probability was 66.67% across 6 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
