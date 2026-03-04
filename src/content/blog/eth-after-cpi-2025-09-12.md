---
title: "2025-09-12 CPI Release: ETH Directional Probability Snapshot"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 4
title_template_key: "cpi_4"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-09-12"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -2.51
robust_score: -8.51
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 100
sample_size: 39
freshness_days: 172
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 324.245
event_previous: 323.291
event_delta: 0.954
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -10.0
  mdd_t7: -5.18
  volatility: 17.31
  impact_t1_pct: -1.0
  impact_t7_pct: -5.18
probabilities:
  sample_size: 39
  t1:
    up: 58.97
    down: 41.03
    median: 0.94
    mean: 0.55
    sample: 39
  t7:
    up: 43.59
    down: 56.41
    median: -1.18
    mean: 0.23
    sample: 39
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.96
      mean: 0.64
      sample: 38
    t7:
      up: 44.74
      down: 55.26
      median: -1.52
      mean: 0.24
      sample: 38
related_events: [{"slug": "eth-after-cpi-2025-07-15", "title": "ETH After CPI (2025-07-15): Historical T+1/T+7 Probability", "event_date": "2025-07-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 19.4, "sample_size": 0}, {"slug": "eth-after-cpi-2025-07-12", "title": "ETH After CPI (2025-07-12): Historical T+1/T+7 Probability", "event_date": "2025-07-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 22.17, "sample_size": 0}, {"slug": "eth-after-cpi-2025-04-10", "title": "ETH After CPI (2025-04-10): Historical T+1/T+7 Probability", "event_date": "2025-04-10", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.94, "sample_size": 0}]
chartData: [{"time": "2025-09-09", "open": 4308.28, "high": 4381.23, "low": 4277.85, "close": 4309.04}, {"time": "2025-09-10", "open": 4309.09, "high": 4450.42, "low": 4286.06, "close": 4349.15}, {"time": "2025-09-11", "open": 4349.2, "high": 4471.7, "low": 4339.72, "close": 4461.23}, {"time": "2025-09-12", "open": 4461.48, "high": 4734.27, "low": 4453.28, "close": 4715.25}, {"time": "2025-09-13", "open": 4714.7, "high": 4763.36, "low": 4609.13, "close": 4668.18}, {"time": "2025-09-14", "open": 4668.17, "high": 4690.64, "low": 4581.85, "close": 4609.6}, {"time": "2025-09-15", "open": 4609.72, "high": 4670.53, "low": 4469.86, "close": 4526.82}, {"time": "2025-09-16", "open": 4526.08, "high": 4537.6, "low": 4428.33, "close": 4503.56}, {"time": "2025-09-17", "open": 4503.64, "high": 4617.23, "low": 4429.64, "close": 4592.73}, {"time": "2025-09-18", "open": 4592.44, "high": 4643.97, "low": 4556.27, "close": 4589.92}, {"time": "2025-09-19", "open": 4589.51, "high": 4620.79, "low": 4443.26, "close": 4470.92}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2025-09-12**
- As-of date (T-1): **2026-03-03**
- Freshness age: **172 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 324.245, Previous 323.291, Delta +0.9540)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.94% | 0.55% | 39 |
| T+7 | 43.59% | 56.41% | -1.18% | 0.23% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.96% | 0.64% | 38 |
| T+7 | 44.74% | 55.26% | -1.52% | 0.24% | 38 |

## Historical Distribution Summary

When CPI was **UP**, ETH T+1 up probability was **60.53%** (n=38).

When CPI was **UP**, ETH T+7 up probability was **44.74%** (n=38).

Same-direction T+7 median return: **-1.52%**.

For ETH, historical CPI windows show all-history T+1 up probability of 58.97% and T+7 up probability of 43.59%. When CPI printed Up versus previous, T+1 up probability was 60.53% and T+7 up probability was 44.74% across 38 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
