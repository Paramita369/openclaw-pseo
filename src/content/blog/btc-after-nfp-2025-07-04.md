---
title: "BTC After NFP (2025-07-04): Event Probability and Median Return"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "nfp_3"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-07-04"
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
quality_score: 70
sample_size: 13
freshness_days: 244
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 3.29
hub_baseline_median_t7: 1.54
hub_baseline_std_t7: 5.8462
hub_baseline_delta: 1.75
z_score_t7: 0.0
percentile_t7: 61.54
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 158542.0
event_previous: 158478.0
event_delta: 64.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.08
  mdd_t7: 0.0
  volatility: 3.04
  impact_t1_pct: 0.25
  impact_t7_pct: 3.29
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
chartData: [{"time": "2025-07-01", "open": 107144.38, "high": 107550.68, "low": 105270.23, "close": 105698.28}, {"time": "2025-07-02", "open": 105703.1, "high": 109763.66, "low": 105157.4, "close": 108859.32}, {"time": "2025-07-03", "open": 108845.02, "high": 110541.46, "low": 108605.8, "close": 109647.98}, {"time": "2025-07-04", "open": 109635.66, "high": 109751.98, "low": 107296.38, "close": 108034.34}, {"time": "2025-07-05", "open": 108015.84, "high": 108381.34, "low": 107842.27, "close": 108231.18}, {"time": "2025-07-06", "open": 108231.19, "high": 109731.62, "low": 107847.02, "close": 109232.07}, {"time": "2025-07-07", "open": 109235.33, "high": 109710.25, "low": 107527.05, "close": 108299.85}, {"time": "2025-07-08", "open": 108298.23, "high": 109198.97, "low": 107499.55, "close": 108950.27}, {"time": "2025-07-09", "open": 108950.27, "high": 111925.38, "low": 108357.68, "close": 111326.55}, {"time": "2025-07-10", "open": 111329.2, "high": 116608.78, "low": 110660.75, "close": 115987.2}, {"time": "2025-07-11", "open": 115986.23, "high": 118856.48, "low": 115245.69, "close": 117516.99}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-07-04**
- As-of date (T-1): **2026-03-05**
- Freshness age: **244 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 158542.0, Previous 158478.0, Delta +64.0000)
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
