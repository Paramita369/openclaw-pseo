---
title: "ETH Post-FOMC Reaction (2024-01-30): Quant Backtest Snapshot"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 4
title_template_key: "fomc_4"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-01-30"
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
quality_score: 80
sample_size: 9
freshness_days: 765
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: -0.1
hub_baseline_median_t7: -0.19
hub_baseline_std_t7: 12.9045
hub_baseline_delta: 1.37
z_score_t7: 0.1
percentile_t7: 66.67
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 3.74
  mdd_t7: -2.64
  volatility: 3.82
  impact_t1_pct: -2.64
  impact_t7_pct: 1.18
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
related_events: [{"slug": "eth-after-fomc-2026-01-28", "title": "Fed Decision (2026-01-28) and ETH: Event-Driven Odds", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.19, "sample_size": 9}, {"slug": "eth-after-fomc-2025-12-10", "title": "2025-12-10 FOMC Meeting: ETH T+1/T+7 Probability Profile", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.19, "sample_size": 9}, {"slug": "eth-after-fomc-2025-10-29", "title": "ETH After FOMC (2025-10-29): Historical Signal & Probability", "event_date": "2025-10-29", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.19, "sample_size": 9}]
chartData: [{"time": "2024-01-27", "open": 2267.32, "high": 2282.54, "low": 2252.39, "close": 2267.89}, {"time": "2024-01-28", "open": 2268.19, "high": 2306.9, "low": 2242.68, "close": 2257.21}, {"time": "2024-01-29", "open": 2257.0, "high": 2320.03, "low": 2237.71, "close": 2317.06}, {"time": "2024-01-30", "open": 2317.44, "high": 2388.87, "low": 2298.28, "close": 2344.49}, {"time": "2024-01-31", "open": 2343.56, "high": 2349.61, "low": 2264.44, "close": 2282.54}, {"time": "2024-02-01", "open": 2282.18, "high": 2309.84, "low": 2243.57, "close": 2303.82}, {"time": "2024-02-02", "open": 2303.71, "high": 2323.05, "low": 2282.23, "close": 2308.04}, {"time": "2024-02-03", "open": 2307.98, "high": 2327.35, "low": 2293.54, "close": 2296.04}, {"time": "2024-02-04", "open": 2296.12, "high": 2309.01, "low": 2272.3, "close": 2289.55}, {"time": "2024-02-05", "open": 2289.21, "high": 2334.68, "low": 2270.07, "close": 2298.89}, {"time": "2024-02-06", "open": 2298.96, "high": 2389.83, "low": 2296.79, "close": 2372.2}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2024-01-30**
- As-of date (T-1): **2026-03-05**
- Freshness age: **765 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.5, Previous 5.5, Delta +0.0000)
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
