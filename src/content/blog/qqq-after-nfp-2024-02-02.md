---
title: "NFP Print (2024-02-02) vs QQQ: Quantified Directional Odds"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 4
title_template_key: "nfp_4"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-02-02"
asof_date: "2026-03-09"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 4.14
robust_score: -1.86
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 34
freshness_days: 766
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 1.03
hub_baseline_median_t7: 0.12
hub_baseline_std_t7: 2.5414
hub_baseline_delta: 1.75
z_score_t7: 0.33
percentile_t7: 70.59
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 157238.0
event_previous: 157032.0
event_delta: 206.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -0.27
  mdd_t7: -2.68
  volatility: 1.99
  impact_t1_pct: -0.12
  impact_t7_pct: 1.87
probabilities:
  sample_size: 34
  t1:
    up: 57.14
    down: 42.86
    median: 0.15
    mean: -0.12
    sample: 21
  t7:
    up: 50.0
    down: 50.0
    median: 0.12
    mean: 1.03
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 18
    t1:
      up: 50.0
      down: 50.0
      median: -0.05
      mean: -0.29
      sample: 18
    t7:
      up: 50.0
      down: 50.0
      median: 0.12
      mean: 1.05
      sample: 30
related_events: [{"slug": "qqq-after-nfp-2025-01-10", "title": "2025-01-10 Nonfarm Payrolls: QQQ Historical Win Rate", "event_date": "2025-01-10", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.64, "median_t7_pct": 0.12, "sample_size": 34}, {"slug": "qqq-after-nfp-2024-12-06", "title": "QQQ After NFP (2024-12-06): Event Probability and Median Return", "event_date": "2024-12-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.77, "median_t7_pct": 0.12, "sample_size": 34}, {"slug": "qqq-after-nfp-2024-08-02", "title": "QQQ After NFP (2024-08-02): Event Probability and Median Return", "event_date": "2024-08-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.35, "median_t7_pct": 0.12, "sample_size": 34}]
chartData: [{"time": "2024-01-30", "open": 422.43, "high": 423.01, "low": 419.74, "close": 420.65}, {"time": "2024-01-31", "open": 416.25, "high": 418.25, "low": 412.24, "close": 412.42}, {"time": "2024-02-01", "open": 414.22, "high": 417.77, "low": 413.25, "close": 417.27}, {"time": "2024-02-02", "open": 419.17, "high": 425.54, "low": 418.17, "close": 424.32}, {"time": "2024-02-05", "open": 424.38, "high": 424.92, "low": 420.36, "close": 423.77}, {"time": "2024-02-06", "open": 424.92, "high": 425.52, "low": 420.57, "close": 422.92}, {"time": "2024-02-07", "open": 425.71, "high": 428.1, "low": 424.4, "close": 427.27}, {"time": "2024-02-08", "open": 427.39, "high": 428.82, "low": 426.71, "close": 428.06}, {"time": "2024-02-09", "open": 429.2, "high": 433.07, "low": 428.41, "close": 432.28}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2024-02-02**
- As-of date (T-1): **2026-03-09**
- Freshness age: **766 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157238.0, Previous 157032.0, Delta +206.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 57.14% | 42.86% | 0.15% | -0.12% | 21 |
| T+7 | 50.0% | 50.0% | 0.12% | 1.03% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.05% | -0.29% | 18 |
| T+7 | 50.0% | 50.0% | 0.12% | 1.05% | 30 |

## Historical Distribution Summary

When NFP was **UP**, QQQ T+1 up probability was **50.0%** (n=18).

When NFP was **UP**, QQQ T+7 up probability was **50.0%** (n=30).

Same-direction T+7 median return: **0.12%**.

For QQQ, historical NFP windows show all-history T+1 up probability of 57.14% and T+7 up probability of 50.0%. When NFP printed Up versus previous, T+1 up probability was 50.0% and T+7 up probability was 50.0% across 18 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
