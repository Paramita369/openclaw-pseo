---
title: "Historical Performance of SPY After CPI (2024-11-13)"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-11-13"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 15.44
robust_score: 9.44
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 39
freshness_days: 475
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 316.528
event_previous: 315.631
event_delta: 0.897
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -2.33
  mdd_t7: -1.12
  volatility: 0.48
  impact_t1_pct: -0.64
  impact_t7_pct: -1.12
probabilities:
  sample_size: 39
  t1:
    up: 64.1
    down: 35.9
    median: 0.16
    mean: 0.21
    sample: 39
  t7:
    up: 68.42
    down: 31.58
    median: 0.51
    mean: 0.21
    sample: 38
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 63.16
      down: 36.84
      median: 0.14
      mean: 0.21
      sample: 38
    t7:
      up: 68.42
      down: 31.58
      median: 0.51
      mean: 0.21
      sample: 38
related_events: [{"slug": "spy-after-cpi-2024-03-12", "title": "SPY After CPI (2024-03-12): Historical T+1/T+7 Probability", "event_date": "2024-03-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 3.94, "median_t7_pct": 0.1, "sample_size": 0}, {"slug": "spy-after-cpi-2024-11-14", "title": "SPY After CPI (2024-11-14): Historical T+1/T+7 Probability", "event_date": "2024-11-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.43, "median_t7_pct": 0.05, "sample_size": 0}, {"slug": "spy-after-cpi-2024-05-15", "title": "SPY After CPI (2024-05-15): Historical T+1/T+7 Probability", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.37, "median_t7_pct": 0.01, "sample_size": 0}]
chartData: [{"time": "2024-11-11", "open": 590.86, "high": 591.21, "low": 588.09, "close": 589.83}, {"time": "2024-11-12", "open": 589.75, "high": 590.35, "low": 585.5, "close": 587.99}, {"time": "2024-11-13", "open": 588.46, "high": 590.29, "low": 586.08, "close": 588.28}, {"time": "2024-11-14", "open": 588.41, "high": 588.89, "low": 583.81, "close": 584.5}, {"time": "2024-11-15", "open": 580.92, "high": 581.39, "low": 575.15, "close": 577.01}, {"time": "2024-11-18", "open": 577.47, "high": 580.69, "low": 576.61, "close": 579.37}, {"time": "2024-11-19", "open": 575.98, "high": 582.22, "low": 575.31, "close": 581.49}, {"time": "2024-11-20", "open": 581.57, "high": 581.97, "low": 575.91, "close": 581.69}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2024-11-13**
- As-of date (T-1): **2026-03-03**
- Freshness age: **475 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 316.528, Previous 315.631, Delta +0.8970)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 64.1% | 35.9% | 0.16% | 0.21% | 39 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 63.16% | 36.84% | 0.14% | 0.21% | 38 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Historical Distribution Summary

When CPI was **UP**, SPY T+1 up probability was **63.16%** (n=38).

When CPI was **UP**, SPY T+7 up probability was **68.42%** (n=38).

Same-direction T+7 median return: **0.51%**.

For SPY, historical CPI windows show all-history T+1 up probability of 64.1% and T+7 up probability of 68.42%. When CPI printed Up versus previous, T+1 up probability was 63.16% and T+7 up probability was 68.42% across 38 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
