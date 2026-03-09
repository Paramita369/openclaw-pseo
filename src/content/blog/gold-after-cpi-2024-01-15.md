---
title: "GOLD Reaction to US CPI (2024-01-15): Quant Probability Breakdown"
description: "Historical probability profile for GOLD around CPI events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-01-15"
asof_date: "2026-03-08"
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
quality_score: 90
sample_size: 39
freshness_days: 783
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 1.49
hub_baseline_median_t7: 1.4
hub_baseline_std_t7: 2.4218
hub_baseline_delta: -1.74
z_score_t7: -0.76
percentile_t7: 18.42
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/gold/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:03+00:00"
event_direction: "up"
event_actual: 309.698
event_previous: 308.741
event_delta: 0.957
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -1.1
  mdd_t7: -0.34
  volatility: 0.31
  impact_t1_pct: -0.03
  impact_t7_pct: -0.34
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
    direction: "up"
    sample_size: 38
    t1:
      up: 57.89
      down: 42.11
      median: 0.42
      mean: 0.35
      sample: 38
    t7:
      up: 78.95
      down: 21.05
      median: 1.4
      mean: 1.49
      sample: 38
related_events: [{"slug": "gold-after-cpi-2025-02-12", "title": "US CPI (2025-02-12) and GOLD: Event-Driven Return Odds", "event_date": "2025-02-12", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 7.09, "median_t7_pct": 1.52, "sample_size": 14}, {"slug": "gold-after-cpi-2024-02-20", "title": "US CPI (2024-02-20) and GOLD: Event-Driven Return Odds", "event_date": "2024-02-20", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 6.12, "median_t7_pct": 1.52, "sample_size": 14}, {"slug": "gold-after-cpi-2024-05-15", "title": "US CPI (2024-05-15) and GOLD: Event-Driven Return Odds", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.47, "median_t7_pct": 1.52, "sample_size": 14}]
chartData: [{"time": "2024-01-12", "open": 2031.1, "high": 2057.0, "low": 2031.1, "close": 2046.7}, {"time": "2024-01-16", "open": 2051.7, "high": 2054.8, "low": 2026.0, "close": 2026.0}, {"time": "2024-01-17", "open": 2026.5, "high": 2026.5, "low": 2002.6, "close": 2002.6}, {"time": "2024-01-18", "open": 2012.8, "high": 2018.6, "low": 2009.5, "close": 2018.6}, {"time": "2024-01-19", "open": 2023.2, "high": 2036.0, "low": 2019.5, "close": 2026.5}, {"time": "2024-01-22", "open": 2021.3, "high": 2021.3, "low": 2019.8, "close": 2019.8}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **GOLD**
- Event date: **2024-01-15**
- As-of date (T-1): **2026-03-08**
- Freshness age: **783 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 309.698, Previous 308.741, Delta +0.9570)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 56.41% | 43.59% | 0.34% | 0.3% | 39 |
| T+7 | 78.95% | 21.05% | 1.4% | 1.49% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 57.89% | 42.11% | 0.42% | 0.35% | 38 |
| T+7 | 78.95% | 21.05% | 1.4% | 1.49% | 38 |

## Historical Distribution Summary

When CPI was **UP**, GOLD T+1 up probability was **57.89%** (n=38).

When CPI was **UP**, GOLD T+7 up probability was **78.95%** (n=38).

Same-direction T+7 median return: **1.4%**.

For GOLD, historical CPI windows show all-history T+1 up probability of 56.41% and T+7 up probability of 78.95%. When CPI printed Up versus previous, T+1 up probability was 57.89% and T+7 up probability was 78.95% across 38 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
