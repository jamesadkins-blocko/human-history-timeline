# Migration and Research Queue

## ACTIVE — Phase 1 normalization
- [x] Preserve v0.16 legacy Master Timeline (HT-0001 through HT-0600) as immutable migration input.
- [x] Build first-pass normalized Entities table.
- [x] Conservatively merge 46 exact conceptual duplicate clusters while retaining every Legacy HT ID.
- [x] Build Date Claims with one preserved claim per legacy timeline row.
- [x] Import explicit legacy Related IDs into Relationships.
- [x] Seed Places & Regions from all 245 legacy region labels.
- [x] Seed Traditions & Corpora from all 376 legacy tradition/culture labels.
- [x] Add no-year-zero and one-entity/multiple-claims rules to v0.17.
- [x] Generate v0.17 normalized workbook.
- [x] Run formula/error validation (clean).
- [ ] Refine non-exact duplicate candidates (Buddha, Zarathustra, Jesus, Enoch/text/manuscript boundaries, Qin Shi Huang/Terracotta, Second Temple, modern density duplicates, etc.).
- [ ] Type legacy relationships beyond generic RELATED_TO where sources support the semantics.
- [ ] Refine Places & Regions hierarchy.
- [ ] Refine Traditions & Corpora hierarchy.
- [ ] Correct known source-QA defects and validate suspect URLs.
- [ ] Persist canonical normalized CSV/JSON datasets in GitHub.
- [ ] Complete referential-integrity and duplicate-candidate validation suite.
- [ ] Mark Phase 1 normalization operational.

## NEXT — Phase 2 expansion
Resume historical expansion only after normalization is operational. First new legacy-compatible identifier after the frozen v0.16 baseline is HT-0601.
