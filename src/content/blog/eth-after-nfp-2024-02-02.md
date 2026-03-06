---
title: "2024-02-02 Nonfarm Payrolls: ETH Historical Win Rate"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-02-02"
asof_date: "2026-03-05"
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
quality_score: 100
sample_size: 34
freshness_days: 762
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:29+00:00"
event_direction: "up"
event_actual: 157238.0
event_previous: 157032.0
event_delta: 206.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: -0.52
  volatility: 84.63
  impact_t1_pct: -0.52
  impact_t7_pct: 7.78
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
related_events: [{"slug": "eth-after-nfp-2026-01-09", "title": "ETH After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 6.89, "sample_size": 0}, {"slug": "eth-after-nfp-2025-11-20", "title": "ETH After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 6.45, "sample_size": 0}, {"slug": "eth-after-nfp-2025-09-05", "title": "ETH After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 9.48, "sample_size": 0}]
chartData: [{"time": "2024-01-30", "open": 2317.44, "high": 2388.87, "low": 2298.28, "close": 2344.49}, {"time": "2024-01-31", "open": 2343.56, "high": 2349.61, "low": 2264.44, "close": 2282.54}, {"time": "2024-02-01", "open": 2282.18, "high": 2309.84, "low": 2243.57, "close": 2303.82}, {"time": "2024-02-02", "open": 2303.71, "high": 2323.05, "low": 2282.23, "close": 2308.04}, {"time": "2024-02-03", "open": 2307.98, "high": 2327.35, "low": 2293.54, "close": 2296.04}, {"time": "2024-02-04", "open": 2296.12, "high": 2309.01, "low": 2272.3, "close": 2289.55}, {"time": "2024-02-05", "open": 2289.21, "high": 2334.68, "low": 2270.07, "close": 2298.89}, {"time": "2024-02-06", "open": 2298.96, "high": 2389.83, "low": 2296.79, "close": 2372.2}, {"time": "2024-02-07", "open": 2372.26, "high": 2442.64, "low": 2353.71, "close": 2423.75}, {"time": "2024-02-08", "open": 2424.08, "high": 2459.56, "low": 2414.75, "close": 2419.91}, {"time": "2024-02-09", "open": 2419.77, "high": 2522.72, "low": 2419.36, "close": 2487.52}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2024-02-02**
- As-of date (T-1): **2026-03-05**
- Freshness age: **762 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157238.0, Previous 157032.0, Delta +206.0000)
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
