---
title: "US CPI (2024-10-10) and SPY: Event-Driven Return Odds"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-10-10"
asof_date: "2026-03-09"
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
freshness_days: 515
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.21
hub_baseline_median_t7: 0.51
hub_baseline_std_t7: 1.714
hub_baseline_delta: 0.57
z_score_t7: 0.51
percentile_t7: 65.79
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:22+00:00"
event_direction: "up"
event_actual: 315.631
event_previous: 314.732
event_delta: 0.899
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 2.25
  mdd_t7: 0.0
  volatility: 0.48
  impact_t1_pct: 0.6
  impact_t7_pct: 1.08
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
chartData: [{"time": "2024-10-07", "open": 562.77, "high": 563.43, "low": 558.17, "close": 559.33}, {"time": "2024-10-08", "open": 561.91, "high": 565.22, "low": 561.03, "close": 564.62}, {"time": "2024-10-09", "open": 564.61, "high": 569.09, "low": 564.01, "close": 568.53}, {"time": "2024-10-10", "open": 567.18, "high": 568.96, "low": 565.92, "close": 567.53}, {"time": "2024-10-11", "open": 567.45, "high": 571.67, "low": 567.32, "close": 570.93}, {"time": "2024-10-14", "open": 572.55, "high": 576.54, "low": 572.06, "close": 575.6}, {"time": "2024-10-15", "open": 575.87, "high": 576.17, "low": 569.91, "close": 571.13}, {"time": "2024-10-16", "open": 571.13, "high": 574.13, "low": 570.32, "close": 573.61}, {"time": "2024-10-17", "open": 577.17, "high": 577.37, "low": 573.47, "close": 573.66}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2024-10-10**
- As-of date (T-1): **2026-03-09**
- Freshness age: **515 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 315.631, Previous 314.732, Delta +0.8990)
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
