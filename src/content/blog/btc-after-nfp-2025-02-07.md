---
title: "NFP Print (2025-02-07) vs BTC: Quantified Directional Odds"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 4
title_template_key: "nfp_4"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-02-07"
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
quality_score: 70
sample_size: 13
freshness_days: 391
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 3.29
hub_baseline_median_t7: 1.54
hub_baseline_std_t7: 5.8462
hub_baseline_delta: 1.75
z_score_t7: 0.0
percentile_t7: 61.54
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 158310.0
event_previous: 158268.0
event_delta: 42.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.08
  mdd_t7: 0.0
  volatility: 3.04
  impact_t1_pct: 0.25
  impact_t7_pct: 3.29
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
chartData: [{"time": "2025-02-04", "open": 101398.72, "high": 101745.62, "low": 96208.11, "close": 97871.82}, {"time": "2025-02-05", "open": 97878.01, "high": 99113.21, "low": 96174.83, "close": 96615.45}, {"time": "2025-02-06", "open": 96610.64, "high": 99168.61, "low": 95707.35, "close": 96593.3}, {"time": "2025-02-07", "open": 96581.32, "high": 100154.14, "low": 95653.88, "close": 96529.09}, {"time": "2025-02-08", "open": 96533.26, "high": 96877.8, "low": 95702.49, "close": 96482.45}, {"time": "2025-02-09", "open": 96481.31, "high": 97325.28, "low": 94745.26, "close": 96500.09}, {"time": "2025-02-10", "open": 96499.46, "high": 98333.22, "low": 95320.84, "close": 97437.55}, {"time": "2025-02-11", "open": 97438.13, "high": 98492.9, "low": 94875.04, "close": 95747.43}, {"time": "2025-02-12", "open": 95745.7, "high": 98151.02, "low": 94101.2, "close": 97885.86}, {"time": "2025-02-13", "open": 97888.75, "high": 98111.09, "low": 95269.71, "close": 96623.87}, {"time": "2025-02-14", "open": 96623.37, "high": 98819.47, "low": 96342.8, "close": 97508.97}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-02-07**
- As-of date (T-1): **2026-03-05**
- Freshness age: **391 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 158310.0, Previous 158268.0, Delta +42.0000)
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
