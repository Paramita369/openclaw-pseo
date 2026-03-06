---
title: "2024-01-11 CPI Release: ETH Directional Probability Snapshot"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 4
title_template_key: "cpi_4"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-01-11"
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
freshness_days: 784
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 309.698
event_previous: 308.741
event_delta: 0.957
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -10.0
  mdd_t7: -5.83
  volatility: 26.72
  impact_t1_pct: -3.63
  impact_t7_pct: -5.83
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
chartData: [{"time": "2024-01-08", "open": 2222.86, "high": 2358.82, "low": 2171.99, "close": 2333.03}, {"time": "2024-01-09", "open": 2332.87, "high": 2369.64, "low": 2243.22, "close": 2344.83}, {"time": "2024-01-10", "open": 2344.92, "high": 2626.98, "low": 2341.94, "close": 2582.1}, {"time": "2024-01-11", "open": 2584.17, "high": 2687.78, "low": 2567.99, "close": 2619.62}, {"time": "2024-01-12", "open": 2619.18, "high": 2710.42, "low": 2460.93, "close": 2524.46}, {"time": "2024-01-13", "open": 2522.93, "high": 2589.08, "low": 2498.59, "close": 2576.6}, {"time": "2024-01-14", "open": 2578.0, "high": 2578.33, "low": 2470.42, "close": 2472.24}, {"time": "2024-01-15", "open": 2471.67, "high": 2550.77, "low": 2470.82, "close": 2511.36}, {"time": "2024-01-16", "open": 2510.63, "high": 2613.57, "low": 2500.0, "close": 2587.69}, {"time": "2024-01-17", "open": 2587.04, "high": 2592.74, "low": 2508.43, "close": 2528.37}, {"time": "2024-01-18", "open": 2528.59, "high": 2546.26, "low": 2426.14, "close": 2467.02}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-01-11**
- As-of date (T-1): **2026-03-05**
- Freshness age: **784 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 309.698, Previous 308.741, Delta +0.9570)
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
