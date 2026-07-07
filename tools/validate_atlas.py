"""Canonical Atlas validation and scoring helpers."""

import json
from pathlib import Path

from jsonschema import Draft202012Validator

FACTOR_KEYS = {
    "market_demand",
    "competition_opportunity",
    "profitability",
    "evergreen_potential",
    "brand_alignment",
    "collection_potential",
    "bundle_potential",
    "physical_product_potential",
    "seo_opportunity",
    "resin_printability",
    "ai_production_efficiency",
    "customer_value",
    "production_simplicity",
    "marketplace_fit",
}


def calculate_atlas_score(scores, risk_penalty, weights):
    """Return a 0–100 weighted score after applying the risk penalty."""
    if set(scores) != FACTOR_KEYS or set(weights) != FACTOR_KEYS:
        raise ValueError("Atlas Score requires all 14 canonical factors")
    if not 0 <= risk_penalty <= 10:
        raise ValueError("risk_penalty must be between 0 and 10")
    if abs(sum(weights.values()) - 1.0) > 1e-9:
        raise ValueError("weights must sum to 1.0")
    if any(not 0 <= value <= 10 for value in scores.values()):
        raise ValueError("factor scores must be between 0 and 10")
    base = sum(scores[key] * 10 * weights[key] for key in FACTOR_KEYS)
    return round(base - risk_penalty, 2)


def load_contract(root: Path) -> dict:
    """Load canonical controlled vocabularies from a repository root."""
    path = Path(root) / "Atlas" / "schema" / "controlled-vocabularies.json"
    return json.loads(path.read_text(encoding="utf-8"))


def validate_repository(root: Path) -> list[str]:
    """Return schema errors for structured product records."""
    root = Path(root)
    schema_path = root / "Atlas" / "schema" / "product.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors = []
    product_dir = root / "Atlas" / "products" / "data"
    if not product_dir.exists():
        return errors
    for path in sorted(product_dir.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        for error in validator.iter_errors(record):
            location = ".".join(str(part) for part in error.absolute_path) or "record"
            errors.append(f"{path.name}:{location}: {error.message}")
    return errors
