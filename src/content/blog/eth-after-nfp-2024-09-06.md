---
title: "ETH Post-NFP Setup (2024-09-06): Historical Probability Lens"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-09-06"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Bullish"
raw_signal_score: 8.93
robust_score: 2.93
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 13
freshness_days: 545
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 3.32
hub_baseline_median_t7: 5.12
hub_baseline_std_t7: 8.5559
hub_baseline_delta: 4.67
z_score_t7: 0.76
percentile_t7: 76.92
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 157912.0
event_previous: 157757.0
event_delta: 155.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.3
  mdd_t7: 0.0
  volatility: 7.53
  impact_t1_pct: 2.26
  impact_t7_pct: 9.79
probabilities:
  sample_size: 13
  t1:
    up: 53.85
    down: 46.15
    median: 0.03
    mean: 0.11
    sample: 13
  t7:
    up: 61.54
    down: 38.46
    median: 5.12
    mean: 3.32
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 12
    t1:
      up: 50.0
      down: 50.0
      median: -0.03
      mean: 0.09
      sample: 12
    t7:
      up: 58.33
      down: 41.67
      median: 3.01
      mean: 3.07
      sample: 12
related_events: [{"slug": "eth-after-nfp-2026-02-06", "title": "ETH NFP Reaction (2026-02-06): T+1/T+7 Up Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 5.12, "sample_size": 13}, {"slug": "eth-after-nfp-2026-01-02", "title": "2026-01-02 Nonfarm Payrolls: ETH Historical Win Rate", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 5.12, "sample_size": 13}, {"slug": "eth-after-nfp-2025-12-05", "title": "ETH Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 5.12, "sample_size": 13}]
chartData: [{"time": "2024-09-03", "open": 2538.16, "high": 2552.8, "low": 2419.88, "close": 2420.6}, {"time": "2024-09-04", "open": 2420.19, "high": 2488.92, "low": 2313.27, "close": 2448.98}, {"time": "2024-09-05", "open": 2448.99, "high": 2465.39, "low": 2348.86, "close": 2367.74}, {"time": "2024-09-06", "open": 2367.7, "high": 2406.51, "low": 2150.86, "close": 2223.88}, {"time": "2024-09-07", "open": 2223.93, "high": 2310.19, "low": 2222.1, "close": 2274.11}, {"time": "2024-09-08", "open": 2274.44, "high": 2332.36, "low": 2243.91, "close": 2297.29}, {"time": "2024-09-09", "open": 2297.9, "high": 2379.79, "low": 2274.12, "close": 2358.48}, {"time": "2024-09-10", "open": 2358.5, "high": 2398.5, "low": 2323.07, "close": 2389.58}, {"time": "2024-09-11", "open": 2389.6, "high": 2389.72, "low": 2279.05, "close": 2339.84}, {"time": "2024-09-12", "open": 2339.84, "high": 2390.19, "low": 2316.16, "close": 2361.78}, {"time": "2024-09-13", "open": 2361.74, "high": 2462.8, "low": 2338.14, "close": 2441.61}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2024-09-06**
- As-of date (T-1): **2026-03-05**
- Freshness age: **545 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 157912.0, Previous 157757.0, Delta +155.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.03% | 0.11% | 13 |
| T+7 | 61.54% | 38.46% | 5.12% | 3.32% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.03% | 0.09% | 12 |
| T+7 | 58.33% | 41.67% | 3.01% | 3.07% | 12 |

## Historical Distribution Summary

When NFP was **UP**, ETH T+1 up probability was **50.0%** (n=12).

When NFP was **UP**, ETH T+7 up probability was **58.33%** (n=12).

Same-direction T+7 median return: **3.01%**.

For ETH, historical NFP windows show all-history T+1 up probability of 53.85% and T+7 up probability of 61.54%. When NFP printed Up versus previous, T+1 up probability was 50.0% and T+7 up probability was 58.33% across 12 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
