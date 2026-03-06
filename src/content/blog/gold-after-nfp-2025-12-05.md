---
title: "GOLD Post-NFP Setup (2025-12-05): Historical Probability Lens"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-12-05"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 4.31
robust_score: -1.69
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 40
sample_size: 13
freshness_days: 90
freshness_status: "stale"
index_tier: "C"
is_recent_90d: true
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.14
hub_baseline_median_t7: 1.07
hub_baseline_std_t7: 1.6215
hub_baseline_delta: 0.07
z_score_t7: 0.0
percentile_t7: 61.54
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "none"
canonical_url: ""
robots_directive: "noindex,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 158497.0
event_previous: 158449.0
event_delta: 48.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.0
  mdd_t7: 0.0
  volatility: 1.14
  impact_t1_pct: 0.0
  impact_t7_pct: 1.14
probabilities:
  sample_size: 13
  t1:
    up: 0.0
    down: 100.0
    median: 0.0
    mean: 0.0
    sample: 0
  t7:
    up: 84.62
    down: 15.38
    median: 1.07
    mean: 1.14
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 0
    t1:
      up: 0.0
      down: 100.0
      median: 0.0
      mean: 0.0
      sample: 0
    t7:
      up: 83.33
      down: 16.67
      median: 0.86
      mean: 1.12
      sample: 12
related_events: [{"slug": "gold-after-nfp-2024-03-01", "title": "GOLD NFP Reaction (2024-03-01): T+1/T+7 Up Probability", "event_date": "2024-03-01", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.57, "median_t7_pct": 1.07, "sample_size": 13}, {"slug": "gold-after-nfp-2024-04-05", "title": "NFP Print (2024-04-05) vs GOLD: Quantified Directional Odds", "event_date": "2024-04-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 4.16, "median_t7_pct": 1.07, "sample_size": 13}, {"slug": "gold-after-nfp-2024-09-06", "title": "GOLD Post-NFP Setup (2024-09-06): Historical Probability Lens", "event_date": "2024-09-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 1.09, "median_t7_pct": 1.07, "sample_size": 13}]
chartData: [{"time": "2025-12-02", "open": 4230.5, "high": 4230.5, "low": 4167.0, "close": 4186.6}, {"time": "2025-12-03", "open": 4215.7, "high": 4234.1, "low": 4195.7, "close": 4199.3}, {"time": "2025-12-04", "open": 4211.0, "high": 4211.8, "low": 4175.0, "close": 4211.8}, {"time": "2025-12-05", "open": 4204.1, "high": 4255.7, "low": 4194.5, "close": 4212.9}, {"time": "2025-12-08", "open": 4205.5, "high": 4215.8, "low": 4175.5, "close": 4187.2}, {"time": "2025-12-09", "open": 4190.7, "high": 4219.7, "low": 4177.7, "close": 4206.7}, {"time": "2025-12-10", "open": 4209.0, "high": 4234.5, "low": 4183.6, "close": 4196.4}, {"time": "2025-12-11", "open": 4224.0, "high": 4286.9, "low": 4214.3, "close": 4285.5}, {"time": "2025-12-12", "open": 4276.4, "high": 4355.0, "low": 4260.0, "close": 4300.1}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
- Event date: **2025-12-05**
- As-of date (T-1): **2026-03-05**
- Freshness age: **90 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 158497.0, Previous 158449.0, Delta +48.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 84.62% | 15.38% | 1.07% | 1.14% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 83.33% | 16.67% | 0.86% | 1.12% | 12 |

## Historical Distribution Summary

When NFP was **UP**, GOLD T+1 up probability was **0.0%** (n=0).

When NFP was **UP**, GOLD T+7 up probability was **83.33%** (n=12).

Same-direction T+7 median return: **0.86%**.

For GOLD, historical NFP windows show all-history T+1 up probability of 0.0% and T+7 up probability of 84.62%. When NFP printed Up versus previous, T+1 up probability was 0.0% and T+7 up probability was 83.33% across 0 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
