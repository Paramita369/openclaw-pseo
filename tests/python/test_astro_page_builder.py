from __future__ import annotations

from astro_page_builder import compose_core_body


def build_body(trigger: str) -> str:
    return compose_core_body(
        slug="btc-after-cpi-2026-02-12",
        asset="BTC",
        event_label="CPI",
        event_direction="up",
        event_actual=326.588,
        event_previous=326.031,
        event_delta=0.557,
        probabilities={
            "t7": {"up": 57.14, "down": 42.86, "median": 3.64},
            "conditional": {"sample_size": 13, "t7": {"up": 61.54, "median": 4.10}},
        },
        metrics={"impact_t7_pct": 5.25},
        signal="Bullish",
        features={
            "narrative_trigger": trigger,
            "z_score_t7": 1.75 if "outperformance" in trigger else (-1.75 if "underperformance" in trigger else 0.1),
            "percentile_t7": 92.0 if trigger == "extreme_outperformance" else 76.0 if trigger == "moderate_outperformance" else 54.0 if trigger == "strict_median_norm" else 22.0 if trigger == "moderate_underperformance" else 8.0 if trigger == "extreme_underperformance" else 0.0,
            "hub_baseline_mean_t7": 1.69,
            "hub_baseline_median_t7": 3.64,
            "hub_baseline_std_t7": 8.5155,
            "hub_baseline_delta": 1.61,
            "sample_size": 13 if trigger != "low_context" else 4,
        },
        brief={
            "thesis": "Bitcoin should be framed through liquidity sensitivity and not through a single inflation headline.",
            "what_changed_recently": "ETF flow sensitivity and rate repricing are now more important than they were in the earlier tightening cycle.",
            "risk_watchouts": "Funding pressure and cross-asset confirmation failures can break the initial read quickly.",
            "execution_checklist": [
                "Wait for rates confirmation before acting on the initial move.",
                "Check dollar strength before upgrading conviction.",
                "Define invalidation before sizing any directional view.",
            ],
        },
    )


def test_compose_core_body_semantic_divergence() -> None:
    extreme_positive = build_body("extreme_outperformance").lower()
    median_norm = build_body("strict_median_norm").lower()
    extreme_negative = build_body("extreme_underperformance").lower()
    low_context = build_body("low_context").lower()

    assert "upper decile" in extreme_positive or "tail" in extreme_positive
    assert "reversion risk" in extreme_positive
    assert "median band" in median_norm or "calibration" in median_norm
    assert "tail" not in median_norm
    assert "weak tail" in extreme_negative or "downside tail" in extreme_negative
    assert "insufficient sample" in low_context or "research breadcrumb" in low_context
    assert extreme_positive != median_norm
    assert extreme_negative != median_norm


def test_compose_core_body_moderate_buckets_have_required_anchors() -> None:
    moderate_positive = build_body("moderate_outperformance").lower()
    moderate_negative = build_body("moderate_underperformance").lower()

    assert "above baseline" in moderate_positive or "constructive" in moderate_positive
    assert "below baseline" in moderate_negative or "fragile" in moderate_negative
    assert "bounce risk" in moderate_negative
