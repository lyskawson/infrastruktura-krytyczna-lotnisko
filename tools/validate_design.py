#!/usr/bin/env python3
"""Check quantitative consistency, not engineering compliance."""
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/"data/design.json").read_text())
nodes=d["nodes"]
expected={"fixed":20,"ptz":4,"doors":12,"gates":2,"kd_controllers":8,"pir":24,"contacts":16,"fire_detectors":80,"rop":12,"fire_sounders":12,"ups_load_w":1335}
for field,value in expected.items():
    actual=sum(n[field] for n in nodes)
    if actual!=value: raise SystemExit(f"{field}: {actual}, expected {value}")
for n in nodes:
    if 2*n["kd_controllers"]<n["doors"]+n["gates"]: raise SystemExit("KD capacity: "+n["id"])
    if n["pir"]+n["contacts"]+2>32: raise SystemExit("SSWiN capacity: "+n["id"])
    watts=n["fixed"]*12+n["ptz"]*30
    if 1.25*watts>240: raise SystemExit("PoE budget: "+n["id"])
    # Cameras + controllers + SSWiN + local link; core has separate server ports.
    if n["fixed"]+n["ptz"]+n["kd_controllers"]+2>24: raise SystemExit("Port budget: "+n["id"])
route_sum=0
for r in d["routes"]:
    length=sum(math.dist(a,b) for a,b in zip(r["points"],r["points"][1:]))
    if not math.isclose(length,r["length_m"]): raise SystemExit("Route geometry: "+r["id"])
    route_sum+=length
if route_sum!=1520: raise SystemExit("Main route total differs from PDF")
video=d["video"]
count=expected["fixed"]+expected["ptz"]
recording_tb=count*video["bitrate_mbps"]*1e6/8*video["retention_days"]*86400/1e12
available_tb=(video["disks"]-video["raid_parity_disks"])*video["disk_tb"]*.9
if available_tb<recording_tb*1.25: raise SystemExit("Insufficient disk capacity")
power=sum(d["power_w"].values())
if power!=expected["ups_load_w"]: raise SystemExit("Power distribution mismatch")
for name in ("architecture","site-plan","routes","terminal","ai-flow","power"):
    if not (ROOT/f"figures/{name}.pdf").is_file(): raise SystemExit("Missing figure: "+name)
report=f"""Weryfikacja danych: OK (nie potwierdza zgodności wykonawczej).
Kamery: {count}; czytniki: {expected['doors']+2*expected['gates']}; kanały KD: {2*expected['kd_controllers']}.
Trasa: {route_sum:.0f} m; kabel z 10%: {route_sum*1.1:.0f} m.
Wideo: {recording_tb:.4f} TB; z 25%: {recording_tb*1.25:.4f} TB; dostępne: {available_tb:.1f} TB.
Moc: {power} W; bateria UPS: {power/1000*.5/.9*1.25:.3f} kWh.
"""
print(report)
