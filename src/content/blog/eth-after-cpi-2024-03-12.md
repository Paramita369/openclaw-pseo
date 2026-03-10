---
title: "ETH After CPI (2024-03-12): Up/Down Odds and Median Returns"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 5
title_template_key: "cpi_5"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-03-12"
asof_date: "2026-03-09"
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
quality_score: 90
sample_size: 39
freshness_days: 727
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.23
hub_baseline_median_t7: -1.18
hub_baseline_std_t7: 9.719
hub_baseline_delta: -19.49
z_score_t7: -2.15
percentile_t7: 2.56
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:08+00:00"
event_direction: "up"
event_actual: 312.345
event_previous: 310.967
event_delta: 1.378
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -0.97
  mdd_t7: -20.67
  volatility: 21.33
  impact_t1_pct: 0.66
  impact_t7_pct: -20.67
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
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.96
      mean: 0.64
      sample: 38
    t7:
      up: 44.74
      down: 55.26
      median: -1.52
      mean: 0.24
      sample: 38
related_events: [{"slug": "eth-after-cpi-2024-06-12", "title": "ETH Reaction to US CPI (2024-06-12): Quant Probability Breakdown", "event_date": "2024-06-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.22, "median_t7_pct": -1.18, "sample_size": 39}, {"slug": "eth-after-cpi-2026-02-12", "title": "ETH CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.18, "sample_size": 39}, {"slug": "eth-after-cpi-2026-01-12", "title": "2026-01-12 CPI Release: ETH Directional Probability Snapshot", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.18, "sample_size": 39}]
chartData: [{"time": "2024-03-09", "open": 3892.12, "high": 3950.4, "low": 3880.66, "close": 3915.42}, {"time": "2024-03-10", "open": 3915.59, "high": 3968.72, "low": 3800.56, "close": 3881.19}, {"time": "2024-03-11", "open": 3881.24, "high": 4087.05, "low": 3745.13, "close": 4066.45}, {"time": "2024-03-12", "open": 4066.69, "high": 4092.28, "low": 3831.89, "close": 3980.27}, {"time": "2024-03-13", "open": 3980.27, "high": 4083.01, "low": 3936.63, "close": 4006.46}, {"time": "2024-03-14", "open": 4005.75, "high": 4011.1, "low": 3721.79, "close": 3883.14}, {"time": "2024-03-15", "open": 3882.86, "high": 3928.78, "low": 3571.77, "close": 3735.22}, {"time": "2024-03-16", "open": 3736.1, "high": 3780.89, "low": 3468.08, "close": 3522.86}, {"time": "2024-03-17", "open": 3523.03, "high": 3676.26, "low": 3414.17, "close": 3642.41}, {"time": "2024-03-18", "open": 3642.3, "high": 3642.5, "low": 3456.09, "close": 3517.99}, {"time": "2024-03-19", "open": 3518.35, "high": 3546.58, "low": 3149.29, "close": 3157.62}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-03-12**
- As-of date (T-1): **2026-03-09**
- Freshness age: **727 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 312.345, Previous 310.967, Delta +1.3780)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.94% | 0.55% | 39 |
| T+7 | 43.59% | 56.41% | -1.18% | 0.23% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.96% | 0.64% | 38 |
| T+7 | 44.74% | 55.26% | -1.52% | 0.24% | 38 |

## Historical Distribution Summary

When CPI was **UP**, ETH T+1 up probability was **60.53%** (n=38).

When CPI was **UP**, ETH T+7 up probability was **44.74%** (n=38).

Same-direction T+7 median return: **-1.52%**.

For ETH, historical CPI windows show all-history T+1 up probability of 58.97% and T+7 up probability of 43.59%. When CPI printed Up versus previous, T+1 up probability was 60.53% and T+7 up probability was 44.74% across 38 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
