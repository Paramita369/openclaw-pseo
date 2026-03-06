---
title: "US CPI (2025-02-12) and ETH: Event-Driven Return Odds"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-02-12"
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
quality_score: 90
sample_size: 14
freshness_days: 386
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.26
hub_baseline_median_t7: -0.39
hub_baseline_std_t7: 11.002
hub_baseline_delta: -0.38
z_score_t7: -0.09
percentile_t7: 50.0
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 319.679
event_previous: 318.961
event_delta: 0.718
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -3.8
  mdd_t7: -2.23
  volatility: 1.46
  impact_t1_pct: -2.23
  impact_t7_pct: -0.77
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
chartData: [{"time": "2025-02-09", "open": 2632.58, "high": 2695.22, "low": 2530.44, "close": 2628.72}, {"time": "2025-02-10", "open": 2628.65, "high": 2692.81, "low": 2564.02, "close": 2661.17}, {"time": "2025-02-11", "open": 2661.32, "high": 2724.9, "low": 2565.4, "close": 2602.78}, {"time": "2025-02-12", "open": 2602.83, "high": 2794.87, "low": 2551.17, "close": 2736.9}, {"time": "2025-02-13", "open": 2737.03, "high": 2756.44, "low": 2615.67, "close": 2675.9}, {"time": "2025-02-14", "open": 2675.94, "high": 2790.02, "low": 2666.27, "close": 2726.09}, {"time": "2025-02-15", "open": 2726.07, "high": 2738.68, "low": 2668.53, "close": 2693.56}, {"time": "2025-02-16", "open": 2693.56, "high": 2724.1, "low": 2655.3, "close": 2663.32}, {"time": "2025-02-17", "open": 2663.23, "high": 2848.78, "low": 2640.18, "close": 2743.2}, {"time": "2025-02-18", "open": 2743.02, "high": 2754.68, "low": 2606.9, "close": 2669.34}, {"time": "2025-02-19", "open": 2669.21, "high": 2735.92, "low": 2656.38, "close": 2715.77}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2025-02-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **386 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 319.679, Previous 318.961, Delta +0.7180)
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
