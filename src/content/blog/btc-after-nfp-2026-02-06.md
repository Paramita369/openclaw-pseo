---
title: "BTC Post-NFP Setup (2026-02-06): Historical Probability Lens"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-08"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-02-06"
asof_date: "2026-03-07"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 0.23
robust_score: 0.23
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 34
freshness_days: 29
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 1.55
hub_baseline_median_t7: 1.0
hub_baseline_std_t7: 5.3733
hub_baseline_delta: -3.41
z_score_t7: -0.74
percentile_t7: 23.53
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/btc-after-nfp-2026-02-06"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158627.0
event_previous: 158497.0
event_delta: 130.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -4.01
  mdd_t7: -2.41
  volatility: 0.6
  impact_t1_pct: -1.8
  impact_t7_pct: -2.41
probabilities:
  sample_size: 34
  t1:
    up: 29.41
    down: 70.59
    median: -0.33
    mean: -0.26
    sample: 34
  t7:
    up: 58.82
    down: 41.18
    median: 1.0
    mean: 1.55
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 30
    t1:
      up: 26.67
      down: 73.33
      median: -0.39
      mean: -0.31
      sample: 30
    t7:
      up: 56.67
      down: 43.33
      median: 0.81
      mean: 1.51
      sample: 30
related_events: [{"slug": "btc-after-nfp-2026-01-02", "title": "NFP Print (2026-01-02) vs BTC: Quantified Directional Odds", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.54, "sample_size": 13}, {"slug": "btc-after-nfp-2025-12-05", "title": "BTC Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.54, "sample_size": 13}, {"slug": "btc-after-nfp-2025-11-07", "title": "BTC Post-NFP Setup (2025-11-07): Historical Probability Lens", "event_date": "2025-11-07", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.54, "sample_size": 13}]
chartData: [{"time": "2026-02-03", "open": 78693.51, "high": 79118.85, "low": 72897.14, "close": 75633.55}, {"time": "2026-02-04", "open": 75640.09, "high": 76864.66, "low": 71779.93, "close": 73019.7}, {"time": "2026-02-05", "open": 73016.38, "high": 73161.55, "low": 62353.54, "close": 62702.1}, {"time": "2026-02-06", "open": 62704.45, "high": 71681.3, "low": 60074.2, "close": 70555.39}, {"time": "2026-02-07", "open": 70553.8, "high": 71611.15, "low": 67364.45, "close": 69281.97}, {"time": "2026-02-08", "open": 69283.73, "high": 72206.91, "low": 68852.9, "close": 70264.73}, {"time": "2026-02-09", "open": 70243.33, "high": 71369.97, "low": 68291.03, "close": 70120.78}, {"time": "2026-02-10", "open": 70137.39, "high": 70464.27, "low": 67913.09, "close": 68793.96}, {"time": "2026-02-11", "open": 68791.86, "high": 69242.68, "low": 65757.3, "close": 66991.97}, {"time": "2026-02-12", "open": 66992.2, "high": 68339.49, "low": 65092.11, "close": 66221.84}, {"time": "2026-02-13", "open": 66213.38, "high": 69382.84, "low": 65835.78, "close": 68857.84}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2026-02-06**
- As-of date (T-1): **2026-03-07**
- Freshness age: **29 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158627.0, Previous 158497.0, Delta +130.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 29.41% | 70.59% | -0.33% | -0.26% | 34 |
| T+7 | 58.82% | 41.18% | 1.0% | 1.55% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 26.67% | 73.33% | -0.39% | -0.31% | 30 |
| T+7 | 56.67% | 43.33% | 0.81% | 1.51% | 30 |

## Event Outcome Interpretation

The useful signal is where this release sits inside the historical range, not the headline in isolation. BTC around NFP is best framed through how the release landed higher than the previous release. The current observation shows actual value 158627.0000 versus previous 158497.0000, a delta of +130.0000. Across the full history, BTC has a T+7 up probability of 58.82% versus 41.18% down, with a median return of 1.00%. When only matching the same event direction, the T+7 up probability shifts to 56.67% across 30 comparable releases, with a same-direction median of 0.81%. The current release therefore reads as a below-baseline and fragile response rather than a collapse. The standing hub thesis for this asset-event pair is: BTC often responds to payroll surprises through USD liquidity expectations rather than labor data itself. The first reaction is usually a rates-and-dollar impulse, while directional follow-through depends on whether the...

## Distribution Position

This window is below baseline and looks fragile rather than structurally broken. The current T+7 move of -2.41% carries a z-score of -0.74 and a percentile rank of 23.53, leaving the release in the lower quartile of observed windows. That puts the event on the weak side of normal without forcing it into a full downside tail label. The important distinction is that fragile reactions can still bounce, which is why a mild underperformance should not be confused with regime failure.

## Comparison vs Hub Baseline

This comparison is below baseline, but it is still better read as fragile than catastrophic. Relative to the hub baseline, this release can be located with a concrete distance from normal behavior. The hub baseline median T+7 return is 1.00% and the current gap is -3.41%. Same-direction probability differs by -2.15% and the same-direction median differs by -0.19%. The baseline gap is large enough to matter, but not large enough to imply that the broader playbook is broken. The current regime context also matters: Post-ETF positioning has reduced immediate panic selling on routine NFP beats, but reaction speed has increased because macro desks and crypto venues now arbitrage the rates signal faster. This shortens the useful decis...

## Failure Modes

The failure mode here is reading a fragile window as proof of permanent weakness. The main failure mode is forgetting that distributions absorb noise before they change shape. A sharp DXY spike can override crypto-specific momentum in the first hour, even when crypto order flow initially looks constructive. Revisions, wages, and unemployment-rate cross-signals can also flip the headline interpretation and invalidate the first impulse. Moderate underperformance often creates bounce risk, especially if rates or the dollar stop reinforcing the weak read.

## Execution Relevance

Use this page as a distribution map, not a shortcut to conviction. The operational takeaway is to respect the below-baseline read without assuming collapse. The checklist is Track DXY and US2Y move in the first 15 minutes.; Avoid full-size entries before volatility normalizes.; Use stop placement outside event candle extremes.. Fragile setups demand tighter invalidation and more patience because bounce risk is often highest when traders treat every weak release as a one-way trend.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
