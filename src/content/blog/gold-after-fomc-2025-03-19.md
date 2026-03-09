---
title: "Fed Decision (2025-03-19) and GOLD: Event-Driven Odds"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-03-19"
asof_date: "2026-03-08"
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
freshness_days: 354
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.05
hub_baseline_median_t7: 0.9
hub_baseline_std_t7: 2.9027
hub_baseline_delta: -1.39
z_score_t7: -0.18
percentile_t7: 39.13
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/gold/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "flat"
event_actual: 4.5
event_previous: 4.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -0.78
  mdd_t7: -0.49
  volatility: 0.63
  impact_t1_pct: 0.14
  impact_t7_pct: -0.49
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
related_events: [{"slug": "gold-after-fomc-2024-01-30", "title": "2024-01-30 FOMC Meeting: GOLD T+1/T+7 Probability Profile", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 1.61, "median_t7_pct": 0.9, "sample_size": 9}, {"slug": "gold-after-fomc-2026-01-28", "title": "GOLD After FOMC (2026-01-28): Historical Signal & Probability", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 0.9, "sample_size": 23}, {"slug": "gold-after-fomc-2025-12-10", "title": "2025-12-10 FOMC Meeting: GOLD T+1/T+7 Probability Profile", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 0.9, "sample_size": 23}]
chartData: [{"time": "2025-03-17", "open": 2991.0, "high": 3001.5, "low": 2989.0, "close": 3000.0}, {"time": "2025-03-18", "open": 3006.4, "high": 3039.2, "low": 3004.4, "close": 3035.1}, {"time": "2025-03-19", "open": 3035.2, "high": 3050.9, "low": 3030.9, "close": 3035.9}, {"time": "2025-03-20", "open": 3047.3, "high": 3047.3, "low": 3034.4, "close": 3040.0}, {"time": "2025-03-21", "open": 3034.5, "high": 3037.5, "low": 3000.9, "close": 3018.2}, {"time": "2025-03-24", "open": 3024.3, "high": 3024.3, "low": 3006.0, "close": 3013.1}, {"time": "2025-03-25", "open": 3026.4, "high": 3028.8, "low": 3023.7, "close": 3023.7}, {"time": "2025-03-26", "open": 3033.2, "high": 3033.2, "low": 3019.5, "close": 3020.9}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2025-03-19**
- As-of date (T-1): **2026-03-08**
- Freshness age: **354 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.5, Previous 4.5, Delta +0.0000)
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
