---
title: "US CPI (2024-06-12) and QQQ: Event-Driven Return Odds"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-06-12"
asof_date: "2026-03-09"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 8.09
robust_score: 2.09
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 50
sample_size: 39
freshness_days: 635
freshness_status: "stale"
index_tier: "C"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.2
hub_baseline_median_t7: 0.58
hub_baseline_std_t7: 2.2166
hub_baseline_delta: -0.38
z_score_t7: -0.0
percentile_t7: 44.74
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "none"
canonical_url: ""
robots_directive: "noindex,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:14+00:00"
event_direction: "down"
event_actual: 313.044
event_previous: 313.175
event_delta: -0.131
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.59
  mdd_t7: 0.0
  volatility: 0.34
  impact_t1_pct: 0.54
  impact_t7_pct: 0.2
probabilities:
  sample_size: 39
  t1:
    up: 61.54
    down: 38.46
    median: 0.21
    mean: 0.23
    sample: 39
  t7:
    up: 55.26
    down: 44.74
    median: 0.58
    mean: 0.2
    sample: 38
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 0
    t1:
      up: 100.0
      down: 0.0
      median: 0.54
      mean: 0.54
      sample: 1
    t7:
      up: 0.0
      down: 100.0
      median: 0.0
      mean: 0.0
      sample: 0
related_events: [{"slug": "qqq-after-cpi-2024-05-15", "title": "2024-05-15 CPI Release: QQQ Directional Probability Snapshot", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 9.6, "median_t7_pct": 0.58, "sample_size": 39}, {"slug": "qqq-after-cpi-2024-09-11", "title": "US CPI (2024-09-11) and QQQ: Event-Driven Return Odds", "event_date": "2024-09-11", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 7.08, "median_t7_pct": 0.58, "sample_size": 39}, {"slug": "qqq-after-cpi-2026-02-12", "title": "QQQ CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 0.58, "sample_size": 39}]
chartData: [{"time": "2024-06-10", "open": 457.38, "high": 460.72, "low": 457.09, "close": 460.36}, {"time": "2024-06-11", "open": 459.08, "high": 463.64, "low": 457.59, "close": 463.52}, {"time": "2024-06-12", "open": 467.45, "high": 471.92, "low": 466.76, "close": 469.59}, {"time": "2024-06-13", "open": 473.13, "high": 473.79, "low": 469.86, "close": 472.14}, {"time": "2024-06-14", "open": 471.94, "high": 474.65, "low": 471.47, "close": 474.58}, {"time": "2024-06-17", "open": 474.85, "high": 482.18, "low": 473.54, "close": 480.4}, {"time": "2024-06-18", "open": 480.35, "high": 481.23, "low": 478.78, "close": 480.54}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2024-06-12**
- As-of date (T-1): **2026-03-09**
- Freshness age: **635 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **DOWN** (Actual 313.044, Previous 313.175, Delta -0.1310)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 61.54% | 38.46% | 0.21% | 0.23% | 39 |
| T+7 | 55.26% | 44.74% | 0.58% | 0.2% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 100.0% | 0.0% | 0.54% | 0.54% | 1 |
| T+7 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |

## Historical Distribution Summary

When CPI was **DOWN**, QQQ T+1 up probability was **100.0%** (n=1).

When CPI was **DOWN**, QQQ T+7 up probability was **0.0%** (n=0).

Same-direction T+7 median return: **0.0%**.

For QQQ, historical CPI windows show all-history T+1 up probability of 61.54% and T+7 up probability of 55.26%. When CPI printed Down versus previous, T+1 up probability was 100.0% and T+7 up probability was 0.0% across 0 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
