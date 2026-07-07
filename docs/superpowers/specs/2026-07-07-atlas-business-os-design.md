# Atlas Business Operating System v1 Design

**Status:** Approved design  
**Version:** 1.0.0  
**Date:** 2026-07-07  
**Product domain:** Resin-printable home decor  
**Brand direction:** Quiet Architectural  
**Market position:** Accessible premium  
**Primary validation markets:** Etsy and Cults3D

## 1. Purpose

Atlas v1 is a documentation-and-Excel business operating system for building a global resin digital-product brand. It must support consistent generation, evaluation, documentation, release, and expansion of more than 1,000 products without fabricating market evidence.

Atlas v1 does not include STL modeling, automated marketplace scraping, live marketplace APIs, inventory management, or a software dashboard.

## 2. Decision Record

Three architectures were evaluated with these weights: scalability 25%, evidence auditability 20%, daily usability 20%, data consistency 15%, maintainability 10%, and implementation speed 10%.

| Architecture | Weighted score |
| --- | ---: |
| Workbook-first | 7.15/10 |
| Documentation-first | 7.20/10 |
| Schema-centered hybrid | 8.75/10 |

The approved architecture is the schema-centered hybrid. A canonical schema governs products, collections, evidence, scores, and lifecycle stages. Excel is the operational interface. Documentation and prompts use the same terminology and rules.

### Strengths

- Supports more than 1,000 product records.
- Keeps claims, evidence, assumptions, and confidence traceable.
- Prevents Excel, documentation, and prompts from creating competing definitions.
- Provides a migration path to databases, dashboards, automation, and APIs.

### Weaknesses and risks

- Initial design is slower than a workbook-only approach.
- Strict identifiers, field definitions, and validation rules require maintenance.
- Excessive v1 complexity could reduce adoption.

The complexity risk is controlled by a compact initial schema, controlled vocabularies, and the exclusion of a software application from v1.

## 3. Repository Architecture

The implementation will create `Atlas/` as the operating-system root with the following bounded modules:

- `schema/`: canonical fields, scoring factors, controlled vocabularies, identifiers, lifecycle states, and validation rules.
- `excel/`: operational workbook, workbook instructions, formulas, dashboards, and data dictionary.
- `business/`: strategy, business model, pricing, licensing, and financial assumptions.
- `brand/`: Quiet Architectural identity, audience, positioning, and design tokens.
- `marketplaces/`: Etsy, Cults3D, Gumroad, Printables, MyMiniFactory, MakerWorld, and Ko-fi playbooks.
- `collections/`: collection registry, templates, and the researched launch collection.
- `products/`: structured product records, each assigned to exactly one collection.
- `research/`: dated evidence, source register, assumptions, and confidence assessments.
- `seo/`: keyword methodology, listing templates, and marketplace-specific SEO.
- `prompts/`: self-contained prompt-engineering repository.
- `standards/`: resin printing, rendering, QA, naming, and product-design rules.
- `roadmap/`: lifecycle plans, releases, and expansion.
- `docs/`: navigation, governance, workflows, and architecture.

The primary data flow is:

`Research evidence -> Product record -> QA gates -> Atlas Score -> Collection decision -> Marketplace package -> Lifecycle tracking`

## 4. Canonical Data Model

The canonical model contains independent records for products, collections, evidence, scores, QA reviews, marketplace packages, lifecycle events, versions, and roadmap items. Stable identifiers join records across Markdown and Excel.

Product identifiers use `ATL-QA-CCC-PPP`, where `QA` identifies Quiet Architectural, `CCC` identifies the collection, and `PPP` identifies the product within that collection. A product belongs to exactly one collection. It may participate in multiple bundles without changing collection ownership.

Every product record includes:

- Product DNA: core purpose, design philosophy, emotional appeal, target customer, functional and decorative benefits, print complexity, material efficiency, brand alignment, future evolution, and physical-manufacturing potential.
- Design tokens: corner radius, wall thickness, chamfer and fillet styles, edge language, texture density, surface finish, relief depth, pattern scale, shadow language, visual weight, design balance, and material simulation.
- Technical assumptions: dimensions, resin assumptions, wall thickness, hollowing and drain strategy when relevant, support strategy, structural concerns, and test status.
- Commercial fields: target use, pricing logic, licensing, marketplace fit, SEO hypothesis, customer value, and profitability assumptions.
- Evaluation fields: evidence, individual scores and rationales, Atlas Score, strengths, weaknesses, risks, improvement actions, and expansion opportunities.
- Governance fields: owner, reviewer, lifecycle stage, asset status, semantic version, dates, and change history.

## 5. Collection Architecture

Every collection defines a hero product, supporting products, mini and XL variants, bundle and premium editions, a commercial-license edition, a future physical product, and a multi-year expansion map.

The researched launch collection will contain one hero candidate and four to six supporting concepts. A concept becomes a recommendation only after evidence review and QA. Failed concepts remain documented as rejected decisions.

## 6. Atlas Score Engine

Each factor is scored from 0 to 10, with higher values always representing a more favorable outcome. `Competition Opportunity` is high when the competitive opening is favorable. `Production Simplicity` is the inverse of production complexity.

| Factor | Weight |
| --- | ---: |
| Market Demand | 14% |
| Competition Opportunity | 8% |
| Profitability | 10% |
| Evergreen Potential | 10% |
| Brand Alignment | 10% |
| Collection Potential | 7% |
| Bundle Potential | 7% |
| Physical Product Potential | 6% |
| SEO Opportunity | 7% |
| Resin Printability | 8% |
| AI Production Efficiency | 3% |
| Customer Value | 5% |
| Production Simplicity | 3% |
| Marketplace Fit | 2% |
| **Total** | **100%** |

The formula is:

`Weighted Base Score = SUM(factor score / 10 * factor weight)`

`Final Atlas Score = Weighted Base Score - Risk Penalty`

The weighted base and final score both use a 0-to-100 scale. The risk penalty ranges from 0 to 10 points and requires a written rationale.

Decision bands are:

- 80 to 100: Prioritize.
- 70 to 79.99: Validate.
- 60 to 69.99: Revise.
- Below 60: Reject.

A hard QA failure overrides the numeric result and forces rejection until resolved.

## 7. Evidence and Confidence Policy

Every scored factor stores a rationale, source URL, access date, evidence type, confidence, reviewer, and review date.

Evidence types are `Verified`, `Proxy`, `Assumption`, and `Unknown`. Confidence levels are `High`, `Medium`, and `Low`.

- High confidence requires multiple current, independent, directly relevant sources.
- Medium confidence uses credible proxy evidence, limited coverage, or modest uncertainty.
- Low confidence applies to assumptions, weak proxies, substantial uncertainty, or conflicting evidence.

Atlas never invents search volume, sales, demand, or revenue. Because Etsy and Cults3D do not expose complete market-wide demand data, research may use clearly labeled proxies such as listing density, review activity, price patterns, recurring themes, and marketplace prominence. Unknown values remain unknown; they are not silently converted to zero or a fabricated fact.

## 8. Quality Gates

Every product is checked for resin printability, structural integrity, support complexity, commercial viability, SEO opportunity, marketplace compatibility, collection compatibility, bundle compatibility, brand consistency, and long-term scalability.

Unresolved failures in printability, structural integrity, commercial rights, collection compatibility, or evidence integrity are hard failures. Other failures require revision or explicit risk acceptance. Each gate records status, rationale, reviewer, date, and remediation.

## 9. Lifecycle and Versioning

Product lifecycle stages are:

`Idea -> Prototype -> Validated Product -> Hero Product -> Collection -> Bundle -> Premium Version -> Commercial License -> Physical Product -> Membership Exclusive -> Legacy Product -> Retired`

These stages are available milestones, not mandatory promotions. Supporting products are not required to become hero products. Every transition requires documented evidence and approval criteria.

Asset status is tracked independently as `Draft`, `Experimental`, `Approved`, `Released`, or `Deprecated`. Major assets use semantic versions such as `v1.0.0`, `v1.1.0`, and `v2.0.0` with a change history.

## 10. Excel Workbook

The workbook contains `Dashboard`, `Product Registry`, `Collection Registry`, `Evidence Register`, `Atlas Scoring`, `QA Gates`, `Marketplace Matrix`, `Pricing`, `SEO Keywords`, `Lifecycle`, `Roadmap`, `Controlled Lists`, and `Instructions` worksheets.

The workbook uses formulas, validation lists, conditional formatting, filters, frozen headers, protected formula cells, and visible warnings. Unknown evidence remains visibly unknown. The workbook does not define terms or weights independently from the canonical schema.

## 11. Documentation and Prompt Repository

Documentation covers business strategy, brand guidelines, marketplace playbooks, product-design rules, SEO, pricing, collections, resin printing, rendering, AI workflow, governance, and versioning. Documents link to their dependencies and define ownership and update triggers.

The prompt repository contains:

- `SYSTEM_PROMPT.md`
- `AI_BEHAVIOR.md`
- `DESIGN_RULES.md`
- `PRODUCT_DNA.md`
- `PRODUCT_SCORING.md`
- `MARKETPLACE_RULES.md`
- `COLLECTION_RULES.md`
- `PRINTING_RULES.md`
- `RENDER_RULES.md`
- `SEO_RULES.md`
- `NAMING_RULES.md`
- `BRAND_GUIDELINES.md`
- `CONTENT_STRATEGY.md`
- `PRICING_ENGINE.md`
- `ROADMAP.md`
- `BUSINESS_MODEL.md`
- `PROMPT_LIBRARY.md`
- `QUALITY_CONTROL.md`

Every prompt is independently usable while remaining consistent with canonical terminology, evidence requirements, score definitions, QA gates, and output schemas.

## 12. Operating Workflow

1. Capture a sourced market signal.
2. Create a product hypothesis.
3. Assign exactly one collection.
4. Define Product DNA and design tokens.
5. Run technical and commercial QA.
6. Score all Atlas factors with rationales and evidence.
7. Apply the documented risk penalty.
8. Prioritize, validate, revise, or reject.
9. Generate marketplace-specific packages.
10. Track lifecycle, version, and review dates.

## 13. Marketplace Outputs

- Etsy emphasizes lifestyle imagery, gift positioning, Pinterest-friendly thumbnails, SEO, bundles, emotional copy, and mockups.
- Cults3D emphasizes premium STL presentation, detailed renders, assembly and cross-section previews, print photographs, commercial licensing, and technical descriptions.
- Gumroad emphasizes digital bundles, premium collections, commercial licenses, and creator-facing branding.
- Printables emphasizes community engagement, reliable printing, educational content, and practical value.
- MyMiniFactory emphasizes premium quality, collector appeal, exclusivity, and high-detail resin models.
- MakerWorld emphasizes presentation, print reliability, and community visibility.
- Ko-fi emphasizes memberships, exclusive releases, supporter rewards, and monthly drops.

## 14. Failure Handling

- Missing evidence is marked `Unknown` and triggers validation.
- Broken sources retain their citation and receive a refresh flag.
- Formula or input errors produce visible workbook warnings.
- Hard QA failures force rejection regardless of score.
- Conflicting evidence is retained, explained, and reflected in lower confidence.
- Outdated research is flagged by its review date and preserved for audit history.

## 15. Verification and Acceptance

Release verification includes workbook formula and validation checks, recalculation, visual inspection of every worksheet, score reproduction from sample inputs, required-field tests, controlled-vocabulary tests, product-to-collection integrity checks, documentation link checks, prompt consistency scans, placeholder scans, QA rejection tests, and source-confidence audits.

Every recommended launch product must include its score rationales, strengths, weaknesses, risks, improvement suggestions, future expansion opportunities, and confidence level. If available evidence is insufficient, the output is explicitly labeled as a low-confidence hypothesis rather than a validated recommendation.

Atlas v1 is accepted when the repository is navigable, all required modules and prompt files exist, the workbook operates consistently with the canonical schema, the launch collection is researched and fully traceable, hard QA gates behave correctly, and verification results are documented.
