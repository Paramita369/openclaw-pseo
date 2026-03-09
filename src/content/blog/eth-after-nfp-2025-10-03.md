---
title: "ETH NFP Reaction (2025-10-03): T+1/T+7 Up Probability"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 1
title_template_key: "nfp_1"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-10-03"
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
freshness_days: 156
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 2.65
hub_baseline_median_t7: 1.44
hub_baseline_std_t7: 9.723
hub_baseline_delta: -16.32
z_score_t7: -1.8
percentile_t7: 2.94
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/eth/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 158408.0
event_previous: 158548.0
event_delta: -140.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -1.04
  mdd_t7: -14.88
  volatility: 14.31
  impact_t1_pct: -0.57
  impact_t7_pct: -14.88
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
chartData: [{"time": "2025-09-30", "open": 4217.06, "high": 4238.67, "low": 4095.44, "close": 4145.96}, {"time": "2025-10-01", "open": 4146.03, "high": 4351.11, "low": 4125.54, "close": 4351.11}, {"time": "2025-10-02", "open": 4352.24, "high": 4517.67, "low": 4336.53, "close": 4487.92}, {"time": "2025-10-03", "open": 4486.93, "high": 4591.44, "low": 4431.48, "close": 4514.87}, {"time": "2025-10-04", "open": 4514.91, "high": 4519.53, "low": 4444.01, "close": 4489.2}, {"time": "2025-10-05", "open": 4489.05, "high": 4616.53, "low": 4472.14, "close": 4515.42}, {"time": "2025-10-06", "open": 4515.3, "high": 4736.21, "low": 4492.87, "close": 4687.77}, {"time": "2025-10-07", "open": 4687.71, "high": 4755.22, "low": 4443.57, "close": 4451.15}, {"time": "2025-10-08", "open": 4451.11, "high": 4556.22, "low": 4417.77, "close": 4527.65}, {"time": "2025-10-09", "open": 4526.96, "high": 4531.72, "low": 4273.56, "close": 4369.14}, {"time": "2025-10-10", "open": 4369.07, "high": 4395.57, "low": 3460.22, "close": 3843.01}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2025-10-03**
- As-of date (T-1): **2026-03-08**
- Freshness age: **156 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158408.0, Previous 158548.0, Delta -140.0000)
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
