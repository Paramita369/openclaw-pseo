---
title: "2024-08-02 Nonfarm Payrolls: BTC Historical Win Rate"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-08-02"
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
freshness_days: 580
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 3.29
hub_baseline_median_t7: 1.54
hub_baseline_std_t7: 5.8462
hub_baseline_delta: -2.41
z_score_t7: -0.71
percentile_t7: 38.46
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 157757.0
event_previous: 157748.0
event_delta: 9.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -2.64
  mdd_t7: -1.2
  volatility: 0.33
  impact_t1_pct: -1.2
  impact_t7_pct: -0.87
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
chartData: [{"time": "2024-07-30", "open": 66819.05, "high": 66987.67, "low": 65323.19, "close": 66201.02}, {"time": "2024-07-31", "open": 66201.27, "high": 66810.21, "low": 64532.05, "close": 64619.25}, {"time": "2024-08-01", "open": 64625.84, "high": 65593.24, "low": 62248.94, "close": 65357.5}, {"time": "2024-08-02", "open": 65353.5, "high": 65523.22, "low": 61184.89, "close": 61415.07}, {"time": "2024-08-03", "open": 61414.81, "high": 62148.37, "low": 59836.53, "close": 60680.09}, {"time": "2024-08-04", "open": 60676.09, "high": 61062.99, "low": 57210.8, "close": 58116.98}, {"time": "2024-08-05", "open": 58110.3, "high": 58268.83, "low": 49121.24, "close": 53991.46}, {"time": "2024-08-06", "open": 53991.35, "high": 57059.92, "low": 53973.27, "close": 56034.32}, {"time": "2024-08-07", "open": 56040.63, "high": 57726.88, "low": 54620.51, "close": 55027.46}, {"time": "2024-08-08", "open": 55030.03, "high": 62673.77, "low": 54766.73, "close": 61710.14}, {"time": "2024-08-09", "open": 61728.21, "high": 61751.86, "low": 59587.86, "close": 60880.11}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2024-08-02**
- As-of date (T-1): **2026-03-05**
- Freshness age: **580 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 157757.0, Previous 157748.0, Delta +9.0000)
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
