---
title: "BTC After NFP (2025-06-06): Event Probability and Median Return"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 3
title_template_key: "nfp_3"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-06-06"
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
quality_score: 70
sample_size: 34
freshness_days: 270
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "down"
event_actual: 158478.0
event_previous: 158498.0
event_delta: -20.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 3.37
  mdd_t7: -3.81
  volatility: 64.74
  impact_t1_pct: 1.17
  impact_t7_pct: 1.63
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
    direction: "down"
    sample_size: 4
    t1:
      up: 50.0
      down: 50.0
      median: -0.01
      mean: 0.12
      sample: 4
    t7:
      up: 75.0
      down: 25.0
      median: 2.3
      mean: 1.88
      sample: 4
related_events: [{"slug": "btc-after-nfp-2026-01-09", "title": "BTC After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 5.54, "sample_size": 0}, {"slug": "btc-after-nfp-2025-11-20", "title": "BTC After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 5.37, "sample_size": 0}, {"slug": "btc-after-nfp-2025-09-05", "title": "BTC After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.93, "sample_size": 0}]
chartData: [{"time": "2025-06-03", "open": 105888.48, "high": 106813.58, "low": 104920.84, "close": 105432.47}, {"time": "2025-06-04", "open": 105434.37, "high": 105997.7, "low": 104232.7, "close": 104731.98}, {"time": "2025-06-05", "open": 104750.78, "high": 105936.69, "low": 100436.88, "close": 101575.95}, {"time": "2025-06-06", "open": 101574.37, "high": 105376.77, "low": 101169.57, "close": 104390.34}, {"time": "2025-06-07", "open": 104390.65, "high": 105972.76, "low": 103987.31, "close": 105615.62}, {"time": "2025-06-08", "open": 105617.51, "high": 106497.06, "low": 105075.33, "close": 105793.65}, {"time": "2025-06-09", "open": 105793.02, "high": 110561.42, "low": 105400.23, "close": 110294.1}, {"time": "2025-06-10", "open": 110295.69, "high": 110380.12, "low": 108367.71, "close": 110257.23}, {"time": "2025-06-11", "open": 110261.8, "high": 110384.22, "low": 108086.33, "close": 108686.62}, {"time": "2025-06-12", "open": 108685.91, "high": 108780.7, "low": 105785.69, "close": 105929.05}, {"time": "2025-06-13", "open": 105924.59, "high": 106182.55, "low": 102822.02, "close": 106090.97}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2025-06-06**
- As-of date (T-1): **2026-03-03**
- Freshness age: **270 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158478.0, Previous 158498.0, Delta -20.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 29.41% | 70.59% | -0.33% | -0.26% | 34 |
| T+7 | 58.82% | 41.18% | 1.0% | 1.55% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.01% | 0.12% | 4 |
| T+7 | 75.0% | 25.0% | 2.3% | 1.88% | 4 |

## Historical Distribution Summary

When NFP was **DOWN**, BTC T+1 up probability was **50.0%** (n=4).

When NFP was **DOWN**, BTC T+7 up probability was **75.0%** (n=4).

Same-direction T+7 median return: **2.3%**.

For BTC, historical NFP windows show all-history T+1 up probability of 29.41% and T+7 up probability of 58.82%. When NFP printed Down versus previous, T+1 up probability was 50.0% and T+7 up probability was 75.0% across 4 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
