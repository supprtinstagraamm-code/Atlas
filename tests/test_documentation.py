import re
from pathlib import Path


ROOT = Path(__file__).parents[1]
ATLAS = ROOT / "Atlas"

REQUIRED_DOCS = [
    "README.md",
    "business/BUSINESS_STRATEGY.md", "business/BUSINESS_MODEL.md",
    "business/PRICING_HANDBOOK.md", "business/LICENSING.md",
    "brand/BRAND_GUIDELINES.md", "brand/DESIGN_TOKENS.md",
    "brand/AUDIENCE_AND_POSITIONING.md",
    "marketplaces/ETSY.md", "marketplaces/CULTS3D.md", "marketplaces/GUMROAD.md",
    "marketplaces/PRINTABLES.md", "marketplaces/MYMINIFACTORY.md",
    "marketplaces/MAKERWORLD.md", "marketplaces/KO_FI.md",
    "standards/PRODUCT_DESIGN_RULES.md", "standards/RESIN_PRINTING_STANDARDS.md",
    "standards/RENDERING_STANDARDS.md", "standards/NAMING_RULES.md",
    "standards/QUALITY_ASSURANCE.md",
    "seo/SEO_HANDBOOK.md", "seo/LISTING_TEMPLATES.md",
    "docs/ARCHITECTURE.md", "docs/GOVERNANCE.md", "docs/OPERATING_WORKFLOW.md",
    "docs/AI_WORKFLOW.md", "roadmap/ROADMAP.md", "roadmap/LIFECYCLE.md",
]


def test_required_documentation_exists():
    missing = [path for path in REQUIRED_DOCS if not (ATLAS / path).exists()]
    assert missing == []


def test_documents_have_governance_metadata():
    required = ["**Status:**", "**Version:**", "**Owner:**", "**Review date:**", "**Change history:**"]
    for relative in REQUIRED_DOCS:
        text = (ATLAS / relative).read_text(encoding="utf-8")
        assert all(field in text for field in required), relative


def test_documents_have_no_unfinished_markers():
    forbidden = re.compile(r"\b(?:TBD|TODO|FIXME)\b|\[insert[^\]]*\]", re.IGNORECASE)
    for relative in REQUIRED_DOCS:
        text = (ATLAS / relative).read_text(encoding="utf-8")
        assert forbidden.search(text) is None, relative


def test_relative_markdown_links_resolve():
    pattern = re.compile(r"\[[^\]]+\]\((?!https?://|#)([^)]+\.md(?:#[^)]+)?)\)")
    failures = []
    for relative in REQUIRED_DOCS:
        path = ATLAS / relative
        for target in pattern.findall(path.read_text(encoding="utf-8")):
            target_path = target.split("#", 1)[0]
            if not (path.parent / target_path).resolve().exists():
                failures.append(f"{relative} -> {target}")
    assert failures == []
