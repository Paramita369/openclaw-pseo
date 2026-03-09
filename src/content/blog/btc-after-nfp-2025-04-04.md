---
title: "BTC Post-NFP Setup (2025-04-04): Historical Probability Lens"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-04-04"
asof_date: "2026-03-08"
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
freshness_days: 338
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.55
hub_baseline_median_t7: 1.0
hub_baseline_std_t7: 5.3733
hub_baseline_delta: -1.52
z_score_t7: -0.39
percentile_t7: 38.24
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158485.0
event_previous: 158377.0
event_delta: 108.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -4.36
  mdd_t7: -0.52
  volatility: 0.12
  impact_t1_pct: -0.4
  impact_t7_pct: -0.52
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
chartData: [{"time": "2025-04-01", "open": 82551.92, "high": 85487.37, "low": 82429.36, "close": 85169.17}, {"time": "2025-04-02", "open": 85180.61, "high": 88466.95, "low": 82343.54, "close": 82485.71}, {"time": "2025-04-03", "open": 82487.48, "high": 83909.3, "low": 81282.1, "close": 83102.83}, {"time": "2025-04-04", "open": 83100.25, "high": 84696.15, "low": 81670.75, "close": 83843.8}, {"time": "2025-04-05", "open": 83844.7, "high": 84207.02, "low": 82377.73, "close": 83504.8}, {"time": "2025-04-06", "open": 83504.51, "high": 83704.72, "low": 77097.74, "close": 78214.48}, {"time": "2025-04-07", "open": 78221.34, "high": 81119.06, "low": 74436.68, "close": 79235.34}, {"time": "2025-04-08", "open": 79218.48, "high": 80823.89, "low": 76198.02, "close": 76271.95}, {"time": "2025-04-09", "open": 76273.56, "high": 83541.0, "low": 74589.67, "close": 82573.95}, {"time": "2025-04-10", "open": 82565.98, "high": 82700.93, "low": 78456.13, "close": 79626.14}, {"time": "2025-04-11", "open": 79625.05, "high": 84247.48, "low": 78936.32, "close": 83404.84}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-04-04**
- As-of date (T-1): **2026-03-08**
- Freshness age: **338 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158485.0, Previous 158377.0, Delta +108.0000)
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
