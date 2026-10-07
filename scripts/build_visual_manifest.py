#!/usr/bin/env python3
"""Build the visual-scene manifest consumed by the illustrated timeline layer.

This does not invent imagery. It selects canonical entities/date claims and
assigns a defensible presentation treatment from existing metadata.
"""
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"data"; OUT=ROOT/"rendered"
def rows(n):
 with (DATA/n).open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def treatment(e):
 t=(e["Entity Type"]+" "+e["Subtype"]+" "+e["Classification"]).lower()
 if "manuscript" in t:return "manuscript-or-text-witness"
 if "artifact" in t or "inscription" in t:return "artifact-or-inscription"
 if "site" in t or "monument" in t:return "site-or-monument"
 if "person" in t or "ruler" in t or "figure" in t:return "authenticated-likeness-or-neutral"
 if "civilization" in t or "empire" in t or "dynasty" in t or "period" in t:return "civilization-band"
 if "event" in t or "migration" in t:return "event-marker"
 if "text" in t:return "text-tradition"
 return "typographic-or-neutral"
ents={r["Entity ID"]:r for r in rows("entities.csv")}
claims=rows("date_claims.csv")
visual_sources=rows("visual_sources.csv") if (DATA/"visual_sources.csv").exists() else []
seen_visual_ids=set()
for a in visual_sources:
 vid=a.get("Visual Source ID","").strip()
 if not vid: raise SystemExit("visual_sources.csv contains a blank Visual Source ID")
 if vid in seen_visual_ids: raise SystemExit("duplicate Visual Source ID: "+vid)
 seen_visual_ids.add(vid)
 if a.get("Verification Status","").strip().lower()=="verified":
  if not a.get("Source URL","").strip() or not a.get("Source Organization","").strip() or not a.get("License / Rights","").strip():
   raise SystemExit("verified visual asset lacks provenance/rights: "+vid)
  if not a.get("Image URL","").strip() and not a.get("Local Asset Path","").strip():
   print("WARNING verified visual asset has no renderable image yet:",vid)
  if a.get("Image URL","").strip() and "metmuseum.org" in a.get("Source URL","") and "/original/" not in a.get("Image URL",""):
   print("WARNING Met asset is not registered with original-resolution image:",vid)
verified_assets={}
for a in visual_sources:
 if a.get("Verification Status","").strip().lower()=="verified" and a.get("Entity ID"):
  verified_assets.setdefault(a["Entity ID"],[]).append(a)
by={}; 
for c in claims: by.setdefault(c["Entity ID"],[]).append(c)
out=[]
for eid,e in ents.items():
 if e["Significance Tier"] not in ("Master","Timeline","Feature"):continue
 numeric=[c for c in by.get(eid,[]) if c["Start Preferred"].strip() or c["Start Min"].strip()]
 if not numeric:continue
 out.append({"entity_id":eid,"name":e["Display Name"] or e["Canonical Name"],"entity_type":e["Entity Type"],
 "classification":e["Classification"],"significance_tier":e["Significance Tier"],"region_id":e["Region ID"],
 "culture_tradition":e["Culture / Tradition"],"visual_treatment":treatment(e),
 "image_policy":"Use only sourced/defensible historical imagery; never invent a likeness.",
 "verified_visual_assets":[{"visual_source_id":a["Visual Source ID"],"asset_type":a["Asset Type"],"source_url":a["Source URL"],"image_url":a.get("Image URL",""),"source_organization":a["Source Organization"],"rights":a["License / Rights"],"attribution":a["Attribution"],"local_asset_path":a["Local Asset Path"],"verification_status":a["Verification Status"]} for a in verified_assets.get(eid,[])],
 "preferred_visual_source_id":(verified_assets.get(eid,[{}])[0].get("Visual Source ID","") if verified_assets.get(eid) else ""),
 "date_claim_ids":[c["Date Claim ID"] for c in numeric]})
OUT.mkdir(exist_ok=True)
p=OUT/"visual_scene_manifest.json";p.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
print("visual candidates",len(out),p)
