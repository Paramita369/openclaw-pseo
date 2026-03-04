---
title: "US CPI (2024-12-11) and ETH: Event-Driven Return Odds"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2024-12-11"
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
freshness_days: 447
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 317.604
event_previous: 316.528
event_delta: 1.076
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -10.0
  mdd_t7: -6.81
  volatility: 77.55
  impact_t1_pct: 1.31
  impact_t7_pct: -5.58
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
chartData: [{"time": "2024-12-08", "open": 4007.69, "high": 4018.0, "low": 3927.85, "close": 4005.7}, {"time": "2024-12-09", "open": 4006.1, "high": 4008.78, "low": 3525.23, "close": 3718.69}, {"time": "2024-12-10", "open": 3719.0, "high": 3780.75, "low": 3520.37, "close": 3631.83}, {"time": "2024-12-11", "open": 3631.28, "high": 3850.77, "low": 3567.57, "close": 3832.82}, {"time": "2024-12-12", "open": 3833.17, "high": 3987.01, "low": 3800.09, "close": 3883.1}, {"time": "2024-12-13", "open": 3883.03, "high": 3967.4, "low": 3855.02, "close": 3911.21}, {"time": "2024-12-14", "open": 3910.85, "high": 3943.28, "low": 3826.76, "close": 3868.41}, {"time": "2024-12-15", "open": 3868.44, "high": 3971.5, "low": 3832.1, "close": 3951.94}, {"time": "2024-12-16", "open": 3951.65, "high": 4106.96, "low": 3882.71, "close": 3987.48}, {"time": "2024-12-17", "open": 3987.33, "high": 4040.34, "low": 3849.29, "close": 3886.77}, {"time": "2024-12-18", "open": 3886.89, "high": 3902.72, "low": 3617.84, "close": 3618.79}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2024-12-11**
- As-of date (T-1): **2026-03-03**
- Freshness age: **447 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 317.604, Previous 316.528, Delta +1.0760)
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
