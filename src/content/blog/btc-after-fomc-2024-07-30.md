---
title: "Fed Decision (2024-07-30) and BTC: Event-Driven Odds"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-07-30"
asof_date: "2026-03-08"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -4.61
robust_score: -10.61
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 23
freshness_days: 586
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: -0.7
hub_baseline_median_t7: -2.38
hub_baseline_std_t7: 9.162
hub_baseline_delta: -12.98
z_score_t7: -1.6
percentile_t7: 8.7
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:56+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.18
  mdd_t7: -15.36
  volatility: 12.97
  impact_t1_pct: -2.39
  impact_t7_pct: -15.36
probabilities:
  sample_size: 23
  t1:
    up: 52.17
    down: 47.83
    median: 0.27
    mean: -0.18
    sample: 23
  t7:
    up: 43.48
    down: 56.52
    median: -2.38
    mean: -0.7
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 17
    t1:
      up: 47.06
      down: 52.94
      median: -0.19
      mean: -0.15
      sample: 17
    t7:
      up: 47.06
      down: 52.94
      median: -2.38
      mean: -0.94
      sample: 17
related_events: [{"slug": "btc-after-fomc-2024-04-30", "title": "BTC After FOMC (2024-04-30): Historical Signal & Probability", "event_date": "2024-04-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 5.37, "median_t7_pct": 0.31, "sample_size": 9}, {"slug": "btc-after-fomc-2024-01-30", "title": "BTC Post-FOMC Reaction (2024-01-30): Quant Backtest Snapshot", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.97, "median_t7_pct": 0.31, "sample_size": 9}, {"slug": "btc-after-fomc-2026-01-28", "title": "FOMC Outcome (2026-01-28) for BTC: Up/Down Probability View", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -2.38, "sample_size": 23}]
chartData: [{"time": "2024-07-27", "open": 67911.81, "high": 69398.51, "low": 66705.22, "close": 67813.34}, {"time": "2024-07-28", "open": 67808.66, "high": 68301.85, "low": 67085.83, "close": 68255.87}, {"time": "2024-07-29", "open": 68259.05, "high": 69987.54, "low": 66532.59, "close": 66819.91}, {"time": "2024-07-30", "open": 66819.05, "high": 66987.67, "low": 65323.19, "close": 66201.02}, {"time": "2024-07-31", "open": 66201.27, "high": 66810.21, "low": 64532.05, "close": 64619.25}, {"time": "2024-08-01", "open": 64625.84, "high": 65593.24, "low": 62248.94, "close": 65357.5}, {"time": "2024-08-02", "open": 65353.5, "high": 65523.22, "low": 61184.89, "close": 61415.07}, {"time": "2024-08-03", "open": 61414.81, "high": 62148.37, "low": 59836.53, "close": 60680.09}, {"time": "2024-08-04", "open": 60676.09, "high": 61062.99, "low": 57210.8, "close": 58116.98}, {"time": "2024-08-05", "open": 58110.3, "high": 58268.83, "low": 49121.24, "close": 53991.46}, {"time": "2024-08-06", "open": 53991.35, "high": 57059.92, "low": 53973.27, "close": 56034.32}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2024-07-30**
- As-of date (T-1): **2026-03-08**
- Freshness age: **586 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.5, Previous 5.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 52.17% | 47.83% | 0.27% | -0.18% | 23 |
| T+7 | 43.48% | 56.52% | -2.38% | -0.7% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 47.06% | 52.94% | -0.19% | -0.15% | 17 |
| T+7 | 47.06% | 52.94% | -2.38% | -0.94% | 17 |

## Historical Distribution Summary

When FOMC was **FLAT**, BTC T+1 up probability was **47.06%** (n=17).

When FOMC was **FLAT**, BTC T+7 up probability was **47.06%** (n=17).

Same-direction T+7 median return: **-2.38%**.

For BTC, historical FOMC windows show all-history T+1 up probability of 52.17% and T+7 up probability of 43.48%. When FOMC printed Flat versus previous, T+1 up probability was 47.06% and T+7 up probability was 47.06% across 17 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
