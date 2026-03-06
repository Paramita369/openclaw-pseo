---
title: "2024-12-17 FOMC Meeting: BTC T+1/T+7 Probability Profile"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "fomc_3"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-12-17"
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
quality_score: 80
sample_size: 9
freshness_days: 443
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 1.12
hub_baseline_median_t7: 0.31
hub_baseline_std_t7: 10.2392
hub_baseline_delta: -7.34
z_score_t7: -0.8
percentile_t7: 22.22
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "flat"
event_actual: 4.75
event_previous: 4.75
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -5.49
  mdd_t7: -7.03
  volatility: 1.28
  impact_t1_pct: -5.75
  impact_t7_pct: -7.03
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
chartData: [{"time": "2024-12-14", "open": 101451.44, "high": 102618.88, "low": 100634.05, "close": 101372.97}, {"time": "2024-12-15", "open": 101373.53, "high": 105047.54, "low": 101227.03, "close": 104298.7}, {"time": "2024-12-16", "open": 104293.58, "high": 107780.58, "low": 103322.98, "close": 106029.72}, {"time": "2024-12-17", "open": 106030.69, "high": 108268.45, "low": 105291.73, "close": 106140.6}, {"time": "2024-12-18", "open": 106147.3, "high": 106470.61, "low": 100041.54, "close": 100041.54}, {"time": "2024-12-19", "open": 100070.69, "high": 102748.15, "low": 95587.68, "close": 97490.95}, {"time": "2024-12-20", "open": 97484.7, "high": 98098.91, "low": 92175.18, "close": 97755.93}, {"time": "2024-12-21", "open": 97756.2, "high": 99507.1, "low": 96426.52, "close": 97224.73}, {"time": "2024-12-22", "open": 97218.32, "high": 97360.27, "low": 94202.19, "close": 95104.94}, {"time": "2024-12-23", "open": 95099.39, "high": 96416.21, "low": 92403.13, "close": 94686.24}, {"time": "2024-12-24", "open": 94684.34, "high": 99404.06, "low": 93448.02, "close": 98676.09}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2024-12-17**
- As-of date (T-1): **2026-03-05**
- Freshness age: **443 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.75, Previous 4.75, Delta +0.0000)
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
