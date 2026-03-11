---
title: "NFP Print (2024-04-05) vs BTC: Quantified Directional Odds"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 4
title_template_key: "nfp_4"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-04-05"
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
freshness_days: 704
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 1.55
hub_baseline_median_t7: 1.0
hub_baseline_std_t7: 5.3733
hub_baseline_delta: -1.95
z_score_t7: -0.47
percentile_t7: 29.41
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 157530.0
event_previous: 157466.0
event_delta: 64.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -4.3
  mdd_t7: -2.47
  volatility: 2.51
  impact_t1_pct: 1.56
  impact_t7_pct: -0.95
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
chartData: [{"time": "2024-04-02", "open": 69705.02, "high": 69708.38, "low": 64586.59, "close": 65446.97}, {"time": "2024-04-03", "open": 65446.67, "high": 66914.32, "low": 64559.9, "close": 65980.81}, {"time": "2024-04-04", "open": 65975.7, "high": 69291.26, "low": 65113.8, "close": 68508.84}, {"time": "2024-04-05", "open": 68515.76, "high": 68725.76, "low": 66011.48, "close": 67837.64}, {"time": "2024-04-06", "open": 67840.57, "high": 69629.6, "low": 67491.72, "close": 68896.11}, {"time": "2024-04-07", "open": 68897.11, "high": 70284.43, "low": 68851.63, "close": 69362.55}, {"time": "2024-04-08", "open": 69362.55, "high": 72715.36, "low": 69064.24, "close": 71631.36}, {"time": "2024-04-09", "open": 71632.5, "high": 71742.51, "low": 68212.92, "close": 69139.02}, {"time": "2024-04-10", "open": 69140.24, "high": 71093.43, "low": 67503.56, "close": 70587.88}, {"time": "2024-04-11", "open": 70575.73, "high": 71256.23, "low": 69571.81, "close": 70060.61}, {"time": "2024-04-12", "open": 70061.38, "high": 71222.74, "low": 65254.84, "close": 67195.87}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2024-04-05**
- As-of date (T-1): **2026-03-10**
- Freshness age: **704 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157530.0, Previous 157466.0, Delta +64.0000)
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
