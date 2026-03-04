---
title: "FOMC Outcome (2025-09-18) for BTC: Up/Down Probability View"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 5
title_template_key: "fomc_5"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-09-18"
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
freshness_days: 166
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "down"
event_actual: 4.25
event_previous: 4.5
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -10.0
  mdd_t7: -6.9
  volatility: 42.4
  impact_t1_pct: -1.24
  impact_t7_pct: -6.9
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
chartData: [{"time": "2025-09-15", "open": 115399.63, "high": 116747.88, "low": 114461.06, "close": 115444.88}, {"time": "2025-09-16", "open": 115423.76, "high": 117005.27, "low": 114813.09, "close": 116843.19}, {"time": "2025-09-17", "open": 116840.51, "high": 117328.61, "low": 114794.98, "close": 116468.51}, {"time": "2025-09-18", "open": 116461.27, "high": 117911.79, "low": 116188.8, "close": 117137.2}, {"time": "2025-09-19", "open": 117137.67, "high": 117479.76, "low": 115141.82, "close": 115688.86}, {"time": "2025-09-20", "open": 115691.12, "high": 116191.15, "low": 115473.52, "close": 115721.96}, {"time": "2025-09-21", "open": 115730.23, "high": 115901.09, "low": 115252.58, "close": 115306.09}, {"time": "2025-09-22", "open": 115309.22, "high": 115431.31, "low": 112037.65, "close": 112748.51}, {"time": "2025-09-23", "open": 112757.48, "high": 113351.91, "low": 111535.57, "close": 112014.5}, {"time": "2025-09-24", "open": 112007.66, "high": 113986.27, "low": 111229.64, "close": 113328.63}, {"time": "2025-09-25", "open": 113330.16, "high": 113541.09, "low": 108713.4, "close": 109049.29}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
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
