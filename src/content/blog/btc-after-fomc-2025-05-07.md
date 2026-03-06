---
title: "Fed Decision (2025-05-07) and BTC: Event-Driven Odds"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-05-07"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 6.45
robust_score: -3.55
penalties:
  sample: 4.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 60
sample_size: 9
freshness_days: 302
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 1.12
hub_baseline_median_t7: 0.31
hub_baseline_std_t7: 10.2392
hub_baseline_delta: 0.81
z_score_t7: 0.0
percentile_t7: 55.56
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "flat"
event_actual: 4.5
event_previous: 4.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 1.2
  mdd_t7: 0.0
  volatility: 0.93
  impact_t1_pct: 0.19
  impact_t7_pct: 1.12
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 0.35
    mean: 0.19
    sample: 9
  t7:
    up: 55.56
    down: 44.44
    median: 0.31
    mean: 1.12
    sample: 9
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 9
    t1:
      up: 55.56
      down: 44.44
      median: 0.35
      mean: 0.19
      sample: 9
    t7:
      up: 55.56
      down: 44.44
      median: 0.31
      mean: 1.12
      sample: 9
related_events: [{"slug": "btc-after-fomc-2024-04-30", "title": "BTC After FOMC (2024-04-30): Historical Signal & Probability", "event_date": "2024-04-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 5.37, "median_t7_pct": 0.31, "sample_size": 9}, {"slug": "btc-after-fomc-2024-01-30", "title": "BTC Post-FOMC Reaction (2024-01-30): Quant Backtest Snapshot", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.97, "median_t7_pct": 0.31, "sample_size": 9}, {"slug": "btc-after-fomc-2026-01-28", "title": "FOMC Outcome (2026-01-28) for BTC: Up/Down Probability View", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.31, "sample_size": 9}]
chartData: [{"time": "2025-05-04", "open": 95877.19, "high": 96318.92, "low": 94173.43, "close": 94315.98}, {"time": "2025-05-05", "open": 94319.56, "high": 95193.19, "low": 93566.27, "close": 94748.05}, {"time": "2025-05-06", "open": 94748.38, "high": 96889.18, "low": 93399.86, "close": 96802.48}, {"time": "2025-05-07", "open": 96800.2, "high": 97625.8, "low": 95829.34, "close": 97032.32}, {"time": "2025-05-08", "open": 97034.25, "high": 103969.54, "low": 96913.88, "close": 103241.46}, {"time": "2025-05-09", "open": 103239.12, "high": 104297.49, "low": 102343.09, "close": 102970.85}, {"time": "2025-05-10", "open": 102973.71, "high": 104961.77, "low": 102830.48, "close": 104696.33}, {"time": "2025-05-11", "open": 104701.07, "high": 104937.99, "low": 103364.74, "close": 104106.36}, {"time": "2025-05-12", "open": 104106.96, "high": 105747.45, "low": 100814.41, "close": 102812.95}, {"time": "2025-05-13", "open": 102812.49, "high": 104997.42, "low": 101515.09, "close": 104169.81}, {"time": "2025-05-14", "open": 104167.33, "high": 104303.56, "low": 102618.3, "close": 103539.41}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2025-05-07**
- As-of date (T-1): **2026-03-05**
- Freshness age: **302 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.5, Previous 4.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.35% | 0.19% | 9 |
| T+7 | 55.56% | 44.44% | 0.31% | 1.12% | 9 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.35% | 0.19% | 9 |
| T+7 | 55.56% | 44.44% | 0.31% | 1.12% | 9 |

## Historical Distribution Summary

When FOMC was **FLAT**, BTC T+1 up probability was **55.56%** (n=9).

When FOMC was **FLAT**, BTC T+7 up probability was **55.56%** (n=9).

Same-direction T+7 median return: **0.31%**.

For BTC, historical FOMC windows show all-history T+1 up probability of 55.56% and T+7 up probability of 55.56%. When FOMC printed Flat versus previous, T+1 up probability was 55.56% and T+7 up probability was 55.56% across 9 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
