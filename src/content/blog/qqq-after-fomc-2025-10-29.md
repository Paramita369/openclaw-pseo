---
title: "2025-10-29 FOMC Meeting: QQQ T+1/T+7 Probability Profile"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "fomc_3"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-10-29"
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
quality_score: 60
sample_size: 9
freshness_days: 127
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 1.03
hub_baseline_median_t7: 1.16
hub_baseline_std_t7: 2.2487
hub_baseline_delta: -0.13
z_score_t7: 0.0
percentile_t7: 33.33
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "flat"
event_actual: 4.25
event_previous: 4.25
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 1.08
  mdd_t7: 0.0
  volatility: 0.95
  impact_t1_pct: 0.08
  impact_t7_pct: 1.03
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
chartData: [{"time": "2025-10-27", "open": 623.72, "high": 627.74, "low": 623.23, "close": 627.28}, {"time": "2025-10-28", "open": 629.55, "high": 633.86, "low": 628.44, "close": 632.11}, {"time": "2025-10-29", "open": 634.77, "high": 636.19, "low": 629.44, "close": 634.95}, {"time": "2025-10-30", "open": 631.36, "high": 632.68, "low": 625.13, "close": 625.24}, {"time": "2025-10-31", "open": 633.35, "high": 633.38, "low": 625.88, "close": 628.26}, {"time": "2025-11-03", "open": 634.29, "high": 635.0, "low": 629.04, "close": 631.27}, {"time": "2025-11-04", "open": 622.48, "high": 626.14, "low": 617.66, "close": 618.45}, {"time": "2025-11-05", "open": 617.69, "high": 625.79, "low": 616.42, "close": 622.48}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
- Event date: **2025-10-29**
- As-of date (T-1): **2026-03-05**
- Freshness age: **127 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.25, Previous 4.25, Delta +0.0000)
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
