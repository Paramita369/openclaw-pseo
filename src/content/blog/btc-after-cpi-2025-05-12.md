---
title: "2025-05-12 CPI Release: BTC Directional Probability Snapshot"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 4
title_template_key: "cpi_4"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-05-12"
asof_date: "2026-03-09"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 6.62
robust_score: 0.62
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 39
freshness_days: 301
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: 1.61
z_score_t7: 0.35
percentile_t7: 66.67
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 320.62
event_previous: 320.302
event_delta: 0.318
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 1.94
  mdd_t7: 0.0
  volatility: 1.4
  impact_t1_pct: 1.32
  impact_t7_pct: 2.72
probabilities:
  sample_size: 39
  t1:
    up: 58.97
    down: 41.03
    median: 0.51
    mean: 0.37
    sample: 39
  t7:
    up: 53.85
    down: 46.15
    median: 1.11
    mean: 0.44
    sample: 39
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.53
      mean: 0.44
      sample: 38
    t7:
      up: 55.26
      down: 44.74
      median: 1.26
      mean: 0.58
      sample: 38
related_events: [{"slug": "btc-after-cpi-2024-08-14", "title": "BTC Reaction to US CPI (2024-08-14): Quant Probability Breakdown", "event_date": "2024-08-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.86, "median_t7_pct": 1.11, "sample_size": 39}, {"slug": "btc-after-cpi-2026-02-12", "title": "BTC After CPI (2026-02-12): Up/Down Odds and Median Returns", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 39}, {"slug": "btc-after-cpi-2026-01-12", "title": "BTC CPI Win Rate (2026-01-12): Historical T+1/T+7 Probability", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 39}]
chartData: [{"time": "2025-05-09", "open": 103239.12, "high": 104297.49, "low": 102343.09, "close": 102970.85}, {"time": "2025-05-10", "open": 102973.71, "high": 104961.77, "low": 102830.48, "close": 104696.33}, {"time": "2025-05-11", "open": 104701.07, "high": 104937.99, "low": 103364.74, "close": 104106.36}, {"time": "2025-05-12", "open": 104106.96, "high": 105747.45, "low": 100814.41, "close": 102812.95}, {"time": "2025-05-13", "open": 102812.49, "high": 104997.42, "low": 101515.09, "close": 104169.81}, {"time": "2025-05-14", "open": 104167.33, "high": 104303.56, "low": 102618.3, "close": 103539.41}, {"time": "2025-05-15", "open": 103538.83, "high": 104153.62, "low": 101440.81, "close": 103744.64}, {"time": "2025-05-16", "open": 103735.66, "high": 104533.48, "low": 103137.48, "close": 103489.29}, {"time": "2025-05-17", "open": 103489.29, "high": 103716.95, "low": 102659.18, "close": 103191.09}, {"time": "2025-05-18", "open": 103186.95, "high": 106597.17, "low": 103142.6, "close": 106446.01}, {"time": "2025-05-19", "open": 106430.53, "high": 107068.72, "low": 102112.69, "close": 105606.18}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2025-05-12**
- As-of date (T-1): **2026-03-09**
- Freshness age: **301 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 320.62, Previous 320.302, Delta +0.3180)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.51% | 0.37% | 39 |
| T+7 | 53.85% | 46.15% | 1.11% | 0.44% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.53% | 0.44% | 38 |
| T+7 | 55.26% | 44.74% | 1.26% | 0.58% | 38 |

## Historical Distribution Summary

When CPI was **UP**, BTC T+1 up probability was **60.53%** (n=38).

When CPI was **UP**, BTC T+7 up probability was **55.26%** (n=38).

Same-direction T+7 median return: **1.26%**.

For BTC, historical CPI windows show all-history T+1 up probability of 58.97% and T+7 up probability of 53.85%. When CPI printed Up versus previous, T+1 up probability was 60.53% and T+7 up probability was 55.26% across 38 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
