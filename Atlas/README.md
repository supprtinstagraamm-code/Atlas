# Atlas Business Operating System

**Status:** Experimental  
**Version:** 1.0.0  
**Owner:** Atlas Studio  
**Review date:** 2026-10-07  
**Change history:** 1.0.0 - Initial Atlas operating-system release candidate.

Atlas is the operating system for a Quiet Architectural, accessible-premium resin home-decor brand. It keeps evidence, product hypotheses, scoring, technical QA, marketplace packaging, and release governance connected through one canonical contract.

## What Atlas controls

- Product recommendations must be evidence-backed, scored, and assigned to exactly one collection.
- Atlas Scores use the canonical 14-factor weighting contract plus a 0-to-10 risk penalty.
- Hard QA failures override the score and force rejection.
- Unknown evidence stays visible instead of being converted into fake certainty.
- Workbook outputs are regenerated from source records instead of hand-edited.

## Founder path

1. Start with [business strategy](business/BUSINESS_STRATEGY.md).
2. Confirm commercial rules in [business model](business/BUSINESS_MODEL.md) and [pricing handbook](business/PRICING_HANDBOOK.md).
3. Review the current launch set in [launch collection](collections/launch-collection.md).
4. Check release readiness in [verification report](docs/VERIFICATION_REPORT.md).

## Product designer path

1. Read [brand guidelines](brand/BRAND_GUIDELINES.md) and [design tokens](brand/DESIGN_TOKENS.md).
2. Apply [product design rules](standards/PRODUCT_DESIGN_RULES.md).
3. Validate technical assumptions with [resin printing standards](standards/RESIN_PRINTING_STANDARDS.md).
4. Review current product records under [products](products).

## Researcher path

1. Follow the [operating workflow](docs/OPERATING_WORKFLOW.md).
2. Add evidence using [data dictionary](schema/DATA_DICTIONARY.md) field rules.
3. Refresh source conventions in [market research](research/MARKET_RESEARCH.md).
4. Recheck governance in [release checklist](docs/RELEASE_CHECKLIST.md).

## Listing creator path

1. Start with [SEO handbook](seo/SEO_HANDBOOK.md).
2. Use [listing templates](seo/LISTING_TEMPLATES.md).
3. Match the target channel with the right marketplace playbook in [marketplaces](marketplaces).
4. Keep all claims aligned with the product record and evidence register.

## Reviewer path

1. Run the [quality assurance standard](standards/QUALITY_ASSURANCE.md).
2. Review approval rules in [governance](docs/GOVERNANCE.md).
3. Validate workbook and score behavior with [verification report](docs/VERIFICATION_REPORT.md).
4. Confirm release steps in [release checklist](docs/RELEASE_CHECKLIST.md).

## Core map

- Contract: [schema](schema)
- Business: [business](business)
- Brand: [brand](brand)
- Standards: [standards](standards)
- Marketplaces: [marketplaces](marketplaces)
- SEO: [seo](seo)
- Research: [research](research)
- Collections: [collections](collections)
- Products: [products](products)
- Workbook: [excel](excel)
- Prompts: [prompts](prompts)
- Governance docs: [docs](docs)
- Roadmap: [roadmap](roadmap)

## Release commands

```powershell
.\.venv\Scripts\python.exe -m pytest -v
.\.venv\Scripts\python.exe .\tools\build_workbook.py
.\.venv\Scripts\python.exe .\tools\release_audit.py
```

## Refresh commands

```powershell
.\.venv\Scripts\python.exe -m pytest .\tests\test_launch_collection.py -v
.\.venv\Scripts\python.exe -m pytest .\tests\test_workbook.py -v
.\.venv\Scripts\python.exe .\tools\build_workbook.py
```
