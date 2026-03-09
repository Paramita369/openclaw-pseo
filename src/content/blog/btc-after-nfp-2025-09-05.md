---
title: "BTC NFP Reaction (2025-09-05): T+1/T+7 Up Probability"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 1
title_template_key: "nfp_1"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-09-05"
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
freshness_days: 184
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 1.55
hub_baseline_median_t7: 1.0
hub_baseline_std_t7: 5.3733
hub_baseline_delta: 3.93
z_score_t7: 0.63
percentile_t7: 70.59
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158548.0
event_previous: 158472.0
event_delta: 76.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.93
  mdd_t7: -0.39
  volatility: 5.31
  impact_t1_pct: -0.39
  impact_t7_pct: 4.93
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
chartData: [{"time": "2025-09-02", "open": 109243.07, "high": 111748.02, "low": 108454.03, "close": 111200.59}, {"time": "2025-09-03", "open": 111190.7, "high": 112600.23, "low": 110582.96, "close": 111723.21}, {"time": "2025-09-04", "open": 111718.15, "high": 112208.33, "low": 109347.23, "close": 110723.6}, {"time": "2025-09-05", "open": 110723.02, "high": 113357.49, "low": 110233.4, "close": 110650.98}, {"time": "2025-09-06", "open": 110650.57, "high": 111275.02, "low": 110024.09, "close": 110224.7}, {"time": "2025-09-07", "open": 110221.33, "high": 111591.08, "low": 110211.62, "close": 111167.62}, {"time": "2025-09-08", "open": 111163.02, "high": 112869.23, "low": 110630.61, "close": 112071.43}, {"time": "2025-09-09", "open": 112077.58, "high": 113225.44, "low": 110776.7, "close": 111530.55}, {"time": "2025-09-10", "open": 111531.25, "high": 114275.25, "low": 110940.08, "close": 113955.36}, {"time": "2025-09-11", "open": 113961.43, "high": 115522.55, "low": 113453.84, "close": 115507.54}, {"time": "2025-09-12", "open": 115507.79, "high": 116769.38, "low": 114794.48, "close": 116101.58}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-09-05**
- As-of date (T-1): **2026-03-08**
- Freshness age: **184 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158548.0, Previous 158472.0, Delta +76.0000)
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
