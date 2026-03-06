from __future__ import annotations

from content_features import compute_statistical_features


def test_low_context_trigger_when_baseline_too_small() -> None:
    features = compute_statistical_features(1.2, [0.1, 0.2, 0.3])
    assert features.narrative_trigger == 'low_context'
    assert features.z_score_t7 == 0.0
    assert features.percentile_t7 == 0.0


def test_zero_std_clamps_z_score() -> None:
    features = compute_statistical_features(1.0, [1.0] * 8)
    assert features.z_score_t7 == 0.0
    assert 0.0 <= features.percentile_t7 <= 100.0


def test_significant_outperformance_trigger() -> None:
    features = compute_statistical_features(8.0, [0.5, 0.8, 1.0, 0.3, 1.1, 0.9, 0.7, 1.2, 1.0, 0.4])
    assert features.narrative_trigger == 'significant_outperformance'


def test_significant_underperformance_trigger() -> None:
    features = compute_statistical_features(-5.0, [0.5, 0.8, 1.0, 0.3, 1.1, 0.9, 0.7, 1.2, 1.0, 0.4])
    assert features.narrative_trigger == 'significant_underperformance'
