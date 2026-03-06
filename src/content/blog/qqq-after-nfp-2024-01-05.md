---
title: "QQQ Post-NFP Setup (2024-01-05): Historical Probability Lens"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-01-05"
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
freshness_days: 790
freshness_status: "stale"
index_tier: "C"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 1.89
hub_baseline_median_t7: 1.51
hub_baseline_std_t7: 2.1579
hub_baseline_delta: 1.72
z_score_t7: 0.62
percentile_t7: 76.92
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "none"
canonical_url: ""
robots_directive: "noindex,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 157032.0
event_previous: 156857.0
event_delta: 175.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.0
  mdd_t7: 0.0
  volatility: 3.23
  impact_t1_pct: 0.0
  impact_t7_pct: 3.23
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
    median: 1.51
    mean: 1.89
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
      median: 1.38
      mean: 1.81
      sample: 12
related_events: [{"slug": "qqq-after-nfp-2025-01-10", "title": "2025-01-10 Nonfarm Payrolls: QQQ Historical Win Rate", "event_date": "2025-01-10", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.64, "median_t7_pct": 1.51, "sample_size": 13}, {"slug": "qqq-after-nfp-2024-12-06", "title": "QQQ After NFP (2024-12-06): Event Probability and Median Return", "event_date": "2024-12-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.77, "median_t7_pct": 1.51, "sample_size": 13}, {"slug": "qqq-after-nfp-2024-08-02", "title": "QQQ After NFP (2024-08-02): Event Probability and Median Return", "event_date": "2024-08-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.35, "median_t7_pct": 1.51, "sample_size": 13}]
chartData: [{"time": "2024-01-02", "open": 401.41, "high": 401.65, "low": 395.87, "close": 398.19}, {"time": "2024-01-03", "open": 395.56, "high": 396.62, "low": 393.54, "close": 393.98}, {"time": "2024-01-04", "open": 392.11, "high": 395.22, "low": 391.73, "close": 391.95}, {"time": "2024-01-05", "open": 392.12, "high": 395.2, "low": 391.02, "close": 392.42}, {"time": "2024-01-08", "open": 393.64, "high": 400.81, "low": 393.49, "close": 400.53}, {"time": "2024-01-09", "open": 397.52, "high": 402.25, "low": 397.32, "close": 401.32}, {"time": "2024-01-10", "open": 401.63, "high": 405.05, "low": 400.74, "close": 404.04}, {"time": "2024-01-11", "open": 405.31, "high": 406.71, "low": 399.82, "close": 404.88}, {"time": "2024-01-12", "open": 405.92, "high": 406.76, "low": 403.69, "close": 405.09}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
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
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 76.92% | 23.08% | 1.51% | 1.89% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 75.0% | 25.0% | 1.38% | 1.81% | 12 |

## Historical Distribution Summary

When NFP was **UP**, QQQ T+1 up probability was **0.0%** (n=0).

When NFP was **UP**, QQQ T+7 up probability was **75.0%** (n=12).

Same-direction T+7 median return: **1.38%**.

For QQQ, historical NFP windows show all-history T+1 up probability of 0.0% and T+7 up probability of 76.92%. When NFP printed Up versus previous, T+1 up probability was 0.0% and T+7 up probability was 75.0% across 0 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
