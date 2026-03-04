---
title: "GOLD After NFP (2025-12-16): Event Probability and Median Return"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 3
title_template_key: "nfp_3"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-12-16"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 21.71
robust_score: 15.71
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
canonical_url: "https://quantmacro.vercel.app/blog/gold-after-nfp-2025-12-16"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 158497.0
event_previous: 158449.0
event_delta: 48.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 16.49
  impact_t1_pct: 1.0
  impact_t7_pct: 4.14
probabilities:
  sample_size: 34
  t1:
    up: 66.67
    down: 33.33
    median: 0.5
    mean: 0.57
    sample: 21
  t7:
    up: 79.41
    down: 20.59
    median: 1.31
    mean: 1.61
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 18
    t1:
      up: 61.11
      down: 38.89
      median: 0.34
      mean: 0.51
      sample: 18
    t7:
      up: 76.67
      down: 23.33
      median: 1.1
      mean: 1.49
      sample: 30
related_events: [{"slug": "gold-after-nfp-2026-01-02", "title": "GOLD After NFP (2026-01-02): Historical T+1/T+7 Probability", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.08, "sample_size": 0}, {"slug": "gold-after-nfp-2025-11-20", "title": "GOLD After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.99, "sample_size": 0}, {"slug": "gold-after-nfp-2025-10-03", "title": "GOLD After NFP (2025-10-03): Historical T+1/T+7 Probability", "event_date": "2025-10-03", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.45, "sample_size": 0}]
chartData: [{"time": "2025-12-15", "open": 4308.3, "high": 4349.2, "low": 4292.9, "close": 4306.7}, {"time": "2025-12-16", "open": 4270.5, "high": 4321.4, "low": 4270.5, "close": 4304.5}, {"time": "2025-12-17", "open": 4308.5, "high": 4351.4, "low": 4308.5, "close": 4347.5}, {"time": "2025-12-18", "open": 4331.0, "high": 4348.1, "low": 4328.2, "close": 4339.5}, {"time": "2025-12-19", "open": 4350.1, "high": 4361.4, "low": 4350.1, "close": 4361.4}, {"time": "2025-12-22", "open": 4371.1, "high": 4447.6, "low": 4371.1, "close": 4444.6}, {"time": "2025-12-23", "open": 4503.3, "high": 4503.8, "low": 4450.4, "close": 4482.8}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
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
| T+1 | 66.67% | 33.33% | 0.5% | 0.57% | 21 |
| T+7 | 79.41% | 20.59% | 1.31% | 1.61% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 61.11% | 38.89% | 0.34% | 0.51% | 18 |
| T+7 | 76.67% | 23.33% | 1.1% | 1.49% | 30 |

## Historical Distribution Summary

When NFP was **UP**, GOLD T+1 up probability was **61.11%** (n=18).

When NFP was **UP**, GOLD T+7 up probability was **76.67%** (n=30).

Same-direction T+7 median return: **1.1%**.

For GOLD, historical NFP windows show all-history T+1 up probability of 66.67% and T+7 up probability of 79.41%. When NFP printed Up versus previous, T+1 up probability was 61.11% and T+7 up probability was 76.67% across 18 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
