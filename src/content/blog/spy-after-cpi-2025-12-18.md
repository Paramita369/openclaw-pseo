---
title: "SPY CPI Win Rate (2025-12-18): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-12-18"
asof_date: "2026-03-03"
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
quality_score: 100
sample_size: 39
freshness_days: 75
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/spy-after-cpi-2025-12-18"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 326.031
event_previous: 325.063
event_delta: 0.968
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 1.86
  impact_t1_pct: 0.91
  impact_t7_pct: 2.35
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
related_events: [{"slug": "spy-after-cpi-2026-02-13", "title": "SPY After CPI (2026-02-13): Historical T+1/T+7 Probability", "event_date": "2026-02-13", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.13, "sample_size": 0}, {"slug": "spy-after-cpi-2026-02-12", "title": "SPY After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 0.47, "sample_size": 0}, {"slug": "spy-after-cpi-2025-10-12", "title": "SPY After CPI (2025-10-12): Historical T+1/T+7 Probability", "event_date": "2025-10-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.8, "sample_size": 0}]
chartData: [{"time": "2025-12-15", "open": 683.72, "high": 683.74, "low": 677.25, "close": 678.72}, {"time": "2025-12-16", "open": 677.23, "high": 679.07, "low": 672.99, "close": 676.87}, {"time": "2025-12-17", "open": 677.89, "high": 678.44, "low": 669.22, "close": 669.42}, {"time": "2025-12-18", "open": 675.6, "high": 678.73, "low": 672.91, "close": 674.48}, {"time": "2025-12-19", "open": 676.59, "high": 681.09, "low": 676.47, "close": 680.59}, {"time": "2025-12-22", "open": 683.94, "high": 685.36, "low": 680.59, "close": 684.83}, {"time": "2025-12-23", "open": 683.92, "high": 688.2, "low": 683.87, "close": 687.96}, {"time": "2025-12-24", "open": 687.95, "high": 690.83, "low": 687.8, "close": 690.38}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2025-12-18**
- As-of date (T-1): **2026-03-03**
- Freshness age: **75 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.031, Previous 325.063, Delta +0.9680)
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
