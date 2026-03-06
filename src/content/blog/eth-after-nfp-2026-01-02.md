---
title: "2026-01-02 Nonfarm Payrolls: ETH Historical Win Rate"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-01-02"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Bullish"
raw_signal_score: 8.93
robust_score: 2.93
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 70
sample_size: 13
freshness_days: 62
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 3.32
hub_baseline_median_t7: 5.12
hub_baseline_std_t7: 8.5559
hub_baseline_delta: -1.8
z_score_t7: -0.0
percentile_t7: 46.15
narrative_trigger: "within_historical_norm"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/eth-after-nfp-2026-01-02"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 158627.0
event_previous: 158497.0
event_delta: 130.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 1.03
  mdd_t7: 0.0
  volatility: 3.21
  impact_t1_pct: 0.11
  impact_t7_pct: 3.32
probabilities:
  sample_size: 13
  t1:
    up: 53.85
    down: 46.15
    median: 0.03
    mean: 0.11
    sample: 13
  t7:
    up: 61.54
    down: 38.46
    median: 5.12
    mean: 3.32
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 12
    t1:
      up: 50.0
      down: 50.0
      median: -0.03
      mean: 0.09
      sample: 12
    t7:
      up: 58.33
      down: 41.67
      median: 3.01
      mean: 3.07
      sample: 12
related_events: [{"slug": "eth-after-nfp-2026-02-06", "title": "ETH NFP Reaction (2026-02-06): T+1/T+7 Up Probability", "event_date": "2026-02-06", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 5.12, "sample_size": 13}, {"slug": "eth-after-nfp-2025-12-05", "title": "ETH Post-NFP Setup (2025-12-05): Historical Probability Lens", "event_date": "2025-12-05", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 5.12, "sample_size": 13}, {"slug": "eth-after-nfp-2025-11-07", "title": "NFP Print (2025-11-07) vs ETH: Quantified Directional Odds", "event_date": "2025-11-07", "event_type": "NFP", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 5.12, "sample_size": 13}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2026-01-02**
- As-of date (T-1): **2026-03-05**
- Freshness age: **62 days**
- Sample size (all-history): **13**

## Event Outcome

- NFP Outcome: **UP** (Actual 158627.0, Previous 158497.0, Delta +130.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.03% | 0.11% | 13 |
| T+7 | 61.54% | 38.46% | 5.12% | 3.32% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | -0.03% | 0.09% | 12 |
| T+7 | 58.33% | 41.67% | 3.01% | 3.07% | 12 |

## Event Outcome Interpretation

The main mistake after macro releases is to treat every surprise as a regime break. ETH around NFP is best framed through how the release landed higher than the previous release. The current observation shows actual value 158627.0000 versus previous 158497.0000, a delta of +130.0000. Across the full history, ETH has a T+7 up probability of 61.54% versus 38.46% down, with a median return of 5.12%. When only matching the same event direction, the T+7 up probability shifts to 58.33% across 12 comparable releases, with a same-direction median of 3.01%. That is the immediate context behind the current bullish classification. The standing hub thesis for this asset-event pair is: ETH has historically shown mixed first-day response to payroll shocks, but directional follow-through improves when dollar trend aligns with crypto market breadth.

## Distribution Position

The current T+7 reaction of 3.32% sits in the middle of its historical distribution for ETH after NFP. Its z-score is -0.00, which measures distance from the historical mean, and its percentile rank is 46.15, which shows how often prior releases were weaker than this one. That places the observation inside the central band of observed windows, not in an obvious tail bucket. That is the difference between a manageable macro impulse and a tail event that can invalidate prior playbooks. In practice this means the page is useful for calibration, but it does not justify upgrading a routine macro response into a regime-break narrative.

## Comparison vs Hub Baseline

The baseline comparison matters because most false positives come from overreacting to ordinary noise. The hub baseline median T+7 return for ETH after NFP is 5.12%, while the baseline mean is 3.32% and the baseline standard deviation is 8.5559. The current event is running at -1.80% versus the baseline median. Same-direction probability is -3.21% versus the all-history T+7 up rate, and the same-direction median differs by -2.11%. That distance from baseline is what determines whether this is noise, pressure, or a real outlier worth extra caution. This release is classified as within historical norm rather than handled as a generic macro template. If the current move only differed by a few basis points, the narrative would collapse back toward historical norm. The current regime context also matters: Cross-exchange depth has improved, reducing single-venue distortion.

## Failure Modes

The main failure mode is assuming the first interpretation of the release will survive cross-asset confirmation. Thin weekend-adjacent liquidity can produce false breaks. This matters because the historical distribution is built on end-of-window outcomes, not the first minute of price discovery. A release can look constructive initially, then fail once rates, the dollar, and sector breadth reprice in a different direction. That is also why low sample environments and mixed reaction functions should be handled as weaker evidence.

## Execution Relevance

Treat this as an educational risk framework, not investment advice. The practical takeaway is to use the current page as a decision filter: read the release, compare it with the hub baseline, then decide whether the event is behaving like a normal NFP setup or a tail observation. For this asset-event pair, the operational checklist is: Validate move with ETH perp funding and open interest.; Use smaller first entry and add on confirmation.; Monitor ETH/BTC and TOTAL3 for breadth confirmation.. When the page is marked within historical norm, the right response is not automatically to trade more aggressively; it is to decide whether confirmation quality is strong enough to justify action.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
