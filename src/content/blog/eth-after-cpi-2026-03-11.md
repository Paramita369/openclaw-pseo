---
title: "ETH CPI Win Rate (2026-03-11): Historical T+1/T+7 Probability"
description: "Historical probability profile for ETH around CPI events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-03-11"
asof_date: "2026-03-12"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: -2.2
robust_score: -2.2
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 40
freshness_days: 1
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.23
hub_baseline_median_t7: -1.18
hub_baseline_std_t7: 9.719
hub_baseline_delta: 1.41
z_score_t7: -0.0
percentile_t7: 58.97
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/eth-after-cpi-2026-03-11"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "up"
event_actual: 327.46
event_previous: 326.588
event_delta: 0.872
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.28
  mdd_t7: 0.0
  volatility: 0.82
  impact_t1_pct: 1.05
  impact_t7_pct: 0.23
probabilities:
  sample_size: 40
  t1:
    up: 60.0
    down: 40.0
    median: 0.96
    mean: 0.57
    sample: 40
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
      up: 61.54
      down: 38.46
      median: 0.98
      mean: 0.65
      sample: 39
    t7:
      up: 44.74
      down: 55.26
      median: -1.52
      mean: 0.24
      sample: 38
related_events: [{"slug": "eth-after-cpi-2025-07-15", "title": "ETH After CPI (2025-07-15): Historical T+1/T+7 Probability", "event_date": "2025-07-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 19.4, "sample_size": 0}, {"slug": "eth-after-cpi-2025-07-12", "title": "ETH After CPI (2025-07-12): Historical T+1/T+7 Probability", "event_date": "2025-07-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 22.17, "sample_size": 0}, {"slug": "eth-after-cpi-2025-04-10", "title": "ETH After CPI (2025-04-10): Historical T+1/T+7 Probability", "event_date": "2025-04-10", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.94, "sample_size": 0}]
chartData: [{"time": "2026-03-08", "open": 1969.45, "high": 1978.71, "low": 1915.3, "close": 1936.6}, {"time": "2026-03-09", "open": 1936.64, "high": 2052.33, "low": 1930.6, "close": 1992.94}, {"time": "2026-03-10", "open": 1992.99, "high": 2087.99, "low": 1992.01, "close": 2037.12}, {"time": "2026-03-11", "open": 2037.12, "high": 2085.29, "low": 2008.04, "close": 2051.57}, {"time": "2026-03-12", "open": 2051.77, "high": 2094.33, "low": 2019.28, "close": 2073.14}, {"time": "2026-03-13", "open": 2073.83, "high": 2143.55, "low": 2073.83, "close": 2106.32}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **ETH**
- Event date: **2026-03-11**
- As-of date (T-1): **2026-03-12**
- Freshness age: **1 days**
- Sample size (all-history): **40**

## Event Outcome

- CPI Outcome: **UP** (Actual 327.46, Previous 326.588, Delta +0.8720)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.0% | 40.0% | 0.96% | 0.57% | 40 |
| T+7 | 43.59% | 56.41% | -1.18% | 0.23% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 61.54% | 38.46% | 0.98% | 0.65% | 39 |
| T+7 | 44.74% | 55.26% | -1.52% | 0.24% | 38 |

## Event Outcome Interpretation

The main mistake after macro releases is to treat every surprise as a regime break. ETH around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 327.4600 versus previous 326.5880, a delta of +0.8720. Across the full history, ETH has a T+7 up probability of 43.59% versus 56.41% down, with a median return of -1.18%. When only matching the same event direction, the T+7 up probability shifts to 44.74% across 38 comparable releases, with a same-direction median of -1.52%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: ETH reacts to inflation prints through both risk appetite and crypto-beta rotation, often showing larger relative swings than BTC during regime shifts. CPI surprises can trigger an initial valuation shock, then a second...

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of 0.23% carries a z-score of -0.00 and a percentile rank of 58.97, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. The baseline comparison matters because most false positives come from overreacting to ordinary noise. The hub baseline median T+7 return is -1.18% and the current gap is +1.41%. Same-direction probability moves by +1.15% and the same-direction median differs by -0.34%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Layer-2 and ETF-adjacent narrative flows can amplify post-CPI trend continuation, especially when macro surprise aligns with existing positioning. At the same time, cross-exchange liquidity has become more synchronized...

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is assuming the first interpretation will survive cross-asset confirmation. Network-specific headlines and protocol news can contaminate pure macro interpretation around release windows. If USD and front-end yields diverge, ETH can print misleading first-candle direction before reverting; leverage-driven liquidations then increase realized slippage and drawdown risk. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Treat this as an educational risk framework, not investment advice. The operational takeaway is calibration, not escalation. The checklist remains Compare ETH/BTC ratio around event open.; Confirm spot-volume participation before breakout trades.; Reduce leverage when spread volatility widens.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
