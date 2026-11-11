#!/usr/bin/env python3
"""List media files in docs/zh that no Chinese page references."""
from __future__ import annotations

import os
import re

ZH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "zh")
MEDIA = (".mp4", ".webm", ".mov")
SRC = re.compile(r'(?:src|href)="([^"]+)"')

text = "\n".join(
    open(os.path.join(dp, f), encoding="utf-8", errors="replace").read()
    for dp, _dn, fn in os.walk(ZH)
    for f in fn
    if f.endswith(".md")
)

rows = []
for dp, _dn, fn in os.walk(ZH):
    for f in fn:
        if not f.endswith(MEDIA):
            continue
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, ZH)
        if os.path.basename(rel) not in text:
            rows.append((os.path.getsize(p), rel))

for size, rel in sorted(rows, reverse=True):
    print(f"{size/1e6:7.2f} MB  UNUSED  {rel}")
print(f"\n{len(rows)} unreferenced media file(s), {sum(r[0] for r in rows)/1e6:.2f} MB")
