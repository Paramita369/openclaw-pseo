---
title: "BTC CPI Win Rate (2026-01-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-01-12"
asof_date: "2026-03-09"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 6.62
robust_score: 0.62
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 39
freshness_days: 56
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: 0.38
z_score_t7: 0.16
percentile_t7: 53.85
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/btc-after-cpi-2026-01-12"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 326.588
event_previous: 326.031
event_delta: 0.557
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.49
  mdd_t7: 0.0
  volatility: 3.04
  impact_t1_pct: 4.53
  impact_t7_pct: 1.49
probabilities:
  sample_size: 39
  t1:
    up: 58.97
    down: 41.03
    median: 0.51
    mean: 0.37
    sample: 39
  t7:
    up: 53.85
    down: 46.15
    median: 1.11
    mean: 0.44
    sample: 39
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.53
      mean: 0.44
      sample: 38
    t7:
      up: 55.26
      down: 44.74
      median: 1.26
      mean: 0.58
      sample: 38
related_events: [{"slug": "btc-after-cpi-2024-08-14", "title": "BTC Reaction to US CPI (2024-08-14): Quant Probability Breakdown", "event_date": "2024-08-14", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.86, "median_t7_pct": 1.11, "sample_size": 39}, {"slug": "btc-after-cpi-2026-02-12", "title": "BTC After CPI (2026-02-12): Up/Down Odds and Median Returns", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 39}, {"slug": "btc-after-cpi-2025-12-12", "title": "BTC After CPI (2025-12-12): Up/Down Odds and Median Returns", "event_date": "2025-12-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.11, "sample_size": 39}]
chartData: [{"time": "2026-01-09", "open": 91026.27, "high": 91910.67, "low": 89625.38, "close": 90513.1}, {"time": "2026-01-10", "open": 90510.1, "high": 90713.03, "low": 90283.4, "close": 90386.65}, {"time": "2026-01-11", "open": 90385.36, "high": 91155.23, "low": 90212.02, "close": 90827.46}, {"time": "2026-01-12", "open": 90825.86, "high": 92395.52, "low": 90055.02, "close": 91192.99}, {"time": "2026-01-13", "open": 91185.34, "high": 96011.62, "low": 90941.93, "close": 95321.78}, {"time": "2026-01-14", "open": 95322.91, "high": 97860.6, "low": 94583.05, "close": 96929.33}, {"time": "2026-01-15", "open": 96931.29, "high": 97150.17, "low": 95103.24, "close": 95551.19}, {"time": "2026-01-16", "open": 95554.1, "high": 95801.89, "low": 94259.27, "close": 95525.12}, {"time": "2026-01-17", "open": 95525.16, "high": 95598.48, "low": 95005.62, "close": 95099.92}, {"time": "2026-01-18", "open": 95101.18, "high": 95491.51, "low": 93588.87, "close": 93634.43}, {"time": "2026-01-19", "open": 93655.67, "high": 93660.83, "low": 92089.25, "close": 92553.59}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
- Event date: **2026-01-12**
- As-of date (T-1): **2026-03-09**
- Freshness age: **56 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.588, Previous 326.031, Delta +0.5570)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.51% | 0.37% | 39 |
| T+7 | 53.85% | 46.15% | 1.11% | 0.44% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.53% | 0.44% | 38 |
| T+7 | 55.26% | 44.74% | 1.26% | 0.58% | 38 |

## Event Outcome Interpretation

Execution quality here comes from context discipline rather than reacting to the first candle. BTC around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 326.5880 versus previous 326.0310, a delta of +0.5570. Across the full history, BTC has a T+7 up probability of 53.85% versus 46.15% down, with a median return of 1.11%. When only matching the same event direction, the T+7 up probability shifts to 55.26% across 38 comparable releases, with a same-direction median of 1.26%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: Bitcoin's sensitivity to US inflation data has shifted from a pure risk-on asset to a complex liquidity proxy. Historical analysis reveals that upside CPI surprises often trigger acute T+1 drawdowns, followed by a robus...

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of 1.49% carries a z-score of 0.16 and a percentile rank of 53.85, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. The baseline comparison is what turns the page from observation into a repeatable checklist. The hub baseline median T+7 return is 1.11% and the current gap is +0.38%. Same-direction probability moves by +1.41% and the same-direction median differs by +0.15%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Institutional ETF flows now absorb immediate volatility shockwaves faster than in the 2022 tightening cycle, which means CPI-driven drawdowns can exhaust sooner than older crypto bear-market analogs suggested. The first...

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is skipping confirmation steps because the headline feels obvious. Elevated funding rates on offshore exchanges can exacerbate liquidations independent of the CPI print, so a mechanically weak first candle is not enough on its own. Traders also need to watch whether real yields and DXY confirm the same macro read, because mismatched cross-asset signals often reverse the initial BTC move. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Treat this page as an execution checklist input, not a buy or sell signal. The operational takeaway is calibration, not escalation. The checklist remains Monitor CME futures basis pre-print.; Set limit orders 3-5% below current spot for flash crashes.; Wait for 1-hour candle close before deploying directional delta.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
