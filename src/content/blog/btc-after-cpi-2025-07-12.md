---
title: "BTC CPI Win Rate (2025-07-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-07-12"
asof_date: "2026-03-12"
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
freshness_days: 243
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: -0.68
z_score_t7: -0.0
percentile_t7: 48.72
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 322.169
event_previous: 321.435
event_delta: 0.734
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.43
  mdd_t7: 0.0
  volatility: 1.0
  impact_t1_pct: 1.43
  impact_t7_pct: 0.43
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
related_events: [{"slug": "btc-after-cpi-2024-08-14", "title": "BTC Reaction to US CPI (2024-08-14): Quant Probability Breakdown", "event_date": "2024-08-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.86, "median_t7_pct": 1.11, "sample_size": 39}, {"slug": "btc-after-cpi-2026-02-12", "title": "BTC After CPI (2026-02-12): Up/Down Odds and Median Returns", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 39}, {"slug": "btc-after-cpi-2026-01-12", "title": "BTC CPI Win Rate (2026-01-12): Historical T+1/T+7 Probability", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 39}]
chartData: [{"time": "2025-07-09", "open": 108950.27, "high": 111925.38, "low": 108357.68, "close": 111326.55}, {"time": "2025-07-10", "open": 111329.2, "high": 116608.78, "low": 110660.75, "close": 115987.2}, {"time": "2025-07-11", "open": 115986.23, "high": 118856.48, "low": 115245.69, "close": 117516.99}, {"time": "2025-07-12", "open": 117530.71, "high": 118219.9, "low": 116977.02, "close": 117435.23}, {"time": "2025-07-13", "open": 117432.2, "high": 119449.57, "low": 117265.44, "close": 119116.12}, {"time": "2025-07-14", "open": 119115.79, "high": 123091.61, "low": 118959.2, "close": 119849.7}, {"time": "2025-07-15", "open": 119853.85, "high": 119935.56, "low": 115765.69, "close": 117777.19}, {"time": "2025-07-16", "open": 117777.19, "high": 120065.52, "low": 117064.82, "close": 118738.51}, {"time": "2025-07-17", "open": 118738.51, "high": 120999.61, "low": 117508.22, "close": 119289.84}, {"time": "2025-07-18", "open": 119284.11, "high": 120851.91, "low": 116925.98, "close": 118003.23}, {"time": "2025-07-19", "open": 117998.12, "high": 118541.4, "low": 117388.41, "close": 117939.98}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2025-07-12**
- As-of date (T-1): **2026-03-12**
- Freshness age: **243 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 322.169, Previous 321.435, Delta +0.7340)
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
