---
title: "ETH After NFP (2024-12-06): Event Probability and Median Return"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-12"
title_variant_id: 3
title_template_key: "nfp_3"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-12-06"
asof_date: "2026-03-11"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 4.94
robust_score: -1.06
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 34
freshness_days: 460
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 2.65
hub_baseline_median_t7: 1.44
hub_baseline_std_t7: 9.723
hub_baseline_delta: -3.8
z_score_t7: -0.51
percentile_t7: 29.41
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-05T00:03:48+00:00"
event_direction: "up"
event_actual: 158316.0
event_previous: 158079.0
event_delta: 237.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -1.04
  mdd_t7: -2.36
  volatility: 2.28
  impact_t1_pct: -0.08
  impact_t7_pct: -2.36
probabilities:
  sample_size: 34
  t1:
    up: 50.0
    down: 50.0
    median: 0.0
    mean: -0.15
    sample: 34
  t7:
    up: 55.88
    down: 44.12
    median: 1.44
    mean: 2.65
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 30
    t1:
      up: 50.0
      down: 50.0
      median: 0.0
      mean: -0.14
      sample: 30
    t7:
      up: 53.33
      down: 46.67
      median: 0.79
      mean: 2.65
      sample: 30
related_events: [{"slug": "eth-after-nfp-2026-02-06", "title": "ETH NFP Reaction (2026-02-06): T+1/T+7 Up Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}, {"slug": "eth-after-nfp-2026-01-02", "title": "2026-01-02 Nonfarm Payrolls: ETH Historical Win Rate", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}, {"slug": "eth-after-nfp-2025-12-05", "title": "ETH Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}]
chartData: [{"time": "2024-12-03", "open": 3643.74, "high": 3670.22, "low": 3504.23, "close": 3620.71}, {"time": "2024-12-04", "open": 3620.04, "high": 3895.17, "low": 3617.74, "close": 3841.33}, {"time": "2024-12-05", "open": 3840.84, "high": 3956.54, "low": 3683.42, "close": 3811.01}, {"time": "2024-12-06", "open": 3792.21, "high": 4093.17, "low": 3782.68, "close": 4005.81}, {"time": "2024-12-07", "open": 4006.03, "high": 4029.45, "low": 3974.18, "close": 4002.69}, {"time": "2024-12-08", "open": 4007.69, "high": 4018.0, "low": 3927.85, "close": 4005.7}, {"time": "2024-12-09", "open": 4006.1, "high": 4008.78, "low": 3525.23, "close": 3718.69}, {"time": "2024-12-10", "open": 3719.0, "high": 3780.75, "low": 3520.37, "close": 3631.83}, {"time": "2024-12-11", "open": 3631.28, "high": 3850.77, "low": 3567.57, "close": 3832.82}, {"time": "2024-12-12", "open": 3833.17, "high": 3987.01, "low": 3800.09, "close": 3883.1}, {"time": "2024-12-13", "open": 3883.03, "high": 3967.4, "low": 3855.02, "close": 3911.21}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2024-12-06**
- As-of date (T-1): **2026-03-11**
- Freshness age: **460 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158316.0, Previous 158079.0, Delta +237.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.15% | 34 |
| T+7 | 55.88% | 44.12% | 1.44% | 2.65% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.14% | 30 |
| T+7 | 53.33% | 46.67% | 0.79% | 2.65% | 30 |

## Historical Distribution Summary

When NFP was **UP**, ETH T+1 up probability was **50.0%** (n=30).

When NFP was **UP**, ETH T+7 up probability was **53.33%** (n=30).

Same-direction T+7 median return: **0.79%**.

For ETH, historical NFP windows show all-history T+1 up probability of 50.0% and T+7 up probability of 55.88%. When NFP printed Up versus previous, T+1 up probability was 50.0% and T+7 up probability was 53.33% across 30 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
