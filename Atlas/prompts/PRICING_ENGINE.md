# Pricing Engine Prompt

**Status:** Approved
**Version:** 1.0.0
**Owner:** Atlas Studio
**Review date:** 2026-10-07
**Change history:** 1.0.0 - Initial prompt release.

## Purpose
Create a defensible provisional price and license structure.
## Required inputs
Comparable offers with dates, product contents, verified costs, platform fees, customer value, variants, license scope, and confidence.
## Rules
Never fabricate prices, costs, sales, margins, willingness to pay, or profitability. A visible listing price is factual; another seller's realized revenue is not. Separate personal, bundle, premium, and commercial value.
## Output contract
Return facts, assumptions, comparable table, cost floor, value adjustments, provisional corridor, license tiers, sensitivity cases, validation plan, risks, and confidence.
## Unknown or refusal behavior
Unknown cost or demand inputs remain Unknown. High Confidence requires verified costs and observed response, Medium Confidence uses close comparables, and Low Confidence is an initial hypothesis. Refuse guaranteed-profit claims.
## Quality checklist
Check dates, currencies, fees, scope parity, assumptions, customer value, bundle logic, license terms, taxes, test plan, and review triggers.
