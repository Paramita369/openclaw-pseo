---
title: "BTC CPI Win Rate (2024-12-11): Historical T+1/T+7 Probability"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-12-11"
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
freshness_days: 454
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: -2.23
z_score_t7: -0.24
percentile_t7: 41.03
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:24+00:00"
event_direction: "up"
event_actual: 317.604
event_previous: 316.528
event_delta: 1.076
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -1.12
  mdd_t7: -1.12
  volatility: 0.0
  impact_t1_pct: -1.12
  impact_t7_pct: -1.12
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
chartData: [{"time": "2024-12-08", "open": 99921.91, "high": 101399.99, "low": 98771.52, "close": 101236.02}, {"time": "2024-12-09", "open": 101237.06, "high": 101272.51, "low": 94355.91, "close": 97432.72}, {"time": "2024-12-10", "open": 97441.23, "high": 98270.16, "low": 94321.26, "close": 96675.43}, {"time": "2024-12-11", "open": 96656.06, "high": 101913.36, "low": 95747.23, "close": 101173.03}, {"time": "2024-12-12", "open": 101167.8, "high": 102524.91, "low": 99339.95, "close": 100043.0}, {"time": "2024-12-13", "open": 100046.65, "high": 101888.8, "low": 99233.28, "close": 101459.26}, {"time": "2024-12-14", "open": 101451.44, "high": 102618.88, "low": 100634.05, "close": 101372.97}, {"time": "2024-12-15", "open": 101373.53, "high": 105047.54, "low": 101227.03, "close": 104298.7}, {"time": "2024-12-16", "open": 104293.58, "high": 107780.58, "low": 103322.98, "close": 106029.72}, {"time": "2024-12-17", "open": 106030.69, "high": 108268.45, "low": 105291.73, "close": 106140.6}, {"time": "2024-12-18", "open": 106147.3, "high": 106470.61, "low": 100041.54, "close": 100041.54}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2024-12-11**
- As-of date (T-1): **2026-03-10**
- Freshness age: **454 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 317.604, Previous 316.528, Delta +1.0760)
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
