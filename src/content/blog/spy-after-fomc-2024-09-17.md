---
title: "2024-09-17 FOMC Meeting: SPY T+1/T+7 Probability Profile"
description: "Historical probability profile for SPY around FOMC events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 3
title_template_key: "fomc_3"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-09-17"
asof_date: "2026-03-09"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 5.91
robust_score: -0.09
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 23
freshness_days: 538
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.26
hub_baseline_median_t7: 0.54
hub_baseline_std_t7: 1.9274
hub_baseline_delta: 1.23
z_score_t7: 0.78
percentile_t7: 78.26
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:59+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 0.86
  mdd_t7: -0.3
  volatility: 2.07
  impact_t1_pct: -0.3
  impact_t7_pct: 1.77
probabilities:
  sample_size: 23
  t1:
    up: 52.17
    down: 47.83
    median: 0.1
    mean: -0.02
    sample: 23
  t7:
    up: 56.52
    down: 43.48
    median: 0.54
    mean: 0.26
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 17
    t1:
      up: 47.06
      down: 52.94
      median: -0.2
      mean: -0.08
      sample: 17
    t7:
      up: 64.71
      down: 35.29
      median: 0.57
      mean: 0.48
      sample: 17
related_events: [{"slug": "spy-after-fomc-2025-01-29", "title": "Fed Decision (2025-01-29) and SPY: Event-Driven Odds", "event_date": "2025-01-29", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 9.47, "median_t7_pct": 0.54, "sample_size": 23}, {"slug": "spy-after-fomc-2024-03-19", "title": "SPY After FOMC (2024-03-19): Historical Signal & Probability", "event_date": "2024-03-19", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 7.7, "median_t7_pct": 0.54, "sample_size": 23}, {"slug": "spy-after-fomc-2024-01-30", "title": "Fed Decision (2024-01-30) and SPY: Event-Driven Odds", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.69, "median_t7_pct": 0.54, "sample_size": 23}]
chartData: [{"time": "2024-09-16", "open": 551.67, "high": 553.01, "low": 549.86, "close": 552.75}, {"time": "2024-09-17", "open": 554.97, "high": 556.42, "low": 550.73, "close": 552.97}, {"time": "2024-09-18", "open": 553.63, "high": 558.49, "low": 550.77, "close": 551.33}, {"time": "2024-09-19", "open": 560.77, "high": 562.61, "low": 557.89, "close": 560.74}, {"time": "2024-09-20", "open": 559.37, "high": 560.81, "low": 556.74, "close": 559.77}, {"time": "2024-09-23", "open": 560.84, "high": 561.82, "low": 559.62, "close": 561.17}, {"time": "2024-09-24", "open": 561.97, "high": 562.83, "low": 559.13, "close": 562.77}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **SPY**
- Event date: **2024-09-17**
- As-of date (T-1): **2026-03-09**
- Freshness age: **538 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.5, Previous 5.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 52.17% | 47.83% | 0.1% | -0.02% | 23 |
| T+7 | 56.52% | 43.48% | 0.54% | 0.26% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 47.06% | 52.94% | -0.2% | -0.08% | 17 |
| T+7 | 64.71% | 35.29% | 0.57% | 0.48% | 17 |

## Historical Distribution Summary

When FOMC was **FLAT**, SPY T+1 up probability was **47.06%** (n=17).

When FOMC was **FLAT**, SPY T+7 up probability was **64.71%** (n=17).

Same-direction T+7 median return: **0.57%**.

For SPY, historical FOMC windows show all-history T+1 up probability of 52.17% and T+7 up probability of 56.52%. When FOMC printed Flat versus previous, T+1 up probability was 47.06% and T+7 up probability was 64.71% across 17 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
