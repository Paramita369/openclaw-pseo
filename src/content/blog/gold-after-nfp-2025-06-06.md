---
title: "GOLD After NFP (2025-06-06): Event Probability and Median Return"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "nfp_3"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-06-06"
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
quality_score: 70
sample_size: 34
freshness_days: 272
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/gold/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 158478.0
event_previous: 158498.0
event_delta: -20.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 21.28
  impact_t1_pct: 0.28
  impact_t7_pct: 3.27
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
chartData: [{"time": "2025-06-03", "open": 3385.1, "high": 3390.0, "low": 3331.3, "close": 3350.2}, {"time": "2025-06-04", "open": 3355.0, "high": 3380.0, "low": 3344.0, "close": 3373.5}, {"time": "2025-06-05", "open": 3371.5, "high": 3400.0, "low": 3343.7, "close": 3350.7}, {"time": "2025-06-06", "open": 3364.3, "high": 3364.3, "low": 3306.0, "close": 3322.7}, {"time": "2025-06-09", "open": 3315.6, "high": 3334.6, "low": 3290.0, "close": 3332.1}, {"time": "2025-06-10", "open": 3302.0, "high": 3344.3, "low": 3302.0, "close": 3320.9}, {"time": "2025-06-11", "open": 3328.0, "high": 3356.0, "low": 3321.3, "close": 3321.3}, {"time": "2025-06-12", "open": 3363.0, "high": 3395.9, "low": 3353.4, "close": 3380.9}, {"time": "2025-06-13", "open": 3407.3, "high": 3444.0, "low": 3407.3, "close": 3431.2}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
- Event date: **2025-06-06**
- As-of date (T-1): **2026-03-05**
- Freshness age: **272 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158478.0, Previous 158498.0, Delta -20.0000)
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
