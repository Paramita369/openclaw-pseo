---
title: "Fed Decision (2025-12-10) and SPY: Event-Driven Odds"
description: "Historical probability profile for SPY around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-12-10"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 5.91
robust_score: 5.91
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 100
sample_size: 23
freshness_days: 83
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/spy-after-fomc-2025-12-10"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "flat"
event_actual: 4.0
event_previous: 4.0
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -10.0
  mdd_t7: -2.58
  volatility: 11.49
  impact_t1_pct: 0.23
  impact_t7_pct: -2.35
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
related_events: [{"slug": "spy-after-fomc-2025-06-18", "title": "SPY After FOMC (2025-06-18): Historical T+1/T+7 Probability", "event_date": "2025-06-18", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.92, "sample_size": 0}, {"slug": "spy-after-fomc-2025-05-07", "title": "SPY After FOMC (2025-05-07): Historical T+1/T+7 Probability", "event_date": "2025-05-07", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.71, "sample_size": 0}, {"slug": "spy-after-fomc-2024-12-19", "title": "SPY After FOMC (2024-12-19): Historical T+1/T+7 Probability", "event_date": "2024-12-19", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.95, "sample_size": 0}]
chartData: [{"time": "2025-12-08", "open": 684.57, "high": 684.62, "low": 679.56, "close": 681.62}, {"time": "2025-12-09", "open": 681.14, "high": 683.37, "low": 680.58, "close": 681.03}, {"time": "2025-12-10", "open": 680.55, "high": 686.94, "low": 679.3, "close": 685.54}, {"time": "2025-12-11", "open": 683.12, "high": 687.22, "low": 680.16, "close": 687.14}, {"time": "2025-12-12", "open": 686.14, "high": 686.85, "low": 677.17, "close": 679.75}, {"time": "2025-12-15", "open": 683.72, "high": 683.74, "low": 677.25, "close": 678.72}, {"time": "2025-12-16", "open": 677.23, "high": 679.07, "low": 672.99, "close": 676.87}, {"time": "2025-12-17", "open": 677.89, "high": 678.44, "low": 669.22, "close": 669.42}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **SPY**
- Event date: **2025-12-10**
- As-of date (T-1): **2026-03-03**
- Freshness age: **83 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.0, Previous 4.0, Delta +0.0000)
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
