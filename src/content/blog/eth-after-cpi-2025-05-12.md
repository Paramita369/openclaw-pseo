---
title: "US CPI (2025-05-12) and ETH: Event-Driven Return Odds"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-05-12"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -5.57
robust_score: -11.57
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 70
sample_size: 14
freshness_days: 297
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 0.26
hub_baseline_median_t7: -0.39
hub_baseline_std_t7: 11.002
hub_baseline_delta: 0.65
z_score_t7: 0.0
percentile_t7: 57.14
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 320.62
event_previous: 320.302
event_delta: 0.318
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.33
  mdd_t7: -0.52
  volatility: 0.78
  impact_t1_pct: -0.52
  impact_t7_pct: 0.26
probabilities:
  sample_size: 14
  t1:
    up: 50.0
    down: 50.0
    median: -0.22
    mean: -0.52
    sample: 14
  t7:
    up: 42.86
    down: 57.14
    median: -0.39
    mean: 0.26
    sample: 14
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 53.85
      down: 46.15
      median: 0.66
      mean: -0.36
      sample: 13
    t7:
      up: 46.15
      down: 53.85
      median: -0.77
      mean: 0.28
      sample: 13
related_events: [{"slug": "eth-after-cpi-2024-06-12", "title": "ETH Reaction to US CPI (2024-06-12): Quant Probability Breakdown", "event_date": "2024-06-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.22, "median_t7_pct": -0.39, "sample_size": 14}, {"slug": "eth-after-cpi-2026-02-12", "title": "ETH CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.39, "sample_size": 14}, {"slug": "eth-after-cpi-2026-01-12", "title": "2026-01-12 CPI Release: ETH Directional Probability Snapshot", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.39, "sample_size": 14}]
chartData: [{"time": "2025-05-09", "open": 2206.13, "high": 2486.01, "low": 2186.05, "close": 2345.51}, {"time": "2025-05-10", "open": 2345.76, "high": 2597.54, "low": 2320.24, "close": 2582.42}, {"time": "2025-05-11", "open": 2582.71, "high": 2603.26, "low": 2441.73, "close": 2510.24}, {"time": "2025-05-12", "open": 2510.29, "high": 2620.9, "low": 2411.59, "close": 2496.4}, {"time": "2025-05-13", "open": 2496.34, "high": 2736.89, "low": 2418.33, "close": 2680.13}, {"time": "2025-05-14", "open": 2680.26, "high": 2721.95, "low": 2549.69, "close": 2610.06}, {"time": "2025-05-15", "open": 2610.03, "high": 2645.07, "low": 2482.21, "close": 2546.86}, {"time": "2025-05-16", "open": 2547.06, "high": 2645.61, "low": 2532.03, "close": 2536.3}, {"time": "2025-05-17", "open": 2536.3, "high": 2537.78, "low": 2449.07, "close": 2475.75}, {"time": "2025-05-18", "open": 2475.77, "high": 2585.7, "low": 2344.67, "close": 2498.23}, {"time": "2025-05-19", "open": 2498.8, "high": 2545.46, "low": 2353.43, "close": 2529.17}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2025-05-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **297 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 320.62, Previous 320.302, Delta +0.3180)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.22% | -0.52% | 14 |
| T+7 | 42.86% | 57.14% | -0.39% | 0.26% | 14 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.66% | -0.36% | 13 |
| T+7 | 46.15% | 53.85% | -0.77% | 0.28% | 13 |

## Historical Distribution Summary

When CPI was **UP**, ETH T+1 up probability was **53.85%** (n=13).

When CPI was **UP**, ETH T+7 up probability was **46.15%** (n=13).

Same-direction T+7 median return: **-0.77%**.

For ETH, historical CPI windows show all-history T+1 up probability of 50.0% and T+7 up probability of 42.86%. When CPI printed Up versus previous, T+1 up probability was 53.85% and T+7 up probability was 46.15% across 13 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
