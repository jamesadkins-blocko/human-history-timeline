# v0.20 Hierarchy QA

Status: IN PROGRESS

## Audit result

The current Places & Regions and Traditions & Corpora tables are legacy-label registries, not true ontologies.

### Places & Regions
- 245 rows
- all 245 typed as `Legacy region label`
- 0 parent-region assignments

The labels mix several fundamentally different concepts:
- geographic regions (e.g. Africa, Europe, Levant)
- modern countries (e.g. China, India)
- cities/sites (e.g. Athens, Babylon, Qumran)
- empires/political entities (e.g. Byzantine Empire, Roman Empire)
- compound synchronization scopes (e.g. Europe / Americas / Africa / Asia)
- conceptual/non-geographic scopes (e.g. Global science)
- astronomical locations (Moon, Earth orbit, Sun-Earth L2)
- textual/traditional settings (Primeval biblical world, Atlantic as described by Plato)
- at least one clear non-place label: Codex Sinaiticus

### Traditions & Corpora
- 376 rows
- all 376 typed as `Legacy tradition/culture label`
- 0 parent-tradition assignments

These labels mix:
- civilizations/cultures
- religions and denominations
- dynastic/political identities
- intellectual/scientific traditions
- coalitions and conflict participants
- paired comparison labels
- modern national identities
- archaeological cultures
- textual/traditional corpora

## Decision

Do not manufacture parent IDs directly from slash-separated names. A string such as `British / South Asian` is not necessarily a child of either `British` or `South Asian`; it may represent an interaction/context label.

The safe v0.20 hierarchy strategy is therefore:
1. preserve every legacy label unchanged;
2. classify label kind before assigning parentage;
3. assign parents only where containment is explicit and unambiguous;
4. move political entities, texts, conceptual scopes, and astronomical locations out of a purely geographic ontology in a later controlled migration rather than pretending they are geographic regions;
5. document malformed/misclassified labels for correction without deleting historical lineage.

## Immediate QA flags
- REG-0069 `Codex Sinaiticus` is not a geographic region.
- REG-0192 `Primeval biblical world` is a traditional/textual setting, not modern geography.
- REG-0026 `Atlantic (as described by Plato)` is a narrative geographic claim and must remain qualified.
- REG-0031 `Atlantic / legendary` is a qualified narrative scope.
- REG-0113 `Global science` is conceptual rather than geographic.
- REG-0051 `CERN / global` mixes institution and scope.
- REG-0073 `Earth orbit`, REG-0164 `Moon`, and REG-0217 `Sun-Earth L2 / deep space` require an astronomical-location type rather than terrestrial region hierarchy.

These are classification issues, not grounds to discard the associated historical records.
