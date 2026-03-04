---
title: "QQQ After NFP (2026-01-02): Event Probability and Median Return"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 3
title_template_key: "nfp_3"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-01-02"
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
quality_score: 100
sample_size: 34
freshness_days: 60
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/qqq-after-nfp-2026-01-02"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 158627.0
event_previous: 158497.0
event_delta: 130.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 9.11
  impact_t1_pct: 0.79
  impact_t7_pct: 2.21
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
related_events: [{"slug": "qqq-after-nfp-2025-11-20", "title": "QQQ After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 5.73, "sample_size": 0}, {"slug": "qqq-after-nfp-2025-09-05", "title": "QQQ After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.84, "sample_size": 0}, {"slug": "qqq-after-nfp-2025-08-01", "title": "QQQ After NFP (2025-08-01): Historical T+1/T+7 Probability", "event_date": "2025-08-01", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.73, "sample_size": 0}]
chartData: [{"time": "2025-12-30", "open": 619.84, "high": 622.18, "low": 619.22, "close": 619.43}, {"time": "2025-12-31", "open": 619.65, "high": 619.96, "low": 614.05, "close": 614.31}, {"time": "2026-01-02", "open": 620.06, "high": 622.85, "low": 610.15, "close": 613.12}, {"time": "2026-01-05", "open": 619.32, "high": 620.81, "low": 616.72, "close": 617.99}, {"time": "2026-01-06", "open": 619.23, "high": 624.02, "low": 618.54, "close": 623.42}, {"time": "2026-01-07", "open": 623.04, "high": 627.94, "low": 622.56, "close": 624.02}, {"time": "2026-01-08", "open": 623.03, "high": 623.42, "low": 617.8, "close": 620.47}, {"time": "2026-01-09", "open": 621.41, "high": 627.89, "low": 619.06, "close": 626.65}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2026-01-02**
- As-of date (T-1): **2026-03-03**
- Freshness age: **60 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158627.0, Previous 158497.0, Delta +130.0000)
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
