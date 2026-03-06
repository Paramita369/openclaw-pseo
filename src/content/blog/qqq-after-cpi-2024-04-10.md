---
title: "2024-04-10 CPI Release: QQQ Directional Probability Snapshot"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 4
title_template_key: "cpi_4"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-04-10"
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
freshness_days: 694
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.54
hub_baseline_median_t7: 0.6
hub_baseline_std_t7: 2.3774
hub_baseline_delta: -3.46
z_score_t7: -1.43
percentile_t7: 7.69
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 313.023
event_previous: 312.345
event_delta: 0.678
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -7.4
  mdd_t7: -4.39
  volatility: 4.46
  impact_t1_pct: 1.6
  impact_t7_pct: -2.86
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
chartData: [{"time": "2024-04-08", "open": 437.17, "high": 438.24, "low": 434.98, "close": 436.36}, {"time": "2024-04-09", "open": 438.7, "high": 438.98, "low": 433.23, "close": 437.98}, {"time": "2024-04-10", "open": 432.8, "high": 435.02, "low": 432.08, "close": 434.15}, {"time": "2024-04-11", "open": 436.03, "high": 442.04, "low": 433.75, "close": 441.09}, {"time": "2024-04-12", "open": 436.86, "high": 437.99, "low": 432.68, "close": 434.06}, {"time": "2024-04-15", "open": 437.81, "high": 437.9, "low": 426.07, "close": 426.91}, {"time": "2024-04-16", "open": 426.76, "high": 429.59, "low": 425.57, "close": 426.95}, {"time": "2024-04-17", "open": 428.94, "high": 428.96, "low": 420.81, "close": 421.75}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2024-04-10**
- As-of date (T-1): **2026-03-05**
- Freshness age: **694 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 313.023, Previous 312.345, Delta +0.6780)
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
