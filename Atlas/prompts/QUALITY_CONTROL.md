# Quality Control Prompt

**Status:** Approved
**Version:** 1.0.0
**Owner:** Atlas Studio
**Review date:** 2026-10-07
**Change history:** 1.0.0 - Initial prompt release.

## Purpose
Audit a product recommendation or release package against all Atlas requirements.
## Required inputs
Product, collection, evidence, score calculation, QA record, marketplace package, files, version, and change history.
## Rules
Never fabricate a pass. Verify resin printability, structural integrity, support complexity, commercial viability, SEO opportunity, marketplace fit, collection fit, bundle fit, brand consistency, scalability, evidence integrity, and rights. Hard failures force Reject.
## Output contract
Return gate-by-gate result, evidence, arithmetic check, missing fields, contradictions, hard failures, required remediation, release decision, and confidence.
## Unknown or refusal behavior
Unknown hard-gate evidence blocks release. High Confidence requires complete traceable proof, Medium Confidence permits noncritical proxy evidence, and Low Confidence indicates major gaps. Refuse approval when required inputs are absent.
## Quality checklist
Check all gates, 14 factors, risk penalty, source dates, print evidence, rights, one collection, listing truth, file integrity, semantic version, and reviewer sign-off.
