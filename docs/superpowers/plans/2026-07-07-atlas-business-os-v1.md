# Atlas Business Operating System v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a schema-centered Markdown and Excel operating system for evaluating, documenting, and scaling an accessible-premium Quiet Architectural resin home-decor brand.

**Architecture:** Canonical JSON schemas and controlled vocabularies define the operating contract. Markdown playbooks, structured launch-product records, prompts, and a generated Excel workbook consume that contract; Python validators enforce consistency and produce a release audit.

**Tech Stack:** Markdown, JSON Schema Draft 2020-12, Python 3.11+, pytest 8.x, jsonschema 4.x, openpyxl 3.1.x, Git.

## Global Constraints

- Repository deliverables live under `Atlas/`; implementation support code and tests live under `tools/` and `tests/`.
- Product domain is resin-printable home decor with a Quiet Architectural visual direction and accessible-premium positioning.
- Primary market evidence comes from current Etsy and Cults3D research; every source records its URL and access date.
- Never invent search volume, sales, demand, revenue, or marketplace statistics.
- Evidence type is exactly one of `Verified`, `Proxy`, `Assumption`, or `Unknown`; confidence is exactly one of `High`, `Medium`, or `Low`.
- Every product belongs to exactly one collection and uses an `ATL-QA-CCC-PPP` identifier.
- Every recommended product includes score reasoning, strengths, weaknesses, risks, improvement actions, expansion opportunities, and confidence.
- Hard QA failures override the numeric score and force rejection.
- Atlas Score uses the approved 14-factor weights and a documented 0-to-10-point risk penalty.
- Out of scope: STL modeling, automated marketplace scraping, live APIs, inventory management, and a software dashboard.
- All major assets include status, semantic version, owner, review date, and change history.

## File Map

- `Atlas/README.md`: top-level navigation and operating-system quick start.
- `Atlas/schema/*.schema.json`: canonical product, collection, evidence, scoring, and QA contracts.
- `Atlas/schema/controlled-vocabularies.json`: enums, weights, lifecycle states, statuses, and decision bands.
- `Atlas/schema/DATA_DICTIONARY.md`: human-readable contract.
- `Atlas/business/*.md`: strategy, business model, pricing, and licensing.
- `Atlas/brand/*.md`: brand guidelines, audience, and design tokens.
- `Atlas/marketplaces/*.md`: seven marketplace playbooks.
- `Atlas/standards/*.md`: design, printing, rendering, naming, and QA rules.
- `Atlas/seo/*.md`: SEO methodology and listing rules.
- `Atlas/collections/launch-collection.md`: researched collection architecture and decisions.
- `Atlas/products/*.md`: human-readable launch-product decision records.
- `Atlas/research/evidence.json`: canonical evidence register.
- `Atlas/research/MARKET_RESEARCH.md`: sourced Etsy and Cults3D synthesis.
- `Atlas/prompts/*.md`: the 18 required prompt files.
- `Atlas/excel/Atlas_Business_OS_v1.0.0.xlsx`: generated operational workbook.
- `Atlas/roadmap/*.md`: release roadmap and lifecycle plan.
- `Atlas/docs/*.md`: governance, workflows, architecture, and navigation.
- `tools/validate_atlas.py`: repository contract validator.
- `tools/build_workbook.py`: deterministic workbook generator.
- `tools/release_audit.py`: combined validation and release report generator.
- `tests/`: schema, scoring, workbook, prompts, links, and integration tests.

---

### Task 1: Canonical Schema and Score Engine

**Files:**
- Create: `requirements-dev.txt`
- Create: `Atlas/schema/controlled-vocabularies.json`
- Create: `Atlas/schema/evidence.schema.json`
- Create: `Atlas/schema/collection.schema.json`
- Create: `Atlas/schema/product.schema.json`
- Create: `Atlas/schema/DATA_DICTIONARY.md`
- Create: `tools/validate_atlas.py`
- Create: `tests/test_schema.py`
- Create: `tests/test_scoring.py`

**Interfaces:**
- Consumes: approved weights and governance rules from the design specification.
- Produces: `load_contract(root: Path) -> dict`, `calculate_atlas_score(scores: dict[str, float], risk_penalty: float, weights: dict[str, float]) -> float`, and `validate_repository(root: Path) -> list[str]`.

- [ ] **Step 1: Add pinned development dependencies**

Create `requirements-dev.txt` with:

```text
jsonschema>=4.22,<5
openpyxl>=3.1,<4
pytest>=8,<9
```

Run: `python -m pip install -r requirements-dev.txt`
Expected: all three packages install successfully.

- [ ] **Step 2: Write failing score tests**

Create `tests/test_scoring.py` with tests asserting that the 14 weights sum to `1.0`, all-ten inputs with zero risk return `100.0`, a `7.5` risk penalty returns `92.5`, missing factors raise `ValueError`, and risk outside `0..10` raises `ValueError`.

Run: `python -m pytest tests/test_scoring.py -v`
Expected: FAIL because `tools.validate_atlas` does not exist.

- [ ] **Step 3: Implement the minimal score contract**

In `tools/validate_atlas.py`, define the approved keys and implement:

```python
from pathlib import Path
import json

FACTOR_KEYS = {
    "market_demand", "competition_opportunity", "profitability",
    "evergreen_potential", "brand_alignment", "collection_potential",
    "bundle_potential", "physical_product_potential", "seo_opportunity",
    "resin_printability", "ai_production_efficiency", "customer_value",
    "production_simplicity", "marketplace_fit",
}

def calculate_atlas_score(scores, risk_penalty, weights):
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
```

- [ ] **Step 4: Add canonical vocabularies and JSON schemas**

Define exact weights as decimals (`0.14`, `0.08`, `0.10`, `0.10`, `0.10`, `0.07`, `0.07`, `0.06`, `0.07`, `0.08`, `0.03`, `0.05`, `0.03`, `0.02`), lifecycle stages, asset statuses, evidence types, confidence values, QA statuses, and decision bands in `controlled-vocabularies.json`. Require product DNA, design tokens, evidence references, all factor scores and rationales, strengths, weaknesses, risks, improvements, expansions, lifecycle, version, and exactly one `collection_id` in `product.schema.json`.

- [ ] **Step 5: Write and run schema tests**

Test one valid product, rejection of a malformed ID, rejection of two collection IDs, rejection of a missing rationale, and rejection of an unsupported confidence value.

Run: `python -m pytest tests/test_schema.py tests/test_scoring.py -v`
Expected: all tests PASS.

- [ ] **Step 6: Document and commit the canonical contract**

Document every field, type, allowed value, unit, ownership rule, and update trigger in `DATA_DICTIONARY.md`.

Run: `git add requirements-dev.txt Atlas/schema tools/validate_atlas.py tests/test_schema.py tests/test_scoring.py && git commit -m "feat: add Atlas canonical schema and score engine"`
Expected: one commit containing only Task 1 files.

---

### Task 2: Business, Brand, Marketplace, and Production Documentation

**Files:**
- Create: `Atlas/README.md`
- Create: `Atlas/business/BUSINESS_STRATEGY.md`
- Create: `Atlas/business/BUSINESS_MODEL.md`
- Create: `Atlas/business/PRICING_HANDBOOK.md`
- Create: `Atlas/business/LICENSING.md`
- Create: `Atlas/brand/BRAND_GUIDELINES.md`
- Create: `Atlas/brand/DESIGN_TOKENS.md`
- Create: `Atlas/brand/AUDIENCE_AND_POSITIONING.md`
- Create: `Atlas/marketplaces/{ETSY,CULTS3D,GUMROAD,PRINTABLES,MYMINIFACTORY,MAKERWORLD,KO_FI}.md`
- Create: `Atlas/standards/{PRODUCT_DESIGN_RULES,RESIN_PRINTING_STANDARDS,RENDERING_STANDARDS,NAMING_RULES,QUALITY_ASSURANCE}.md`
- Create: `Atlas/seo/{SEO_HANDBOOK,LISTING_TEMPLATES}.md`
- Create: `Atlas/docs/{ARCHITECTURE,GOVERNANCE,OPERATING_WORKFLOW,AI_WORKFLOW}.md`
- Create: `Atlas/roadmap/{ROADMAP,LIFECYCLE}.md`
- Create: `tests/test_documentation.py`

**Interfaces:**
- Consumes: canonical vocabulary and field names from Task 1.
- Produces: linked operating rules that prompt files and launch-product records cite by stable relative path.

- [ ] **Step 1: Write failing documentation tests**

Test that every listed file exists, contains `Status`, `Version`, `Owner`, `Review date`, and `Change history`, passes the validator's unfinished-content scan, and that every relative Markdown link resolves.

Run: `python -m pytest tests/test_documentation.py -v`
Expected: FAIL with missing document paths.

- [ ] **Step 2: Write the business and brand core**

Define accessible-premium positioning, Quiet Architectural principles, audience, value proposition, licensing tiers, cost-based pricing inputs, validation rules, and the exact design-token vocabulary. Clearly label financial examples as assumptions until replaced with sourced costs.

- [ ] **Step 3: Write marketplace playbooks**

Give each marketplace document these exact sections: `Role in Portfolio`, `Customer Intent`, `Suitable Products`, `Listing Requirements`, `Image Sequence`, `Copy Structure`, `SEO Rules`, `Pricing and Licensing`, `Success Evidence`, `Risks`, and `Release Checklist`. Preserve the marketplace priorities approved in the specification.

- [ ] **Step 4: Write production, SEO, governance, and workflow standards**

Define resin QA checkpoints without claiming universal dimensions; require prototype validation for wall thickness, supports, drainage, stability, cure behavior, and fit. Define evidence refresh, versioning, approvals, retirement, and the ten-step operating workflow.

- [ ] **Step 5: Run documentation tests and commit**

Run: `python -m pytest tests/test_documentation.py -v`
Expected: all tests PASS.

Run: `git add Atlas tests/test_documentation.py && git commit -m "docs: add Atlas operating playbooks and standards"`
Expected: one documentation commit.

---

### Task 3: Prompt Engineering Repository

**Files:**
- Create: all 18 required files under `Atlas/prompts/`
- Create: `tests/test_prompts.py`

**Interfaces:**
- Consumes: schema fields, evidence types, confidence rules, QA gates, and operating documentation.
- Produces: self-contained prompts with the output sections `Facts`, `Assumptions`, `Evidence`, `Scores`, `Decision`, `Strengths`, `Weaknesses`, `Risks`, `Improvements`, `Expansion`, and `Confidence` where product evaluation applies.

- [ ] **Step 1: Write failing prompt-contract tests**

Require all 18 filenames; require each file to contain purpose, required inputs, rules, output contract, refusal/unknown behavior, and quality checklist; require scoring prompts to name all 14 factors and forbid fabricated statistics.

Run: `python -m pytest tests/test_prompts.py -v`
Expected: FAIL because prompt files do not exist.

- [ ] **Step 2: Author system, behavior, and domain prompts**

Write `SYSTEM_PROMPT.md`, `AI_BEHAVIOR.md`, `DESIGN_RULES.md`, `PRODUCT_DNA.md`, `PRODUCT_SCORING.md`, `MARKETPLACE_RULES.md`, `COLLECTION_RULES.md`, `PRINTING_RULES.md`, and `RENDER_RULES.md` with explicit inputs and deterministic output headings.

- [ ] **Step 3: Author commercial and governance prompts**

Write `SEO_RULES.md`, `NAMING_RULES.md`, `BRAND_GUIDELINES.md`, `CONTENT_STRATEGY.md`, `PRICING_ENGINE.md`, `ROADMAP.md`, `BUSINESS_MODEL.md`, `PROMPT_LIBRARY.md`, and `QUALITY_CONTROL.md`. Pricing must distinguish facts from assumptions and refuse unsupported profit claims.

- [ ] **Step 4: Test and commit prompts**

Run: `python -m pytest tests/test_prompts.py tests/test_documentation.py -v`
Expected: all tests PASS.

Run: `git add Atlas/prompts tests/test_prompts.py && git commit -m "feat: add Atlas prompt engineering repository"`
Expected: one prompt-repository commit.

---

### Task 4: Current Market Research and Launch Collection

**Files:**
- Create: `Atlas/research/evidence.json`
- Create: `Atlas/research/MARKET_RESEARCH.md`
- Create: `Atlas/collections/COLLECTION_HANDBOOK.md`
- Create: `Atlas/collections/launch-collection.md`
- Create: `Atlas/products/ATL-QA-001-001.md`
- Create: `Atlas/products/ATL-QA-001-002.md`
- Create: `Atlas/products/ATL-QA-001-003.md`
- Create: `Atlas/products/ATL-QA-001-004.md`
- Create: `Atlas/products/ATL-QA-001-005.md`
- Create: `Atlas/products/ATL-QA-001-006.md`
- Create: `Atlas/products/ATL-QA-001-007.md`
- Create: `Atlas/products/data/*.json`
- Create: `tests/test_launch_collection.py`

**Interfaces:**
- Consumes: Etsy and Cults3D pages accessed during implementation, canonical schemas, design rules, and Atlas scoring.
- Produces: one hero candidate, four to six supporting concepts, and retained rejection records with traceable evidence.

- [ ] **Step 1: Define the research protocol test**

Test that each evidence entry has `evidence_id`, `claim`, `source_url`, ISO `accessed_at`, `marketplace`, `evidence_type`, `confidence`, and `notes`; each scored claim references at least one evidence ID or is explicitly `Unknown`; each product has exactly one collection and passes schema validation.

Run: `python -m pytest tests/test_launch_collection.py -v`
Expected: FAIL because research records do not exist.

- [ ] **Step 2: Research Etsy and Cults3D using current sources**

Record dated evidence for product themes, listing density proxies, price patterns, visible engagement proxies, presentation patterns, licensing patterns, and recurring customer-use language. Cite source pages directly. Do not record a search-volume or sales number unless the source explicitly provides it.

- [ ] **Step 3: Synthesize evidence and generate hypotheses**

Write a fact/assumption-separated market synthesis. Generate candidate concepts only within Quiet Architectural resin home decor and assign each to collection `ATL-QA-001`.

- [ ] **Step 4: Run QA and score every concept**

Populate all 14 scores and rationales, risk penalty, strengths, weaknesses, risks, improvements, expansions, and confidence. Document hard-gate failures as rejected records. Do not promote a concept based solely on aesthetics.

- [ ] **Step 5: Select the collection architecture**

Name one hero candidate and four to six supporting concepts, plus mini, XL, bundle, premium, commercial-license, physical-product, and multi-year expansion paths. If evidence cannot support a validated recommendation, label the set `Low Confidence Hypothesis`.

- [ ] **Step 6: Test and commit research**

Run: `python -m pytest tests/test_launch_collection.py tests/test_schema.py tests/test_scoring.py -v`
Expected: all tests PASS.

Run: `git add Atlas/research Atlas/collections Atlas/products tests/test_launch_collection.py && git commit -m "research: validate Atlas launch collection"`
Expected: one traceable research commit.

---

### Task 5: Excel Operating Workbook

**Files:**
- Create: `tools/build_workbook.py`
- Create: `Atlas/excel/README.md`
- Generate: `Atlas/excel/Atlas_Business_OS_v1.0.0.xlsx`
- Create: `tests/test_workbook.py`

**Interfaces:**
- Consumes: controlled vocabularies, evidence register, collection data, and product JSON records.
- Produces: `build_workbook(root: Path, output_path: Path) -> Path` and the 13-sheet operational workbook.

- [ ] **Step 1: Write failing workbook structure tests**

Require the exact sheet order: `Dashboard`, `Product Registry`, `Collection Registry`, `Evidence Register`, `Atlas Scoring`, `QA Gates`, `Marketplace Matrix`, `Pricing`, `SEO Keywords`, `Lifecycle`, `Roadmap`, `Controlled Lists`, `Instructions`. Test frozen headers, autofilters, validation lists, protected formula columns, and warning formatting.

Run: `python -m pytest tests/test_workbook.py -v`
Expected: FAIL because the builder does not exist.

- [ ] **Step 2: Implement deterministic workbook generation**

Implement `build_workbook` with openpyxl. Load canonical JSON rather than duplicating weights. Populate source data, named tables, validation lists, formulas, filters, frozen panes, accessible colors, number formats, and concise instructions.

The Atlas formula for row 2 must calculate the weighted base from all 14 factor columns and subtract the risk penalty; the decision formula must first check the hard-fail field, then apply the four decision bands.

- [ ] **Step 3: Add dashboard and visible failure states**

Show product count, collection count, decision-band counts, confidence counts, QA failure count, evidence-refresh count, and average Atlas Score. Use `Unknown` and warning colors instead of zero-filling absent evidence.

- [ ] **Step 4: Generate, recalculate, and inspect the workbook**

Run: `python tools/build_workbook.py`
Expected: creates `Atlas/excel/Atlas_Business_OS_v1.0.0.xlsx` without warnings.

Open the workbook through the spreadsheet verification workflow, recalculate formulas, render every sheet, and inspect for clipped headers, unreadable widths, broken formulas, invalid validations, and misleading empty values. Record corrections in the builder and regenerate rather than manually patching the workbook.

- [ ] **Step 5: Test and commit the workbook**

Run: `python -m pytest tests/test_workbook.py tests/test_scoring.py -v`
Expected: all tests PASS.

Run: `git add tools/build_workbook.py Atlas/excel tests/test_workbook.py && git commit -m "feat: add Atlas Excel operating workbook"`
Expected: builder, workbook, instructions, and tests committed together.

---

### Task 6: Integration, Release Audit, and v1.0.0 Handoff

**Files:**
- Create: `tools/release_audit.py`
- Create: `tests/test_integration.py`
- Create: `Atlas/docs/RELEASE_CHECKLIST.md`
- Create: `Atlas/docs/VERIFICATION_REPORT.md`
- Create: `.gitignore`
- Modify: `Atlas/README.md`

**Interfaces:**
- Consumes: all Atlas modules and test results.
- Produces: `run_release_audit(root: Path) -> dict` and a human-readable verification report.

- [ ] **Step 1: Write failing integration tests**

Test repository navigation, all relative links, schema validity, collection ownership, evidence references, score reproduction, hard-fail override, prompt completeness, workbook sheet contract, required metadata, and unfinished-content scan results.

Run: `python -m pytest tests/test_integration.py -v`
Expected: FAIL because the release audit does not exist.

- [ ] **Step 2: Implement the release audit**

Return a dictionary with `passed`, `errors`, `warnings`, `counts`, and `generated_at`. Treat schema errors, broken internal links, score mismatches, missing evidence references, missing prompt files, and workbook contract failures as errors. Treat stale research and low-confidence hypotheses as warnings.

- [ ] **Step 3: Complete navigation and release documentation**

Make `Atlas/README.md` the single entry point with role-based paths for founder, product designer, researcher, listing creator, and reviewer. Document exact build, test, research-refresh, workbook-regeneration, version-bump, and release commands.

- [ ] **Step 4: Run the complete verification suite**

Run: `python -m pytest -v`
Expected: all tests PASS.

Run: `python tools/release_audit.py`
Expected: `passed: true`, zero errors, and warnings only for explicitly accepted low-confidence or research-refresh items.

- [ ] **Step 5: Review changes and commit v1**

Run: `git status --short && git diff --check`
Expected: only planned files are modified and `git diff --check` reports no whitespace errors.

Run: `git add .gitignore Atlas tools/release_audit.py tests/test_integration.py && git commit -m "chore: complete Atlas v1 release audit"`
Expected: final implementation commit succeeds.

- [ ] **Step 6: Tag the approved release**

After human review of `VERIFICATION_REPORT.md` and the rendered workbook, run:

```bash
git tag -a v1.0.0 -m "Atlas Business Operating System v1.0.0"
```

Expected: `git tag --list v1.0.0` prints `v1.0.0`.
