---
title: "GOLD Reaction to US CPI (2025-01-15): Quant Probability Breakdown"
description: "Historical probability profile for GOLD around CPI events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-01-15"
asof_date: "2026-03-10"
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
freshness_days: 419
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.49
hub_baseline_median_t7: 1.4
hub_baseline_std_t7: 2.4218
hub_baseline_delta: 0.63
z_score_t7: 0.22
percentile_t7: 63.16
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/gold/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:04:05+00:00"
event_direction: "up"
event_actual: 318.961
event_previous: 317.604
event_delta: 1.357
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 2.6
  mdd_t7: 0.0
  volatility: 0.78
  impact_t1_pct: 1.25
  impact_t7_pct: 2.03
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
related_events: [{"slug": "gold-after-cpi-2025-02-12", "title": "US CPI (2025-02-12) and GOLD: Event-Driven Return Odds", "event_date": "2025-02-12", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 7.09, "median_t7_pct": 1.4, "sample_size": 39}, {"slug": "gold-after-cpi-2024-02-20", "title": "US CPI (2024-02-20) and GOLD: Event-Driven Return Odds", "event_date": "2024-02-20", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 6.12, "median_t7_pct": 1.4, "sample_size": 39}, {"slug": "gold-after-cpi-2024-05-15", "title": "US CPI (2024-05-15) and GOLD: Event-Driven Return Odds", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.47, "median_t7_pct": 1.4, "sample_size": 39}]
chartData: [{"time": "2025-01-13", "open": 2711.1, "high": 2711.2, "low": 2673.5, "close": 2673.5}, {"time": "2025-01-14", "open": 2673.6, "high": 2688.3, "low": 2670.8, "close": 2677.5}, {"time": "2025-01-15", "open": 2690.8, "high": 2712.5, "low": 2690.8, "close": 2712.5}, {"time": "2025-01-16", "open": 2731.7, "high": 2749.8, "low": 2731.7, "close": 2746.4}, {"time": "2025-01-17", "open": 2736.0, "high": 2751.6, "low": 2725.5, "close": 2744.3}, {"time": "2025-01-21", "open": 2746.0, "high": 2755.0, "low": 2724.8, "close": 2755.0}, {"time": "2025-01-22", "open": 2754.5, "high": 2768.8, "low": 2753.5, "close": 2767.6}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **GOLD**
- Event date: **2025-01-15**
- As-of date (T-1): **2026-03-10**
- Freshness age: **419 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 318.961, Previous 317.604, Delta +1.3570)
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
