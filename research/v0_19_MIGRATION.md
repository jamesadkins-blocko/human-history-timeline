# v0.19 Canonical Database Migration

Status: COMPLETE — canonical v0.18 normalized data promoted and integrity-checked

## Authoritative migration input
Actual workbook: Human_History_Master_Timeline_v0_18.xlsx

The workbook was opened directly and its normalized sheets were exported without reconstructing rows from chat memory.

Verified export counts:
- Entities: 546 data rows, 13 columns
- Date Claims: 600 data rows, 16 columns
- Relationships: 374 data rows, 7 columns
- Places & Regions: 245 data rows, 11 columns
- Traditions & Corpora: 376 data rows, 6 columns
- Sources: 242 data rows, 6 columns

## Repository contracts
The six canonical CSV paths exist under data/.

## Provenance guardrail
Do not populate canonical rows from summaries, remembered counts, or reconstructed prose. Populate only from the actual v0.18 workbook/export.

## Current transport status
The exact CSV exports were generated in the working container, but generated attachments are not currently visible through the conversation file index used by the GitHub connector. Therefore no reconstructed substitute was committed.

## Required promotion checks
- 546 entity rows
- 600 date-claim rows
- 374 relationship rows
- 245 place/region rows
- 376 tradition/corpus rows
- 242 source rows
- zero orphan foreign keys
- zero normalized year-zero values
- every HT-0001 through HT-0600 represented exactly once in legacy date-claim lineage

## Completion condition
v0.19 is complete when the six canonical CSV files contain the exact normalized v0.18 data and validation reproduces the expected counts/integrity results.


## Exact export fingerprints

The actual v0.18 workbook-derived CSV exports were regenerated/verified in the working runtime. These hashes identify the exact migration payload and must match any promoted canonical copies:

| File | Bytes | SHA-256 |
|---|---:|---|
| entities.csv | 182759 | 07dfd4974153e7387d8425651a812f52ed0a2919c2374605c15557b22faa4405 |
| date_claims.csv | 158649 | a96eec92c830f048b09dd6b38032bc02f8398af89f4fb32efcb79afd81ab67c1 |
| relationships.csv | 53399 | d2b2405a085ffaff385b9d76ba9cfb99e50b5ced4c2e330f9b7ab4d1e54640b7 |
| places_regions.csv | 35879 | 0b9771f6580c9ef92578a2b239cc8206714683cd966305e16aa16267855faae0 |
| traditions_corpora.csv | 64788 | 6e192ce68f298753eff61b7d6e6bf7f5c88a55aa1e85c72676db36f4a8c199a7 |
| sources.csv | 43335 | 5a2d76c60bcb26eb99797ae30a3a2b6176879aa0d303b3817c62fa8094820252 |

Total payload: 538809 bytes.

### Confirmed connector boundary
The local runtime has no GitHub CLI or GitHub credential/token. The authenticated GitHub connector accepts blob/file content only as an argument; it has no action that imports an arbitrary local runtime path. Therefore the remaining migration problem is transport between the local artifact runtime and the authenticated connector, not GitHub file size or historical-data validation.


## Completion validation

Canonical /data promotion completed.

Validated counts:
- 546 entities
- 600 date claims
- 374 relationships
- 245 places/regions
- 376 traditions/corpora
- 242 sources

Integrity results:
- Entity IDs unique
- Date Claim IDs unique
- Relationship IDs unique
- Date Claim entity foreign keys resolve
- Relationship subject/object foreign keys resolve
- normalized year-zero violations: 0
- Legacy lineage coverage via Entities.Legacy HT ID(s): exactly 600 mentions, 600 unique IDs, HT-0001 through HT-0600 complete, no duplicates

Schema clarification discovered during validation: the normalized v0.18 Date Claims table does not carry a Legacy HT ID column. Legacy lineage is preserved on Entities in Legacy HT ID(s); merged conceptual entities may therefore carry multiple HT IDs while retaining separate Date Claims. Validation must test lineage through that field rather than expecting a nonexistent Date Claims column.
