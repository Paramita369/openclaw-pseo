---
title: "Fed Decision (2026-01-28) and QQQ: Event-Driven Odds"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2026-01-28"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 17.56
robust_score: 13.56
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
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.03
hub_baseline_median_t7: 1.16
hub_baseline_std_t7: 2.2487
hub_baseline_delta: -0.13
z_score_t7: 0.0
percentile_t7: 33.33
narrative_trigger: "within_historical_norm"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/qqq-after-fomc-2026-01-28"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "flat"
event_actual: 3.75
event_previous: 3.75
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 1.08
  mdd_t7: 0.0
  volatility: 0.95
  impact_t1_pct: 0.08
  impact_t7_pct: 1.03
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 0.43
    mean: 0.08
    sample: 9
  t7:
    up: 77.78
    down: 22.22
    median: 1.16
    mean: 1.03
    sample: 9
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 9
    t1:
      up: 55.56
      down: 44.44
      median: 0.43
      mean: 0.08
      sample: 9
    t7:
      up: 77.78
      down: 22.22
      median: 1.16
      mean: 1.03
      sample: 9
related_events: [{"slug": "qqq-after-fomc-2024-01-30", "title": "Fed Decision (2024-01-30) and QQQ: Event-Driven Odds", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 2.07, "median_t7_pct": 1.16, "sample_size": 9}, {"slug": "qqq-after-fomc-2025-12-10", "title": "QQQ Post-FOMC Reaction (2025-12-10): Quant Backtest Snapshot", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 1.16, "sample_size": 9}, {"slug": "qqq-after-fomc-2025-10-29", "title": "2025-10-29 FOMC Meeting: QQQ T+1/T+7 Probability Profile", "event_date": "2025-10-29", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 1.16, "sample_size": 9}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
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
| T+1 | 55.56% | 44.44% | 0.43% | 0.08% | 9 |
| T+7 | 77.78% | 22.22% | 1.16% | 1.03% | 9 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.43% | 0.08% | 9 |
| T+7 | 77.78% | 22.22% | 1.16% | 1.03% | 9 |

## Event Outcome Interpretation

Execution quality here comes from context discipline rather than reacting to the first candle. QQQ around FOMC is best framed through how the release landed unchanged versus the previous release. The current observation shows actual value 3.7500 versus previous 3.7500, a delta of +0.0000. Across the full history, QQQ has a T+7 up probability of 77.78% versus 22.22% down, with a median return of 1.16%. When only matching the same event direction, the T+7 up probability shifts to 77.78% across 9 comparable releases, with a same-direction median of 1.16%. That is the immediate context behind the current bullish classification. The standing hub thesis for this asset-event pair is: QQQ generally trends with forward-rate expectations, and reactions are magnified when valuation is stretched before the meeting. The highest-quality playbook setup occurs when statement language, dot-plot repricing, and...

## Distribution Position

The current T+7 reaction of 1.03% sits in the middle of its historical distribution for QQQ after FOMC. Its z-score is 0.00, which measures distance from the historical mean, and its percentile rank is 33.33, which shows how often prior releases were weaker than this one. That places the observation inside the central band of observed windows, not in an obvious tail bucket. That distinction is what tells an operator whether to slow down, confirm, or stand aside. In practice this means the page is useful for calibration, but it does not justify upgrading a routine macro response into a regime-break narrative.

## Comparison vs Hub Baseline

The baseline comparison is what turns this page from observation into a repeatable checklist. The hub baseline median T+7 return for QQQ after FOMC is 1.16%, while the baseline mean is 1.03% and the baseline standard deviation is 2.2487. The current event is running at -0.13% versus the baseline median. Same-direction probability is +0.00% versus the all-history T+7 up rate, and the same-direction median differs by +0.00%. That baseline gap is what turns the page into an action filter instead of a generic macro recap. This release is classified as within historical norm rather than handled as a generic macro template. If the current move only differed by a few basis points, the narrative would collapse back toward historical norm. The current regime context also matters: Communication tone has become a bigger driver than the headline rate level itself, particularly in periods where terminal-rate uncertainty is lower and policy-path uncertainty is higher. This increases the importance of...

## Failure Modes

The main failure mode is skipping confirmation steps because the headline seems obvious. A dovish statement can still fail if Q&A tone turns cautious or if long-end yields reprice higher into the close. Mega-cap concentration can mask weak breadth, so index-level strength without broad participation often leads to late-session fade and poor risk-adjusted continuation. This matters because the historical distribution is built on end-of-window outcomes, not the first minute of price discovery. A release can look constructive initially, then fail once rates, the dollar, and sector breadth reprice in a different direction. That is also why low sample environments and mixed reaction functions should be handled as weaker evidence.

## Execution Relevance

Treat this page as an execution checklist input, not a buy or sell signal. The practical takeaway is to use the current page as a decision filter: read the release, compare it with the hub baseline, then decide whether the event is behaving like a normal FOMC setup or a tail observation. For this asset-event pair, the operational checklist is: Track implied cuts path before and after statement.; Wait for confirmation after Q&A begins.; Size positions based on realized volatility percentile.. When the page is marked within historical norm, the right response is not automatically to trade more aggressively; it is to decide whether confirmation quality is strong enough to justify action.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
