---
title: "BTC After FOMC (2024-04-30): Historical Signal & Probability"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 1
title_template_key: "fomc_1"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-04-30"
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
freshness_days: 674
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.12
hub_baseline_median_t7: 0.31
hub_baseline_std_t7: 10.2392
hub_baseline_delta: 2.49
z_score_t7: 0.16
percentile_t7: 66.67
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 5.37
  mdd_t7: -3.93
  volatility: 6.73
  impact_t1_pct: -3.93
  impact_t7_pct: 2.8
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
related_events: [{"slug": "btc-after-fomc-2024-01-30", "title": "BTC Post-FOMC Reaction (2024-01-30): Quant Backtest Snapshot", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.97, "median_t7_pct": 0.31, "sample_size": 9}, {"slug": "btc-after-fomc-2026-01-28", "title": "FOMC Outcome (2026-01-28) for BTC: Up/Down Probability View", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.31, "sample_size": 9}, {"slug": "btc-after-fomc-2025-12-10", "title": "Fed Decision (2025-12-10) and BTC: Event-Driven Odds", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.31, "sample_size": 9}]
chartData: [{"time": "2024-04-27", "open": 63750.99, "high": 63898.36, "low": 62424.72, "close": 63419.14}, {"time": "2024-04-28", "open": 63423.52, "high": 64321.48, "low": 62793.6, "close": 63113.23}, {"time": "2024-04-29", "open": 63106.36, "high": 64174.88, "low": 61795.46, "close": 63841.12}, {"time": "2024-04-30", "open": 63839.42, "high": 64703.33, "low": 59120.07, "close": 60636.86}, {"time": "2024-05-01", "open": 60609.5, "high": 60780.5, "low": 56555.29, "close": 58254.01}, {"time": "2024-05-02", "open": 58253.7, "high": 59602.3, "low": 56937.2, "close": 59123.43}, {"time": "2024-05-03", "open": 59122.3, "high": 63320.5, "low": 58848.31, "close": 62889.84}, {"time": "2024-05-04", "open": 62891.03, "high": 64494.96, "low": 62599.35, "close": 63891.47}, {"time": "2024-05-05", "open": 63892.45, "high": 64610.89, "low": 62955.3, "close": 64031.13}, {"time": "2024-05-06", "open": 64038.31, "high": 65494.9, "low": 62746.24, "close": 63161.95}, {"time": "2024-05-07", "open": 63162.76, "high": 64390.46, "low": 62285.98, "close": 62334.82}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2024-04-30**
- As-of date (T-1): **2026-03-05**
- Freshness age: **674 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.5, Previous 5.5, Delta +0.0000)
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
