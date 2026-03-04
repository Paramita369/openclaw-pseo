---
title: "US CPI (2025-10-24) and BTC: Event-Driven Return Odds"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-10-24"
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
freshness_days: 130
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 324.245
event_previous: 323.291
event_delta: 0.954
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -2.99
  mdd_t7: -4.0
  volatility: 50.19
  impact_t1_pct: 0.55
  impact_t7_pct: -1.33
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
chartData: [{"time": "2025-10-21", "open": 110587.63, "high": 113996.34, "low": 107534.75, "close": 108476.89}, {"time": "2025-10-22", "open": 108491.53, "high": 109115.13, "low": 106778.0, "close": 107688.59}, {"time": "2025-10-23", "open": 107679.44, "high": 111288.59, "low": 107548.43, "close": 110069.73}, {"time": "2025-10-24", "open": 110069.35, "high": 111842.53, "low": 109770.15, "close": 111033.92}, {"time": "2025-10-25", "open": 111032.62, "high": 111947.7, "low": 110704.41, "close": 111641.73}, {"time": "2025-10-26", "open": 111639.05, "high": 115260.91, "low": 111268.48, "close": 114472.45}, {"time": "2025-10-27", "open": 114479.85, "high": 116273.31, "low": 113882.29, "close": 114119.33}, {"time": "2025-10-28", "open": 114129.09, "high": 116078.98, "low": 112291.68, "close": 112956.16}, {"time": "2025-10-29", "open": 112921.33, "high": 113642.73, "low": 109368.72, "close": 110055.3}, {"time": "2025-10-30", "open": 110059.2, "high": 111612.35, "low": 106376.69, "close": 108305.55}, {"time": "2025-10-31", "open": 108304.41, "high": 111031.82, "low": 108288.27, "close": 109556.16}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2025-10-24**
- As-of date (T-1): **2026-03-03**
- Freshness age: **130 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 324.245, Previous 323.291, Delta +0.9540)
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
