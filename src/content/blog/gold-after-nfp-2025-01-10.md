---
title: "GOLD Post-NFP Setup (2025-01-10): Historical Probability Lens"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-01-10"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 21.71
robust_score: 15.71
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 50
sample_size: 34
freshness_days: 419
freshness_status: "stale"
index_tier: "C"
is_recent_90d: false
canonical_target: "none"
canonical_url: ""
robots_directive: "noindex,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 158268.0
event_previous: 158316.0
event_delta: -48.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -3.71
  mdd_t7: -4.91
  volatility: 0.75
  impact_t1_pct: 0.57
  impact_t7_pct: 1.32
probabilities:
  sample_size: 34
  t1:
    up: 66.67
    down: 33.33
    median: 0.5
    mean: 0.57
    sample: 21
  t7:
    up: 79.41
    down: 20.59
    median: 1.31
    mean: 1.61
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 3
    t1:
      up: 100.0
      down: 0.0
      median: 0.8
      mean: 0.94
      sample: 3
    t7:
      up: 100.0
      down: 0.0
      median: 2.59
      mean: 2.44
      sample: 4
related_events: [{"slug": "gold-after-nfp-2026-01-02", "title": "GOLD After NFP (2026-01-02): Historical T+1/T+7 Probability", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.08, "sample_size": 0}, {"slug": "gold-after-nfp-2025-12-16", "title": "GOLD After NFP (2025-12-16): Historical T+1/T+7 Probability", "event_date": "2025-12-16", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.14, "sample_size": 0}, {"slug": "gold-after-nfp-2025-11-20", "title": "GOLD After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.99, "sample_size": 0}]
chartData: [{"time": "2025-01-07", "open": 2653.4, "high": 2657.5, "low": 2653.0, "close": 2656.7}, {"time": "2025-01-08", "open": 2655.5, "high": 2676.9, "low": 2653.5, "close": 2664.5}, {"time": "2025-01-09", "open": 2669.7, "high": 2686.3, "low": 2667.9, "close": 2683.8}, {"time": "2025-01-10", "open": 2686.1, "high": 2720.1, "low": 2683.7, "close": 2708.5}, {"time": "2025-01-13", "open": 2711.1, "high": 2711.2, "low": 2673.5, "close": 2673.5}, {"time": "2025-01-14", "open": 2673.6, "high": 2688.3, "low": 2670.8, "close": 2677.5}, {"time": "2025-01-15", "open": 2690.8, "high": 2712.5, "low": 2690.8, "close": 2712.5}, {"time": "2025-01-16", "open": 2731.7, "high": 2749.8, "low": 2731.7, "close": 2746.4}, {"time": "2025-01-17", "open": 2736.0, "high": 2751.6, "low": 2725.5, "close": 2744.3}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
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
| T+1 | 66.67% | 33.33% | 0.5% | 0.57% | 21 |
| T+7 | 79.41% | 20.59% | 1.31% | 1.61% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 100.0% | 0.0% | 0.8% | 0.94% | 3 |
| T+7 | 100.0% | 0.0% | 2.59% | 2.44% | 4 |

## Historical Distribution Summary

When NFP was **DOWN**, GOLD T+1 up probability was **100.0%** (n=3).

When NFP was **DOWN**, GOLD T+7 up probability was **100.0%** (n=4).

Same-direction T+7 median return: **2.59%**.

For GOLD, historical NFP windows show all-history T+1 up probability of 66.67% and T+7 up probability of 79.41%. When NFP printed Down versus previous, T+1 up probability was 100.0% and T+7 up probability was 100.0% across 3 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
