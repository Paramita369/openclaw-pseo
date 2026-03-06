---
title: "BTC After NFP (2024-11-01): Event Probability and Median Return"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "nfp_3"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-11-01"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 4.31
robust_score: -1.69
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 13
freshness_days: 489
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 3.29
hub_baseline_median_t7: 1.54
hub_baseline_std_t7: 5.8462
hub_baseline_delta: 8.63
z_score_t7: 1.18
percentile_t7: 84.62
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 158079.0
event_previous: 157945.0
event_delta: 134.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.97
  mdd_t7: -0.28
  volatility: 10.45
  impact_t1_pct: -0.28
  impact_t7_pct: 10.17
probabilities:
  sample_size: 13
  t1:
    up: 38.46
    down: 61.54
    median: -0.05
    mean: 0.25
    sample: 13
  t7:
    up: 61.54
    down: 38.46
    median: 1.54
    mean: 3.29
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 12
    t1:
      up: 41.67
      down: 58.33
      median: -0.03
      mean: 0.28
      sample: 12
    t7:
      up: 58.33
      down: 41.67
      median: 1.07
      mean: 2.7
      sample: 12
related_events: [{"slug": "btc-after-nfp-2026-02-06", "title": "BTC Post-NFP Setup (2026-02-06): Historical Probability Lens", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.54, "sample_size": 13}, {"slug": "btc-after-nfp-2026-01-02", "title": "NFP Print (2026-01-02) vs BTC: Quantified Directional Odds", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.54, "sample_size": 13}, {"slug": "btc-after-nfp-2025-12-05", "title": "BTC Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.54, "sample_size": 13}]
chartData: [{"time": "2024-10-29", "open": 69910.05, "high": 73577.21, "low": 69729.91, "close": 72720.49}, {"time": "2024-10-30", "open": 72715.37, "high": 72905.3, "low": 71411.73, "close": 72339.54}, {"time": "2024-10-31", "open": 72335.05, "high": 72662.31, "low": 69590.5, "close": 70215.19}, {"time": "2024-11-01", "open": 70216.9, "high": 71559.02, "low": 68779.7, "close": 69482.47}, {"time": "2024-11-02", "open": 69486.02, "high": 69867.35, "low": 69033.72, "close": 69289.27}, {"time": "2024-11-03", "open": 69296.38, "high": 69361.66, "low": 67482.52, "close": 68741.12}, {"time": "2024-11-04", "open": 68742.13, "high": 69433.18, "low": 66803.65, "close": 67811.51}, {"time": "2024-11-05", "open": 67811.17, "high": 70522.79, "low": 67458.87, "close": 69359.56}, {"time": "2024-11-06", "open": 69358.5, "high": 76460.16, "low": 69322.03, "close": 75639.08}, {"time": "2024-11-07", "open": 75637.09, "high": 76943.12, "low": 74480.42, "close": 75904.86}, {"time": "2024-11-08", "open": 75902.84, "high": 77252.75, "low": 75648.74, "close": 76545.48}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2024-11-01**
- As-of date (T-1): **2026-03-05**
- Freshness age: **489 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 158079.0, Previous 157945.0, Delta +134.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 38.46% | 61.54% | -0.05% | 0.25% | 13 |
| T+7 | 61.54% | 38.46% | 1.54% | 3.29% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 41.67% | 58.33% | -0.03% | 0.28% | 12 |
| T+7 | 58.33% | 41.67% | 1.07% | 2.7% | 12 |

## Historical Distribution Summary

When NFP was **UP**, BTC T+1 up probability was **41.67%** (n=12).

When NFP was **UP**, BTC T+7 up probability was **58.33%** (n=12).

Same-direction T+7 median return: **1.07%**.

For BTC, historical NFP windows show all-history T+1 up probability of 38.46% and T+7 up probability of 61.54%. When NFP printed Up versus previous, T+1 up probability was 41.67% and T+7 up probability was 58.33% across 12 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
