---
title: "QQQ After FOMC (2024-09-19): Historical Signal & Probability"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 1
title_template_key: "fomc_1"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-09-19"
asof_date: "2026-03-05"
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
freshness_days: 532
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 5.0
event_previous: 5.5
event_delta: -0.5
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: -0.19
  volatility: 10.12
  impact_t1_pct: -0.19
  impact_t7_pct: 1.41
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
chartData: [{"time": "2024-09-16", "open": 469.38, "high": 470.05, "low": 466.11, "close": 469.43}, {"time": "2024-09-17", "open": 472.46, "high": 473.76, "low": 467.18, "close": 469.68}, {"time": "2024-09-18", "open": 470.88, "high": 474.98, "low": 467.04, "close": 467.65}, {"time": "2024-09-19", "open": 478.73, "high": 482.32, "low": 476.63, "close": 479.47}, {"time": "2024-09-20", "open": 478.61, "high": 479.8, "low": 474.45, "close": 478.56}, {"time": "2024-09-23", "open": 479.74, "high": 480.92, "low": 478.4, "close": 479.83}, {"time": "2024-09-24", "open": 481.24, "high": 483.1, "low": 476.98, "close": 482.14}, {"time": "2024-09-25", "open": 481.52, "high": 484.55, "low": 481.34, "close": 482.59}, {"time": "2024-09-26", "open": 490.09, "high": 490.42, "low": 482.57, "close": 486.22}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
- Event date: **2024-09-19**
- As-of date (T-1): **2026-03-05**
- Freshness age: **532 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **DOWN** (Actual 5.0, Previous 5.5, Delta -0.5000)
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
