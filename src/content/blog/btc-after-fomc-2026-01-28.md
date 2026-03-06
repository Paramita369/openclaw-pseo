---
title: "FOMC Outcome (2026-01-28) for BTC: Up/Down Probability View"
description: "Historical probability profile for BTC around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 5
title_template_key: "fomc_5"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2026-01-28"
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
freshness_days: 36
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
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/btc-after-fomc-2026-01-28"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "flat"
event_actual: 3.75
event_previous: 3.75
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
related_events: [{"slug": "btc-after-fomc-2024-04-30", "title": "BTC After FOMC (2024-04-30): Historical Signal & Probability", "event_date": "2024-04-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 5.37, "median_t7_pct": 0.31, "sample_size": 9}, {"slug": "btc-after-fomc-2024-01-30", "title": "BTC Post-FOMC Reaction (2024-01-30): Quant Backtest Snapshot", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 2.97, "median_t7_pct": 0.31, "sample_size": 9}, {"slug": "btc-after-fomc-2025-12-10", "title": "Fed Decision (2025-12-10) and BTC: Event-Driven Odds", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.31, "sample_size": 9}]
chartData: [{"time": "2026-01-25", "open": 89104.77, "high": 89193.15, "low": 86003.71, "close": 86572.22}, {"time": "2026-01-26", "open": 86566.52, "high": 88743.07, "low": 86429.29, "close": 88267.14}, {"time": "2026-01-27", "open": 88257.48, "high": 89427.12, "low": 87228.92, "close": 89102.57}, {"time": "2026-01-28", "open": 89104.05, "high": 90439.29, "low": 88721.46, "close": 89184.57}, {"time": "2026-01-29", "open": 89169.85, "high": 89200.78, "low": 83250.6, "close": 84561.59}, {"time": "2026-01-30", "open": 84562.73, "high": 84602.16, "low": 81071.48, "close": 84128.66}, {"time": "2026-01-31", "open": 84126.5, "high": 84136.92, "low": 75815.88, "close": 78621.12}, {"time": "2026-02-01", "open": 78626.12, "high": 79322.61, "low": 75698.9, "close": 76974.45}, {"time": "2026-02-02", "open": 76968.88, "high": 79258.61, "low": 74551.34, "close": 78688.77}, {"time": "2026-02-03", "open": 78693.51, "high": 79118.85, "low": 72897.14, "close": 75633.55}, {"time": "2026-02-04", "open": 75640.09, "high": 76864.66, "low": 71779.93, "close": 73019.7}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **BTC**
- Event date: **2026-01-28**
- As-of date (T-1): **2026-03-05**
- Freshness age: **36 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 3.75, Previous 3.75, Delta +0.0000)
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

The useful signal is where this release sits inside the historical range, not the headline in isolation. BTC around FOMC is best framed through how the release landed unchanged versus the previous release. The current observation shows actual value 3.7500 versus previous 3.7500, a delta of +0.0000. Across the full history, BTC has a T+7 up probability of 55.56% versus 44.44% down, with a median return of 0.31%. When only matching the same event direction, the T+7 up probability shifts to 55.56% across 9 comparable releases, with a same-direction median of 0.31%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: BTC tends to price the path of liquidity and real yields around FOMC, and the press-conference tone often dominates the initial statement reaction. The strongest setups appear when policy language, dot-plot implications...

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of 1.12% carries a z-score of 0.00 and a percentile rank of 55.56, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. Relative to the hub baseline, this release can be located with a concrete distance from normal behavior. The hub baseline median T+7 return is 0.31% and the current gap is +0.81%. Same-direction probability moves by +0.00% and the same-direction median differs by +0.00%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Rate-path sensitivity has increased versus the headline policy-rate level, especially after ETF-driven participation expanded macro crossover flow. Markets now reprice expected cuts and real-yield trajectory faster than...

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is forgetting that distributions absorb noise before they change shape. Whipsaw risk is highest between statement release and Powell Q&A, where a second narrative can reverse the first move. Funding-rate extremes, thin liquidity in correlated alt markets, and sudden bond-volatility spikes can magnify false breakouts during this window. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Use this page as a distribution map, not a shortcut to conviction. The operational takeaway is calibration, not escalation. The checklist remains Map expected policy path versus futures pricing pre-event.; Wait for confirmation after press conference starts.; Scale entries in multiple tranches, not one fill.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
