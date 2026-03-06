---
title: "Fed Decision (2025-09-17) and BTC: Event-Driven Odds"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-09-17"
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
freshness_days: 169
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
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
chartData: [{"time": "2025-09-14", "open": 115950.29, "high": 116181.5, "low": 115222.4, "close": 115407.66}, {"time": "2025-09-15", "open": 115399.63, "high": 116747.88, "low": 114461.06, "close": 115444.88}, {"time": "2025-09-16", "open": 115423.76, "high": 117005.27, "low": 114813.09, "close": 116843.19}, {"time": "2025-09-17", "open": 116840.51, "high": 117328.61, "low": 114794.98, "close": 116468.51}, {"time": "2025-09-18", "open": 116461.27, "high": 117911.79, "low": 116188.8, "close": 117137.2}, {"time": "2025-09-19", "open": 117137.67, "high": 117479.76, "low": 115141.82, "close": 115688.86}, {"time": "2025-09-20", "open": 115691.12, "high": 116191.15, "low": 115473.52, "close": 115721.96}, {"time": "2025-09-21", "open": 115730.23, "high": 115901.09, "low": 115252.58, "close": 115306.09}, {"time": "2025-09-22", "open": 115309.22, "high": 115431.31, "low": 112037.65, "close": 112748.51}, {"time": "2025-09-23", "open": 112757.48, "high": 113351.91, "low": 111535.57, "close": 112014.5}, {"time": "2025-09-24", "open": 112007.66, "high": 113986.27, "low": 111229.64, "close": 113328.63}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2025-09-17**
- As-of date (T-1): **2026-03-05**
- Freshness age: **169 days**
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
