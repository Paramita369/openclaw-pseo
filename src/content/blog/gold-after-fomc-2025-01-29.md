---
title: "GOLD Post-FOMC Reaction (2025-01-29): Quant Backtest Snapshot"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 4
title_template_key: "fomc_4"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-01-29"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 22.0
robust_score: 12.0
penalties:
  sample: 4.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 9
freshness_days: 400
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.59
hub_baseline_median_t7: 0.9
hub_baseline_std_t7: 2.0208
hub_baseline_delta: 2.8
z_score_t7: 1.54
percentile_t7: 100.0
narrative_trigger: "extreme_outperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/gold/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "flat"
event_actual: 4.5
event_previous: 4.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 2.11
  mdd_t7: 0.0
  volatility: 1.75
  impact_t1_pct: 1.95
  impact_t7_pct: 3.7
probabilities:
  sample_size: 9
  t1:
    up: 88.89
    down: 11.11
    median: 0.83
    mean: 0.72
    sample: 9
  t7:
    up: 66.67
    down: 33.33
    median: 0.9
    mean: 0.59
    sample: 9
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 9
    t1:
      up: 88.89
      down: 11.11
      median: 0.83
      mean: 0.72
      sample: 9
    t7:
      up: 66.67
      down: 33.33
      median: 0.9
      mean: 0.59
      sample: 9
related_events: [{"slug": "gold-after-fomc-2024-01-30", "title": "2024-01-30 FOMC Meeting: GOLD T+1/T+7 Probability Profile", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 1.61, "median_t7_pct": 0.9, "sample_size": 9}, {"slug": "gold-after-fomc-2026-01-28", "title": "GOLD After FOMC (2026-01-28): Historical Signal & Probability", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 0.9, "sample_size": 9}, {"slug": "gold-after-fomc-2025-12-10", "title": "2025-12-10 FOMC Meeting: GOLD T+1/T+7 Probability Profile", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 0.9, "sample_size": 9}]
chartData: [{"time": "2025-01-27", "open": 2761.1, "high": 2762.2, "low": 2737.5, "close": 2737.5}, {"time": "2025-01-28", "open": 2738.0, "high": 2766.8, "low": 2738.0, "close": 2766.8}, {"time": "2025-01-29", "open": 2769.1, "high": 2769.1, "low": 2769.1, "close": 2769.1}, {"time": "2025-01-30", "open": 2772.5, "high": 2829.5, "low": 2770.0, "close": 2823.0}, {"time": "2025-01-31", "open": 2829.0, "high": 2838.0, "low": 2804.0, "close": 2812.5}, {"time": "2025-02-03", "open": 2818.2, "high": 2848.4, "low": 2780.9, "close": 2833.9}, {"time": "2025-02-04", "open": 2827.6, "high": 2853.3, "low": 2816.1, "close": 2853.3}, {"time": "2025-02-05", "open": 2850.0, "high": 2880.5, "low": 2848.0, "close": 2871.6}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2025-01-29**
- As-of date (T-1): **2026-03-05**
- Freshness age: **400 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.5, Previous 4.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 88.89% | 11.11% | 0.83% | 0.72% | 9 |
| T+7 | 66.67% | 33.33% | 0.9% | 0.59% | 9 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 88.89% | 11.11% | 0.83% | 0.72% | 9 |
| T+7 | 66.67% | 33.33% | 0.9% | 0.59% | 9 |

## Historical Distribution Summary

When FOMC was **FLAT**, GOLD T+1 up probability was **88.89%** (n=9).

When FOMC was **FLAT**, GOLD T+7 up probability was **66.67%** (n=9).

Same-direction T+7 median return: **0.9%**.

For GOLD, historical FOMC windows show all-history T+1 up probability of 88.89% and T+7 up probability of 66.67%. When FOMC printed Flat versus previous, T+1 up probability was 88.89% and T+7 up probability was 66.67% across 9 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
