# v0.19 Canonical Database Migration

Status: IN PROGRESS — workbook export verified; repository row promotion pending transport

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
