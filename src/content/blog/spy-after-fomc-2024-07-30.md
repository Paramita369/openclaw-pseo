---
title: "SPY After FOMC (2024-07-30): Historical Signal & Probability"
description: "Historical probability profile for SPY around FOMC events (T+1/T+7)."
pubDate: "2026-03-12"
title_variant_id: 1
title_template_key: "fomc_1"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-07-30"
asof_date: "2026-03-11"
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
freshness_days: 589
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 0.26
hub_baseline_median_t7: 0.54
hub_baseline_std_t7: 1.9274
hub_baseline_delta: -4.2
z_score_t7: -2.03
percentile_t7: 4.35
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -8.32
  mdd_t7: -5.2
  volatility: 5.29
  impact_t1_pct: 1.63
  impact_t7_pct: -3.66
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
chartData: [{"time": "2024-07-29", "open": 536.23, "high": 537.24, "low": 532.99, "close": 534.99}, {"time": "2024-07-30", "open": 536.46, "high": 537.52, "low": 528.86, "close": 532.28}, {"time": "2024-07-31", "open": 539.13, "high": 543.57, "low": 537.76, "close": 540.93}, {"time": "2024-08-01", "open": 542.66, "high": 544.92, "low": 529.76, "close": 533.27}, {"time": "2024-08-02", "open": 526.14, "high": 527.36, "low": 519.12, "close": 523.34}, {"time": "2024-08-05", "open": 502.46, "high": 514.19, "low": 501.12, "close": 508.1}, {"time": "2024-08-06", "open": 509.91, "high": 520.25, "low": 508.58, "close": 512.79}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **SPY**
- Event date: **2024-07-30**
- As-of date (T-1): **2026-03-11**
- Freshness age: **589 days**
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
