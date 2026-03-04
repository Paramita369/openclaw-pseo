---
title: "QQQ Post-NFP Setup (2025-09-05): Historical Probability Lens"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-09-05"
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
freshness_days: 179
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 158548.0
event_previous: 158472.0
event_delta: 76.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 8.83
  impact_t1_pct: 0.49
  impact_t7_pct: 1.84
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
related_events: [{"slug": "qqq-after-nfp-2026-01-02", "title": "QQQ After NFP (2026-01-02): Historical T+1/T+7 Probability", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.21, "sample_size": 0}, {"slug": "qqq-after-nfp-2025-11-20", "title": "QQQ After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 5.73, "sample_size": 0}, {"slug": "qqq-after-nfp-2025-08-01", "title": "QQQ After NFP (2025-08-01): Historical T+1/T+7 Probability", "event_date": "2025-08-01", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.73, "sample_size": 0}]
chartData: [{"time": "2025-09-02", "open": 559.94, "high": 564.59, "low": 558.17, "close": 564.24}, {"time": "2025-09-03", "open": 567.84, "high": 570.3, "low": 565.35, "close": 568.68}, {"time": "2025-09-04", "open": 569.35, "high": 574.19, "low": 567.64, "close": 573.82}, {"time": "2025-09-05", "open": 579.07, "high": 579.7, "low": 570.13, "close": 574.65}, {"time": "2025-09-08", "open": 576.96, "high": 579.42, "low": 576.36, "close": 577.46}, {"time": "2025-09-09", "open": 578.25, "high": 579.52, "low": 575.63, "close": 579.09}, {"time": "2025-09-10", "open": 582.31, "high": 582.34, "low": 577.14, "close": 579.28}, {"time": "2025-09-11", "open": 581.82, "high": 583.45, "low": 580.2, "close": 582.65}, {"time": "2025-09-12", "open": 583.61, "high": 586.42, "low": 582.67, "close": 585.23}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2025-09-05**
- As-of date (T-1): **2026-03-03**
- Freshness age: **179 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158548.0, Previous 158472.0, Delta +76.0000)
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
