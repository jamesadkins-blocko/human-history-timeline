# v1.0 Foundation Release

Status: RENDER-READY

## Declaration
The normalized HT-0001 through HT-0600 foundation is approved as the initial data source for rebuilding the synchronized graphical timeline.

## Foundation counts
- 546 normalized entities
- 600 date claims
- 374 relationships
- 245 legacy place/region labels
- 376 legacy tradition/corpus labels
- 242 sources

## Validation
GitHub Actions canonical validation passed after the final canonical relationship-direction mutations:
- workflow run: 37555564204
- validated commit: bc38f4e0f947fd0893386e4cee7d30ea9f931eef

Subsequent commits through the render-contract freeze changed documentation/controlled-vocabulary text only and did not mutate the six canonical CSV datasets.

Validated invariants include:
- canonical row counts
- unique Entity, Date Claim, and Relationship IDs
- Date Claim -> Entity referential integrity
- Relationship Subject/Object -> Entity referential integrity
- zero normalized year-zero values
- complete HT-0001 through HT-0600 legacy lineage exactly once

## Frozen contracts
- docs/SCHEMA.md
- docs/RESEARCH_RULES.md
- docs/VALIDATION.md
- docs/RENDER_CONTRACT.md
- data/RELATIONSHIP_TYPES.md

## Known non-blocking enrichment
Source URL reachability/quality enrichment and deeper hierarchy parentage may continue. They do not authorize silent changes to claims and are not prerequisites for the first graphical rebuild.

## Next phase
Build the graphical timeline engine/view from canonical normalized data. Future historical expansion resumes at HT-0601 and must remain regenerable under the render contract.
