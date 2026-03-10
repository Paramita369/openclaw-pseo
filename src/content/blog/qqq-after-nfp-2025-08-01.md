---
title: "QQQ Post-NFP Setup (2025-08-01): Historical Probability Lens"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-08-01"
asof_date: "2026-03-09"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 4.14
robust_score: -1.86
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 60
sample_size: 34
freshness_days: 220
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.03
hub_baseline_median_t7: 0.12
hub_baseline_std_t7: 2.5414
hub_baseline_delta: 3.61
z_score_t7: 1.06
percentile_t7: 85.29
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 158472.0
event_previous: 158542.0
event_delta: -70.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.97
  mdd_t7: 0.0
  volatility: 1.89
  impact_t1_pct: 1.85
  impact_t7_pct: 3.73
probabilities:
  sample_size: 34
  t1:
    up: 57.14
    down: 42.86
    median: 0.15
    mean: -0.12
    sample: 21
  t7:
    up: 50.0
    down: 50.0
    median: 0.12
    mean: 1.03
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 3
    t1:
      up: 100.0
      down: 0.0
      median: 0.75
      mean: 0.91
      sample: 3
    t7:
      up: 50.0
      down: 50.0
      median: 1.16
      mean: 0.94
      sample: 4
related_events: [{"slug": "qqq-after-nfp-2025-01-10", "title": "2025-01-10 Nonfarm Payrolls: QQQ Historical Win Rate", "event_date": "2025-01-10", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.64, "median_t7_pct": 0.12, "sample_size": 34}, {"slug": "qqq-after-nfp-2024-12-06", "title": "QQQ After NFP (2024-12-06): Event Probability and Median Return", "event_date": "2024-12-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.77, "median_t7_pct": 0.12, "sample_size": 34}, {"slug": "qqq-after-nfp-2024-08-02", "title": "QQQ After NFP (2024-08-02): Event Probability and Median Return", "event_date": "2024-08-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.35, "median_t7_pct": 0.12, "sample_size": 34}]
chartData: [{"time": "2025-07-29", "open": 569.37, "high": 570.71, "low": 565.15, "close": 565.87}, {"time": "2025-07-30", "open": 566.79, "high": 569.23, "low": 563.67, "close": 566.63}, {"time": "2025-07-31", "open": 573.14, "high": 573.23, "low": 562.49, "close": 563.63}, {"time": "2025-08-01", "open": 557.46, "high": 557.65, "low": 550.33, "close": 552.53}, {"time": "2025-08-04", "open": 557.68, "high": 562.94, "low": 557.58, "close": 562.72}, {"time": "2025-08-05", "open": 564.01, "high": 565.18, "low": 558.36, "close": 558.9}, {"time": "2025-08-06", "open": 559.74, "high": 566.37, "low": 559.26, "close": 565.93}, {"time": "2025-08-07", "open": 570.27, "high": 571.92, "low": 563.73, "close": 567.85}, {"time": "2025-08-08", "open": 569.06, "high": 573.37, "low": 568.76, "close": 573.15}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2025-08-01**
- As-of date (T-1): **2026-03-09**
- Freshness age: **220 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158472.0, Previous 158542.0, Delta -70.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 57.14% | 42.86% | 0.15% | -0.12% | 21 |
| T+7 | 50.0% | 50.0% | 0.12% | 1.03% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 100.0% | 0.0% | 0.75% | 0.91% | 3 |
| T+7 | 50.0% | 50.0% | 1.16% | 0.94% | 4 |

## Historical Distribution Summary

When NFP was **DOWN**, QQQ T+1 up probability was **100.0%** (n=3).

When NFP was **DOWN**, QQQ T+7 up probability was **50.0%** (n=4).

Same-direction T+7 median return: **1.16%**.

For QQQ, historical NFP windows show all-history T+1 up probability of 57.14% and T+7 up probability of 50.0%. When NFP printed Down versus previous, T+1 up probability was 100.0% and T+7 up probability was 50.0% across 3 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
