---
title: "Fed Decision (2025-01-29) and ETH: Event-Driven Odds"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-12"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-01-29"
asof_date: "2026-03-11"
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
freshness_days: 406
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: -2.8
hub_baseline_median_t7: -3.26
hub_baseline_std_t7: 15.0818
hub_baseline_delta: -7.19
z_score_t7: -0.51
percentile_t7: 34.78
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:04:10+00:00"
event_direction: "flat"
event_actual: 4.5
event_previous: 4.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -0.71
  mdd_t7: -10.45
  volatility: 14.78
  impact_t1_pct: 4.33
  impact_t7_pct: -10.45
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
chartData: [{"time": "2025-01-26", "open": 3317.29, "high": 3359.31, "low": 3233.92, "close": 3236.13}, {"time": "2025-01-27", "open": 3235.86, "high": 3250.4, "low": 3024.09, "close": 3178.92}, {"time": "2025-01-28", "open": 3179.09, "high": 3222.74, "low": 3040.09, "close": 3077.11}, {"time": "2025-01-29", "open": 3076.38, "high": 3177.98, "low": 3055.18, "close": 3113.0}, {"time": "2025-01-30", "open": 3113.29, "high": 3282.99, "low": 3093.12, "close": 3247.78}, {"time": "2025-01-31", "open": 3247.87, "high": 3437.57, "low": 3214.94, "close": 3298.27}, {"time": "2025-02-01", "open": 3298.82, "high": 3329.66, "low": 3103.92, "close": 3118.33}, {"time": "2025-02-02", "open": 3118.61, "high": 3161.89, "low": 2755.47, "close": 2868.69}, {"time": "2025-02-03", "open": 2868.08, "high": 2919.48, "low": 2159.28, "close": 2884.57}, {"time": "2025-02-04", "open": 2883.82, "high": 2888.25, "low": 2636.17, "close": 2735.05}, {"time": "2025-02-05", "open": 2735.23, "high": 2824.4, "low": 2701.1, "close": 2787.78}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2025-01-29**
- As-of date (T-1): **2026-03-11**
- Freshness age: **406 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.5, Previous 4.5, Delta +0.0000)
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
