---
title: "GOLD After FOMC (2025-07-30): Historical Signal & Probability"
description: "Historical probability profile for GOLD around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 1
title_template_key: "fomc_1"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-07-30"
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
quality_score: 60
sample_size: 9
freshness_days: 218
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.59
hub_baseline_median_t7: 0.9
hub_baseline_std_t7: 2.0208
hub_baseline_delta: -0.31
z_score_t7: -0.0
percentile_t7: 44.44
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/gold/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "flat"
event_actual: 4.5
event_previous: 4.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 4.54
  mdd_t7: 0.0
  volatility: 0.13
  impact_t1_pct: 0.72
  impact_t7_pct: 0.59
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
chartData: [{"time": "2025-07-28", "open": 3326.6, "high": 3326.8, "low": 3309.1, "close": 3309.1}, {"time": "2025-07-29", "open": 3323.4, "high": 3323.4, "low": 3323.4, "close": 3323.4}, {"time": "2025-07-30", "open": 3325.8, "high": 3331.8, "low": 3263.9, "close": 3295.8}, {"time": "2025-07-31", "open": 3272.9, "high": 3312.0, "low": 3272.9, "close": 3293.2}, {"time": "2025-08-01", "open": 3286.2, "high": 3360.6, "low": 3281.0, "close": 3347.7}, {"time": "2025-08-04", "open": 3367.6, "high": 3386.5, "low": 3347.4, "close": 3374.4}, {"time": "2025-08-05", "open": 3378.5, "high": 3387.2, "low": 3351.2, "close": 3381.9}, {"time": "2025-08-06", "open": 3380.7, "high": 3383.3, "low": 3361.3, "close": 3380.0}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **GOLD**
- Event date: **2025-07-30**
- As-of date (T-1): **2026-03-05**
- Freshness age: **218 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.5, Previous 4.5, Delta +0.0000)
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
