---
title: "BTC After CPI (2025-01-15): Up/Down Odds and Median Returns"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 5
title_template_key: "cpi_5"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-01-15"
asof_date: "2026-03-08"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 6.62
robust_score: 0.62
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 39
freshness_days: 417
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: 2.02
z_score_t7: 0.41
percentile_t7: 69.23
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:04:03+00:00"
event_direction: "up"
event_actual: 318.961
event_previous: 317.604
event_delta: 1.357
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.81
  mdd_t7: -0.74
  volatility: 3.87
  impact_t1_pct: -0.74
  impact_t7_pct: 3.13
probabilities:
  sample_size: 39
  t1:
    up: 58.97
    down: 41.03
    median: 0.51
    mean: 0.37
    sample: 39
  t7:
    up: 53.85
    down: 46.15
    median: 1.11
    mean: 0.44
    sample: 39
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.53
      mean: 0.44
      sample: 38
    t7:
      up: 55.26
      down: 44.74
      median: 1.26
      mean: 0.58
      sample: 38
related_events: [{"slug": "btc-after-cpi-2024-08-14", "title": "BTC Reaction to US CPI (2024-08-14): Quant Probability Breakdown", "event_date": "2024-08-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.86, "median_t7_pct": 3.64, "sample_size": 14}, {"slug": "btc-after-cpi-2026-02-12", "title": "BTC After CPI (2026-02-12): Up/Down Odds and Median Returns", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 39}, {"slug": "btc-after-cpi-2026-01-12", "title": "BTC CPI Win Rate (2026-01-12): Historical T+1/T+7 Probability", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 39}]
chartData: [{"time": "2025-01-12", "open": 94565.73, "high": 95367.54, "low": 93712.51, "close": 94488.44}, {"time": "2025-01-13", "open": 94488.89, "high": 95837.0, "low": 89260.1, "close": 94516.52}, {"time": "2025-01-14", "open": 94519.01, "high": 97352.66, "low": 94322.16, "close": 96534.05}, {"time": "2025-01-15", "open": 96534.05, "high": 100697.23, "low": 96501.64, "close": 100504.49}, {"time": "2025-01-16", "open": 100505.3, "high": 100781.59, "low": 97364.45, "close": 99756.91}, {"time": "2025-01-17", "open": 100025.77, "high": 105884.23, "low": 99948.91, "close": 104462.04}, {"time": "2025-01-18", "open": 104124.95, "high": 104913.2, "low": 102226.62, "close": 104408.07}, {"time": "2025-01-19", "open": 104411.29, "high": 106299.8, "low": 99570.53, "close": 101089.61}, {"time": "2025-01-20", "open": 101083.75, "high": 109114.88, "low": 99471.36, "close": 102016.66}, {"time": "2025-01-21", "open": 102052.58, "high": 107180.92, "low": 100103.95, "close": 106146.27}, {"time": "2025-01-22", "open": 106136.38, "high": 106294.34, "low": 103360.27, "close": 103653.07}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2025-01-15**
- As-of date (T-1): **2026-03-08**
- Freshness age: **417 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 318.961, Previous 317.604, Delta +1.3570)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.51% | 0.37% | 39 |
| T+7 | 53.85% | 46.15% | 1.11% | 0.44% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.53% | 0.44% | 38 |
| T+7 | 55.26% | 44.74% | 1.26% | 0.58% | 38 |

## Historical Distribution Summary

When CPI was **UP**, BTC T+1 up probability was **60.53%** (n=38).

When CPI was **UP**, BTC T+7 up probability was **55.26%** (n=38).

Same-direction T+7 median return: **1.26%**.

For BTC, historical CPI windows show all-history T+1 up probability of 58.97% and T+7 up probability of 53.85%. When CPI printed Up versus previous, T+1 up probability was 60.53% and T+7 up probability was 55.26% across 38 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
