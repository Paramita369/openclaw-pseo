---
title: "ETH After FOMC (2024-07-30): Historical Signal & Probability"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 1
title_template_key: "fomc_1"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-07-30"
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
freshness_days: 587
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: -2.8
hub_baseline_median_t7: -3.26
hub_baseline_std_t7: 15.0818
hub_baseline_delta: -21.75
z_score_t7: -1.47
percentile_t7: 8.7
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:56+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.06
  mdd_t7: -25.01
  volatility: 23.57
  impact_t1_pct: -1.44
  impact_t7_pct: -25.01
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
chartData: [{"time": "2024-07-27", "open": 3275.89, "high": 3327.43, "low": 3195.36, "close": 3247.61}, {"time": "2024-07-28", "open": 3247.51, "high": 3283.15, "low": 3201.76, "close": 3271.46}, {"time": "2024-07-29", "open": 3271.45, "high": 3396.63, "low": 3257.72, "close": 3320.54}, {"time": "2024-07-30", "open": 3320.64, "high": 3365.32, "low": 3235.76, "close": 3278.67}, {"time": "2024-07-31", "open": 3278.69, "high": 3347.64, "low": 3216.07, "close": 3231.3}, {"time": "2024-08-01", "open": 3231.25, "high": 3241.78, "low": 3078.54, "close": 3201.56}, {"time": "2024-08-02", "open": 3201.6, "high": 3214.53, "low": 2965.73, "close": 2986.01}, {"time": "2024-08-03", "open": 2985.95, "high": 3015.3, "low": 2861.18, "close": 2903.39}, {"time": "2024-08-04", "open": 2903.09, "high": 2931.47, "low": 2639.57, "close": 2686.4}, {"time": "2024-08-05", "open": 2686.03, "high": 2695.89, "low": 2122.55, "close": 2417.21}, {"time": "2024-08-06", "open": 2417.27, "high": 2553.58, "low": 2416.53, "close": 2458.72}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2024-07-30**
- As-of date (T-1): **2026-03-09**
- Freshness age: **587 days**
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
