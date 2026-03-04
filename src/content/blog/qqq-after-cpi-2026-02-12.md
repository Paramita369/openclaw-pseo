---
title: "QQQ CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-02-12"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 8.09
robust_score: 8.09
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 100
sample_size: 39
freshness_days: 19
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/qqq-after-cpi-2026-02-12"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "up"
event_actual: 326.588
event_previous: 326.031
event_delta: 0.557
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: -0.1
  volatility: 3.07
  impact_t1_pct: 0.21
  impact_t7_pct: 0.47
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
related_events: [{"slug": "qqq-after-cpi-2025-12-18", "title": "QQQ After CPI (2025-12-18): Historical T+1/T+7 Probability", "event_date": "2025-12-18", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.56, "sample_size": 0}, {"slug": "qqq-after-cpi-2025-10-24", "title": "QQQ After CPI (2025-10-24): Historical T+1/T+7 Probability", "event_date": "2025-10-24", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.94, "sample_size": 0}, {"slug": "qqq-after-cpi-2025-10-12", "title": "QQQ After CPI (2025-10-12): Historical T+1/T+7 Probability", "event_date": "2025-10-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.74, "sample_size": 0}]
chartData: [{"time": "2026-02-09", "open": 607.54, "high": 616.46, "low": 605.07, "close": 614.32}, {"time": "2026-02-10", "open": 615.31, "high": 617.02, "low": 611.01, "close": 611.47}, {"time": "2026-02-11", "open": 616.38, "high": 617.52, "low": 607.69, "close": 613.11}, {"time": "2026-02-12", "open": 614.71, "high": 615.81, "low": 599.57, "close": 600.64}, {"time": "2026-02-13", "open": 600.43, "high": 606.48, "low": 596.42, "close": 601.92}, {"time": "2026-02-17", "open": 598.38, "high": 603.95, "low": 593.34, "close": 601.3}, {"time": "2026-02-18", "open": 602.11, "high": 609.77, "low": 600.72, "close": 605.79}, {"time": "2026-02-19", "open": 602.81, "high": 605.82, "low": 600.75, "close": 603.47}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2026-02-12**
- As-of date (T-1): **2026-03-03**
- Freshness age: **19 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.588, Previous 326.031, Delta +0.5570)
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
