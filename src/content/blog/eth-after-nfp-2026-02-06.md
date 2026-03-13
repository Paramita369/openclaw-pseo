---
title: "ETH NFP Reaction (2026-02-06): T+1/T+7 Up Probability"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 1
title_template_key: "nfp_1"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-02-06"
asof_date: "2026-03-12"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 5.14
robust_score: 5.14
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 35
freshness_days: 34
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 2.74
hub_baseline_median_t7: 1.98
hub_baseline_std_t7: 9.6006
hub_baseline_delta: -2.7
z_score_t7: -0.36
percentile_t7: 40.0
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/eth-after-nfp-2026-02-06"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "down"
event_actual: 158466.0
event_previous: 158558.0
event_delta: -92.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -2.52
  mdd_t7: -2.62
  volatility: 32.75
  impact_t1_pct: 1.32
  impact_t7_pct: -0.72
probabilities:
  sample_size: 35
  t1:
    up: 48.57
    down: 51.43
    median: -0.02
    mean: -0.16
    sample: 35
  t7:
    up: 57.14
    down: 42.86
    median: 1.98
    mean: 2.74
    sample: 35
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 9
    t1:
      up: 55.56
      down: 44.44
      median: 0.33
      mean: -0.41
      sample: 9
    t7:
      up: 66.67
      down: 33.33
      median: 1.98
      mean: 2.06
      sample: 9
related_events: [{"slug": "eth-after-nfp-2026-01-09", "title": "ETH After NFP (2026-01-09): Historical T+1/T+7 Probability", "event_date": "2026-01-09", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 6.89, "sample_size": 0}, {"slug": "eth-after-nfp-2025-11-20", "title": "ETH After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 6.45, "sample_size": 0}, {"slug": "eth-after-nfp-2025-09-05", "title": "ETH After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 9.48, "sample_size": 0}]
chartData: [{"time": "2026-02-03", "open": 2344.45, "high": 2357.21, "low": 2109.06, "close": 2227.56}, {"time": "2026-02-04", "open": 2227.97, "high": 2291.13, "low": 2074.1, "close": 2143.5}, {"time": "2026-02-05", "open": 2143.62, "high": 2167.14, "low": 1818.66, "close": 1821.68}, {"time": "2026-02-06", "open": 1821.13, "high": 2090.33, "low": 1748.63, "close": 2063.39}, {"time": "2026-02-07", "open": 2063.33, "high": 2115.82, "low": 1995.92, "close": 2090.55}, {"time": "2026-02-08", "open": 2090.63, "high": 2148.12, "low": 2066.38, "close": 2088.76}, {"time": "2026-02-09", "open": 2087.92, "high": 2144.98, "low": 2008.36, "close": 2103.57}, {"time": "2026-02-10", "open": 2104.18, "high": 2122.02, "low": 1990.14, "close": 2019.5}, {"time": "2026-02-11", "open": 2019.58, "high": 2030.41, "low": 1903.69, "close": 1940.62}, {"time": "2026-02-12", "open": 1940.84, "high": 1999.5, "low": 1897.33, "close": 1946.94}, {"time": "2026-02-13", "open": 1946.61, "high": 2069.46, "low": 1924.14, "close": 2048.53}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2026-02-06**
- As-of date (T-1): **2026-03-12**
- Freshness age: **34 days**
- Sample size (all-history): **35**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158466.0, Previous 158558.0, Delta -92.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 48.57% | 51.43% | -0.02% | -0.16% | 35 |
| T+7 | 57.14% | 42.86% | 1.98% | 2.74% | 35 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.33% | -0.41% | 9 |
| T+7 | 66.67% | 33.33% | 1.98% | 2.06% | 9 |

## Event Outcome Interpretation

The useful signal is where this release sits inside the historical range, not the headline in isolation. ETH around NFP is best framed through how the release landed lower than the previous release. The current observation shows actual value 158466.0000 versus previous 158558.0000, a delta of -92.0000. Across the full history, ETH has a T+7 up probability of 57.14% versus 42.86% down, with a median return of 1.98%. When only matching the same event direction, the T+7 up probability shifts to 66.67% across 9 comparable releases, with a same-direction median of 1.98%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: ETH has historically shown mixed first-day response to payroll shocks, but directional follow-through improves when dollar trend aligns with crypto market breadth.

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of -0.72% carries a z-score of -0.36 and a percentile rank of 40.00, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. Relative to the hub baseline, this release can be located with a concrete distance from normal behavior. The hub baseline median T+7 return is 1.98% and the current gap is -2.70%. Same-direction probability moves by +9.53% and the same-direction median differs by +0.00%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Cross-exchange depth has improved, reducing single-venue distortion.

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is forgetting that distributions absorb noise before they change shape. Thin weekend-adjacent liquidity can produce false breaks. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Use this page as a distribution map, not a shortcut to conviction. The operational takeaway is calibration, not escalation. The checklist remains Validate move with ETH perp funding and open interest.; Use smaller first entry and add on confirmation.; Monitor ETH/BTC and TOTAL3 for breadth confirmation.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
