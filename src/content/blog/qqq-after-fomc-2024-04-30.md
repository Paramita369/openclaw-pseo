---
title: "FOMC Outcome (2024-04-30) for QQQ: Up/Down Probability View"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 5
title_template_key: "fomc_5"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-04-30"
asof_date: "2026-03-08"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 3.3
robust_score: -2.7
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 23
freshness_days: 677
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.27
hub_baseline_median_t7: 0.88
hub_baseline_std_t7: 2.891
hub_baseline_delta: 2.82
z_score_t7: 1.19
percentile_t7: 95.65
narrative_trigger: "extreme_outperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:53+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 0.84
  mdd_t7: -0.72
  volatility: 4.42
  impact_t1_pct: -0.72
  impact_t7_pct: 3.7
probabilities:
  sample_size: 23
  t1:
    up: 43.48
    down: 56.52
    median: -0.19
    mean: -0.05
    sample: 23
  t7:
    up: 56.52
    down: 43.48
    median: 0.88
    mean: 0.27
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 17
    t1:
      up: 41.18
      down: 58.82
      median: -0.34
      mean: -0.06
      sample: 17
    t7:
      up: 64.71
      down: 35.29
      median: 1.08
      mean: 0.6
      sample: 17
related_events: [{"slug": "qqq-after-fomc-2024-01-30", "title": "Fed Decision (2024-01-30) and QQQ: Event-Driven Odds", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 2.07, "median_t7_pct": 1.16, "sample_size": 9}, {"slug": "qqq-after-fomc-2026-01-28", "title": "Fed Decision (2026-01-28) and QQQ: Event-Driven Odds", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.88, "sample_size": 23}, {"slug": "qqq-after-fomc-2025-12-10", "title": "QQQ Post-FOMC Reaction (2025-12-10): Quant Backtest Snapshot", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.88, "sample_size": 23}]
chartData: [{"time": "2024-04-29", "open": 428.97, "high": 429.59, "low": 425.85, "close": 428.59}, {"time": "2024-04-30", "open": 427.0, "high": 428.4, "low": 420.43, "close": 420.51}, {"time": "2024-05-01", "open": 419.08, "high": 426.0, "low": 416.61, "close": 417.47}, {"time": "2024-05-02", "open": 421.21, "high": 423.7, "low": 416.59, "close": 422.79}, {"time": "2024-05-03", "open": 430.26, "high": 432.28, "low": 428.46, "close": 431.29}, {"time": "2024-05-06", "open": 433.09, "high": 436.11, "low": 432.32, "close": 436.02}, {"time": "2024-05-07", "open": 436.46, "high": 437.72, "low": 435.35, "close": 436.09}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
- Event date: **2024-04-30**
- As-of date (T-1): **2026-03-08**
- Freshness age: **677 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.5, Previous 5.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 43.48% | 56.52% | -0.19% | -0.05% | 23 |
| T+7 | 56.52% | 43.48% | 0.88% | 0.27% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 41.18% | 58.82% | -0.34% | -0.06% | 17 |
| T+7 | 64.71% | 35.29% | 1.08% | 0.6% | 17 |

## Historical Distribution Summary

When FOMC was **FLAT**, QQQ T+1 up probability was **41.18%** (n=17).

When FOMC was **FLAT**, QQQ T+7 up probability was **64.71%** (n=17).

Same-direction T+7 median return: **1.08%**.

For QQQ, historical FOMC windows show all-history T+1 up probability of 43.48% and T+7 up probability of 56.52%. When FOMC printed Flat versus previous, T+1 up probability was 41.18% and T+7 up probability was 64.71% across 17 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
