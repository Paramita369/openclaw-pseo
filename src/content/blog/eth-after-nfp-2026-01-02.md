---
title: "2026-01-02 Nonfarm Payrolls: ETH Historical Win Rate"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-01-02"
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
freshness_days: 60
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/eth-after-nfp-2026-01-02"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 158627.0
event_previous: 158497.0
event_delta: 130.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -2.4
  mdd_t7: -4.44
  volatility: 59.89
  impact_t1_pct: 0.05
  impact_t7_pct: -1.32
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
chartData: [{"time": "2025-12-30", "open": 2934.42, "high": 3002.8, "low": 2916.33, "close": 2971.42}, {"time": "2025-12-31", "open": 2971.41, "high": 3021.85, "low": 2959.14, "close": 2967.04}, {"time": "2026-01-01", "open": 2967.0, "high": 3006.01, "low": 2966.85, "close": 3000.39}, {"time": "2026-01-02", "open": 3000.45, "high": 3146.98, "low": 2989.9, "close": 3124.42}, {"time": "2026-01-03", "open": 3124.31, "high": 3135.03, "low": 3077.47, "close": 3125.92}, {"time": "2026-01-04", "open": 3125.96, "high": 3160.55, "low": 3119.43, "close": 3140.71}, {"time": "2026-01-05", "open": 3141.49, "high": 3261.25, "low": 3134.09, "close": 3226.13}, {"time": "2026-01-06", "open": 3226.12, "high": 3303.56, "low": 3184.01, "close": 3295.95}, {"time": "2026-01-07", "open": 3295.91, "high": 3296.39, "low": 3126.55, "close": 3166.84}, {"time": "2026-01-08", "open": 3166.92, "high": 3179.87, "low": 3052.51, "close": 3104.38}, {"time": "2026-01-09", "open": 3104.33, "high": 3140.71, "low": 3058.1, "close": 3083.05}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2026-01-02**
- As-of date (T-1): **2026-03-03**
- Freshness age: **60 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158627.0, Previous 158497.0, Delta +130.0000)
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
