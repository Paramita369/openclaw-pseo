from __future__ import annotations

from content_features import (
    compute_statistical_features,
    narrative_direction_band,
    narrative_rank_band,
    resolve_narrative_trigger,
)


def test_low_context_trigger_when_sample_too_small() -> None:
    features = compute_statistical_features(1.2, [0.1, 0.2, 0.3])
    assert features.narrative_trigger == "low_context"
    assert features.narrative_rank_band == "low_context"
    assert features.narrative_direction_band == "unknown"
    assert features.z_score_t7 == 0.0
    assert features.percentile_t7 == 0.0


def test_zero_std_clamps_z_score_to_zero() -> None:
    features = compute_statistical_features(1.0, [1.0] * 8)
    assert features.z_score_t7 == 0.0
    assert 0.0 <= features.percentile_t7 <= 100.0


def test_extreme_outperformance_trigger_resolution() -> None:
    assert resolve_narrative_trigger(1.6, 88.0, 20) == "extreme_outperformance"


def test_moderate_outperformance_trigger_resolution() -> None:
    assert resolve_narrative_trigger(0.8, 72.0, 20) == "moderate_outperformance"


def test_strict_median_norm_trigger_resolution() -> None:
    assert resolve_narrative_trigger(0.1, 55.0, 20) == "strict_median_norm"


def test_moderate_underperformance_trigger_resolution() -> None:
    assert resolve_narrative_trigger(-0.7, 20.0, 20) == "moderate_underperformance"


def test_extreme_underperformance_trigger_resolution() -> None:
    assert resolve_narrative_trigger(-1.7, 8.0, 20) == "extreme_underperformance"


def test_conflicting_zscore_and_percentile_choose_more_extreme_bucket() -> None:
    assert resolve_narrative_trigger(0.3, 91.0, 20) == "extreme_outperformance"
    assert resolve_narrative_trigger(-0.8, 42.0, 20) == "moderate_underperformance"


def test_rank_and_direction_band_mappings() -> None:
    assert narrative_rank_band("extreme_outperformance") == "extreme"
    assert narrative_rank_band("moderate_underperformance") == "moderate"
    assert narrative_rank_band("strict_median_norm") == "median"
    assert narrative_direction_band("moderate_outperformance") == "positive"
    assert narrative_direction_band("extreme_underperformance") == "negative"
    assert narrative_direction_band("low_context") == "unknown"
