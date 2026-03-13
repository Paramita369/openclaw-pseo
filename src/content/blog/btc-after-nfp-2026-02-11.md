---
title: "BTC After NFP (2026-02-11): Event Probability and Median Return"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 3
title_template_key: "nfp_3"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-02-11"
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
freshness_days: 29
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 1.66
hub_baseline_median_t7: 1.02
hub_baseline_std_t7: 5.3301
hub_baseline_delta: -1.87
z_score_t7: -0.47
percentile_t7: 31.43
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/btc-after-nfp-2026-02-11"
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
  sharpe_t7: -0.89
  mdd_t7: -4.79
  volatility: 80.17
  impact_t1_pct: -1.15
  impact_t7_pct: -0.85
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
chartData: [{"time": "2026-02-08", "open": 69283.73, "high": 72206.91, "low": 68852.9, "close": 70264.73}, {"time": "2026-02-09", "open": 70243.33, "high": 71369.97, "low": 68291.03, "close": 70120.78}, {"time": "2026-02-10", "open": 70137.39, "high": 70464.27, "low": 67913.09, "close": 68793.96}, {"time": "2026-02-11", "open": 68791.86, "high": 69242.68, "low": 65757.3, "close": 66991.97}, {"time": "2026-02-12", "open": 66992.2, "high": 68339.49, "low": 65092.11, "close": 66221.84}, {"time": "2026-02-13", "open": 66213.38, "high": 69382.84, "low": 65835.78, "close": 68857.84}, {"time": "2026-02-14", "open": 68856.98, "high": 70481.16, "low": 68706.62, "close": 69767.62}, {"time": "2026-02-15", "open": 69764.95, "high": 70939.29, "low": 68052.55, "close": 68788.19}, {"time": "2026-02-16", "open": 68782.4, "high": 70067.23, "low": 67301.59, "close": 68843.16}, {"time": "2026-02-17", "open": 68843.09, "high": 69201.87, "low": 66615.28, "close": 67494.22}, {"time": "2026-02-18", "open": 67488.02, "high": 68434.43, "low": 65845.9, "close": 66425.32}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2026-02-11**
- As-of date (T-1): **2026-03-12**
- Freshness age: **29 days**
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

This event should be read as a distribution problem, not a headline-only trade. BTC around NFP is best framed through how the release landed lower than the previous release. The current observation shows actual value 158466.0000 versus previous 158558.0000, a delta of -92.0000. Across the full history, BTC has a T+7 up probability of 60.00% versus 40.00% down, with a median return of 1.02%. When only matching the same event direction, the T+7 up probability shifts to 55.56% across 9 comparable releases, with a same-direction median of 0.99%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: BTC often responds to payroll surprises through USD liquidity expectations rather than labor data itself. The first reaction is usually a rates-and-dollar impulse, while directional follow-through depends on whether the...

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of -0.85% carries a z-score of -0.47 and a percentile rank of 31.43, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. Against the hub baseline for this asset-event pair, the current print is measurable rather than anecdotal. The hub baseline median T+7 return is 1.02% and the current gap is -1.87%. Same-direction probability moves by -4.44% and the same-direction median differs by -0.03%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Post-ETF positioning has reduced immediate panic selling on routine NFP beats, but reaction speed has increased because macro desks and crypto venues now arbitrage the rates signal faster. This shortens the useful decis...

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is confusing distribution evidence with certainty. A sharp DXY spike can override crypto-specific momentum in the first hour, even when crypto order flow initially looks constructive. Revisions, wages, and unemployment-rate cross-signals can also flip the headline interpretation and invalidate the first impulse. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Use this page as an educational operating lens, not a trading instruction. The operational takeaway is calibration, not escalation. The checklist remains Track DXY and US2Y move in the first 15 minutes.; Avoid full-size entries before volatility normalizes.; Use stop placement outside event candle extremes.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
