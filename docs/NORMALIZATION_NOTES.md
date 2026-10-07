# Normalization notes

## v0.17 first pass
The first structural pass preserved all 600 legacy timeline rows as 600 date claims and consolidated 46 exact conceptual duplicate clusters into 554 normalized entities.

## Conservative merge policy
A merge requires identity of the conceptual entity, not merely similar names or historical relationship.

Examples that must remain distinct:
- Enoch (traditional figure) vs 1 Enoch (textual tradition) vs 4Q201 (manuscript)
- Gilgamesh (figure) vs Epic of Gilgamesh (work/tradition) vs individual tablets
- Plato (person) vs Timaeus/Critias (works) vs Atlantis narrative date claim
- Qin Shi Huang (person) vs Terracotta Army (archaeological/artifact complex)
- Second Temple (institution/building/period claims) vs its completion/destruction events where separately modeled
- Trojan War narrative/event tradition vs Achilles/Odysseus vs Homeric epics

## Next duplicate review
Non-exact candidates require explicit review. Do not auto-merge with fuzzy matching. Priority clusters include Buddha, Zarathustra, Jesus, Second Temple records, Qin/Terracotta records, medieval density-pass duplicates, early-modern duplicates, and modern v0.9 vs v0.15/v0.16 duplicates.

## Relationship policy
Legacy Related IDs were imported as RELATED_TO. They are evidence of an intended link, not evidence of a specific semantic relation. Upgrade them only when the workbook/source context supports the type.
