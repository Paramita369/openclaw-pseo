---
title: "ETH After FOMC (2024-09-19): Historical Signal & Probability"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 1
title_template_key: "fomc_1"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-09-19"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Bearish"
raw_signal_score: -13.74
robust_score: -19.74
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 23
freshness_days: 532
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 5.0
event_previous: 5.5
event_delta: -0.5
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 24.22
  impact_t1_pct: 3.91
  impact_t7_pct: 6.79
probabilities:
  sample_size: 23
  t1:
    up: 43.48
    down: 56.52
    median: -0.1
    mean: 0.91
    sample: 23
  t7:
    up: 30.43
    down: 69.57
    median: -3.26
    mean: -2.8
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 6
    t1:
      up: 66.67
      down: 33.33
      median: 1.36
      mean: 0.84
      sample: 6
    t7:
      up: 33.33
      down: 66.67
      median: -7.6
      mean: -5.39
      sample: 6
related_events: [{"slug": "eth-after-fomc-2025-05-07", "title": "ETH After FOMC (2025-05-07): Historical T+1/T+7 Probability", "event_date": "2025-05-07", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 44.07, "sample_size": 0}, {"slug": "eth-after-fomc-2024-11-06", "title": "ETH After FOMC (2024-11-06): Historical T+1/T+7 Probability", "event_date": "2024-11-06", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 17.2, "sample_size": 0}, {"slug": "eth-after-fomc-2024-09-17", "title": "ETH After FOMC (2024-09-17): Historical T+1/T+7 Probability", "event_date": "2024-09-17", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 13.35, "sample_size": 0}]
chartData: [{"time": "2024-09-16", "open": 2320.89, "high": 2334.79, "low": 2253.72, "close": 2295.28}, {"time": "2024-09-17", "open": 2295.28, "high": 2392.15, "low": 2263.79, "close": 2341.71}, {"time": "2024-09-18", "open": 2341.73, "high": 2369.73, "low": 2278.66, "close": 2369.73}, {"time": "2024-09-19", "open": 2369.37, "high": 2492.2, "low": 2369.37, "close": 2464.75}, {"time": "2024-09-20", "open": 2464.78, "high": 2571.99, "low": 2439.38, "close": 2561.07}, {"time": "2024-09-21", "open": 2560.88, "high": 2621.62, "low": 2530.84, "close": 2615.86}, {"time": "2024-09-22", "open": 2615.85, "high": 2632.04, "low": 2528.52, "close": 2582.86}, {"time": "2024-09-23", "open": 2582.77, "high": 2701.68, "low": 2541.91, "close": 2648.55}, {"time": "2024-09-24", "open": 2648.48, "high": 2671.28, "low": 2593.15, "close": 2654.35}, {"time": "2024-09-25", "open": 2654.36, "high": 2672.46, "low": 2557.72, "close": 2579.39}, {"time": "2024-09-26", "open": 2579.22, "high": 2665.99, "low": 2559.95, "close": 2632.2}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2024-09-19**
- As-of date (T-1): **2026-03-05**
- Freshness age: **532 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 5.0, Previous 5.5, Delta -0.5000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 43.48% | 56.52% | -0.1% | 0.91% | 23 |
| T+7 | 30.43% | 69.57% | -3.26% | -2.8% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 66.67% | 33.33% | 1.36% | 0.84% | 6 |
| T+7 | 33.33% | 66.67% | -7.6% | -5.39% | 6 |

## Historical Distribution Summary

When FOMC was **DOWN**, ETH T+1 up probability was **66.67%** (n=6).

When FOMC was **DOWN**, ETH T+7 up probability was **33.33%** (n=6).

Same-direction T+7 median return: **-7.6%**.

For ETH, historical FOMC windows show all-history T+1 up probability of 43.48% and T+7 up probability of 30.43%. When FOMC printed Down versus previous, T+1 up probability was 66.67% and T+7 up probability was 33.33% across 6 matched cases. Current classification is Bearish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
