# Human History Timeline — Project State

## Purpose
Build a synchronized global human-history knowledge base on one mathematical chronological axis.

## Current baseline
- Frozen legacy workbook: v0.16
- Legacy Master Timeline records: HT-0001 through HT-0600 (600 records)
- Legacy Sources sheet: 242 populated source rows through SRC-0243
- GitHub is the persistent project-state and normalized-data workspace going forward.
- The legacy Master Timeline is preserved while data is normalized.

## Phase 1 normalization — ACTIVE
A first complete structural normalization pass has been generated as v0.17 from the actual v0.16 workbook.

Current v0.17 counts:
- Legacy timeline records preserved: 600
- Normalized entities: 554
- Date claims: 600
- Relationships imported from explicit legacy Related IDs: 376
- Places & Regions labels: 245
- Traditions & Corpora legacy labels: 376
- Exact conceptual duplicate clusters conservatively merged: 46
- Formula/error scan: clean (0 #REF!, #DIV/0!, #VALUE!, #NAME?, #N/A matches)

The merge policy is deliberately conservative: false merges are worse than temporarily retaining extra entities. Every merged entity retains all contributing Legacy HT IDs and every legacy row retains its own Date Claim.

## v0.17 normalized sheets
- Entities
- Date Claims
- Relationships
- Places & Regions
- Traditions & Corpora

Existing legacy sheets remain present:
- Master Timeline
- Sources
- Schema & Rules
- Source Registry
- Research Queue

## Next work
1. Refine non-exact conceptual duplicate clusters not captured by exact normalized-name matching.
2. Replace generic RELATED_TO relationships with typed semantics where supported.
3. Refine Places & Regions hierarchy and Traditions & Corpora hierarchy.
4. Perform targeted source QA/corrections (including known legacy URL/date issues).
5. Persist canonical normalized CSV/JSON datasets in this repository.
6. Only after normalization QA is operational, resume expansion at HT-0601.

## Non-negotiable research rules
- No AI-invented historical content.
- Every historical assertion derives from an identifiable source or identifiable textual/traditional corpus.
- Traditional, religious, legendary, disputed, archaeological, and historically documented material may coexist with explicit classification.
- Competing chronologies are preserved rather than collapsed.
- Person, story/tradition, text composition, manuscript copy, artifact, and archaeological discovery are distinct entities/claims.
- One mathematical time axis; no silent chronology shifting.
- No-year-zero handling is explicit in normalized date claims.
- Inclusion is based on prominence, historical significance, synchronization value, or major significance within an important corpus—not mere existence.

## Continuity rule
Before substantial work, read PROJECT_STATE.md, SCHEMA.md, RESEARCH_RULES.md, and research/QUEUE.md. Commit durable state before ending a work session. Stop only for a genuine decision or blocker requiring user input.
