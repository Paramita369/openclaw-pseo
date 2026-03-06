---
title: "Fed Decision (2024-12-19) and ETH: Event-Driven Odds"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-12-19"
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
freshness_days: 441
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 4.5
event_previous: 4.75
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -4.44
  mdd_t7: -5.62
  volatility: 65.15
  impact_t1_pct: 1.6
  impact_t7_pct: -2.54
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
chartData: [{"time": "2024-12-16", "open": 3951.65, "high": 4106.96, "low": 3882.71, "close": 3987.48}, {"time": "2024-12-17", "open": 3987.33, "high": 4040.34, "low": 3849.29, "close": 3886.77}, {"time": "2024-12-18", "open": 3886.89, "high": 3902.72, "low": 3617.84, "close": 3618.79}, {"time": "2024-12-19", "open": 3619.58, "high": 3717.66, "low": 3330.87, "close": 3417.93}, {"time": "2024-12-20", "open": 3417.93, "high": 3496.33, "low": 3098.2, "close": 3472.55}, {"time": "2024-12-21", "open": 3472.59, "high": 3552.92, "low": 3293.51, "close": 3337.22}, {"time": "2024-12-22", "open": 3337.0, "high": 3398.66, "low": 3219.29, "close": 3277.54}, {"time": "2024-12-23", "open": 3277.51, "high": 3461.53, "low": 3217.37, "close": 3415.79}, {"time": "2024-12-24", "open": 3415.74, "high": 3535.86, "low": 3355.61, "close": 3492.05}, {"time": "2024-12-25", "open": 3491.96, "high": 3542.83, "low": 3440.1, "close": 3493.24}, {"time": "2024-12-26", "open": 3493.3, "high": 3512.6, "low": 3302.31, "close": 3331.23}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2024-12-19**
- As-of date (T-1): **2026-03-05**
- Freshness age: **441 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 4.5, Previous 4.75, Delta -0.2500)
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
