---
title: "2025-08-12 CPI Release: BTC Directional Probability Snapshot"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 4
title_template_key: "cpi_4"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-08-12"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 3.43
robust_score: -2.57
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 70
sample_size: 14
freshness_days: 205
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.69
hub_baseline_median_t7: 3.64
hub_baseline_std_t7: 8.5155
hub_baseline_delta: -1.95
z_score_t7: -0.0
percentile_t7: 42.86
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 323.291
event_previous: 322.169
event_delta: 1.122
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 1.18
  mdd_t7: 0.0
  volatility: 1.43
  impact_t1_pct: 0.26
  impact_t7_pct: 1.69
probabilities:
  sample_size: 14
  t1:
    up: 42.86
    down: 57.14
    median: -0.74
    mean: 0.26
    sample: 14
  t7:
    up: 57.14
    down: 42.86
    median: 3.64
    mean: 1.69
    sample: 14
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 46.15
      down: 53.85
      median: -0.74
      mean: 0.44
      sample: 13
    t7:
      up: 61.54
      down: 38.46
      median: 4.15
      mean: 2.19
      sample: 13
related_events: [{"slug": "btc-after-cpi-2024-08-14", "title": "BTC Reaction to US CPI (2024-08-14): Quant Probability Breakdown", "event_date": "2024-08-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.86, "median_t7_pct": 3.64, "sample_size": 14}, {"slug": "btc-after-cpi-2026-02-12", "title": "BTC After CPI (2026-02-12): Up/Down Odds and Median Returns", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 3.64, "sample_size": 14}, {"slug": "btc-after-cpi-2026-01-12", "title": "BTC CPI Win Rate (2026-01-12): Historical T+1/T+7 Probability", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 3.64, "sample_size": 14}]
chartData: [{"time": "2025-08-09", "open": 116678.27, "high": 117906.61, "low": 116363.84, "close": 116500.36}, {"time": "2025-08-10", "open": 116497.72, "high": 119320.71, "low": 116485.16, "close": 119306.76}, {"time": "2025-08-11", "open": 119306.81, "high": 122321.09, "low": 118159.03, "close": 118731.45}, {"time": "2025-08-12", "open": 118717.66, "high": 120302.47, "low": 118228.72, "close": 120172.91}, {"time": "2025-08-13", "open": 120168.98, "high": 123682.45, "low": 118939.63, "close": 123344.06}, {"time": "2025-08-14", "open": 123339.4, "high": 124457.12, "low": 117254.88, "close": 118359.58}, {"time": "2025-08-15", "open": 118365.78, "high": 119332.31, "low": 116864.57, "close": 117398.35}, {"time": "2025-08-16", "open": 117398.42, "high": 117996.06, "low": 117271.95, "close": 117491.35}, {"time": "2025-08-17", "open": 117492.79, "high": 118595.77, "low": 117279.52, "close": 117453.06}, {"time": "2025-08-18", "open": 117453.91, "high": 117614.17, "low": 114723.68, "close": 116252.31}, {"time": "2025-08-19", "open": 116241.86, "high": 116764.5, "low": 112730.4, "close": 112831.18}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2025-08-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **205 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 323.291, Previous 322.169, Delta +1.1220)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 42.86% | 57.14% | -0.74% | 0.26% | 14 |
| T+7 | 57.14% | 42.86% | 3.64% | 1.69% | 14 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 46.15% | 53.85% | -0.74% | 0.44% | 13 |
| T+7 | 61.54% | 38.46% | 4.15% | 2.19% | 13 |

## Historical Distribution Summary

When CPI was **UP**, BTC T+1 up probability was **46.15%** (n=13).

When CPI was **UP**, BTC T+7 up probability was **61.54%** (n=13).

Same-direction T+7 median return: **4.15%**.

For BTC, historical CPI windows show all-history T+1 up probability of 42.86% and T+7 up probability of 57.14%. When CPI printed Up versus previous, T+1 up probability was 46.15% and T+7 up probability was 61.54% across 13 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
