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


## Russian Revolution reference review
The legacy Library of Congress Soviet Archives exhibit is real and useful as an archival collection, but it is broader than the specific 1917 timeline claim. A more directly scoped Library of Congress primary-source item is Melville Elijah Stone, *The Russian revolution* (1917), LCCN 17023073. LOC also holds contemporary/near-contemporary materials and a dedicated subject collection for the Revolution of 1917–1921.

QA disposition: retain the Soviet Archives exhibit as a broader archival resource, but prefer a directly scoped 1917 LOC item for the specific Russian Revolution timeline claim.

## Nanjing / Nanking source review
The previously suspected USHMM Nanjing URL should not be treated as verified merely because it resembles a USHMM article path. Live search did not establish that page as a dependable current source.

The U.S. Department of State Office of the Historian has primary diplomatic records in *Foreign Relations of the United States, Diplomatic Papers, 1937, The Far East*, documenting events at Nanking in December 1937, including the Panay incident and contemporary reporting from the theater.

QA disposition: replace/augment the questionable legacy Nanjing URL with authoritative archival/diplomatic material and, in a later source-enrichment pass, add a modern scholarly source specifically addressing the Nanjing Massacre. Do not silently broaden a Panay-specific document into evidence for every massacre claim.


## Nanjing source enrichment — verified
A dedicated archival source has now been identified: Yale University Library's Nanking Massacre Project, a digital archive from Yale Divinity Library Special Collections. It contains letters, diaries, reports, photographs, and films from American missionaries and other witnesses who remained in Nanking during the 1937–1938 occupation. The project explicitly describes these as firsthand accounts and warns that the collection is an important historical lens rather than a comprehensive account.

Examples in the archive include Miner Searle Bates's December 1937 / January 1938 notes and reports and John Magee film material documenting victims and refugee conditions.

A modern scholarly complement is Zhang Sheng, "The Nanjing Massacre as recorded in American sources," Chinese Studies in History 50(4), 2017/2018, pp. 279–298.

QA disposition:
- Yale Nanking Massacre Project: suitable primary-source archival collection for the Nanjing Massacre claim.
- Zhang Sheng article: suitable modern scholarly secondary source focused on the evidentiary value of American records.
- retain FRUS/Panay documentation only for diplomatic and contextual claims it directly supports.
- retire the unverified legacy USHMM Nanjing URL from preferred-source status; do not delete frozen lineage.
