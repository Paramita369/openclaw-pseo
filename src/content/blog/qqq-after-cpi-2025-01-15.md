---
title: "US CPI (2025-01-15) and QQQ: Event-Driven Return Odds"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-01-15"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 6.07
robust_score: 0.07
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 14
freshness_days: 414
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 0.54
hub_baseline_median_t7: 0.6
hub_baseline_std_t7: 2.3774
hub_baseline_delta: 2.27
z_score_t7: 0.98
percentile_t7: 84.62
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 318.961
event_previous: 317.604
event_delta: 1.357
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.8
  mdd_t7: -0.7
  volatility: 3.57
  impact_t1_pct: -0.7
  impact_t7_pct: 2.87
probabilities:
  sample_size: 14
  t1:
    up: 57.14
    down: 42.86
    median: 0.35
    mean: 0.28
    sample: 14
  t7:
    up: 53.85
    down: 46.15
    median: 0.6
    mean: 0.54
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 53.85
      down: 46.15
      median: 0.16
      mean: 0.26
      sample: 13
    t7:
      up: 53.85
      down: 46.15
      median: 0.6
      mean: 0.54
      sample: 13
related_events: [{"slug": "qqq-after-cpi-2024-05-15", "title": "2024-05-15 CPI Release: QQQ Directional Probability Snapshot", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.6, "median_t7_pct": 0.6, "sample_size": 14}, {"slug": "qqq-after-cpi-2024-09-11", "title": "US CPI (2024-09-11) and QQQ: Event-Driven Return Odds", "event_date": "2024-09-11", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 7.08, "median_t7_pct": 0.6, "sample_size": 14}, {"slug": "qqq-after-cpi-2026-02-12", "title": "QQQ CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.6, "sample_size": 14}]
chartData: [{"time": "2025-01-13", "open": 498.67, "high": 503.47, "low": 497.18, "close": 503.01}, {"time": "2025-01-14", "open": 506.17, "high": 507.59, "low": 499.06, "close": 502.53}, {"time": "2025-01-15", "open": 510.44, "high": 515.24, "low": 508.88, "close": 514.09}, {"time": "2025-01-16", "open": 516.36, "high": 516.44, "low": 510.36, "close": 510.49}, {"time": "2025-01-17", "open": 520.21, "high": 521.43, "low": 510.52, "close": 519.11}, {"time": "2025-01-21", "open": 521.83, "high": 523.32, "low": 517.44, "close": 522.15}, {"time": "2025-01-22", "open": 526.9, "high": 531.13, "low": 526.59, "close": 528.83}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2025-01-15**
- As-of date (T-1): **2026-03-05**
- Freshness age: **414 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 318.961, Previous 317.604, Delta +1.3570)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 57.14% | 42.86% | 0.35% | 0.28% | 14 |
| T+7 | 53.85% | 46.15% | 0.6% | 0.54% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.16% | 0.26% | 13 |
| T+7 | 53.85% | 46.15% | 0.6% | 0.54% | 13 |

## Historical Distribution Summary

When CPI was **UP**, QQQ T+1 up probability was **53.85%** (n=13).

When CPI was **UP**, QQQ T+7 up probability was **53.85%** (n=13).

Same-direction T+7 median return: **0.6%**.

For QQQ, historical CPI windows show all-history T+1 up probability of 57.14% and T+7 up probability of 53.85%. When CPI printed Up versus previous, T+1 up probability was 53.85% and T+7 up probability was 53.85% across 13 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
