---
title: "ETH NFP Reaction (2024-05-03): T+1/T+7 Up Probability"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 1
title_template_key: "nfp_1"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-05-03"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Bullish"
raw_signal_score: 8.93
robust_score: 2.93
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 13
freshness_days: 671
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 3.32
hub_baseline_median_t7: 5.12
hub_baseline_std_t7: 8.5559
hub_baseline_delta: -11.36
z_score_t7: -1.12
percentile_t7: 15.38
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 157608.0
event_previous: 157530.0
event_delta: 78.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -0.93
  mdd_t7: -6.24
  volatility: 6.69
  impact_t1_pct: 0.45
  impact_t7_pct: -6.24
probabilities:
  sample_size: 13
  t1:
    up: 53.85
    down: 46.15
    median: 0.03
    mean: 0.11
    sample: 13
  t7:
    up: 61.54
    down: 38.46
    median: 5.12
    mean: 3.32
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 12
    t1:
      up: 50.0
      down: 50.0
      median: -0.03
      mean: 0.09
      sample: 12
    t7:
      up: 58.33
      down: 41.67
      median: 3.01
      mean: 3.07
      sample: 12
related_events: [{"slug": "eth-after-nfp-2026-02-06", "title": "ETH NFP Reaction (2026-02-06): T+1/T+7 Up Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 5.12, "sample_size": 13}, {"slug": "eth-after-nfp-2026-01-02", "title": "2026-01-02 Nonfarm Payrolls: ETH Historical Win Rate", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 5.12, "sample_size": 13}, {"slug": "eth-after-nfp-2025-12-05", "title": "ETH Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 5.12, "sample_size": 13}]
chartData: [{"time": "2024-04-30", "open": 3215.38, "high": 3249.38, "low": 2918.23, "close": 3012.29}, {"time": "2024-05-01", "open": 3011.02, "high": 3020.17, "low": 2815.92, "close": 2969.78}, {"time": "2024-05-02", "open": 2969.79, "high": 3015.05, "low": 2894.33, "close": 2988.17}, {"time": "2024-05-03", "open": 2988.13, "high": 3127.16, "low": 2960.18, "close": 3103.54}, {"time": "2024-05-04", "open": 3103.62, "high": 3167.54, "low": 3096.27, "close": 3117.58}, {"time": "2024-05-05", "open": 3117.64, "high": 3170.06, "low": 3075.59, "close": 3137.25}, {"time": "2024-05-06", "open": 3137.51, "high": 3220.15, "low": 3048.24, "close": 3062.73}, {"time": "2024-05-07", "open": 3062.75, "high": 3129.08, "low": 3003.01, "close": 3006.58}, {"time": "2024-05-08", "open": 3006.32, "high": 3037.2, "low": 2938.47, "close": 2973.66}, {"time": "2024-05-09", "open": 2973.97, "high": 3057.96, "low": 2951.22, "close": 3036.02}, {"time": "2024-05-10", "open": 3036.23, "high": 3052.73, "low": 2881.0, "close": 2909.79}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2024-05-03**
- As-of date (T-1): **2026-03-05**
- Freshness age: **671 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 157608.0, Previous 157530.0, Delta +78.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.03% | 0.11% | 13 |
| T+7 | 61.54% | 38.46% | 5.12% | 3.32% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.03% | 0.09% | 12 |
| T+7 | 58.33% | 41.67% | 3.01% | 3.07% | 12 |

## Historical Distribution Summary

When NFP was **UP**, ETH T+1 up probability was **50.0%** (n=12).

When NFP was **UP**, ETH T+7 up probability was **58.33%** (n=12).

Same-direction T+7 median return: **3.01%**.

For ETH, historical NFP windows show all-history T+1 up probability of 53.85% and T+7 up probability of 61.54%. When NFP printed Up versus previous, T+1 up probability was 50.0% and T+7 up probability was 58.33% across 12 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
