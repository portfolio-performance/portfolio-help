#!/usr/bin/env python3
"""Find captions that mkdocs-caption will reject.

`mkdocs-caption` builds an XML-ish string from the caption text and runs it
through an XML parser. Inline code (`` `x` ``) becomes a <code> element, which
the parser rejects as invalid XML, and the caption then does not render AT ALL
with no build error. This scans docs/zh for that and for any other construct
the parser would choke on, then confirms against the built HTML.
"""
from __future__ import annotations

import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH = os.path.join(REPO, "docs", "zh")
SITE = os.path.join(REPO, "site", "zh")

CAPTION = re.compile(r"^图：\s*(.+)$", re.M)
FIGCAP = re.compile(r"<figcaption[^>]*>(.*?)</figcaption>", re.S)
CODE = re.compile(r"`[^`]+`")


def main() -> int:
    bad = 0
    total = 0
    for dp, _dn, fn in os.walk(ZH):
        for f in sorted(fn):
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, ZH)
            text = open(p, encoding="utf-8").read()
            for i, line in enumerate(text.splitlines(), 1):
                m = CAPTION.match(line.strip())
                if not m:
                    continue
                total += 1
                cap = m.group(1)
                # Inline code becomes a <code> element, which the plugin's XML
                # parse rejects -> caption silently does not render. Valid HTML
                # (<a href=...>) and bare "&" (S&P) are fine, so only code spans
                # are a defect here.
                if CODE.search(cap):
                    print(f"BACKTICK  {rel}:L{i} {cap[:60]!r}")
                    bad += 1

    print(f"\n{total} caption(s) scanned, {bad} at risk of failing to render")

    # Confirm: does the built HTML actually contain a figcaption per caption?
    if os.path.isdir(SITE):
        n_pages = n_caps = 0
        missing = []
        for dp, _dn, fn in os.walk(SITE):
            for f in fn:
                if not f.endswith(".html"):
                    continue
                html_path = os.path.join(dp, f)
                html = open(html_path, encoding="utf-8", errors="replace").read()
                # docs/zh/a/b.md builds to site/zh/a/b/index.html
                rel_html = os.path.relpath(dp, SITE)
                src = (
                    os.path.join(ZH, "index.md")
                    if rel_html == "."
                    else os.path.join(ZH, rel_html + ".md")
                )
                if os.path.exists(src):
                    n_pages += 1
                    want = len(CAPTION.findall(open(src, encoding="utf-8").read()))
                    got = len(FIGCAP.findall(html))
                    n_caps += got
                    if got < want:
                        missing.append(
                            f"{os.path.relpath(html_path, SITE)}: "
                            f"{want} caption(s) in md, {got} rendered"
                        )
        for m in missing:
            print("NOT-RENDERED", m)
        print(f"{n_caps} figcaption(s) rendered across {n_pages} page(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
