---
title: "2026-01-09 Nonfarm Payrolls: QQQ Historical Win Rate"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-01-09"
asof_date: "2026-03-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 4.73
robust_score: -1.27
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 100
sample_size: 35
freshness_days: 62
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 1.03
hub_baseline_median_t7: 0.12
hub_baseline_std_t7: 2.5414
hub_baseline_delta: -0.98
z_score_t7: -0.75
percentile_t7: 26.47
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/qqq-after-nfp-2026-01-09"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "up"
event_actual: 158558.0
event_previous: 158432.0
event_delta: 126.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -9.78
  mdd_t7: -0.94
  volatility: 7.38
  impact_t1_pct: 0.08
  impact_t7_pct: -0.86
probabilities:
  sample_size: 35
  t1:
    up: 59.09
    down: 40.91
    median: 0.18
    mean: -0.05
    sample: 22
  t7:
    up: 50.0
    down: 50.0
    median: 0.12
    mean: 1.03
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 14
    t1:
      up: 57.14
      down: 42.86
      median: 0.15
      mean: -0.14
      sample: 14
    t7:
      up: 53.85
      down: 46.15
      median: 0.57
      mean: 1.31
      sample: 26
related_events: [{"slug": "qqq-after-nfp-2026-01-02", "title": "QQQ After NFP (2026-01-02): Historical T+1/T+7 Probability", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.21, "sample_size": 0}, {"slug": "qqq-after-nfp-2025-11-20", "title": "QQQ After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 5.73, "sample_size": 0}, {"slug": "qqq-after-nfp-2025-09-05", "title": "QQQ After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.84, "sample_size": 0}]
chartData: [{"time": "2026-01-06", "open": 619.23, "high": 624.02, "low": 618.54, "close": 623.42}, {"time": "2026-01-07", "open": 623.04, "high": 627.94, "low": 622.56, "close": 624.02}, {"time": "2026-01-08", "open": 623.03, "high": 623.42, "low": 617.8, "close": 620.47}, {"time": "2026-01-09", "open": 621.41, "high": 627.89, "low": 619.06, "close": 626.65}, {"time": "2026-01-12", "open": 622.31, "high": 628.85, "low": 622.26, "close": 627.17}, {"time": "2026-01-13", "open": 627.27, "high": 629.47, "low": 623.7, "close": 626.24}, {"time": "2026-01-14", "open": 622.24, "high": 623.45, "low": 614.56, "close": 619.55}, {"time": "2026-01-15", "open": 626.6, "high": 630.0, "low": 620.75, "close": 621.78}, {"time": "2026-01-16", "open": 625.5, "high": 626.08, "low": 618.88, "close": 621.26}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2026-01-09**
- As-of date (T-1): **2026-03-12**
- Freshness age: **62 days**
- Sample size (all-history): **35**

## Event Outcome

- NFP Outcome: **UP** (Actual 158558.0, Previous 158432.0, Delta +126.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 59.09% | 40.91% | 0.18% | -0.05% | 22 |
| T+7 | 50.0% | 50.0% | 0.12% | 1.03% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 57.14% | 42.86% | 0.15% | -0.14% | 14 |
| T+7 | 53.85% | 46.15% | 0.57% | 1.31% | 26 |

## Event Outcome Interpretation

This event should be read as a distribution problem, not a headline-only trade. QQQ around NFP is best framed through how the release landed higher than the previous release. The current observation shows actual value 158558.0000 versus previous 158432.0000, a delta of +126.0000. Across the full history, QQQ has a T+7 up probability of 50.00% versus 50.00% down, with a median return of 0.12%. When only matching the same event direction, the T+7 up probability shifts to 53.85% across 14 comparable releases, with a same-direction median of 0.57%. The current release therefore reads as a below-baseline and fragile response rather than a collapse. The standing hub thesis for this asset-event pair is: QQQ's NFP response is conditional: strong jobs can be bearish through yields, but bullish if interpreted as soft-landing without hawkish repricing.

## Distribution Position

This window is below baseline and looks fragile rather than structurally broken. The current T+7 move of -0.86% carries a z-score of -0.75 and a percentile rank of 26.47, leaving the release in the central band of observed windows. That puts the event on the weak side of normal without forcing it into a full downside tail label. The important distinction is that fragile reactions can still bounce, which is why a mild underperformance should not be confused with regime failure.

## Comparison vs Hub Baseline

This comparison is below baseline, but it is still better read as fragile than catastrophic. Against the hub baseline for this asset-event pair, the current print is measurable rather than anecdotal. The hub baseline median T+7 return is 0.12% and the current gap is -0.98%. Same-direction probability differs by +3.85% and the same-direction median differs by +0.45%. The baseline gap is large enough to matter, but not large enough to imply that the broader playbook is broken. The current regime context also matters: Market has shifted to balancing growth optimism against rate pressure.

## Failure Modes

The failure mode here is reading a fragile window as proof of permanent weakness. The main failure mode is confusing distribution evidence with certainty. Conflicting wage and unemployment signals can increase intraday chop. Moderate underperformance often creates bounce risk, especially if rates or the dollar stop reinforcing the weak read.

## Execution Relevance

Use this page as an educational operating lens, not a trading instruction. The operational takeaway is to respect the below-baseline read without assuming collapse. The checklist is Check average hourly earnings alongside payrolls.; Confirm direction with Nasdaq futures breadth.; Avoid oversized 0DTE exposure in first 20 minutes.. Fragile setups demand tighter invalidation and more patience because bounce risk is often highest when traders treat every weak release as a one-way trend.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
