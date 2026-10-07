# Relationship type vocabulary

Use the narrowest defensible relationship. Do not infer a relationship merely because two entities overlap chronologically.

Initial controlled vocabulary:
- RELATED_TO — legacy/imported relationship whose semantics have not yet been safely typed
- ATTRIBUTED_TO — work/tradition attributed to a figure; does not assert authorship
- MANUSCRIPT_OF — manuscript witness/copy of a text or textual tradition
- TEXT_DESCRIBES — text/work describes or contains a narrative/event/figure
- ASSOCIATED_WITH — sourced association not strong enough for a narrower relation
- CREATED_BY — artifact/work demonstrably created/commissioned by
- COMMISSIONED_BY — ruler/patron commissioned work/building
- FOUNDED_BY — polity/institution/tradition founded by, where historically defensible
- RULED_BY — polity/realm ruled by a person
- PART_OF — entity is a component/phase/member of a larger entity
- PRECEDED_BY / SUCCEEDED_BY — historical succession
- OCCURRED_WITHIN — event occurred within a polity/period
- RESULTED_IN — event directly resulted in another entity/event
- DISCOVERED_AT — artifact/manuscript discovered at a place/site
- LOCATED_AT — site/artifact location association
- TRADITIONALLY_ASSOCIATED_WITH — relationship belongs to a named traditional/religious/legendary chronology
- CONTEMPORARY_WITH — use sparingly and only when synchronization itself is analytically important

Qualification/certainty belongs in the relationship row; it is not encoded by pretending a disputed relation is certain.


## Canonical types already present in v0.19 data

The following legacy-normalized types are already used in canonical rows and are retained during v0.20 pending any later alias consolidation:
- AUTHORED — explicit authorship relationship in the normalized source data
- PARTICIPATED_IN_EVENT — person/polity participated in an event
- INCLUDES_EVENT — period/war/process includes a named event
- CONTAINS_TEXT — corpus/manuscript/collection contains a text
- COMMISSIONED_INSCRIPTIONS — ruler/patron commissioned inscriptions
- RULER_ASSOCIATED_WITH_FUNERARY_COMPLEX — ruler has an explicit funerary-complex association
- PATRON_OF_BUILDING_PROJECT — patron/ruler explicitly associated with a building project
- PRODUCED_DOCUMENT — institution/person produced a document
- FIGURE_ASSOCIATED_WITH_TEXT — figure associated with a text without asserting authorship
- FIGURE_NAMED_IN_MANUSCRIPT_TRADITION — figure is named in a manuscript tradition
- WORK_ATTESTED_BY_MANUSCRIPT — literary work is attested by a manuscript witness
- FIGURE_CENTRAL_TO_TEXT — figure is central to a text/narrative
- SPONSORED_VOYAGES — ruler/patron sponsored voyages
- RESULTED_FROM — inverse-direction causal relation retained where source row is oriented result -> cause
- SPONSORED_BY — inverse-direction sponsorship relation
- ESCALATION_TRIGGERED_BY — event/process escalation explicitly triggered by another event
- DEVELOPED_WEAPONS_USED_IN — project/program developed weapons used in an event

These labels are semantic, not truth scores. Qualification and uncertainty remain in the relationship row.

## Directionality rules

Relationship direction must be read literally from Subject Entity ID -> Object Entity ID.

Use paired inverse labels only when reversing the row would otherwise obscure the imported subject/object orientation. Do not silently reverse legacy relationships merely to fit a preferred verb.

## v0.20 retyping guardrail

A RELATED_TO row may be promoted only when the relationship is explicit in the entity semantics or supported source context. Chronological overlap alone is never sufficient.
