---
title: "ETH Post-FOMC Reaction (2024-11-08): Quant Backtest Snapshot"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 4
title_template_key: "fomc_4"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-11-08"
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
freshness_days: 482
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 4.75
event_previous: 5.0
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 4.92
  mdd_t7: -8.05
  volatility: 134.22
  impact_t1_pct: 5.7
  impact_t7_pct: 4.75
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
related_events: [{"slug": "eth-after-fomc-2025-05-07", "title": "ETH After FOMC (2025-05-07): Historical T+1/T+7 Probability", "event_date": "2025-05-07", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 44.07, "sample_size": 0}, {"slug": "eth-after-fomc-2024-11-06", "title": "ETH After FOMC (2024-11-06): Historical T+1/T+7 Probability", "event_date": "2024-11-06", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 17.2, "sample_size": 0}, {"slug": "eth-after-fomc-2024-09-19", "title": "ETH After FOMC (2024-09-19): Historical T+1/T+7 Probability", "event_date": "2024-09-19", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 6.79, "sample_size": 0}]
chartData: [{"time": "2024-11-05", "open": 2397.04, "high": 2478.62, "low": 2380.6, "close": 2422.65}, {"time": "2024-11-06", "open": 2422.54, "high": 2743.96, "low": 2421.81, "close": 2724.17}, {"time": "2024-11-07", "open": 2724.01, "high": 2918.74, "low": 2701.59, "close": 2895.59}, {"time": "2024-11-08", "open": 2895.6, "high": 2983.74, "low": 2889.48, "close": 2962.3}, {"time": "2024-11-09", "open": 2962.79, "high": 3156.37, "low": 2957.18, "close": 3131.14}, {"time": "2024-11-10", "open": 3130.73, "high": 3249.91, "low": 3073.25, "close": 3191.33}, {"time": "2024-11-11", "open": 3191.66, "high": 3389.53, "low": 3109.77, "close": 3374.81}, {"time": "2024-11-12", "open": 3375.15, "high": 3444.15, "low": 3211.2, "close": 3246.26}, {"time": "2024-11-13", "open": 3244.54, "high": 3337.88, "low": 3121.67, "close": 3192.6}, {"time": "2024-11-14", "open": 3192.52, "high": 3240.27, "low": 3032.97, "close": 3058.95}, {"time": "2024-11-15", "open": 3059.53, "high": 3130.7, "low": 3016.14, "close": 3103.04}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2024-11-08**
- As-of date (T-1): **2026-03-05**
- Freshness age: **482 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 4.75, Previous 5.0, Delta -0.2500)
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
