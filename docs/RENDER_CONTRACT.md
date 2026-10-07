# v1.0 Render Contract

Status: FROZEN FOR INITIAL GRAPHICAL REBUILD

## Purpose
This contract defines how the canonical normalized history dataset is converted into synchronized graphical timeline views. Rendering may simplify presentation, but it may not alter historical claims.

## Canonical inputs
- data/entities.csv
- data/date_claims.csv
- data/relationships.csv
- data/places_regions.csv
- data/traditions_corpora.csv
- data/sources.csv

The frozen HT-0001 through HT-0600 lineage remains migration provenance. The normalized tables above are the rendering source.

## Time-axis contract
1. Every lane uses one mathematical chronological coordinate system.
2. A given normalized year must occupy the same x-coordinate in every lane.
3. Year zero is prohibited. 1 BCE is followed by 1 CE.
4. Ranges and uncertainty must remain ranges/uncertainty; the renderer may not manufacture precision.
5. Competing Date Claims may coexist and must not be silently collapsed.
6. Traditional/internal chronology must remain distinguishable from modern estimated chronology.

## Entity/claim separation
A person, event, text, manuscript witness, artifact, site, tradition, and discovery are distinct concepts when the data model represents them separately. The renderer must not convert a manuscript-copy date into a figure's lifetime, a literary composition date into an event date, or a traditional narrative date into an archaeological assertion.

## Classification display
The graphical layer must visually distinguish at minimum:
- historically documented
- approximate/disputed chronology
- traditional/religious chronology
- legendary/mythological tradition
- archaeological evidence/artifact
- manuscript/text composition or surviving copy

Classification describes evidence/source type, not a truth score.

## Lane and synchronization behavior
Regional/cultural lanes are presentation groupings, not independent clocks. Cross-regional synchronization is a first-class function. Vertical synchronization lines must intersect the same chronological coordinate across all displayed lanes.

Composite, conceptual, astronomical, narrative, or misclassified legacy region labels must not be presented as ordinary geographic regions merely because they occur in places_regions.csv.

## Relationships
Relationship arrows/links must read literally Subject Entity ID -> Object Entity ID using the controlled relationship vocabulary. RELATED_TO synchronization links do not imply causation, contact, influence, or descent.

## Visual evidence
Do not invent a historical likeness. Where no defensible portrait exists, use a name/date treatment, authenticated artifact/coin/statue/manuscript/site image, or neutral symbolic treatment clearly presented as such.

## Density / significance
Rendering priority follows significance and synchronization value, not mere database existence. Master data may exceed what appears in a single view. Timeline and Feature tiers can progressively expose detail without deleting underlying records.

## Source/provenance behavior
The graphic need not print full citations beside every mark, but every rendered historical item must remain traceable through canonical IDs to its Date Claim and source/provenance record. Weak or pending legacy source cleanup does not authorize changing the historical claim.

## Initial rebuild acceptance tests
A render is acceptable only if:
1. identical years align across all lanes;
2. BCE/CE transition contains no year zero;
3. date ranges are mathematically scaled from canonical claims;
4. alternative/traditional claims remain labeled rather than merged;
5. entity/text/manuscript/artifact distinctions survive rendering;
6. no generated historical person, date, event, relationship, or likeness is introduced;
7. a rendered mark can be traced back to canonical IDs;
8. the output can be regenerated from the dataset after future HT-0601+ expansion.

## v1.0 foundation
The initial render foundation consists of 546 normalized entities, 600 date claims, 374 relationships, 245 legacy place/region labels, 376 legacy tradition/corpus labels, and 242 source records preserving complete HT-0001 through HT-0600 lineage.

Future expansion begins at HT-0601 and must use this same rendering contract unless the contract is explicitly versioned.
