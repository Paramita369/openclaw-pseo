---
title: "2026-03-06 Nonfarm Payrolls: BTC Historical Win Rate"
description: "Historical probability profile for BTC around NFP events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-03-06"
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
quality_score: 80
sample_size: 35
freshness_days: 6
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 1.66
hub_baseline_median_t7: 1.02
hub_baseline_std_t7: 5.3301
hub_baseline_delta: 4.15
z_score_t7: 0.66
percentile_t7: 71.43
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/btc-after-nfp-2026-03-06"
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
  sharpe_t7: 0.8
  mdd_t7: -1.27
  volatility: 6.44
  impact_t1_pct: -1.27
  impact_t7_pct: 5.17
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
chartData: [{"time": "2026-03-03", "open": 68785.08, "high": 69232.89, "low": 66237.62, "close": 68293.65}, {"time": "2026-03-04", "open": 68290.56, "high": 74051.8, "low": 67437.41, "close": 72710.58}, {"time": "2026-03-05", "open": 72712.66, "high": 73555.79, "low": 70654.88, "close": 70841.12}, {"time": "2026-03-06", "open": 70842.16, "high": 71378.57, "low": 67757.82, "close": 68136.49}, {"time": "2026-03-07", "open": 68136.69, "high": 68515.16, "low": 66969.26, "close": 67272.59}, {"time": "2026-03-08", "open": 67272.5, "high": 68177.79, "low": 65639.2, "close": 65969.78}, {"time": "2026-03-09", "open": 65969.59, "high": 69474.95, "low": 65858.01, "close": 68402.38}, {"time": "2026-03-10", "open": 68402.72, "high": 71770.9, "low": 68402.72, "close": 69926.92}, {"time": "2026-03-11", "open": 69931.25, "high": 71337.66, "low": 68998.87, "close": 70204.88}, {"time": "2026-03-12", "open": 70209.77, "high": 70775.83, "low": 69230.16, "close": 70493.46}, {"time": "2026-03-13", "open": 70509.98, "high": 72017.16, "low": 70491.65, "close": 71865.4}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **BTC**
- Event date: **2026-03-06**
- As-of date (T-1): **2026-03-12**
- Freshness age: **6 days**
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

The useful signal is where this release sits inside the historical range, not the headline in isolation. BTC around NFP is best framed through how the release landed lower than the previous release. The current observation shows actual value 158466.0000 versus previous 158558.0000, a delta of -92.0000. Across the full history, BTC has a T+7 up probability of 60.00% versus 40.00% down, with a median return of 1.02%. When only matching the same event direction, the T+7 up probability shifts to 55.56% across 9 comparable releases, with a same-direction median of 0.99%. The current release therefore reads as constructive and above baseline, but not as a full regime break. The standing hub thesis for this asset-event pair is: BTC often responds to payroll surprises through USD liquidity expectations rather than labor data itself. The first reaction is usually a rates-and-dollar impulse, while directional follow-through depends on whether the...

## Distribution Position

This window is above baseline and reads as constructive, positive but not extreme. The current T+7 move of 5.17% carries a z-score of 0.66 and a percentile rank of 71.43, placing the release in the central band of observed windows. That keeps the interpretation on the stronger side of normal without pushing it into tail language. The right read is that the event behaved better than usual, but not so far beyond baseline that it should be mistaken for a structural break.

## Comparison vs Hub Baseline

This comparison is above baseline, but it remains constructive rather than extreme. Relative to the hub baseline, this release can be located with a concrete distance from normal behavior. The hub baseline median T+7 return is 1.02% and the current gap is +4.15%. Same-direction probability is -4.44% versus all-history, and the same-direction median differs by -0.03%. That is enough to mark the page as positively skewed, while still requiring cross-asset confirmation before upgrading conviction. The current regime context also matters: Post-ETF positioning has reduced immediate panic selling on routine NFP beats, but reaction speed has increased because macro desks and crypto venues now arbitrage the rates signal faster. This shortens the useful decis...

## Failure Modes

The failure mode here is over-promoting a constructive setup into a false regime break. The main failure mode is forgetting that distributions absorb noise before they change shape. A sharp DXY spike can override crypto-specific momentum in the first hour, even when crypto order flow initially looks constructive. Revisions, wages, and unemployment-rate cross-signals can also flip the headline interpretation and invalidate the first impulse. Moderate upside events often fail when secondary markets stop confirming, so the biggest mistake is ignoring the difference between above-baseline behavior and true tail behavior.

## Execution Relevance

Use this page as a distribution map, not a shortcut to conviction. The correct stance is to treat this as constructive but not extreme. The checklist is still Track DXY and US2Y move in the first 15 minutes.; Avoid full-size entries before volatility normalizes.; Use stop placement outside event candle extremes., and confirmation is still required before acting on the signal. Above-baseline pages deserve attention, but they do not eliminate the need for discipline.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
