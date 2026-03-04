---
title: "QQQ After FOMC (2025-12-11): Historical Signal & Probability"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 1
title_template_key: "fomc_1"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-12-11"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 3.3
robust_score: 3.3
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 23
freshness_days: 82
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/qqq-after-fomc-2025-12-11"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "down"
event_actual: 3.75
event_previous: 4.0
event_delta: -0.25
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -10.0
  mdd_t7: -2.63
  volatility: 11.68
  impact_t1_pct: -1.91
  impact_t7_pct: -2.63
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
chartData: [{"time": "2025-12-08", "open": 626.4, "high": 628.03, "low": 620.89, "close": 623.48}, {"time": "2025-12-09", "open": 622.21, "high": 625.06, "low": 620.2, "close": 624.25}, {"time": "2025-12-10", "open": 623.05, "high": 628.4, "low": 620.19, "close": 626.8}, {"time": "2025-12-11", "open": 623.02, "high": 624.97, "low": 616.93, "close": 624.78}, {"time": "2025-12-12", "open": 621.28, "high": 622.74, "low": 610.57, "close": 612.83}, {"time": "2025-12-15", "open": 617.57, "high": 617.62, "low": 608.54, "close": 609.75}, {"time": "2025-12-16", "open": 607.48, "high": 612.72, "low": 606.13, "close": 610.96}, {"time": "2025-12-17", "open": 612.27, "high": 612.86, "low": 599.51, "close": 599.64}, {"time": "2025-12-18", "open": 609.02, "high": 612.14, "low": 606.14, "close": 608.33}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
- Event date: **2025-12-11**
- As-of date (T-1): **2026-03-03**
- Freshness age: **82 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 3.75, Previous 4.0, Delta -0.2500)
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
