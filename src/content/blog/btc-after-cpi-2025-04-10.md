---
title: "US CPI (2025-04-10) and BTC: Event-Driven Return Odds"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-04-10"
asof_date: "2026-03-03"
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
quality_score: 100
sample_size: 39
freshness_days: 327
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 320.302
event_previous: 319.785
event_delta: 0.517
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 35.78
  impact_t1_pct: 4.75
  impact_t7_pct: 6.62
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
related_events: [{"slug": "btc-after-cpi-2025-09-11", "title": "BTC After CPI (2025-09-11): Historical T+1/T+7 Probability", "event_date": "2025-09-11", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.41, "sample_size": 0}, {"slug": "btc-after-cpi-2025-07-15", "title": "BTC After CPI (2025-07-15): Historical T+1/T+7 Probability", "event_date": "2025-07-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.88, "sample_size": 0}, {"slug": "btc-after-cpi-2025-05-12", "title": "BTC After CPI (2025-05-12): Historical T+1/T+7 Probability", "event_date": "2025-05-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.72, "sample_size": 0}]
chartData: [{"time": "2025-04-07", "open": 78221.34, "high": 81119.06, "low": 74436.68, "close": 79235.34}, {"time": "2025-04-08", "open": 79218.48, "high": 80823.89, "low": 76198.02, "close": 76271.95}, {"time": "2025-04-09", "open": 76273.56, "high": 83541.0, "low": 74589.67, "close": 82573.95}, {"time": "2025-04-10", "open": 82565.98, "high": 82700.93, "low": 78456.13, "close": 79626.14}, {"time": "2025-04-11", "open": 79625.05, "high": 84247.48, "low": 78936.32, "close": 83404.84}, {"time": "2025-04-12", "open": 83404.52, "high": 85856.19, "low": 82769.38, "close": 85287.11}, {"time": "2025-04-13", "open": 85279.47, "high": 86015.19, "low": 83027.01, "close": 83684.98}, {"time": "2025-04-14", "open": 83694.52, "high": 85785.0, "low": 83690.64, "close": 84542.39}, {"time": "2025-04-15", "open": 84539.7, "high": 86429.35, "low": 83598.82, "close": 83668.99}, {"time": "2025-04-16", "open": 83674.51, "high": 85428.28, "low": 83100.62, "close": 84033.87}, {"time": "2025-04-17", "open": 84030.67, "high": 85449.07, "low": 83749.75, "close": 84895.75}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2025-04-10**
- As-of date (T-1): **2026-03-03**
- Freshness age: **327 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 320.302, Previous 319.785, Delta +0.5170)
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
