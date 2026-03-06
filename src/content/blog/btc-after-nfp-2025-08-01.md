---
title: "BTC Post-NFP Setup (2025-08-01): Historical Probability Lens"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-08-01"
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
quality_score: 40
sample_size: 13
freshness_days: 216
freshness_status: "stale"
index_tier: "C"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 3.29
hub_baseline_median_t7: 1.54
hub_baseline_std_t7: 5.8462
hub_baseline_delta: 1.75
z_score_t7: 0.0
percentile_t7: 61.54
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "none"
canonical_url: ""
robots_directive: "noindex,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "down"
event_actual: 158472.0
event_previous: 158542.0
event_delta: -70.0
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
chartData: [{"time": "2025-07-29", "open": 117938.59, "high": 119273.87, "low": 116987.37, "close": 117922.15}, {"time": "2025-07-30", "open": 117921.99, "high": 118780.73, "low": 115800.83, "close": 117831.19}, {"time": "2025-07-31", "open": 117833.63, "high": 118919.98, "low": 115505.22, "close": 115758.2}, {"time": "2025-08-01", "open": 115738.95, "high": 116060.77, "low": 112724.45, "close": 113320.09}, {"time": "2025-08-02", "open": 113320.39, "high": 114021.6, "low": 112005.77, "close": 112526.91}, {"time": "2025-08-03", "open": 112525.8, "high": 114747.42, "low": 111943.8, "close": 114217.67}, {"time": "2025-08-04", "open": 114223.92, "high": 115729.47, "low": 114130.41, "close": 115071.88}, {"time": "2025-08-05", "open": 115072.19, "high": 115117.44, "low": 112701.11, "close": 114141.45}, {"time": "2025-08-06", "open": 114140.91, "high": 115737.84, "low": 113372.25, "close": 115028.0}, {"time": "2025-08-07", "open": 115030.05, "high": 117676.91, "low": 114279.71, "close": 117496.9}, {"time": "2025-08-08", "open": 117505.5, "high": 117689.2, "low": 115917.46, "close": 116688.73}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-08-01**
- As-of date (T-1): **2026-03-05**
- Freshness age: **216 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158472.0, Previous 158542.0, Delta -70.0000)
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
