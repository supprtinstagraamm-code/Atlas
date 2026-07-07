from pathlib import Path


ROOT = Path(__file__).parents[1]
PROMPTS = ROOT / "Atlas" / "prompts"
REQUIRED = [
    "SYSTEM_PROMPT.md", "AI_BEHAVIOR.md", "DESIGN_RULES.md", "PRODUCT_DNA.md",
    "PRODUCT_SCORING.md", "MARKETPLACE_RULES.md", "COLLECTION_RULES.md",
    "PRINTING_RULES.md", "RENDER_RULES.md", "SEO_RULES.md", "NAMING_RULES.md",
    "BRAND_GUIDELINES.md", "CONTENT_STRATEGY.md", "PRICING_ENGINE.md",
    "ROADMAP.md", "BUSINESS_MODEL.md", "PROMPT_LIBRARY.md", "QUALITY_CONTROL.md",
]
SECTIONS = ["## Purpose", "## Required inputs", "## Rules", "## Output contract", "## Unknown or refusal behavior", "## Quality checklist"]
FACTORS = [
    "Market Demand", "Competition Opportunity", "Profitability", "Evergreen Potential",
    "Brand Alignment", "Collection Potential", "Bundle Potential",
    "Physical Product Potential", "SEO Opportunity", "Resin Printability",
    "AI Production Efficiency", "Customer Value", "Production Simplicity", "Marketplace Fit",
]


def test_all_required_prompt_files_exist():
    assert sorted(path.name for path in PROMPTS.glob("*.md")) == sorted(REQUIRED)


def test_each_prompt_is_self_contained():
    for name in REQUIRED:
        text = (PROMPTS / name).read_text(encoding="utf-8")
        assert all(section in text for section in SECTIONS), name
        assert "Never fabricate" in text, name
        assert "High Confidence" in text and "Medium Confidence" in text and "Low Confidence" in text, name


def test_product_scoring_names_every_factor_and_required_decision_output():
    text = (PROMPTS / "PRODUCT_SCORING.md").read_text(encoding="utf-8")
    assert all(factor in text for factor in FACTORS)
    for heading in ["Facts", "Assumptions", "Evidence", "Scores", "Decision", "Strengths", "Weaknesses", "Risks", "Improvements", "Expansion", "Confidence"]:
        assert heading in text
    assert "search volume" in text and "sales estimates" in text
