---
title: "BTC Post-NFP Setup (2024-02-02): Historical Probability Lens"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-02-02"
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
freshness_days: 762
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 3.29
hub_baseline_median_t7: 1.54
hub_baseline_std_t7: 5.8462
hub_baseline_delta: 7.63
z_score_t7: 1.01
percentile_t7: 69.23
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 157238.0
event_previous: 157032.0
event_delta: 206.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.95
  mdd_t7: -0.45
  volatility: 9.62
  impact_t1_pct: -0.45
  impact_t7_pct: 9.17
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
chartData: [{"time": "2024-01-30", "open": 43300.23, "high": 43838.95, "low": 42711.37, "close": 42952.61}, {"time": "2024-01-31", "open": 42946.25, "high": 43717.41, "low": 42298.95, "close": 42582.61}, {"time": "2024-02-01", "open": 42569.76, "high": 43243.17, "low": 41879.19, "close": 43075.77}, {"time": "2024-02-02", "open": 43077.64, "high": 43422.49, "low": 42584.34, "close": 43185.86}, {"time": "2024-02-03", "open": 43184.96, "high": 43359.94, "low": 42890.81, "close": 42992.25}, {"time": "2024-02-04", "open": 42994.94, "high": 43097.64, "low": 42374.83, "close": 42583.58}, {"time": "2024-02-05", "open": 42577.62, "high": 43494.25, "low": 42264.82, "close": 42658.67}, {"time": "2024-02-06", "open": 42657.39, "high": 43344.15, "low": 42529.02, "close": 43084.67}, {"time": "2024-02-07", "open": 43090.02, "high": 44341.95, "low": 42775.96, "close": 44318.22}, {"time": "2024-02-08", "open": 44332.12, "high": 45575.84, "low": 44332.12, "close": 45301.57}, {"time": "2024-02-09", "open": 45297.38, "high": 48152.5, "low": 45260.82, "close": 47147.2}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2024-02-02**
- As-of date (T-1): **2026-03-05**
- Freshness age: **762 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 157238.0, Previous 157032.0, Delta +206.0000)
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
