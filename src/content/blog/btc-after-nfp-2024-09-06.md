---
title: "BTC Post-NFP Setup (2024-09-06): Historical Probability Lens"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-09-06"
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
freshness_days: 545
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 3.29
hub_baseline_median_t7: 1.54
hub_baseline_std_t7: 5.8462
hub_baseline_delta: 10.74
z_score_t7: 1.54
percentile_t7: 100.0
narrative_trigger: "extreme_outperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 157912.0
event_previous: 157757.0
event_delta: 155.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.03
  mdd_t7: 0.0
  volatility: 11.93
  impact_t1_pct: 0.35
  impact_t7_pct: 12.28
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
chartData: [{"time": "2024-09-03", "open": 59106.19, "high": 59815.06, "low": 57425.17, "close": 57431.02}, {"time": "2024-09-04", "open": 57430.35, "high": 58511.57, "low": 55673.16, "close": 57971.54}, {"time": "2024-09-05", "open": 57971.7, "high": 58300.58, "low": 55712.45, "close": 56160.49}, {"time": "2024-09-06", "open": 56160.19, "high": 56976.11, "low": 52598.7, "close": 53948.75}, {"time": "2024-09-07", "open": 53949.09, "high": 54838.14, "low": 53740.07, "close": 54139.69}, {"time": "2024-09-08", "open": 54147.93, "high": 55300.86, "low": 53653.76, "close": 54841.57}, {"time": "2024-09-09", "open": 54851.89, "high": 58041.12, "low": 54598.43, "close": 57019.54}, {"time": "2024-09-10", "open": 57020.1, "high": 58029.98, "low": 56419.41, "close": 57648.71}, {"time": "2024-09-11", "open": 57650.29, "high": 57991.32, "low": 55567.34, "close": 57343.17}, {"time": "2024-09-12", "open": 57343.17, "high": 58534.36, "low": 57330.1, "close": 58127.01}, {"time": "2024-09-13", "open": 58130.32, "high": 60648.02, "low": 57650.11, "close": 60571.3}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2024-09-06**
- As-of date (T-1): **2026-03-05**
- Freshness age: **545 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 157912.0, Previous 157757.0, Delta +155.0000)
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
