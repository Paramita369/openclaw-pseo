---
title: "2024-01-05 Nonfarm Payrolls: SPY Historical Win Rate"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-01-05"
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
quality_score: 80
sample_size: 34
freshness_days: 793
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.81
hub_baseline_median_t7: 0.11
hub_baseline_std_t7: 1.9337
hub_baseline_delta: 1.76
z_score_t7: 0.55
percentile_t7: 82.35
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 157032.0
event_previous: 156857.0
event_delta: 175.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 6.04
  mdd_t7: -1.33
  volatility: 1.97
  impact_t1_pct: -0.1
  impact_t7_pct: 1.87
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
    direction: "up"
    sample_size: 18
    t1:
      up: 38.89
      down: 61.11
      median: -0.13
      mean: -0.22
      sample: 18
    t7:
      up: 56.67
      down: 43.33
      median: 0.11
      mean: 0.83
      sample: 30
related_events: [{"slug": "spy-after-nfp-2024-07-05", "title": "2024-07-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-07-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.02, "median_t7_pct": 1.39, "sample_size": 13}, {"slug": "spy-after-nfp-2024-10-04", "title": "SPY NFP Reaction (2024-10-04): T+1/T+7 Up Probability", "event_date": "2024-10-04", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.43, "median_t7_pct": 1.39, "sample_size": 13}, {"slug": "spy-after-nfp-2024-08-02", "title": "NFP Print (2024-08-02) vs SPY: Quantified Directional Odds", "event_date": "2024-08-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 2.25, "median_t7_pct": 1.39, "sample_size": 13}]
chartData: [{"time": "2024-01-02", "open": 460.77, "high": 462.24, "low": 459.14, "close": 461.25}, {"time": "2024-01-03", "open": 459.08, "high": 459.82, "low": 456.88, "close": 457.48}, {"time": "2024-01-04", "open": 457.0, "high": 459.6, "low": 455.78, "close": 456.01}, {"time": "2024-01-05", "open": 456.21, "high": 459.09, "low": 455.18, "close": 456.63}, {"time": "2024-01-08", "open": 457.13, "high": 463.3, "low": 457.0, "close": 463.15}, {"time": "2024-01-09", "open": 460.49, "high": 463.47, "low": 459.98, "close": 462.45}, {"time": "2024-01-10", "open": 462.72, "high": 465.93, "low": 462.44, "close": 465.06}, {"time": "2024-01-11", "open": 466.07, "high": 466.59, "low": 460.87, "close": 464.86}, {"time": "2024-01-12", "open": 466.31, "high": 467.05, "low": 463.77, "close": 465.18}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2024-01-05**
- As-of date (T-1): **2026-03-08**
- Freshness age: **793 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157032.0, Previous 156857.0, Delta +175.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 47.62% | 52.38% | -0.04% | -0.1% | 21 |
| T+7 | 55.88% | 44.12% | 0.11% | 0.81% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 38.89% | 61.11% | -0.13% | -0.22% | 18 |
| T+7 | 56.67% | 43.33% | 0.11% | 0.83% | 30 |

## Historical Distribution Summary

When NFP was **UP**, SPY T+1 up probability was **38.89%** (n=18).

When NFP was **UP**, SPY T+7 up probability was **56.67%** (n=30).

Same-direction T+7 median return: **0.11%**.

For SPY, historical NFP windows show all-history T+1 up probability of 47.62% and T+7 up probability of 55.88%. When NFP printed Up versus previous, T+1 up probability was 38.89% and T+7 up probability was 56.67% across 18 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
