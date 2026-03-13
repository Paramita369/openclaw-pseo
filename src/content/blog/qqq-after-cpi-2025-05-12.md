---
title: "QQQ After CPI (2025-05-12): Up/Down Odds and Median Returns"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-12"
title_variant_id: 5
title_template_key: "cpi_5"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-05-12"
asof_date: "2026-03-11"
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
quality_score: 90
sample_size: 39
freshness_days: 303
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.2
hub_baseline_median_t7: 0.58
hub_baseline_std_t7: 2.2166
hub_baseline_delta: 2.21
z_score_t7: 1.17
percentile_t7: 89.47
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 320.62
event_previous: 320.302
event_delta: 0.318
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 2.21
  mdd_t7: 0.0
  volatility: 1.26
  impact_t1_pct: 1.52
  impact_t7_pct: 2.79
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
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.19
      mean: 0.23
      sample: 38
    t7:
      up: 55.26
      down: 44.74
      median: 0.58
      mean: 0.2
      sample: 38
related_events: [{"slug": "qqq-after-cpi-2024-05-15", "title": "2024-05-15 CPI Release: QQQ Directional Probability Snapshot", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 9.6, "median_t7_pct": 0.58, "sample_size": 39}, {"slug": "qqq-after-cpi-2024-09-11", "title": "US CPI (2024-09-11) and QQQ: Event-Driven Return Odds", "event_date": "2024-09-11", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 7.08, "median_t7_pct": 0.58, "sample_size": 39}, {"slug": "qqq-after-cpi-2026-02-12", "title": "QQQ CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 0.58, "sample_size": 39}]
chartData: [{"time": "2025-05-09", "open": 488.46, "high": 489.79, "low": 484.47, "close": 486.23}, {"time": "2025-05-12", "open": 505.18, "high": 506.08, "low": 499.69, "close": 506.04}, {"time": "2025-05-13", "open": 507.35, "high": 515.55, "low": 506.61, "close": 513.75}, {"time": "2025-05-14", "open": 514.93, "high": 517.38, "low": 513.91, "close": 516.83}, {"time": "2025-05-15", "open": 514.68, "high": 520.07, "low": 513.33, "close": 517.4}, {"time": "2025-05-16", "open": 518.81, "high": 519.84, "low": 515.26, "close": 519.65}, {"time": "2025-05-19", "open": 512.41, "high": 520.67, "low": 512.41, "close": 520.15}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2025-05-12**
- As-of date (T-1): **2026-03-11**
- Freshness age: **303 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 320.62, Previous 320.302, Delta +0.3180)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 61.54% | 38.46% | 0.21% | 0.23% | 39 |
| T+7 | 55.26% | 44.74% | 0.58% | 0.2% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.19% | 0.23% | 38 |
| T+7 | 55.26% | 44.74% | 0.58% | 0.2% | 38 |

## Historical Distribution Summary

When CPI was **UP**, QQQ T+1 up probability was **60.53%** (n=38).

When CPI was **UP**, QQQ T+7 up probability was **55.26%** (n=38).

Same-direction T+7 median return: **0.58%**.

For QQQ, historical CPI windows show all-history T+1 up probability of 61.54% and T+7 up probability of 55.26%. When CPI printed Up versus previous, T+1 up probability was 60.53% and T+7 up probability was 55.26% across 38 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
