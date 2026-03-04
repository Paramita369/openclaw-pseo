---
title: "FOMC Outcome (2025-06-18) for QQQ: Up/Down Probability View"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 5
title_template_key: "fomc_5"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-06-18"
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
quality_score: 100
sample_size: 23
freshness_days: 258
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "flat"
event_actual: 4.5
event_previous: 4.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: -0.41
  volatility: 14.46
  impact_t1_pct: -0.41
  impact_t7_pct: 2.42
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
    direction: "flat"
    sample_size: 17
    t1:
      up: 41.18
      down: 58.82
      median: -0.34
      mean: -0.06
      sample: 17
    t7:
      up: 64.71
      down: 35.29
      median: 1.08
      mean: 0.6
      sample: 17
related_events: [{"slug": "qqq-after-fomc-2025-05-07", "title": "QQQ After FOMC (2025-05-07): Historical T+1/T+7 Probability", "event_date": "2025-05-07", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 7.32, "sample_size": 0}, {"slug": "qqq-after-fomc-2025-01-29", "title": "QQQ After FOMC (2025-01-29): Historical T+1/T+7 Probability", "event_date": "2025-01-29", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.16, "sample_size": 0}, {"slug": "qqq-after-fomc-2024-12-19", "title": "QQQ After FOMC (2024-12-19): Historical T+1/T+7 Probability", "event_date": "2024-12-19", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.17, "sample_size": 0}]
chartData: [{"time": "2025-06-16", "open": 528.61, "high": 533.46, "low": 528.56, "close": 532.39}, {"time": "2025-06-17", "open": 529.82, "high": 531.43, "low": 526.03, "close": 527.2}, {"time": "2025-06-18", "open": 528.21, "high": 530.65, "low": 525.52, "close": 527.11}, {"time": "2025-06-20", "open": 530.36, "high": 531.66, "low": 523.01, "close": 524.95}, {"time": "2025-06-23", "open": 525.52, "high": 530.87, "low": 522.37, "close": 530.35}, {"time": "2025-06-24", "open": 535.58, "high": 539.38, "low": 534.96, "close": 538.46}, {"time": "2025-06-25", "open": 540.74, "high": 541.98, "low": 538.06, "close": 539.84}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
- Event date: **2025-06-18**
- As-of date (T-1): **2026-03-03**
- Freshness age: **258 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.5, Previous 4.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 43.48% | 56.52% | -0.19% | -0.05% | 23 |
| T+7 | 56.52% | 43.48% | 0.88% | 0.27% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 41.18% | 58.82% | -0.34% | -0.06% | 17 |
| T+7 | 64.71% | 35.29% | 1.08% | 0.6% | 17 |

## Historical Distribution Summary

When FOMC was **FLAT**, QQQ T+1 up probability was **41.18%** (n=17).

When FOMC was **FLAT**, QQQ T+7 up probability was **64.71%** (n=17).

Same-direction T+7 median return: **1.08%**.

For QQQ, historical FOMC windows show all-history T+1 up probability of 43.48% and T+7 up probability of 56.52%. When FOMC printed Flat versus previous, T+1 up probability was 41.18% and T+7 up probability was 64.71% across 17 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
