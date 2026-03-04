---
title: "Historical Performance of ETH After NFP (2024-03-01)"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-03-01"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 4.94
robust_score: -1.06
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 34
freshness_days: 732
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 157466.0
event_previous: 157238.0
event_delta: 228.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.97
  mdd_t7: -0.38
  volatility: 13.68
  impact_t1_pct: -0.38
  impact_t7_pct: 13.3
probabilities:
  sample_size: 34
  t1:
    up: 50.0
    down: 50.0
    median: 0.0
    mean: -0.15
    sample: 34
  t7:
    up: 55.88
    down: 44.12
    median: 1.44
    mean: 2.65
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 30
    t1:
      up: 50.0
      down: 50.0
      median: 0.0
      mean: -0.14
      sample: 30
    t7:
      up: 53.33
      down: 46.67
      median: 0.79
      mean: 2.65
      sample: 30
related_events: [{"slug": "eth-after-nfp-2026-02-11", "title": "ETH After NFP (2026-02-11): Historical T+1/T+7 Probability", "event_date": "2026-02-11", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.69, "sample_size": 0}, {"slug": "eth-after-nfp-2026-02-06", "title": "ETH After NFP (2026-02-06): Historical T+1/T+7 Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.72, "sample_size": 0}, {"slug": "eth-after-nfp-2026-01-09", "title": "ETH After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 6.89, "sample_size": 0}]
chartData: [{"time": "2024-02-27", "open": 3178.41, "high": 3287.96, "low": 3167.83, "close": 3244.52}, {"time": "2024-02-28", "open": 3243.89, "high": 3485.45, "low": 3201.58, "close": 3385.7}, {"time": "2024-02-29", "open": 3386.8, "high": 3518.97, "low": 3303.91, "close": 3341.92}, {"time": "2024-03-01", "open": 3341.97, "high": 3452.63, "low": 3341.85, "close": 3435.05}, {"time": "2024-03-02", "open": 3436.16, "high": 3459.75, "low": 3398.9, "close": 3422.05}, {"time": "2024-03-03", "open": 3422.88, "high": 3491.17, "low": 3372.21, "close": 3490.99}, {"time": "2024-03-04", "open": 3489.34, "high": 3641.46, "low": 3446.02, "close": 3630.43}, {"time": "2024-03-05", "open": 3631.93, "high": 3828.16, "low": 3224.12, "close": 3554.96}, {"time": "2024-03-06", "open": 3554.07, "high": 3901.43, "low": 3502.8, "close": 3819.23}, {"time": "2024-03-07", "open": 3818.31, "high": 3939.59, "low": 3738.69, "close": 3874.35}, {"time": "2024-03-08", "open": 3874.83, "high": 3998.83, "low": 3828.36, "close": 3892.06}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2024-03-01**
- As-of date (T-1): **2026-03-03**
- Freshness age: **732 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157466.0, Previous 157238.0, Delta +228.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.15% | 34 |
| T+7 | 55.88% | 44.12% | 1.44% | 2.65% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.14% | 30 |
| T+7 | 53.33% | 46.67% | 0.79% | 2.65% | 30 |

## Historical Distribution Summary

When NFP was **UP**, ETH T+1 up probability was **50.0%** (n=30).

When NFP was **UP**, ETH T+7 up probability was **53.33%** (n=30).

Same-direction T+7 median return: **0.79%**.

For ETH, historical NFP windows show all-history T+1 up probability of 50.0% and T+7 up probability of 55.88%. When NFP printed Up versus previous, T+1 up probability was 50.0% and T+7 up probability was 53.33% across 30 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
