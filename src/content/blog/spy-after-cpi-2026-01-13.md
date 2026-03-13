---
title: "SPY CPI Win Rate (2026-01-13): Historical T+1/T+7 Probability"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-01-13"
asof_date: "2026-03-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 14.96
robust_score: 8.96
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 100
sample_size: 40
freshness_days: 58
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 0.21
hub_baseline_median_t7: 0.51
hub_baseline_std_t7: 1.714
hub_baseline_delta: -2.84
z_score_t7: -1.48
percentile_t7: 15.79
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/spy-after-cpi-2026-01-13"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "up"
event_actual: 326.588
event_previous: 326.031
event_delta: 0.557
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -10.0
  mdd_t7: -2.33
  volatility: 14.77
  impact_t1_pct: -0.49
  impact_t7_pct: -2.33
probabilities:
  sample_size: 40
  t1:
    up: 62.5
    down: 37.5
    median: 0.14
    mean: 0.16
    sample: 40
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
      up: 61.54
      down: 38.46
      median: 0.13
      mean: 0.16
      sample: 39
    t7:
      up: 68.42
      down: 31.58
      median: 0.51
      mean: 0.21
      sample: 38
related_events: [{"slug": "spy-after-cpi-2026-02-13", "title": "SPY After CPI (2026-02-13): Historical T+1/T+7 Probability", "event_date": "2026-02-13", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.13, "sample_size": 0}, {"slug": "spy-after-cpi-2026-02-12", "title": "SPY After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 0.47, "sample_size": 0}, {"slug": "spy-after-cpi-2025-12-18", "title": "SPY After CPI (2025-12-18): Historical T+1/T+7 Probability", "event_date": "2025-12-18", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.35, "sample_size": 0}]
chartData: [{"time": "2026-01-12", "open": 690.68, "high": 696.09, "low": 690.63, "close": 695.16}, {"time": "2026-01-13", "open": 695.49, "high": 696.09, "low": 691.35, "close": 693.77}, {"time": "2026-01-14", "open": 691.0, "high": 691.72, "low": 686.04, "close": 690.36}, {"time": "2026-01-15", "open": 694.57, "high": 695.45, "low": 691.25, "close": 692.24}, {"time": "2026-01-16", "open": 693.66, "high": 694.25, "low": 690.1, "close": 691.66}, {"time": "2026-01-20", "open": 681.49, "high": 684.77, "low": 676.57, "close": 677.58}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2026-01-13**
- As-of date (T-1): **2026-03-12**
- Freshness age: **58 days**
- Sample size (all-history): **40**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.588, Previous 326.031, Delta +0.5570)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 62.5% | 37.5% | 0.14% | 0.16% | 40 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 61.54% | 38.46% | 0.13% | 0.16% | 39 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Event Outcome Interpretation

Execution quality here comes from context discipline rather than reacting to the first candle. SPY around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 326.5880 versus previous 326.0310, a delta of +0.5570. Across the full history, SPY has a T+7 up probability of 68.42% versus 31.58% down, with a median return of 0.51%. When only matching the same event direction, the T+7 up probability shifts to 68.42% across 38 comparable releases, with a same-direction median of 0.51%. The current release therefore reads as a below-baseline and fragile response rather than a collapse. The standing hub thesis for this asset-event pair is: SPY reacts to CPI through broad risk-premium repricing; downside inflation surprises often support index breadth while upside shocks compress valuation multiples.

## Distribution Position

This window is below baseline and looks fragile rather than structurally broken. The current T+7 move of -2.33% carries a z-score of -1.48 and a percentile rank of 15.79, leaving the release in the lower quartile of observed windows. That puts the event on the weak side of normal without forcing it into a full downside tail label. The important distinction is that fragile reactions can still bounce, which is why a mild underperformance should not be confused with regime failure.

## Comparison vs Hub Baseline

This comparison is below baseline, but it is still better read as fragile than catastrophic. The baseline comparison is what turns the page from observation into a repeatable checklist. The hub baseline median T+7 return is 0.51% and the current gap is -2.84%. Same-direction probability differs by +0.00% and the same-direction median differs by +0.00%. The baseline gap is large enough to matter, but not large enough to imply that the broader playbook is broken. The current regime context also matters: Sector rotation speed has accelerated in the post-tightening phase.

## Failure Modes

The failure mode here is reading a fragile window as proof of permanent weakness. The main failure mode is skipping confirmation steps because the headline feels obvious. Energy and healthcare moves can offset index-level signal clarity. Moderate underperformance often creates bounce risk, especially if rates or the dollar stop reinforcing the weak read.

## Execution Relevance

Treat this page as an execution checklist input, not a buy or sell signal. The operational takeaway is to respect the below-baseline read without assuming collapse. The checklist is Track breadth (advance/decline) with index move.; Compare rate-sensitive sectors versus defensives.; Use predefined stop distance from event range.. Fragile setups demand tighter invalidation and more patience because bounce risk is often highest when traders treat every weak release as a one-way trend.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
