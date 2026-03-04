---
title: "Fed Decision (2025-12-11) and GOLD: Event-Driven Odds"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-12-11"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 11.13
robust_score: 11.13
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 23
freshness_days: 82
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/gold-after-fomc-2025-12-11"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "down"
event_actual: 3.75
event_previous: 4.0
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 4.04
  impact_t1_pct: 0.34
  impact_t7_pct: 1.26
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
related_events: [{"slug": "gold-after-fomc-2025-12-10", "title": "GOLD After FOMC (2025-12-10): Historical T+1/T+7 Probability", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.6, "sample_size": 0}, {"slug": "gold-after-fomc-2025-09-18", "title": "GOLD After FOMC (2025-09-18): Historical T+1/T+7 Probability", "event_date": "2025-09-18", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.56, "sample_size": 0}, {"slug": "gold-after-fomc-2025-07-30", "title": "GOLD After FOMC (2025-07-30): Historical T+1/T+7 Probability", "event_date": "2025-07-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.55, "sample_size": 0}]
chartData: [{"time": "2025-12-08", "open": 4205.5, "high": 4215.8, "low": 4175.5, "close": 4187.2}, {"time": "2025-12-09", "open": 4190.7, "high": 4219.7, "low": 4177.7, "close": 4206.7}, {"time": "2025-12-10", "open": 4209.0, "high": 4234.5, "low": 4183.6, "close": 4196.4}, {"time": "2025-12-11", "open": 4224.0, "high": 4286.9, "low": 4214.3, "close": 4285.5}, {"time": "2025-12-12", "open": 4276.4, "high": 4355.0, "low": 4260.0, "close": 4300.1}, {"time": "2025-12-15", "open": 4308.3, "high": 4349.2, "low": 4292.9, "close": 4306.7}, {"time": "2025-12-16", "open": 4270.5, "high": 4321.4, "low": 4270.5, "close": 4304.5}, {"time": "2025-12-17", "open": 4308.5, "high": 4351.4, "low": 4308.5, "close": 4347.5}, {"time": "2025-12-18", "open": 4331.0, "high": 4348.1, "low": 4328.2, "close": 4339.5}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2025-12-11**
- As-of date (T-1): **2026-03-03**
- Freshness age: **82 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 3.75, Previous 4.0, Delta -0.2500)
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
