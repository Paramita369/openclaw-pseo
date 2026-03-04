---
title: "NFP Print (2025-12-16) vs QQQ: Quantified Directional Odds"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 4
title_template_key: "nfp_4"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-12-16"
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
freshness_days: 77
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/qqq-after-nfp-2025-12-16"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 158497.0
event_previous: 158449.0
event_delta: 48.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 5.2
  mdd_t7: -1.85
  volatility: 30.2
  impact_t1_pct: -1.85
  impact_t7_pct: 1.82
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
chartData: [{"time": "2025-12-15", "open": 617.57, "high": 617.62, "low": 608.54, "close": 609.75}, {"time": "2025-12-16", "open": 607.48, "high": 612.72, "low": 606.13, "close": 610.96}, {"time": "2025-12-17", "open": 612.27, "high": 612.86, "low": 599.51, "close": 599.64}, {"time": "2025-12-18", "open": 609.02, "high": 612.14, "low": 606.14, "close": 608.33}, {"time": "2025-12-19", "open": 611.16, "high": 616.83, "low": 611.08, "close": 616.26}, {"time": "2025-12-22", "open": 621.35, "high": 621.65, "low": 617.77, "close": 619.21}, {"time": "2025-12-23", "open": 618.2, "high": 622.41, "low": 617.78, "close": 622.11}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2025-12-16**
- As-of date (T-1): **2026-03-03**
- Freshness age: **77 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158497.0, Previous 158449.0, Delta +48.0000)
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
