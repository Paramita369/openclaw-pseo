---
title: "QQQ Post-NFP Setup (2025-02-07): Historical Probability Lens"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-02-07"
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
freshness_days: 389
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 158310.0
event_previous: 158268.0
event_delta: 42.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 11.24
  impact_t1_pct: 1.21
  impact_t7_pct: 2.91
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
chartData: [{"time": "2025-02-04", "open": 516.01, "high": 522.46, "low": 515.61, "close": 521.82}, {"time": "2025-02-05", "open": 519.19, "high": 524.35, "low": 517.99, "close": 524.19}, {"time": "2025-02-06", "open": 524.7, "high": 527.14, "low": 523.09, "close": 526.93}, {"time": "2025-02-07", "open": 527.46, "high": 529.41, "low": 519.56, "close": 520.28}, {"time": "2025-02-10", "open": 524.56, "high": 527.68, "low": 524.09, "close": 526.58}, {"time": "2025-02-11", "open": 523.31, "high": 527.25, "low": 523.18, "close": 525.33}, {"time": "2025-02-12", "open": 519.66, "high": 526.52, "low": 519.32, "close": 525.63}, {"time": "2025-02-13", "open": 527.31, "high": 533.51, "low": 526.52, "close": 533.2}, {"time": "2025-02-14", "open": 533.31, "high": 536.12, "low": 532.97, "close": 535.43}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2025-02-07**
- As-of date (T-1): **2026-03-03**
- Freshness age: **389 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158310.0, Previous 158268.0, Delta +42.0000)
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
