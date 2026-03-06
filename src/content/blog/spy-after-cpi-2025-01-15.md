---
title: "SPY CPI Win Rate (2025-01-15): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-01-15"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 19.75
robust_score: 13.75
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
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.51
hub_baseline_median_t7: 1.08
hub_baseline_std_t7: 1.8429
hub_baseline_delta: 1.22
z_score_t7: 0.97
percentile_t7: 92.31
narrative_trigger: "extreme_outperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 318.961
event_previous: 317.604
event_delta: 1.357
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.92
  mdd_t7: -0.19
  volatility: 2.49
  impact_t1_pct: -0.19
  impact_t7_pct: 2.3
probabilities:
  sample_size: 14
  t1:
    up: 64.29
    down: 35.71
    median: 0.15
    mean: 0.26
    sample: 14
  t7:
    up: 76.92
    down: 23.08
    median: 1.08
    mean: 0.51
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 61.54
      down: 38.46
      median: 0.09
      mean: 0.26
      sample: 13
    t7:
      up: 76.92
      down: 23.08
      median: 1.08
      mean: 0.51
      sample: 13
related_events: [{"slug": "spy-after-cpi-2024-03-12", "title": "SPY CPI Win Rate (2024-03-12): Historical T+1/T+7 Probability", "event_date": "2024-03-12", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 3.94, "median_t7_pct": 1.08, "sample_size": 14}, {"slug": "spy-after-cpi-2024-11-14", "title": "2024-11-14 CPI Release: SPY Directional Probability Snapshot", "event_date": "2024-11-14", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.43, "median_t7_pct": 1.08, "sample_size": 14}, {"slug": "spy-after-cpi-2024-05-15", "title": "2024-05-15 CPI Release: SPY Directional Probability Snapshot", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.37, "median_t7_pct": 1.08, "sample_size": 14}]
chartData: [{"time": "2025-01-13", "open": 569.09, "high": 575.0, "low": 568.67, "close": 574.64}, {"time": "2025-01-14", "open": 577.58, "high": 578.21, "low": 571.64, "close": 575.43}, {"time": "2025-01-15", "open": 583.48, "high": 587.05, "low": 582.36, "close": 585.9}, {"time": "2025-01-16", "open": 587.27, "high": 587.45, "low": 584.07, "close": 584.77}, {"time": "2025-01-17", "open": 590.03, "high": 592.4, "low": 588.7, "close": 590.64}, {"time": "2025-01-21", "open": 593.7, "high": 596.06, "low": 591.72, "close": 596.05}, {"time": "2025-01-22", "open": 598.89, "high": 600.77, "low": 598.33, "close": 599.4}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
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
| T+1 | 64.29% | 35.71% | 0.15% | 0.26% | 14 |
| T+7 | 76.92% | 23.08% | 1.08% | 0.51% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 61.54% | 38.46% | 0.09% | 0.26% | 13 |
| T+7 | 76.92% | 23.08% | 1.08% | 0.51% | 13 |

## Historical Distribution Summary

When CPI was **UP**, SPY T+1 up probability was **61.54%** (n=13).

When CPI was **UP**, SPY T+7 up probability was **76.92%** (n=13).

Same-direction T+7 median return: **1.08%**.

For SPY, historical CPI windows show all-history T+1 up probability of 64.29% and T+7 up probability of 76.92%. When CPI printed Up versus previous, T+1 up probability was 61.54% and T+7 up probability was 76.92% across 13 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
