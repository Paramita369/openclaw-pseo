---
title: "2026-02-06 Nonfarm Payrolls: QQQ Historical Win Rate"
description: "Historical probability profile for QQQ around NFP events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-02-06"
asof_date: "2026-03-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 4.73
robust_score: 4.73
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 35
freshness_days: 34
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 1.03
hub_baseline_median_t7: 0.12
hub_baseline_std_t7: 2.5414
hub_baseline_delta: -1.39
z_score_t7: -0.91
percentile_t7: 14.71
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/qqq-after-nfp-2026-02-06"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "down"
event_actual: 158466.0
event_previous: 158558.0
event_delta: -92.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -5.64
  mdd_t7: -2.02
  volatility: 18.64
  impact_t1_pct: 0.77
  impact_t7_pct: -1.27
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
    direction: "down"
    sample_size: 8
    t1:
      up: 62.5
      down: 37.5
      median: 0.45
      mean: 0.1
      sample: 8
    t7:
      up: 37.5
      down: 62.5
      median: -0.88
      mean: 0.16
      sample: 8
related_events: [{"slug": "qqq-after-nfp-2026-01-02", "title": "QQQ After NFP (2026-01-02): Historical T+1/T+7 Probability", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.21, "sample_size": 0}, {"slug": "qqq-after-nfp-2025-11-20", "title": "QQQ After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 5.73, "sample_size": 0}, {"slug": "qqq-after-nfp-2025-09-05", "title": "QQQ After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.84, "sample_size": 0}]
chartData: [{"time": "2026-02-03", "open": 628.3, "high": 629.98, "low": 610.96, "close": 616.52}, {"time": "2026-02-04", "open": 615.02, "high": 615.1, "low": 600.47, "close": 605.75}, {"time": "2026-02-05", "open": 600.21, "high": 604.81, "low": 594.76, "close": 597.03}, {"time": "2026-02-06", "open": 600.19, "high": 611.41, "low": 598.77, "close": 609.65}, {"time": "2026-02-09", "open": 607.54, "high": 616.46, "low": 605.07, "close": 614.32}, {"time": "2026-02-10", "open": 615.31, "high": 617.02, "low": 611.01, "close": 611.47}, {"time": "2026-02-11", "open": 616.38, "high": 617.52, "low": 607.69, "close": 613.11}, {"time": "2026-02-12", "open": 614.71, "high": 615.81, "low": 599.57, "close": 600.64}, {"time": "2026-02-13", "open": 600.43, "high": 606.48, "low": 596.42, "close": 601.92}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **QQQ**
- Event date: **2026-02-06**
- As-of date (T-1): **2026-03-12**
- Freshness age: **34 days**
- Sample size (all-history): **35**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158466.0, Previous 158558.0, Delta -92.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 59.09% | 40.91% | 0.18% | -0.05% | 22 |
| T+7 | 50.0% | 50.0% | 0.12% | 1.03% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 62.5% | 37.5% | 0.45% | 0.1% | 8 |
| T+7 | 37.5% | 62.5% | -0.88% | 0.16% | 8 |

## Event Outcome Interpretation

The useful signal is where this release sits inside the historical range, not the headline in isolation. QQQ around NFP is best framed through how the release landed lower than the previous release. The current observation shows actual value 158466.0000 versus previous 158558.0000, a delta of -92.0000. Across the full history, QQQ has a T+7 up probability of 50.00% versus 50.00% down, with a median return of 0.12%. When only matching the same event direction, the T+7 up probability shifts to 37.50% across 8 comparable releases, with a same-direction median of -0.88%. The current release therefore reads as a below-baseline and fragile response rather than a collapse. The standing hub thesis for this asset-event pair is: QQQ's NFP response is conditional: strong jobs can be bearish through yields, but bullish if interpreted as soft-landing without hawkish repricing.

## Distribution Position

This window is below baseline and looks fragile rather than structurally broken. The current T+7 move of -1.27% carries a z-score of -0.91 and a percentile rank of 14.71, leaving the release in the lower quartile of observed windows. That puts the event on the weak side of normal without forcing it into a full downside tail label. The important distinction is that fragile reactions can still bounce, which is why a mild underperformance should not be confused with regime failure.

## Comparison vs Hub Baseline

This comparison is below baseline, but it is still better read as fragile than catastrophic. Relative to the hub baseline, this release can be located with a concrete distance from normal behavior. The hub baseline median T+7 return is 0.12% and the current gap is -1.39%. Same-direction probability differs by -12.50% and the same-direction median differs by -1.00%. The baseline gap is large enough to matter, but not large enough to imply that the broader playbook is broken. The current regime context also matters: Market has shifted to balancing growth optimism against rate pressure.

## Failure Modes

The failure mode here is reading a fragile window as proof of permanent weakness. The main failure mode is forgetting that distributions absorb noise before they change shape. Conflicting wage and unemployment signals can increase intraday chop. Moderate underperformance often creates bounce risk, especially if rates or the dollar stop reinforcing the weak read.

## Execution Relevance

Use this page as a distribution map, not a shortcut to conviction. The operational takeaway is to respect the below-baseline read without assuming collapse. The checklist is Check average hourly earnings alongside payrolls.; Confirm direction with Nasdaq futures breadth.; Avoid oversized 0DTE exposure in first 20 minutes.. Fragile setups demand tighter invalidation and more patience because bounce risk is often highest when traders treat every weak release as a one-way trend.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
