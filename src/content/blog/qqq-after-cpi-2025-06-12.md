---
title: "QQQ CPI Win Rate (2025-06-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-06-12"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 8.09
robust_score: 2.09
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 100
sample_size: 39
freshness_days: 264
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/cpi"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 321.435
event_previous: 320.62
event_delta: 0.815
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -5.2
  mdd_t7: -1.4
  volatility: 20.35
  impact_t1_pct: -1.26
  impact_t7_pct: -1.28
probabilities:
  sample_size: 39
  t1:
    up: 61.54
    down: 38.46
    median: 0.21
    mean: 0.23
    sample: 39
  t7:
    up: 55.26
    down: 44.74
    median: 0.58
    mean: 0.2
    sample: 38
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.19
      mean: 0.23
      sample: 38
    t7:
      up: 55.26
      down: 44.74
      median: 0.58
      mean: 0.2
      sample: 38
related_events: [{"slug": "qqq-after-cpi-2026-02-12", "title": "QQQ After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 0.47, "sample_size": 0}, {"slug": "qqq-after-cpi-2025-12-18", "title": "QQQ After CPI (2025-12-18): Historical T+1/T+7 Probability", "event_date": "2025-12-18", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.56, "sample_size": 0}, {"slug": "qqq-after-cpi-2025-10-24", "title": "QQQ After CPI (2025-10-24): Historical T+1/T+7 Probability", "event_date": "2025-10-24", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.94, "sample_size": 0}]
chartData: [{"time": "2025-06-09", "open": 528.25, "high": 530.45, "low": 527.13, "close": 528.81}, {"time": "2025-06-10", "open": 529.28, "high": 532.99, "low": 527.01, "close": 532.31}, {"time": "2025-06-11", "open": 533.71, "high": 534.87, "low": 528.22, "close": 530.51}, {"time": "2025-06-12", "open": 529.2, "high": 532.74, "low": 528.95, "close": 531.76}, {"time": "2025-06-13", "open": 525.8, "high": 529.98, "low": 523.86, "close": 525.08}, {"time": "2025-06-16", "open": 528.61, "high": 533.46, "low": 528.56, "close": 532.39}, {"time": "2025-06-17", "open": 529.82, "high": 531.43, "low": 526.03, "close": 527.2}, {"time": "2025-06-18", "open": 528.21, "high": 530.65, "low": 525.52, "close": 527.11}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2025-06-12**
- As-of date (T-1): **2026-03-03**
- Freshness age: **264 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 321.435, Previous 320.62, Delta +0.8150)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 61.54% | 38.46% | 0.21% | 0.23% | 39 |
| T+7 | 55.26% | 44.74% | 0.58% | 0.2% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.19% | 0.23% | 38 |
| T+7 | 55.26% | 44.74% | 0.58% | 0.2% | 38 |

## Historical Distribution Summary

When CPI was **UP**, QQQ T+1 up probability was **60.53%** (n=38).

When CPI was **UP**, QQQ T+7 up probability was **55.26%** (n=38).

Same-direction T+7 median return: **0.58%**.

For QQQ, historical CPI windows show all-history T+1 up probability of 61.54% and T+7 up probability of 55.26%. When CPI printed Up versus previous, T+1 up probability was 60.53% and T+7 up probability was 55.26% across 38 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
