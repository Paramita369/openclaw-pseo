---
title: "2024-06-07 Nonfarm Payrolls: BTC Historical Win Rate"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-06-07"
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
freshness_days: 636
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 3.29
hub_baseline_median_t7: 1.54
hub_baseline_std_t7: 5.8462
hub_baseline_delta: -6.34
z_score_t7: -1.38
percentile_t7: 7.69
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 157695.0
event_previous: 157608.0
event_delta: 87.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -1.01
  mdd_t7: -4.8
  volatility: 4.75
  impact_t1_pct: -0.05
  impact_t7_pct: -4.8
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
chartData: [{"time": "2024-06-04", "open": 68804.57, "high": 71047.41, "low": 68564.64, "close": 70567.77}, {"time": "2024-06-05", "open": 70568.35, "high": 71735.41, "low": 70390.71, "close": 71082.82}, {"time": "2024-06-06", "open": 71082.84, "high": 71625.73, "low": 70119.12, "close": 70757.16}, {"time": "2024-06-07", "open": 70759.19, "high": 71907.85, "low": 68507.26, "close": 69342.59}, {"time": "2024-06-08", "open": 69324.18, "high": 69533.32, "low": 69210.74, "close": 69305.77}, {"time": "2024-06-09", "open": 69297.49, "high": 69817.52, "low": 69160.84, "close": 69647.99}, {"time": "2024-06-10", "open": 69644.31, "high": 70146.07, "low": 69232.42, "close": 69512.28}, {"time": "2024-06-11", "open": 69508.08, "high": 69549.41, "low": 66123.6, "close": 67332.03}, {"time": "2024-06-12", "open": 67321.38, "high": 69977.89, "low": 66902.45, "close": 68241.19}, {"time": "2024-06-13", "open": 68243.1, "high": 68365.78, "low": 66304.56, "close": 66756.4}, {"time": "2024-06-14", "open": 66747.57, "high": 67294.65, "low": 65056.89, "close": 66011.09}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2024-06-07**
- As-of date (T-1): **2026-03-05**
- Freshness age: **636 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 157695.0, Previous 157608.0, Delta +87.0000)
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
