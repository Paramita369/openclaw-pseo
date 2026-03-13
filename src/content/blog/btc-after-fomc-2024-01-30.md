---
title: "BTC Post-FOMC Reaction (2024-01-30): Quant Backtest Snapshot"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-12"
title_variant_id: 4
title_template_key: "fomc_4"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-01-30"
asof_date: "2026-03-11"
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
freshness_days: 771
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: -0.7
hub_baseline_median_t7: -2.38
hub_baseline_std_t7: 9.162
hub_baseline_delta: 2.69
z_score_t7: 0.11
percentile_t7: 65.22
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 2.97
  mdd_t7: -0.86
  volatility: 1.17
  impact_t1_pct: -0.86
  impact_t7_pct: 0.31
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
related_events: [{"slug": "btc-after-fomc-2024-04-30", "title": "BTC After FOMC (2024-04-30): Historical Signal & Probability", "event_date": "2024-04-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 5.37, "median_t7_pct": -2.38, "sample_size": 23}, {"slug": "btc-after-fomc-2026-01-28", "title": "FOMC Outcome (2026-01-28) for BTC: Up/Down Probability View", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -2.38, "sample_size": 23}, {"slug": "btc-after-fomc-2025-12-10", "title": "Fed Decision (2025-12-10) and BTC: Event-Driven Odds", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -2.38, "sample_size": 23}]
chartData: [{"time": "2024-01-27", "open": 41815.62, "high": 42195.63, "low": 41431.28, "close": 42120.05}, {"time": "2024-01-28", "open": 42126.12, "high": 42797.18, "low": 41696.91, "close": 42035.59}, {"time": "2024-01-29", "open": 42030.91, "high": 43305.87, "low": 41818.33, "close": 43288.25}, {"time": "2024-01-30", "open": 43300.23, "high": 43838.95, "low": 42711.37, "close": 42952.61}, {"time": "2024-01-31", "open": 42946.25, "high": 43717.41, "low": 42298.95, "close": 42582.61}, {"time": "2024-02-01", "open": 42569.76, "high": 43243.17, "low": 41879.19, "close": 43075.77}, {"time": "2024-02-02", "open": 43077.64, "high": 43422.49, "low": 42584.34, "close": 43185.86}, {"time": "2024-02-03", "open": 43184.96, "high": 43359.94, "low": 42890.81, "close": 42992.25}, {"time": "2024-02-04", "open": 42994.94, "high": 43097.64, "low": 42374.83, "close": 42583.58}, {"time": "2024-02-05", "open": 42577.62, "high": 43494.25, "low": 42264.82, "close": 42658.67}, {"time": "2024-02-06", "open": 42657.39, "high": 43344.15, "low": 42529.02, "close": 43084.67}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2024-01-30**
- As-of date (T-1): **2026-03-11**
- Freshness age: **771 days**
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
