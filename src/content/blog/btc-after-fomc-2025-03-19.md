---
title: "2025-03-19 FOMC Meeting: BTC T+1/T+7 Probability Profile"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 3
title_template_key: "fomc_3"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-03-19"
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
quality_score: 100
sample_size: 23
freshness_days: 349
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/btc/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "flat"
event_actual: 4.5
event_previous: 4.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 0.39
  mdd_t7: -3.48
  volatility: 53.03
  impact_t1_pct: -3.09
  impact_t7_pct: 0.05
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
chartData: [{"time": "2025-03-16", "open": 84333.32, "high": 85051.6, "low": 82017.91, "close": 82579.69}, {"time": "2025-03-17", "open": 82576.34, "high": 84725.33, "low": 82492.16, "close": 84075.69}, {"time": "2025-03-18", "open": 84075.72, "high": 84075.72, "low": 81179.99, "close": 82718.5}, {"time": "2025-03-19", "open": 82718.8, "high": 87021.19, "low": 82569.73, "close": 86854.23}, {"time": "2025-03-20", "open": 86872.95, "high": 87443.27, "low": 83647.2, "close": 84167.2}, {"time": "2025-03-21", "open": 84164.54, "high": 84782.27, "low": 83171.07, "close": 84043.24}, {"time": "2025-03-22", "open": 84046.26, "high": 84513.88, "low": 83674.78, "close": 83832.48}, {"time": "2025-03-23", "open": 83831.9, "high": 86094.78, "low": 83794.91, "close": 86054.38}, {"time": "2025-03-24", "open": 86070.93, "high": 88758.73, "low": 85541.2, "close": 87498.91}, {"time": "2025-03-25", "open": 87512.82, "high": 88542.4, "low": 86346.08, "close": 87471.7}, {"time": "2025-03-26", "open": 87460.23, "high": 88292.16, "low": 85861.45, "close": 86900.88}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2025-03-19**
- As-of date (T-1): **2026-03-03**
- Freshness age: **349 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.5, Previous 4.5, Delta +0.0000)
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
