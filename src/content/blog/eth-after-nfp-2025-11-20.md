---
title: "ETH Post-NFP Setup (2025-11-20): Historical Probability Lens"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-11-20"
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
freshness_days: 105
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158449.0
event_previous: 158408.0
event_delta: 41.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: -2.33
  volatility: 78.38
  impact_t1_pct: -2.33
  impact_t7_pct: 6.45
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
related_events: [{"slug": "eth-after-nfp-2026-01-09", "title": "ETH After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 6.89, "sample_size": 0}, {"slug": "eth-after-nfp-2025-09-05", "title": "ETH After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 9.48, "sample_size": 0}, {"slug": "eth-after-nfp-2025-08-01", "title": "ETH After NFP (2025-08-01): Historical T+1/T+7 Probability", "event_date": "2025-08-01", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 14.95, "sample_size": 0}]
chartData: [{"time": "2025-11-17", "open": 3092.94, "high": 3218.13, "low": 2957.31, "close": 3024.54}, {"time": "2025-11-18", "open": 3024.41, "high": 3167.93, "low": 2948.33, "close": 3122.98}, {"time": "2025-11-19", "open": 3122.65, "high": 3122.65, "low": 2871.23, "close": 3023.07}, {"time": "2025-11-20", "open": 3022.89, "high": 3057.79, "low": 2790.6, "close": 2831.78}, {"time": "2025-11-21", "open": 2829.26, "high": 2880.6, "low": 2626.87, "close": 2765.7}, {"time": "2025-11-22", "open": 2766.09, "high": 2795.43, "low": 2704.5, "close": 2767.61}, {"time": "2025-11-23", "open": 2767.59, "high": 2856.45, "low": 2767.47, "close": 2801.68}, {"time": "2025-11-24", "open": 2801.2, "high": 2982.82, "low": 2763.38, "close": 2952.71}, {"time": "2025-11-25", "open": 2952.58, "high": 2978.7, "low": 2857.84, "close": 2957.94}, {"time": "2025-11-26", "open": 2958.33, "high": 3043.93, "low": 2889.89, "close": 3027.81}, {"time": "2025-11-27", "open": 3027.8, "high": 3070.73, "low": 2987.2, "close": 3014.54}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2025-11-20**
- As-of date (T-1): **2026-03-05**
- Freshness age: **105 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158449.0, Previous 158408.0, Delta +41.0000)
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
