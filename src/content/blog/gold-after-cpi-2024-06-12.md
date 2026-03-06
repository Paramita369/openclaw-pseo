---
title: "US CPI (2024-06-12) and GOLD: Event-Driven Return Odds"
description: "Historical probability profile for GOLD around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-06-12"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 18.4
robust_score: 12.4
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 50
sample_size: 39
freshness_days: 631
freshness_status: "stale"
index_tier: "C"
is_recent_90d: false
canonical_target: "none"
canonical_url: ""
robots_directive: "noindex,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:13+00:00"
event_direction: "down"
event_actual: 313.044
event_previous: 313.175
event_delta: -0.131
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.49
  mdd_t7: -1.53
  volatility: 3.02
  impact_t1_pct: -1.53
  impact_t7_pct: 1.49
probabilities:
  sample_size: 39
  t1:
    up: 56.41
    down: 43.59
    median: 0.34
    mean: 0.3
    sample: 39
  t7:
    up: 78.95
    down: 21.05
    median: 1.4
    mean: 1.49
    sample: 38
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 0
    t1:
      up: 0.0
      down: 100.0
      median: -1.53
      mean: -1.53
      sample: 1
    t7:
      up: 0.0
      down: 100.0
      median: 0.0
      mean: 0.0
      sample: 0
related_events: [{"slug": "gold-after-cpi-2026-01-13", "title": "GOLD After CPI (2026-01-13): Historical T+1/T+7 Probability", "event_date": "2026-01-13", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.71, "sample_size": 0}, {"slug": "gold-after-cpi-2026-01-12", "title": "GOLD After CPI (2026-01-12): Historical T+1/T+7 Probability", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.37, "sample_size": 0}, {"slug": "gold-after-cpi-2025-12-18", "title": "GOLD After CPI (2025-12-18): Historical T+1/T+7 Probability", "event_date": "2025-12-18", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.37, "sample_size": 0}]
chartData: [{"time": "2024-06-10", "open": 2290.6, "high": 2309.3, "low": 2290.5, "close": 2307.7}, {"time": "2024-06-11", "open": 2300.0, "high": 2314.1, "low": 2300.0, "close": 2307.5}, {"time": "2024-06-12", "open": 2314.9, "high": 2338.7, "low": 2310.3, "close": 2336.0}, {"time": "2024-06-13", "open": 2309.4, "high": 2317.7, "low": 2296.2, "close": 2300.2}, {"time": "2024-06-14", "open": 2307.0, "high": 2331.4, "low": 2305.8, "close": 2331.4}, {"time": "2024-06-17", "open": 2320.2, "high": 2320.2, "low": 2309.6, "close": 2312.4}, {"time": "2024-06-18", "open": 2311.8, "high": 2330.4, "low": 2311.8, "close": 2330.4}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **GOLD**
- Event date: **2024-06-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **631 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **DOWN** (Actual 313.044, Previous 313.175, Delta -0.1310)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 56.41% | 43.59% | 0.34% | 0.3% | 39 |
| T+7 | 78.95% | 21.05% | 1.4% | 1.49% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | -1.53% | -1.53% | 1 |
| T+7 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |

## Historical Distribution Summary

When CPI was **DOWN**, GOLD T+1 up probability was **0.0%** (n=1).

When CPI was **DOWN**, GOLD T+7 up probability was **0.0%** (n=0).

Same-direction T+7 median return: **0.0%**.

For GOLD, historical CPI windows show all-history T+1 up probability of 56.41% and T+7 up probability of 78.95%. When CPI printed Down versus previous, T+1 up probability was 0.0% and T+7 up probability was 0.0% across 0 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
