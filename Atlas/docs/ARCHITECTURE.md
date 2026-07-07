# Architecture

**Status:** Approved  
**Version:** 1.0.0  
**Owner:** System Owner  
**Review date:** 2026-10-07  
**Change history:** 1.0.0 — Schema-centered architecture established.

JSON schemas and controlled vocabularies are canonical. Markdown explains how to operate; structured product and evidence JSON holds decisions; Excel provides the working interface. Consumers load weights and enums from `schema/controlled-vocabularies.json`.

The flow is evidence to product hypothesis, QA, Atlas Score, collection decision, marketplace package, and lifecycle record. Interfaces use stable product, collection, and evidence IDs.

See the [operating workflow](OPERATING_WORKFLOW.md) and [governance](GOVERNANCE.md).
