---
title: "Fed Decision (2025-10-30) and ETH: Event-Driven Odds"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-10-30"
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
freshness_days: 124
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "down"
event_actual: 4.0
event_previous: 4.25
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -10.0
  mdd_t7: -15.31
  volatility: 150.49
  impact_t1_pct: 1.12
  impact_t7_pct: -12.94
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
chartData: [{"time": "2025-10-27", "open": 4158.01, "high": 4250.67, "low": 4099.57, "close": 4120.12}, {"time": "2025-10-28", "open": 4120.27, "high": 4173.51, "low": 3940.83, "close": 3982.26}, {"time": "2025-10-29", "open": 3980.76, "high": 4036.35, "low": 3849.54, "close": 3903.35}, {"time": "2025-10-30", "open": 3903.32, "high": 3948.22, "low": 3681.91, "close": 3804.38}, {"time": "2025-10-31", "open": 3805.08, "high": 3900.58, "low": 3797.67, "close": 3847.08}, {"time": "2025-11-01", "open": 3847.17, "high": 3906.78, "low": 3832.63, "close": 3874.19}, {"time": "2025-11-02", "open": 3873.89, "high": 3914.88, "low": 3840.0, "close": 3911.06}, {"time": "2025-11-03", "open": 3911.75, "high": 3912.63, "low": 3560.26, "close": 3602.31}, {"time": "2025-11-04", "open": 3602.04, "high": 3652.69, "low": 3063.09, "close": 3292.57}, {"time": "2025-11-05", "open": 3292.15, "high": 3479.81, "low": 3170.51, "close": 3425.17}, {"time": "2025-11-06", "open": 3425.36, "high": 3454.34, "low": 3245.28, "close": 3312.26}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2025-10-30**
- As-of date (T-1): **2026-03-03**
- Freshness age: **124 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 4.0, Previous 4.25, Delta -0.2500)
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
