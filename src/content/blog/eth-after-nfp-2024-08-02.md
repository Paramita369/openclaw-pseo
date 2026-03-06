---
title: "ETH NFP Reaction (2024-08-02): T+1/T+7 Up Probability"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 1
title_template_key: "nfp_1"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2024-08-02"
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
freshness_days: 580
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 3.32
hub_baseline_median_t7: 5.12
hub_baseline_std_t7: 8.5559
hub_baseline_delta: -18.06
z_score_t7: -1.9
percentile_t7: 7.69
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "up"
event_actual: 157757.0
event_previous: 157748.0
event_delta: 9.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -1.27
  mdd_t7: -12.94
  volatility: 10.17
  impact_t1_pct: -2.77
  impact_t7_pct: -12.94
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
chartData: [{"time": "2024-07-30", "open": 3320.64, "high": 3365.32, "low": 3235.76, "close": 3278.67}, {"time": "2024-07-31", "open": 3278.69, "high": 3347.64, "low": 3216.07, "close": 3231.3}, {"time": "2024-08-01", "open": 3231.25, "high": 3241.78, "low": 3078.54, "close": 3201.56}, {"time": "2024-08-02", "open": 3201.6, "high": 3214.53, "low": 2965.73, "close": 2986.01}, {"time": "2024-08-03", "open": 2985.95, "high": 3015.3, "low": 2861.18, "close": 2903.39}, {"time": "2024-08-04", "open": 2903.09, "high": 2931.47, "low": 2639.57, "close": 2686.4}, {"time": "2024-08-05", "open": 2686.03, "high": 2695.89, "low": 2122.55, "close": 2417.21}, {"time": "2024-08-06", "open": 2417.27, "high": 2553.58, "low": 2416.53, "close": 2458.72}, {"time": "2024-08-07", "open": 2458.99, "high": 2551.56, "low": 2312.17, "close": 2336.59}, {"time": "2024-08-08", "open": 2336.92, "high": 2721.95, "low": 2322.53, "close": 2683.35}, {"time": "2024-08-09", "open": 2683.72, "high": 2706.45, "low": 2555.23, "close": 2599.6}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2024-08-02**
- As-of date (T-1): **2026-03-05**
- Freshness age: **580 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 157757.0, Previous 157748.0, Delta +9.0000)
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
