# Human History Data Schema

## Core principle
The repository stores normalized historical claims. Rendered spreadsheets, graphics, and timelines are derived outputs.

## Entities
One conceptual thing per entity: person, polity/civilization, event, text/work, manuscript, artifact, site, technology, tradition, climate/geology event, or other significant historical entity.

Fields:
- entity_id
- legacy_ht_ids
- canonical_name
- display_name
- entity_type
- subtype
- culture_tradition
- region_id
- significance_tier
- inclusion_rationale
- classification
- external_ids
- notes

## Date Claims
An entity may have multiple competing date claims.

Fields:
- date_claim_id
- entity_id
- claim_type
- start_min
- start_preferred
- start_max
- end_min
- end_preferred
- end_max
- display_date
- chronology_system
- evidence_claim_class
- precision_uncertainty
- source_id
- claim_scope
- notes

### No year zero
Normalized signed years use -1 = 1 BCE and +1 = 1 CE. Year 0 is prohibited. Legacy spreadsheet coordinates remain preserved as imported legacy data and are not silently reinterpreted.

## Relationships
Fields: relationship_id, subject_entity_id, relationship_type, object_entity_id, source_id, certainty_qualification, notes.

## Places and Regions
Fields: region_id, name, type, parent_region_id, modern_geography, latitude, longitude, pleiades_id, tgn_id, unesco_id, notes. Coordinates require a source.

## Traditions and Corpora
Fields: tradition_id, name, type, parent_tradition_id, description, notes.

## Sources
Source IDs and provenance are preserved from the legacy workbook and expanded without overwriting competing evidence.

## Separation rules
Person != story/tradition != text composition != manuscript copy != artifact != archaeological discovery.
Traditional internal chronology != modern scholarly estimate.
One entity may have many date claims; competing chronologies are retained rather than collapsed.
