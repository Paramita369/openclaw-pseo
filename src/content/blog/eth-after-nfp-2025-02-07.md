---
title: "ETH Post-NFP Setup (2025-02-07): Historical Probability Lens"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-02-07"
asof_date: "2026-03-03"
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
freshness_days: 389
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 158310.0
event_previous: 158268.0
event_delta: 42.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 16.28
  impact_t1_pct: 0.39
  impact_t7_pct: 3.96
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
chartData: [{"time": "2025-02-04", "open": 2883.82, "high": 2888.25, "low": 2636.17, "close": 2735.05}, {"time": "2025-02-05", "open": 2735.23, "high": 2824.4, "low": 2701.1, "close": 2787.78}, {"time": "2025-02-06", "open": 2787.66, "high": 2857.14, "low": 2662.45, "close": 2688.4}, {"time": "2025-02-07", "open": 2688.9, "high": 2798.03, "low": 2564.97, "close": 2622.21}, {"time": "2025-02-08", "open": 2623.0, "high": 2665.48, "low": 2591.78, "close": 2632.31}, {"time": "2025-02-09", "open": 2632.58, "high": 2695.22, "low": 2530.44, "close": 2628.72}, {"time": "2025-02-10", "open": 2628.65, "high": 2692.81, "low": 2564.02, "close": 2661.17}, {"time": "2025-02-11", "open": 2661.32, "high": 2724.9, "low": 2565.4, "close": 2602.78}, {"time": "2025-02-12", "open": 2602.83, "high": 2794.87, "low": 2551.17, "close": 2736.9}, {"time": "2025-02-13", "open": 2737.03, "high": 2756.44, "low": 2615.67, "close": 2675.9}, {"time": "2025-02-14", "open": 2675.94, "high": 2790.02, "low": 2666.27, "close": 2726.09}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
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
