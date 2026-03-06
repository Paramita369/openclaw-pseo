---
title: "BTC After NFP (2025-01-10): Event Probability and Median Return"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "nfp_3"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-01-10"
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
quality_score: 60
sample_size: 13
freshness_days: 419
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 3.29
hub_baseline_median_t7: 1.54
hub_baseline_std_t7: 5.8462
hub_baseline_delta: 8.77
z_score_t7: 1.2
percentile_t7: 92.31
narrative_trigger: "extreme_outperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "down"
event_actual: 158268.0
event_previous: 158316.0
event_delta: -48.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.99
  mdd_t7: -0.14
  volatility: 10.45
  impact_t1_pct: -0.14
  impact_t7_pct: 10.31
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
    direction: "down"
    sample_size: 1
    t1:
      up: 0.0
      down: 100.0
      median: -0.14
      mean: -0.14
      sample: 1
    t7:
      up: 100.0
      down: 0.0
      median: 10.31
      mean: 10.31
      sample: 1
related_events: [{"slug": "btc-after-nfp-2026-02-06", "title": "BTC Post-NFP Setup (2026-02-06): Historical Probability Lens", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.54, "sample_size": 13}, {"slug": "btc-after-nfp-2026-01-02", "title": "NFP Print (2026-01-02) vs BTC: Quantified Directional Odds", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.54, "sample_size": 13}, {"slug": "btc-after-nfp-2025-12-05", "title": "BTC Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.54, "sample_size": 13}]
chartData: [{"time": "2025-01-07", "open": 102248.85, "high": 102712.48, "low": 96132.88, "close": 96922.7}, {"time": "2025-01-08", "open": 96924.16, "high": 97258.32, "low": 92525.84, "close": 95043.52}, {"time": "2025-01-09", "open": 95043.48, "high": 95349.72, "low": 91220.84, "close": 92484.04}, {"time": "2025-01-10", "open": 92494.49, "high": 95770.61, "low": 92250.09, "close": 94701.45}, {"time": "2025-01-11", "open": 94700.84, "high": 94977.69, "low": 93840.05, "close": 94566.59}, {"time": "2025-01-12", "open": 94565.73, "high": 95367.54, "low": 93712.51, "close": 94488.44}, {"time": "2025-01-13", "open": 94488.89, "high": 95837.0, "low": 89260.1, "close": 94516.52}, {"time": "2025-01-14", "open": 94519.01, "high": 97352.66, "low": 94322.16, "close": 96534.05}, {"time": "2025-01-15", "open": 96534.05, "high": 100697.23, "low": 96501.64, "close": 100504.49}, {"time": "2025-01-16", "open": 100505.3, "high": 100781.59, "low": 97364.45, "close": 99756.91}, {"time": "2025-01-17", "open": 100025.77, "high": 105884.23, "low": 99948.91, "close": 104462.04}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
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
| T+1 | 38.46% | 61.54% | -0.05% | 0.25% | 13 |
| T+7 | 61.54% | 38.46% | 1.54% | 3.29% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | -0.14% | -0.14% | 1 |
| T+7 | 100.0% | 0.0% | 10.31% | 10.31% | 1 |

## Historical Distribution Summary

When NFP was **DOWN**, BTC T+1 up probability was **0.0%** (n=1).

When NFP was **DOWN**, BTC T+7 up probability was **100.0%** (n=1).

Same-direction T+7 median return: **10.31%**.

For BTC, historical NFP windows show all-history T+1 up probability of 38.46% and T+7 up probability of 61.54%. When NFP printed Down versus previous, T+1 up probability was 0.0% and T+7 up probability was 100.0% across 1 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
