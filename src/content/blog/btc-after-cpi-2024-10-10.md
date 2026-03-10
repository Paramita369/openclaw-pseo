---
title: "US CPI (2024-10-10) and BTC: Event-Driven Return Odds"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-10-10"
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
freshness_days: 515
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: 10.71
z_score_t7: 1.75
percentile_t7: 97.44
narrative_trigger: "extreme_outperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:20+00:00"
event_direction: "up"
event_actual: 315.631
event_previous: 314.732
event_delta: 0.899
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 1.44
  mdd_t7: 0.0
  volatility: 8.22
  impact_t1_pct: 3.6
  impact_t7_pct: 11.82
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
chartData: [{"time": "2024-10-07", "open": 62819.11, "high": 64443.71, "low": 62152.55, "close": 62236.66}, {"time": "2024-10-08", "open": 62221.64, "high": 63174.3, "low": 61843.56, "close": 62131.97}, {"time": "2024-10-09", "open": 62131.73, "high": 62508.84, "low": 60314.61, "close": 60582.1}, {"time": "2024-10-10", "open": 60581.93, "high": 61236.72, "low": 58895.21, "close": 60274.5}, {"time": "2024-10-11", "open": 60275.46, "high": 63400.87, "low": 60046.12, "close": 62445.09}, {"time": "2024-10-12", "open": 62444.62, "high": 63448.79, "low": 62443.27, "close": 63193.02}, {"time": "2024-10-13", "open": 63192.95, "high": 63272.65, "low": 62035.64, "close": 62851.38}, {"time": "2024-10-14", "open": 62848.4, "high": 66482.49, "low": 62442.15, "close": 66046.12}, {"time": "2024-10-15", "open": 66050.37, "high": 67881.68, "low": 64809.2, "close": 67041.11}, {"time": "2024-10-16", "open": 67042.46, "high": 68375.29, "low": 66758.73, "close": 67612.72}, {"time": "2024-10-17", "open": 67617.08, "high": 67912.21, "low": 66647.39, "close": 67399.84}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2024-10-10**
- As-of date (T-1): **2026-03-09**
- Freshness age: **515 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 315.631, Previous 314.732, Delta +0.8990)
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
