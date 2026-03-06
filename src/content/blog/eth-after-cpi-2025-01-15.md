---
title: "ETH Reaction to US CPI (2025-01-15): Quant Probability Breakdown"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-01-15"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -2.51
robust_score: -8.51
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 100
sample_size: 39
freshness_days: 414
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:04:04+00:00"
event_direction: "up"
event_actual: 318.961
event_previous: 317.604
event_delta: 1.357
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -10.0
  mdd_t7: -6.1
  volatility: 19.7
  impact_t1_pct: -4.12
  impact_t7_pct: -6.1
probabilities:
  sample_size: 39
  t1:
    up: 58.97
    down: 41.03
    median: 0.94
    mean: 0.55
    sample: 39
  t7:
    up: 43.59
    down: 56.41
    median: -1.18
    mean: 0.23
    sample: 39
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.96
      mean: 0.64
      sample: 38
    t7:
      up: 44.74
      down: 55.26
      median: -1.52
      mean: 0.24
      sample: 38
related_events: [{"slug": "eth-after-cpi-2025-07-15", "title": "ETH After CPI (2025-07-15): Historical T+1/T+7 Probability", "event_date": "2025-07-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 19.4, "sample_size": 0}, {"slug": "eth-after-cpi-2025-07-12", "title": "ETH After CPI (2025-07-12): Historical T+1/T+7 Probability", "event_date": "2025-07-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 22.17, "sample_size": 0}, {"slug": "eth-after-cpi-2025-04-10", "title": "ETH After CPI (2025-04-10): Historical T+1/T+7 Probability", "event_date": "2025-04-10", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.94, "sample_size": 0}]
chartData: [{"time": "2025-01-12", "open": 3282.15, "high": 3298.02, "low": 3224.51, "close": 3265.95}, {"time": "2025-01-13", "open": 3266.1, "high": 3335.19, "low": 2920.59, "close": 3135.5}, {"time": "2025-01-14", "open": 3135.67, "high": 3254.75, "low": 3126.81, "close": 3223.68}, {"time": "2025-01-15", "open": 3223.68, "high": 3473.1, "low": 3186.14, "close": 3450.54}, {"time": "2025-01-16", "open": 3450.31, "high": 3458.18, "low": 3265.68, "close": 3308.35}, {"time": "2025-01-17", "open": 3308.19, "high": 3525.54, "low": 3307.31, "close": 3474.11}, {"time": "2025-01-18", "open": 3473.56, "high": 3493.06, "low": 3228.33, "close": 3305.79}, {"time": "2025-01-19", "open": 3305.4, "high": 3444.21, "low": 3127.62, "close": 3208.96}, {"time": "2025-01-20", "open": 3208.93, "high": 3444.28, "low": 3147.52, "close": 3278.04}, {"time": "2025-01-21", "open": 3278.44, "high": 3365.78, "low": 3202.49, "close": 3327.41}, {"time": "2025-01-22", "open": 3327.24, "high": 3364.75, "low": 3223.39, "close": 3240.22}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2025-01-15**
- As-of date (T-1): **2026-03-05**
- Freshness age: **414 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 318.961, Previous 317.604, Delta +1.3570)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.94% | 0.55% | 39 |
| T+7 | 43.59% | 56.41% | -1.18% | 0.23% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.96% | 0.64% | 38 |
| T+7 | 44.74% | 55.26% | -1.52% | 0.24% | 38 |

## Historical Distribution Summary

When CPI was **UP**, ETH T+1 up probability was **60.53%** (n=38).

When CPI was **UP**, ETH T+7 up probability was **44.74%** (n=38).

Same-direction T+7 median return: **-1.52%**.

For ETH, historical CPI windows show all-history T+1 up probability of 58.97% and T+7 up probability of 43.59%. When CPI printed Up versus previous, T+1 up probability was 60.53% and T+7 up probability was 44.74% across 38 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
