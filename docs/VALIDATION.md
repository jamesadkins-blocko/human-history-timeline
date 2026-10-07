# Validation policy

Normalization is not operational until all mandatory checks pass.

## Mandatory integrity checks
1. Entity IDs are unique.
2. Date Claim IDs are unique.
3. Relationship IDs are unique.
4. Region IDs are unique.
5. Tradition IDs are unique.
6. Every Date Claim entity_id resolves to an Entity.
7. Every Relationship subject_entity_id and object_entity_id resolves to an Entity.
8. Every source_id used by a normalized claim resolves to a source record or is explicitly marked pending migration.
9. Normalized signed year fields contain no year 0.
10. Every legacy HT-0001 through HT-0600 is represented by exactly one preserved legacy date claim.
11. Every legacy HT ID appearing on a normalized Entity exists in the frozen legacy baseline.
12. No entity merge may silently discard a legacy date/source claim.

## Duplicate-candidate checks
Exact normalized-name matching is only a candidate generator, never automatic authority.
Flag:
- same normalized name on multiple entities;
- overlapping legacy HT records with highly similar names;
- repeated major anchors from later density passes;
- person/event or figure/text name collisions.

Explicitly protect against false merges across entity types.

## Relationship checks
- RELATED_TO is permitted during migration but reported as unresolved technical debt.
- Typed relationships must use the controlled vocabulary.
- Disputed/traditional relations require qualification where appropriate.
- Chronological overlap alone does not create CONTEMPORARY_WITH.

## Release gate
Phase 1 becomes operational only when mandatory integrity checks pass and unresolved duplicate/source issues are documented rather than silently ignored.
