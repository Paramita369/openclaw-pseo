---
title: "US CPI (2025-03-12) and ETH: Event-Driven Return Odds"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-03-12"
asof_date: "2026-03-09"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -2.51
robust_score: -8.51
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 39
freshness_days: 362
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.23
hub_baseline_median_t7: -1.18
hub_baseline_std_t7: 9.719
hub_baseline_delta: 8.97
z_score_t7: 0.78
percentile_t7: 76.92
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 319.785
event_previous: 319.679
event_delta: 0.106
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.76
  mdd_t7: -2.41
  volatility: 10.2
  impact_t1_pct: -2.41
  impact_t7_pct: 7.79
probabilities:
  sample_size: 39
  t1:
    up: 58.97
    down: 41.03
    median: 0.94
    mean: 0.55
    sample: 39
  t7:
    up: 43.59
    down: 56.41
    median: -1.18
    mean: 0.23
    sample: 39
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.96
      mean: 0.64
      sample: 38
    t7:
      up: 44.74
      down: 55.26
      median: -1.52
      mean: 0.24
      sample: 38
related_events: [{"slug": "eth-after-cpi-2024-06-12", "title": "ETH Reaction to US CPI (2024-06-12): Quant Probability Breakdown", "event_date": "2024-06-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.22, "median_t7_pct": -1.18, "sample_size": 39}, {"slug": "eth-after-cpi-2026-02-12", "title": "ETH CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.18, "sample_size": 39}, {"slug": "eth-after-cpi-2026-01-12", "title": "2026-01-12 CPI Release: ETH Directional Probability Snapshot", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.18, "sample_size": 39}]
chartData: [{"time": "2025-03-09", "open": 2201.71, "high": 2210.31, "low": 1991.19, "close": 2015.51}, {"time": "2025-03-10", "open": 2015.43, "high": 2150.71, "low": 1812.77, "close": 1861.15}, {"time": "2025-03-11", "open": 1859.78, "high": 1961.8, "low": 1760.94, "close": 1919.84}, {"time": "2025-03-12", "open": 1919.66, "high": 1954.57, "low": 1832.02, "close": 1908.98}, {"time": "2025-03-13", "open": 1909.02, "high": 1919.69, "low": 1823.53, "close": 1862.97}, {"time": "2025-03-14", "open": 1863.0, "high": 1945.09, "low": 1861.11, "close": 1909.47}, {"time": "2025-03-15", "open": 1909.53, "high": 1955.24, "low": 1904.97, "close": 1937.39}, {"time": "2025-03-16", "open": 1937.38, "high": 1940.47, "low": 1863.49, "close": 1887.44}, {"time": "2025-03-17", "open": 1887.45, "high": 1951.63, "low": 1880.48, "close": 1927.0}, {"time": "2025-03-18", "open": 1927.01, "high": 1935.18, "low": 1872.51, "close": 1932.54}, {"time": "2025-03-19", "open": 1932.54, "high": 2068.76, "low": 1928.25, "close": 2057.75}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2025-03-12**
- As-of date (T-1): **2026-03-09**
- Freshness age: **362 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 319.785, Previous 319.679, Delta +0.1060)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.94% | 0.55% | 39 |
| T+7 | 43.59% | 56.41% | -1.18% | 0.23% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.96% | 0.64% | 38 |
| T+7 | 44.74% | 55.26% | -1.52% | 0.24% | 38 |

## Historical Distribution Summary

When CPI was **UP**, ETH T+1 up probability was **60.53%** (n=38).

When CPI was **UP**, ETH T+7 up probability was **44.74%** (n=38).

Same-direction T+7 median return: **-1.52%**.

For ETH, historical CPI windows show all-history T+1 up probability of 58.97% and T+7 up probability of 43.59%. When CPI printed Up versus previous, T+1 up probability was 60.53% and T+7 up probability was 44.74% across 38 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
