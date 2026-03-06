---
title: "BTC NFP Reaction (2024-10-04): T+1/T+7 Up Probability"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 1
title_template_key: "nfp_1"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-10-04"
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
freshness_days: 517
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 3.29
hub_baseline_median_t7: 1.54
hub_baseline_std_t7: 5.8462
hub_baseline_delta: -0.93
z_score_t7: -0.46
percentile_t7: 46.15
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 157945.0
event_previous: 157912.0
event_delta: 33.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.07
  mdd_t7: 0.0
  volatility: 0.57
  impact_t1_pct: 0.04
  impact_t7_pct: 0.61
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
chartData: [{"time": "2024-10-01", "open": 63335.61, "high": 64110.98, "low": 60189.28, "close": 60837.01}, {"time": "2024-10-02", "open": 60836.32, "high": 62357.69, "low": 59996.95, "close": 60632.79}, {"time": "2024-10-03", "open": 60632.48, "high": 61469.04, "low": 59878.8, "close": 60759.4}, {"time": "2024-10-04", "open": 60754.62, "high": 62465.99, "low": 60459.94, "close": 62067.48}, {"time": "2024-10-05", "open": 62067.61, "high": 62371.02, "low": 61689.58, "close": 62089.95}, {"time": "2024-10-06", "open": 62084.99, "high": 62959.57, "low": 61833.15, "close": 62818.95}, {"time": "2024-10-07", "open": 62819.11, "high": 64443.71, "low": 62152.55, "close": 62236.66}, {"time": "2024-10-08", "open": 62221.64, "high": 63174.3, "low": 61843.56, "close": 62131.97}, {"time": "2024-10-09", "open": 62131.73, "high": 62508.84, "low": 60314.61, "close": 60582.1}, {"time": "2024-10-10", "open": 60581.93, "high": 61236.72, "low": 58895.21, "close": 60274.5}, {"time": "2024-10-11", "open": 60275.46, "high": 63400.87, "low": 60046.12, "close": 62445.09}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2024-10-04**
- As-of date (T-1): **2026-03-05**
- Freshness age: **517 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 157945.0, Previous 157912.0, Delta +33.0000)
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
