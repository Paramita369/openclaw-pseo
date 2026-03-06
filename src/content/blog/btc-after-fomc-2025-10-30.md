---
title: "FOMC Outcome (2025-10-30) for BTC: Up/Down Probability View"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "fomc_5"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-10-30"
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
quality_score: 90
sample_size: 23
freshness_days: 126
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 4.0
event_previous: 4.25
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -8.94
  mdd_t7: -8.44
  volatility: 85.68
  impact_t1_pct: 1.15
  impact_t7_pct: -6.47
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
chartData: [{"time": "2025-10-27", "open": 114479.85, "high": 116273.31, "low": 113882.29, "close": 114119.33}, {"time": "2025-10-28", "open": 114129.09, "high": 116078.98, "low": 112291.68, "close": 112956.16}, {"time": "2025-10-29", "open": 112921.33, "high": 113642.73, "low": 109368.72, "close": 110055.3}, {"time": "2025-10-30", "open": 110059.2, "high": 111612.35, "low": 106376.69, "close": 108305.55}, {"time": "2025-10-31", "open": 108304.41, "high": 111031.82, "low": 108288.27, "close": 109556.16}, {"time": "2025-11-01", "open": 109558.62, "high": 110574.9, "low": 109372.95, "close": 110064.02}, {"time": "2025-11-02", "open": 110064.43, "high": 111167.31, "low": 109523.45, "close": 110639.62}, {"time": "2025-11-03", "open": 110646.91, "high": 110764.91, "low": 105336.36, "close": 106547.52}, {"time": "2025-11-04", "open": 106541.42, "high": 107264.88, "low": 98962.06, "close": 101590.52}, {"time": "2025-11-05", "open": 101579.23, "high": 104534.7, "low": 98989.91, "close": 103891.84}, {"time": "2025-11-06", "open": 103893.66, "high": 104147.3, "low": 100336.87, "close": 101301.29}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2025-10-30**
- As-of date (T-1): **2026-03-05**
- Freshness age: **126 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 4.0, Previous 4.25, Delta -0.2500)
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
