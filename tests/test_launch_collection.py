import json
import re
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validate_atlas import calculate_atlas_score


ROOT = Path(__file__).parents[1]
ATLAS = ROOT / "Atlas"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_evidence_register_has_traceable_records():
    records = read_json(ATLAS / "research" / "evidence.json")
    required = {"evidence_id", "claim", "source_url", "accessed_at", "marketplace", "evidence_type", "confidence", "notes"}
    assert len(records) >= 8
    assert all(set(record) == required for record in records)
    assert all(re.fullmatch(r"EVD-[0-9]{3,}", record["evidence_id"]) for record in records)
    assert all(record["accessed_at"] == "2026-07-07" for record in records)


def test_seven_launch_product_records_pass_schema_and_reference_evidence():
    schema = read_json(ATLAS / "schema" / "product.schema.json")
    validator = Draft202012Validator(schema)
    evidence_ids = {item["evidence_id"] for item in read_json(ATLAS / "research" / "evidence.json")}
    paths = sorted((ATLAS / "products" / "data").glob("ATL-QA-001-*.json"))
    assert len(paths) == 7
    for path in paths:
        product = read_json(path)
        assert list(validator.iter_errors(product)) == []
        assert set(product["evidence_ids"]) <= evidence_ids
        assert all("EVD-" in item["rationale"] or "Unknown" in item["rationale"] for item in product["scores"].values())


def test_stored_atlas_scores_reproduce_from_canonical_weights():
    weights = read_json(ATLAS / "schema" / "controlled-vocabularies.json")["factor_weights"]
    for path in (ATLAS / "products" / "data").glob("*.json"):
        product = read_json(path)
        raw_scores = {key: value["score"] for key, value in product["scores"].items()}
        expected = calculate_atlas_score(raw_scores, product["risk_penalty"], weights)
        assert product["atlas_score"] == expected


def test_collection_has_one_hero_six_supporting_and_required_expansions():
    collection = read_json(ATLAS / "collections" / "launch-collection.json")
    schema = read_json(ATLAS / "schema" / "collection.schema.json")
    assert list(Draft202012Validator(schema).iter_errors(collection)) == []
    assert collection["collection_id"] == "ATL-QA-001"
    assert len(collection["supporting_product_ids"]) == 6
    assert collection["hero_product_id"] not in collection["supporting_product_ids"]


def test_each_product_has_human_readable_decision_record():
    for number in range(1, 8):
        path = ATLAS / "products" / f"ATL-QA-001-{number:03}.md"
        text = path.read_text(encoding="utf-8")
        for heading in ["## Decision", "## Score reasoning", "## Strengths", "## Weaknesses", "## Risks", "## Improvement actions", "## Expansion opportunities", "## Confidence"]:
            assert heading in text, f"{path.name}: {heading}"
