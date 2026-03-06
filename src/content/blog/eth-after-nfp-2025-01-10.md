---
title: "ETH Post-NFP Setup (2025-01-10): Historical Probability Lens"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-01-10"
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
quality_score: 70
sample_size: 34
freshness_days: 419
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:04:09+00:00"
event_direction: "down"
event_actual: 158268.0
event_previous: 158316.0
event_delta: -48.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 51.54
  impact_t1_pct: 0.45
  impact_t7_pct: 6.32
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
    direction: "down"
    sample_size: 4
    t1:
      up: 50.0
      down: 50.0
      median: -0.06
      mean: -0.22
      sample: 4
    t7:
      up: 75.0
      down: 25.0
      median: 5.22
      mean: 2.63
      sample: 4
related_events: [{"slug": "eth-after-nfp-2026-01-09", "title": "ETH After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 6.89, "sample_size": 0}, {"slug": "eth-after-nfp-2025-11-20", "title": "ETH After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 6.45, "sample_size": 0}, {"slug": "eth-after-nfp-2025-09-05", "title": "ETH After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 9.48, "sample_size": 0}]
chartData: [{"time": "2025-01-07", "open": 3688.34, "high": 3701.11, "low": 3358.09, "close": 3381.58}, {"time": "2025-01-08", "open": 3381.62, "high": 3413.68, "low": 3209.21, "close": 3326.33}, {"time": "2025-01-09", "open": 3326.36, "high": 3355.86, "low": 3159.38, "close": 3219.43}, {"time": "2025-01-10", "open": 3219.5, "high": 3320.5, "low": 3196.11, "close": 3267.49}, {"time": "2025-01-11", "open": 3267.52, "high": 3317.65, "low": 3219.7, "close": 3282.22}, {"time": "2025-01-12", "open": 3282.15, "high": 3298.02, "low": 3224.51, "close": 3265.95}, {"time": "2025-01-13", "open": 3266.1, "high": 3335.19, "low": 2920.59, "close": 3135.5}, {"time": "2025-01-14", "open": 3135.67, "high": 3254.75, "low": 3126.81, "close": 3223.68}, {"time": "2025-01-15", "open": 3223.68, "high": 3473.1, "low": 3186.14, "close": 3450.54}, {"time": "2025-01-16", "open": 3450.31, "high": 3458.18, "low": 3265.68, "close": 3308.35}, {"time": "2025-01-17", "open": 3308.19, "high": 3525.54, "low": 3307.31, "close": 3474.11}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2025-01-10**
- As-of date (T-1): **2026-03-05**
- Freshness age: **419 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158268.0, Previous 158316.0, Delta -48.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.15% | 34 |
| T+7 | 55.88% | 44.12% | 1.44% | 2.65% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.06% | -0.22% | 4 |
| T+7 | 75.0% | 25.0% | 5.22% | 2.63% | 4 |

## Historical Distribution Summary

When NFP was **DOWN**, ETH T+1 up probability was **50.0%** (n=4).

When NFP was **DOWN**, ETH T+7 up probability was **75.0%** (n=4).

Same-direction T+7 median return: **5.22%**.

For ETH, historical NFP windows show all-history T+1 up probability of 50.0% and T+7 up probability of 55.88%. When NFP printed Down versus previous, T+1 up probability was 50.0% and T+7 up probability was 75.0% across 4 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
