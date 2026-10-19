#!/usr/bin/env python3
"""Package only sources/assets required by Overleaf; no local paths or Git."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root=Path(__file__).resolve().parents[1]
dest=root/"output/lotnisko-overleaf.zip"
dest.parent.mkdir(exist_ok=True)
files=[root/n for n in ("main.tex","preamble.tex","metadata.tex")]
for directory in ("sections","figures","images"):
    files.extend(p for p in (root/directory).rglob("*") if p.is_file())
with ZipFile(dest,"w",compression=ZIP_DEFLATED) as z:
    for f in sorted(files):
        z.write(f,f.relative_to(root).as_posix())
    z.writestr("INSTRUKCJA.txt","Overleaf: main.tex, kompilator pdfLaTeX. Edytuj metadata.tex i sections/. Rysunki PDF są gotowe; generator nie jest potrzebny do kompilacji.\n")
print(dest)
