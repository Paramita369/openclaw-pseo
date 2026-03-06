---
title: "ETH After NFP (2024-06-07): Event Probability and Median Return"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "nfp_3"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-06-07"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 4.94
robust_score: -1.06
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 100
sample_size: 34
freshness_days: 636
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:36+00:00"
event_direction: "up"
event_actual: 157695.0
event_previous: 157608.0
event_delta: 87.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -10.0
  mdd_t7: -5.45
  volatility: 52.68
  impact_t1_pct: 0.06
  impact_t7_pct: -5.39
probabilities:
  sample_size: 34
  t1:
    up: 50.0
    down: 50.0
    median: 0.0
    mean: -0.15
    sample: 34
  t7:
    up: 55.88
    down: 44.12
    median: 1.44
    mean: 2.65
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 30
    t1:
      up: 50.0
      down: 50.0
      median: 0.0
      mean: -0.14
      sample: 30
    t7:
      up: 53.33
      down: 46.67
      median: 0.79
      mean: 2.65
      sample: 30
related_events: [{"slug": "eth-after-nfp-2026-01-09", "title": "ETH After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 6.89, "sample_size": 0}, {"slug": "eth-after-nfp-2025-11-20", "title": "ETH After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 6.45, "sample_size": 0}, {"slug": "eth-after-nfp-2025-09-05", "title": "ETH After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 9.48, "sample_size": 0}]
chartData: [{"time": "2024-06-04", "open": 3766.48, "high": 3831.36, "low": 3738.13, "close": 3812.52}, {"time": "2024-06-05", "open": 3812.56, "high": 3887.49, "low": 3778.66, "close": 3864.26}, {"time": "2024-06-06", "open": 3864.26, "high": 3878.05, "low": 3761.78, "close": 3811.61}, {"time": "2024-06-07", "open": 3811.67, "high": 3838.45, "low": 3615.28, "close": 3678.63}, {"time": "2024-06-08", "open": 3677.4, "high": 3707.5, "low": 3669.64, "close": 3680.95}, {"time": "2024-06-09", "open": 3680.94, "high": 3719.37, "low": 3668.12, "close": 3705.9}, {"time": "2024-06-10", "open": 3705.88, "high": 3711.43, "low": 3648.16, "close": 3666.72}, {"time": "2024-06-11", "open": 3666.36, "high": 3669.89, "low": 3434.75, "close": 3498.33}, {"time": "2024-06-12", "open": 3497.9, "high": 3652.49, "low": 3463.78, "close": 3559.62}, {"time": "2024-06-13", "open": 3559.73, "high": 3559.73, "low": 3431.33, "close": 3469.28}, {"time": "2024-06-14", "open": 3467.97, "high": 3528.6, "low": 3366.22, "close": 3480.27}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2024-06-07**
- As-of date (T-1): **2026-03-05**
- Freshness age: **636 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157695.0, Previous 157608.0, Delta +87.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.15% | 34 |
| T+7 | 55.88% | 44.12% | 1.44% | 2.65% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.14% | 30 |
| T+7 | 53.33% | 46.67% | 0.79% | 2.65% | 30 |

## Historical Distribution Summary

When NFP was **UP**, ETH T+1 up probability was **50.0%** (n=30).

When NFP was **UP**, ETH T+7 up probability was **53.33%** (n=30).

Same-direction T+7 median return: **0.79%**.

For ETH, historical NFP windows show all-history T+1 up probability of 50.0% and T+7 up probability of 55.88%. When NFP printed Up versus previous, T+1 up probability was 50.0% and T+7 up probability was 53.33% across 30 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
