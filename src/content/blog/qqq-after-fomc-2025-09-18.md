---
title: "2025-09-18 FOMC Meeting: QQQ T+1/T+7 Probability Profile"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 3
title_template_key: "fomc_3"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-09-18"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 3.3
robust_score: -2.7
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
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "down"
event_actual: 4.25
event_previous: 4.5
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -0.92
  mdd_t7: -1.44
  volatility: 15.53
  impact_t1_pct: 0.68
  impact_t7_pct: -0.19
probabilities:
  sample_size: 23
  t1:
    up: 43.48
    down: 56.52
    median: -0.19
    mean: -0.05
    sample: 23
  t7:
    up: 56.52
    down: 43.48
    median: 0.88
    mean: 0.27
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 6
    t1:
      up: 50.0
      down: 50.0
      median: 0.21
      mean: -0.02
      sample: 6
    t7:
      up: 33.33
      down: 66.67
      median: -1.24
      mean: -0.66
      sample: 6
related_events: [{"slug": "qqq-after-fomc-2025-06-18", "title": "QQQ After FOMC (2025-06-18): Historical T+1/T+7 Probability", "event_date": "2025-06-18", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.42, "sample_size": 0}, {"slug": "qqq-after-fomc-2025-05-07", "title": "QQQ After FOMC (2025-05-07): Historical T+1/T+7 Probability", "event_date": "2025-05-07", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 7.32, "sample_size": 0}, {"slug": "qqq-after-fomc-2025-01-29", "title": "QQQ After FOMC (2025-01-29): Historical T+1/T+7 Probability", "event_date": "2025-01-29", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.16, "sample_size": 0}]
chartData: [{"time": "2025-09-15", "open": 587.0, "high": 590.34, "low": 586.85, "close": 590.23}, {"time": "2025-09-16", "open": 591.16, "high": 591.41, "low": 589.05, "close": 589.74}, {"time": "2025-09-17", "open": 589.66, "high": 590.3, "low": 582.94, "close": 588.56}, {"time": "2025-09-18", "open": 593.46, "high": 596.68, "low": 591.51, "close": 593.87}, {"time": "2025-09-19", "open": 595.87, "high": 598.58, "low": 594.39, "close": 597.89}, {"time": "2025-09-22", "open": 596.97, "high": 602.09, "low": 596.95, "close": 601.43}, {"time": "2025-09-23", "open": 601.59, "high": 601.79, "low": 596.21, "close": 597.43}, {"time": "2025-09-24", "open": 598.81, "high": 599.13, "low": 592.6, "close": 595.33}, {"time": "2025-09-25", "open": 591.44, "high": 594.35, "low": 587.74, "close": 592.77}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
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
| T+1 | 43.48% | 56.52% | -0.19% | -0.05% | 23 |
| T+7 | 56.52% | 43.48% | 0.88% | 0.27% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.21% | -0.02% | 6 |
| T+7 | 33.33% | 66.67% | -1.24% | -0.66% | 6 |

## Historical Distribution Summary

When FOMC was **DOWN**, QQQ T+1 up probability was **50.0%** (n=6).

When FOMC was **DOWN**, QQQ T+7 up probability was **33.33%** (n=6).

Same-direction T+7 median return: **-1.24%**.

For QQQ, historical FOMC windows show all-history T+1 up probability of 43.48% and T+7 up probability of 56.52%. When FOMC printed Down versus previous, T+1 up probability was 50.0% and T+7 up probability was 33.33% across 6 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
