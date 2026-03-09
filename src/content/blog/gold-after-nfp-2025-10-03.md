---
title: "GOLD Post-NFP Setup (2025-10-03): Historical Probability Lens"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2025-10-03"
asof_date: "2026-03-08"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 21.71
robust_score: 15.71
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
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.61
hub_baseline_median_t7: 1.31
hub_baseline_std_t7: 1.944
hub_baseline_delta: 1.14
z_score_t7: 0.43
percentile_t7: 64.71
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "hub"
canonical_url: "https://quantmacro.vercel.app/playbooks/gold/nfp"
robots_directive: "index,follow"
in_blog_sitemap: false
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "down"
event_actual: 158408.0
event_previous: 158548.0
event_delta: -140.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 3.45
  mdd_t7: 0.0
  volatility: 0.71
  impact_t1_pct: 1.74
  impact_t7_pct: 2.45
probabilities:
  sample_size: 34
  t1:
    up: 66.67
    down: 33.33
    median: 0.5
    mean: 0.57
    sample: 21
  t7:
    up: 79.41
    down: 20.59
    median: 1.31
    mean: 1.61
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 3
    t1:
      up: 100.0
      down: 0.0
      median: 0.8
      mean: 0.94
      sample: 3
    t7:
      up: 100.0
      down: 0.0
      median: 2.59
      mean: 2.44
      sample: 4
related_events: [{"slug": "gold-after-nfp-2024-03-01", "title": "GOLD NFP Reaction (2024-03-01): T+1/T+7 Up Probability", "event_date": "2024-03-01", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 6.57, "median_t7_pct": 1.07, "sample_size": 13}, {"slug": "gold-after-nfp-2024-04-05", "title": "NFP Print (2024-04-05) vs GOLD: Quantified Directional Odds", "event_date": "2024-04-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 4.16, "median_t7_pct": 1.07, "sample_size": 13}, {"slug": "gold-after-nfp-2024-09-06", "title": "GOLD Post-NFP Setup (2024-09-06): Historical Probability Lens", "event_date": "2024-09-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 1.09, "median_t7_pct": 1.07, "sample_size": 13}]
chartData: [{"time": "2025-09-30", "open": 3827.5, "high": 3865.5, "low": 3793.4, "close": 3840.8}, {"time": "2025-10-01", "open": 3863.5, "high": 3891.9, "low": 3853.3, "close": 3867.5}, {"time": "2025-10-02", "open": 3856.2, "high": 3888.6, "low": 3823.7, "close": 3839.7}, {"time": "2025-10-03", "open": 3855.2, "high": 3886.8, "low": 3853.7, "close": 3880.8}, {"time": "2025-10-06", "open": 3931.3, "high": 3960.0, "low": 3926.8, "close": 3948.5}, {"time": "2025-10-07", "open": 3959.4, "high": 3981.5, "low": 3940.0, "close": 3976.6}, {"time": "2025-10-08", "open": 3987.2, "high": 4049.2, "low": 3987.2, "close": 4043.3}, {"time": "2025-10-09", "open": 4011.2, "high": 4046.2, "low": 3940.0, "close": 3946.3}, {"time": "2025-10-10", "open": 3957.0, "high": 4012.0, "low": 3945.5, "close": 3975.9}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
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
| T+1 | 66.67% | 33.33% | 0.5% | 0.57% | 21 |
| T+7 | 79.41% | 20.59% | 1.31% | 1.61% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 100.0% | 0.0% | 0.8% | 0.94% | 3 |
| T+7 | 100.0% | 0.0% | 2.59% | 2.44% | 4 |

## Historical Distribution Summary

When NFP was **DOWN**, GOLD T+1 up probability was **100.0%** (n=3).

When NFP was **DOWN**, GOLD T+7 up probability was **100.0%** (n=4).

Same-direction T+7 median return: **2.59%**.

For GOLD, historical NFP windows show all-history T+1 up probability of 66.67% and T+7 up probability of 79.41%. When NFP printed Down versus previous, T+1 up probability was 100.0% and T+7 up probability was 100.0% across 3 matched cases. Current classification is Bullish; this remains an educational probability lens, not investment advice.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
