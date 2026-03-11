---
title: "Fed Decision (2026-01-28) and SPY: Event-Driven Odds"
description: "Historical probability profile for SPY around FOMC events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2026-01-28"
asof_date: "2026-03-10"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 5.91
robust_score: 5.91
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 23
freshness_days: 41
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 0.26
hub_baseline_median_t7: 0.54
hub_baseline_std_t7: 1.9274
hub_baseline_delta: -1.87
z_score_t7: -0.82
percentile_t7: 26.09
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/spy-after-fomc-2026-01-28"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "flat"
event_actual: 3.75
event_previous: 3.75
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.17
  mdd_t7: -1.33
  volatility: 1.13
  impact_t1_pct: -0.2
  impact_t7_pct: -1.33
probabilities:
  sample_size: 23
  t1:
    up: 52.17
    down: 47.83
    median: 0.1
    mean: -0.02
    sample: 23
  t7:
    up: 56.52
    down: 43.48
    median: 0.54
    mean: 0.26
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 17
    t1:
      up: 47.06
      down: 52.94
      median: -0.2
      mean: -0.08
      sample: 17
    t7:
      up: 64.71
      down: 35.29
      median: 0.57
      mean: 0.48
      sample: 17
related_events: [{"slug": "spy-after-fomc-2025-01-29", "title": "Fed Decision (2025-01-29) and SPY: Event-Driven Odds", "event_date": "2025-01-29", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 9.47, "median_t7_pct": 0.54, "sample_size": 23}, {"slug": "spy-after-fomc-2024-03-19", "title": "SPY After FOMC (2024-03-19): Historical Signal & Probability", "event_date": "2024-03-19", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 7.7, "median_t7_pct": 0.54, "sample_size": 23}, {"slug": "spy-after-fomc-2024-01-30", "title": "Fed Decision (2024-01-30) and SPY: Event-Driven Odds", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.69, "median_t7_pct": 0.54, "sample_size": 23}]
chartData: [{"time": "2026-01-26", "open": 690.49, "high": 694.13, "low": 689.92, "close": 692.73}, {"time": "2026-01-27", "open": 694.18, "high": 696.53, "low": 693.57, "close": 695.49}, {"time": "2026-01-28", "open": 697.05, "high": 697.84, "low": 693.94, "close": 695.42}, {"time": "2026-01-29", "open": 696.39, "high": 697.06, "low": 684.83, "close": 694.04}, {"time": "2026-01-30", "open": 691.79, "high": 694.21, "low": 687.12, "close": 691.97}, {"time": "2026-02-02", "open": 689.58, "high": 696.93, "low": 689.42, "close": 695.41}, {"time": "2026-02-03", "open": 696.21, "high": 696.96, "low": 684.03, "close": 689.53}, {"time": "2026-02-04", "open": 690.35, "high": 691.45, "low": 681.76, "close": 686.19}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **SPY**
- Event date: **2026-01-28**
- As-of date (T-1): **2026-03-10**
- Freshness age: **41 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 3.75, Previous 3.75, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 52.17% | 47.83% | 0.1% | -0.02% | 23 |
| T+7 | 56.52% | 43.48% | 0.54% | 0.26% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 47.06% | 52.94% | -0.2% | -0.08% | 17 |
| T+7 | 64.71% | 35.29% | 0.57% | 0.48% | 17 |

## Event Outcome Interpretation

The useful signal is where this release sits inside the historical range, not the headline in isolation. SPY around FOMC is best framed through how the release landed unchanged versus the previous release. The current observation shows actual value 3.7500 versus previous 3.7500, a delta of +0.0000. Across the full history, SPY has a T+7 up probability of 56.52% versus 43.48% down, with a median return of 0.54%. When only matching the same event direction, the T+7 up probability shifts to 64.71% across 17 comparable releases, with a same-direction median of 0.57%. The current release therefore reads as a below-baseline and fragile response rather than a collapse. The standing hub thesis for this asset-event pair is: The S&P 500's reaction to FOMC rate decisions is heavily dictated by the preceding 30-day index trajectory. A 'buy the rumor, sell the fact' dynamic dominates when equities enter the meeting at all-time highs. Conversel...

## Distribution Position

This window is below baseline and looks fragile rather than structurally broken. The current T+7 move of -1.33% carries a z-score of -0.82 and a percentile rank of 26.09, leaving the release in the central band of observed windows. That puts the event on the weak side of normal without forcing it into a full downside tail label. The important distinction is that fragile reactions can still bounce, which is why a mild underperformance should not be confused with regime failure.

## Comparison vs Hub Baseline

This comparison is below baseline, but it is still better read as fragile than catastrophic. Relative to the hub baseline, this release can be located with a concrete distance from normal behavior. The hub baseline median T+7 return is 0.54% and the current gap is -1.87%. Same-direction probability differs by +8.19% and the same-direction median differs by +0.03%. The baseline gap is large enough to matter, but not large enough to imply that the broader playbook is broken. The current regime context also matters: The market's focal point has pivoted from terminal rate pricing to the trajectory of quantitative tightening (QT) tapering.

## Failure Modes

The failure mode here is reading a fragile window as proof of permanent weakness. The main failure mode is forgetting that distributions absorb noise before they change shape. Jerome Powell's press conference (30 minutes post-release) frequently reverses the initial algorithmic reaction, especially when the statement appears neutral but the Q&A shifts the market's view of cuts, QT tapering, or growth sensitivity. Breadth deterioration under an index-level bounce is a common warning that the first move is failing. Moderate underperformance often creates bounce risk, especially if rates or the dollar stop reinforcing the weak read.

## Execution Relevance

Use this page as a distribution map, not a shortcut to conviction. The operational takeaway is to respect the below-baseline read without assuming collapse. The checklist is Hedge long portfolios with short-dated VIX call options 24h prior.; Avoid initiating 0DTE (Zero Days to Expiration) option strategies during the first 15 minutes of the release.; Analyze the initial sector rotation (e.g., Tech vs. Utilities) for duration risk clues.. Fragile setups demand tighter invalidation and more patience because bounce risk is often highest when traders treat every weak release as a one-way trend.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
