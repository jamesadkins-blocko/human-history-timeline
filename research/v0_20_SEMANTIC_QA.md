# v0.20 Semantic / QA Pass

Status: IN PROGRESS

## Baseline
v0.19 canonical migration is complete.

Canonical counts:
- 546 entities
- 600 date claims
- 374 relationships
- 245 places/regions
- 376 traditions/corpora
- 242 sources

## Validator correction
The repository validator has been aligned with the actual normalized schema. Legacy HT lineage is validated through `Entities.Legacy HT ID(s)`, because Date Claims intentionally has no Legacy HT ID column.

## Relationship semantic inventory
Current relationship-type counts:
- RELATED_TO: 341
- semantically typed relationships: 33

The 33 typed rows are preserved. The 341 RELATED_TO rows are semantic debt, not data loss.

## v0.20 work order
1. Reconcile the controlled vocabulary in `data/RELATIONSHIP_TYPES.md` with relationship types already present in canonical data.
2. Retype only high-confidence RELATED_TO relationships supported by explicit entity semantics/source context. Do not infer relationships merely from chronological overlap.
3. Refine Places & Regions hierarchy without inventing geocoding.
4. Refine Traditions & Corpora hierarchy.
5. Continue Source QA, including the queued An Shigao chronology review and malformed/weak legacy URLs.
6. Run full validation after every canonical mutation.
7. Document unresolved ambiguity rather than forcing a type or date.

## Guardrail
RELATED_TO is preferable to an invented semantic relationship. False specificity is worse than unresolved generic linkage.
