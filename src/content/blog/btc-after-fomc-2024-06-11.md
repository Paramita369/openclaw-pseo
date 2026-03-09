---
title: "FOMC Outcome (2024-06-11) for BTC: Up/Down Probability View"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 5
title_template_key: "fomc_5"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-06-11"
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
freshness_days: 635
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: -0.7
hub_baseline_median_t7: -2.38
hub_baseline_std_t7: 9.162
hub_baseline_delta: -0.87
z_score_t7: -0.28
percentile_t7: 43.48
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:54+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -0.71
  mdd_t7: -3.25
  volatility: 4.6
  impact_t1_pct: 1.35
  impact_t7_pct: -3.25
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
chartData: [{"time": "2024-06-08", "open": 69324.18, "high": 69533.32, "low": 69210.74, "close": 69305.77}, {"time": "2024-06-09", "open": 69297.49, "high": 69817.52, "low": 69160.84, "close": 69647.99}, {"time": "2024-06-10", "open": 69644.31, "high": 70146.07, "low": 69232.42, "close": 69512.28}, {"time": "2024-06-11", "open": 69508.08, "high": 69549.41, "low": 66123.6, "close": 67332.03}, {"time": "2024-06-12", "open": 67321.38, "high": 69977.89, "low": 66902.45, "close": 68241.19}, {"time": "2024-06-13", "open": 68243.1, "high": 68365.78, "low": 66304.56, "close": 66756.4}, {"time": "2024-06-14", "open": 66747.57, "high": 67294.65, "low": 65056.89, "close": 66011.09}, {"time": "2024-06-15", "open": 66006.74, "high": 66402.19, "low": 65871.77, "close": 66191.0}, {"time": "2024-06-16", "open": 66189.36, "high": 66894.84, "low": 66018.25, "close": 66639.05}, {"time": "2024-06-17", "open": 66636.52, "high": 67188.32, "low": 65094.96, "close": 66490.3}, {"time": "2024-06-18", "open": 66490.98, "high": 66556.7, "low": 64066.96, "close": 65140.75}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2024-06-11**
- As-of date (T-1): **2026-03-08**
- Freshness age: **635 days**
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
