---
title: "GOLD After FOMC (2024-07-30): Historical Signal & Probability"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 1
title_template_key: "fomc_1"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-07-30"
asof_date: "2026-03-10"
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
freshness_days: 588
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 0.05
hub_baseline_median_t7: 0.9
hub_baseline_std_t7: 2.9027
hub_baseline_delta: -1.56
z_score_t7: -0.24
percentile_t7: 30.43
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/gold/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -4.22
  mdd_t7: -1.54
  volatility: 1.55
  impact_t1_pct: 0.89
  impact_t7_pct: -0.66
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
chartData: [{"time": "2024-07-29", "open": 2377.3, "high": 2377.3, "low": 2377.3, "close": 2377.3}, {"time": "2024-07-30", "open": 2380.9, "high": 2409.3, "low": 2373.8, "close": 2405.0}, {"time": "2024-07-31", "open": 2407.1, "high": 2447.6, "low": 2402.8, "close": 2426.5}, {"time": "2024-08-01", "open": 2446.7, "high": 2455.1, "low": 2430.4, "close": 2435.0}, {"time": "2024-08-02", "open": 2444.0, "high": 2477.0, "low": 2416.0, "close": 2425.7}, {"time": "2024-08-05", "open": 2442.0, "high": 2449.8, "low": 2367.4, "close": 2401.7}, {"time": "2024-08-06", "open": 2414.5, "high": 2421.8, "low": 2380.0, "close": 2389.1}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2024-07-30**
- As-of date (T-1): **2026-03-10**
- Freshness age: **588 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.5, Previous 5.5, Delta +0.0000)
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
