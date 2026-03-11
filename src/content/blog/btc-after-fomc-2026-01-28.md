---
title: "FOMC Outcome (2026-01-28) for BTC: Up/Down Probability View"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 5
title_template_key: "fomc_5"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2026-01-28"
asof_date: "2026-03-10"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -4.61
robust_score: -4.61
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
hub_baseline_mean_t7: -0.7
hub_baseline_median_t7: -2.38
hub_baseline_std_t7: 9.162
hub_baseline_delta: -15.75
z_score_t7: -1.9
percentile_t7: 0.0
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/btc-after-fomc-2026-01-28"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "flat"
event_actual: 3.75
event_previous: 3.75
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.4
  mdd_t7: -18.13
  volatility: 12.94
  impact_t1_pct: -5.18
  impact_t7_pct: -18.13
probabilities:
  sample_size: 23
  t1:
    up: 52.17
    down: 47.83
    median: 0.27
    mean: -0.18
    sample: 23
  t7:
    up: 43.48
    down: 56.52
    median: -2.38
    mean: -0.7
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 17
    t1:
      up: 47.06
      down: 52.94
      median: -0.19
      mean: -0.15
      sample: 17
    t7:
      up: 47.06
      down: 52.94
      median: -2.38
      mean: -0.94
      sample: 17
related_events: [{"slug": "btc-after-fomc-2024-04-30", "title": "BTC After FOMC (2024-04-30): Historical Signal & Probability", "event_date": "2024-04-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 5.37, "median_t7_pct": -2.38, "sample_size": 23}, {"slug": "btc-after-fomc-2024-01-30", "title": "BTC Post-FOMC Reaction (2024-01-30): Quant Backtest Snapshot", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.97, "median_t7_pct": -2.38, "sample_size": 23}, {"slug": "btc-after-fomc-2025-12-10", "title": "Fed Decision (2025-12-10) and BTC: Event-Driven Odds", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -2.38, "sample_size": 23}]
chartData: [{"time": "2026-01-25", "open": 89104.77, "high": 89193.15, "low": 86003.71, "close": 86572.22}, {"time": "2026-01-26", "open": 86566.52, "high": 88743.07, "low": 86429.29, "close": 88267.14}, {"time": "2026-01-27", "open": 88257.48, "high": 89427.12, "low": 87228.92, "close": 89102.57}, {"time": "2026-01-28", "open": 89104.05, "high": 90439.29, "low": 88721.46, "close": 89184.57}, {"time": "2026-01-29", "open": 89169.85, "high": 89200.78, "low": 83250.6, "close": 84561.59}, {"time": "2026-01-30", "open": 84562.73, "high": 84602.16, "low": 81071.48, "close": 84128.66}, {"time": "2026-01-31", "open": 84126.5, "high": 84136.92, "low": 75815.88, "close": 78621.12}, {"time": "2026-02-01", "open": 78626.12, "high": 79322.61, "low": 75698.9, "close": 76974.45}, {"time": "2026-02-02", "open": 76968.88, "high": 79258.61, "low": 74551.34, "close": 78688.77}, {"time": "2026-02-03", "open": 78693.51, "high": 79118.85, "low": 72897.14, "close": 75633.55}, {"time": "2026-02-04", "open": 75640.09, "high": 76864.66, "low": 71779.93, "close": 73019.7}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
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
| T+1 | 52.17% | 47.83% | 0.27% | -0.18% | 23 |
| T+7 | 43.48% | 56.52% | -2.38% | -0.7% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 47.06% | 52.94% | -0.19% | -0.15% | 17 |
| T+7 | 47.06% | 52.94% | -2.38% | -0.94% | 17 |

## Event Outcome Interpretation

The useful signal is where this release sits inside the historical range, not the headline in isolation. BTC around FOMC is best framed through how the release landed unchanged versus the previous release. The current observation shows actual value 3.7500 versus previous 3.7500, a delta of +0.0000. Across the full history, BTC has a T+7 up probability of 43.48% versus 56.52% down, with a median return of -2.38%. When only matching the same event direction, the T+7 up probability shifts to 47.06% across 17 comparable releases, with a same-direction median of -2.38%. The current release therefore belongs to the downside tail and should be treated as materially weak. The standing hub thesis for this asset-event pair is: BTC tends to price the path of liquidity and real yields around FOMC, and the press-conference tone often dominates the initial statement reaction. The strongest setups appear when policy language, dot-plot implications...

## Distribution Position

This window sits in the weak tail and should be classified as a downside tail event for BTC after FOMC. The current T+7 move of -18.13% carries a z-score of -1.90 and a percentile rank of 0.00, which pushes the release into the weakest decile of observed windows and away from ordinary downside noise. That makes this an extreme negative deviation rather than a routine weak print, so the page should be read with explicit downside-tail caution.

## Comparison vs Hub Baseline

This comparison is materially below baseline and should be treated as a true downside-tail gap. Relative to the hub baseline, this release can be located with a concrete distance from normal behavior. The hub baseline median T+7 return is -2.38% and the current gap is -15.75%. Same-direction probability differs by +3.58% and the same-direction median differs by +0.00%. The baseline gap is now large enough to justify a weak-tail classification and a more defensive interpretation. The current regime context also matters: Rate-path sensitivity has increased versus the headline policy-rate level, especially after ETF-driven participation expanded macro crossover flow. Markets now reprice expected cuts and real-yield trajectory faster than...

## Failure Modes

The failure mode here is underestimating how far a downside tail can travel before it stabilizes. The main failure mode is forgetting that distributions absorb noise before they change shape. Whipsaw risk is highest between statement release and Powell Q&A, where a second narrative can reverse the first move. Funding-rate extremes, thin liquidity in correlated alt markets, and sudden bond-volatility spikes can magnify false breakouts during this window. Invalidation needs to be tighter because weak-tail conditions can extend farther than a normal weak window.

## Execution Relevance

Use this page as a distribution map, not a shortcut to conviction. The operational takeaway is to respect the downside tail and accept a higher invalidation burden before assuming the move is spent. The checklist remains Map expected policy path versus futures pricing pre-event.; Wait for confirmation after press conference starts.; Scale entries in multiple tranches, not one fill.. This is exactly the state where waiting for confirmation matters more than trying to fade weakness too early.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
