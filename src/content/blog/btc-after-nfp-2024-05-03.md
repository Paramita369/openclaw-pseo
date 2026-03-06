---
title: "2024-05-03 Nonfarm Payrolls: BTC Historical Win Rate"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-05-03"
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
freshness_days: 671
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 3.29
hub_baseline_median_t7: 1.54
hub_baseline_std_t7: 5.8462
hub_baseline_delta: -4.87
z_score_t7: -1.13
percentile_t7: 15.38
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 157608.0
event_previous: 157530.0
event_delta: 78.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -9.66
  mdd_t7: -4.85
  volatility: 4.92
  impact_t1_pct: 1.59
  impact_t7_pct: -3.33
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
chartData: [{"time": "2024-04-30", "open": 63839.42, "high": 64703.33, "low": 59120.07, "close": 60636.86}, {"time": "2024-05-01", "open": 60609.5, "high": 60780.5, "low": 56555.29, "close": 58254.01}, {"time": "2024-05-02", "open": 58253.7, "high": 59602.3, "low": 56937.2, "close": 59123.43}, {"time": "2024-05-03", "open": 59122.3, "high": 63320.5, "low": 58848.31, "close": 62889.84}, {"time": "2024-05-04", "open": 62891.03, "high": 64494.96, "low": 62599.35, "close": 63891.47}, {"time": "2024-05-05", "open": 63892.45, "high": 64610.89, "low": 62955.3, "close": 64031.13}, {"time": "2024-05-06", "open": 64038.31, "high": 65494.9, "low": 62746.24, "close": 63161.95}, {"time": "2024-05-07", "open": 63162.76, "high": 64390.46, "low": 62285.98, "close": 62334.82}, {"time": "2024-05-08", "open": 62332.64, "high": 62986.09, "low": 60877.13, "close": 61187.94}, {"time": "2024-05-09", "open": 61191.2, "high": 63404.91, "low": 60648.07, "close": 63049.96}, {"time": "2024-05-10", "open": 63055.19, "high": 63446.74, "low": 60208.78, "close": 60792.78}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2024-05-03**
- As-of date (T-1): **2026-03-05**
- Freshness age: **671 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 157608.0, Previous 157530.0, Delta +78.0000)
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
