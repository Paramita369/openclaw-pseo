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
raw_signal_score: 15.46
robust_score: 9.46
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 50
sample_size: 14
freshness_days: 631
freshness_status: "stale"
index_tier: "C"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.07
hub_baseline_median_t7: 1.52
hub_baseline_std_t7: 1.8614
hub_baseline_delta: -0.45
z_score_t7: 0.0
percentile_t7: 46.15
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "none"
canonical_url: ""
robots_directive: "noindex,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "down"
event_actual: 313.044
event_previous: 313.175
event_delta: -0.131
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.41
  mdd_t7: -1.53
  volatility: 2.6
  impact_t1_pct: -1.53
  impact_t7_pct: 1.07
probabilities:
  sample_size: 14
  t1:
    up: 50.0
    down: 50.0
    median: 0.27
    mean: 0.22
    sample: 14
  t7:
    up: 76.92
    down: 23.08
    median: 1.52
    mean: 1.07
    sample: 13
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
related_events: [{"slug": "gold-after-cpi-2025-02-12", "title": "US CPI (2025-02-12) and GOLD: Event-Driven Return Odds", "event_date": "2025-02-12", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 7.09, "median_t7_pct": 1.52, "sample_size": 14}, {"slug": "gold-after-cpi-2024-02-20", "title": "US CPI (2024-02-20) and GOLD: Event-Driven Return Odds", "event_date": "2024-02-20", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 6.12, "median_t7_pct": 1.52, "sample_size": 14}, {"slug": "gold-after-cpi-2024-05-15", "title": "US CPI (2024-05-15) and GOLD: Event-Driven Return Odds", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.47, "median_t7_pct": 1.52, "sample_size": 14}]
chartData: [{"time": "2024-06-10", "open": 2290.6, "high": 2309.3, "low": 2290.5, "close": 2307.7}, {"time": "2024-06-11", "open": 2300.0, "high": 2314.1, "low": 2300.0, "close": 2307.5}, {"time": "2024-06-12", "open": 2314.9, "high": 2338.7, "low": 2310.3, "close": 2336.0}, {"time": "2024-06-13", "open": 2309.4, "high": 2317.7, "low": 2296.2, "close": 2300.2}, {"time": "2024-06-14", "open": 2307.0, "high": 2331.4, "low": 2305.8, "close": 2331.4}, {"time": "2024-06-17", "open": 2320.2, "high": 2320.2, "low": 2309.6, "close": 2312.4}, {"time": "2024-06-18", "open": 2311.8, "high": 2330.4, "low": 2311.8, "close": 2330.4}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **GOLD**
- Event date: **2024-06-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **631 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **DOWN** (Actual 313.044, Previous 313.175, Delta -0.1310)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.27% | 0.22% | 14 |
| T+7 | 76.92% | 23.08% | 1.52% | 1.07% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | -1.53% | -1.53% | 1 |
| T+7 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |

## Historical Distribution Summary

When CPI was **DOWN**, GOLD T+1 up probability was **0.0%** (n=1).

When CPI was **DOWN**, GOLD T+7 up probability was **0.0%** (n=0).

Same-direction T+7 median return: **0.0%**.

For GOLD, historical CPI windows show all-history T+1 up probability of 50.0% and T+7 up probability of 76.92%. When CPI printed Down versus previous, T+1 up probability was 0.0% and T+7 up probability was 0.0% across 0 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
