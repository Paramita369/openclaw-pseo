---
title: "SPY Reaction to US CPI (2024-07-11): Quant Probability Breakdown"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-07-11"
asof_date: "2026-03-08"
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
freshness_days: 605
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 0.21
hub_baseline_median_t7: 0.51
hub_baseline_std_t7: 1.714
hub_baseline_delta: -1.2
z_score_t7: -0.52
percentile_t7: 23.68
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 313.569
event_previous: 313.044
event_delta: 0.525
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -5.55
  mdd_t7: -1.31
  volatility: 1.32
  impact_t1_pct: 0.63
  impact_t7_pct: -0.69
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
related_events: [{"slug": "spy-after-cpi-2024-03-12", "title": "SPY CPI Win Rate (2024-03-12): Historical T+1/T+7 Probability", "event_date": "2024-03-12", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 3.94, "median_t7_pct": 1.08, "sample_size": 14}, {"slug": "spy-after-cpi-2024-11-14", "title": "2024-11-14 CPI Release: SPY Directional Probability Snapshot", "event_date": "2024-11-14", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.43, "median_t7_pct": 1.08, "sample_size": 14}, {"slug": "spy-after-cpi-2024-05-15", "title": "2024-05-15 CPI Release: SPY Directional Probability Snapshot", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.37, "median_t7_pct": 1.08, "sample_size": 14}]
chartData: [{"time": "2024-07-08", "open": 545.48, "high": 546.27, "low": 544.25, "close": 545.32}, {"time": "2024-07-09", "open": 546.28, "high": 547.19, "low": 545.56, "close": 545.85}, {"time": "2024-07-10", "open": 547.08, "high": 551.6, "low": 546.78, "close": 551.25}, {"time": "2024-07-11", "open": 551.37, "high": 552.24, "low": 545.86, "close": 546.5}, {"time": "2024-07-12", "open": 547.63, "high": 553.56, "low": 547.16, "close": 549.95}, {"time": "2024-07-15", "open": 551.95, "high": 554.71, "low": 549.59, "close": 551.46}, {"time": "2024-07-16", "open": 552.78, "high": 555.02, "low": 552.02, "close": 554.73}, {"time": "2024-07-17", "open": 548.78, "high": 550.46, "low": 546.63, "close": 546.95}, {"time": "2024-07-18", "open": 548.49, "high": 549.49, "low": 540.56, "close": 542.75}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2024-07-11**
- As-of date (T-1): **2026-03-08**
- Freshness age: **605 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 313.569, Previous 313.044, Delta +0.5250)
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
