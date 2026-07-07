import json
from copy import deepcopy
from pathlib import Path

import pytest
from jsonschema import ValidationError, validate

from tools.validate_atlas import load_contract, validate_repository


ROOT = Path(__file__).parents[1]


def load_schema(name):
    return json.loads((ROOT / "Atlas" / "schema" / name).read_text(encoding="utf-8"))


@pytest.fixture
def valid_product():
    factors = [
        "market_demand", "competition_opportunity", "profitability",
        "evergreen_potential", "brand_alignment", "collection_potential",
        "bundle_potential", "physical_product_potential", "seo_opportunity",
        "resin_printability", "ai_production_efficiency", "customer_value",
        "production_simplicity", "marketplace_fit",
    ]
    return {
        "product_id": "ATL-QA-001-001",
        "collection_id": "ATL-QA-001",
        "name": "Arc Vessel",
        "status": "Draft",
        "version": "1.0.0",
        "owner": "Atlas Studio",
        "review_date": "2026-07-07",
        "lifecycle_stage": "Idea",
        "confidence": "Medium",
        "product_dna": {
            key: "Documented hypothesis"
            for key in [
                "core_purpose", "design_philosophy", "emotional_appeal",
                "target_customer", "functional_benefits", "decorative_benefits",
                "print_complexity", "material_efficiency", "brand_alignment",
                "future_evolution", "physical_manufacturing_potential",
            ]
        },
        "design_tokens": {
            key: "Quiet Architectural"
            for key in [
                "corner_radius", "wall_thickness", "chamfer_style", "fillet_style",
                "edge_language", "texture_density", "surface_finish", "relief_depth",
                "pattern_scale", "shadow_language", "visual_weight", "design_balance",
                "material_simulation",
            ]
        },
        "evidence_ids": ["EVD-001"],
        "scores": {
            key: {"score": 7, "rationale": "Supported by EVD-001"}
            for key in factors
        },
        "risk_penalty": 2,
        "atlas_score": 68.0,
        "strengths": ["Coherent collection fit"],
        "weaknesses": ["Requires prototype validation"],
        "risks": ["Support scarring is untested"],
        "improvement_actions": ["Print two orientations"],
        "expansion_opportunities": ["Mini and XL variants"],
        "change_history": [{"version": "1.0.0", "date": "2026-07-07", "change": "Initial hypothesis"}],
    }


def test_valid_product_matches_contract(valid_product):
    validate(valid_product, load_schema("product.schema.json"))


def test_malformed_product_id_is_rejected(valid_product):
    invalid = deepcopy(valid_product)
    invalid["product_id"] = "ARC-1"
    with pytest.raises(ValidationError):
        validate(invalid, load_schema("product.schema.json"))


def test_multiple_collection_ids_are_rejected(valid_product):
    invalid = deepcopy(valid_product)
    invalid["collection_id"] = ["ATL-QA-001", "ATL-QA-002"]
    with pytest.raises(ValidationError):
        validate(invalid, load_schema("product.schema.json"))


def test_missing_score_rationale_is_rejected(valid_product):
    invalid = deepcopy(valid_product)
    del invalid["scores"]["market_demand"]["rationale"]
    with pytest.raises(ValidationError):
        validate(invalid, load_schema("product.schema.json"))


def test_unsupported_confidence_is_rejected(valid_product):
    invalid = deepcopy(valid_product)
    invalid["confidence"] = "Certain"
    with pytest.raises(ValidationError):
        validate(invalid, load_schema("product.schema.json"))


def test_missing_stored_atlas_score_is_rejected(valid_product):
    invalid = deepcopy(valid_product)
    del invalid["atlas_score"]
    with pytest.raises(ValidationError):
        validate(invalid, load_schema("product.schema.json"))


def test_load_contract_returns_canonical_weights():
    contract = load_contract(ROOT)
    assert contract["factor_weights"]["market_demand"] == 0.14


def test_repository_validator_reports_invalid_product(tmp_path, valid_product):
    schema_dir = tmp_path / "Atlas" / "schema"
    schema_dir.mkdir(parents=True)
    schema_dir.joinpath("controlled-vocabularies.json").write_text(
        (ROOT / "Atlas" / "schema" / "controlled-vocabularies.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    schema_dir.joinpath("product.schema.json").write_text(
        (ROOT / "Atlas" / "schema" / "product.schema.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    product_dir = tmp_path / "Atlas" / "products" / "data"
    product_dir.mkdir(parents=True)
    valid_product["confidence"] = "Certain"
    product_dir.joinpath("invalid.json").write_text(json.dumps(valid_product), encoding="utf-8")

    errors = validate_repository(tmp_path)

    assert len(errors) == 1
    assert "invalid.json" in errors[0]
