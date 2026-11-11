#!/usr/bin/env python3
"""Verify every explicit {#anchor} in docs/zh matches what the English heading
would have produced, and vice versa: that the English site's slug set is a
subset of the Chinese page's anchor set."""
from __future__ import annotations

import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN = os.path.join(REPO, "docs", "en")
ZH = os.path.join(REPO, "docs", "zh")

H = re.compile(r"^(#{1,6})\s+(.*)$")
A = re.compile(r"\{#([^}]+)\}")


def slug(t: str) -> str:
    # A heading like "## [Installation](installation.md)" keeps the link text
    # and drops the URL: mkdocs' toc strips the target, keeping "installation".
    t = re.sub(r"\[([^\]]*)\]\([^)]+\)", r"\1", t)
    t = re.sub(r"\*\*|`|\*", "", t).strip().lower()
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"[^\w\s-]", "", t, flags=re.UNICODE)
    return re.sub(r"[\s]+", "-", t).strip("-")


def heads(text: str) -> list[tuple[int, str]]:
    out, fm = [], False
    for i, line in enumerate(text.splitlines()):
        s = line.strip()
        if s == "---":
            fm = not fm
            continue
        if fm:
            continue
        m = H.match(s)
        if m and len(m.group(1)) >= 2:
            out.append((i, m.group(2)))
    return out


def link_heading(title: str) -> bool:
    """`## [Installation](installation.md)` emits no id in mkdocs, so it needs
    no anchor; only prose headings do."""
    return bool(re.match(r"\[[^\]]*\]\([^)]+\)\s*$", title.strip()))


def main() -> int:
    bad = 0
    for dp, _dn, fn in os.walk(ZH):
        for f in sorted(fn):
            if not f.endswith(".md"):
                continue
            zh_path = os.path.join(dp, f)
            rel = os.path.relpath(zh_path, ZH)
            en_path = os.path.join(EN, rel)
            if not os.path.exists(en_path):
                continue
            zh_lines = open(zh_path, encoding="utf-8").read().splitlines()
            zh_h = heads("\n".join(zh_lines))
            en_h = heads(open(en_path, encoding="utf-8").read())
            if len(zh_h) != len(en_h):
                print(f"COUNT  {rel}: en {len(en_h)} vs zh {len(zh_h)}")
                bad += 1
                continue
            for (zi, ztitle), (_, etitle) in zip(zh_h, en_h):
                m = A.search(ztitle)
                if m:
                    want = slug(etitle)
                    if m.group(1) != want:
                        print(f"WRONG   {rel}:L{zi + 1} have #{m.group(1)} want #{want}")
                        bad += 1
                elif not link_heading(etitle):
                    print(f"MISSING {rel}:L{zi + 1} {ztitle[:44]}")
                    bad += 1
    print(f"\n{bad} anchor problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
