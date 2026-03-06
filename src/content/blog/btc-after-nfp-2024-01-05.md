---
title: "BTC Post-NFP Setup (2024-01-05): Historical Probability Lens"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-01-05"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 4.31
robust_score: -1.69
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 13
freshness_days: 790
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 3.29
hub_baseline_median_t7: 1.54
hub_baseline_std_t7: 5.8462
hub_baseline_delta: -4.51
z_score_t7: -1.07
percentile_t7: 23.08
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 157032.0
event_previous: 156857.0
event_delta: 175.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -1.15
  mdd_t7: -2.97
  volatility: 2.58
  impact_t1_pct: -0.39
  impact_t7_pct: -2.97
probabilities:
  sample_size: 13
  t1:
    up: 38.46
    down: 61.54
    median: -0.05
    mean: 0.25
    sample: 13
  t7:
    up: 61.54
    down: 38.46
    median: 1.54
    mean: 3.29
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 12
    t1:
      up: 41.67
      down: 58.33
      median: -0.03
      mean: 0.28
      sample: 12
    t7:
      up: 58.33
      down: 41.67
      median: 1.07
      mean: 2.7
      sample: 12
related_events: [{"slug": "btc-after-nfp-2026-02-06", "title": "BTC Post-NFP Setup (2026-02-06): Historical Probability Lens", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.54, "sample_size": 13}, {"slug": "btc-after-nfp-2026-01-02", "title": "NFP Print (2026-01-02) vs BTC: Quantified Directional Odds", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.54, "sample_size": 13}, {"slug": "btc-after-nfp-2025-12-05", "title": "BTC Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.54, "sample_size": 13}]
chartData: [{"time": "2024-01-02", "open": 44187.14, "high": 45899.71, "low": 44176.95, "close": 44957.97}, {"time": "2024-01-03", "open": 44961.6, "high": 45503.24, "low": 40813.54, "close": 42848.18}, {"time": "2024-01-04", "open": 42855.82, "high": 44770.02, "low": 42675.18, "close": 44179.92}, {"time": "2024-01-05", "open": 44192.98, "high": 44353.29, "low": 42784.72, "close": 44162.69}, {"time": "2024-01-06", "open": 44178.95, "high": 44227.63, "low": 43475.16, "close": 43989.2}, {"time": "2024-01-07", "open": 43998.46, "high": 44495.57, "low": 43662.23, "close": 43943.1}, {"time": "2024-01-08", "open": 43948.71, "high": 47218.0, "low": 43244.08, "close": 46970.5}, {"time": "2024-01-09", "open": 46987.64, "high": 47893.7, "low": 45244.71, "close": 46139.73}, {"time": "2024-01-10", "open": 46121.54, "high": 47647.22, "low": 44483.15, "close": 46627.78}, {"time": "2024-01-11", "open": 46656.07, "high": 48969.37, "low": 45678.64, "close": 46368.59}, {"time": "2024-01-12", "open": 46354.79, "high": 46498.14, "low": 41903.77, "close": 42853.17}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2024-01-05**
- As-of date (T-1): **2026-03-05**
- Freshness age: **790 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 157032.0, Previous 156857.0, Delta +175.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 38.46% | 61.54% | -0.05% | 0.25% | 13 |
| T+7 | 61.54% | 38.46% | 1.54% | 3.29% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 41.67% | 58.33% | -0.03% | 0.28% | 12 |
| T+7 | 58.33% | 41.67% | 1.07% | 2.7% | 12 |

## Historical Distribution Summary

When NFP was **UP**, BTC T+1 up probability was **41.67%** (n=12).

When NFP was **UP**, BTC T+7 up probability was **58.33%** (n=12).

Same-direction T+7 median return: **1.07%**.

For BTC, historical NFP windows show all-history T+1 up probability of 38.46% and T+7 up probability of 61.54%. When NFP printed Up versus previous, T+1 up probability was 41.67% and T+7 up probability was 58.33% across 12 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
