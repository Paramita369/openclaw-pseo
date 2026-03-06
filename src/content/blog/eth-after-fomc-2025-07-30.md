---
title: "ETH Post-FOMC Reaction (2025-07-30): Quant Backtest Snapshot"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 4
title_template_key: "fomc_4"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-07-30"
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
quality_score: 60
sample_size: 9
freshness_days: 218
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: -0.1
hub_baseline_median_t7: -0.19
hub_baseline_std_t7: 12.9045
hub_baseline_delta: 0.09
z_score_t7: -0.0
percentile_t7: 55.56
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "flat"
event_actual: 4.5
event_previous: 4.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -0.07
  mdd_t7: -0.1
  volatility: 1.48
  impact_t1_pct: 1.38
  impact_t7_pct: -0.1
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
chartData: [{"time": "2025-07-27", "open": 3741.26, "high": 3876.93, "low": 3733.68, "close": 3875.25}, {"time": "2025-07-28", "open": 3875.26, "high": 3940.65, "low": 3756.52, "close": 3787.43}, {"time": "2025-07-29", "open": 3788.32, "high": 3884.0, "low": 3716.88, "close": 3793.45}, {"time": "2025-07-30", "open": 3793.58, "high": 3832.88, "low": 3683.14, "close": 3808.2}, {"time": "2025-07-31", "open": 3808.25, "high": 3877.47, "low": 3685.0, "close": 3696.71}, {"time": "2025-08-01", "open": 3696.14, "high": 3722.59, "low": 3432.38, "close": 3488.37}, {"time": "2025-08-02", "open": 3487.96, "high": 3535.56, "low": 3370.94, "close": 3392.74}, {"time": "2025-08-03", "open": 3392.74, "high": 3520.83, "low": 3357.94, "close": 3497.38}, {"time": "2025-08-04", "open": 3497.61, "high": 3734.98, "low": 3491.55, "close": 3718.99}, {"time": "2025-08-05", "open": 3719.82, "high": 3720.66, "low": 3547.62, "close": 3611.9}, {"time": "2025-08-06", "open": 3612.04, "high": 3698.12, "low": 3567.1, "close": 3683.92}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2025-07-30**
- As-of date (T-1): **2026-03-05**
- Freshness age: **218 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.5, Previous 4.5, Delta +0.0000)
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
