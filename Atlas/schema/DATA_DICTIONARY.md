# Atlas Data Dictionary

**Status:** Approved  
**Version:** 1.0.0  
**Owner:** Atlas Studio  
**Review date:** 2026-10-07  
**Change history:** 1.0.0 — Initial canonical contract.

## Record boundaries

Products, collections, evidence, scores, QA reviews, marketplace packages, lifecycle events, versions, and roadmap items are separate records joined by stable identifiers. JSON is canonical; Markdown and Excel are human interfaces.

## Identifiers

- Product: `ATL-QA-CCC-PPP`, where `CCC` is the collection and `PPP` is the product.
- Collection: `ATL-QA-CCC`.
- Evidence: `EVD-NNN`, with at least three digits.

## Product fields

The product schema requires identity, governance, exactly one collection, Product DNA, all design tokens, at least one evidence reference, all 14 score/rationale pairs, risk penalty, decision analysis, and change history. Scores use 0–10; risk uses 0–10 points.

## Evidence fields

Every evidence record states the claim, direct URL when available, access date, marketplace, evidence type, confidence, and notes. `Unknown` evidence may use a null URL but must explain the gap.

## Controlled values

Canonical enums and weights live in `controlled-vocabularies.json`. Consumers must load them rather than copying them. Higher factor scores always mean a more favorable result: competition is represented as opportunity, and complexity as production simplicity.

## Ownership and updates

The record owner proposes changes; a reviewer verifies evidence, QA, and formula integrity. Review dates use ISO `YYYY-MM-DD`. Contract-breaking changes require a major semantic-version increment.
