---
title: "NFP Print (2025-06-06) vs SPY: Quantified Directional Odds"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-12"
title_variant_id: 4
title_template_key: "nfp_4"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-06-06"
asof_date: "2026-03-11"
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
quality_score: 60
sample_size: 34
freshness_days: 278
freshness_status: "stale"
index_tier: "B"
is_recent_90d: false
is_core_page: false
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.81
hub_baseline_median_t7: 0.11
hub_baseline_std_t7: 1.9337
hub_baseline_delta: -0.47
z_score_t7: -0.61
percentile_t7: 29.41
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/spy/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 158478.0
event_previous: 158498.0
event_delta: -20.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -0.79
  mdd_t7: -0.36
  volatility: 0.45
  impact_t1_pct: 0.09
  impact_t7_pct: -0.36
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
    direction: "down"
    sample_size: 3
    t1:
      up: 100.0
      down: 0.0
      median: 0.36
      mean: 0.66
      sample: 3
    t7:
      up: 50.0
      down: 50.0
      median: 1.06
      mean: 0.66
      sample: 4
related_events: [{"slug": "spy-after-nfp-2024-07-05", "title": "2024-07-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-07-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 7.02, "median_t7_pct": 0.11, "sample_size": 34}, {"slug": "spy-after-nfp-2024-01-05", "title": "2024-01-05 Nonfarm Payrolls: SPY Historical Win Rate", "event_date": "2024-01-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.04, "median_t7_pct": 0.11, "sample_size": 34}, {"slug": "spy-after-nfp-2024-10-04", "title": "SPY NFP Reaction (2024-10-04): T+1/T+7 Up Probability", "event_date": "2024-10-04", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 3.43, "median_t7_pct": 0.11, "sample_size": 34}]
chartData: [{"time": "2025-06-03", "open": 587.23, "high": 591.93, "low": 586.74, "close": 590.94}, {"time": "2025-06-04", "open": 591.81, "high": 592.79, "low": 590.35, "close": 590.78}, {"time": "2025-06-05", "open": 592.47, "high": 593.83, "low": 585.95, "close": 587.93}, {"time": "2025-06-06", "open": 593.49, "high": 595.64, "low": 591.71, "close": 593.97}, {"time": "2025-06-09", "open": 594.54, "high": 596.06, "low": 593.32, "close": 594.5}, {"time": "2025-06-10", "open": 595.04, "high": 598.26, "low": 593.92, "close": 597.87}, {"time": "2025-06-11", "open": 598.97, "high": 599.84, "low": 594.1, "close": 596.17}, {"time": "2025-06-12", "open": 594.83, "high": 598.54, "low": 594.34, "close": 598.54}, {"time": "2025-06-13", "open": 593.33, "high": 596.65, "low": 590.34, "close": 591.85}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
- Event date: **2025-06-06**
- As-of date (T-1): **2026-03-11**
- Freshness age: **278 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158478.0, Previous 158498.0, Delta -20.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 47.62% | 52.38% | -0.04% | -0.1% | 21 |
| T+7 | 55.88% | 44.12% | 0.11% | 0.81% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 100.0% | 0.0% | 0.36% | 0.66% | 3 |
| T+7 | 50.0% | 50.0% | 1.06% | 0.66% | 4 |

## Historical Distribution Summary

When NFP was **DOWN**, SPY T+1 up probability was **100.0%** (n=3).

When NFP was **DOWN**, SPY T+7 up probability was **50.0%** (n=4).

Same-direction T+7 median return: **1.06%**.

For SPY, historical NFP windows show all-history T+1 up probability of 47.62% and T+7 up probability of 55.88%. When NFP printed Down versus previous, T+1 up probability was 100.0% and T+7 up probability was 50.0% across 3 matched cases. Current classification is Neutral; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
