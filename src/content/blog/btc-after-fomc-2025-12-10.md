---
title: "Fed Decision (2025-12-10) and BTC: Event-Driven Odds"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2025-12-10"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 6.45
robust_score: 2.45
penalties:
  sample: 4.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 60
sample_size: 9
freshness_days: 85
freshness_status: "fresh"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 1.12
hub_baseline_median_t7: 0.31
hub_baseline_std_t7: 10.2392
hub_baseline_delta: 0.81
z_score_t7: 0.0
percentile_t7: 55.56
narrative_trigger: "within_historical_norm"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/btc-after-fomc-2025-12-10"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "flat"
event_actual: 4.0
event_previous: 4.0
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 1.2
  mdd_t7: 0.0
  volatility: 0.93
  impact_t1_pct: 0.19
  impact_t7_pct: 1.12
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 0.35
    mean: 0.19
    sample: 9
  t7:
    up: 55.56
    down: 44.44
    median: 0.31
    mean: 1.12
    sample: 9
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 9
    t1:
      up: 55.56
      down: 44.44
      median: 0.35
      mean: 0.19
      sample: 9
    t7:
      up: 55.56
      down: 44.44
      median: 0.31
      mean: 1.12
      sample: 9
related_events: [{"slug": "btc-after-fomc-2024-04-30", "title": "BTC After FOMC (2024-04-30): Historical Signal & Probability", "event_date": "2024-04-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 5.37, "median_t7_pct": 0.31, "sample_size": 9}, {"slug": "btc-after-fomc-2024-01-30", "title": "BTC Post-FOMC Reaction (2024-01-30): Quant Backtest Snapshot", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.97, "median_t7_pct": 0.31, "sample_size": 9}, {"slug": "btc-after-fomc-2026-01-28", "title": "FOMC Outcome (2026-01-28) for BTC: Up/Down Probability View", "event_date": "2026-01-28", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.31, "sample_size": 9}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2025-12-10**
- As-of date (T-1): **2026-03-05**
- Freshness age: **85 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 4.0, Previous 4.0, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.35% | 0.19% | 9 |
| T+7 | 55.56% | 44.44% | 0.31% | 1.12% | 9 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.35% | 0.19% | 9 |
| T+7 | 55.56% | 44.44% | 0.31% | 1.12% | 9 |

## Event Outcome Interpretation

The useful signal is where this release sits inside the historical range, not the headline in isolation. BTC around FOMC is best framed through how the release landed unchanged versus the previous release. The current observation shows actual value 4.0000 versus previous 4.0000, a delta of +0.0000. Across the full history, BTC has a T+7 up probability of 55.56% versus 44.44% down, with a median return of 0.31%. When only matching the same event direction, the T+7 up probability shifts to 55.56% across 9 comparable releases, with a same-direction median of 0.31%. That is the immediate context behind the current neutral classification. The standing hub thesis for this asset-event pair is: BTC tends to price the path of liquidity and real yields around FOMC, and the press-conference tone often dominates the initial statement reaction. The strongest setups appear when policy language, dot-plot implications...

## Distribution Position

The current T+7 reaction of 1.12% sits in the middle of its historical distribution for BTC after FOMC. Its z-score is 0.00, which measures distance from the historical mean, and its percentile rank is 55.56, which shows how often prior releases were weaker than this one. That places the observation inside the central band of observed windows, not in an obvious tail bucket. That framing matters because it separates ordinary event noise from true tail behavior inside the same distribution. In practice this means the page is useful for calibration, but it does not justify upgrading a routine macro response into a regime-break narrative.

## Comparison vs Hub Baseline

Relative to the hub baseline, this release can be located with a concrete distance from normal behavior. The hub baseline median T+7 return for BTC after FOMC is 0.31%, while the baseline mean is 1.12% and the baseline standard deviation is 10.2392. The current event is running at +0.81% versus the baseline median. Same-direction probability is +0.00% versus the all-history T+7 up rate, and the same-direction median differs by +0.00%. In other words, the baseline gap decides the narrative, not a cosmetic change in wording. This release is classified as within historical norm rather than handled as a generic macro template. If the current move only differed by a few basis points, the narrative would collapse back toward historical norm. The current regime context also matters: Rate-path sensitivity has increased versus the headline policy-rate level, especially after ETF-driven participation expanded macro crossover flow. Markets now reprice expected cuts and real-yield trajectory faster than...

## Failure Modes

The main failure mode is forgetting that distributions absorb a lot of noise before they change shape. Whipsaw risk is highest between statement release and Powell Q&A, where a second narrative can reverse the first move. Funding-rate extremes, thin liquidity in correlated alt markets, and sudden bond-volatility spikes can magnify false breakouts during this window. This matters because the historical distribution is built on end-of-window outcomes, not the first minute of price discovery. A release can look constructive initially, then fail once rates, the dollar, and sector breadth reprice in a different direction. That is also why low sample environments and mixed reaction functions should be handled as weaker evidence.

## Execution Relevance

Use this page as a distribution map, not a shortcut to conviction. The practical takeaway is to use the current page as a decision filter: read the release, compare it with the hub baseline, then decide whether the event is behaving like a normal FOMC setup or a tail observation. For this asset-event pair, the operational checklist is: Map expected policy path versus futures pricing pre-event.; Wait for confirmation after press conference starts.; Scale entries in multiple tranches, not one fill.. When the page is marked within historical norm, the right response is not automatically to trade more aggressively; it is to decide whether confirmation quality is strong enough to justify action.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
