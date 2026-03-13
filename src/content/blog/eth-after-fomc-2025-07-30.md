---
title: "ETH Post-FOMC Reaction (2025-07-30): Quant Backtest Snapshot"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 4
title_template_key: "fomc_4"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-07-30"
asof_date: "2026-03-12"
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
freshness_days: 225
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: -2.8
hub_baseline_median_t7: -3.26
hub_baseline_std_t7: 15.0818
hub_baseline_delta: 0.0
z_score_t7: -0.03
percentile_t7: 52.17
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
  sharpe_t7: -9.6
  mdd_t7: -3.26
  volatility: 0.34
  impact_t1_pct: -2.93
  impact_t7_pct: -3.26
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
chartData: [{"time": "2025-07-27", "open": 3741.26, "high": 3876.93, "low": 3733.68, "close": 3875.25}, {"time": "2025-07-28", "open": 3875.26, "high": 3940.65, "low": 3756.52, "close": 3787.43}, {"time": "2025-07-29", "open": 3788.32, "high": 3884.0, "low": 3716.88, "close": 3793.45}, {"time": "2025-07-30", "open": 3793.58, "high": 3832.88, "low": 3683.14, "close": 3808.2}, {"time": "2025-07-31", "open": 3808.25, "high": 3877.47, "low": 3685.0, "close": 3696.71}, {"time": "2025-08-01", "open": 3696.14, "high": 3722.59, "low": 3432.38, "close": 3488.37}, {"time": "2025-08-02", "open": 3487.96, "high": 3535.56, "low": 3370.94, "close": 3392.74}, {"time": "2025-08-03", "open": 3392.74, "high": 3520.83, "low": 3357.94, "close": 3497.38}, {"time": "2025-08-04", "open": 3497.61, "high": 3734.98, "low": 3491.55, "close": 3718.99}, {"time": "2025-08-05", "open": 3719.82, "high": 3720.66, "low": 3547.62, "close": 3611.9}, {"time": "2025-08-06", "open": 3612.04, "high": 3698.12, "low": 3567.1, "close": 3683.92}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2025-07-30**
- As-of date (T-1): **2026-03-12**
- Freshness age: **225 days**
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
