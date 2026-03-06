---
title: "SPY Post-NFP Setup (2025-09-05): Historical Probability Lens"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-09-05"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 0.46
robust_score: -5.54
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 40
sample_size: 13
freshness_days: 181
freshness_status: "stale"
index_tier: "C"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.41
hub_baseline_median_t7: 1.39
hub_baseline_std_t7: 1.7058
hub_baseline_delta: 0.02
z_score_t7: 0.0
percentile_t7: 53.85
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "none"
canonical_url: ""
robots_directive: "noindex,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 158548.0
event_previous: 158472.0
event_delta: 76.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.0
  mdd_t7: 0.0
  volatility: 1.41
  impact_t1_pct: 0.0
  impact_t7_pct: 1.41
probabilities:
  sample_size: 13
  t1:
    up: 0.0
    down: 100.0
    median: 0.0
    mean: 0.0
    sample: 0
  t7:
    up: 76.92
    down: 23.08
    median: 1.39
    mean: 1.41
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
      up: 75.0
      down: 25.0
      median: 1.27
      mean: 1.28
      sample: 12
related_events: [{"slug": "spy-after-nfp-2024-07-05", "title": "2024-07-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-07-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.02, "median_t7_pct": 1.39, "sample_size": 13}, {"slug": "spy-after-nfp-2024-01-05", "title": "2024-01-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-01-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.04, "median_t7_pct": 1.39, "sample_size": 13}, {"slug": "spy-after-nfp-2024-10-04", "title": "SPY NFP Reaction (2024-10-04): T+1/T+7 Up Probability", "event_date": "2024-10-04", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.43, "median_t7_pct": 1.39, "sample_size": 13}]
chartData: [{"time": "2025-09-02", "open": 633.86, "high": 636.84, "low": 631.3, "close": 636.62}, {"time": "2025-09-03", "open": 639.0, "high": 640.54, "low": 636.81, "close": 640.07}, {"time": "2025-09-04", "open": 640.75, "high": 645.45, "low": 639.84, "close": 645.42}, {"time": "2025-09-05", "open": 647.76, "high": 648.49, "low": 639.66, "close": 643.55}, {"time": "2025-09-08", "open": 644.92, "high": 646.13, "low": 643.54, "close": 645.13}, {"time": "2025-09-09", "open": 645.27, "high": 647.15, "low": 643.53, "close": 646.62}, {"time": "2025-09-10", "open": 649.89, "high": 650.82, "low": 646.92, "close": 648.49}, {"time": "2025-09-11", "open": 650.45, "high": 654.58, "low": 649.86, "close": 653.88}, {"time": "2025-09-12", "open": 653.85, "high": 655.35, "low": 653.15, "close": 653.66}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2025-09-05**
- As-of date (T-1): **2026-03-05**
- Freshness age: **181 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 158548.0, Previous 158472.0, Delta +76.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 76.92% | 23.08% | 1.39% | 1.41% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 0.0% | 100.0% | 0.0% | 0.0% | 0 |
| T+7 | 75.0% | 25.0% | 1.27% | 1.28% | 12 |

## Historical Distribution Summary

When NFP was **UP**, SPY T+1 up probability was **0.0%** (n=0).

When NFP was **UP**, SPY T+7 up probability was **75.0%** (n=12).

Same-direction T+7 median return: **1.27%**.

For SPY, historical NFP windows show all-history T+1 up probability of 0.0% and T+7 up probability of 76.92%. When NFP printed Up versus previous, T+1 up probability was 0.0% and T+7 up probability was 75.0% across 0 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
