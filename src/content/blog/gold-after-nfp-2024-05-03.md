---
title: "GOLD After NFP (2024-05-03): Event Probability and Median Return"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 3
title_template_key: "nfp_3"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-05-03"
asof_date: "2026-03-10"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 21.71
robust_score: 15.71
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 34
freshness_days: 676
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 1.61
hub_baseline_median_t7: 1.31
hub_baseline_std_t7: 1.944
hub_baseline_delta: 1.66
z_score_t7: 0.7
percentile_t7: 73.53
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/gold/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 157608.0
event_previous: 157530.0
event_delta: 78.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -1.41
  mdd_t7: -15.3
  volatility: 2.4
  impact_t1_pct: 0.57
  impact_t7_pct: 2.97
probabilities:
  sample_size: 34
  t1:
    up: 66.67
    down: 33.33
    median: 0.5
    mean: 0.57
    sample: 21
  t7:
    up: 79.41
    down: 20.59
    median: 1.31
    mean: 1.61
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 18
    t1:
      up: 61.11
      down: 38.89
      median: 0.34
      mean: 0.51
      sample: 18
    t7:
      up: 76.67
      down: 23.33
      median: 1.1
      mean: 1.49
      sample: 30
related_events: [{"slug": "gold-after-nfp-2024-03-01", "title": "GOLD NFP Reaction (2024-03-01): T+1/T+7 Up Probability", "event_date": "2024-03-01", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 6.57, "median_t7_pct": 1.31, "sample_size": 34}, {"slug": "gold-after-nfp-2024-04-05", "title": "NFP Print (2024-04-05) vs GOLD: Quantified Directional Odds", "event_date": "2024-04-05", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 4.16, "median_t7_pct": 1.31, "sample_size": 34}, {"slug": "gold-after-nfp-2024-09-06", "title": "GOLD Post-NFP Setup (2024-09-06): Historical Probability Lens", "event_date": "2024-09-06", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 1.09, "median_t7_pct": 1.31, "sample_size": 34}]
chartData: [{"time": "2024-04-30", "open": 2322.5, "high": 2322.5, "low": 2291.4, "close": 2291.4}, {"time": "2024-05-01", "open": 2287.7, "high": 2327.3, "low": 2283.8, "close": 2299.9}, {"time": "2024-05-02", "open": 2321.7, "high": 2324.7, "low": 2292.3, "close": 2299.2}, {"time": "2024-05-03", "open": 2300.0, "high": 2301.0, "low": 2277.6, "close": 2299.0}, {"time": "2024-05-06", "open": 2322.8, "high": 2325.5, "low": 2314.2, "close": 2321.6}, {"time": "2024-05-07", "open": 2324.3, "high": 2324.3, "low": 2315.2, "close": 2315.2}, {"time": "2024-05-08", "open": 2313.6, "high": 2313.6, "low": 2313.6, "close": 2313.6}, {"time": "2024-05-09", "open": 2310.7, "high": 2339.5, "low": 2310.7, "close": 2332.1}, {"time": "2024-05-10", "open": 2367.3, "high": 2367.3, "low": 2367.3, "close": 2367.3}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
- Event date: **2024-05-03**
- As-of date (T-1): **2026-03-10**
- Freshness age: **676 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157608.0, Previous 157530.0, Delta +78.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 66.67% | 33.33% | 0.5% | 0.57% | 21 |
| T+7 | 79.41% | 20.59% | 1.31% | 1.61% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 61.11% | 38.89% | 0.34% | 0.51% | 18 |
| T+7 | 76.67% | 23.33% | 1.1% | 1.49% | 30 |

## Historical Distribution Summary

When NFP was **UP**, GOLD T+1 up probability was **61.11%** (n=18).

When NFP was **UP**, GOLD T+7 up probability was **76.67%** (n=30).

Same-direction T+7 median return: **1.1%**.

For GOLD, historical NFP windows show all-history T+1 up probability of 66.67% and T+7 up probability of 79.41%. When NFP printed Up versus previous, T+1 up probability was 61.11% and T+7 up probability was 76.67% across 18 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
