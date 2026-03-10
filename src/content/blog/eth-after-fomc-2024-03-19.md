---
title: "ETH Post-FOMC Reaction (2024-03-19): Quant Backtest Snapshot"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 4
title_template_key: "fomc_4"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-03-19"
asof_date: "2026-03-09"
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
freshness_days: 720
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: -2.8
hub_baseline_median_t7: -3.26
hub_baseline_std_t7: 15.0818
hub_baseline_delta: 16.87
z_score_t7: 1.09
percentile_t7: 91.3
narrative_trigger: "extreme_outperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:51+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 5.82
  mdd_t7: 0.0
  volatility: 2.34
  impact_t1_pct: 11.27
  impact_t7_pct: 13.61
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
    direction: "flat"
    sample_size: 17
    t1:
      up: 35.29
      down: 64.71
      median: -1.41
      mean: 0.94
      sample: 17
    t7:
      up: 29.41
      down: 70.59
      median: -3.26
      mean: -1.88
      sample: 17
related_events: [{"slug": "eth-after-fomc-2024-01-30", "title": "ETH Post-FOMC Reaction (2024-01-30): Quant Backtest Snapshot", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Bearish", "sharpe_t7": 3.74, "median_t7_pct": -3.26, "sample_size": 23}, {"slug": "eth-after-fomc-2026-01-28", "title": "Fed Decision (2026-01-28) and ETH: Event-Driven Odds", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Bearish", "sharpe_t7": 0.0, "median_t7_pct": -3.26, "sample_size": 23}, {"slug": "eth-after-fomc-2025-12-10", "title": "2025-12-10 FOMC Meeting: ETH T+1/T+7 Probability Profile", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Bearish", "sharpe_t7": 0.0, "median_t7_pct": -3.26, "sample_size": 23}]
chartData: [{"time": "2024-03-16", "open": 3736.1, "high": 3780.89, "low": 3468.08, "close": 3522.86}, {"time": "2024-03-17", "open": 3523.03, "high": 3676.26, "low": 3414.17, "close": 3642.41}, {"time": "2024-03-18", "open": 3642.3, "high": 3642.5, "low": 3456.09, "close": 3517.99}, {"time": "2024-03-19", "open": 3518.35, "high": 3546.58, "low": 3149.29, "close": 3157.62}, {"time": "2024-03-20", "open": 3158.4, "high": 3534.83, "low": 3059.65, "close": 3513.39}, {"time": "2024-03-21", "open": 3514.02, "high": 3586.91, "low": 3412.22, "close": 3492.99}, {"time": "2024-03-22", "open": 3492.9, "high": 3541.9, "low": 3254.97, "close": 3333.69}, {"time": "2024-03-23", "open": 3335.59, "high": 3433.76, "low": 3273.12, "close": 3336.59}, {"time": "2024-03-24", "open": 3336.67, "high": 3470.34, "low": 3301.28, "close": 3454.64}, {"time": "2024-03-25", "open": 3454.89, "high": 3657.12, "low": 3421.79, "close": 3590.88}, {"time": "2024-03-26", "open": 3591.09, "high": 3678.79, "low": 3545.43, "close": 3587.5}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2024-03-19**
- As-of date (T-1): **2026-03-09**
- Freshness age: **720 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.5, Previous 5.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 43.48% | 56.52% | -0.1% | 0.91% | 23 |
| T+7 | 30.43% | 69.57% | -3.26% | -2.8% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 35.29% | 64.71% | -1.41% | 0.94% | 17 |
| T+7 | 29.41% | 70.59% | -3.26% | -1.88% | 17 |

## Historical Distribution Summary

When FOMC was **FLAT**, ETH T+1 up probability was **35.29%** (n=17).

When FOMC was **FLAT**, ETH T+7 up probability was **29.41%** (n=17).

Same-direction T+7 median return: **-3.26%**.

For ETH, historical FOMC windows show all-history T+1 up probability of 43.48% and T+7 up probability of 30.43%. When FOMC printed Flat versus previous, T+1 up probability was 35.29% and T+7 up probability was 29.41% across 17 matched cases. Current classification is Bearish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
