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


## Relationship semantic review — COMPLETE

All 374 canonical relationship rows were reviewed during v0.20.

Final disposition:
- 370 relationships carry a specific semantic relationship type.
- 4 relationships intentionally remain RELATED_TO as cross-regional synchronization/comparison links.
- 0 RELATED_TO rows remain as unexplained semantic debt.

Intentional synchronization links:
- REL-0211 — Olmec colossal-head / ceremonial-center florescence ↔ New Guinea early agriculture
- REL-0212 — Chavín de Huántar florescence ↔ Adena cultures
- REL-0213 — Adena mound-building tradition ↔ Great houses begin at Chaco Canyon
- REL-0246 — Hopewell Interaction Sphere ↔ Song dynasty

These rows do not assert causation, contact, descent, or influence. They exist to support the project's core synchronization function.

Next v0.20 workstream: Places & Regions hierarchy, Traditions & Corpora hierarchy, and Source QA.


## Directionality audit — COMPLETE
The known directionality defects were corrected without reversing imported Subject -> Object orientation:
REL-0006 and REL-0007 -> INCLUDES_PERIOD; REL-0025 -> FOUNDED; REL-0032 -> RULED; REL-0050 -> INCLUDES_PERIOD; REL-0065 -> ENDED; REL-0076 -> INCLUDES_COMPONENT; REL-0078 -> ENDED.
Controlled inverse labels were added to data/RELATIONSHIP_TYPES.md.
Post-mutation GitHub Actions validation passed (run 37555564204).

## Hierarchy classification contract — ESTABLISHED
v0.20 hierarchy QA now defines controlled label kinds for geographic, political, composite, conceptual, astronomical, traditional/textual, narrative, and misclassified-place labels, plus corresponding tradition/corpus categories. Parentage remains optional unless containment is explicit and unambiguous.

## Render-gate disposition
The remaining source-QA work is enrichment rather than a structural blocker. Frozen provenance remains preserved, and unresolved/weak legacy references are documented rather than silently rewritten. The normalized architecture is therefore structurally ready for the v1.0 render contract, subject to a final canonical validation after milestone documentation updates.
