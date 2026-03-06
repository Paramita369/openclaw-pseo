---
title: "BTC After CPI (2026-02-12): Up/Down Odds and Median Returns"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "cpi_5"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-02-12"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 3.43
robust_score: 3.43
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 70
sample_size: 14
freshness_days: 21
freshness_status: "fresh"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 1.69
hub_baseline_median_t7: 3.64
hub_baseline_std_t7: 8.5155
hub_baseline_delta: -1.95
z_score_t7: -0.0
percentile_t7: 42.86
narrative_trigger: "within_historical_norm"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/btc-after-cpi-2026-02-12"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 326.588
event_previous: 326.031
event_delta: 0.557
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 1.18
  mdd_t7: 0.0
  volatility: 1.43
  impact_t1_pct: 0.26
  impact_t7_pct: 1.69
probabilities:
  sample_size: 14
  t1:
    up: 42.86
    down: 57.14
    median: -0.74
    mean: 0.26
    sample: 14
  t7:
    up: 57.14
    down: 42.86
    median: 3.64
    mean: 1.69
    sample: 14
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 46.15
      down: 53.85
      median: -0.74
      mean: 0.44
      sample: 13
    t7:
      up: 61.54
      down: 38.46
      median: 4.15
      mean: 2.19
      sample: 13
related_events: [{"slug": "btc-after-cpi-2024-08-14", "title": "BTC Reaction to US CPI (2024-08-14): Quant Probability Breakdown", "event_date": "2024-08-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.86, "median_t7_pct": 3.64, "sample_size": 14}, {"slug": "btc-after-cpi-2026-01-12", "title": "BTC CPI Win Rate (2026-01-12): Historical T+1/T+7 Probability", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 3.64, "sample_size": 14}, {"slug": "btc-after-cpi-2025-12-12", "title": "BTC After CPI (2025-12-12): Up/Down Odds and Median Returns", "event_date": "2025-12-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 3.64, "sample_size": 14}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2026-02-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **21 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.588, Previous 326.031, Delta +0.5570)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 42.86% | 57.14% | -0.74% | 0.26% | 14 |
| T+7 | 57.14% | 42.86% | 3.64% | 1.69% | 14 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 46.15% | 53.85% | -0.74% | 0.44% | 13 |
| T+7 | 61.54% | 38.46% | 4.15% | 2.19% | 13 |

## Event Outcome Interpretation

This event should be read as a distribution problem, not a headline-only trade. BTC around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 326.5880 versus previous 326.0310, a delta of +0.5570. Across the full history, BTC has a T+7 up probability of 57.14% versus 42.86% down, with a median return of 3.64%. When only matching the same event direction, the T+7 up probability shifts to 61.54% across 13 comparable releases, with a same-direction median of 4.15%. That is the immediate context behind the current neutral classification. The standing hub thesis for this asset-event pair is: Bitcoin's sensitivity to US inflation data has shifted from a pure risk-on asset to a complex liquidity proxy. Historical analysis reveals that upside CPI surprises often trigger acute T+1 drawdowns, followed by a robus...

## Distribution Position

The current T+7 reaction of 1.69% sits in the middle of its historical distribution for BTC after CPI. Its z-score is -0.00, which measures distance from the historical mean, and its percentile rank is 42.86, which shows how often prior releases were weaker than this one. That places the observation inside the central band of observed windows, not in an obvious tail bucket. That keeps the interpretation anchored in the shape of the historical sample rather than the release headline. In practice this means the page is useful for calibration, but it does not justify upgrading a routine macro response into a regime-break narrative.

## Comparison vs Hub Baseline

Against the hub baseline for this asset-event pair, the current print is measurable rather than anecdotal. The hub baseline median T+7 return for BTC after CPI is 3.64%, while the baseline mean is 1.69% and the baseline standard deviation is 8.5155. The current event is running at -1.95% versus the baseline median. Same-direction probability is +4.40% versus the all-history T+7 up rate, and the same-direction median differs by +0.51%. The classification is therefore tied to a measurable gap versus baseline, not to narrative convenience. This release is classified as within historical norm rather than handled as a generic macro template. If the current move only differed by a few basis points, the narrative would collapse back toward historical norm. The current regime context also matters: Institutional ETF flows now absorb immediate volatility shockwaves faster than in the 2022 tightening cycle, which means CPI-driven drawdowns can exhaust sooner than older crypto bear-market analogs suggested. The first...

## Failure Modes

The main failure mode is misreading a statistically ordinary move as a structural break. Elevated funding rates on offshore exchanges can exacerbate liquidations independent of the CPI print, so a mechanically weak first candle is not enough on its own. Traders also need to watch whether real yields and DXY confirm the same macro read, because mismatched cross-asset signals often reverse the initial BTC move. This matters because the historical distribution is built on end-of-window outcomes, not the first minute of price discovery. A release can look constructive initially, then fail once rates, the dollar, and sector breadth reprice in a different direction. That is also why low sample environments and mixed reaction functions should be handled as weaker evidence.

## Execution Relevance

Use this page as an educational operating lens, not a trading instruction. The practical takeaway is to use the current page as a decision filter: read the release, compare it with the hub baseline, then decide whether the event is behaving like a normal CPI setup or a tail observation. For this asset-event pair, the operational checklist is: Monitor CME futures basis pre-print.; Set limit orders 3-5% below current spot for flash crashes.; Wait for 1-hour candle close before deploying directional delta.. When the page is marked within historical norm, the right response is not automatically to trade more aggressively; it is to decide whether confirmation quality is strong enough to justify action.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
