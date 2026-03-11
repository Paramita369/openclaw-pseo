---
title: "BTC Post-NFP Setup (2025-12-05): Historical Probability Lens"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-12-05"
asof_date: "2026-03-10"
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
freshness_days: 95
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 1.55
hub_baseline_median_t7: 1.0
hub_baseline_std_t7: 5.3733
hub_baseline_delta: -0.01
z_score_t7: -0.1
percentile_t7: 50.0
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158497.0
event_previous: 158449.0
event_delta: 48.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.88
  mdd_t7: -0.13
  volatility: 1.12
  impact_t1_pct: -0.13
  impact_t7_pct: 0.99
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
related_events: [{"slug": "btc-after-nfp-2026-02-06", "title": "BTC Post-NFP Setup (2026-02-06): Historical Probability Lens", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.0, "sample_size": 34}, {"slug": "btc-after-nfp-2026-01-02", "title": "NFP Print (2026-01-02) vs BTC: Quantified Directional Odds", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.0, "sample_size": 34}, {"slug": "btc-after-nfp-2025-11-07", "title": "BTC Post-NFP Setup (2025-11-07): Historical Probability Lens", "event_date": "2025-11-07", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.0, "sample_size": 34}]
chartData: [{"time": "2025-12-02", "open": 86322.54, "high": 92316.63, "low": 86202.2, "close": 91350.2}, {"time": "2025-12-03", "open": 91345.09, "high": 94060.77, "low": 91056.39, "close": 93527.8}, {"time": "2025-12-04", "open": 93454.26, "high": 94038.24, "low": 90976.1, "close": 92141.62}, {"time": "2025-12-05", "open": 92133.65, "high": 92702.64, "low": 88152.14, "close": 89387.76}, {"time": "2025-12-06", "open": 89389.36, "high": 90267.46, "low": 88951.66, "close": 89272.38}, {"time": "2025-12-07", "open": 89277.81, "high": 91740.84, "low": 87799.56, "close": 90405.64}, {"time": "2025-12-08", "open": 90424.59, "high": 92267.12, "low": 89644.89, "close": 90640.2}, {"time": "2025-12-09", "open": 90639.7, "high": 94601.57, "low": 89586.98, "close": 92691.71}, {"time": "2025-12-10", "open": 92695.23, "high": 94477.16, "low": 91640.13, "close": 92020.95}, {"time": "2025-12-11", "open": 92011.3, "high": 93554.27, "low": 89335.3, "close": 92511.34}, {"time": "2025-12-12", "open": 92513.66, "high": 92747.93, "low": 89532.6, "close": 90270.41}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-12-05**
- As-of date (T-1): **2026-03-10**
- Freshness age: **95 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158497.0, Previous 158449.0, Delta +48.0000)
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
