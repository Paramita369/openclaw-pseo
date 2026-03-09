---
title: "SPY Reaction to US CPI (2025-02-12): Quant Probability Breakdown"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-02-12"
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
freshness_days: 389
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.21
hub_baseline_median_t7: 0.51
hub_baseline_std_t7: 1.714
hub_baseline_delta: 1.08
z_score_t7: 0.81
percentile_t7: 81.58
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:04:07+00:00"
event_direction: "up"
event_actual: 319.679
event_previous: 318.961
event_delta: 0.718
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 3.0
  mdd_t7: 0.0
  volatility: 0.53
  impact_t1_pct: 1.06
  impact_t7_pct: 1.59
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
chartData: [{"time": "2025-02-10", "open": 597.02, "high": 598.47, "low": 595.74, "close": 597.83}, {"time": "2025-02-11", "open": 595.56, "high": 598.83, "low": 595.44, "close": 598.28}, {"time": "2025-02-12", "open": 592.25, "high": 597.53, "low": 591.56, "close": 596.36}, {"time": "2025-02-13", "open": 597.46, "high": 602.86, "low": 596.2, "close": 602.65}, {"time": "2025-02-14", "open": 602.86, "high": 603.9, "low": 602.0, "close": 602.62}, {"time": "2025-02-18", "open": 603.79, "high": 604.39, "low": 601.32, "close": 604.39}, {"time": "2025-02-19", "open": 603.0, "high": 606.11, "low": 602.48, "close": 605.82}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2025-02-12**
- As-of date (T-1): **2026-03-08**
- Freshness age: **389 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 319.679, Previous 318.961, Delta +0.7180)
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
