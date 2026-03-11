---
title: "ETH Reaction to US CPI (2024-09-11): Quant Probability Breakdown"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-09-11"
asof_date: "2026-03-10"
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
freshness_days: 545
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 0.23
hub_baseline_median_t7: -1.18
hub_baseline_std_t7: 9.719
hub_baseline_delta: 2.46
z_score_t7: 0.11
percentile_t7: 61.54
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:19+00:00"
event_direction: "up"
event_actual: 314.732
event_previous: 314.062
event_delta: 0.67
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 3.76
  mdd_t7: 0.0
  volatility: 0.34
  impact_t1_pct: 0.94
  impact_t7_pct: 1.28
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
chartData: [{"time": "2024-09-08", "open": 2274.44, "high": 2332.36, "low": 2243.91, "close": 2297.29}, {"time": "2024-09-09", "open": 2297.9, "high": 2379.79, "low": 2274.12, "close": 2358.48}, {"time": "2024-09-10", "open": 2358.5, "high": 2398.5, "low": 2323.07, "close": 2389.58}, {"time": "2024-09-11", "open": 2389.6, "high": 2389.72, "low": 2279.05, "close": 2339.84}, {"time": "2024-09-12", "open": 2339.84, "high": 2390.19, "low": 2316.16, "close": 2361.78}, {"time": "2024-09-13", "open": 2361.74, "high": 2462.8, "low": 2338.14, "close": 2441.61}, {"time": "2024-09-14", "open": 2441.58, "high": 2442.63, "low": 2386.98, "close": 2418.6}, {"time": "2024-09-15", "open": 2418.27, "high": 2430.38, "low": 2286.63, "close": 2320.9}, {"time": "2024-09-16", "open": 2320.89, "high": 2334.79, "low": 2253.72, "close": 2295.28}, {"time": "2024-09-17", "open": 2295.28, "high": 2392.15, "low": 2263.79, "close": 2341.71}, {"time": "2024-09-18", "open": 2341.73, "high": 2369.73, "low": 2278.66, "close": 2369.73}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-09-11**
- As-of date (T-1): **2026-03-10**
- Freshness age: **545 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 314.732, Previous 314.062, Delta +0.6700)
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
