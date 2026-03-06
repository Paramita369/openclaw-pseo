---
title: "ETH After CPI (2025-04-12): Up/Down Odds and Median Returns"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "cpi_5"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-04-12"
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
freshness_days: 327
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
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
event_actual: 320.302
event_previous: 319.785
event_delta: 0.517
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
chartData: [{"time": "2025-04-09", "open": 1472.6, "high": 1687.19, "low": 1386.8, "close": 1668.04}, {"time": "2025-04-10", "open": 1668.2, "high": 1669.39, "low": 1474.91, "close": 1522.52}, {"time": "2025-04-11", "open": 1522.47, "high": 1587.54, "low": 1505.0, "close": 1567.15}, {"time": "2025-04-12", "open": 1567.16, "high": 1666.02, "low": 1546.82, "close": 1643.53}, {"time": "2025-04-13", "open": 1643.5, "high": 1648.29, "low": 1564.84, "close": 1596.69}, {"time": "2025-04-14", "open": 1596.88, "high": 1689.86, "low": 1596.09, "close": 1622.77}, {"time": "2025-04-15", "open": 1622.77, "high": 1659.84, "low": 1585.23, "close": 1588.63}, {"time": "2025-04-16", "open": 1589.03, "high": 1610.78, "low": 1540.03, "close": 1578.11}, {"time": "2025-04-17", "open": 1578.01, "high": 1615.31, "low": 1564.2, "close": 1582.55}, {"time": "2025-04-18", "open": 1582.4, "high": 1599.42, "low": 1573.9, "close": 1588.92}, {"time": "2025-04-19", "open": 1588.97, "high": 1629.05, "low": 1585.47, "close": 1612.92}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2025-04-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **327 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 320.302, Previous 319.785, Delta +0.5170)
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
