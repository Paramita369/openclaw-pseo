---
title: "US CPI (2024-09-11) and SPY: Event-Driven Return Odds"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-12"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-09-11"
asof_date: "2026-03-11"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 15.44
robust_score: 9.44
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 39
freshness_days: 546
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.21
hub_baseline_median_t7: 0.51
hub_baseline_std_t7: 1.714
hub_baseline_delta: 0.75
z_score_t7: 0.61
percentile_t7: 76.32
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:20+00:00"
event_direction: "up"
event_actual: 314.732
event_previous: 314.062
event_delta: 0.67
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 3.0
  mdd_t7: 0.0
  volatility: 0.42
  impact_t1_pct: 0.84
  impact_t7_pct: 1.26
probabilities:
  sample_size: 39
  t1:
    up: 64.1
    down: 35.9
    median: 0.16
    mean: 0.21
    sample: 39
  t7:
    up: 68.42
    down: 31.58
    median: 0.51
    mean: 0.21
    sample: 38
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 63.16
      down: 36.84
      median: 0.14
      mean: 0.21
      sample: 38
    t7:
      up: 68.42
      down: 31.58
      median: 0.51
      mean: 0.21
      sample: 38
related_events: [{"slug": "spy-after-cpi-2024-03-12", "title": "SPY CPI Win Rate (2024-03-12): Historical T+1/T+7 Probability", "event_date": "2024-03-12", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 3.94, "median_t7_pct": 0.51, "sample_size": 39}, {"slug": "spy-after-cpi-2024-11-14", "title": "2024-11-14 CPI Release: SPY Directional Probability Snapshot", "event_date": "2024-11-14", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.43, "median_t7_pct": 0.51, "sample_size": 39}, {"slug": "spy-after-cpi-2024-05-15", "title": "2024-05-15 CPI Release: SPY Directional Probability Snapshot", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.37, "median_t7_pct": 0.51, "sample_size": 39}]
chartData: [{"time": "2024-09-09", "open": 534.88, "high": 537.89, "low": 532.95, "close": 536.61}, {"time": "2024-09-10", "open": 538.53, "high": 539.3, "low": 533.63, "close": 538.95}, {"time": "2024-09-11", "open": 538.86, "high": 545.4, "low": 530.28, "close": 544.48}, {"time": "2024-09-12", "open": 545.06, "high": 549.37, "low": 542.83, "close": 549.06}, {"time": "2024-09-13", "open": 549.67, "high": 552.93, "low": 549.42, "close": 551.93}, {"time": "2024-09-16", "open": 551.67, "high": 553.01, "low": 549.86, "close": 552.75}, {"time": "2024-09-17", "open": 554.97, "high": 556.42, "low": 550.73, "close": 552.97}, {"time": "2024-09-18", "open": 553.63, "high": 558.49, "low": 550.77, "close": 551.33}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2024-09-11**
- As-of date (T-1): **2026-03-11**
- Freshness age: **546 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 314.732, Previous 314.062, Delta +0.6700)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 64.1% | 35.9% | 0.16% | 0.21% | 39 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 63.16% | 36.84% | 0.14% | 0.21% | 38 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Historical Distribution Summary

When CPI was **UP**, SPY T+1 up probability was **63.16%** (n=38).

When CPI was **UP**, SPY T+7 up probability was **68.42%** (n=38).

Same-direction T+7 median return: **0.51%**.

For SPY, historical CPI windows show all-history T+1 up probability of 64.1% and T+7 up probability of 68.42%. When CPI printed Up versus previous, T+1 up probability was 63.16% and T+7 up probability was 68.42% across 38 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
