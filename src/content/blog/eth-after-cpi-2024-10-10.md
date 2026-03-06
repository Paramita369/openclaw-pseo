---
title: "US CPI (2024-10-10) and ETH: Event-Driven Return Odds"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-10-10"
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
freshness_days: 511
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.26
hub_baseline_median_t7: -0.39
hub_baseline_std_t7: 11.002
hub_baseline_delta: 9.64
z_score_t7: 0.82
percentile_t7: 78.57
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 315.631
event_previous: 314.732
event_delta: 0.899
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 1.31
  mdd_t7: 0.0
  volatility: 7.04
  impact_t1_pct: 2.21
  impact_t7_pct: 9.25
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
chartData: [{"time": "2024-10-07", "open": 2439.94, "high": 2520.41, "low": 2405.13, "close": 2421.8}, {"time": "2024-10-08", "open": 2421.98, "high": 2464.13, "low": 2400.51, "close": 2439.84}, {"time": "2024-10-09", "open": 2439.84, "high": 2470.91, "low": 2350.95, "close": 2368.28}, {"time": "2024-10-10", "open": 2368.27, "high": 2417.29, "low": 2329.78, "close": 2383.86}, {"time": "2024-10-11", "open": 2383.94, "high": 2470.4, "low": 2380.5, "close": 2436.51}, {"time": "2024-10-12", "open": 2436.52, "high": 2488.24, "low": 2434.2, "close": 2476.52}, {"time": "2024-10-13", "open": 2476.52, "high": 2484.13, "low": 2436.97, "close": 2467.68}, {"time": "2024-10-14", "open": 2467.65, "high": 2652.88, "low": 2443.55, "close": 2628.9}, {"time": "2024-10-15", "open": 2629.02, "high": 2685.17, "low": 2537.94, "close": 2606.02}, {"time": "2024-10-16", "open": 2606.02, "high": 2644.85, "low": 2589.61, "close": 2611.1}, {"time": "2024-10-17", "open": 2611.19, "high": 2646.87, "low": 2577.31, "close": 2604.27}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-10-10**
- As-of date (T-1): **2026-03-05**
- Freshness age: **511 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 315.631, Previous 314.732, Delta +0.8990)
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
