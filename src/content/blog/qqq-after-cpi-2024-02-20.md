---
title: "US CPI (2024-02-20) and QQQ: Event-Driven Return Odds"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-12"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-02-20"
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
freshness_days: 750
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.2
hub_baseline_median_t7: 0.58
hub_baseline_std_t7: 2.2166
hub_baseline_delta: 1.83
z_score_t7: 0.99
percentile_t7: 84.21
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:06+00:00"
event_direction: "up"
event_actual: 310.967
event_previous: 309.698
event_delta: 1.269
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.86
  mdd_t7: -0.4
  volatility: 2.81
  impact_t1_pct: -0.4
  impact_t7_pct: 2.41
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
chartData: [{"time": "2024-02-20", "open": 423.87, "high": 425.38, "low": 418.87, "close": 422.65}, {"time": "2024-02-21", "open": 419.91, "high": 421.05, "low": 417.02, "close": 420.96}, {"time": "2024-02-22", "open": 429.74, "high": 434.32, "low": 428.97, "close": 433.28}, {"time": "2024-02-23", "open": 434.85, "high": 435.78, "low": 431.03, "close": 432.01}, {"time": "2024-02-26", "open": 432.82, "high": 433.81, "low": 431.59, "close": 431.78}, {"time": "2024-02-27", "open": 432.89, "high": 433.21, "low": 430.28, "close": 432.82}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2024-02-20**
- As-of date (T-1): **2026-03-11**
- Freshness age: **750 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 310.967, Previous 309.698, Delta +1.2690)
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
