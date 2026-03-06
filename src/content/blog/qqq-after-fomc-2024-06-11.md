---
title: "Fed Decision (2024-06-11) and QQQ: Event-Driven Odds"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-06-11"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 17.56
robust_score: 7.56
penalties:
  sample: 4.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 9
freshness_days: 632
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 1.03
hub_baseline_median_t7: 1.16
hub_baseline_std_t7: 2.2487
hub_baseline_delta: 2.51
z_score_t7: 1.17
percentile_t7: 88.89
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 1.56
  mdd_t7: 0.0
  volatility: 2.36
  impact_t1_pct: 1.31
  impact_t7_pct: 3.67
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 0.43
    mean: 0.08
    sample: 9
  t7:
    up: 77.78
    down: 22.22
    median: 1.16
    mean: 1.03
    sample: 9
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 9
    t1:
      up: 55.56
      down: 44.44
      median: 0.43
      mean: 0.08
      sample: 9
    t7:
      up: 77.78
      down: 22.22
      median: 1.16
      mean: 1.03
      sample: 9
related_events: [{"slug": "qqq-after-fomc-2024-01-30", "title": "Fed Decision (2024-01-30) and QQQ: Event-Driven Odds", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 2.07, "median_t7_pct": 1.16, "sample_size": 9}, {"slug": "qqq-after-fomc-2026-01-28", "title": "Fed Decision (2026-01-28) and QQQ: Event-Driven Odds", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 1.16, "sample_size": 9}, {"slug": "qqq-after-fomc-2025-12-10", "title": "QQQ Post-FOMC Reaction (2025-12-10): Quant Backtest Snapshot", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 1.16, "sample_size": 9}]
chartData: [{"time": "2024-06-10", "open": 457.38, "high": 460.72, "low": 457.09, "close": 460.36}, {"time": "2024-06-11", "open": 459.08, "high": 463.64, "low": 457.59, "close": 463.52}, {"time": "2024-06-12", "open": 467.45, "high": 471.92, "low": 466.76, "close": 469.59}, {"time": "2024-06-13", "open": 473.13, "high": 473.79, "low": 469.86, "close": 472.14}, {"time": "2024-06-14", "open": 471.94, "high": 474.65, "low": 471.47, "close": 474.58}, {"time": "2024-06-17", "open": 474.85, "high": 482.18, "low": 473.54, "close": 480.4}, {"time": "2024-06-18", "open": 480.35, "high": 481.23, "low": 478.78, "close": 480.54}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
- Event date: **2024-06-11**
- As-of date (T-1): **2026-03-05**
- Freshness age: **632 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.5, Previous 5.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.43% | 0.08% | 9 |
| T+7 | 77.78% | 22.22% | 1.16% | 1.03% | 9 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.43% | 0.08% | 9 |
| T+7 | 77.78% | 22.22% | 1.16% | 1.03% | 9 |

## Historical Distribution Summary

When FOMC was **FLAT**, QQQ T+1 up probability was **55.56%** (n=9).

When FOMC was **FLAT**, QQQ T+7 up probability was **77.78%** (n=9).

Same-direction T+7 median return: **1.16%**.

For QQQ, historical FOMC windows show all-history T+1 up probability of 55.56% and T+7 up probability of 77.78%. When FOMC printed Flat versus previous, T+1 up probability was 55.56% and T+7 up probability was 77.78% across 9 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
