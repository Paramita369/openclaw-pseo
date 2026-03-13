---
title: "ETH Post-NFP Setup (2024-09-06): Historical Probability Lens"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-12"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-09-06"
asof_date: "2026-03-11"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 4.94
robust_score: -1.06
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 34
freshness_days: 551
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 2.65
hub_baseline_median_t7: 1.44
hub_baseline_std_t7: 9.723
hub_baseline_delta: 8.35
z_score_t7: 0.73
percentile_t7: 79.41
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:42+00:00"
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
  sample_size: 34
  t1:
    up: 50.0
    down: 50.0
    median: 0.0
    mean: -0.15
    sample: 34
  t7:
    up: 55.88
    down: 44.12
    median: 1.44
    mean: 2.65
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 30
    t1:
      up: 50.0
      down: 50.0
      median: 0.0
      mean: -0.14
      sample: 30
    t7:
      up: 53.33
      down: 46.67
      median: 0.79
      mean: 2.65
      sample: 30
related_events: [{"slug": "eth-after-nfp-2026-02-06", "title": "ETH NFP Reaction (2026-02-06): T+1/T+7 Up Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}, {"slug": "eth-after-nfp-2026-01-02", "title": "2026-01-02 Nonfarm Payrolls: ETH Historical Win Rate", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}, {"slug": "eth-after-nfp-2025-12-05", "title": "ETH Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}]
chartData: [{"time": "2024-09-03", "open": 2538.16, "high": 2552.8, "low": 2419.88, "close": 2420.6}, {"time": "2024-09-04", "open": 2420.19, "high": 2488.92, "low": 2313.27, "close": 2448.98}, {"time": "2024-09-05", "open": 2448.99, "high": 2465.39, "low": 2348.86, "close": 2367.74}, {"time": "2024-09-06", "open": 2367.7, "high": 2406.51, "low": 2150.86, "close": 2223.88}, {"time": "2024-09-07", "open": 2223.93, "high": 2310.19, "low": 2222.1, "close": 2274.11}, {"time": "2024-09-08", "open": 2274.44, "high": 2332.36, "low": 2243.91, "close": 2297.29}, {"time": "2024-09-09", "open": 2297.9, "high": 2379.79, "low": 2274.12, "close": 2358.48}, {"time": "2024-09-10", "open": 2358.5, "high": 2398.5, "low": 2323.07, "close": 2389.58}, {"time": "2024-09-11", "open": 2389.6, "high": 2389.72, "low": 2279.05, "close": 2339.84}, {"time": "2024-09-12", "open": 2339.84, "high": 2390.19, "low": 2316.16, "close": 2361.78}, {"time": "2024-09-13", "open": 2361.74, "high": 2462.8, "low": 2338.14, "close": 2441.61}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2024-09-06**
- As-of date (T-1): **2026-03-11**
- Freshness age: **551 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157912.0, Previous 157757.0, Delta +155.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.15% | 34 |
| T+7 | 55.88% | 44.12% | 1.44% | 2.65% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.14% | 30 |
| T+7 | 53.33% | 46.67% | 0.79% | 2.65% | 30 |

## Historical Distribution Summary

When NFP was **UP**, ETH T+1 up probability was **50.0%** (n=30).

When NFP was **UP**, ETH T+7 up probability was **53.33%** (n=30).

Same-direction T+7 median return: **0.79%**.

For ETH, historical NFP windows show all-history T+1 up probability of 50.0% and T+7 up probability of 55.88%. When NFP printed Up versus previous, T+1 up probability was 50.0% and T+7 up probability was 53.33% across 30 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
