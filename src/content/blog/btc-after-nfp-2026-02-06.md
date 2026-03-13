---
title: "BTC Post-NFP Setup (2026-02-06): Historical Probability Lens"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-02-06"
asof_date: "2026-03-12"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 0.57
robust_score: 0.57
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
hub_baseline_mean_t7: 1.66
hub_baseline_median_t7: 1.02
hub_baseline_std_t7: 5.3301
hub_baseline_delta: -3.43
z_score_t7: -0.76
percentile_t7: 22.86
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/btc-after-nfp-2026-02-06"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "down"
event_actual: 158466.0
event_previous: 158558.0
event_delta: -92.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -10.0
  mdd_t7: -2.41
  volatility: 27.14
  impact_t1_pct: -1.8
  impact_t7_pct: -2.41
probabilities:
  sample_size: 35
  t1:
    up: 28.57
    down: 71.43
    median: -0.39
    mean: -0.29
    sample: 35
  t7:
    up: 60.0
    down: 40.0
    median: 1.02
    mean: 1.66
    sample: 35
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 9
    t1:
      up: 22.22
      down: 77.78
      median: -0.7
      mean: -0.65
      sample: 9
    t7:
      up: 55.56
      down: 44.44
      median: 0.99
      mean: 1.1
      sample: 9
related_events: [{"slug": "btc-after-nfp-2026-01-09", "title": "BTC After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 5.54, "sample_size": 0}, {"slug": "btc-after-nfp-2025-11-20", "title": "BTC After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 5.37, "sample_size": 0}, {"slug": "btc-after-nfp-2025-09-05", "title": "BTC After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.93, "sample_size": 0}]
chartData: [{"time": "2026-02-03", "open": 78693.51, "high": 79118.85, "low": 72897.14, "close": 75633.55}, {"time": "2026-02-04", "open": 75640.09, "high": 76864.66, "low": 71779.93, "close": 73019.7}, {"time": "2026-02-05", "open": 73016.38, "high": 73161.55, "low": 62353.54, "close": 62702.1}, {"time": "2026-02-06", "open": 62704.45, "high": 71681.3, "low": 60074.2, "close": 70555.39}, {"time": "2026-02-07", "open": 70553.8, "high": 71611.15, "low": 67364.45, "close": 69281.97}, {"time": "2026-02-08", "open": 69283.73, "high": 72206.91, "low": 68852.9, "close": 70264.73}, {"time": "2026-02-09", "open": 70243.33, "high": 71369.97, "low": 68291.03, "close": 70120.78}, {"time": "2026-02-10", "open": 70137.39, "high": 70464.27, "low": 67913.09, "close": 68793.96}, {"time": "2026-02-11", "open": 68791.86, "high": 69242.68, "low": 65757.3, "close": 66991.97}, {"time": "2026-02-12", "open": 66992.2, "high": 68339.49, "low": 65092.11, "close": 66221.84}, {"time": "2026-02-13", "open": 66213.38, "high": 69382.84, "low": 65835.78, "close": 68857.84}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
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
| T+1 | 28.57% | 71.43% | -0.39% | -0.29% | 35 |
| T+7 | 60.0% | 40.0% | 1.02% | 1.66% | 35 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 22.22% | 77.78% | -0.7% | -0.65% | 9 |
| T+7 | 55.56% | 44.44% | 0.99% | 1.1% | 9 |

## Event Outcome Interpretation

The useful signal is where this release sits inside the historical range, not the headline in isolation. BTC around NFP is best framed through how the release landed lower than the previous release. The current observation shows actual value 158466.0000 versus previous 158558.0000, a delta of -92.0000. Across the full history, BTC has a T+7 up probability of 60.00% versus 40.00% down, with a median return of 1.02%. When only matching the same event direction, the T+7 up probability shifts to 55.56% across 9 comparable releases, with a same-direction median of 0.99%. The current release therefore reads as a below-baseline and fragile response rather than a collapse. The standing hub thesis for this asset-event pair is: BTC often responds to payroll surprises through USD liquidity expectations rather than labor data itself. The first reaction is usually a rates-and-dollar impulse, while directional follow-through depends on whether the...

## Distribution Position

This window is below baseline and looks fragile rather than structurally broken. The current T+7 move of -2.41% carries a z-score of -0.76 and a percentile rank of 22.86, leaving the release in the lower quartile of observed windows. That puts the event on the weak side of normal without forcing it into a full downside tail label. The important distinction is that fragile reactions can still bounce, which is why a mild underperformance should not be confused with regime failure.

## Comparison vs Hub Baseline

This comparison is below baseline, but it is still better read as fragile than catastrophic. Relative to the hub baseline, this release can be located with a concrete distance from normal behavior. The hub baseline median T+7 return is 1.02% and the current gap is -3.43%. Same-direction probability differs by -4.44% and the same-direction median differs by -0.03%. The baseline gap is large enough to matter, but not large enough to imply that the broader playbook is broken. The current regime context also matters: Post-ETF positioning has reduced immediate panic selling on routine NFP beats, but reaction speed has increased because macro desks and crypto venues now arbitrage the rates signal faster. This shortens the useful decis...

## Failure Modes

The failure mode here is reading a fragile window as proof of permanent weakness. The main failure mode is forgetting that distributions absorb noise before they change shape. A sharp DXY spike can override crypto-specific momentum in the first hour, even when crypto order flow initially looks constructive. Revisions, wages, and unemployment-rate cross-signals can also flip the headline interpretation and invalidate the first impulse. Moderate underperformance often creates bounce risk, especially if rates or the dollar stop reinforcing the weak read.

## Execution Relevance

Use this page as a distribution map, not a shortcut to conviction. The operational takeaway is to respect the below-baseline read without assuming collapse. The checklist is Track DXY and US2Y move in the first 15 minutes.; Avoid full-size entries before volatility normalizes.; Use stop placement outside event candle extremes.. Fragile setups demand tighter invalidation and more patience because bounce risk is often highest when traders treat every weak release as a one-way trend.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
