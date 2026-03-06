---
title: "GOLD After CPI (2024-04-10): Up/Down Odds and Median Returns"
description: "Historical probability profile for GOLD around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "cpi_5"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-04-10"
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
quality_score: 90
sample_size: 14
freshness_days: 694
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 1.07
hub_baseline_median_t7: 1.52
hub_baseline_std_t7: 1.8614
hub_baseline_delta: 0.29
z_score_t7: 0.4
percentile_t7: 61.54
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/gold/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 313.023
event_previous: 312.345
event_delta: 0.678
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 2.48
  mdd_t7: 0.0
  volatility: 0.73
  impact_t1_pct: 1.08
  impact_t7_pct: 1.81
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
    direction: "up"
    sample_size: 13
    t1:
      up: 53.85
      down: 46.15
      median: 0.56
      mean: 0.36
      sample: 13
    t7:
      up: 76.92
      down: 23.08
      median: 1.52
      mean: 1.07
      sample: 13
related_events: [{"slug": "gold-after-cpi-2025-02-12", "title": "US CPI (2025-02-12) and GOLD: Event-Driven Return Odds", "event_date": "2025-02-12", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 7.09, "median_t7_pct": 1.52, "sample_size": 14}, {"slug": "gold-after-cpi-2024-02-20", "title": "US CPI (2024-02-20) and GOLD: Event-Driven Return Odds", "event_date": "2024-02-20", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 6.12, "median_t7_pct": 1.52, "sample_size": 14}, {"slug": "gold-after-cpi-2024-05-15", "title": "US CPI (2024-05-15) and GOLD: Event-Driven Return Odds", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.47, "median_t7_pct": 1.52, "sample_size": 14}]
chartData: [{"time": "2024-04-08", "open": 2325.6, "high": 2341.8, "low": 2319.0, "close": 2331.7}, {"time": "2024-04-09", "open": 2337.8, "high": 2364.7, "low": 2337.8, "close": 2343.5}, {"time": "2024-04-10", "open": 2346.6, "high": 2358.1, "low": 2327.7, "close": 2329.6}, {"time": "2024-04-11", "open": 2341.5, "high": 2376.3, "low": 2330.6, "close": 2354.8}, {"time": "2024-04-12", "open": 2377.3, "high": 2429.0, "low": 2334.3, "close": 2356.2}, {"time": "2024-04-15", "open": 2362.1, "high": 2384.7, "low": 2326.0, "close": 2365.8}, {"time": "2024-04-16", "open": 2384.0, "high": 2390.8, "low": 2371.4, "close": 2390.8}, {"time": "2024-04-17", "open": 2384.2, "high": 2391.4, "low": 2369.3, "close": 2371.7}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **GOLD**
- Event date: **2024-04-10**
- As-of date (T-1): **2026-03-05**
- Freshness age: **694 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 313.023, Previous 312.345, Delta +0.6780)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.27% | 0.22% | 14 |
| T+7 | 76.92% | 23.08% | 1.52% | 1.07% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.56% | 0.36% | 13 |
| T+7 | 76.92% | 23.08% | 1.52% | 1.07% | 13 |

## Historical Distribution Summary

When CPI was **UP**, GOLD T+1 up probability was **53.85%** (n=13).

When CPI was **UP**, GOLD T+7 up probability was **76.92%** (n=13).

Same-direction T+7 median return: **1.52%**.

For GOLD, historical CPI windows show all-history T+1 up probability of 50.0% and T+7 up probability of 76.92%. When CPI printed Up versus previous, T+1 up probability was 53.85% and T+7 up probability was 76.92% across 13 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
