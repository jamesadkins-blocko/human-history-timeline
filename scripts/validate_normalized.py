#!/usr/bin/env python3
"""Validate canonical Human History Timeline CSV exports.

This script intentionally does not invent, infer, or repair historical data.
It validates exported normalized datasets against the frozen migration contract.
"""
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

EXPECTED = {
    "entities.csv": 546,
    "date_claims.csv": 600,
    "relationships.csv": 374,
    "places_regions.csv": 245,
    "traditions_corpora.csv": 376,
    "sources.csv": 242,
}

def read_csv(name):
    p = DATA / name
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def nonblank(row, *names):
    for n in names:
        v = row.get(n)
        if v not in (None, ""):
            return v
    return None

def main():
    tables = {name: read_csv(name) for name in EXPECTED}
    errors = []

    for name, expected in EXPECTED.items():
        actual = len(tables[name])
        if actual != expected:
            errors.append(f"{name}: expected {expected} rows, found {actual}")

    entities = tables["entities.csv"]
    claims = tables["date_claims.csv"]
    rels = tables["relationships.csv"]

    entity_ids = {nonblank(r, "entity_id") for r in entities}
    entity_ids.discard(None)
    if len(entity_ids) != len(entities):
        errors.append("entities.csv: blank or duplicate entity_id")

    claim_ids = [nonblank(r, "date_claim_id") for r in claims]
    if None in claim_ids or len(set(claim_ids)) != len(claim_ids):
        errors.append("date_claims.csv: blank or duplicate date_claim_id")

    rel_ids = [nonblank(r, "relationship_id") for r in rels]
    if None in rel_ids or len(set(rel_ids)) != len(rel_ids):
        errors.append("relationships.csv: blank or duplicate relationship_id")

    for r in claims:
        eid = nonblank(r, "entity_id")
        if eid not in entity_ids:
            errors.append(f"orphan date claim entity: {eid}")
        for field in ("start_min","start_preferred","start_max",
                      "end_min","end_preferred","end_max"):
            if str(r.get(field, "")).strip() == "0":
                errors.append(f"year zero prohibited: {r.get('date_claim_id')} {field}")

    for r in rels:
        s = nonblank(r, "subject_entity_id")
        o = nonblank(r, "object_entity_id")
        if s not in entity_ids:
            errors.append(f"orphan relationship subject: {s}")
        if o not in entity_ids:
            errors.append(f"orphan relationship object: {o}")

    # Legacy lineage is preserved on Entities, not Date Claims.
    # Merged conceptual entities may carry multiple HT IDs in Legacy HT ID(s).
    import re
    legacy = []
    for r in entities:
        v = nonblank(r, "Legacy HT ID(s)", "legacy_ht_ids")
        if v:
            legacy.extend(re.findall(r"HT-\\d{4}", str(v)))
    expected_ht = {f"HT-{i:04d}" for i in range(1,601)}
    got_ht = set(legacy)
    missing = sorted(expected_ht - got_ht)
    extra = sorted(got_ht - expected_ht)
    duplicates = sorted(x for x in got_ht if legacy.count(x) != 1)
    if missing:
        errors.append(f"missing legacy HT IDs: {missing[:20]}")
    if extra:
        errors.append(f"unexpected legacy HT IDs: {extra[:20]}")
    if len(legacy) != 600 or len(got_ht) != 600 or duplicates:
        errors.append("legacy HT lineage must contain HT-0001..HT-0600 exactly once")

    if errors:
        print("VALIDATION FAILED")
        for e in errors:
            print(" -", e)
        raise SystemExit(1)

    print("VALIDATION PASSED")
    for name in EXPECTED:
        print(f" - {name}: {len(tables[name])}")
    print(" - orphan foreign keys: 0")
    print(" - normalized year-zero violations: 0")
    print(" - HT-0001..HT-0600 coverage: complete")

if __name__ == "__main__":
    main()
