---
title: "NFP Print (2025-10-03) vs SPY: Quantified Directional Odds"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 4
title_template_key: "nfp_4"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-10-03"
asof_date: "2026-03-12"
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
quality_score: 60
sample_size: 34
freshness_days: 160
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.81
hub_baseline_median_t7: 0.11
hub_baseline_std_t7: 1.9337
hub_baseline_delta: -2.53
z_score_t7: -1.67
percentile_t7: 0.0
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 158408.0
event_previous: 158548.0
event_delta: -140.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -0.87
  mdd_t7: -2.42
  volatility: 2.78
  impact_t1_pct: 0.36
  impact_t7_pct: -2.42
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
related_events: [{"slug": "spy-after-nfp-2024-07-05", "title": "2024-07-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-07-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.02, "median_t7_pct": 0.11, "sample_size": 34}, {"slug": "spy-after-nfp-2024-01-05", "title": "2024-01-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-01-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.04, "median_t7_pct": 0.11, "sample_size": 34}, {"slug": "spy-after-nfp-2024-10-04", "title": "SPY NFP Reaction (2024-10-04): T+1/T+7 Up Probability", "event_date": "2024-10-04", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.43, "median_t7_pct": 0.11, "sample_size": 34}]
chartData: [{"time": "2025-09-30", "open": 660.98, "high": 664.69, "low": 659.66, "close": 664.22}, {"time": "2025-10-01", "open": 661.22, "high": 667.4, "low": 661.11, "close": 666.48}, {"time": "2025-10-02", "open": 668.47, "high": 668.59, "low": 664.82, "close": 667.25}, {"time": "2025-10-03", "open": 668.02, "high": 670.7, "low": 666.19, "close": 667.24}, {"time": "2025-10-06", "open": 669.64, "high": 670.53, "low": 667.49, "close": 669.63}, {"time": "2025-10-07", "open": 670.56, "high": 671.01, "low": 665.7, "close": 667.15}, {"time": "2025-10-08", "open": 668.28, "high": 671.23, "low": 667.45, "close": 671.13}, {"time": "2025-10-09", "open": 671.55, "high": 671.95, "low": 667.24, "close": 669.18}, {"time": "2025-10-10", "open": 670.15, "high": 671.96, "low": 650.92, "close": 651.1}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2025-10-03**
- As-of date (T-1): **2026-03-12**
- Freshness age: **160 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158408.0, Previous 158548.0, Delta -140.0000)
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
