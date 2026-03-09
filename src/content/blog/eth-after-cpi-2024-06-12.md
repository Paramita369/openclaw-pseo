---
title: "ETH Reaction to US CPI (2024-06-12): Quant Probability Breakdown"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-06-12"
asof_date: "2026-03-08"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -2.51
robust_score: -8.51
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 60
sample_size: 39
freshness_days: 634
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.23
hub_baseline_median_t7: -1.18
hub_baseline_std_t7: 9.719
hub_baseline_delta: 1.17
z_score_t7: -0.03
percentile_t7: 56.41
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 313.044
event_previous: 313.175
event_delta: -0.131
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.22
  mdd_t7: -2.54
  volatility: 2.53
  impact_t1_pct: -2.54
  impact_t7_pct: -0.01
probabilities:
  sample_size: 39
  t1:
    up: 58.97
    down: 41.03
    median: 0.94
    mean: 0.55
    sample: 39
  t7:
    up: 43.59
    down: 56.41
    median: -1.18
    mean: 0.23
    sample: 39
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 1
    t1:
      up: 0.0
      down: 100.0
      median: -2.54
      mean: -2.54
      sample: 1
    t7:
      up: 0.0
      down: 100.0
      median: -0.01
      mean: -0.01
      sample: 1
related_events: [{"slug": "eth-after-cpi-2026-02-12", "title": "ETH CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.18, "sample_size": 39}, {"slug": "eth-after-cpi-2026-01-12", "title": "2026-01-12 CPI Release: ETH Directional Probability Snapshot", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.18, "sample_size": 39}, {"slug": "eth-after-cpi-2025-12-12", "title": "ETH Reaction to US CPI (2025-12-12): Quant Probability Breakdown", "event_date": "2025-12-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.18, "sample_size": 39}]
chartData: [{"time": "2024-06-09", "open": 3680.94, "high": 3719.37, "low": 3668.12, "close": 3705.9}, {"time": "2024-06-10", "open": 3705.88, "high": 3711.43, "low": 3648.16, "close": 3666.72}, {"time": "2024-06-11", "open": 3666.36, "high": 3669.89, "low": 3434.75, "close": 3498.33}, {"time": "2024-06-12", "open": 3497.9, "high": 3652.49, "low": 3463.78, "close": 3559.62}, {"time": "2024-06-13", "open": 3559.73, "high": 3559.73, "low": 3431.33, "close": 3469.28}, {"time": "2024-06-14", "open": 3467.97, "high": 3528.6, "low": 3366.22, "close": 3480.27}, {"time": "2024-06-15", "open": 3479.79, "high": 3589.89, "low": 3473.45, "close": 3565.55}, {"time": "2024-06-16", "open": 3566.76, "high": 3648.09, "low": 3541.53, "close": 3620.56}, {"time": "2024-06-17", "open": 3622.38, "high": 3634.29, "low": 3468.15, "close": 3511.38}, {"time": "2024-06-18", "open": 3510.57, "high": 3514.18, "low": 3371.59, "close": 3483.68}, {"time": "2024-06-19", "open": 3482.35, "high": 3583.32, "low": 3466.48, "close": 3559.35}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-06-12**
- As-of date (T-1): **2026-03-08**
- Freshness age: **634 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **DOWN** (Actual 313.044, Previous 313.175, Delta -0.1310)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.94% | 0.55% | 39 |
| T+7 | 43.59% | 56.41% | -1.18% | 0.23% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | -2.54% | -2.54% | 1 |
| T+7 | 0.0% | 100.0% | -0.01% | -0.01% | 1 |

## Historical Distribution Summary

When CPI was **DOWN**, ETH T+1 up probability was **0.0%** (n=1).

When CPI was **DOWN**, ETH T+7 up probability was **0.0%** (n=1).

Same-direction T+7 median return: **-0.01%**.

For ETH, historical CPI windows show all-history T+1 up probability of 58.97% and T+7 up probability of 43.59%. When CPI printed Down versus previous, T+1 up probability was 0.0% and T+7 up probability was 0.0% across 1 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
