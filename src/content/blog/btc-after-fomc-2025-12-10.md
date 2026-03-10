---
title: "Fed Decision (2025-12-10) and BTC: Event-Driven Odds"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-12-10"
asof_date: "2026-03-09"
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
freshness_days: 89
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: -0.7
hub_baseline_median_t7: -2.38
hub_baseline_std_t7: 9.162
hub_baseline_delta: -4.01
z_score_t7: -0.62
percentile_t7: 30.43
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/btc-after-fomc-2025-12-10"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "flat"
event_actual: 4.0
event_previous: 4.0
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -0.92
  mdd_t7: -6.39
  volatility: 6.92
  impact_t1_pct: 0.53
  impact_t7_pct: -6.39
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
related_events: [{"slug": "btc-after-fomc-2024-04-30", "title": "BTC After FOMC (2024-04-30): Historical Signal & Probability", "event_date": "2024-04-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 5.37, "median_t7_pct": -2.38, "sample_size": 23}, {"slug": "btc-after-fomc-2024-01-30", "title": "BTC Post-FOMC Reaction (2024-01-30): Quant Backtest Snapshot", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.97, "median_t7_pct": -2.38, "sample_size": 23}, {"slug": "btc-after-fomc-2026-01-28", "title": "FOMC Outcome (2026-01-28) for BTC: Up/Down Probability View", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -2.38, "sample_size": 23}]
chartData: [{"time": "2025-12-07", "open": 89277.81, "high": 91740.84, "low": 87799.56, "close": 90405.64}, {"time": "2025-12-08", "open": 90424.59, "high": 92267.12, "low": 89644.89, "close": 90640.2}, {"time": "2025-12-09", "open": 90639.7, "high": 94601.57, "low": 89586.98, "close": 92691.71}, {"time": "2025-12-10", "open": 92695.23, "high": 94477.16, "low": 91640.13, "close": 92020.95}, {"time": "2025-12-11", "open": 92011.3, "high": 93554.27, "low": 89335.3, "close": 92511.34}, {"time": "2025-12-12", "open": 92513.66, "high": 92747.93, "low": 89532.6, "close": 90270.41}, {"time": "2025-12-13", "open": 90257.8, "high": 90647.57, "low": 89800.99, "close": 90298.71}, {"time": "2025-12-14", "open": 90296.44, "high": 90498.11, "low": 87634.94, "close": 88175.18}, {"time": "2025-12-15", "open": 88171.08, "high": 89983.92, "low": 85304.08, "close": 86419.78}, {"time": "2025-12-16", "open": 86424.41, "high": 88170.09, "low": 85381.69, "close": 87843.98}, {"time": "2025-12-17", "open": 87847.62, "high": 90264.57, "low": 85316.27, "close": 86143.76}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2025-12-10**
- As-of date (T-1): **2026-03-09**
- Freshness age: **89 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.0, Previous 4.0, Delta +0.0000)
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

The useful signal is where this release sits inside the historical range, not the headline in isolation. BTC around FOMC is best framed through how the release landed unchanged versus the previous release. The current observation shows actual value 4.0000 versus previous 4.0000, a delta of +0.0000. Across the full history, BTC has a T+7 up probability of 43.48% versus 56.52% down, with a median return of -2.38%. When only matching the same event direction, the T+7 up probability shifts to 47.06% across 17 comparable releases, with a same-direction median of -2.38%. The current release therefore reads as a below-baseline and fragile response rather than a collapse. The standing hub thesis for this asset-event pair is: BTC tends to price the path of liquidity and real yields around FOMC, and the press-conference tone often dominates the initial statement reaction. The strongest setups appear when policy language, dot-plot implications...

## Distribution Position

This window is below baseline and looks fragile rather than structurally broken. The current T+7 move of -6.39% carries a z-score of -0.62 and a percentile rank of 30.43, leaving the release in the central band of observed windows. That puts the event on the weak side of normal without forcing it into a full downside tail label. The important distinction is that fragile reactions can still bounce, which is why a mild underperformance should not be confused with regime failure.

## Comparison vs Hub Baseline

This comparison is below baseline, but it is still better read as fragile than catastrophic. Relative to the hub baseline, this release can be located with a concrete distance from normal behavior. The hub baseline median T+7 return is -2.38% and the current gap is -4.01%. Same-direction probability differs by +3.58% and the same-direction median differs by +0.00%. The baseline gap is large enough to matter, but not large enough to imply that the broader playbook is broken. The current regime context also matters: Rate-path sensitivity has increased versus the headline policy-rate level, especially after ETF-driven participation expanded macro crossover flow. Markets now reprice expected cuts and real-yield trajectory faster than...

## Failure Modes

The failure mode here is reading a fragile window as proof of permanent weakness. The main failure mode is forgetting that distributions absorb noise before they change shape. Whipsaw risk is highest between statement release and Powell Q&A, where a second narrative can reverse the first move. Funding-rate extremes, thin liquidity in correlated alt markets, and sudden bond-volatility spikes can magnify false breakouts during this window. Moderate underperformance often creates bounce risk, especially if rates or the dollar stop reinforcing the weak read.

## Execution Relevance

Use this page as a distribution map, not a shortcut to conviction. The operational takeaway is to respect the below-baseline read without assuming collapse. The checklist is Map expected policy path versus futures pricing pre-event.; Wait for confirmation after press conference starts.; Scale entries in multiple tranches, not one fill.. Fragile setups demand tighter invalidation and more patience because bounce risk is often highest when traders treat every weak release as a one-way trend.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
