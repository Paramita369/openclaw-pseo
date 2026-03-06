---
title: "2024-06-11 FOMC Meeting: GOLD T+1/T+7 Probability Profile"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "fomc_3"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-06-11"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 22.0
robust_score: 12.0
penalties:
  sample: 4.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 9
freshness_days: 632
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.59
hub_baseline_median_t7: 0.9
hub_baseline_std_t7: 2.0208
hub_baseline_delta: 0.09
z_score_t7: 0.2
percentile_t7: 66.67
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/gold/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 3.96
  mdd_t7: 0.0
  volatility: 0.25
  impact_t1_pct: 1.24
  impact_t7_pct: 0.99
probabilities:
  sample_size: 9
  t1:
    up: 88.89
    down: 11.11
    median: 0.83
    mean: 0.72
    sample: 9
  t7:
    up: 66.67
    down: 33.33
    median: 0.9
    mean: 0.59
    sample: 9
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 9
    t1:
      up: 88.89
      down: 11.11
      median: 0.83
      mean: 0.72
      sample: 9
    t7:
      up: 66.67
      down: 33.33
      median: 0.9
      mean: 0.59
      sample: 9
related_events: [{"slug": "gold-after-fomc-2024-01-30", "title": "2024-01-30 FOMC Meeting: GOLD T+1/T+7 Probability Profile", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 1.61, "median_t7_pct": 0.9, "sample_size": 9}, {"slug": "gold-after-fomc-2026-01-28", "title": "GOLD After FOMC (2026-01-28): Historical Signal & Probability", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 0.9, "sample_size": 9}, {"slug": "gold-after-fomc-2025-12-10", "title": "2025-12-10 FOMC Meeting: GOLD T+1/T+7 Probability Profile", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 0.9, "sample_size": 9}]
chartData: [{"time": "2024-06-10", "open": 2290.6, "high": 2309.3, "low": 2290.5, "close": 2307.7}, {"time": "2024-06-11", "open": 2300.0, "high": 2314.1, "low": 2300.0, "close": 2307.5}, {"time": "2024-06-12", "open": 2314.9, "high": 2338.7, "low": 2310.3, "close": 2336.0}, {"time": "2024-06-13", "open": 2309.4, "high": 2317.7, "low": 2296.2, "close": 2300.2}, {"time": "2024-06-14", "open": 2307.0, "high": 2331.4, "low": 2305.8, "close": 2331.4}, {"time": "2024-06-17", "open": 2320.2, "high": 2320.2, "low": 2309.6, "close": 2312.4}, {"time": "2024-06-18", "open": 2311.8, "high": 2330.4, "low": 2311.8, "close": 2330.4}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2024-06-11**
- As-of date (T-1): **2026-03-05**
- Freshness age: **632 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.5, Previous 5.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 88.89% | 11.11% | 0.83% | 0.72% | 9 |
| T+7 | 66.67% | 33.33% | 0.9% | 0.59% | 9 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 88.89% | 11.11% | 0.83% | 0.72% | 9 |
| T+7 | 66.67% | 33.33% | 0.9% | 0.59% | 9 |

## Historical Distribution Summary

When FOMC was **FLAT**, GOLD T+1 up probability was **88.89%** (n=9).

When FOMC was **FLAT**, GOLD T+7 up probability was **66.67%** (n=9).

Same-direction T+7 median return: **0.9%**.

For GOLD, historical FOMC windows show all-history T+1 up probability of 88.89% and T+7 up probability of 66.67%. When FOMC printed Flat versus previous, T+1 up probability was 88.89% and T+7 up probability was 66.67% across 9 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
