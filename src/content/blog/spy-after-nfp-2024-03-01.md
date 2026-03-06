---
title: "2024-03-01 Nonfarm Payrolls: SPY Historical Win Rate"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-03-01"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 0.46
robust_score: -5.54
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 50
sample_size: 13
freshness_days: 734
freshness_status: "stale"
index_tier: "C"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 1.41
hub_baseline_median_t7: 1.39
hub_baseline_std_t7: 1.7058
hub_baseline_delta: -1.61
z_score_t7: -0.96
percentile_t7: 23.08
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "none"
canonical_url: ""
robots_directive: "noindex,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 157466.0
event_previous: 157238.0
event_delta: 228.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -1.0
  mdd_t7: -0.22
  volatility: 0.22
  impact_t1_pct: 0.0
  impact_t7_pct: -0.22
probabilities:
  sample_size: 13
  t1:
    up: 0.0
    down: 100.0
    median: 0.0
    mean: 0.0
    sample: 0
  t7:
    up: 76.92
    down: 23.08
    median: 1.39
    mean: 1.41
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 0
    t1:
      up: 0.0
      down: 100.0
      median: 0.0
      mean: 0.0
      sample: 0
    t7:
      up: 75.0
      down: 25.0
      median: 1.27
      mean: 1.28
      sample: 12
related_events: [{"slug": "spy-after-nfp-2024-07-05", "title": "2024-07-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-07-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.02, "median_t7_pct": 1.39, "sample_size": 13}, {"slug": "spy-after-nfp-2024-01-05", "title": "2024-01-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-01-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.04, "median_t7_pct": 1.39, "sample_size": 13}, {"slug": "spy-after-nfp-2024-10-04", "title": "SPY NFP Reaction (2024-10-04): T+1/T+7 Up Probability", "event_date": "2024-10-04", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.43, "median_t7_pct": 1.39, "sample_size": 13}]
chartData: [{"time": "2024-02-27", "open": 494.48, "high": 494.92, "low": 492.57, "close": 494.7}, {"time": "2024-02-28", "open": 493.14, "high": 494.63, "low": 492.78, "close": 494.05}, {"time": "2024-02-29", "open": 495.81, "high": 497.44, "low": 493.16, "close": 495.82}, {"time": "2024-03-01", "open": 496.7, "high": 500.91, "low": 496.29, "close": 500.48}, {"time": "2024-03-04", "open": 499.68, "high": 501.8, "low": 499.65, "close": 499.94}, {"time": "2024-03-05", "open": 497.93, "high": 498.38, "low": 492.73, "close": 494.94}, {"time": "2024-03-06", "open": 498.23, "high": 499.72, "low": 496.15, "close": 497.45}, {"time": "2024-03-07", "open": 500.76, "high": 503.44, "low": 497.51, "close": 502.39}, {"time": "2024-03-08", "open": 503.02, "high": 505.72, "low": 498.8, "close": 499.37}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2024-03-01**
- As-of date (T-1): **2026-03-05**
- Freshness age: **734 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 157466.0, Previous 157238.0, Delta +228.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 76.92% | 23.08% | 1.39% | 1.41% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 75.0% | 25.0% | 1.27% | 1.28% | 12 |

## Historical Distribution Summary

When NFP was **UP**, SPY T+1 up probability was **0.0%** (n=0).

When NFP was **UP**, SPY T+7 up probability was **75.0%** (n=12).

Same-direction T+7 median return: **1.27%**.

For SPY, historical NFP windows show all-history T+1 up probability of 0.0% and T+7 up probability of 76.92%. When NFP printed Up versus previous, T+1 up probability was 0.0% and T+7 up probability was 75.0% across 0 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
