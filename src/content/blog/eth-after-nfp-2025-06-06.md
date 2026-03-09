---
title: "NFP Print (2025-06-06) vs ETH: Quantified Directional Odds"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 4
title_template_key: "nfp_4"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-06-06"
asof_date: "2026-03-08"
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
quality_score: 60
sample_size: 34
freshness_days: 275
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 2.65
hub_baseline_median_t7: 1.44
hub_baseline_std_t7: 9.723
hub_baseline_delta: 2.69
z_score_t7: 0.15
percentile_t7: 58.82
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 158478.0
event_previous: 158498.0
event_delta: -20.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.93
  mdd_t7: 0.0
  volatility: 2.14
  impact_t1_pct: 1.99
  impact_t7_pct: 4.13
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
    direction: "down"
    sample_size: 4
    t1:
      up: 50.0
      down: 50.0
      median: -0.06
      mean: -0.22
      sample: 4
    t7:
      up: 75.0
      down: 25.0
      median: 5.22
      mean: 2.63
      sample: 4
related_events: [{"slug": "eth-after-nfp-2026-02-06", "title": "ETH NFP Reaction (2026-02-06): T+1/T+7 Up Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}, {"slug": "eth-after-nfp-2026-01-02", "title": "2026-01-02 Nonfarm Payrolls: ETH Historical Win Rate", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}, {"slug": "eth-after-nfp-2025-12-05", "title": "ETH Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}]
chartData: [{"time": "2025-06-03", "open": 2607.2, "high": 2652.42, "low": 2582.25, "close": 2593.28}, {"time": "2025-06-04", "open": 2593.48, "high": 2677.97, "low": 2585.74, "close": 2608.64}, {"time": "2025-06-05", "open": 2608.61, "high": 2640.6, "low": 2395.75, "close": 2416.29}, {"time": "2025-06-06", "open": 2416.46, "high": 2530.39, "low": 2387.61, "close": 2477.19}, {"time": "2025-06-07", "open": 2477.18, "high": 2543.05, "low": 2459.14, "close": 2526.51}, {"time": "2025-06-08", "open": 2526.19, "high": 2547.47, "low": 2493.92, "close": 2510.79}, {"time": "2025-06-09", "open": 2510.84, "high": 2693.81, "low": 2479.87, "close": 2681.52}, {"time": "2025-06-10", "open": 2681.29, "high": 2824.81, "low": 2658.68, "close": 2813.52}, {"time": "2025-06-11", "open": 2813.74, "high": 2877.63, "low": 2746.46, "close": 2773.53}, {"time": "2025-06-12", "open": 2773.6, "high": 2784.26, "low": 2619.97, "close": 2651.8}, {"time": "2025-06-13", "open": 2651.92, "high": 2651.92, "low": 2443.96, "close": 2579.49}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2025-06-06**
- As-of date (T-1): **2026-03-08**
- Freshness age: **275 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158478.0, Previous 158498.0, Delta -20.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.15% | 34 |
| T+7 | 55.88% | 44.12% | 1.44% | 2.65% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.06% | -0.22% | 4 |
| T+7 | 75.0% | 25.0% | 5.22% | 2.63% | 4 |

## Historical Distribution Summary

When NFP was **DOWN**, ETH T+1 up probability was **50.0%** (n=4).

When NFP was **DOWN**, ETH T+7 up probability was **75.0%** (n=4).

Same-direction T+7 median return: **5.22%**.

For ETH, historical NFP windows show all-history T+1 up probability of 50.0% and T+7 up probability of 55.88%. When NFP printed Down versus previous, T+1 up probability was 50.0% and T+7 up probability was 75.0% across 4 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
