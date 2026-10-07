# v0.20 Source QA

Status: IN PROGRESS

## Structural audit
- canonical source rows: 242
- duplicate Source IDs: 0
- orphan Source IDs referenced by Date Claims or Relationships: 0
- actual canonical columns: Source ID; Title / Institution; Source Type; URL; Use / Scope; Notes

## Verified targeted corrections / findings

### HT-0277 / Amarna
The previously flagged malformed Met Amarna URL must not be reused. Current Metropolitan Museum collection records independently confirm Akhenaten / Amarna-period objects dated ca. 1347–1330 BCE, including object 544686 (Funerary Figure of Akhenaten) and related Amarna objects. Use a current Met object/collection record when the legacy claim requires an Amarna reference.

### An Shigao chronology
The old approximate endpoint must not be presented as a secure lifespan date.

Source review establishes:
- arrival/activity in Luoyang from 148 CE is well supported;
- Encyclopaedia Iranica reports arrival in 148 and notes the scarcity of reliable biographical information;
- the Chinese Buddhist Canonical Attributions project gives fl. ca. 148–168, citing Nattier 2008;
- modern scholarship discussing early evidence can place his death around 170, while other reference traditions extend activity to ca. 180.

Normalization action: represent An Shigao as a floruit/activity chronology with uncertainty, not a precise birth/death lifespan. Preserve competing scholarly ranges rather than choosing an artificial exact endpoint.

### Mexican Constitution of 1917
Library of Congress item 17021628 is a digitized primary-source record titled "Mexican constitution of 1917", published Washington, D.C., 1917. This is a clean replacement/reference for the corresponding timeline claim.

## Still queued
- Russian Revolution / Library of Congress reference suitability
- Nanjing Massacre source replacement/verification
- systematic HTTP reachability sweep for legacy URLs
- source-quality tiering (primary/institutional scholarly/reference/secondary)
