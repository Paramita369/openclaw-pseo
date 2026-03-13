---
title: "BTC NFP Reaction (2024-07-05): T+1/T+7 Up Probability"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-12"
title_variant_id: 1
title_template_key: "nfp_1"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-07-05"
asof_date: "2026-03-11"
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
freshness_days: 614
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.55
hub_baseline_median_t7: 1.0
hub_baseline_std_t7: 5.3733
hub_baseline_delta: 1.18
z_score_t7: 0.12
percentile_t7: 64.71
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:37+00:00"
event_direction: "up"
event_actual: 157748.0
event_previous: 157695.0
event_delta: 53.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 3.03
  mdd_t7: 0.0
  volatility: 0.72
  impact_t1_pct: 2.9
  impact_t7_pct: 2.18
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
chartData: [{"time": "2024-07-02", "open": 62844.41, "high": 63203.36, "low": 61752.75, "close": 62029.02}, {"time": "2024-07-03", "open": 62034.33, "high": 62187.7, "low": 59419.39, "close": 60173.92}, {"time": "2024-07-04", "open": 60147.14, "high": 60399.68, "low": 56777.8, "close": 56977.7}, {"time": "2024-07-05", "open": 57022.81, "high": 57497.15, "low": 53717.38, "close": 56662.38}, {"time": "2024-07-06", "open": 56659.07, "high": 58472.55, "low": 56038.96, "close": 58303.54}, {"time": "2024-07-07", "open": 58239.43, "high": 58371.12, "low": 55793.32, "close": 55849.11}, {"time": "2024-07-08", "open": 55849.57, "high": 58131.34, "low": 54321.02, "close": 56705.1}, {"time": "2024-07-09", "open": 56704.6, "high": 58239.2, "low": 56316.88, "close": 58009.23}, {"time": "2024-07-10", "open": 58033.88, "high": 59359.43, "low": 57178.41, "close": 57742.5}, {"time": "2024-07-11", "open": 57729.89, "high": 59299.43, "low": 57120.38, "close": 57344.91}, {"time": "2024-07-12", "open": 57341.2, "high": 58532.55, "low": 56590.18, "close": 57899.46}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2024-07-05**
- As-of date (T-1): **2026-03-11**
- Freshness age: **614 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157748.0, Previous 157695.0, Delta +53.0000)
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
