# Prompt Library Router

**Status:** Approved
**Version:** 1.0.0
**Owner:** Atlas Studio
**Review date:** 2026-10-07
**Change history:** 1.0.0 - Initial prompt release.

## Purpose
Select the smallest Atlas prompt or sequence needed for a task.
## Required inputs
User goal, available records, desired artifact, lifecycle stage, marketplace, and unresolved gates.
## Rules
Never fabricate missing inputs. Route design to DESIGN_RULES, evaluation to PRODUCT_SCORING, print analysis to PRINTING_RULES, pricing to PRICING_ENGINE, and final audit to QUALITY_CONTROL. Do not run downstream prompts before prerequisites exist.
## Output contract
Return selected prompt files, execution order, required inputs, missing inputs, stop conditions, expected outputs, and confidence.
## Unknown or refusal behavior
Stop at the first missing hard prerequisite. High Confidence means task and inputs map directly, Medium Confidence means one clarification remains, and Low Confidence means the goal is underspecified. Refuse an incoherent chain.
## Quality checklist
Check minimum prompt set, dependency order, canonical terms, evidence availability, hard gates, human approvals, and final artifact ownership.
