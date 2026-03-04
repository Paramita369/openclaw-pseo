---
title: "SPY CPI Win Rate (2025-01-15): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-01-15"
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
freshness_days: 412
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 318.961
event_previous: 317.604
event_delta: 1.357
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: -0.19
  volatility: 21.38
  impact_t1_pct: -0.19
  impact_t7_pct: 2.3
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
related_events: [{"slug": "spy-after-cpi-2026-02-13", "title": "SPY After CPI (2026-02-13): Historical T+1/T+7 Probability", "event_date": "2026-02-13", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.13, "sample_size": 0}, {"slug": "spy-after-cpi-2026-02-12", "title": "SPY After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 0.47, "sample_size": 0}, {"slug": "spy-after-cpi-2025-12-18", "title": "SPY After CPI (2025-12-18): Historical T+1/T+7 Probability", "event_date": "2025-12-18", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.35, "sample_size": 0}]
chartData: [{"time": "2025-01-13", "open": 569.09, "high": 575.0, "low": 568.67, "close": 574.64}, {"time": "2025-01-14", "open": 577.58, "high": 578.21, "low": 571.64, "close": 575.43}, {"time": "2025-01-15", "open": 583.48, "high": 587.05, "low": 582.36, "close": 585.9}, {"time": "2025-01-16", "open": 587.27, "high": 587.45, "low": 584.07, "close": 584.77}, {"time": "2025-01-17", "open": 590.03, "high": 592.4, "low": 588.7, "close": 590.64}, {"time": "2025-01-21", "open": 593.7, "high": 596.06, "low": 591.72, "close": 596.05}, {"time": "2025-01-22", "open": 598.89, "high": 600.77, "low": 598.33, "close": 599.4}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2025-01-15**
- As-of date (T-1): **2026-03-03**
- Freshness age: **412 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 318.961, Previous 317.604, Delta +1.3570)
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
