---
title: "FOMC Outcome (2025-03-19) for ETH: Up/Down Probability View"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "fomc_5"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-03-19"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -3.11
robust_score: -13.11
penalties:
  sample: 4.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 60
sample_size: 9
freshness_days: 351
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: -0.1
hub_baseline_median_t7: -0.19
hub_baseline_std_t7: 12.9045
hub_baseline_delta: 0.09
z_score_t7: -0.0
percentile_t7: 55.56
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "flat"
event_actual: 4.5
event_previous: 4.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -0.07
  mdd_t7: -0.1
  volatility: 1.48
  impact_t1_pct: 1.38
  impact_t7_pct: -0.1
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 1.2
    mean: 1.38
    sample: 9
  t7:
    up: 44.44
    down: 55.56
    median: -0.19
    mean: -0.1
    sample: 9
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 9
    t1:
      up: 55.56
      down: 44.44
      median: 1.2
      mean: 1.38
      sample: 9
    t7:
      up: 44.44
      down: 55.56
      median: -0.19
      mean: -0.1
      sample: 9
related_events: [{"slug": "eth-after-fomc-2024-01-30", "title": "ETH Post-FOMC Reaction (2024-01-30): Quant Backtest Snapshot", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 3.74, "median_t7_pct": -0.19, "sample_size": 9}, {"slug": "eth-after-fomc-2026-01-28", "title": "Fed Decision (2026-01-28) and ETH: Event-Driven Odds", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.19, "sample_size": 9}, {"slug": "eth-after-fomc-2025-12-10", "title": "2025-12-10 FOMC Meeting: ETH T+1/T+7 Probability Profile", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.19, "sample_size": 9}]
chartData: [{"time": "2025-03-16", "open": 1937.38, "high": 1940.47, "low": 1863.49, "close": 1887.44}, {"time": "2025-03-17", "open": 1887.45, "high": 1951.63, "low": 1880.48, "close": 1927.0}, {"time": "2025-03-18", "open": 1927.01, "high": 1935.18, "low": 1872.51, "close": 1932.54}, {"time": "2025-03-19", "open": 1932.54, "high": 2068.76, "low": 1928.25, "close": 2057.75}, {"time": "2025-03-20", "open": 2057.95, "high": 2067.48, "low": 1952.24, "close": 1982.1}, {"time": "2025-03-21", "open": 1981.85, "high": 1994.89, "low": 1937.21, "close": 1964.85}, {"time": "2025-03-22", "open": 1964.94, "high": 2005.04, "low": 1964.27, "close": 1980.04}, {"time": "2025-03-23", "open": 1979.98, "high": 2019.89, "low": 1977.71, "close": 2005.3}, {"time": "2025-03-24", "open": 2005.72, "high": 2101.98, "low": 1978.76, "close": 2077.48}, {"time": "2025-03-25", "open": 2078.57, "high": 2096.52, "low": 2038.64, "close": 2067.76}, {"time": "2025-03-26", "open": 2067.51, "high": 2078.37, "low": 1982.41, "close": 2009.19}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2025-03-19**
- As-of date (T-1): **2026-03-05**
- Freshness age: **351 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.5, Previous 4.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 1.2% | 1.38% | 9 |
| T+7 | 44.44% | 55.56% | -0.19% | -0.1% | 9 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 1.2% | 1.38% | 9 |
| T+7 | 44.44% | 55.56% | -0.19% | -0.1% | 9 |

## Historical Distribution Summary

When FOMC was **FLAT**, ETH T+1 up probability was **55.56%** (n=9).

When FOMC was **FLAT**, ETH T+7 up probability was **44.44%** (n=9).

Same-direction T+7 median return: **-0.19%**.

For ETH, historical FOMC windows show all-history T+1 up probability of 55.56% and T+7 up probability of 44.44%. When FOMC printed Flat versus previous, T+1 up probability was 55.56% and T+7 up probability was 44.44% across 9 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
