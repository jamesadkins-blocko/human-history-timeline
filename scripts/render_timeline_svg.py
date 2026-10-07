#!/usr/bin/env python3
"""Generate the first authoritative synchronized SVG timeline from canonical CSV data.

No historical content is invented here. Marks are emitted only from canonical
Entities + Date Claims having normalized numeric coordinates.
"""
from __future__ import annotations
import csv, html
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"; OUT=ROOT/"rendered"\n\n# Evidence-class visual encoding. Classification remains descriptive, never a truth score.\nCLASS_STYLES=[\n ("Traditional",("none","4 3")),("religious",("none","4 3")),("Legend",("none","2 3")),("myth",("none","2 3")),\n ("Artifact",("none","")),("inscription",("none","")),("Manuscript",("none","6 2")),("text",("none","6 2")),\n ("Approx",("none","3 2")),("disputed",("none","3 2"))]\n\ndef dash_for(classification):\n s=(classification or "").lower()\n if "legend" in s or "myth" in s:return "2 3"\n if "traditional" in s or "religious" in s:return "4 3"\n if "manuscript" in s or "text" in s:return "6 2"\n if "approx" in s or "disputed" in s:return "3 2"\n return ""
START=-1500; END=500; PIXELS_PER_YEAR=6.0; LEFT=520; RIGHT=120; TOP=210\nW=int(LEFT+RIGHT+(END-START)*PIXELS_PER_YEAR)
LANE_H=180

LANES=[
 ("Mesopotamia / Persia", {"REG-0035","REG-0036","REG-0160","REG-0161","REG-0173","REG-0225","REG-0226","REG-0125","REG-0127","REG-0128","REG-0129","REG-0130"}),
 ("Egypt", {"REG-0086","REG-0081","REG-0087","REG-0088","REG-0089","REG-0090"}),
 ("Kush / Nubia", {"REG-0149","REG-0186"}),
 ("Levant / Judea", {"REG-0147","REG-0140","REG-0139","REG-0144","REG-0193","REG-0194","REG-0201","REG-0105"}),
 ("Greece / Rome", {"REG-0001","REG-0023","REG-0114","REG-0155","REG-0195","REG-0196","REG-0134"}),
 ("South Asia", {"REG-0122","REG-0124","REG-0179","REG-0185","REG-0204","REG-0205"}),
 ("China / East Asia", {"REG-0066","REG-0076","REG-0150"}),
 ("Central Asia", {"REG-0058","REG-0059","REG-0079","REG-0230","REG-0238"}),
 ("Africa", {"REG-0004","REG-0092","REG-0093","REG-0120","REG-0231","REG-0172"}),
 ("Mesoamerica", {"REG-0117","REG-0159","REG-0187","REG-0154"}),
 ("South America", {"REG-0017","REG-0018","REG-0061","REG-0062","REG-0180","REG-0181","REG-0190","REG-0203","REG-0212"}),
 ("North America", {"REG-0065","REG-0085","REG-0174","REG-0176","REG-0182","REG-0213","REG-0163"}),
 ("Oceania", {"REG-0034","REG-0168","REG-0189","REG-0242","REG-0132","REG-0133"}),
]

def rows(name):
 with (DATA/name).open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def num(v):
 try:return float(v) if str(v).strip() else None
 except:return None
def esc(s):return html.escape(str(s or ""))
def x(year):
 # astronomical-like continuous rendering coordinate with no displayed year zero.
 return LEFT+(year-START)/(END-START)*(W-LEFT-RIGHT)
def label_year(y):
 y=int(y)
 return f"{abs(y)} BCE" if y<0 else f"{y} CE"

entities={r["Entity ID"]:r for r in rows("entities.csv")}
claims=rows("date_claims.csv")
marks=defaultdict(list); skipped=0
for c in claims:
 e=entities.get(c["Entity ID"])
 if not e: continue
 s=num(c["Start Preferred"]) or num(c["Start Min"])
 en=num(c["End Preferred"]) or num(c["End Max"]) or s
 if s is None: skipped+=1; continue
 if en is None: en=s
 if en<START or s>END: continue
 reg=e["Region ID"]
 lane=next((i for i,(_,ids) in enumerate(LANES) if reg in ids),None)
 if lane is None: continue
 marks[lane].append((s,en,e,c))

height=TOP+len(LANES)*LANE_H+100
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}">']
svg+=['<rect width="100%" height="100%" fill="#f7f4ed"/>',
'<style>text{font-family:Arial,sans-serif;fill:#171717}.title{font-size:38px;font-weight:700}.sub{font-size:19px}.lane{font-size:21px;font-weight:700}.tick{font-size:15px}.item{font-size:14px}.meta{font-size:12px;fill:#555}</style>',
'<text x="30" y="48" class="title">Synchronized Human History — v1.0 Foundation</text>',
f'<text x="30" y="78" class="sub">Canonical render • {START*-1} BCE–{END} CE • one shared chronological axis • generated from normalized data</text>',
f'<text x="30" y="103" class="meta">Numeric claims only. {skipped} non-numeric/textual date claims remain in the database and are intentionally not assigned invented coordinates.</text>']

# axis: skip display year zero
for yr in range(START,END+1,100):
 if yr==0: continue
 xx=x(yr); svg.append(f'<line x1="{xx:.1f}" y1="125" x2="{xx:.1f}" y2="{height-55}" stroke="#bbb" stroke-width="1"/>')
 svg.append(f'<text x="{xx:.1f}" y="145" text-anchor="middle" class="tick">{esc(label_year(yr))}</text>')
# explicit BCE/CE boundary at mathematical midpoint between -1 and +1
boundary=(x(-1)+x(1))/2
svg.append(f'<line x1="{boundary:.1f}" y1="118" x2="{boundary:.1f}" y2="{height-55}" stroke="#111" stroke-width="2"/>')
svg.append(f'<text x="{boundary+5:.1f}" y="122" class="meta">1 BCE | 1 CE (no year 0)</text>')

for li,(name,_) in enumerate(LANES):
 y0=TOP+li*LANE_H
 svg.append(f'<rect x="0" y="{y0}" width="{W}" height="{LANE_H}" fill="{"#ffffff" if li%2==0 else "#efede7"}" opacity=".65"/>')
 svg.append(f'<text x="25" y="{y0+27}" class="lane">{esc(name)}</text>')
 items=sorted(marks[li],key=lambda z:(z[0],z[1]))
 tracks=[-10**9]*7
 for s,en,e,c in items:
  xs=max(x(START),x(max(s,START))); xe=min(x(END),x(min(en,END)))
  t=next((k for k,v in enumerate(tracks) if xs>v+8),None)
  if t is None: continue
  yy=y0+43+t*20; tracks[t]=max(xe,xs+65)
  cls=esc(e["Classification"]); nm=esc(e["Display Name"] or e["Canonical Name"]); dash=dash_for(e["Classification"])
  title=esc(f'{e["Entity ID"]} | {c["Date Claim ID"]} | {c["Display Date"]} | {e["Classification"]}')
  if abs(xe-xs)<4:
   svg.append(f'<circle cx="{xs:.1f}" cy="{yy}" r="4"><title>{title}</title></circle>')
  else:
   svg.append(f'<line x1="{xs:.1f}" y1="{yy}" x2="{xe:.1f}" y2="{yy}" stroke="#222" stroke-width="5" stroke-dasharray="{dash}"><title>{title}</title></line>')
  svg.append(f'<text x="{xs+6:.1f}" y="{yy-5}" class="item">{nm}<title>{title}</title></text>')

# legend
ly=height-62
svg.append(f'<text x="30" y="{ly}" class="meta">Line encoding: solid = documented/artifact or other non-special classification • 4/3 dash = traditional/religious • 2/3 = legendary/mythological • 6/2 = manuscript/text • 3/2 = approximate/disputed</text>')
svg.append(f'<text x="30" y="{height-25}" class="meta">Source: canonical data/*.csv • Generated by scripts/render_timeline_svg.py • Historical placement is data-driven, not image-generated.</text>')
svg.append('</svg>')
OUT.mkdir(exist_ok=True)
p=OUT/"timeline_v1_foundation_1500BCE_500CE.svg"; p.write_text("\n".join(svg),encoding="utf-8")
print(p)
print("rendered marks",sum(len(v) for v in marks.values()),"numeric textual claims skipped",skipped)
