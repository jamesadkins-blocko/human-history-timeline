# v0.19 Canonical Database Migration

Status: IN PROGRESS

The canonical CSV contracts now exist in `data/`.

## Promotion rule
Do not populate canonical rows from chat summaries, remembered counts, or reconstructed prose. Populate them only from the actual normalized v0.18 workbook/dataset so every field retains workbook provenance.

## Required promotion checks
- 546 entity rows expected from v0.18
- 600 date-claim rows expected
- 374 relationship rows expected
- 245 place/region seed rows expected
- 376 tradition/corpus seed rows expected
- source rows must preserve legacy Source IDs
- zero orphan foreign keys
- zero normalized year-zero values
- every HT-0001 through HT-0600 represented exactly once in legacy date-claim lineage

## Completion condition
v0.19 is complete when the six canonical CSV files contain the normalized v0.18 data and validation reproduces the expected counts/integrity results.
