---
title: "2025-03-07 Nonfarm Payrolls: BTC Historical Win Rate"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-03-07"
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
freshness_days: 361
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 158377.0
event_previous: 158310.0
event_delta: 67.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -2.57
  mdd_t7: -9.47
  volatility: 123.03
  impact_t1_pct: -0.68
  impact_t7_pct: -3.2
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
chartData: [{"time": "2025-03-04", "open": 86064.07, "high": 88911.27, "low": 81529.24, "close": 87222.2}, {"time": "2025-03-05", "open": 87222.95, "high": 90998.24, "low": 86379.77, "close": 90623.56}, {"time": "2025-03-06", "open": 90622.36, "high": 92804.94, "low": 87852.14, "close": 89961.73}, {"time": "2025-03-07", "open": 89963.28, "high": 91191.05, "low": 84717.68, "close": 86742.67}, {"time": "2025-03-08", "open": 86742.66, "high": 86847.27, "low": 85247.48, "close": 86154.59}, {"time": "2025-03-09", "open": 86154.3, "high": 86471.13, "low": 80052.48, "close": 80601.04}, {"time": "2025-03-10", "open": 80597.15, "high": 83955.93, "low": 77420.59, "close": 78532.0}, {"time": "2025-03-11", "open": 78523.88, "high": 83577.76, "low": 76624.25, "close": 82862.21}, {"time": "2025-03-12", "open": 82857.38, "high": 84358.58, "low": 80635.25, "close": 83722.36}, {"time": "2025-03-13", "open": 83724.92, "high": 84301.7, "low": 79931.85, "close": 81066.7}, {"time": "2025-03-14", "open": 81066.99, "high": 85263.29, "low": 80797.56, "close": 83969.1}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-03-07**
- As-of date (T-1): **2026-03-03**
- Freshness age: **361 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158377.0, Previous 158310.0, Delta +67.0000)
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
