---
title: "BTC Reaction to US CPI (2025-10-12): Quant Probability Breakdown"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-10-12"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 3.43
robust_score: -2.57
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 70
sample_size: 14
freshness_days: 144
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 1.69
hub_baseline_median_t7: 3.64
hub_baseline_std_t7: 8.5155
hub_baseline_delta: -1.95
z_score_t7: -0.0
percentile_t7: 42.86
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 324.245
event_previous: 323.291
event_delta: 0.954
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 1.18
  mdd_t7: 0.0
  volatility: 1.43
  impact_t1_pct: 0.26
  impact_t7_pct: 1.69
probabilities:
  sample_size: 14
  t1:
    up: 42.86
    down: 57.14
    median: -0.74
    mean: 0.26
    sample: 14
  t7:
    up: 57.14
    down: 42.86
    median: 3.64
    mean: 1.69
    sample: 14
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 46.15
      down: 53.85
      median: -0.74
      mean: 0.44
      sample: 13
    t7:
      up: 61.54
      down: 38.46
      median: 4.15
      mean: 2.19
      sample: 13
related_events: [{"slug": "btc-after-cpi-2024-08-14", "title": "BTC Reaction to US CPI (2024-08-14): Quant Probability Breakdown", "event_date": "2024-08-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.86, "median_t7_pct": 3.64, "sample_size": 14}, {"slug": "btc-after-cpi-2026-02-12", "title": "BTC After CPI (2026-02-12): Up/Down Odds and Median Returns", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 3.64, "sample_size": 14}, {"slug": "btc-after-cpi-2026-01-12", "title": "BTC CPI Win Rate (2026-01-12): Historical T+1/T+7 Probability", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 3.64, "sample_size": 14}]
chartData: [{"time": "2025-10-09", "open": 123337.07, "high": 123739.34, "low": 119812.03, "close": 121705.59}, {"time": "2025-10-10", "open": 121704.74, "high": 122509.66, "low": 104582.41, "close": 113214.37}, {"time": "2025-10-11", "open": 113236.43, "high": 113429.73, "low": 109760.56, "close": 110807.88}, {"time": "2025-10-12", "open": 110811.52, "high": 115805.06, "low": 109715.54, "close": 115169.77}, {"time": "2025-10-13", "open": 115161.68, "high": 116020.48, "low": 113821.19, "close": 115271.08}, {"time": "2025-10-14", "open": 115264.88, "high": 115502.88, "low": 110029.48, "close": 113118.66}, {"time": "2025-10-15", "open": 113113.97, "high": 113622.38, "low": 110235.84, "close": 110783.16}, {"time": "2025-10-16", "open": 110782.17, "high": 111990.81, "low": 107537.03, "close": 108186.04}, {"time": "2025-10-17", "open": 108179.13, "high": 109235.8, "low": 103598.43, "close": 106467.79}, {"time": "2025-10-18", "open": 106483.73, "high": 107490.98, "low": 106387.45, "close": 107198.27}, {"time": "2025-10-19", "open": 107204.31, "high": 109488.99, "low": 106157.79, "close": 108666.71}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2025-10-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **144 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 324.245, Previous 323.291, Delta +0.9540)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 42.86% | 57.14% | -0.74% | 0.26% | 14 |
| T+7 | 57.14% | 42.86% | 3.64% | 1.69% | 14 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 46.15% | 53.85% | -0.74% | 0.44% | 13 |
| T+7 | 61.54% | 38.46% | 4.15% | 2.19% | 13 |

## Historical Distribution Summary

When CPI was **UP**, BTC T+1 up probability was **46.15%** (n=13).

When CPI was **UP**, BTC T+7 up probability was **61.54%** (n=13).

Same-direction T+7 median return: **4.15%**.

For BTC, historical CPI windows show all-history T+1 up probability of 42.86% and T+7 up probability of 57.14%. When CPI printed Up versus previous, T+1 up probability was 46.15% and T+7 up probability was 61.54% across 13 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
