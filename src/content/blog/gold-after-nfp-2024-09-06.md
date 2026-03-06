---
title: "GOLD Post-NFP Setup (2024-09-06): Historical Probability Lens"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-09-06"
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
quality_score: 50
sample_size: 13
freshness_days: 545
freshness_status: "stale"
index_tier: "C"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 1.14
hub_baseline_median_t7: 1.07
hub_baseline_std_t7: 1.6215
hub_baseline_delta: 2.45
z_score_t7: 1.47
percentile_t7: 92.31
narrative_trigger: "extreme_outperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "positive"
canonical_target: "none"
canonical_url: ""
robots_directive: "noindex,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 157912.0
event_previous: 157757.0
event_delta: 155.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.09
  mdd_t7: -6.54
  volatility: 3.52
  impact_t1_pct: 0.0
  impact_t7_pct: 3.52
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
related_events: [{"slug": "gold-after-nfp-2024-03-01", "title": "GOLD NFP Reaction (2024-03-01): T+1/T+7 Up Probability", "event_date": "2024-03-01", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.57, "median_t7_pct": 1.07, "sample_size": 13}, {"slug": "gold-after-nfp-2024-04-05", "title": "NFP Print (2024-04-05) vs GOLD: Quantified Directional Odds", "event_date": "2024-04-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 4.16, "median_t7_pct": 1.07, "sample_size": 13}, {"slug": "gold-after-nfp-2026-02-06", "title": "GOLD NFP Reaction (2026-02-06): T+1/T+7 Up Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.07, "sample_size": 13}]
chartData: [{"time": "2024-09-03", "open": 2501.6, "high": 2501.8, "low": 2476.3, "close": 2489.9}, {"time": "2024-09-04", "open": 2490.9, "high": 2493.4, "low": 2483.5, "close": 2493.4}, {"time": "2024-09-05", "open": 2493.7, "high": 2513.3, "low": 2493.4, "close": 2511.4}, {"time": "2024-09-06", "open": 2510.3, "high": 2517.9, "low": 2483.7, "close": 2493.5}, {"time": "2024-09-09", "open": 2491.3, "high": 2504.7, "low": 2491.3, "close": 2501.8}, {"time": "2024-09-10", "open": 2512.3, "high": 2512.3, "low": 2512.3, "close": 2512.3}, {"time": "2024-09-11", "open": 2525.8, "high": 2525.8, "low": 2502.3, "close": 2512.1}, {"time": "2024-09-12", "open": 2529.1, "high": 2557.0, "low": 2523.4, "close": 2551.2}, {"time": "2024-09-13", "open": 2568.8, "high": 2581.8, "low": 2565.0, "close": 2581.3}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
- Event date: **2024-09-06**
- As-of date (T-1): **2026-03-05**
- Freshness age: **545 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 157912.0, Previous 157757.0, Delta +155.0000)
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
