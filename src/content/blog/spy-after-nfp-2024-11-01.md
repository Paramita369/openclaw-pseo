---
title: "SPY After NFP (2024-11-01): Event Probability and Median Return"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 3
title_template_key: "nfp_3"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-11-01"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 4.23
robust_score: -1.77
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
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 158079.0
event_previous: 157945.0
event_delta: 134.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.98
  mdd_t7: -0.1
  volatility: 4.85
  impact_t1_pct: -0.1
  impact_t7_pct: 4.75
probabilities:
  sample_size: 34
  t1:
    up: 47.62
    down: 52.38
    median: -0.04
    mean: -0.1
    sample: 21
  t7:
    up: 55.88
    down: 44.12
    median: 0.11
    mean: 0.81
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 18
    t1:
      up: 38.89
      down: 61.11
      median: -0.13
      mean: -0.22
      sample: 18
    t7:
      up: 56.67
      down: 43.33
      median: 0.11
      mean: 0.83
      sample: 30
related_events: [{"slug": "spy-after-nfp-2026-01-02", "title": "SPY After NFP (2026-01-02): Historical T+1/T+7 Probability", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.6, "sample_size": 0}, {"slug": "spy-after-nfp-2025-11-20", "title": "SPY After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.73, "sample_size": 0}, {"slug": "spy-after-nfp-2025-09-05", "title": "SPY After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.57, "sample_size": 0}]
chartData: [{"time": "2024-10-29", "open": 571.2, "high": 574.21, "low": 569.8, "close": 573.09}, {"time": "2024-10-30", "open": 572.62, "high": 574.62, "low": 570.65, "close": 571.35}, {"time": "2024-10-31", "open": 566.97, "high": 567.04, "low": 559.96, "close": 560.15}, {"time": "2024-11-01", "open": 562.79, "high": 566.96, "low": 562.11, "close": 562.52}, {"time": "2024-11-04", "open": 562.66, "high": 563.96, "low": 559.42, "close": 561.31}, {"time": "2024-11-05", "open": 562.22, "high": 568.13, "low": 562.01, "close": 568.09}, {"time": "2024-11-06", "open": 580.41, "high": 583.1, "low": 576.65, "close": 582.22}, {"time": "2024-11-07", "open": 584.23, "high": 587.75, "low": 584.15, "close": 586.72}, {"time": "2024-11-08", "open": 587.27, "high": 590.69, "low": 587.27, "close": 589.26}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
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
| T+1 | 47.62% | 52.38% | -0.04% | -0.1% | 21 |
| T+7 | 55.88% | 44.12% | 0.11% | 0.81% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 38.89% | 61.11% | -0.13% | -0.22% | 18 |
| T+7 | 56.67% | 43.33% | 0.11% | 0.83% | 30 |

## Historical Distribution Summary

When NFP was **UP**, SPY T+1 up probability was **38.89%** (n=18).

When NFP was **UP**, SPY T+7 up probability was **56.67%** (n=30).

Same-direction T+7 median return: **0.11%**.

For SPY, historical NFP windows show all-history T+1 up probability of 47.62% and T+7 up probability of 55.88%. When NFP printed Up versus previous, T+1 up probability was 38.89% and T+7 up probability was 56.67% across 18 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
