---
title: "Fed Decision (2025-01-29) and SPY: Event-Driven Odds"
description: "Historical probability profile for SPY around FOMC events (T+1/T+7)."
pubDate: "2026-03-04"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-01-29"
asof_date: "2026-03-03"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 5.91
robust_score: -0.09
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 100
sample_size: 23
freshness_days: 398
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T11:37:55+00:00"
event_direction: "flat"
event_actual: 4.5
event_previous: 4.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 9.47
  mdd_t7: -0.14
  volatility: 5.34
  impact_t1_pct: 0.54
  impact_t7_pct: 0.4
probabilities:
  sample_size: 23
  t1:
    up: 52.17
    down: 47.83
    median: 0.1
    mean: -0.02
    sample: 23
  t7:
    up: 56.52
    down: 43.48
    median: 0.54
    mean: 0.26
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 17
    t1:
      up: 47.06
      down: 52.94
      median: -0.2
      mean: -0.08
      sample: 17
    t7:
      up: 64.71
      down: 35.29
      median: 0.57
      mean: 0.48
      sample: 17
related_events: [{"slug": "spy-after-fomc-2025-06-18", "title": "SPY After FOMC (2025-06-18): Historical T+1/T+7 Probability", "event_date": "2025-06-18", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.92, "sample_size": 0}, {"slug": "spy-after-fomc-2025-05-07", "title": "SPY After FOMC (2025-05-07): Historical T+1/T+7 Probability", "event_date": "2025-05-07", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.71, "sample_size": 0}, {"slug": "spy-after-fomc-2024-12-19", "title": "SPY After FOMC (2024-12-19): Historical T+1/T+7 Probability", "event_date": "2024-12-19", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.95, "sample_size": 0}]
chartData: [{"time": "2025-01-27", "open": 587.91, "high": 592.73, "low": 587.74, "close": 592.41}, {"time": "2025-01-28", "open": 593.65, "high": 598.34, "low": 590.32, "close": 597.5}, {"time": "2025-01-29", "open": 596.71, "high": 597.12, "low": 592.26, "close": 594.82}, {"time": "2025-01-30", "open": 596.95, "high": 599.56, "low": 593.75, "close": 598.02}, {"time": "2025-01-31", "open": 600.45, "high": 602.88, "low": 594.07, "close": 594.83}, {"time": "2025-02-03", "open": 585.79, "high": 593.32, "low": 583.64, "close": 590.83}, {"time": "2025-02-04", "open": 590.89, "high": 595.31, "low": 590.35, "close": 594.8}, {"time": "2025-02-05", "open": 593.67, "high": 597.36, "low": 591.63, "close": 597.21}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **SPY**
- Event date: **2025-01-29**
- As-of date (T-1): **2026-03-03**
- Freshness age: **398 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.5, Previous 4.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 52.17% | 47.83% | 0.1% | -0.02% | 23 |
| T+7 | 56.52% | 43.48% | 0.54% | 0.26% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 47.06% | 52.94% | -0.2% | -0.08% | 17 |
| T+7 | 64.71% | 35.29% | 0.57% | 0.48% | 17 |

## Historical Distribution Summary

When FOMC was **FLAT**, SPY T+1 up probability was **47.06%** (n=17).

When FOMC was **FLAT**, SPY T+7 up probability was **64.71%** (n=17).

Same-direction T+7 median return: **0.57%**.

For SPY, historical FOMC windows show all-history T+1 up probability of 52.17% and T+7 up probability of 56.52%. When FOMC printed Flat versus previous, T+1 up probability was 47.06% and T+7 up probability was 64.71% across 17 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
