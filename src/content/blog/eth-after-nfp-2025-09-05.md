---
title: "Historical Performance of ETH After NFP (2025-09-05)"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-09-05"
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
freshness_days: 179
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158548.0
event_previous: 158472.0
event_delta: 76.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.93
  mdd_t7: -0.76
  volatility: 10.24
  impact_t1_pct: -0.76
  impact_t7_pct: 9.48
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
chartData: [{"time": "2025-09-02", "open": 4314.39, "high": 4414.93, "low": 4260.46, "close": 4325.37}, {"time": "2025-09-03", "open": 4324.7, "high": 4489.2, "low": 4286.21, "close": 4450.39}, {"time": "2025-09-04", "open": 4450.22, "high": 4483.45, "low": 4268.59, "close": 4298.74}, {"time": "2025-09-05", "open": 4298.84, "high": 4484.36, "low": 4258.05, "close": 4306.99}, {"time": "2025-09-06", "open": 4306.97, "high": 4327.44, "low": 4244.75, "close": 4274.24}, {"time": "2025-09-07", "open": 4274.17, "high": 4334.27, "low": 4271.53, "close": 4305.35}, {"time": "2025-09-08", "open": 4305.38, "high": 4381.27, "low": 4279.97, "close": 4308.07}, {"time": "2025-09-09", "open": 4308.28, "high": 4381.23, "low": 4277.85, "close": 4309.04}, {"time": "2025-09-10", "open": 4309.09, "high": 4450.42, "low": 4286.06, "close": 4349.15}, {"time": "2025-09-11", "open": 4349.2, "high": 4471.7, "low": 4339.72, "close": 4461.23}, {"time": "2025-09-12", "open": 4461.48, "high": 4734.27, "low": 4453.28, "close": 4715.25}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2025-09-05**
- As-of date (T-1): **2026-03-03**
- Freshness age: **179 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158548.0, Previous 158472.0, Delta +76.0000)
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
