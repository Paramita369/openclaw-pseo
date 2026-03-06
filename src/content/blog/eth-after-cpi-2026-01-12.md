---
title: "2026-01-12 CPI Release: ETH Directional Probability Snapshot"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 4
title_template_key: "cpi_4"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-01-12"
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
freshness_days: 52
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 0.26
hub_baseline_median_t7: -0.39
hub_baseline_std_t7: 11.002
hub_baseline_delta: 0.65
z_score_t7: 0.0
percentile_t7: 57.14
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/eth-after-cpi-2026-01-12"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 326.588
event_previous: 326.031
event_delta: 0.557
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
related_events: [{"slug": "eth-after-cpi-2024-06-12", "title": "ETH Reaction to US CPI (2024-06-12): Quant Probability Breakdown", "event_date": "2024-06-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.22, "median_t7_pct": -0.39, "sample_size": 14}, {"slug": "eth-after-cpi-2026-02-12", "title": "ETH CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.39, "sample_size": 14}, {"slug": "eth-after-cpi-2025-12-12", "title": "ETH Reaction to US CPI (2025-12-12): Quant Probability Breakdown", "event_date": "2025-12-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -0.39, "sample_size": 14}]
chartData: [{"time": "2026-01-09", "open": 3104.33, "high": 3140.71, "low": 3058.1, "close": 3083.05}, {"time": "2026-01-10", "open": 3083.17, "high": 3099.17, "low": 3075.14, "close": 3082.4}, {"time": "2026-01-11", "open": 3082.41, "high": 3141.96, "low": 3080.75, "close": 3118.89}, {"time": "2026-01-12", "open": 3118.83, "high": 3166.22, "low": 3068.07, "close": 3092.33}, {"time": "2026-01-13", "open": 3092.01, "high": 3352.58, "low": 3088.51, "close": 3322.1}, {"time": "2026-01-14", "open": 3322.19, "high": 3397.9, "low": 3280.38, "close": 3354.72}, {"time": "2026-01-15", "open": 3354.77, "high": 3382.45, "low": 3276.82, "close": 3317.1}, {"time": "2026-01-16", "open": 3317.34, "high": 3325.25, "low": 3251.81, "close": 3295.48}, {"time": "2026-01-17", "open": 3295.48, "high": 3328.28, "low": 3282.66, "close": 3308.86}, {"time": "2026-01-18", "open": 3308.91, "high": 3367.17, "low": 3278.43, "close": 3281.16}, {"time": "2026-01-19", "open": 3282.2, "high": 3282.65, "low": 3166.02, "close": 3186.62}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2026-01-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **52 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.588, Previous 326.031, Delta +0.5570)
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

Execution quality here comes from context discipline rather than reacting to the first candle. ETH around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 326.5880 versus previous 326.0310, a delta of +0.5570. Across the full history, ETH has a T+7 up probability of 42.86% versus 57.14% down, with a median return of -0.39%. When only matching the same event direction, the T+7 up probability shifts to 46.15% across 13 comparable releases, with a same-direction median of -0.77%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: ETH reacts to inflation prints through both risk appetite and crypto-beta rotation, often showing larger relative swings than BTC during regime shifts. CPI surprises can trigger an initial valuation shock, then a second...

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of 0.26% carries a z-score of 0.00 and a percentile rank of 57.14, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. The baseline comparison is what turns the page from observation into a repeatable checklist. The hub baseline median T+7 return is -0.39% and the current gap is +0.65%. Same-direction probability moves by +3.29% and the same-direction median differs by -0.38%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Layer-2 and ETF-adjacent narrative flows can amplify post-CPI trend continuation, especially when macro surprise aligns with existing positioning. At the same time, cross-exchange liquidity has become more synchronized...

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is skipping confirmation steps because the headline feels obvious. Network-specific headlines and protocol news can contaminate pure macro interpretation around release windows. If USD and front-end yields diverge, ETH can print misleading first-candle direction before reverting; leverage-driven liquidations then increase realized slippage and drawdown risk. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Treat this page as an execution checklist input, not a buy or sell signal. The operational takeaway is calibration, not escalation. The checklist remains Compare ETH/BTC ratio around event open.; Confirm spot-volume participation before breakout trades.; Reduce leverage when spread volatility widens.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
