---
title: "2026-01-02 Nonfarm Payrolls: ETH Historical Win Rate"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-01-02"
asof_date: "2026-03-08"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 4.94
robust_score: -1.06
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 34
freshness_days: 65
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 2.65
hub_baseline_median_t7: 1.44
hub_baseline_std_t7: 9.723
hub_baseline_delta: -2.76
z_score_t7: -0.41
percentile_t7: 38.24
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/eth-after-nfp-2026-01-02"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 158627.0
event_previous: 158497.0
event_delta: 130.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -0.97
  mdd_t7: -1.32
  volatility: 1.37
  impact_t1_pct: 0.05
  impact_t7_pct: -1.32
probabilities:
  sample_size: 34
  t1:
    up: 50.0
    down: 50.0
    median: 0.0
    mean: -0.15
    sample: 34
  t7:
    up: 55.88
    down: 44.12
    median: 1.44
    mean: 2.65
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 30
    t1:
      up: 50.0
      down: 50.0
      median: 0.0
      mean: -0.14
      sample: 30
    t7:
      up: 53.33
      down: 46.67
      median: 0.79
      mean: 2.65
      sample: 30
related_events: [{"slug": "eth-after-nfp-2026-02-06", "title": "ETH NFP Reaction (2026-02-06): T+1/T+7 Up Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}, {"slug": "eth-after-nfp-2025-12-05", "title": "ETH Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}, {"slug": "eth-after-nfp-2025-11-07", "title": "NFP Print (2025-11-07) vs ETH: Quantified Directional Odds", "event_date": "2025-11-07", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 1.44, "sample_size": 34}]
chartData: [{"time": "2025-12-30", "open": 2934.42, "high": 3002.8, "low": 2916.33, "close": 2971.42}, {"time": "2025-12-31", "open": 2971.41, "high": 3021.85, "low": 2959.14, "close": 2967.04}, {"time": "2026-01-01", "open": 2967.0, "high": 3006.01, "low": 2966.85, "close": 3000.39}, {"time": "2026-01-02", "open": 3000.45, "high": 3146.98, "low": 2989.9, "close": 3124.42}, {"time": "2026-01-03", "open": 3124.31, "high": 3135.03, "low": 3077.47, "close": 3125.92}, {"time": "2026-01-04", "open": 3125.96, "high": 3160.55, "low": 3119.43, "close": 3140.71}, {"time": "2026-01-05", "open": 3141.49, "high": 3261.25, "low": 3134.09, "close": 3226.13}, {"time": "2026-01-06", "open": 3226.12, "high": 3303.56, "low": 3184.01, "close": 3295.95}, {"time": "2026-01-07", "open": 3295.91, "high": 3296.39, "low": 3126.55, "close": 3166.84}, {"time": "2026-01-08", "open": 3166.92, "high": 3179.87, "low": 3052.51, "close": 3104.38}, {"time": "2026-01-09", "open": 3104.33, "high": 3140.71, "low": 3058.1, "close": 3083.05}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2026-01-02**
- As-of date (T-1): **2026-03-08**
- Freshness age: **65 days**
- Sample size (all-history): **34**

## Event Outcome

- NFP Outcome: **UP** (Actual 158627.0, Previous 158497.0, Delta +130.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.15% | 34 |
| T+7 | 55.88% | 44.12% | 1.44% | 2.65% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.0% | -0.14% | 30 |
| T+7 | 53.33% | 46.67% | 0.79% | 2.65% | 30 |

## Event Outcome Interpretation

The main mistake after macro releases is to treat every surprise as a regime break. ETH around NFP is best framed through how the release landed higher than the previous release. The current observation shows actual value 158627.0000 versus previous 158497.0000, a delta of +130.0000. Across the full history, ETH has a T+7 up probability of 55.88% versus 44.12% down, with a median return of 1.44%. When only matching the same event direction, the T+7 up probability shifts to 53.33% across 30 comparable releases, with a same-direction median of 0.79%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: ETH has historically shown mixed first-day response to payroll shocks, but directional follow-through improves when dollar trend aligns with crypto market breadth.

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of -1.32% carries a z-score of -0.41 and a percentile rank of 38.24, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. The baseline comparison matters because most false positives come from overreacting to ordinary noise. The hub baseline median T+7 return is 1.44% and the current gap is -2.76%. Same-direction probability moves by -2.55% and the same-direction median differs by -0.65%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Cross-exchange depth has improved, reducing single-venue distortion.

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is assuming the first interpretation will survive cross-asset confirmation. Thin weekend-adjacent liquidity can produce false breaks. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Treat this as an educational risk framework, not investment advice. The operational takeaway is calibration, not escalation. The checklist remains Validate move with ETH perp funding and open interest.; Use smaller first entry and add on confirmation.; Monitor ETH/BTC and TOTAL3 for breadth confirmation.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
