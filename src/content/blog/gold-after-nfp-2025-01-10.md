---
title: "GOLD Post-NFP Setup (2025-01-10): Historical Probability Lens"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-01-10"
asof_date: "2026-03-05"
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
quality_score: 50
sample_size: 13
freshness_days: 419
freshness_status: "stale"
index_tier: "C"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.14
hub_baseline_median_t7: 1.07
hub_baseline_std_t7: 1.6215
hub_baseline_delta: 0.25
z_score_t7: 0.11
percentile_t7: 76.92
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "none"
canonical_url: ""
robots_directive: "noindex,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "down"
event_actual: 158268.0
event_previous: 158316.0
event_delta: -48.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -3.71
  mdd_t7: -4.91
  volatility: 1.32
  impact_t1_pct: 0.0
  impact_t7_pct: 1.32
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
related_events: [{"slug": "gold-after-nfp-2024-03-01", "title": "GOLD NFP Reaction (2024-03-01): T+1/T+7 Up Probability", "event_date": "2024-03-01", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.57, "median_t7_pct": 1.07, "sample_size": 13}, {"slug": "gold-after-nfp-2024-04-05", "title": "NFP Print (2024-04-05) vs GOLD: Quantified Directional Odds", "event_date": "2024-04-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 4.16, "median_t7_pct": 1.07, "sample_size": 13}, {"slug": "gold-after-nfp-2024-09-06", "title": "GOLD Post-NFP Setup (2024-09-06): Historical Probability Lens", "event_date": "2024-09-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 1.09, "median_t7_pct": 1.07, "sample_size": 13}]
chartData: [{"time": "2025-01-07", "open": 2653.4, "high": 2657.5, "low": 2653.0, "close": 2656.7}, {"time": "2025-01-08", "open": 2655.5, "high": 2676.9, "low": 2653.5, "close": 2664.5}, {"time": "2025-01-09", "open": 2669.7, "high": 2686.3, "low": 2667.9, "close": 2683.8}, {"time": "2025-01-10", "open": 2686.1, "high": 2720.1, "low": 2683.7, "close": 2708.5}, {"time": "2025-01-13", "open": 2711.1, "high": 2711.2, "low": 2673.5, "close": 2673.5}, {"time": "2025-01-14", "open": 2673.6, "high": 2688.3, "low": 2670.8, "close": 2677.5}, {"time": "2025-01-15", "open": 2690.8, "high": 2712.5, "low": 2690.8, "close": 2712.5}, {"time": "2025-01-16", "open": 2731.7, "high": 2749.8, "low": 2731.7, "close": 2746.4}, {"time": "2025-01-17", "open": 2736.0, "high": 2751.6, "low": 2725.5, "close": 2744.3}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
- Event date: **2025-01-10**
- As-of date (T-1): **2026-03-05**
- Freshness age: **419 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158268.0, Previous 158316.0, Delta -48.0000)
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
