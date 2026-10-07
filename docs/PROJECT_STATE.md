# Human History Timeline — Project State

## Purpose
Build a synchronized global human-history knowledge base on one mathematical chronological axis.

## Current baseline
- Latest workbook release: v0.16
- Legacy Master Timeline records: HT-0001 through HT-0600
- Current record count: 600
- GitHub is the persistent source-of-truth workspace going forward.
- The legacy Master Timeline must be preserved while the data is normalized into entities, date claims, relationships, places/regions, traditions/corpora, and sources.

## Non-negotiable research rules
- No AI-invented historical content.
- Every historical assertion must derive from an identifiable source or clearly identified textual/traditional corpus.
- Traditional, religious, legendary, disputed, archaeological, and historically documented material may coexist with explicit classification.
- Competing chronologies are preserved rather than collapsed.
- Person, story/tradition, text composition, manuscript copy, artifact, and archaeological discovery are distinct entities/claims.
- One mathematical time axis; no silent chronology shifting.
- No-year-zero handling must be explicit in normalized date claims.
- Inclusion is based on prominence, historical significance, synchronization value, or major significance within an important corpus—not mere existence.

## Current transition
The next architectural priority is normalization of the existing 600-record workbook into the persistent repository schema before uncontrolled flat-record expansion continues.

## Automation handoff
Each continuation run should read this file and the repository rules/schema first, take the next unfinished item from the research/migration queue, validate its work, commit durable state, and update this file before ending. Stop only for a genuine decision or blocker requiring user input.
