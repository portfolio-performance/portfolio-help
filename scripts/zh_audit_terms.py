#!/usr/bin/env python3
"""Audit docs/zh terminology against the agreed termbase.

Substring matching is unsafe for CJK: 行情 occurs inside 执行情况 ("status"),
and "Performance" occurs inside the product name Portfolio Performance.
Every rule below therefore carries the surrounding context that makes it an
actual error rather than a coincidental substring.
"""
from __future__ import annotations

import os
import re
import sys
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH = os.path.join(REPO, "docs", "zh")

# (label, regex) — each must be an unambiguous error in context.
FORBIDDEN = [
    ("transaction rendered as 交易", r"交易类型|交易菜单"),
    ("FIFO as 先入先出", r"先入先出"),
    # 行情 is legitimate in 上涨行情/下跌行情 (bull/bear market); only flag when
    # it stands in for the PP "quote" concept.
    ("quote as 行情", r"(?<![执行市上天下])行情(?=[，。、；：的与和或])"),
    ("dividend as 红利", r"红利"),
    ("delivery as 交割", r"交割"),
    ("deposit account as 存款账户", r"存款账户"),
    ("money-weighted as 金额加权", r"金额加权"),
    ("interest charge as 利息费用", r"利息费用"),
]

# English UI labels that must not remain untranslated inside backticks.
UI_PAIRS = [
    ("Reporting Period", "报告期"),
    ("Purchase Value", "成本"),
    ("Purchase Price", "买价"),
    ("All Securities", "全部证券"),
    ("Reference Account", "关联账户"),
    ("Securities Account", "证券账户"),
    ("Statement of Assets", "资产明细"),
    ("Market Value", "市值"),
    ("Interest charge", "利息支出"),
    ("Withdrawal", "取款"),
]
# Product name, Windows paths, URLs and file names are deliberately untranslated.
# CSV column names are literal identifiers the user types into their file, so they
# must stay English too (csv-import.md documents them inside backticks).
EXEMPT = re.compile(
    r"Portfolio\s+Performance|[A-Za-z]:\\|\.xml|\.csv|\.json|\.pdf|https?://|\.portfolio"
    r"|^\(?\s*(Deposit|Withdrawal|Dividend|Interest|Interest Charge|Fees"
    r"|Fees Refund|Taxes|Tax Refund|Transfer|Securities? Account|Cash Account"
    r"|Securities Account|Reference Account|Portfolio|Security|Account"
    r"|Shares|Quote|Value|Amount|Date|Currency|Notes?)\b"
)


def walk() -> list[str]:
    out = []
    for dp, _dn, fn in os.walk(ZH):
        for f in sorted(fn):
            if f.endswith(".md"):
                out.append(os.path.join(dp, f))
    return out


def main() -> int:
    issues: dict[str, list[str]] = defaultdict(list)
    pages = cjk = ascii_words = 0

    for p in walk():
        rel = os.path.relpath(p, ZH)
        text = open(p, encoding="utf-8").read()
        pages += 1
        cjk += len(re.findall(r"[\u4e00-\u9fff]", text))
        ascii_words += len(re.findall(r"\b[A-Za-z]{3,}\b", text))

        for label, pat in FORBIDDEN:
            for m in re.finditer(pat, text):
                line = text.count("\n", 0, m.start()) + 1
                issues[rel].append(f"L{line} {label}: {m.group(0)!r}")

        for m in re.finditer(r"`([^`\n]+)`", text):
            inner = m.group(1)
            if EXEMPT.search(inner):
                continue
            if re.search(r"[\u4e00-\u9fff]", inner):
                continue  # already Chinese
            for en, zh in UI_PAIRS:
                if re.search(rf"\b{re.escape(en)}\b", inner):
                    line = text.count("\n", 0, m.start()) + 1
                    issues[rel].append(
                        f"L{line} UI label left in English, expected {zh!r}: {inner[:44]!r}"
                    )

    for rel in sorted(issues):
        for msg in issues[rel]:
            print(f"[{rel}] {msg}")

    print("\n--- coverage ---")
    print(f"pages           : {pages}")
    print(f"CJK characters  : {cjk:,}")
    print(f"ASCII words     : {ascii_words:,}")
    print(f"ASCII/CJK ratio : {ascii_words / max(cjk, 1):.3f}")
    print(f"\n{len(issues)} file(s) with terminology issues")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
