---
title: "NFP Print (2024-11-01) vs QQQ: Quantified Directional Odds"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 4
title_template_key: "nfp_4"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-11-01"
asof_date: "2026-03-03"
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
quality_score: 80
sample_size: 34
freshness_days: 487
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 158079.0
event_previous: 157945.0
event_delta: 134.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.98
  mdd_t7: -0.12
  volatility: 5.6
  impact_t1_pct: -0.12
  impact_t7_pct: 5.48
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
    direction: "up"
    sample_size: 18
    t1:
      up: 50.0
      down: 50.0
      median: -0.05
      mean: -0.29
      sample: 18
    t7:
      up: 50.0
      down: 50.0
      median: 0.12
      mean: 1.05
      sample: 30
related_events: [{"slug": "qqq-after-nfp-2026-01-02", "title": "QQQ After NFP (2026-01-02): Historical T+1/T+7 Probability", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.21, "sample_size": 0}, {"slug": "qqq-after-nfp-2025-11-20", "title": "QQQ After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 5.73, "sample_size": 0}, {"slug": "qqq-after-nfp-2025-09-05", "title": "QQQ After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.84, "sample_size": 0}]
chartData: [{"time": "2024-10-29", "open": 492.42, "high": 498.02, "low": 490.57, "close": 496.84}, {"time": "2024-10-30", "open": 496.07, "high": 497.02, "low": 492.59, "close": 493.08}, {"time": "2024-10-31", "open": 489.11, "high": 489.16, "low": 480.53, "close": 480.63}, {"time": "2024-11-01", "open": 482.27, "high": 487.49, "low": 481.97, "close": 484.19}, {"time": "2024-11-04", "open": 483.58, "high": 486.13, "low": 481.03, "close": 482.78}, {"time": "2024-11-05", "open": 484.37, "high": 489.6, "low": 484.28, "close": 488.94}, {"time": "2024-11-06", "open": 497.23, "high": 503.04, "low": 496.28, "close": 502.22}, {"time": "2024-11-07", "open": 505.02, "high": 510.91, "low": 504.96, "close": 510.13}, {"time": "2024-11-08", "open": 509.63, "high": 511.5, "low": 509.0, "close": 510.72}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2024-11-01**
- As-of date (T-1): **2026-03-03**
- Freshness age: **487 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158079.0, Previous 157945.0, Delta +134.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 57.14% | 42.86% | 0.15% | -0.12% | 21 |
| T+7 | 50.0% | 50.0% | 0.12% | 1.03% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.05% | -0.29% | 18 |
| T+7 | 50.0% | 50.0% | 0.12% | 1.05% | 30 |

## Historical Distribution Summary

When NFP was **UP**, QQQ T+1 up probability was **50.0%** (n=18).

When NFP was **UP**, QQQ T+7 up probability was **50.0%** (n=30).

Same-direction T+7 median return: **0.12%**.

For QQQ, historical NFP windows show all-history T+1 up probability of 57.14% and T+7 up probability of 50.0%. When NFP printed Up versus previous, T+1 up probability was 50.0% and T+7 up probability was 50.0% across 18 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
