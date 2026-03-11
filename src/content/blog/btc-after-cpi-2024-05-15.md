---
title: "BTC Reaction to US CPI (2024-05-15): Quant Probability Breakdown"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-05-15"
asof_date: "2026-03-10"
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
freshness_days: 664
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: 3.2
z_score_t7: 0.59
percentile_t7: 79.49
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:11+00:00"
event_direction: "up"
event_actual: 313.175
event_previous: 313.023
event_delta: 0.152
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.73
  mdd_t7: -1.56
  volatility: 5.87
  impact_t1_pct: -1.56
  impact_t7_pct: 4.31
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
chartData: [{"time": "2024-05-12", "open": 60793.5, "high": 61818.16, "low": 60632.6, "close": 61448.39}, {"time": "2024-05-13", "open": 61451.22, "high": 63422.66, "low": 60769.84, "close": 62901.45}, {"time": "2024-05-14", "open": 62900.77, "high": 63092.12, "low": 61123.77, "close": 61552.79}, {"time": "2024-05-15", "open": 61553.99, "high": 66454.45, "low": 61330.41, "close": 66267.49}, {"time": "2024-05-16", "open": 66256.11, "high": 66712.43, "low": 64613.05, "close": 65231.58}, {"time": "2024-05-17", "open": 65231.3, "high": 67459.46, "low": 65119.32, "close": 67051.88}, {"time": "2024-05-18", "open": 67066.21, "high": 67387.33, "low": 66663.5, "close": 66940.8}, {"time": "2024-05-19", "open": 66937.93, "high": 67694.3, "low": 65937.18, "close": 66278.37}, {"time": "2024-05-20", "open": 66278.74, "high": 71483.56, "low": 66086.17, "close": 71448.2}, {"time": "2024-05-21", "open": 71443.06, "high": 71946.46, "low": 69191.12, "close": 70136.53}, {"time": "2024-05-22", "open": 70135.32, "high": 70623.7, "low": 68977.7, "close": 69122.34}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2024-05-15**
- As-of date (T-1): **2026-03-10**
- Freshness age: **664 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 313.175, Previous 313.023, Delta +0.1520)
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
