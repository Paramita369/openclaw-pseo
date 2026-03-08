---
title: "Fed Decision (2026-01-28) and ETH: Event-Driven Odds"
description: "Historical probability profile for ETH around FOMC events (T+1/T+7)."
pubDate: "2026-03-08"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2026-01-28"
asof_date: "2026-03-07"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Bearish"
raw_signal_score: -13.74
robust_score: -13.74
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 23
freshness_days: 38
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: -2.8
hub_baseline_median_t7: -3.26
hub_baseline_std_t7: 15.0818
hub_baseline_delta: -25.45
z_score_t7: -1.72
percentile_t7: 0.0
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/eth-after-fomc-2026-01-28"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "flat"
event_actual: 3.75
event_previous: 3.75
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.28
  mdd_t7: -28.71
  volatility: 22.44
  impact_t1_pct: -6.27
  impact_t7_pct: -28.71
probabilities:
  sample_size: 23
  t1:
    up: 43.48
    down: 56.52
    median: -0.1
    mean: 0.91
    sample: 23
  t7:
    up: 30.43
    down: 69.57
    median: -3.26
    mean: -2.8
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 17
    t1:
      up: 35.29
      down: 64.71
      median: -1.41
      mean: 0.94
      sample: 17
    t7:
      up: 29.41
      down: 70.59
      median: -3.26
      mean: -1.88
      sample: 17
related_events: [{"slug": "eth-after-fomc-2024-01-30", "title": "ETH Post-FOMC Reaction (2024-01-30): Quant Backtest Snapshot", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 3.74, "median_t7_pct": -0.19, "sample_size": 9}, {"slug": "eth-after-fomc-2025-12-10", "title": "2025-12-10 FOMC Meeting: ETH T+1/T+7 Probability Profile", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.19, "sample_size": 9}, {"slug": "eth-after-fomc-2025-10-29", "title": "ETH After FOMC (2025-10-29): Historical Signal & Probability", "event_date": "2025-10-29", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.19, "sample_size": 9}]
chartData: [{"time": "2026-01-25", "open": 2948.53, "high": 2955.02, "low": 2785.9, "close": 2815.9}, {"time": "2026-01-26", "open": 2815.77, "high": 2946.0, "low": 2811.07, "close": 2926.46}, {"time": "2026-01-27", "open": 2926.2, "high": 3031.04, "low": 2898.31, "close": 3022.21}, {"time": "2026-01-28", "open": 3022.24, "high": 3040.72, "low": 2981.59, "close": 3006.61}, {"time": "2026-01-29", "open": 3006.26, "high": 3008.04, "low": 2751.65, "close": 2818.23}, {"time": "2026-01-30", "open": 2818.14, "high": 2823.91, "low": 2633.84, "close": 2702.38}, {"time": "2026-01-31", "open": 2702.3, "high": 2709.53, "low": 2248.7, "close": 2445.09}, {"time": "2026-02-01", "open": 2445.07, "high": 2472.65, "low": 2224.12, "close": 2267.96}, {"time": "2026-02-02", "open": 2267.56, "high": 2393.06, "low": 2158.94, "close": 2344.36}, {"time": "2026-02-03", "open": 2344.45, "high": 2357.21, "low": 2109.06, "close": 2227.56}, {"time": "2026-02-04", "open": 2227.97, "high": 2291.13, "low": 2074.1, "close": 2143.5}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **ETH**
- Event date: **2026-01-28**
- As-of date (T-1): **2026-03-07**
- Freshness age: **38 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 3.75, Previous 3.75, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 43.48% | 56.52% | -0.1% | 0.91% | 23 |
| T+7 | 30.43% | 69.57% | -3.26% | -2.8% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 35.29% | 64.71% | -1.41% | 0.94% | 17 |
| T+7 | 29.41% | 70.59% | -3.26% | -1.88% | 17 |

## Event Outcome Interpretation

Execution quality here comes from context discipline rather than reacting to the first candle. ETH around FOMC is best framed through how the release landed unchanged versus the previous release. The current observation shows actual value 3.7500 versus previous 3.7500, a delta of +0.0000. Across the full history, ETH has a T+7 up probability of 30.43% versus 69.57% down, with a median return of -3.26%. When only matching the same event direction, the T+7 up probability shifts to 29.41% across 17 comparable releases, with a same-direction median of -3.26%. The current release therefore belongs to the downside tail and should be treated as materially weak. The standing hub thesis for this asset-event pair is: ETH tends to inherit macro direction from rate expectations, but relative performance improves when policy uncertainty falls and volatility compresses.

## Distribution Position

This window sits in the weak tail and should be classified as a downside tail event for ETH after FOMC. The current T+7 move of -28.71% carries a z-score of -1.72 and a percentile rank of 0.00, which pushes the release into the weakest decile of observed windows and away from ordinary downside noise. That makes this an extreme negative deviation rather than a routine weak print, so the page should be read with explicit downside-tail caution.

## Comparison vs Hub Baseline

This comparison is materially below baseline and should be treated as a true downside-tail gap. The baseline comparison is what turns the page from observation into a repeatable checklist. The hub baseline median T+7 return is -3.26% and the current gap is -25.45%. Same-direction probability differs by -1.02% and the same-direction median differs by +0.00%. The baseline gap is now large enough to justify a weak-tail classification and a more defensive interpretation. The current regime context also matters: Macro-to-crypto transmission is faster due to tighter cross-asset monitoring.

## Failure Modes

The failure mode here is underestimating how far a downside tail can travel before it stabilizes. The main failure mode is skipping confirmation steps because the headline feels obvious. Policy surprise can trigger correlated liquidation cascades. Invalidation needs to be tighter because weak-tail conditions can extend farther than a normal weak window.

## Execution Relevance

Treat this page as an execution checklist input, not a buy or sell signal. The operational takeaway is to respect the downside tail and accept a higher invalidation burden before assuming the move is spent. The checklist remains Track implied volatility term structure before event.; Avoid chasing first impulse candle.; Anchor exits to predefined volatility bands.. This is exactly the state where waiting for confirmation matters more than trying to fade weakness too early.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
