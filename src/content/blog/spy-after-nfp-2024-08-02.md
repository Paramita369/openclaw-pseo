---
title: "NFP Print (2024-08-02) vs SPY: Quantified Directional Odds"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 4
title_template_key: "nfp_4"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-08-02"
asof_date: "2026-03-09"
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
freshness_days: 584
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 0.81
hub_baseline_median_t7: 0.11
hub_baseline_std_t7: 1.9337
hub_baseline_delta: -0.09
z_score_t7: -0.41
percentile_t7: 47.06
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 157757.0
event_previous: 157748.0
event_delta: 9.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 2.25
  mdd_t7: -4.25
  volatility: 0.12
  impact_t1_pct: -0.1
  impact_t7_pct: 0.02
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
related_events: [{"slug": "spy-after-nfp-2024-07-05", "title": "2024-07-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-07-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.02, "median_t7_pct": 0.11, "sample_size": 34}, {"slug": "spy-after-nfp-2024-01-05", "title": "2024-01-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-01-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.04, "median_t7_pct": 0.11, "sample_size": 34}, {"slug": "spy-after-nfp-2024-10-04", "title": "SPY NFP Reaction (2024-10-04): T+1/T+7 Up Probability", "event_date": "2024-10-04", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.43, "median_t7_pct": 0.11, "sample_size": 34}]
chartData: [{"time": "2024-07-30", "open": 536.46, "high": 537.52, "low": 528.86, "close": 532.28}, {"time": "2024-07-31", "open": 539.13, "high": 543.57, "low": 537.76, "close": 540.93}, {"time": "2024-08-01", "open": 542.66, "high": 544.92, "low": 529.76, "close": 533.27}, {"time": "2024-08-02", "open": 526.14, "high": 527.36, "low": 519.12, "close": 523.34}, {"time": "2024-08-05", "open": 502.46, "high": 514.19, "low": 501.12, "close": 508.1}, {"time": "2024-08-06", "open": 509.91, "high": 520.25, "low": 508.58, "close": 512.79}, {"time": "2024-08-07", "open": 518.99, "high": 522.06, "low": 508.76, "close": 509.36}, {"time": "2024-08-08", "open": 514.51, "high": 521.76, "low": 512.48, "close": 521.13}, {"time": "2024-08-09", "open": 520.31, "high": 524.92, "low": 519.08, "close": 523.43}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2024-08-02**
- As-of date (T-1): **2026-03-09**
- Freshness age: **584 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 157757.0, Previous 157748.0, Delta +9.0000)
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
