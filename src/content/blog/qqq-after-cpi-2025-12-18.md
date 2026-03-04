---
title: "QQQ After CPI (2025-12-18): Up/Down Odds and Median Returns"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 5
title_template_key: "cpi_5"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-12-18"
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
freshness_days: 75
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/qqq-after-cpi-2025-12-18"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 326.031
event_previous: 325.063
event_delta: 0.968
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 5.44
  impact_t1_pct: 1.3
  impact_t7_pct: 2.56
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
related_events: [{"slug": "qqq-after-cpi-2026-02-12", "title": "QQQ After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 0.47, "sample_size": 0}, {"slug": "qqq-after-cpi-2025-10-24", "title": "QQQ After CPI (2025-10-24): Historical T+1/T+7 Probability", "event_date": "2025-10-24", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.94, "sample_size": 0}, {"slug": "qqq-after-cpi-2025-10-12", "title": "QQQ After CPI (2025-10-12): Historical T+1/T+7 Probability", "event_date": "2025-10-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.74, "sample_size": 0}]
chartData: [{"time": "2025-12-15", "open": 617.57, "high": 617.62, "low": 608.54, "close": 609.75}, {"time": "2025-12-16", "open": 607.48, "high": 612.72, "low": 606.13, "close": 610.96}, {"time": "2025-12-17", "open": 612.27, "high": 612.86, "low": 599.51, "close": 599.64}, {"time": "2025-12-18", "open": 609.02, "high": 612.14, "low": 606.14, "close": 608.33}, {"time": "2025-12-19", "open": 611.16, "high": 616.83, "low": 611.08, "close": 616.26}, {"time": "2025-12-22", "open": 621.35, "high": 621.65, "low": 617.77, "close": 619.21}, {"time": "2025-12-23", "open": 618.2, "high": 622.41, "low": 617.78, "close": 622.11}, {"time": "2025-12-24", "open": 621.99, "high": 624.28, "low": 621.72, "close": 623.93}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2025-12-18**
- As-of date (T-1): **2026-03-03**
- Freshness age: **75 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.031, Previous 325.063, Delta +0.9680)
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
