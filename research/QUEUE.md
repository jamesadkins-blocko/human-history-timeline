# Migration and Research Queue

## COMPLETE — v0.19 canonical migration
- [x] Preserve frozen v0.16 legacy lineage HT-0001 through HT-0600.
- [x] Persist canonical normalized datasets in GitHub.
- [x] Canonical baseline: 546 entities, 600 date claims, 374 relationships, 245 place/region labels, 376 tradition/corpus labels, 242 sources.
- [x] Validate complete HT-0001..HT-0600 lineage and referential integrity.

## ACTIVE — v0.20 Semantic / QA
- [x] Reconcile relationship controlled vocabulary with canonical data.
- [x] Review all 374 relationships: 370 specifically typed; 4 intentionally retained RELATED_TO synchronization links.
- [x] Audit Places & Regions hierarchy and document mixed legacy-label ontology.
- [x] Audit Traditions & Corpora hierarchy and document mixed legacy-label ontology.
- [x] Begin targeted Source QA: malformed Amarna reference, An Shigao chronology, Mexican Constitution, Russian Revolution, Nanjing.
- [x] Repair validator for actual canonical title-case CSV schema.
- [x] Repair legacy HT lineage regex.
- [x] GitHub Actions full canonical validation PASS (run 37555425333; commit 445c1c02318b9852250f53963c78f88b98c6b345).
- [x] Perform targeted relationship directionality audit/corrections before v1.0 freeze.
- [x] Define controlled label-kind vocabulary for Places & Regions; classify obvious non-geographic/astronomical/narrative scopes without inventing parentage.
- [x] Define controlled label-kind vocabulary for Traditions & Corpora; classify obvious categories without blindly parsing compound labels.
- [x] Complete high-priority source-quality review required for render gate; lower-priority URL enrichment continues after render gate.
- [x] Freeze v0.20 structural semantic/QA milestone.

## NEXT — v1.0 normalization operational / render gate
- [x] Run final validation after v0.20 canonical mutations.
- [x] Freeze normalized migration architecture and rendering contract.
- [x] Declare 600-record foundation render-ready.
- [ ] Rebuild synchronized graphical timeline from canonical dataset. **ACTIVE — vector renderer implemented; configurable chronological windows and evidence-class encoding in progress.**

## AFTER RENDER GATE — Phase 2 expansion
Resume historical expansion at HT-0601 while the graphical timeline regenerates from the same canonical data model.
