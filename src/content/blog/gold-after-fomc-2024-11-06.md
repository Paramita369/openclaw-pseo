---
title: "GOLD After FOMC (2024-11-06): Historical Signal & Probability"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 1
title_template_key: "fomc_1"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-11-06"
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
quality_score: 100
sample_size: 23
freshness_days: 482
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/gold/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "flat"
event_actual: 5.0
event_previous: 5.0
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -9.22
  mdd_t7: -4.36
  volatility: 43.76
  impact_t1_pct: 1.15
  impact_t7_pct: -3.25
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
    direction: "flat"
    sample_size: 17
    t1:
      up: 70.59
      down: 29.41
      median: 0.32
      mean: 0.31
      sample: 17
    t7:
      up: 52.94
      down: 47.06
      median: 0.15
      mean: -0.16
      sample: 17
related_events: [{"slug": "gold-after-fomc-2025-12-11", "title": "GOLD After FOMC (2025-12-11): Historical T+1/T+7 Probability", "event_date": "2025-12-11", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.26, "sample_size": 0}, {"slug": "gold-after-fomc-2025-12-10", "title": "GOLD After FOMC (2025-12-10): Historical T+1/T+7 Probability", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.6, "sample_size": 0}, {"slug": "gold-after-fomc-2025-09-18", "title": "GOLD After FOMC (2025-09-18): Historical T+1/T+7 Probability", "event_date": "2025-09-18", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.56, "sample_size": 0}]
chartData: [{"time": "2024-11-04", "open": 2736.5, "high": 2737.1, "low": 2736.1, "close": 2736.1}, {"time": "2024-11-05", "open": 2743.0, "high": 2743.9, "low": 2740.3, "close": 2740.3}, {"time": "2024-11-06", "open": 2734.5, "high": 2734.5, "low": 2659.4, "close": 2667.6}, {"time": "2024-11-07", "open": 2662.5, "high": 2699.1, "low": 2662.5, "close": 2698.4}, {"time": "2024-11-08", "open": 2688.5, "high": 2694.6, "low": 2682.9, "close": 2687.5}, {"time": "2024-11-11", "open": 2671.7, "high": 2671.7, "low": 2611.2, "close": 2611.2}, {"time": "2024-11-12", "open": 2605.5, "high": 2605.5, "low": 2592.8, "close": 2600.0}, {"time": "2024-11-13", "open": 2611.1, "high": 2611.8, "low": 2580.8, "close": 2580.8}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2024-11-06**
- As-of date (T-1): **2026-03-03**
- Freshness age: **482 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.0, Previous 5.0, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 69.57% | 30.43% | 0.34% | 0.24% | 23 |
| T+7 | 56.52% | 43.48% | 0.9% | 0.05% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 70.59% | 29.41% | 0.32% | 0.31% | 17 |
| T+7 | 52.94% | 47.06% | 0.15% | -0.16% | 17 |

## Historical Distribution Summary

When FOMC was **FLAT**, GOLD T+1 up probability was **70.59%** (n=17).

When FOMC was **FLAT**, GOLD T+7 up probability was **52.94%** (n=17).

Same-direction T+7 median return: **0.15%**.

For GOLD, historical FOMC windows show all-history T+1 up probability of 69.57% and T+7 up probability of 56.52%. When FOMC printed Flat versus previous, T+1 up probability was 70.59% and T+7 up probability was 52.94% across 17 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
