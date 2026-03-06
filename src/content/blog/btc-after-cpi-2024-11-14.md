---
title: "US CPI (2024-11-14) and BTC: Event-Driven Return Odds"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-11-14"
asof_date: "2026-03-05"
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
freshness_days: 476
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:22+00:00"
event_direction: "up"
event_actual: 316.528
event_previous: 315.631
event_delta: 0.897
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 36.26
  impact_t1_pct: 4.37
  impact_t7_pct: 12.9
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
chartData: [{"time": "2024-11-11", "open": 80471.41, "high": 89604.5, "low": 80283.25, "close": 88701.48}, {"time": "2024-11-12", "open": 88705.56, "high": 89956.88, "low": 85155.11, "close": 87955.81}, {"time": "2024-11-13", "open": 87929.97, "high": 93434.35, "low": 86256.93, "close": 90584.16}, {"time": "2024-11-14", "open": 90574.88, "high": 91765.22, "low": 86682.81, "close": 87250.43}, {"time": "2024-11-15", "open": 87284.18, "high": 91868.74, "low": 87124.9, "close": 91066.01}, {"time": "2024-11-16", "open": 91064.37, "high": 91763.95, "low": 90094.23, "close": 90558.48}, {"time": "2024-11-17", "open": 90558.46, "high": 91433.04, "low": 88741.66, "close": 89845.85}, {"time": "2024-11-18", "open": 89843.72, "high": 92596.79, "low": 89393.59, "close": 90542.64}, {"time": "2024-11-19", "open": 90536.81, "high": 94002.87, "low": 90426.98, "close": 92343.79}, {"time": "2024-11-20", "open": 92341.89, "high": 94902.02, "low": 91619.5, "close": 94339.49}, {"time": "2024-11-21", "open": 94334.64, "high": 99014.22, "low": 94132.6, "close": 98504.73}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2024-11-14**
- As-of date (T-1): **2026-03-05**
- Freshness age: **476 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 316.528, Previous 315.631, Delta +0.8970)
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
