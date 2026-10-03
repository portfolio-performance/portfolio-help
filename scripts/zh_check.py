#!/usr/bin/env python3
"""Structural comparison of docs/zh against docs/en.

Translation must not change page *structure*: same images, same links,
same math, same code fences, same admonitions. Only prose changes.
This checker enforces that mechanically.
"""
from __future__ import annotations

import os
import re
import sys
from collections import defaultdict

import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN = os.path.join(REPO, "docs", "en")
ZH = os.path.join(REPO, "docs", "zh")

IMG = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
LNK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SRC = re.compile(r'(?:src|href)="([^"]+)"')
H = re.compile(r"^(#{1,6})\s+(.*)$")
ANCHOR = re.compile(r"\{#([^}]+)\}")

problems: dict[str, list[str]] = defaultdict(list)


def rel_files(base: str) -> list[str]:
    out = []
    for dp, _dn, fn in os.walk(base):
        for f in sorted(fn):
            if f.endswith(".md"):
                out.append(os.path.relpath(os.path.join(dp, f), base))
    return sorted(out)


def read(base: str, rel: str) -> str:
    return open(os.path.join(base, rel), encoding="utf-8").read()


def anchors_of(base: str) -> dict[str, set[str]]:
    idx = {}
    for rel in rel_files(base):
        s = set()
        in_fm = False
        for line in read(base, rel).splitlines():
            t = line.strip()
            if t == "---":
                in_fm = not in_fm
                continue
            if in_fm:
                continue
            m = H.match(line)
            if m:
                explicit = ANCHOR.search(m.group(2))
                if explicit:
                    s.add(explicit.group(1))
                else:
                    txt = re.sub(r"\*\*|`|\*|<[^>]+>", "", m.group(2)).strip().lower()
                    txt = re.sub(r"[^\w\s-]", "", txt, flags=re.UNICODE)
                    s.add(re.sub(r"[\s]+", "-", txt))
        idx[rel] = s
    return idx


EN_IDX = anchors_of(EN)
ZH_IDX = anchors_of(ZH)


def check(rel: str) -> None:
    en, zh = read(EN, rel), read(ZH, rel)
    p = problems[rel]

    # front matter title required
    if not zh.lstrip().startswith("---"):
        p.append("missing front matter")
    else:
        fm = zh.split("---", 2)[1]
        if not re.search(r"^title:", fm, re.M):
            p.append("front matter has no title:")

    for tag, pat in (("image", IMG), ("link", LNK), ("src/href", SRC)):
        e = sorted(x.strip() for x in pat.findall(en) if not x.strip().startswith("http"))
        z = sorted(x.strip() for x in pat.findall(zh) if not x.strip().startswith("http"))
        if tag == "image" and e != z:
            miss = set(e) - set(z)
            extra = set(z) - set(e)
            if miss:
                p.append(f"images dropped: {sorted(miss)[:4]}")
            if extra:
                p.append(f"images added: {sorted(extra)[:4]}")
        if tag in ("link", "src/href"):
            # A translation may fold an English gloss into the link text, e.g.
            # "类别（[taxonomies](page.md)）" for "the taxonomies ([page.md])".
            # Compare only the targets, never the link text.
            e_targets = sorted(x.strip().split("#")[0] for x in pat.findall(en) if not x.strip().startswith("http"))
            z_targets = sorted(x.strip().split("#")[0] for x in pat.findall(zh) if not x.strip().startswith("http"))
            if e_targets != z_targets:
                miss = sorted(set(e_targets) - set(z_targets))
                extra = sorted(set(z_targets) - set(e_targets))
                if miss:
                    p.append(f"{tag} targets dropped: {miss[:4]}")
                if extra:
                    p.append(f"{tag} targets added: {extra[:4]}")

    # code fences and math must survive verbatim
    for label, tok in (("code fence", "```"), ("math block", "$$")):
        if en.count(tok) != zh.count(tok):
            p.append(f"{label} count {en.count(tok)} -> {zh.count(tok)}")

    # admonitions
    ea = len(re.findall(r"^!!!", en, re.M))
    za = len(re.findall(r"^!!!", zh, re.M))
    if ea != za:
        p.append(f"admonition count {ea} -> {za}")

    # figure captions must use the Chinese identifier WITH a trailing space
    n_en = len(re.findall(r"(?m)^Figure:", en))
    n_zh = len(re.findall(r"(?m)^图：\s", zh))
    n_zh_bad = len(re.findall(r"(?m)^图：\S", zh))
    if n_en != n_zh:
        p.append(f"figure caption count {n_en} -> {n_zh}")
    if n_zh_bad:
        p.append(f"{n_zh_bad} caption(s) missing the space after 图： (will not render)")
    if re.search(r"(?m)^Figure:", zh):
        p.append("still uses English 'Figure:' caption identifier")

    # every ##+ heading must carry an explicit english anchor
    missing_anchor = [
        m.group(2)
        for m in (H.match(line) for line in zh.splitlines())
        if m and len(m.group(1)) >= 2 and not ANCHOR.search(m.group(2))
    ]
    for t in missing_anchor:
        p.append(f"heading without {{#anchor}}: {t[:44]}")

    # encoding integrity: no U+FFFD, and no private-use chars except the Apple
    # logo (U+F8FF), which the English source also carries verbatim.
    for i, ch in enumerate(zh):
        if ch == "�":
            p.append(f"U+FFFD replacement char at offset {i}")
            break
        if 0xE000 <= ord(ch) <= 0xF8FF and ord(ch) != 0xF8FF:
            p.append(f"private-use char U+{ord(ch):04X} at offset {i}")
            break

    # untranslated English sentences left behind (heuristic: long runs of ASCII)
    for para in re.findall(r"(?m)^[^\n`*|!\[][^\n]{120,}$", zh):
        letters = len(re.findall(r"[A-Za-z]", para))
        if letters / len(para) > 0.85 and " " in para:
            p.append(f"possible untranslated paragraph: {para[:60]!r}")
            break

    # every local link must resolve inside docs/zh
    d = os.path.dirname(os.path.join(ZH, rel))
    for m in LNK.findall(zh) + SRC.findall(zh):
        t = m.strip()
        if t.startswith(("http", "#", "mailto")):
            continue
        path, _, frag = t.partition("#")
        ap = os.path.normpath(os.path.join(d, path))
        if not os.path.exists(ap):
            p.append(f"broken target: {t}")
            continue
        if frag and path.endswith(".md"):
            tr = os.path.relpath(ap, ZH)
            if tr in ZH_IDX and frag not in ZH_IDX[tr]:
                p.append(f"dead anchor: {t}")

    # image files must exist
    for m in IMG.findall(zh):
        t = m.strip()
        if t.startswith(("http", "#")):
            continue
        ap = os.path.normpath(os.path.join(d, t.split("#")[0]))
        if not os.path.exists(ap):
            p.append(f"missing image: {t}")

    # A CJK character immediately after a closing quote makes PyYAML reject the
    # whole front matter block, and MkDocs then renders the raw YAML as body text
    # (the `---` fences become horizontal rules) with no build error. Parse the
    # metadata instead of trusting it to be well-formed.
    if zh.startswith("---"):
        parts = zh.split("---", 2)
        if len(parts) < 3:
            p.append("front matter is not closed by a second ---")
        else:
            try:
                meta = yaml.safe_load(parts[1])
            except yaml.YAMLError as exc:
                first = str(exc).splitlines()[0]
                p.append(f"UNPARSEABLE front matter (renders as body text): {first}")
            else:
                if not isinstance(meta, dict):
                    p.append("front matter is not a mapping")
                else:
                    for key in ("title", "description"):
                        if key in meta and not str(meta[key]).strip():
                            p.append(f"empty metadata field: {key}")


def main() -> int:
    en_files = [f for f in rel_files(EN) if not f.startswith("_")]
    for rel in en_files:
        if not os.path.exists(os.path.join(ZH, rel)):
            problems[rel].append("FILE NOT TRANSLATED")
            continue
        check(rel)
    extra = [f for f in rel_files(ZH) if f not in en_files and not f.startswith("_")]
    for rel in extra:
        problems[rel].append(f"EXTRA FILE not in en ({rel})")

    n = len([rel for rel, msgs in problems.items() if msgs])
    for rel in sorted(problems):
        for msg in problems[rel]:
            print(f"[{rel}] {msg}")
    print(f"\n{n} file(s) with problems out of {len(en_files)}")
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main())