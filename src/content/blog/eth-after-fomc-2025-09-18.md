---
title: "ETH Post-FOMC Reaction (2025-09-18): Quant Backtest Snapshot"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 4
title_template_key: "fomc_4"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-09-18"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Bearish"
raw_signal_score: -13.74
robust_score: -19.74
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 23
freshness_days: 166
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "down"
event_actual: 4.25
event_previous: 4.5
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -10.0
  mdd_t7: -15.72
  volatility: 105.65
  impact_t1_pct: -2.59
  impact_t7_pct: -15.72
probabilities:
  sample_size: 23
  t1:
    up: 43.48
    down: 56.52
    median: -0.1
    mean: 0.91
    sample: 23
  t7:
    up: 30.43
    down: 69.57
    median: -3.26
    mean: -2.8
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 6
    t1:
      up: 66.67
      down: 33.33
      median: 1.36
      mean: 0.84
      sample: 6
    t7:
      up: 33.33
      down: 66.67
      median: -7.6
      mean: -5.39
      sample: 6
related_events: [{"slug": "eth-after-fomc-2025-05-07", "title": "ETH After FOMC (2025-05-07): Historical T+1/T+7 Probability", "event_date": "2025-05-07", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 44.07, "sample_size": 0}, {"slug": "eth-after-fomc-2024-11-06", "title": "ETH After FOMC (2024-11-06): Historical T+1/T+7 Probability", "event_date": "2024-11-06", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 17.2, "sample_size": 0}, {"slug": "eth-after-fomc-2024-09-19", "title": "ETH After FOMC (2024-09-19): Historical T+1/T+7 Probability", "event_date": "2024-09-19", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 6.79, "sample_size": 0}]
chartData: [{"time": "2025-09-15", "open": 4609.72, "high": 4670.53, "low": 4469.86, "close": 4526.82}, {"time": "2025-09-16", "open": 4526.08, "high": 4537.6, "low": 4428.33, "close": 4503.56}, {"time": "2025-09-17", "open": 4503.64, "high": 4617.23, "low": 4429.64, "close": 4592.73}, {"time": "2025-09-18", "open": 4592.44, "high": 4643.97, "low": 4556.27, "close": 4589.92}, {"time": "2025-09-19", "open": 4589.51, "high": 4620.79, "low": 4443.26, "close": 4470.92}, {"time": "2025-09-20", "open": 4470.98, "high": 4509.81, "low": 4459.16, "close": 4482.27}, {"time": "2025-09-21", "open": 4482.58, "high": 4499.39, "low": 4447.12, "close": 4451.33}, {"time": "2025-09-22", "open": 4451.58, "high": 4457.08, "low": 4092.4, "close": 4202.88}, {"time": "2025-09-23", "open": 4203.02, "high": 4227.73, "low": 4120.82, "close": 4165.5}, {"time": "2025-09-24", "open": 4165.41, "high": 4206.9, "low": 4081.35, "close": 4153.47}, {"time": "2025-09-25", "open": 4153.52, "high": 4162.06, "low": 3829.01, "close": 3868.33}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2025-09-18**
- As-of date (T-1): **2026-03-03**
- Freshness age: **166 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 4.25, Previous 4.5, Delta -0.2500)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 43.48% | 56.52% | -0.1% | 0.91% | 23 |
| T+7 | 30.43% | 69.57% | -3.26% | -2.8% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 66.67% | 33.33% | 1.36% | 0.84% | 6 |
| T+7 | 33.33% | 66.67% | -7.6% | -5.39% | 6 |

## Historical Distribution Summary

When FOMC was **DOWN**, ETH T+1 up probability was **66.67%** (n=6).

When FOMC was **DOWN**, ETH T+7 up probability was **33.33%** (n=6).

Same-direction T+7 median return: **-7.6%**.

For ETH, historical FOMC windows show all-history T+1 up probability of 43.48% and T+7 up probability of 30.43%. When FOMC printed Down versus previous, T+1 up probability was 66.67% and T+7 up probability was 33.33% across 6 matched cases. Current classification is Bearish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
