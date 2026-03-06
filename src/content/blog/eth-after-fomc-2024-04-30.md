---
title: "2024-04-30 FOMC Meeting: ETH T+1/T+7 Probability Profile"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "fomc_3"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2024-04-30"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -3.11
robust_score: -13.11
penalties:
  sample: 4.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 9
freshness_days: 674
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: -0.1
hub_baseline_median_t7: -0.19
hub_baseline_std_t7: 12.9045
hub_baseline_delta: 0.0
z_score_t7: -0.01
percentile_t7: 55.56
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/fomc"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T00:01:00+00:00"
event_direction: "flat"
event_actual: 5.5
event_previous: 5.5
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.24
  mdd_t7: -1.41
  volatility: 1.22
  impact_t1_pct: -1.41
  impact_t7_pct: -0.19
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 1.2
    mean: 1.38
    sample: 9
  t7:
    up: 44.44
    down: 55.56
    median: -0.19
    mean: -0.1
    sample: 9
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 9
    t1:
      up: 55.56
      down: 44.44
      median: 1.2
      mean: 1.38
      sample: 9
    t7:
      up: 44.44
      down: 55.56
      median: -0.19
      mean: -0.1
      sample: 9
related_events: [{"slug": "eth-after-fomc-2024-01-30", "title": "ETH Post-FOMC Reaction (2024-01-30): Quant Backtest Snapshot", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 3.74, "median_t7_pct": -0.19, "sample_size": 9}, {"slug": "eth-after-fomc-2026-01-28", "title": "Fed Decision (2026-01-28) and ETH: Event-Driven Odds", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.19, "sample_size": 9}, {"slug": "eth-after-fomc-2025-12-10", "title": "2025-12-10 FOMC Meeting: ETH T+1/T+7 Probability Profile", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.19, "sample_size": 9}]
chartData: [{"time": "2024-04-27", "open": 3129.73, "high": 3279.45, "low": 3071.34, "close": 3252.17}, {"time": "2024-04-28", "open": 3252.25, "high": 3351.18, "low": 3249.15, "close": 3262.77}, {"time": "2024-04-29", "open": 3262.34, "high": 3285.47, "low": 3116.2, "close": 3215.43}, {"time": "2024-04-30", "open": 3215.38, "high": 3249.38, "low": 2918.23, "close": 3012.29}, {"time": "2024-05-01", "open": 3011.02, "high": 3020.17, "low": 2815.92, "close": 2969.78}, {"time": "2024-05-02", "open": 2969.79, "high": 3015.05, "low": 2894.33, "close": 2988.17}, {"time": "2024-05-03", "open": 2988.13, "high": 3127.16, "low": 2960.18, "close": 3103.54}, {"time": "2024-05-04", "open": 3103.62, "high": 3167.54, "low": 3096.27, "close": 3117.58}, {"time": "2024-05-05", "open": 3117.64, "high": 3170.06, "low": 3075.59, "close": 3137.25}, {"time": "2024-05-06", "open": 3137.51, "high": 3220.15, "low": 3048.24, "close": 3062.73}, {"time": "2024-05-07", "open": 3062.75, "high": 3129.08, "low": 3003.01, "close": 3006.58}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2024-04-30**
- As-of date (T-1): **2026-03-05**
- Freshness age: **674 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 5.5, Previous 5.5, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 1.2% | 1.38% | 9 |
| T+7 | 44.44% | 55.56% | -0.19% | -0.1% | 9 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 1.2% | 1.38% | 9 |
| T+7 | 44.44% | 55.56% | -0.19% | -0.1% | 9 |

## Historical Distribution Summary

When FOMC was **FLAT**, ETH T+1 up probability was **55.56%** (n=9).

When FOMC was **FLAT**, ETH T+7 up probability was **44.44%** (n=9).

Same-direction T+7 median return: **-0.19%**.

For ETH, historical FOMC windows show all-history T+1 up probability of 55.56% and T+7 up probability of 44.44%. When FOMC printed Flat versus previous, T+1 up probability was 55.56% and T+7 up probability was 44.44% across 9 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
