# Illustrated Layer

The vector chronology renderer is the chassis. The illustrated layer is driven by `rendered/visual_scene_manifest.json`, generated from canonical entity/date metadata.

Presentation treatments are deliberately conservative:
- civilization-band
- authenticated-likeness-or-neutral
- artifact-or-inscription
- manuscript-or-text-witness
- site-or-monument
- event-marker
- text-tradition
- typographic-or-neutral

A treatment is not an image assertion. Before an external image is incorporated, it must be sourced and defensible for the entity. If no defensible likeness exists, use an artifact, statue, coin, manuscript, site, neutral symbol, or typography. Never generate a face and imply it is historical evidence.

The manifest preserves Entity IDs and Date Claim IDs so visual composition cannot detach from canonical chronology.


## Delivery simplification

The provenance/validation framework is now sufficient. Do not add new infrastructure unless a concrete rendering defect requires it.

Immediate priority is visible output:
1. Build one polished illustrated hero slice (600 BCE–300 BCE).
2. Use canonical chronology and existing neutral fallbacks.
3. Add verified historical imagery opportunistically; missing imagery must not block the slice.
4. Judge success by the rendered panorama, not by additional schemas, registries, validators, or pipeline abstractions.
5. After visual approval, scale the same composition system outward across the master chronology.


## Native SVG interaction rule

Do not add custom zoom, pan, navigator, minimap, or other viewport controls to the canonical SVG. Standard SVG viewers already provide native zoom/pan. Preserve the artwork as a clean, portable vector document and spend visual space only on historical content. Interactive-web controls, if ever desired, belong in a separate derivative viewer rather than the master SVG.
