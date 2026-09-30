#!/usr/bin/env python3
"""Verify every internal href in the built Chinese site resolves to a real file.

linkchecker does not recurse the way CI needs here, so this walks site/zh
directly: every relative href/src must point at a file that exists, and every
`#fragment` must exist as an id in the target document.
"""
from __future__ import annotations

import os
import re
import sys
from urllib.parse import unquote

SITE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site", "zh")

HREF = re.compile(r'(?:href|src)="([^"]+)"')
ID = re.compile(r'id="([^"]+)"')


def main() -> int:
    if not os.path.isdir(SITE):
        print("site/zh not built")
        return 1
    ids: dict[str, set[str]] = {}
    for dp, _dn, fn in os.walk(SITE):
        for f in fn:
            if f.endswith(".html"):
                p = os.path.join(dp, f)
                ids[p] = set(ID.findall(open(p, encoding="utf-8", errors="replace").read()))

    checked = broken = frag_broken = root_link = 0
    for dp, _dn, fn in os.walk(SITE):
        for f in fn:
            if not f.endswith(".html"):
                continue
            page = os.path.join(dp, f)
            for raw in HREF.findall(open(page, encoding="utf-8", errors="replace").read()):
                if raw.startswith(("http://", "https://", "mailto:", "data:")):
                    continue
                target, _, frag = raw.partition("#")
                if not target:
                    if frag and frag not in ids.get(page, ()):
                        frag_broken += 1
                        print(f"FRAGMENT  {os.path.relpath(page, SITE)} -> #{frag}")
                    continue
                if target.startswith("/"):
                    # Site-root links (/en/, /de/, /zh/, /search/) only resolve
                    # after deployment; check against the deployed root instead.
                    root_link += 1
                    continue
                ap = os.path.normpath(os.path.join(dp, unquote(target)))
                if target.endswith("/"):
                    ap = os.path.join(ap, "index.html")
                checked += 1
                if not os.path.exists(ap):
                    broken += 1
                    print(f"MISSING   {os.path.relpath(page, SITE)} -> {raw}")
                elif frag and ap in ids and frag not in ids[ap]:
                    frag_broken += 1
                    print(f"ANCHOR    {os.path.relpath(page, SITE)} -> {raw}")

    print(
        f"\n{checked} internal links checked, {broken} missing targets, "
        f"{frag_broken} bad fragments ({root_link} site-root links skipped)"
    )
    return 1 if (broken or frag_broken) else 0


if __name__ == "__main__":
    sys.exit(main())
