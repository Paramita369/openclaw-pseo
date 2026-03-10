---
title: "BTC Post-NFP Setup (2025-08-01): Historical Probability Lens"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-08-01"
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
quality_score: 60
sample_size: 34
freshness_days: 220
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.55
hub_baseline_median_t7: 1.0
hub_baseline_std_t7: 5.3733
hub_baseline_delta: 1.97
z_score_t7: 0.26
percentile_t7: 64.71
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 158472.0
event_previous: 158542.0
event_delta: -70.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.81
  mdd_t7: -0.7
  volatility: 3.67
  impact_t1_pct: -0.7
  impact_t7_pct: 2.97
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
    direction: "down"
    sample_size: 4
    t1:
      up: 50.0
      down: 50.0
      median: -0.01
      mean: 0.12
      sample: 4
    t7:
      up: 75.0
      down: 25.0
      median: 2.3
      mean: 1.88
      sample: 4
related_events: [{"slug": "btc-after-nfp-2026-02-06", "title": "BTC Post-NFP Setup (2026-02-06): Historical Probability Lens", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.0, "sample_size": 34}, {"slug": "btc-after-nfp-2026-01-02", "title": "NFP Print (2026-01-02) vs BTC: Quantified Directional Odds", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.0, "sample_size": 34}, {"slug": "btc-after-nfp-2025-12-05", "title": "BTC Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.0, "sample_size": 34}]
chartData: [{"time": "2025-07-29", "open": 117938.59, "high": 119273.87, "low": 116987.37, "close": 117922.15}, {"time": "2025-07-30", "open": 117921.99, "high": 118780.73, "low": 115800.83, "close": 117831.19}, {"time": "2025-07-31", "open": 117833.63, "high": 118919.98, "low": 115505.22, "close": 115758.2}, {"time": "2025-08-01", "open": 115738.95, "high": 116060.77, "low": 112724.45, "close": 113320.09}, {"time": "2025-08-02", "open": 113320.39, "high": 114021.6, "low": 112005.77, "close": 112526.91}, {"time": "2025-08-03", "open": 112525.8, "high": 114747.42, "low": 111943.8, "close": 114217.67}, {"time": "2025-08-04", "open": 114223.92, "high": 115729.47, "low": 114130.41, "close": 115071.88}, {"time": "2025-08-05", "open": 115072.19, "high": 115117.44, "low": 112701.11, "close": 114141.45}, {"time": "2025-08-06", "open": 114140.91, "high": 115737.84, "low": 113372.25, "close": 115028.0}, {"time": "2025-08-07", "open": 115030.05, "high": 117676.91, "low": 114279.71, "close": 117496.9}, {"time": "2025-08-08", "open": 117505.5, "high": 117689.2, "low": 115917.46, "close": 116688.73}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-08-01**
- As-of date (T-1): **2026-03-09**
- Freshness age: **220 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158472.0, Previous 158542.0, Delta -70.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 29.41% | 70.59% | -0.33% | -0.26% | 34 |
| T+7 | 58.82% | 41.18% | 1.0% | 1.55% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.01% | 0.12% | 4 |
| T+7 | 75.0% | 25.0% | 2.3% | 1.88% | 4 |

## Historical Distribution Summary

When NFP was **DOWN**, BTC T+1 up probability was **50.0%** (n=4).

When NFP was **DOWN**, BTC T+7 up probability was **75.0%** (n=4).

Same-direction T+7 median return: **2.3%**.

For BTC, historical NFP windows show all-history T+1 up probability of 29.41% and T+7 up probability of 58.82%. When NFP printed Down versus previous, T+1 up probability was 50.0% and T+7 up probability was 75.0% across 4 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
