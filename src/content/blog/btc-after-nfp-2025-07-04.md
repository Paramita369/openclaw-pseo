---
title: "BTC After NFP (2025-07-04): Event Probability and Median Return"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 3
title_template_key: "nfp_3"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-07-04"
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
freshness_days: 242
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 158542.0
event_previous: 158478.0
event_delta: 64.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 75.55
  impact_t1_pct: 0.18
  impact_t7_pct: 8.78
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
chartData: [{"time": "2025-07-01", "open": 107144.38, "high": 107550.68, "low": 105270.23, "close": 105698.28}, {"time": "2025-07-02", "open": 105703.1, "high": 109763.66, "low": 105157.4, "close": 108859.32}, {"time": "2025-07-03", "open": 108845.02, "high": 110541.46, "low": 108605.8, "close": 109647.98}, {"time": "2025-07-04", "open": 109635.66, "high": 109751.98, "low": 107296.38, "close": 108034.34}, {"time": "2025-07-05", "open": 108015.84, "high": 108381.34, "low": 107842.27, "close": 108231.18}, {"time": "2025-07-06", "open": 108231.19, "high": 109731.62, "low": 107847.02, "close": 109232.07}, {"time": "2025-07-07", "open": 109235.33, "high": 109710.25, "low": 107527.05, "close": 108299.85}, {"time": "2025-07-08", "open": 108298.23, "high": 109198.97, "low": 107499.55, "close": 108950.27}, {"time": "2025-07-09", "open": 108950.27, "high": 111925.38, "low": 108357.68, "close": 111326.55}, {"time": "2025-07-10", "open": 111329.2, "high": 116608.78, "low": 110660.75, "close": 115987.2}, {"time": "2025-07-11", "open": 115986.23, "high": 118856.48, "low": 115245.69, "close": 117516.99}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-07-04**
- As-of date (T-1): **2026-03-03**
- Freshness age: **242 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158542.0, Previous 158478.0, Delta +64.0000)
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
