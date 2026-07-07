# Product Scoring Prompt

**Status:** Approved
**Version:** 1.0.0
**Owner:** Atlas Studio
**Review date:** 2026-10-07
**Change history:** 1.0.0 - Initial prompt release.

## Purpose
Calculate and explain one unified Atlas Score without allowing aesthetics to substitute for evidence.
## Required inputs
Product record, evidence register, QA results, canonical weights, risk evidence, marketplace context, and review date.
## Rules
Never fabricate search volume, sales estimates, revenue, demand, competition, or print results. Score 0–10 with higher always better for: Market Demand; Competition Opportunity; Profitability; Evergreen Potential; Brand Alignment; Collection Potential; Bundle Potential; Physical Product Potential; SEO Opportunity; Resin Printability; AI Production Efficiency; Customer Value; Production Simplicity; Marketplace Fit. Apply the canonical weights, then deduct a documented risk penalty from 0–10. Hard QA failure forces Reject.
## Output contract
Return headings: Facts; Assumptions; Evidence; Scores; Decision; Strengths; Weaknesses; Risks; Improvements; Expansion; Confidence. For each score provide value, evidence IDs, rationale, uncertainty, and improvement lever. Show weighted base, penalty, final score, decision band, and hard-gate state.
## Unknown or refusal behavior
Do not turn missing evidence into zero. Mark it Unknown, lower confidence, and request validation. High Confidence requires multiple current direct sources, Medium Confidence uses credible proxies or limited sources, and Low Confidence covers assumptions or conflict. Refuse a numeric score that lacks rationales.
## Quality checklist
Confirm all 14 factors, weights total 100%, score direction, arithmetic, citations, dates, hard gates, risk rationale, recommendation explanation, and no fabricated statistics.
