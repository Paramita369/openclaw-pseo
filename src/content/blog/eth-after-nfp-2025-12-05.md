---
title: "ETH Post-NFP Setup (2025-12-05): Historical Probability Lens"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-12-05"
asof_date: "2026-03-12"
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
freshness_days: 97
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 2.65
hub_baseline_median_t7: 1.44
hub_baseline_std_t7: 9.723
hub_baseline_delta: 0.54
z_score_t7: -0.07
percentile_t7: 52.94
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158497.0
event_previous: 158449.0
event_delta: 48.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.36
  mdd_t7: 0.0
  volatility: 1.45
  impact_t1_pct: 0.52
  impact_t7_pct: 1.98
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
related_events: [{"slug": "eth-after-nfp-2026-02-06", "title": "ETH NFP Reaction (2026-02-06): T+1/T+7 Up Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}, {"slug": "eth-after-nfp-2026-01-02", "title": "2026-01-02 Nonfarm Payrolls: ETH Historical Win Rate", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}, {"slug": "eth-after-nfp-2025-11-07", "title": "NFP Print (2025-11-07) vs ETH: Quantified Directional Odds", "event_date": "2025-11-07", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}]
chartData: [{"time": "2025-12-02", "open": 2800.22, "high": 3032.76, "low": 2784.39, "close": 2997.94}, {"time": "2025-12-03", "open": 2997.8, "high": 3212.56, "low": 2988.14, "close": 3191.57}, {"time": "2025-12-04", "open": 3188.34, "high": 3238.56, "low": 3071.31, "close": 3134.32}, {"time": "2025-12-05", "open": 3134.36, "high": 3192.46, "low": 2989.83, "close": 3024.43}, {"time": "2025-12-06", "open": 3024.49, "high": 3067.66, "low": 3013.98, "close": 3040.21}, {"time": "2025-12-07", "open": 3040.18, "high": 3148.77, "low": 2930.65, "close": 3061.3}, {"time": "2025-12-08", "open": 3061.01, "high": 3177.87, "low": 3043.7, "close": 3125.2}, {"time": "2025-12-09", "open": 3124.94, "high": 3395.84, "low": 3092.88, "close": 3321.11}, {"time": "2025-12-10", "open": 3321.2, "high": 3446.62, "low": 3290.15, "close": 3325.39}, {"time": "2025-12-11", "open": 3324.39, "high": 3327.34, "low": 3149.03, "close": 3237.06}, {"time": "2025-12-12", "open": 3237.03, "high": 3265.37, "low": 3050.27, "close": 3084.17}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2025-12-05**
- As-of date (T-1): **2026-03-12**
- Freshness age: **97 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158497.0, Previous 158449.0, Delta +48.0000)
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
