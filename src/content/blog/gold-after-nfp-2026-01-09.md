---
title: "GOLD Post-NFP Setup (2026-01-09): Historical Probability Lens"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 5
title_template_key: "nfp_5"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-01-09"
asof_date: "2026-03-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 19.66
robust_score: 13.66
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 100
sample_size: 35
freshness_days: 62
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.53
hub_baseline_median_t7: 1.31
hub_baseline_std_t7: 1.9626
hub_baseline_delta: 0.87
z_score_t7: 0.33
percentile_t7: 60.0
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/gold-after-nfp-2026-01-09"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "up"
event_actual: 158558.0
event_previous: 158432.0
event_delta: 126.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 9.03
  mdd_t7: -0.35
  volatility: 20.41
  impact_t1_pct: 2.54
  impact_t7_pct: 2.18
probabilities:
  sample_size: 35
  t1:
    up: 63.64
    down: 36.36
    median: 0.39
    mean: 0.5
    sample: 22
  t7:
    up: 77.14
    down: 22.86
    median: 1.31
    mean: 1.53
    sample: 35
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 14
    t1:
      up: 64.29
      down: 35.71
      median: 0.34
      mean: 0.69
      sample: 14
    t7:
      up: 76.92
      down: 23.08
      median: 1.04
      mean: 1.49
      sample: 26
related_events: [{"slug": "gold-after-nfp-2026-01-02", "title": "GOLD After NFP (2026-01-02): Historical T+1/T+7 Probability", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.08, "sample_size": 0}, {"slug": "gold-after-nfp-2025-12-16", "title": "GOLD After NFP (2025-12-16): Historical T+1/T+7 Probability", "event_date": "2025-12-16", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.14, "sample_size": 0}, {"slug": "gold-after-nfp-2025-11-20", "title": "GOLD After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.99, "sample_size": 0}]
chartData: [{"time": "2026-01-06", "open": 4449.7, "high": 4482.2, "low": 4449.0, "close": 4482.2}, {"time": "2026-01-07", "open": 4450.0, "high": 4450.0, "low": 4449.3, "close": 4449.3}, {"time": "2026-01-08", "open": 4460.2, "high": 4461.3, "low": 4418.0, "close": 4449.7}, {"time": "2026-01-09", "open": 4473.0, "high": 4490.3, "low": 4473.0, "close": 4490.3}, {"time": "2026-01-12", "open": 4579.1, "high": 4620.0, "low": 4577.8, "close": 4604.3}, {"time": "2026-01-13", "open": 4578.6, "high": 4617.1, "low": 4578.6, "close": 4589.2}, {"time": "2026-01-14", "open": 4610.3, "high": 4635.0, "low": 4608.2, "close": 4626.3}, {"time": "2026-01-15", "open": 4612.9, "high": 4616.3, "low": 4612.9, "close": 4616.3}, {"time": "2026-01-16", "open": 4608.0, "high": 4608.0, "low": 4588.4, "close": 4588.4}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
- Event date: **2026-01-09**
- As-of date (T-1): **2026-03-12**
- Freshness age: **62 days**
- Sample size (all-history): **35**

## Event Outcome

- NFP Outcome: **UP** (Actual 158558.0, Previous 158432.0, Delta +126.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 63.64% | 36.36% | 0.39% | 0.5% | 22 |
| T+7 | 77.14% | 22.86% | 1.31% | 1.53% | 35 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 64.29% | 35.71% | 0.34% | 0.69% | 14 |
| T+7 | 76.92% | 23.08% | 1.04% | 1.49% | 26 |

## Event Outcome Interpretation

Execution quality here comes from context discipline rather than reacting to the first candle. GOLD around NFP is best framed through how the release landed higher than the previous release. The current observation shows actual value 158558.0000 versus previous 158432.0000, a delta of +126.0000. Across the full history, GOLD has a T+7 up probability of 77.14% versus 22.86% down, with a median return of 1.31%. When only matching the same event direction, the T+7 up probability shifts to 76.92% across 14 comparable releases, with a same-direction median of 1.04%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: Gold often reacts inversely to payroll strength via rates repricing, but follow-through depends on whether labor surprise changes Fed expectations materially.

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of 2.18% carries a z-score of 0.33 and a percentile rank of 60.00, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. The baseline comparison is what turns the page from observation into a repeatable checklist. The hub baseline median T+7 return is 1.31% and the current gap is +0.87%. Same-direction probability moves by -0.22% and the same-direction median differs by -0.27%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Macro headline digestion has become faster, shortening reaction windows.

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is skipping confirmation steps because the headline feels obvious. Revisions and unemployment-rate cross-signals can flip initial direction. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Treat this page as an execution checklist input, not a buy or sell signal. The operational takeaway is calibration, not escalation. The checklist remains Evaluate headline payroll plus revisions together.; Wait for rate market confirmation before adding size.; Use staggered exits around key session levels.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
