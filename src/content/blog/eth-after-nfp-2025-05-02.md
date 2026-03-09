---
title: "ETH NFP Reaction (2025-05-02): T+1/T+7 Up Probability"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 1
title_template_key: "nfp_1"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-05-02"
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
quality_score: 90
sample_size: 34
freshness_days: 310
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 2.65
hub_baseline_median_t7: 1.44
hub_baseline_std_t7: 9.723
hub_baseline_delta: 25.85
z_score_t7: 2.53
percentile_t7: 100.0
narrative_trigger: "extreme_outperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "positive"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158498.0
event_previous: 158485.0
event_delta: 13.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 0.98
  mdd_t7: -0.48
  volatility: 27.77
  impact_t1_pct: -0.48
  impact_t7_pct: 27.29
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
chartData: [{"time": "2025-04-29", "open": 1798.91, "high": 1842.03, "low": 1782.28, "close": 1799.18}, {"time": "2025-04-30", "open": 1799.21, "high": 1816.69, "low": 1736.14, "close": 1793.78}, {"time": "2025-05-01", "open": 1794.04, "high": 1872.94, "low": 1793.15, "close": 1839.22}, {"time": "2025-05-02", "open": 1839.17, "high": 1869.53, "low": 1814.73, "close": 1842.71}, {"time": "2025-05-03", "open": 1842.72, "high": 1848.25, "low": 1812.82, "close": 1833.84}, {"time": "2025-05-04", "open": 1833.65, "high": 1850.0, "low": 1804.5, "close": 1808.59}, {"time": "2025-05-05", "open": 1808.7, "high": 1832.05, "low": 1783.31, "close": 1819.7}, {"time": "2025-05-06", "open": 1819.73, "high": 1820.8, "low": 1753.32, "close": 1815.09}, {"time": "2025-05-07", "open": 1815.02, "high": 1849.66, "low": 1788.69, "close": 1811.61}, {"time": "2025-05-08", "open": 1811.55, "high": 2222.21, "low": 1809.46, "close": 2206.51}, {"time": "2025-05-09", "open": 2206.13, "high": 2486.01, "low": 2186.05, "close": 2345.51}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2025-05-02**
- As-of date (T-1): **2026-03-08**
- Freshness age: **310 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158498.0, Previous 158485.0, Delta +13.0000)
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
