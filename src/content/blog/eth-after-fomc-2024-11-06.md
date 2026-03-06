---
title: "2024-11-06 FOMC Meeting: ETH T+1/T+7 Probability Profile"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "fomc_3"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-11-06"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -3.11
robust_score: -13.11
penalties:
  sample: 4.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 9
freshness_days: 484
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: -0.1
hub_baseline_median_t7: -0.19
hub_baseline_std_t7: 12.9045
hub_baseline_delta: 17.39
z_score_t7: 1.34
percentile_t7: 100.0
narrative_trigger: "extreme_outperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "flat"
event_actual: 5.0
event_previous: 5.0
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 1.58
  mdd_t7: 0.0
  volatility: 10.91
  impact_t1_pct: 6.29
  impact_t7_pct: 17.2
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 1.2
    mean: 1.38
    sample: 9
  t7:
    up: 44.44
    down: 55.56
    median: -0.19
    mean: -0.1
    sample: 9
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 9
    t1:
      up: 55.56
      down: 44.44
      median: 1.2
      mean: 1.38
      sample: 9
    t7:
      up: 44.44
      down: 55.56
      median: -0.19
      mean: -0.1
      sample: 9
related_events: [{"slug": "eth-after-fomc-2024-01-30", "title": "ETH Post-FOMC Reaction (2024-01-30): Quant Backtest Snapshot", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 3.74, "median_t7_pct": -0.19, "sample_size": 9}, {"slug": "eth-after-fomc-2026-01-28", "title": "Fed Decision (2026-01-28) and ETH: Event-Driven Odds", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.19, "sample_size": 9}, {"slug": "eth-after-fomc-2025-12-10", "title": "2025-12-10 FOMC Meeting: ETH T+1/T+7 Probability Profile", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.19, "sample_size": 9}]
chartData: [{"time": "2024-11-03", "open": 2491.09, "high": 2495.44, "low": 2411.4, "close": 2456.43}, {"time": "2024-11-04", "open": 2456.1, "high": 2488.35, "low": 2359.58, "close": 2397.03}, {"time": "2024-11-05", "open": 2397.04, "high": 2478.62, "low": 2380.6, "close": 2422.65}, {"time": "2024-11-06", "open": 2422.54, "high": 2743.96, "low": 2421.81, "close": 2724.17}, {"time": "2024-11-07", "open": 2724.01, "high": 2918.74, "low": 2701.59, "close": 2895.59}, {"time": "2024-11-08", "open": 2895.6, "high": 2983.74, "low": 2889.48, "close": 2962.3}, {"time": "2024-11-09", "open": 2962.79, "high": 3156.37, "low": 2957.18, "close": 3131.14}, {"time": "2024-11-10", "open": 3130.73, "high": 3249.91, "low": 3073.25, "close": 3191.33}, {"time": "2024-11-11", "open": 3191.66, "high": 3389.53, "low": 3109.77, "close": 3374.81}, {"time": "2024-11-12", "open": 3375.15, "high": 3444.15, "low": 3211.2, "close": 3246.26}, {"time": "2024-11-13", "open": 3244.54, "high": 3337.88, "low": 3121.67, "close": 3192.6}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2024-11-06**
- As-of date (T-1): **2026-03-05**
- Freshness age: **484 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.0, Previous 5.0, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 1.2% | 1.38% | 9 |
| T+7 | 44.44% | 55.56% | -0.19% | -0.1% | 9 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 1.2% | 1.38% | 9 |
| T+7 | 44.44% | 55.56% | -0.19% | -0.1% | 9 |

## Historical Distribution Summary

When FOMC was **FLAT**, ETH T+1 up probability was **55.56%** (n=9).

When FOMC was **FLAT**, ETH T+7 up probability was **44.44%** (n=9).

Same-direction T+7 median return: **-0.19%**.

For ETH, historical FOMC windows show all-history T+1 up probability of 55.56% and T+7 up probability of 44.44%. When FOMC printed Flat versus previous, T+1 up probability was 55.56% and T+7 up probability was 44.44% across 9 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
