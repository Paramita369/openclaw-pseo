---
title: "2026-01-12 CPI Release: ETH Directional Probability Snapshot"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 4
title_template_key: "cpi_4"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-01-12"
asof_date: "2026-03-10"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -2.51
robust_score: -8.51
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 39
freshness_days: 57
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 0.23
hub_baseline_median_t7: -1.18
hub_baseline_std_t7: 9.719
hub_baseline_delta: 4.23
z_score_t7: 0.29
percentile_t7: 71.79
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/eth-after-cpi-2026-01-12"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 326.588
event_previous: 326.031
event_delta: 0.557
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.7
  mdd_t7: 0.0
  volatility: 4.38
  impact_t1_pct: 7.43
  impact_t7_pct: 3.05
probabilities:
  sample_size: 39
  t1:
    up: 58.97
    down: 41.03
    median: 0.94
    mean: 0.55
    sample: 39
  t7:
    up: 43.59
    down: 56.41
    median: -1.18
    mean: 0.23
    sample: 39
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.96
      mean: 0.64
      sample: 38
    t7:
      up: 44.74
      down: 55.26
      median: -1.52
      mean: 0.24
      sample: 38
related_events: [{"slug": "eth-after-cpi-2024-06-12", "title": "ETH Reaction to US CPI (2024-06-12): Quant Probability Breakdown", "event_date": "2024-06-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.22, "median_t7_pct": -1.18, "sample_size": 39}, {"slug": "eth-after-cpi-2026-02-12", "title": "ETH CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.18, "sample_size": 39}, {"slug": "eth-after-cpi-2025-12-12", "title": "ETH Reaction to US CPI (2025-12-12): Quant Probability Breakdown", "event_date": "2025-12-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": -1.18, "sample_size": 39}]
chartData: [{"time": "2026-01-09", "open": 3104.33, "high": 3140.71, "low": 3058.1, "close": 3083.05}, {"time": "2026-01-10", "open": 3083.17, "high": 3099.17, "low": 3075.14, "close": 3082.4}, {"time": "2026-01-11", "open": 3082.41, "high": 3141.96, "low": 3080.75, "close": 3118.89}, {"time": "2026-01-12", "open": 3118.83, "high": 3166.22, "low": 3068.07, "close": 3092.33}, {"time": "2026-01-13", "open": 3092.01, "high": 3352.58, "low": 3088.51, "close": 3322.1}, {"time": "2026-01-14", "open": 3322.19, "high": 3397.9, "low": 3280.38, "close": 3354.72}, {"time": "2026-01-15", "open": 3354.77, "high": 3382.45, "low": 3276.82, "close": 3317.1}, {"time": "2026-01-16", "open": 3317.34, "high": 3325.25, "low": 3251.81, "close": 3295.48}, {"time": "2026-01-17", "open": 3295.48, "high": 3328.28, "low": 3282.66, "close": 3308.86}, {"time": "2026-01-18", "open": 3308.91, "high": 3367.17, "low": 3278.43, "close": 3281.16}, {"time": "2026-01-19", "open": 3282.2, "high": 3282.65, "low": 3166.02, "close": 3186.62}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2026-01-12**
- As-of date (T-1): **2026-03-10**
- Freshness age: **57 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.588, Previous 326.031, Delta +0.5570)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.94% | 0.55% | 39 |
| T+7 | 43.59% | 56.41% | -1.18% | 0.23% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.96% | 0.64% | 38 |
| T+7 | 44.74% | 55.26% | -1.52% | 0.24% | 38 |

## Event Outcome Interpretation

Execution quality here comes from context discipline rather than reacting to the first candle. ETH around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 326.5880 versus previous 326.0310, a delta of +0.5570. Across the full history, ETH has a T+7 up probability of 43.59% versus 56.41% down, with a median return of -1.18%. When only matching the same event direction, the T+7 up probability shifts to 44.74% across 38 comparable releases, with a same-direction median of -1.52%. The current release therefore reads as constructive and above baseline, but not as a full regime break. The standing hub thesis for this asset-event pair is: ETH reacts to inflation prints through both risk appetite and crypto-beta rotation, often showing larger relative swings than BTC during regime shifts. CPI surprises can trigger an initial valuation shock, then a second...

## Distribution Position

This window is above baseline and reads as constructive, positive but not extreme. The current T+7 move of 3.05% carries a z-score of 0.29 and a percentile rank of 71.79, placing the release in the central band of observed windows. That keeps the interpretation on the stronger side of normal without pushing it into tail language. The right read is that the event behaved better than usual, but not so far beyond baseline that it should be mistaken for a structural break.

## Comparison vs Hub Baseline

This comparison is above baseline, but it remains constructive rather than extreme. The baseline comparison is what turns the page from observation into a repeatable checklist. The hub baseline median T+7 return is -1.18% and the current gap is +4.23%. Same-direction probability is +1.15% versus all-history, and the same-direction median differs by -0.34%. That is enough to mark the page as positively skewed, while still requiring cross-asset confirmation before upgrading conviction. The current regime context also matters: Layer-2 and ETF-adjacent narrative flows can amplify post-CPI trend continuation, especially when macro surprise aligns with existing positioning. At the same time, cross-exchange liquidity has become more synchronized...

## Failure Modes

The failure mode here is over-promoting a constructive setup into a false regime break. The main failure mode is skipping confirmation steps because the headline feels obvious. Network-specific headlines and protocol news can contaminate pure macro interpretation around release windows. If USD and front-end yields diverge, ETH can print misleading first-candle direction before reverting; leverage-driven liquidations then increase realized slippage and drawdown risk. Moderate upside events often fail when secondary markets stop confirming, so the biggest mistake is ignoring the difference between above-baseline behavior and true tail behavior.

## Execution Relevance

Treat this page as an execution checklist input, not a buy or sell signal. The correct stance is to treat this as constructive but not extreme. The checklist is still Compare ETH/BTC ratio around event open.; Confirm spot-volume participation before breakout trades.; Reduce leverage when spread volatility widens., and confirmation is still required before acting on the signal. Above-baseline pages deserve attention, but they do not eliminate the need for discipline.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
