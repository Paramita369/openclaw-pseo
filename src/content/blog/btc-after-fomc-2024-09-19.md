---
title: "Historical Performance of BTC After FOMC (2024-09-19)"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-09-19"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -4.61
robust_score: -10.61
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 23
freshness_days: 530
freshness_status: "stale"
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 5.0
event_previous: 5.5
event_delta: -0.5
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 1.13
  mdd_t7: 0.0
  volatility: 3.16
  impact_t1_pct: 0.4
  impact_t7_pct: 3.56
probabilities:
  sample_size: 23
  t1:
    up: 52.17
    down: 47.83
    median: 0.27
    mean: -0.18
    sample: 23
  t7:
    up: 43.48
    down: 56.52
    median: -2.38
    mean: -0.7
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 6
    t1:
      up: 66.67
      down: 33.33
      median: 0.29
      mean: -0.25
      sample: 6
    t7:
      up: 33.33
      down: 66.67
      median: -4.1
      mean: -0.03
      sample: 6
related_events: [{"slug": "btc-after-fomc-2024-04-30", "title": "BTC After FOMC (2024-04-30): Historical T+1/T+7 Probability", "event_date": "2024-04-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 5.37, "median_t7_pct": 2.8, "sample_size": 0}, {"slug": "btc-after-fomc-2024-01-30", "title": "BTC After FOMC (2024-01-30): Historical T+1/T+7 Probability", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.97, "median_t7_pct": 0.31, "sample_size": 0}, {"slug": "btc-after-fomc-2026-01-28", "title": "BTC After FOMC (2026-01-28): Historical T+1/T+7 Probability", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -18.13, "sample_size": 0}]
chartData: [{"time": "2024-09-16", "open": 59185.23, "high": 59205.51, "low": 57501.34, "close": 58192.51}, {"time": "2024-09-17", "open": 58192.51, "high": 61316.09, "low": 57628.07, "close": 60308.54}, {"time": "2024-09-18", "open": 60309.0, "high": 61664.07, "low": 59218.25, "close": 61649.68}, {"time": "2024-09-19", "open": 61651.16, "high": 63872.44, "low": 61609.87, "close": 62940.46}, {"time": "2024-09-20", "open": 62941.43, "high": 64119.53, "low": 62364.61, "close": 63192.98}, {"time": "2024-09-21", "open": 63184.34, "high": 63543.36, "low": 62783.11, "close": 63394.84}, {"time": "2024-09-22", "open": 63396.8, "high": 63993.42, "low": 62440.73, "close": 63648.71}, {"time": "2024-09-23", "open": 63643.1, "high": 64733.56, "low": 62628.08, "close": 63329.8}, {"time": "2024-09-24", "open": 63326.84, "high": 64695.21, "low": 62737.42, "close": 64301.97}, {"time": "2024-09-25", "open": 64302.59, "high": 64804.5, "low": 62945.38, "close": 63143.14}, {"time": "2024-09-26", "open": 63138.55, "high": 65790.8, "low": 62669.27, "close": 65181.02}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2024-09-19**
- As-of date (T-1): **2026-03-03**
- Freshness age: **530 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 5.0, Previous 5.5, Delta -0.5000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 52.17% | 47.83% | 0.27% | -0.18% | 23 |
| T+7 | 43.48% | 56.52% | -2.38% | -0.7% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 66.67% | 33.33% | 0.29% | -0.25% | 6 |
| T+7 | 33.33% | 66.67% | -4.1% | -0.03% | 6 |

## Historical Distribution Summary

When FOMC was **DOWN**, BTC T+1 up probability was **66.67%** (n=6).

When FOMC was **DOWN**, BTC T+7 up probability was **33.33%** (n=6).

Same-direction T+7 median return: **-4.1%**.

For BTC, historical FOMC windows show all-history T+1 up probability of 52.17% and T+7 up probability of 43.48%. When FOMC printed Down versus previous, T+1 up probability was 66.67% and T+7 up probability was 33.33% across 6 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
