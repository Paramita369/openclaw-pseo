---
title: "FOMC Outcome (2024-12-19) for BTC: Up/Down Probability View"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 5
title_template_key: "fomc_5"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-12-19"
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
quality_score: 90
sample_size: 23
freshness_days: 439
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "down"
event_actual: 4.5
event_previous: 4.75
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -7.16
  mdd_t7: -2.71
  volatility: 29.13
  impact_t1_pct: 0.27
  impact_t7_pct: -1.74
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
related_events: [{"slug": "btc-after-fomc-2025-05-07", "title": "BTC After FOMC (2025-05-07): Historical T+1/T+7 Probability", "event_date": "2025-05-07", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 6.71, "sample_size": 0}, {"slug": "btc-after-fomc-2024-11-08", "title": "BTC After FOMC (2024-11-08): Historical T+1/T+7 Probability", "event_date": "2024-11-08", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 18.97, "sample_size": 0}, {"slug": "btc-after-fomc-2024-11-06", "title": "BTC After FOMC (2024-11-06): Historical T+1/T+7 Probability", "event_date": "2024-11-06", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 19.76, "sample_size": 0}]
chartData: [{"time": "2024-12-16", "open": 104293.58, "high": 107780.58, "low": 103322.98, "close": 106029.72}, {"time": "2024-12-17", "open": 106030.69, "high": 108268.45, "low": 105291.73, "close": 106140.6}, {"time": "2024-12-18", "open": 106147.3, "high": 106470.61, "low": 100041.54, "close": 100041.54}, {"time": "2024-12-19", "open": 100070.69, "high": 102748.15, "low": 95587.68, "close": 97490.95}, {"time": "2024-12-20", "open": 97484.7, "high": 98098.91, "low": 92175.18, "close": 97755.93}, {"time": "2024-12-21", "open": 97756.2, "high": 99507.1, "low": 96426.52, "close": 97224.73}, {"time": "2024-12-22", "open": 97218.32, "high": 97360.27, "low": 94202.19, "close": 95104.94}, {"time": "2024-12-23", "open": 95099.39, "high": 96416.21, "low": 92403.13, "close": 94686.24}, {"time": "2024-12-24", "open": 94684.34, "high": 99404.06, "low": 93448.02, "close": 98676.09}, {"time": "2024-12-25", "open": 98675.91, "high": 99478.75, "low": 97593.47, "close": 99299.2}, {"time": "2024-12-26", "open": 99297.7, "high": 99884.57, "low": 95137.88, "close": 95795.52}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2024-12-19**
- As-of date (T-1): **2026-03-03**
- Freshness age: **439 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 4.5, Previous 4.75, Delta -0.2500)
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
