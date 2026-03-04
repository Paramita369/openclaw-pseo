---
title: "2025-03-07 Nonfarm Payrolls: ETH Historical Win Rate"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
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
freshness_days: 361
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 158377.0
event_previous: 158310.0
event_delta: 67.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -7.37
  mdd_t7: -15.46
  volatility: 164.11
  impact_t1_pct: 2.92
  impact_t7_pct: -10.73
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
chartData: [{"time": "2025-03-04", "open": 2145.65, "high": 2220.36, "low": 1996.77, "close": 2170.02}, {"time": "2025-03-05", "open": 2169.99, "high": 2272.8, "low": 2156.1, "close": 2241.98}, {"time": "2025-03-06", "open": 2241.91, "high": 2319.4, "low": 2177.68, "close": 2202.48}, {"time": "2025-03-07", "open": 2202.5, "high": 2254.23, "low": 2103.47, "close": 2138.99}, {"time": "2025-03-08", "open": 2139.8, "high": 2232.33, "low": 2107.73, "close": 2201.51}, {"time": "2025-03-09", "open": 2201.71, "high": 2210.31, "low": 1991.19, "close": 2015.51}, {"time": "2025-03-10", "open": 2015.43, "high": 2150.71, "low": 1812.77, "close": 1861.15}, {"time": "2025-03-11", "open": 1859.78, "high": 1961.8, "low": 1760.94, "close": 1919.84}, {"time": "2025-03-12", "open": 1919.66, "high": 1954.57, "low": 1832.02, "close": 1908.98}, {"time": "2025-03-13", "open": 1909.02, "high": 1919.69, "low": 1823.53, "close": 1862.97}, {"time": "2025-03-14", "open": 1863.0, "high": 1945.09, "low": 1861.11, "close": 1909.47}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
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
