---
title: "Historical Performance of SPY After FOMC (2024-11-08)"
description: "Historical probability profile for SPY around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-11-08"
asof_date: "2026-03-03"
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
quality_score: 80
sample_size: 23
freshness_days: 480
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 4.75
event_previous: 5.0
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -0.96
  mdd_t7: -2.08
  volatility: 2.17
  impact_t1_pct: 0.1
  impact_t7_pct: -2.08
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
    direction: "down"
    sample_size: 6
    t1:
      up: 66.67
      down: 33.33
      median: 0.21
      mean: 0.15
      sample: 6
    t7:
      up: 33.33
      down: 66.67
      median: -0.88
      mean: -0.37
      sample: 6
related_events: [{"slug": "spy-after-fomc-2025-01-29", "title": "SPY After FOMC (2025-01-29): Historical T+1/T+7 Probability", "event_date": "2025-01-29", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 9.47, "median_t7_pct": 0.4, "sample_size": 0}, {"slug": "spy-after-fomc-2024-03-19", "title": "SPY After FOMC (2024-03-19): Historical T+1/T+7 Probability", "event_date": "2024-03-19", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 7.7, "median_t7_pct": 0.6, "sample_size": 0}, {"slug": "spy-after-fomc-2024-01-30", "title": "SPY After FOMC (2024-01-30): Historical T+1/T+7 Probability", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.69, "median_t7_pct": 0.63, "sample_size": 0}]
chartData: [{"time": "2024-11-05", "open": 562.22, "high": 568.13, "low": 562.01, "close": 568.09}, {"time": "2024-11-06", "open": 580.41, "high": 583.1, "low": 576.65, "close": 582.22}, {"time": "2024-11-07", "open": 584.23, "high": 587.75, "low": 584.15, "close": 586.72}, {"time": "2024-11-08", "open": 587.27, "high": 590.69, "low": 587.27, "close": 589.26}, {"time": "2024-11-11", "open": 590.86, "high": 591.21, "low": 588.09, "close": 589.83}, {"time": "2024-11-12", "open": 589.75, "high": 590.35, "low": 585.5, "close": 587.99}, {"time": "2024-11-13", "open": 588.46, "high": 590.29, "low": 586.08, "close": 588.28}, {"time": "2024-11-14", "open": 588.41, "high": 588.89, "low": 583.81, "close": 584.5}, {"time": "2024-11-15", "open": 580.92, "high": 581.39, "low": 575.15, "close": 577.01}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **SPY**
- Event date: **2024-11-08**
- As-of date (T-1): **2026-03-03**
- Freshness age: **480 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 4.75, Previous 5.0, Delta -0.2500)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 52.17% | 47.83% | 0.1% | -0.02% | 23 |
| T+7 | 56.52% | 43.48% | 0.54% | 0.26% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 66.67% | 33.33% | 0.21% | 0.15% | 6 |
| T+7 | 33.33% | 66.67% | -0.88% | -0.37% | 6 |

## Historical Distribution Summary

When FOMC was **DOWN**, SPY T+1 up probability was **66.67%** (n=6).

When FOMC was **DOWN**, SPY T+7 up probability was **33.33%** (n=6).

Same-direction T+7 median return: **-0.88%**.

For SPY, historical FOMC windows show all-history T+1 up probability of 52.17% and T+7 up probability of 56.52%. When FOMC printed Down versus previous, T+1 up probability was 66.67% and T+7 up probability was 33.33% across 6 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
