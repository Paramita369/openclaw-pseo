---
title: "ETH Reaction to US CPI (2025-12-12): Quant Probability Breakdown"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-12-12"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -5.57
robust_score: -11.57
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 70
sample_size: 14
freshness_days: 83
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 0.26
hub_baseline_median_t7: -0.39
hub_baseline_std_t7: 11.002
hub_baseline_delta: 0.65
z_score_t7: 0.0
percentile_t7: 57.14
narrative_trigger: "within_historical_norm"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/eth-after-cpi-2025-12-12"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 326.031
event_previous: 325.063
event_delta: 0.968
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.33
  mdd_t7: -0.52
  volatility: 0.78
  impact_t1_pct: -0.52
  impact_t7_pct: 0.26
probabilities:
  sample_size: 14
  t1:
    up: 50.0
    down: 50.0
    median: -0.22
    mean: -0.52
    sample: 14
  t7:
    up: 42.86
    down: 57.14
    median: -0.39
    mean: 0.26
    sample: 14
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 53.85
      down: 46.15
      median: 0.66
      mean: -0.36
      sample: 13
    t7:
      up: 46.15
      down: 53.85
      median: -0.77
      mean: 0.28
      sample: 13
related_events: [{"slug": "eth-after-cpi-2024-06-12", "title": "ETH Reaction to US CPI (2024-06-12): Quant Probability Breakdown", "event_date": "2024-06-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.22, "median_t7_pct": -0.39, "sample_size": 14}, {"slug": "eth-after-cpi-2026-02-12", "title": "ETH CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.39, "sample_size": 14}, {"slug": "eth-after-cpi-2026-01-12", "title": "2026-01-12 CPI Release: ETH Directional Probability Snapshot", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.39, "sample_size": 14}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2025-12-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **83 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.031, Previous 325.063, Delta +0.9680)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.22% | -0.52% | 14 |
| T+7 | 42.86% | 57.14% | -0.39% | 0.26% | 14 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.66% | -0.36% | 13 |
| T+7 | 46.15% | 53.85% | -0.77% | 0.28% | 13 |

## Event Outcome Interpretation

The useful signal is where this release sits inside the historical range, not the headline in isolation. ETH around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 326.0310 versus previous 325.0630, a delta of +0.9680. Across the full history, ETH has a T+7 up probability of 42.86% versus 57.14% down, with a median return of -0.39%. When only matching the same event direction, the T+7 up probability shifts to 46.15% across 13 comparable releases, with a same-direction median of -0.77%. That is the immediate context behind the current neutral classification. The standing hub thesis for this asset-event pair is: ETH reacts to inflation prints through both risk appetite and crypto-beta rotation, often showing larger relative swings than BTC during regime shifts. CPI surprises can trigger an initial valuation shock, then a second...

## Distribution Position

The current T+7 reaction of 0.26% sits in the middle of its historical distribution for ETH after CPI. Its z-score is 0.00, which measures distance from the historical mean, and its percentile rank is 57.14, which shows how often prior releases were weaker than this one. That places the observation inside the central band of observed windows, not in an obvious tail bucket. That framing matters because it separates ordinary event noise from true tail behavior inside the same distribution. In practice this means the page is useful for calibration, but it does not justify upgrading a routine macro response into a regime-break narrative.

## Comparison vs Hub Baseline

Relative to the hub baseline, this release can be located with a concrete distance from normal behavior. The hub baseline median T+7 return for ETH after CPI is -0.39%, while the baseline mean is 0.26% and the baseline standard deviation is 11.0020. The current event is running at +0.65% versus the baseline median. Same-direction probability is +3.29% versus the all-history T+7 up rate, and the same-direction median differs by -0.38%. In other words, the baseline gap decides the narrative, not a cosmetic change in wording. This release is classified as within historical norm rather than handled as a generic macro template. If the current move only differed by a few basis points, the narrative would collapse back toward historical norm. The current regime context also matters: Layer-2 and ETF-adjacent narrative flows can amplify post-CPI trend continuation, especially when macro surprise aligns with existing positioning. At the same time, cross-exchange liquidity has become more synchronized...

## Failure Modes

The main failure mode is forgetting that distributions absorb a lot of noise before they change shape. Network-specific headlines and protocol news can contaminate pure macro interpretation around release windows. If USD and front-end yields diverge, ETH can print misleading first-candle direction before reverting; leverage-driven liquidations then increase realized slippage and drawdown risk. This matters because the historical distribution is built on end-of-window outcomes, not the first minute of price discovery. A release can look constructive initially, then fail once rates, the dollar, and sector breadth reprice in a different direction. That is also why low sample environments and mixed reaction functions should be handled as weaker evidence.

## Execution Relevance

Use this page as a distribution map, not a shortcut to conviction. The practical takeaway is to use the current page as a decision filter: read the release, compare it with the hub baseline, then decide whether the event is behaving like a normal CPI setup or a tail observation. For this asset-event pair, the operational checklist is: Compare ETH/BTC ratio around event open.; Confirm spot-volume participation before breakout trades.; Reduce leverage when spread volatility widens.. When the page is marked within historical norm, the right response is not automatically to trade more aggressively; it is to decide whether confirmation quality is strong enough to justify action.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
