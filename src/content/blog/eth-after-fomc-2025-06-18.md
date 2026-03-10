---
title: "ETH Post-FOMC Reaction (2025-06-18): Quant Backtest Snapshot"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 4
title_template_key: "fomc_4"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-06-18"
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
freshness_days: 264
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: -2.8
hub_baseline_median_t7: -3.26
hub_baseline_std_t7: 15.0818
hub_baseline_delta: -0.9
z_score_t7: -0.09
percentile_t7: 43.48
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "flat"
event_actual: 4.5
event_previous: 4.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.03
  mdd_t7: -4.16
  volatility: 4.05
  impact_t1_pct: -0.1
  impact_t7_pct: -4.16
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
chartData: [{"time": "2025-06-15", "open": 2533.18, "high": 2558.68, "low": 2493.2, "close": 2546.84}, {"time": "2025-06-16", "open": 2547.23, "high": 2680.09, "low": 2517.15, "close": 2540.6}, {"time": "2025-06-17", "open": 2540.31, "high": 2617.9, "low": 2456.65, "close": 2510.76}, {"time": "2025-06-18", "open": 2510.82, "high": 2546.63, "low": 2469.05, "close": 2524.3}, {"time": "2025-06-19", "open": 2524.4, "high": 2546.77, "low": 2486.1, "close": 2521.65}, {"time": "2025-06-20", "open": 2521.53, "high": 2569.01, "low": 2371.47, "close": 2407.3}, {"time": "2025-06-21", "open": 2407.35, "high": 2448.41, "low": 2222.81, "close": 2300.5}, {"time": "2025-06-22", "open": 2298.84, "high": 2313.85, "low": 2116.68, "close": 2228.21}, {"time": "2025-06-23", "open": 2228.48, "high": 2434.24, "low": 2191.42, "close": 2421.82}, {"time": "2025-06-24", "open": 2421.83, "high": 2481.22, "low": 2379.57, "close": 2448.01}, {"time": "2025-06-25", "open": 2448.74, "high": 2468.68, "low": 2394.61, "close": 2419.31}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2025-06-18**
- As-of date (T-1): **2026-03-09**
- Freshness age: **264 days**
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
