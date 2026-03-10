---
title: "BTC Post-NFP Setup (2025-11-07): Historical Probability Lens"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-11-07"
asof_date: "2026-03-09"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 0.23
robust_score: -5.77
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 34
freshness_days: 122
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 1.55
hub_baseline_median_t7: 1.0
hub_baseline_std_t7: 5.3733
hub_baseline_delta: -9.68
z_score_t7: -1.9
percentile_t7: 2.94
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158449.0
event_previous: 158408.0
event_delta: 41.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -1.14
  mdd_t7: -8.68
  volatility: 7.63
  impact_t1_pct: -1.05
  impact_t7_pct: -8.68
probabilities:
  sample_size: 34
  t1:
    up: 29.41
    down: 70.59
    median: -0.33
    mean: -0.26
    sample: 34
  t7:
    up: 58.82
    down: 41.18
    median: 1.0
    mean: 1.55
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 30
    t1:
      up: 26.67
      down: 73.33
      median: -0.39
      mean: -0.31
      sample: 30
    t7:
      up: 56.67
      down: 43.33
      median: 0.81
      mean: 1.51
      sample: 30
related_events: [{"slug": "btc-after-nfp-2026-02-06", "title": "BTC Post-NFP Setup (2026-02-06): Historical Probability Lens", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.0, "sample_size": 34}, {"slug": "btc-after-nfp-2026-01-02", "title": "NFP Print (2026-01-02) vs BTC: Quantified Directional Odds", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.0, "sample_size": 34}, {"slug": "btc-after-nfp-2025-12-05", "title": "BTC Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.0, "sample_size": 34}]
chartData: [{"time": "2025-11-04", "open": 106541.42, "high": 107264.88, "low": 98962.06, "close": 101590.52}, {"time": "2025-11-05", "open": 101579.23, "high": 104534.7, "low": 98989.91, "close": 103891.84}, {"time": "2025-11-06", "open": 103893.66, "high": 104147.3, "low": 100336.87, "close": 101301.29}, {"time": "2025-11-07", "open": 101286.24, "high": 104052.91, "low": 99257.05, "close": 103372.41}, {"time": "2025-11-08", "open": 103371.7, "high": 103373.56, "low": 101458.04, "close": 102282.12}, {"time": "2025-11-09", "open": 102278.98, "high": 105418.37, "low": 101468.88, "close": 104719.64}, {"time": "2025-11-10", "open": 104723.77, "high": 106564.7, "low": 104350.65, "close": 105996.59}, {"time": "2025-11-11", "open": 105996.86, "high": 107428.26, "low": 102457.33, "close": 102997.47}, {"time": "2025-11-12", "open": 103011.44, "high": 105297.23, "low": 100836.62, "close": 101663.19}, {"time": "2025-11-13", "open": 101674.15, "high": 104005.49, "low": 97988.72, "close": 99697.49}, {"time": "2025-11-14", "open": 99694.7, "high": 99804.43, "low": 94000.73, "close": 94397.79}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-11-07**
- As-of date (T-1): **2026-03-09**
- Freshness age: **122 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158449.0, Previous 158408.0, Delta +41.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 29.41% | 70.59% | -0.33% | -0.26% | 34 |
| T+7 | 58.82% | 41.18% | 1.0% | 1.55% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 26.67% | 73.33% | -0.39% | -0.31% | 30 |
| T+7 | 56.67% | 43.33% | 0.81% | 1.51% | 30 |

## Historical Distribution Summary

When NFP was **UP**, BTC T+1 up probability was **26.67%** (n=30).

When NFP was **UP**, BTC T+7 up probability was **56.67%** (n=30).

Same-direction T+7 median return: **0.81%**.

For BTC, historical NFP windows show all-history T+1 up probability of 29.41% and T+7 up probability of 58.82%. When NFP printed Up versus previous, T+1 up probability was 26.67% and T+7 up probability was 56.67% across 30 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
