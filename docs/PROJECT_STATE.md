# Human History Timeline — Project State

## Purpose
Build a synchronized global human-history knowledge base on one mathematical chronological axis.

## Frozen legacy baseline
- v0.16 Master Timeline: HT-0001 through HT-0600 (600 records)
- Legacy rows are preserved as evidence/migration input and are not silently rewritten.
- GitHub is the persistent project-state and normalized-data workspace.

## Phase 1 normalization — ACTIVE
Latest generated workbook: v0.18.

### v0.18 counts
- Frozen legacy timeline records: 600
- Normalized entities: 546
- Date claims: 600
- Relationships: 374
- High-confidence relationships semantically typed this pass: 33
- Additional non-exact identity duplicates merged this pass: 8 absorbed entities across 7 canonical groups
- Places & Regions seed labels: 245
- Traditions & Corpora seed labels: 376
- Referential-integrity failures: 0
- Normalized year-zero violations: 0
- Formula/error scan: 0

### v0.18 high-confidence identity merges
- Buddha: HT-0056, HT-0057, HT-0315 -> one Siddhartha Gautama entity with separate date claims.
- Zarathustra: HT-0065, HT-0066 -> one Zarathustra/Zoroaster entity with competing chronology claims.
- Jesus: HT-0073, HT-0338 -> one Jesus of Nazareth entity with separate legacy claims.
- Qin Shi Huang: HT-0067, HT-0342 -> one ruler entity.
- Terracotta Army: HT-0068, HT-0343 -> one artifact/complex entity.
- Destruction of Second Temple: HT-0075, HT-0341 -> one event entity.
- Enoch figure: HT-0034, HT-0337 -> one traditional figure entity; remains separate from 1 Enoch and Qumran manuscript witnesses.

### Deliberately NOT merged
- Second Temple period vs Second Temple completed vs destruction event.
- Socrates person vs trial/death event.
- Aristotle person vs founding of Lyceum event.
- Alexander person vs death event.
- Enoch figure vs 1 Enoch literary tradition vs manuscript copies.
- Plato person vs Timaeus/Critias/Atlantis internal chronology.
These separations are structural requirements, not duplicate-cleanup failures.

### Source QA
A Source QA sheet now records corrections/research without altering frozen legacy rows.
- HT-0277 malformed Met Amarna URL: verified replacement reference captured from a current Met Akhenaten/Amarna object record.
- HT-0077 An Shigao approximate end date remains queued for dedicated source review rather than guessing.

## Next work
1. Persist canonical normalized CSV/JSON datasets in GitHub.
2. Continue semantic typing of relationships.
3. Refine Places & Regions hierarchy.
4. Refine Traditions & Corpora hierarchy.
5. Complete source-QA sweep and duplicate-candidate validator.
6. Mark normalization operational.
7. Resume expansion at HT-0601 only after the above foundation is operational.

## Continuity
Read docs/PROJECT_STATE.md, docs/SCHEMA.md, docs/RESEARCH_RULES.md, research/QUEUE.md, and data/README.md before substantial work. Commit durable state before ending.
