---
title: "SPY NFP Reaction (2024-10-04): T+1/T+7 Up Probability"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 1
title_template_key: "nfp_1"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-10-04"
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
freshness_days: 517
freshness_status: "stale"
index_tier: "C"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 1.41
hub_baseline_median_t7: 1.39
hub_baseline_std_t7: 1.7058
hub_baseline_delta: -0.24
z_score_t7: -0.15
percentile_t7: 46.15
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "none"
canonical_url: ""
robots_directive: "noindex,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 157945.0
event_previous: 157912.0
event_delta: 33.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 3.43
  mdd_t7: -1.11
  volatility: 1.15
  impact_t1_pct: 0.0
  impact_t7_pct: 1.15
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
related_events: [{"slug": "spy-after-nfp-2024-07-05", "title": "2024-07-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-07-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.02, "median_t7_pct": 1.39, "sample_size": 13}, {"slug": "spy-after-nfp-2024-01-05", "title": "2024-01-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-01-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.04, "median_t7_pct": 1.39, "sample_size": 13}, {"slug": "spy-after-nfp-2024-08-02", "title": "NFP Print (2024-08-02) vs SPY: Quantified Directional Odds", "event_date": "2024-08-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 2.25, "median_t7_pct": 1.39, "sample_size": 13}]
chartData: [{"time": "2024-10-01", "open": 564.84, "high": 565.49, "low": 557.55, "close": 560.13}, {"time": "2024-10-02", "open": 559.24, "high": 561.4, "low": 556.83, "close": 560.37}, {"time": "2024-10-03", "open": 558.89, "high": 561.3, "low": 557.05, "close": 559.35}, {"time": "2024-10-04", "open": 563.81, "high": 564.8, "low": 559.62, "close": 564.43}, {"time": "2024-10-07", "open": 562.77, "high": 563.43, "low": 558.17, "close": 559.33}, {"time": "2024-10-08", "open": 561.91, "high": 565.22, "low": 561.03, "close": 564.62}, {"time": "2024-10-09", "open": 564.61, "high": 569.09, "low": 564.01, "close": 568.53}, {"time": "2024-10-10", "open": 567.18, "high": 568.96, "low": 565.92, "close": 567.53}, {"time": "2024-10-11", "open": 567.45, "high": 571.67, "low": 567.32, "close": 570.93}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2024-10-04**
- As-of date (T-1): **2026-03-05**
- Freshness age: **517 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 157945.0, Previous 157912.0, Delta +33.0000)
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
