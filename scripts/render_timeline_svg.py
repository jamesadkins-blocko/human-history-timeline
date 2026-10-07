#!/usr/bin/env python3
"""Generate the first authoritative synchronized SVG timeline from canonical CSV data.

No historical content is invented here. Marks are emitted only from canonical
Entities + Date Claims having normalized numeric coordinates.
"""
from __future__ import annotations
import csv, html, sys
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"; OUT=ROOT/"rendered"

# Evidence-class visual encoding. Classification remains descriptive, never a truth score.
CLASS_STYLES=[
 ("Traditional",("none","4 3")),("religious",("none","4 3")),("Legend",("none","2 3")),("myth",("none","2 3")),
 ("Artifact",("none","")),("inscription",("none","")),("Manuscript",("none","6 2")),("text",("none","6 2")),
 ("Approx",("none","3 2")),("disputed",("none","3 2"))]

def dash_for(classification):
 s=(classification or "").lower()
 if "legend" in s or "myth" in s:return "2 3"
 if "traditional" in s or "religious" in s:return "4 3"
 if "manuscript" in s or "text" in s:return "6 2"
 if "approx" in s or "disputed" in s:return "3 2"
 return ""
def visual_kind(e):
 # Neutral vector glyphs indicate record type only; they are never historical likenesses.
 s=" ".join([e.get("Record Type",""),e.get("Subtype",""),e.get("Classification","")]).lower()
 if "manuscript" in s or "text" in s or "literary" in s:return "document"
 if "artifact" in s or "inscription" in s or "coin" in s:return "artifact"
 if "site" in s or "monument" in s or "city" in s:return "site"
 if "person" in s or "figure" in s or "ruler" in s:return "person"
 if "event" in s or "war" in s or "battle" in s:return "event"
 return "record"

def feature_panel(kind,x0,y0,name,title):
 # Illustrated vector anchor: a deliberately neutral visual scene, never an invented likeness.
 # Verified historical imagery will occupy this same panel when present in visual_sources.csv.
 w=118; h=72; left=x0-w/2; top=y0-h
 parts=[f'<g class="feature-panel"><rect x="{left:.1f}" y="{top:.1f}" width="{w}" height="{h}" rx="7" fill="#f7edd8" stroke="#806849" stroke-width="1.2" filter="url(#softShadow)"/>']
 if kind=="site":
  parts.append(f'<path d="M{left+12:.1f},{top+53:.1f} H{left+106:.1f} M{left+23:.1f},{top+53:.1f} V{top+31:.1f} M{left+47:.1f},{top+53:.1f} V{top+31:.1f} M{left+71:.1f},{top+53:.1f} V{top+31:.1f} M{left+95:.1f},{top+53:.1f} V{top+31:.1f} M{left+14:.1f},{top+31:.1f} H{left+104:.1f} L{x0:.1f},{top+13:.1f} Z" fill="none" stroke="#6d5438" stroke-width="2"/>')
 elif kind=="document":
  parts.append(f'<rect x="{x0-23:.1f}" y="{top+12:.1f}" width="46" height="46" rx="2" fill="#fff9ea" stroke="#806849"/><path d="M{x0-15:.1f},{top+23:.1f} H{x0+15:.1f} M{x0-15:.1f},{top+31:.1f} H{x0+15:.1f} M{x0-15:.1f},{top+39:.1f} H{x0+10:.1f} M{x0-15:.1f},{top+47:.1f} H{x0+13:.1f}" stroke="#8b7555"/>')
 elif kind=="artifact":
  parts.append(f'<path d="M{x0-19:.1f},{top+17:.1f} Q{x0-27:.1f},{top+48:.1f} {x0:.1f},{top+59:.1f} Q{x0+27:.1f},{top+48:.1f} {x0+19:.1f},{top+17:.1f} Z" fill="#c6a56d" stroke="#6d5438" stroke-width="2"/>')
 elif kind=="event":
  parts.append(f'<path d="M{x0:.1f},{top+10:.1f} L{x0+7:.1f},{top+29:.1f} L{x0+28:.1f},{top+35:.1f} L{x0+7:.1f},{top+41:.1f} L{x0:.1f},{top+62:.1f} L{x0-7:.1f},{top+41:.1f} L{x0-28:.1f},{top+35:.1f} L{x0-7:.1f},{top+29:.1f} Z" fill="#9a6040" opacity=".9"/>')
 else:
  parts.append(f'<circle cx="{x0:.1f}" cy="{top+28:.1f}" r="13" fill="#d2b98e" stroke="#6d5438"/><path d="M{x0-23:.1f},{top+59:.1f} Q{x0:.1f},{top+35:.1f} {x0+23:.1f},{top+59:.1f}" fill="#d2b98e" stroke="#6d5438"/>')
 parts.append(f'<title>{title}</title></g>')
 return "".join(parts)

def glyph(kind,x0,y0):
 if kind=="person":
  return f'<g transform="translate({x0:.1f},{y0:.1f})"><circle cx="0" cy="-5" r="4" fill="#493827"/><path d="M-6,7 Q0,-1 6,7" fill="none" stroke="#493827" stroke-width="2"/></g>'
 if kind=="document":
  return f'<g transform="translate({x0:.1f},{y0:.1f})"><rect x="-5" y="-8" width="10" height="14" rx="1" fill="#f7f0df" stroke="#493827"/><path d="M-3,-4 H3 M-3,0 H3 M-3,4 H1" stroke="#493827" stroke-width="1"/></g>'
 if kind=="artifact":
  return f'<g transform="translate({x0:.1f},{y0:.1f})"><path d="M-5,-6 Q-7,3 0,7 Q7,3 5,-6 Z" fill="#c7a66b" stroke="#493827"/></g>'
 if kind=="site":
  return f'<g transform="translate({x0:.1f},{y0:.1f})"><path d="M-7,6 H7 M-5,6 V-2 M0,6 V-2 M5,6 V-2 M-7,-2 H7 L0,-8 Z" fill="none" stroke="#493827" stroke-width="1.5"/></g>'
 if kind=="event":
  return f'<g transform="translate({x0:.1f},{y0:.1f})"><path d="M0,-8 L2,-2 L8,0 L2,2 L0,8 L-2,2 L-8,0 L-2,-2 Z" fill="#8d5a3b"/></g>'
 return f'<circle cx="{x0:.1f}" cy="{y0:.1f}" r="3" fill="#493827"/>'
START=int(sys.argv[1]) if len(sys.argv)>1 else -1500
END=int(sys.argv[2]) if len(sys.argv)>2 else 500
if START==0 or END==0 or START>=END: raise SystemExit("Use signed years with no year zero; START must be < END.")
PIXELS_PER_YEAR=float(sys.argv[3]) if len(sys.argv)>3 else 6.0
LEFT=520; RIGHT=120; TOP=210
W=int(LEFT+RIGHT+(CHRONO_SPAN if 'CHRONO_SPAN' in globals() else (END-START))*PIXELS_PER_YEAR)
BASE_LANE_H=180
HERO_SLICE=(START==-600 and END==-300)
HERO_TRACK_STEP=34 if HERO_SLICE else TRACK_STEP
TRACK_STEP=20
TRACK_TOP=43

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
def image_href(asset):
 # Prefer a repository-local, rights-reviewed asset so the SVG works offline on Android.
 local=(asset.get("Local Asset Path") or "").strip()
 if local:
  p=ROOT/local
  if p.exists():
   mime=mimetypes.guess_type(str(p))[0] or "image/jpeg"
   return "data:"+mime+";base64,"+base64.b64encode(p.read_bytes()).decode("ascii")
 # Remote URL remains a development fallback; final archival SVGs should use local embedded assets.
 return (asset.get("Image URL") or "").strip()
def chrono(year):
 # Historical signed-year coordinate: -1 (1 BCE) is immediately followed by +1 (1 CE).
 # There is no year-zero slot on the rendered clock.
 if year == 0: raise ValueError("year zero is not a valid historical coordinate")
 return year if year < 0 else year - 1

CHRONO_START=chrono(START); CHRONO_END=chrono(END)
CHRONO_SPAN=CHRONO_END-CHRONO_START
W=int(LEFT+RIGHT+CHRONO_SPAN*PIXELS_PER_YEAR)
def x(year):
 return LEFT+(chrono(year)-CHRONO_START)/(CHRONO_END-CHRONO_START)*(W-LEFT-RIGHT)
def label_year(y):
 y=int(y)
 return f"{abs(y)} BCE" if y<0 else f"{y} CE"

entities={r["Entity ID"]:r for r in rows("entities.csv")}
claims=rows("date_claims.csv")
visual_sources=rows("visual_sources.csv") if (DATA/"visual_sources.csv").exists() else []
visual_manifest_path=OUT/"visual_scene_manifest.json"
verified_assets={}
for a in visual_sources:
 if a.get("Verification Status","").strip().lower()=="verified" and a.get("Entity ID"):
  verified_assets.setdefault(a["Entity ID"],[]).append(a)
marks=defaultdict(list); skipped=0
for c in claims:
 e=entities.get(c["Entity ID"])
 if not e: continue
 s=num(c["Start Preferred"])
 if s is None: s=num(c["Start Min"])
 en=num(c["End Preferred"])
 if en is None: en=num(c["End Max"])
 if en is None: en=s
 if s is None: skipped+=1; continue
 if en is None: en=s
 if en<START or s>END: continue
 reg=e["Region ID"]
 lane=next((i for i,(_,ids) in enumerate(LANES) if reg in ids),None)
 if lane is None: continue
 marks[lane].append((s,en,e,c))

# Pre-compute collision tracks so each lane grows to fit all canonical marks.
lane_layouts=[]
for li,(name,_) in enumerate(LANES):
 items=sorted(marks[li],key=lambda z:(z[0],z[1]))
 track_ends=[]; placed=[]
 for s,en,e,c in items:
  xs=max(x(START),x(max(s,START))); xe=min(x(END),x(min(en,END)))
  t=next((k for k,v in enumerate(track_ends) if xs>v+8),None)
  if t is None:
   track_ends.append(-10**9); t=len(track_ends)-1
  track_ends[t]=max(xe,xs+65)
  placed.append((s,en,e,c,xs,xe,t))
 lane_h=max(BASE_LANE_H, TRACK_TOP+max(1,len(track_ends))*HERO_TRACK_STEP+45)
 lane_layouts.append((name,placed,lane_h))

height=TOP+sum(z[2] for z in lane_layouts)+100
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}">']
svg+=['<rect width="100%" height="100%" fill="url(#paper)"/>',
'''<defs>
 <linearGradient id="paper" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f8f2e4"/><stop offset="100%" stop-color="#e8dfca"/></linearGradient>
 <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="2" stdDeviation="2" flood-opacity=".18"/></filter>
</defs>
<style>
text{font-family:Georgia,"Times New Roman",serif;fill:#211b14}
.title{font-size:40px;font-weight:700;letter-spacing:.4px}.sub{font-size:18px;fill:#5c4c3b}
.lane{font-size:22px;font-weight:700;letter-spacing:.3px}.tick{font-size:14px;fill:#6b5a46}
.item{font-size:14px;font-weight:600}.meta{font-family:Arial,sans-serif;font-size:12px;fill:#6a6258}
</style>''',
f'<text x="30" y="48" class="title">{"The World, 600–300 BCE" if HERO_SLICE else "Synchronized Human History — v1.0 Foundation"}</text>',
f'<text x="30" y="78" class="sub">{"Illustrated synchronized panorama • " if HERO_SLICE else "Canonical render • "}{label_year(START)}–{label_year(END)} • one shared chronological axis</text>',
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

y_cursor=TOP
for li,(name,items,lane_h) in enumerate(lane_layouts):
 y0=y_cursor; y_cursor+=lane_h
 svg.append(f'<rect x="0" y="{y0}" width="{W}" height="{lane_h}" fill="{"#f7f0df" if li%2==0 else "#e8ddc5"}" opacity=".72"/>')
 svg.append(f'<text x="25" y="{y0+27}" class="lane">{esc(name)}</text>')
 for s,en,e,c,xs,xe,t in items:
  yy=y0+TRACK_TOP+t*HERO_TRACK_STEP
  cls=esc(e["Classification"]); nm=esc(e["Display Name"] or e["Canonical Name"]); dash=dash_for(e["Classification"])
  title=esc(f'{e["Entity ID"]} | {c["Date Claim ID"]} | {c["Display Date"]} | {e["Classification"]}')
  kind=visual_kind(e)
  svg.append(glyph(kind,xs,yy))
  if abs(xe-xs)<4:
   svg.append(f'<circle cx="{xs:.1f}" cy="{yy}" r="5" fill="#493827" filter="url(#softShadow)"><title>{title}</title></circle>')
  else:
   svg.append(f'<line x1="{xs:.1f}" y1="{yy}" x2="{xe:.1f}" y2="{yy}" stroke="#493827" stroke-width="6" stroke-linecap="round" stroke-dasharray="{dash}"><title>{title}</title></line>')
  # Label cards create a readable museum-caption hierarchy while preserving the exact mark coordinate.
  tier=(e.get("Display Level") or e.get("Significance Tier") or "").lower()
  feature=("feature" in tier or "master" in tier)
  label_x=xs+10; label_y=yy-7
  if feature:
   box_w=min(360 if HERO_SLICE else 300,max(120 if HERO_SLICE else 105,(9.0 if HERO_SLICE else 8.0)*len(nm)+18))
   svg.append(f'<rect x="{label_x-5:.1f}" y="{label_y-17:.1f}" width="{box_w:.1f}" height="22" rx="4" fill="#fbf6e9" fill-opacity=".94" stroke="#a98f68" stroke-width=".8" filter="url(#softShadow)"/>')
   # Feature anchors get a larger medallion and chronology tether. This remains neutral until a verified image asset exists.
   svg.append(f'<line x1="{xs:.1f}" y1="{yy:.1f}" x2="{xs:.1f}" y2="{yy-27:.1f}" stroke="#a98f68" stroke-width="1"/>')
   assets=verified_assets.get(e["Entity ID"],[])
   # Authentic imagery is optional. Without a renderable verified asset, typography alone is preferred.
   renderable_assets=[a for a in assets if (a.get("Image URL") or "").strip() or (a.get("Local Asset Path") or "").strip()]
   if renderable_assets:
    # Reserve a larger visual anchor in hero mode; authentic imagery remains tied to the exact date x-coordinate.
    panel_y=yy-38 if HERO_SLICE else yy-28
    svg.append(feature_panel(kind,xs,panel_y,nm,title))
   if renderable_assets:
    a=renderable_assets[0]
    source_label=esc(a.get("Source Organization","Verified source"))
    asset_label=esc(a.get("Asset Type","historical asset"))
    rights=esc(a.get("License / Rights",""))
    source_url=esc(a.get("Source URL",""))
    image_url=esc(image_href(a))
    if image_url:
     svg.append(f'<defs><clipPath id="clip-{esc(e["Entity ID"])}-{esc(c["Date Claim ID"])}"><rect x="{xs-(82 if HERO_SLICE else 55):.1f}" y="{yy-(142 if HERO_SLICE else 99):.1f}" width="{164 if HERO_SLICE else 110}" height="{100 if HERO_SLICE else 66}" rx="5"/></clipPath></defs>')
     svg.append(f'<image href="{image_url}" x="{xs-(82 if HERO_SLICE else 55):.1f}" y="{yy-(142 if HERO_SLICE else 99):.1f}" width="{164 if HERO_SLICE else 110}" height="{100 if HERO_SLICE else 66}" preserveAspectRatio="xMidYMid slice" clip-path="url(#clip-{esc(e["Entity ID"])}-{esc(c["Date Claim ID"])})"><title>{source_label} | {rights}</title></image>')
     svg.append(f'<rect x="{xs-55:.1f}" y="{yy-99:.1f}" width="110" height="66" rx="5" fill="none" stroke="#806849" stroke-width="1.2"/>')
    svg.append(f'<rect x="{xs-57:.1f}" y="{yy-92:.1f}" width="114" height="17" rx="3" fill="#e4d2ae" stroke="#806849" stroke-width=".7"/>')
    svg.append(f'<text x="{xs:.1f}" y="{yy-80:.1f}" text-anchor="middle" class="meta" font-size="9">SOURCED • {asset_label}</text>')
    svg.append(f'<a href="{source_url}" target="_blank"><title>{source_label} | {rights}</title><rect x="{xs-57:.1f}" y="{yy-100:.1f}" width="114" height="80" fill="transparent"/></a>')
   svg.append(f'<line x1="{xs:.1f}" y1="{yy-28:.1f}" x2="{xs:.1f}" y2="{yy-18:.1f}" stroke="#7d6547" stroke-width="1"/>')
   svg.append(f'<text x="{label_x:.1f}" y="{label_y:.1f}" class="item" font-size="{'18' if HERO_SLICE else '15'}">{nm}<title>{title}</title></text>')
  else:
   svg.append(f'<text x="{label_x:.1f}" y="{label_y:.1f}" class="item">{nm}<title>{title}</title></text>')

# legend
ly=height-62
svg.append(f'<text x="30" y="{ly}" class="meta">Line encoding: solid = documented/artifact or other non-special classification • 4/3 dash = traditional/religious • 2/3 = legendary/mythological • 6/2 = manuscript/text • 3/2 = approximate/disputed</text>')
svg.append(f'<text x="30" y="{height-25}" class="meta">Source: canonical data/*.csv • Generated by scripts/render_timeline_svg.py • Historical placement is data-driven, not image-generated.</text>')
svg.append('</svg>')
OUT.mkdir(exist_ok=True)
def year_token(y):
 return f"{abs(y)}BCE" if y < 0 else f"{y}CE"
p=OUT/f"timeline_v1_foundation_{year_token(START)}_{year_token(END)}.svg"
p.write_text(chr(10).join(svg),encoding="utf-8")
print(p)
print("rendered marks",sum(len(v) for v in marks.values()),"numeric textual claims skipped",skipped)
