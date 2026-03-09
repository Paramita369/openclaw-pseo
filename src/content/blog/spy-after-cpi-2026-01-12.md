---
title: "US CPI (2026-01-12) and SPY: Event-Driven Return Odds"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-01-12"
asof_date: "2026-03-08"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 15.44
robust_score: 9.44
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 39
freshness_days: 55
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 0.21
hub_baseline_median_t7: 0.51
hub_baseline_std_t7: 1.714
hub_baseline_delta: -3.04
z_score_t7: -1.6
percentile_t7: 10.53
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/spy-after-cpi-2026-01-12"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 326.588
event_previous: 326.031
event_delta: 0.557
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -1.09
  mdd_t7: -2.53
  volatility: 2.33
  impact_t1_pct: -0.2
  impact_t7_pct: -2.53
probabilities:
  sample_size: 39
  t1:
    up: 64.1
    down: 35.9
    median: 0.16
    mean: 0.21
    sample: 39
  t7:
    up: 68.42
    down: 31.58
    median: 0.51
    mean: 0.21
    sample: 38
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 63.16
      down: 36.84
      median: 0.14
      mean: 0.21
      sample: 38
    t7:
      up: 68.42
      down: 31.58
      median: 0.51
      mean: 0.21
      sample: 38
related_events: [{"slug": "spy-after-cpi-2024-03-12", "title": "SPY CPI Win Rate (2024-03-12): Historical T+1/T+7 Probability", "event_date": "2024-03-12", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 3.94, "median_t7_pct": 1.08, "sample_size": 14}, {"slug": "spy-after-cpi-2024-11-14", "title": "2024-11-14 CPI Release: SPY Directional Probability Snapshot", "event_date": "2024-11-14", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.43, "median_t7_pct": 1.08, "sample_size": 14}, {"slug": "spy-after-cpi-2024-05-15", "title": "2024-05-15 CPI Release: SPY Directional Probability Snapshot", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.37, "median_t7_pct": 1.08, "sample_size": 14}]
chartData: [{"time": "2026-01-09", "open": 690.63, "high": 695.31, "low": 689.18, "close": 694.07}, {"time": "2026-01-12", "open": 690.68, "high": 696.09, "low": 690.63, "close": 695.16}, {"time": "2026-01-13", "open": 695.49, "high": 696.09, "low": 691.35, "close": 693.77}, {"time": "2026-01-14", "open": 691.0, "high": 691.72, "low": 686.04, "close": 690.36}, {"time": "2026-01-15", "open": 694.57, "high": 695.45, "low": 691.25, "close": 692.24}, {"time": "2026-01-16", "open": 693.66, "high": 694.25, "low": 690.1, "close": 691.66}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2026-01-12**
- As-of date (T-1): **2026-03-08**
- Freshness age: **55 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.588, Previous 326.031, Delta +0.5570)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 64.1% | 35.9% | 0.16% | 0.21% | 39 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 63.16% | 36.84% | 0.14% | 0.21% | 38 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Event Outcome Interpretation

Execution quality here comes from context discipline rather than reacting to the first candle. SPY around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 326.5880 versus previous 326.0310, a delta of +0.5570. Across the full history, SPY has a T+7 up probability of 68.42% versus 31.58% down, with a median return of 0.51%. When only matching the same event direction, the T+7 up probability shifts to 68.42% across 38 comparable releases, with a same-direction median of 0.51%. The current release therefore belongs to the downside tail and should be treated as materially weak. The standing hub thesis for this asset-event pair is: SPY reacts to CPI through broad risk-premium repricing; downside inflation surprises often support index breadth while upside shocks compress valuation multiples.

## Distribution Position

This window sits in the weak tail and should be classified as a downside tail event for SPY after CPI. The current T+7 move of -2.53% carries a z-score of -1.60 and a percentile rank of 10.53, which pushes the release into the lower quartile of observed windows and away from ordinary downside noise. That makes this an extreme negative deviation rather than a routine weak print, so the page should be read with explicit downside-tail caution.

## Comparison vs Hub Baseline

This comparison is materially below baseline and should be treated as a true downside-tail gap. The baseline comparison is what turns the page from observation into a repeatable checklist. The hub baseline median T+7 return is 0.51% and the current gap is -3.04%. Same-direction probability differs by +0.00% and the same-direction median differs by +0.00%. The baseline gap is now large enough to justify a weak-tail classification and a more defensive interpretation. The current regime context also matters: Sector rotation speed has accelerated in the post-tightening phase.

## Failure Modes

The failure mode here is underestimating how far a downside tail can travel before it stabilizes. The main failure mode is skipping confirmation steps because the headline feels obvious. Energy and healthcare moves can offset index-level signal clarity. Invalidation needs to be tighter because weak-tail conditions can extend farther than a normal weak window.

## Execution Relevance

Treat this page as an execution checklist input, not a buy or sell signal. The operational takeaway is to respect the downside tail and accept a higher invalidation burden before assuming the move is spent. The checklist remains Track breadth (advance/decline) with index move.; Compare rate-sensitive sectors versus defensives.; Use predefined stop distance from event range.. This is exactly the state where waiting for confirmation matters more than trying to fade weakness too early.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
