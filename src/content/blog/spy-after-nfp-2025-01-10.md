---
title: "NFP Print (2025-01-10) vs SPY: Quantified Directional Odds"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 4
title_template_key: "nfp_4"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-01-10"
asof_date: "2026-03-08"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 4.23
robust_score: -1.77
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 50
sample_size: 34
freshness_days: 422
freshness_status: "stale"
index_tier: "C"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 0.81
hub_baseline_median_t7: 0.11
hub_baseline_std_t7: 1.9337
hub_baseline_delta: 2.83
z_score_t7: 1.1
percentile_t7: 88.24
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "none"
canonical_url: ""
robots_directive: "noindex,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:04:09+00:00"
event_direction: "down"
event_actual: 158268.0
event_previous: 158316.0
event_delta: -48.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.97
  mdd_t7: -0.1
  volatility: 3.04
  impact_t1_pct: -0.1
  impact_t7_pct: 2.94
probabilities:
  sample_size: 34
  t1:
    up: 47.62
    down: 52.38
    median: -0.04
    mean: -0.1
    sample: 21
  t7:
    up: 55.88
    down: 44.12
    median: 0.11
    mean: 0.81
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 3
    t1:
      up: 100.0
      down: 0.0
      median: 0.36
      mean: 0.66
      sample: 3
    t7:
      up: 50.0
      down: 50.0
      median: 1.06
      mean: 0.66
      sample: 4
related_events: [{"slug": "spy-after-nfp-2024-07-05", "title": "2024-07-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-07-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.02, "median_t7_pct": 1.39, "sample_size": 13}, {"slug": "spy-after-nfp-2024-01-05", "title": "2024-01-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-01-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.04, "median_t7_pct": 1.39, "sample_size": 13}, {"slug": "spy-after-nfp-2024-10-04", "title": "SPY NFP Reaction (2024-10-04): T+1/T+7 Up Probability", "event_date": "2024-10-04", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.43, "median_t7_pct": 1.39, "sample_size": 13}]
chartData: [{"time": "2025-01-07", "open": 590.49, "high": 590.81, "low": 579.97, "close": 581.8}, {"time": "2025-01-08", "open": 581.87, "high": 583.73, "low": 578.41, "close": 582.65}, {"time": "2025-01-10", "open": 579.08, "high": 579.15, "low": 571.83, "close": 573.75}, {"time": "2025-01-13", "open": 569.09, "high": 575.0, "low": 568.67, "close": 574.64}, {"time": "2025-01-14", "open": 577.58, "high": 578.21, "low": 571.64, "close": 575.43}, {"time": "2025-01-15", "open": 583.48, "high": 587.05, "low": 582.36, "close": 585.9}, {"time": "2025-01-16", "open": 587.27, "high": 587.45, "low": 584.07, "close": 584.77}, {"time": "2025-01-17", "open": 590.03, "high": 592.4, "low": 588.7, "close": 590.64}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2025-01-10**
- As-of date (T-1): **2026-03-08**
- Freshness age: **422 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158268.0, Previous 158316.0, Delta -48.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 47.62% | 52.38% | -0.04% | -0.1% | 21 |
| T+7 | 55.88% | 44.12% | 0.11% | 0.81% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 100.0% | 0.0% | 0.36% | 0.66% | 3 |
| T+7 | 50.0% | 50.0% | 1.06% | 0.66% | 4 |

## Historical Distribution Summary

When NFP was **DOWN**, SPY T+1 up probability was **100.0%** (n=3).

When NFP was **DOWN**, SPY T+7 up probability was **50.0%** (n=4).

Same-direction T+7 median return: **1.06%**.

For SPY, historical NFP windows show all-history T+1 up probability of 47.62% and T+7 up probability of 55.88%. When NFP printed Down versus previous, T+1 up probability was 100.0% and T+7 up probability was 50.0% across 3 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
