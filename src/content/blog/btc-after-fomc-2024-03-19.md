---
title: "BTC Post-FOMC Reaction (2024-03-19): Quant Backtest Snapshot"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 4
title_template_key: "fomc_4"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-03-19"
asof_date: "2026-03-05"
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
quality_score: 100
sample_size: 23
freshness_days: 716
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:50+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 63.41
  impact_t1_pct: 9.69
  impact_t7_pct: 13.04
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
    direction: "flat"
    sample_size: 17
    t1:
      up: 47.06
      down: 52.94
      median: -0.19
      mean: -0.15
      sample: 17
    t7:
      up: 47.06
      down: 52.94
      median: -2.38
      mean: -0.94
      sample: 17
related_events: [{"slug": "btc-after-fomc-2025-05-07", "title": "BTC After FOMC (2025-05-07): Historical T+1/T+7 Probability", "event_date": "2025-05-07", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 6.71, "sample_size": 0}, {"slug": "btc-after-fomc-2024-11-08", "title": "BTC After FOMC (2024-11-08): Historical T+1/T+7 Probability", "event_date": "2024-11-08", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 18.97, "sample_size": 0}, {"slug": "btc-after-fomc-2024-11-06", "title": "BTC After FOMC (2024-11-06): Historical T+1/T+7 Probability", "event_date": "2024-11-06", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 19.76, "sample_size": 0}]
chartData: [{"time": "2024-03-16", "open": 69392.48, "high": 70046.27, "low": 64801.39, "close": 65315.12}, {"time": "2024-03-17", "open": 65316.34, "high": 68845.72, "low": 64545.32, "close": 68390.62}, {"time": "2024-03-18", "open": 68371.3, "high": 68897.13, "low": 66594.23, "close": 67548.59}, {"time": "2024-03-19", "open": 67556.13, "high": 68106.93, "low": 61536.18, "close": 61912.77}, {"time": "2024-03-20", "open": 61930.16, "high": 68115.26, "low": 60807.79, "close": 67913.67}, {"time": "2024-03-21", "open": 67911.59, "high": 68199.99, "low": 64580.92, "close": 65491.39}, {"time": "2024-03-22", "open": 65489.93, "high": 66623.75, "low": 62355.37, "close": 63778.76}, {"time": "2024-03-23", "open": 63802.72, "high": 65976.4, "low": 63038.49, "close": 64062.2}, {"time": "2024-03-24", "open": 64070.75, "high": 67622.76, "low": 63825.85, "close": 67234.17}, {"time": "2024-03-25", "open": 67234.09, "high": 71162.59, "low": 66414.84, "close": 69958.81}, {"time": "2024-03-26", "open": 69931.33, "high": 71535.74, "low": 69335.61, "close": 69987.84}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2024-03-19**
- As-of date (T-1): **2026-03-05**
- Freshness age: **716 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.5, Previous 5.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 52.17% | 47.83% | 0.27% | -0.18% | 23 |
| T+7 | 43.48% | 56.52% | -2.38% | -0.7% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 47.06% | 52.94% | -0.19% | -0.15% | 17 |
| T+7 | 47.06% | 52.94% | -2.38% | -0.94% | 17 |

## Historical Distribution Summary

When FOMC was **FLAT**, BTC T+1 up probability was **47.06%** (n=17).

When FOMC was **FLAT**, BTC T+7 up probability was **47.06%** (n=17).

Same-direction T+7 median return: **-2.38%**.

For BTC, historical FOMC windows show all-history T+1 up probability of 52.17% and T+7 up probability of 43.48%. When FOMC printed Flat versus previous, T+1 up probability was 47.06% and T+7 up probability was 47.06% across 17 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
