---
title: "BTC CPI Win Rate (2026-03-11): Historical T+1/T+7 Probability"
description: "Historical probability profile for BTC around CPI events (T+1/T+7)."
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
raw_signal_score: 6.93
robust_score: 6.93
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
body_variant_family: "distribution"
hub_baseline_mean_t7: 0.44
hub_baseline_median_t7: 1.11
hub_baseline_std_t7: 6.5186
hub_baseline_delta: -0.67
z_score_t7: -0.0
percentile_t7: 48.72
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/btc-after-cpi-2026-03-11"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "up"
event_actual: 327.46
event_previous: 326.588
event_delta: 0.872
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["btc", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 14.67
  mdd_t7: 0.0
  volatility: 0.03
  impact_t1_pct: 0.41
  impact_t7_pct: 0.44
probabilities:
  sample_size: 40
  t1:
    up: 60.0
    down: 40.0
    median: 0.46
    mean: 0.37
    sample: 40
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
      up: 61.54
      down: 38.46
      median: 0.51
      mean: 0.44
      sample: 39
    t7:
      up: 55.26
      down: 44.74
      median: 1.26
      mean: 0.58
      sample: 38
related_events: [{"slug": "btc-after-cpi-2025-09-11", "title": "BTC After CPI (2025-09-11): Historical T+1/T+7 Probability", "event_date": "2025-09-11", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.41, "sample_size": 0}, {"slug": "btc-after-cpi-2025-07-15", "title": "BTC After CPI (2025-07-15): Historical T+1/T+7 Probability", "event_date": "2025-07-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.88, "sample_size": 0}, {"slug": "btc-after-cpi-2025-05-12", "title": "BTC After CPI (2025-05-12): Historical T+1/T+7 Probability", "event_date": "2025-05-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.72, "sample_size": 0}]
chartData: [{"time": "2026-03-08", "open": 67272.5, "high": 68177.79, "low": 65639.2, "close": 65969.78}, {"time": "2026-03-09", "open": 65969.59, "high": 69474.95, "low": 65858.01, "close": 68402.38}, {"time": "2026-03-10", "open": 68402.72, "high": 71770.9, "low": 68402.72, "close": 69926.92}, {"time": "2026-03-11", "open": 69931.25, "high": 71337.66, "low": 68998.87, "close": 70204.88}, {"time": "2026-03-12", "open": 70209.77, "high": 70775.83, "low": 69230.16, "close": 70493.46}, {"time": "2026-03-13", "open": 70509.98, "high": 72017.16, "low": 70491.65, "close": 71865.4}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **BTC**
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
| T+1 | 60.0% | 40.0% | 0.46% | 0.37% | 40 |
| T+7 | 53.85% | 46.15% | 1.11% | 0.44% | 39 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 61.54% | 38.46% | 0.51% | 0.44% | 39 |
| T+7 | 55.26% | 44.74% | 1.26% | 0.58% | 38 |

## Event Outcome Interpretation

The useful signal is where this release sits inside the historical range, not the headline in isolation. BTC around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 327.4600 versus previous 326.5880, a delta of +0.8720. Across the full history, BTC has a T+7 up probability of 53.85% versus 46.15% down, with a median return of 1.11%. When only matching the same event direction, the T+7 up probability shifts to 55.26% across 38 comparable releases, with a same-direction median of 1.26%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: Bitcoin's sensitivity to US inflation data has shifted from a pure risk-on asset to a complex liquidity proxy. Historical analysis reveals that upside CPI surprises often trigger acute T+1 drawdowns, followed by a robus...

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of 0.44% carries a z-score of -0.00 and a percentile rank of 48.72, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. Relative to the hub baseline, this release can be located with a concrete distance from normal behavior. The hub baseline median T+7 return is 1.11% and the current gap is -0.67%. Same-direction probability moves by +1.41% and the same-direction median differs by +0.15%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Institutional ETF flows now absorb immediate volatility shockwaves faster than in the 2022 tightening cycle, which means CPI-driven drawdowns can exhaust sooner than older crypto bear-market analogs suggested. The first...

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is forgetting that distributions absorb noise before they change shape. Elevated funding rates on offshore exchanges can exacerbate liquidations independent of the CPI print, so a mechanically weak first candle is not enough on its own. Traders also need to watch whether real yields and DXY confirm the same macro read, because mismatched cross-asset signals often reverse the initial BTC move. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Use this page as a distribution map, not a shortcut to conviction. The operational takeaway is calibration, not escalation. The checklist remains Monitor CME futures basis pre-print.; Set limit orders 3-5% below current spot for flash crashes.; Wait for 1-hour candle close before deploying directional delta.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
