---
title: "NFP Print (2025-02-07) vs BTC: Quantified Directional Odds"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 4
title_template_key: "nfp_4"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-02-07"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 0.23
robust_score: -5.77
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
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 158310.0
event_previous: 158268.0
event_delta: 42.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: -0.05
  volatility: 8.85
  impact_t1_pct: -0.05
  impact_t7_pct: 1.02
probabilities:
  sample_size: 34
  t1:
    up: 29.41
    down: 70.59
    median: -0.33
    mean: -0.26
    sample: 34
  t7:
    up: 58.82
    down: 41.18
    median: 1.0
    mean: 1.55
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 30
    t1:
      up: 26.67
      down: 73.33
      median: -0.39
      mean: -0.31
      sample: 30
    t7:
      up: 56.67
      down: 43.33
      median: 0.81
      mean: 1.51
      sample: 30
related_events: [{"slug": "btc-after-nfp-2026-01-09", "title": "BTC After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 5.54, "sample_size": 0}, {"slug": "btc-after-nfp-2025-11-20", "title": "BTC After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 5.37, "sample_size": 0}, {"slug": "btc-after-nfp-2025-09-05", "title": "BTC After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.93, "sample_size": 0}]
chartData: [{"time": "2025-02-04", "open": 101398.72, "high": 101745.62, "low": 96208.11, "close": 97871.82}, {"time": "2025-02-05", "open": 97878.01, "high": 99113.21, "low": 96174.83, "close": 96615.45}, {"time": "2025-02-06", "open": 96610.64, "high": 99168.61, "low": 95707.35, "close": 96593.3}, {"time": "2025-02-07", "open": 96581.32, "high": 100154.14, "low": 95653.88, "close": 96529.09}, {"time": "2025-02-08", "open": 96533.26, "high": 96877.8, "low": 95702.49, "close": 96482.45}, {"time": "2025-02-09", "open": 96481.31, "high": 97325.28, "low": 94745.26, "close": 96500.09}, {"time": "2025-02-10", "open": 96499.46, "high": 98333.22, "low": 95320.84, "close": 97437.55}, {"time": "2025-02-11", "open": 97438.13, "high": 98492.9, "low": 94875.04, "close": 95747.43}, {"time": "2025-02-12", "open": 95745.7, "high": 98151.02, "low": 94101.2, "close": 97885.86}, {"time": "2025-02-13", "open": 97888.75, "high": 98111.09, "low": 95269.71, "close": 96623.87}, {"time": "2025-02-14", "open": 96623.37, "high": 98819.47, "low": 96342.8, "close": 97508.97}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
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
| T+1 | 29.41% | 70.59% | -0.33% | -0.26% | 34 |
| T+7 | 58.82% | 41.18% | 1.0% | 1.55% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 26.67% | 73.33% | -0.39% | -0.31% | 30 |
| T+7 | 56.67% | 43.33% | 0.81% | 1.51% | 30 |

## Historical Distribution Summary

When NFP was **UP**, BTC T+1 up probability was **26.67%** (n=30).

When NFP was **UP**, BTC T+7 up probability was **56.67%** (n=30).

Same-direction T+7 median return: **0.81%**.

For BTC, historical NFP windows show all-history T+1 up probability of 29.41% and T+7 up probability of 58.82%. When NFP printed Up versus previous, T+1 up probability was 26.67% and T+7 up probability was 56.67% across 30 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
