import pytest

from tools.validate_atlas import FACTOR_KEYS, calculate_atlas_score


WEIGHTS = {
    "market_demand": 0.14,
    "competition_opportunity": 0.08,
    "profitability": 0.10,
    "evergreen_potential": 0.10,
    "brand_alignment": 0.10,
    "collection_potential": 0.07,
    "bundle_potential": 0.07,
    "physical_product_potential": 0.06,
    "seo_opportunity": 0.07,
    "resin_printability": 0.08,
    "ai_production_efficiency": 0.03,
    "customer_value": 0.05,
    "production_simplicity": 0.03,
    "marketplace_fit": 0.02,
}


def test_weights_cover_all_factors_and_sum_to_one():
    assert set(WEIGHTS) == FACTOR_KEYS
    assert sum(WEIGHTS.values()) == pytest.approx(1.0)


def test_perfect_scores_with_no_risk_return_one_hundred():
    scores = {key: 10 for key in FACTOR_KEYS}
    assert calculate_atlas_score(scores, 0, WEIGHTS) == 100.0


def test_risk_penalty_is_deducted_from_weighted_base():
    scores = {key: 10 for key in FACTOR_KEYS}
    assert calculate_atlas_score(scores, 7.5, WEIGHTS) == 92.5


def test_missing_factor_is_rejected():
    scores = {key: 8 for key in FACTOR_KEYS}
    scores.pop("market_demand")
    with pytest.raises(ValueError, match="all 14 canonical factors"):
        calculate_atlas_score(scores, 2, WEIGHTS)


@pytest.mark.parametrize("penalty", [-0.1, 10.1])
def test_out_of_range_risk_penalty_is_rejected(penalty):
    scores = {key: 8 for key in FACTOR_KEYS}
    with pytest.raises(ValueError, match="between 0 and 10"):
        calculate_atlas_score(scores, penalty, WEIGHTS)


def test_out_of_range_factor_score_is_rejected():
    scores = {key: 8 for key in FACTOR_KEYS}
    scores["profitability"] = 11
    with pytest.raises(ValueError, match="between 0 and 10"):
        calculate_atlas_score(scores, 2, WEIGHTS)
