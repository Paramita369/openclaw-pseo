---
title: "FOMC Outcome (2024-04-30) for SPY: Up/Down Probability View"
description: "Historical probability profile for SPY around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "fomc_5"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-04-30"
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
freshness_days: 674
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.64
hub_baseline_median_t7: 0.63
hub_baseline_std_t7: 1.7817
hub_baseline_delta: 2.39
z_score_t7: 1.33
percentile_t7: 100.0
narrative_trigger: "extreme_outperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 0.9
  mdd_t7: -0.32
  volatility: 3.34
  impact_t1_pct: -0.32
  impact_t7_pct: 3.02
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 0.54
    mean: -0.06
    sample: 9
  t7:
    up: 77.78
    down: 22.22
    median: 0.63
    mean: 0.64
    sample: 9
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 9
    t1:
      up: 55.56
      down: 44.44
      median: 0.54
      mean: -0.06
      sample: 9
    t7:
      up: 77.78
      down: 22.22
      median: 0.63
      mean: 0.64
      sample: 9
related_events: [{"slug": "spy-after-fomc-2025-01-29", "title": "Fed Decision (2025-01-29) and SPY: Event-Driven Odds", "event_date": "2025-01-29", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 9.47, "median_t7_pct": 0.63, "sample_size": 9}, {"slug": "spy-after-fomc-2024-03-19", "title": "SPY After FOMC (2024-03-19): Historical Signal & Probability", "event_date": "2024-03-19", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 7.7, "median_t7_pct": 0.63, "sample_size": 9}, {"slug": "spy-after-fomc-2024-01-30", "title": "Fed Decision (2024-01-30) and SPY: Event-Driven Odds", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 2.69, "median_t7_pct": 0.63, "sample_size": 9}]
chartData: [{"time": "2024-04-29", "open": 499.33, "high": 499.98, "low": 496.55, "close": 499.3}, {"time": "2024-04-30", "open": 497.83, "high": 498.81, "low": 491.39, "close": 491.39}, {"time": "2024-05-01", "open": 490.8, "high": 497.47, "low": 489.33, "close": 489.8}, {"time": "2024-05-02", "open": 493.52, "high": 495.22, "low": 489.01, "close": 494.38}, {"time": "2024-05-03", "open": 500.38, "high": 501.74, "low": 497.83, "close": 500.51}, {"time": "2024-05-06", "open": 502.91, "high": 505.71, "low": 502.47, "close": 505.67}, {"time": "2024-05-07", "open": 506.64, "high": 507.63, "low": 505.56, "close": 506.23}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **SPY**
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
| T+1 | 55.56% | 44.44% | 0.54% | -0.06% | 9 |
| T+7 | 77.78% | 22.22% | 0.63% | 0.64% | 9 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.54% | -0.06% | 9 |
| T+7 | 77.78% | 22.22% | 0.63% | 0.64% | 9 |

## Historical Distribution Summary

When FOMC was **FLAT**, SPY T+1 up probability was **55.56%** (n=9).

When FOMC was **FLAT**, SPY T+7 up probability was **77.78%** (n=9).

Same-direction T+7 median return: **0.63%**.

For SPY, historical FOMC windows show all-history T+1 up probability of 55.56% and T+7 up probability of 77.78%. When FOMC printed Flat versus previous, T+1 up probability was 55.56% and T+7 up probability was 77.78% across 9 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
