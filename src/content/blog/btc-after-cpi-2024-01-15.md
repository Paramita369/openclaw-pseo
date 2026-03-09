---
title: "BTC CPI Win Rate (2024-01-15): Historical T+1/T+7 Probability"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-01-15"
asof_date: "2026-03-08"
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
freshness_days: 783
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: -8.18
z_score_t7: -1.15
percentile_t7: 15.38
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:02+00:00"
event_direction: "up"
event_actual: 309.698
event_previous: 308.741
event_delta: 0.957
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -0.82
  mdd_t7: -7.07
  volatility: 8.58
  impact_t1_pct: 1.51
  impact_t7_pct: -7.07
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
related_events: [{"slug": "btc-after-cpi-2024-08-14", "title": "BTC Reaction to US CPI (2024-08-14): Quant Probability Breakdown", "event_date": "2024-08-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.86, "median_t7_pct": 3.64, "sample_size": 14}, {"slug": "btc-after-cpi-2026-02-12", "title": "BTC After CPI (2026-02-12): Up/Down Odds and Median Returns", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 39}, {"slug": "btc-after-cpi-2026-01-12", "title": "BTC CPI Win Rate (2026-01-12): Historical T+1/T+7 Probability", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 39}]
chartData: [{"time": "2024-01-12", "open": 46354.79, "high": 46498.14, "low": 41903.77, "close": 42853.17}, {"time": "2024-01-13", "open": 42799.45, "high": 43234.66, "low": 42464.14, "close": 42842.38}, {"time": "2024-01-14", "open": 42842.26, "high": 43065.6, "low": 41724.61, "close": 41796.27}, {"time": "2024-01-15", "open": 41715.07, "high": 43319.72, "low": 41705.42, "close": 42511.97}, {"time": "2024-01-16", "open": 42499.34, "high": 43566.27, "low": 42086.0, "close": 43154.95}, {"time": "2024-01-17", "open": 43132.1, "high": 43189.89, "low": 42189.31, "close": 42742.65}, {"time": "2024-01-18", "open": 42742.31, "high": 42876.35, "low": 40631.17, "close": 41262.06}, {"time": "2024-01-19", "open": 41278.46, "high": 42134.16, "low": 40297.46, "close": 41618.41}, {"time": "2024-01-20", "open": 41624.59, "high": 41877.89, "low": 41446.82, "close": 41665.59}, {"time": "2024-01-21", "open": 41671.49, "high": 41855.37, "low": 41497.01, "close": 41545.79}, {"time": "2024-01-22", "open": 41553.65, "high": 41651.21, "low": 39450.12, "close": 39507.37}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2024-01-15**
- As-of date (T-1): **2026-03-08**
- Freshness age: **783 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 309.698, Previous 308.741, Delta +0.9570)
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
