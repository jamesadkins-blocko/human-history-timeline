# Canonical normalized data format

Canonical repository datasets are UTF-8 CSV. The v0.17 workbook is a reference/rendered release; GitHub CSV data is the durable machine-readable source of truth once migration QA completes.

Required datasets:
- entities.csv
- date_claims.csv
- relationships.csv
- places_regions.csv
- traditions_corpora.csv
- sources.csv

Rules:
- CSV uses a header row and RFC-4180 compatible quoting.
- IDs are stable and never recycled.
- Legacy HT IDs are retained on normalized entities.
- A legacy HT row maps to a distinct date claim even when multiple legacy rows consolidate to one entity.
- Normalized signed years prohibit 0: -1 = 1 BCE; +1 = 1 CE.
- Empty/unknown values remain empty; they are never invented.
- Relationships may remain RELATED_TO until a defensible semantic type is established.
- Coordinates and external identifiers require identifiable provenance.
