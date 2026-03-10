---
title: "BTC After CPI (2024-09-11): Up/Down Odds and Median Returns"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 5
title_template_key: "cpi_5"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-09-11"
asof_date: "2026-03-09"
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
freshness_days: 544
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: 6.4
z_score_t7: 1.08
percentile_t7: 87.18
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:18+00:00"
event_direction: "up"
event_actual: 314.732
event_previous: 314.062
event_delta: 0.67
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 1.22
  mdd_t7: 0.0
  volatility: 6.14
  impact_t1_pct: 1.37
  impact_t7_pct: 7.51
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
chartData: [{"time": "2024-09-08", "open": 54147.93, "high": 55300.86, "low": 53653.76, "close": 54841.57}, {"time": "2024-09-09", "open": 54851.89, "high": 58041.12, "low": 54598.43, "close": 57019.54}, {"time": "2024-09-10", "open": 57020.1, "high": 58029.98, "low": 56419.41, "close": 57648.71}, {"time": "2024-09-11", "open": 57650.29, "high": 57991.32, "low": 55567.34, "close": 57343.17}, {"time": "2024-09-12", "open": 57343.17, "high": 58534.36, "low": 57330.1, "close": 58127.01}, {"time": "2024-09-13", "open": 58130.32, "high": 60648.02, "low": 57650.11, "close": 60571.3}, {"time": "2024-09-14", "open": 60569.12, "high": 60656.72, "low": 59517.88, "close": 60005.12}, {"time": "2024-09-15", "open": 60000.73, "high": 60381.92, "low": 58696.31, "close": 59182.84}, {"time": "2024-09-16", "open": 59185.23, "high": 59205.51, "low": 57501.34, "close": 58192.51}, {"time": "2024-09-17", "open": 58192.51, "high": 61316.09, "low": 57628.07, "close": 60308.54}, {"time": "2024-09-18", "open": 60309.0, "high": 61664.07, "low": 59218.25, "close": 61649.68}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2024-09-11**
- As-of date (T-1): **2026-03-09**
- Freshness age: **544 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 314.732, Previous 314.062, Delta +0.6700)
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
