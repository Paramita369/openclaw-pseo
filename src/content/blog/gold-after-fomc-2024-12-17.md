---
title: "2024-12-17 FOMC Meeting: GOLD T+1/T+7 Probability Profile"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
pubDate: "2026-03-12"
title_variant_id: 3
title_template_key: "fomc_3"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-12-17"
asof_date: "2026-03-11"
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
freshness_days: 449
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.05
hub_baseline_median_t7: 0.9
hub_baseline_std_t7: 2.9027
hub_baseline_delta: -1.82
z_score_t7: -0.33
percentile_t7: 26.09
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/gold/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:04:03+00:00"
event_direction: "flat"
event_actual: 4.75
event_previous: 4.75
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.48
  mdd_t7: -0.92
  volatility: 0.62
  impact_t1_pct: -0.3
  impact_t7_pct: -0.92
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
related_events: [{"slug": "gold-after-fomc-2024-01-30", "title": "2024-01-30 FOMC Meeting: GOLD T+1/T+7 Probability Profile", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 1.61, "median_t7_pct": 0.9, "sample_size": 23}, {"slug": "gold-after-fomc-2026-01-28", "title": "GOLD After FOMC (2026-01-28): Historical Signal & Probability", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 0.9, "sample_size": 23}, {"slug": "gold-after-fomc-2025-12-10", "title": "2025-12-10 FOMC Meeting: GOLD T+1/T+7 Probability Profile", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 0.9, "sample_size": 23}]
chartData: [{"time": "2024-12-16", "open": 2658.3, "high": 2663.3, "low": 2651.0, "close": 2651.4}, {"time": "2024-12-17", "open": 2651.8, "high": 2652.3, "low": 2632.5, "close": 2644.4}, {"time": "2024-12-18", "open": 2644.3, "high": 2647.1, "low": 2590.2, "close": 2636.5}, {"time": "2024-12-19", "open": 2582.1, "high": 2610.3, "low": 2582.1, "close": 2592.2}, {"time": "2024-12-20", "open": 2605.3, "high": 2631.6, "low": 2604.9, "close": 2628.7}, {"time": "2024-12-23", "open": 2620.0, "high": 2627.7, "low": 2611.1, "close": 2612.3}, {"time": "2024-12-24", "open": 2613.0, "high": 2620.0, "low": 2609.5, "close": 2620.0}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2024-12-17**
- As-of date (T-1): **2026-03-11**
- Freshness age: **449 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.75, Previous 4.75, Delta +0.0000)
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
