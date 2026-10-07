#!/usr/bin/env python3
"""Validate the graphical renderer contract without external packages."""
import importlib.util, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
P=ROOT/"scripts"/"render_timeline_svg.py"
src=P.read_text(encoding="utf-8")
checks=[]
def check(name, ok):
 checks.append((name,bool(ok)))
# Static contract guards
check("SVG output", ".svg" in src)
check("canonical entities input", 'entities.csv' in src)
check("canonical date claims input", 'date_claims.csv' in src)
check("provenance IDs in tooltips", 'Date Claim ID' in src and 'Entity ID' in src)
check("evidence-class encoding", "dash_for" in src)
check("configurable window", "sys.argv[1]" in src and "sys.argv[2]" in src)
check("reject explicit year-zero bounds", "START==0 or END==0" in src)
check("vector text retained", "<text" in src)
check("no raster canvas", "<canvas" not in src.lower())
# Prevent regression to the old five-track cap.
check("old five-track cap absent", "tracks=[-10**9]*5" not in src)
failed=[n for n,v in checks if not v]
for n,v in checks: print(("PASS " if v else "FAIL ")+n)
if failed:
 print("FAILED:",", ".join(failed));sys.exit(1)
print("PASS render-contract static gate:",len(checks),"checks")
