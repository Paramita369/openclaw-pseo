---
title: "2025-06-06 Nonfarm Payrolls: QQQ Historical Win Rate"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-06-06"
asof_date: "2026-03-10"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 4.14
robust_score: -1.86
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 60
sample_size: 34
freshness_days: 277
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.03
hub_baseline_median_t7: 0.12
hub_baseline_std_t7: 2.5414
hub_baseline_delta: -0.68
z_score_t7: -0.63
percentile_t7: 26.47
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/qqq/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 158478.0
event_previous: 158498.0
event_delta: -20.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -0.79
  mdd_t7: -0.56
  volatility: 0.71
  impact_t1_pct: 0.15
  impact_t7_pct: -0.56
probabilities:
  sample_size: 34
  t1:
    up: 57.14
    down: 42.86
    median: 0.15
    mean: -0.12
    sample: 21
  t7:
    up: 50.0
    down: 50.0
    median: 0.12
    mean: 1.03
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 3
    t1:
      up: 100.0
      down: 0.0
      median: 0.75
      mean: 0.91
      sample: 3
    t7:
      up: 50.0
      down: 50.0
      median: 1.16
      mean: 0.94
      sample: 4
related_events: [{"slug": "qqq-after-nfp-2025-01-10", "title": "2025-01-10 Nonfarm Payrolls: QQQ Historical Win Rate", "event_date": "2025-01-10", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.64, "median_t7_pct": 0.12, "sample_size": 34}, {"slug": "qqq-after-nfp-2024-12-06", "title": "QQQ After NFP (2024-12-06): Event Probability and Median Return", "event_date": "2024-12-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.77, "median_t7_pct": 0.12, "sample_size": 34}, {"slug": "qqq-after-nfp-2024-08-02", "title": "QQQ After NFP (2024-08-02): Event Probability and Median Return", "event_date": "2024-08-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.35, "median_t7_pct": 0.12, "sample_size": 34}]
chartData: [{"time": "2025-06-03", "open": 521.69, "high": 526.86, "low": 520.83, "close": 525.42}, {"time": "2025-06-04", "open": 526.13, "high": 527.95, "low": 524.1, "close": 526.89}, {"time": "2025-06-05", "open": 528.29, "high": 531.15, "low": 520.8, "close": 522.92}, {"time": "2025-06-06", "open": 528.11, "high": 529.91, "low": 526.33, "close": 528.03}, {"time": "2025-06-09", "open": 528.25, "high": 530.45, "low": 527.13, "close": 528.81}, {"time": "2025-06-10", "open": 529.28, "high": 532.99, "low": 527.01, "close": 532.31}, {"time": "2025-06-11", "open": 533.71, "high": 534.87, "low": 528.22, "close": 530.51}, {"time": "2025-06-12", "open": 529.2, "high": 532.74, "low": 528.95, "close": 531.76}, {"time": "2025-06-13", "open": 525.8, "high": 529.98, "low": 523.86, "close": 525.08}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2025-06-06**
- As-of date (T-1): **2026-03-10**
- Freshness age: **277 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158478.0, Previous 158498.0, Delta -20.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 57.14% | 42.86% | 0.15% | -0.12% | 21 |
| T+7 | 50.0% | 50.0% | 0.12% | 1.03% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 100.0% | 0.0% | 0.75% | 0.91% | 3 |
| T+7 | 50.0% | 50.0% | 1.16% | 0.94% | 4 |

## Historical Distribution Summary

When NFP was **DOWN**, QQQ T+1 up probability was **100.0%** (n=3).

When NFP was **DOWN**, QQQ T+7 up probability was **50.0%** (n=4).

Same-direction T+7 median return: **1.16%**.

For QQQ, historical NFP windows show all-history T+1 up probability of 57.14% and T+7 up probability of 50.0%. When NFP printed Down versus previous, T+1 up probability was 100.0% and T+7 up probability was 50.0% across 3 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
