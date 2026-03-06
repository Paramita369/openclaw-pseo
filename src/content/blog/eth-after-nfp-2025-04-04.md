---
title: "ETH NFP Reaction (2025-04-04): T+1/T+7 Up Probability"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 1
title_template_key: "nfp_1"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-04-04"
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
quality_score: 70
sample_size: 13
freshness_days: 335
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 3.32
hub_baseline_median_t7: 5.12
hub_baseline_std_t7: 8.5559
hub_baseline_delta: -1.8
z_score_t7: -0.0
percentile_t7: 46.15
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 158485.0
event_previous: 158377.0
event_delta: 108.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.03
  mdd_t7: 0.0
  volatility: 3.21
  impact_t1_pct: 0.11
  impact_t7_pct: 3.32
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
chartData: [{"time": "2025-04-01", "open": 1823.56, "high": 1926.3, "low": 1820.35, "close": 1905.49}, {"time": "2025-04-02", "open": 1905.48, "high": 1951.18, "low": 1782.76, "close": 1795.31}, {"time": "2025-04-03", "open": 1794.98, "high": 1844.07, "low": 1751.38, "close": 1815.64}, {"time": "2025-04-04", "open": 1815.61, "high": 1833.96, "low": 1760.59, "close": 1815.34}, {"time": "2025-04-05", "open": 1815.34, "high": 1826.3, "low": 1767.51, "close": 1805.97}, {"time": "2025-04-06", "open": 1805.96, "high": 1815.57, "low": 1539.44, "close": 1576.73}, {"time": "2025-04-07", "open": 1576.95, "high": 1634.04, "low": 1415.37, "close": 1555.24}, {"time": "2025-04-08", "open": 1554.93, "high": 1617.34, "low": 1447.61, "close": 1472.55}, {"time": "2025-04-09", "open": 1472.6, "high": 1687.19, "low": 1386.8, "close": 1668.04}, {"time": "2025-04-10", "open": 1668.2, "high": 1669.39, "low": 1474.91, "close": 1522.52}, {"time": "2025-04-11", "open": 1522.47, "high": 1587.54, "low": 1505.0, "close": 1567.15}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2025-04-04**
- As-of date (T-1): **2026-03-05**
- Freshness age: **335 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 158485.0, Previous 158377.0, Delta +108.0000)
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
