---
title: "2024-06-07 Nonfarm Payrolls: QQQ Historical Win Rate"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-06-07"
asof_date: "2026-03-08"
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
freshness_days: 639
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.03
hub_baseline_median_t7: 0.12
hub_baseline_std_t7: 2.5414
hub_baseline_delta: 3.39
z_score_t7: 0.97
percentile_t7: 85.29
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:37+00:00"
event_direction: "up"
event_actual: 157695.0
event_previous: 157608.0
event_delta: 87.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.97
  mdd_t7: -0.12
  volatility: 3.63
  impact_t1_pct: -0.12
  impact_t7_pct: 3.51
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
related_events: [{"slug": "qqq-after-nfp-2025-01-10", "title": "2025-01-10 Nonfarm Payrolls: QQQ Historical Win Rate", "event_date": "2025-01-10", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.64, "median_t7_pct": 1.51, "sample_size": 13}, {"slug": "qqq-after-nfp-2024-12-06", "title": "QQQ After NFP (2024-12-06): Event Probability and Median Return", "event_date": "2024-12-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.77, "median_t7_pct": 1.51, "sample_size": 13}, {"slug": "qqq-after-nfp-2024-08-02", "title": "QQQ After NFP (2024-08-02): Event Probability and Median Return", "event_date": "2024-08-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.35, "median_t7_pct": 1.51, "sample_size": 13}]
chartData: [{"time": "2024-06-04", "open": 448.52, "high": 451.2, "low": 446.79, "close": 450.0}, {"time": "2024-06-05", "open": 453.58, "high": 459.15, "low": 450.04, "close": 459.07}, {"time": "2024-06-06", "open": 459.76, "high": 460.07, "low": 457.75, "close": 458.91}, {"time": "2024-06-07", "open": 458.55, "high": 461.26, "low": 457.4, "close": 458.51}, {"time": "2024-06-10", "open": 457.38, "high": 460.72, "low": 457.09, "close": 460.36}, {"time": "2024-06-11", "open": 459.08, "high": 463.64, "low": 457.59, "close": 463.52}, {"time": "2024-06-12", "open": 467.45, "high": 471.92, "low": 466.76, "close": 469.59}, {"time": "2024-06-13", "open": 473.13, "high": 473.79, "low": 469.86, "close": 472.14}, {"time": "2024-06-14", "open": 471.94, "high": 474.65, "low": 471.47, "close": 474.58}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2024-06-07**
- As-of date (T-1): **2026-03-08**
- Freshness age: **639 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157695.0, Previous 157608.0, Delta +87.0000)
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
