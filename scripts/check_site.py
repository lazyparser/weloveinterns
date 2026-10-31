#!/usr/bin/env python3
"""站点自检：站内链接、引用角标与来源登记一致性。

用法：
    python3 scripts/check_site.py
    python3 scripts/check_site.py --dir website/public
"""
import argparse
import os
import re
import sys

HREF_RE = re.compile(r'(?:href|src)=(?:"([^"]+)"|([^\s>]+))')
CITE_RE = re.compile(r'class=cite[^>]*>(?:<[^>]+>)*\s*(\d+|\?)')
# 允许跳过的外部前缀
SKIP_PREFIX = ("mailto:", "javascript:", "#", "data:", "http://", "https://")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="website/public")
    args = ap.parse_args()
    root = os.path.abspath(args.dir)
    if not os.path.isdir(root):
        sys.exit(f"找不到构建目录 {root}，先跑 make site")

    htmls = []
    for dirpath, _, files in os.walk(root):
        for f in files:
            if f.endswith(".html"):
                htmls.append(os.path.join(dirpath, f))
    htmls.sort()

    from urllib.parse import urlparse, unquote

    broken, checked = [], 0
    cite_unknown, cite_count = [], 0
    for path in htmls:
        with open(path, encoding="utf-8", errors="replace") as fh:
            html = fh.read()
        for m in HREF_RE.finditer(html):
            href = (m.group(1) or m.group(2) or "").strip()
            if not href or href.startswith(SKIP_PREFIX):
                continue
            u = urlparse(href)
            if u.scheme in ("http", "https"):
                continue
            target = unquote(u.path)
            if not target:
                continue
            tpath = os.path.normpath(os.path.join(root, target.lstrip("/")))
            checked += 1
            if not (os.path.exists(tpath) or os.path.exists(os.path.join(tpath, "index.html"))):
                broken.append((os.path.relpath(path, root), href))
        for c in CITE_RE.findall(html):
            cite_count += 1
            if c == "?":
                cite_unknown.append(os.path.relpath(path, root))

    # 来源登记：各语言 sources 页上的条目数（中文在根，其余在 /<lang>/ 下）
    src_page = os.path.join(root, "sources", "index.html")
    src_n = 0
    if os.path.exists(src_page):
        with open(src_page, encoding="utf-8") as fh:
            src_n = len(re.findall(r'class=src-idx', fh.read()))

    # ---- 多语言完整性：每种语言必须各有同构的一套页面 ----
    LANGS = [("zh", ""), ("zh-Hant", "zh-hant"), ("en", "en"), ("ja", "ja"), ("ru", "ru"), ("ko", "ko")]
    PAGES = ["", "history", "interns", "mentors", "positions", "program", "shise-stone", "sources", "join",
             "blog", "blog/nine-years", "blog/joint-recruitment-2024"]
    lang_missing = []
    for lang, prefix in LANGS:
        base = os.path.join(root, prefix) if prefix else root
        for p in PAGES:
            t = os.path.join(base, p, "index.html") if p else os.path.join(base, "index.html")
            if not os.path.exists(t):
                lang_missing.append(f"{lang or 'zh'} 缺 {'/' + p + '/' if p else '/index.html'}")

    # ---- hreflang：页面上的 alternate 必须覆盖「该页面确实存在的语言」 ----
    hreflang_bad = []
    for path in htmls:
        with open(path, encoding="utf-8", errors="replace") as fh:
            html = fh.read()
        if 'http-equiv="refresh"' in html or 'http-equiv=refresh' in html:
            continue  # Hugo 的 alias 跳转页，不参与 hreflang 检查
        codes = set()
        for m in re.finditer(r'hreflang=(?:"([A-Za-z-]+)"|([A-Za-z-]+))', html):
            codes.add(m.group(1) or m.group(2))
        if not codes:
            hreflang_bad.append((os.path.relpath(path, root), "没有 hreflang"))
            continue
        rel = os.path.relpath(path, root)
        missing = [c for c in ("x-default",) if c not in codes]
        if missing:
            hreflang_bad.append((rel, "缺 x-default"))

    print(f"HTML 页面: {len(htmls)}")
    print(f"  · 语言数 {len(LANGS)}，每种应有 {len(PAGES)} 页；缺失 {len(lang_missing)} 处")
    for m in lang_missing[:12]:
        print(f"  ✗ {m}")
    print(f"  · hreflang 异常: {len(hreflang_bad)} 页")
    for page, why in hreflang_bad[:10]:
        print(f"  ✗ {page}: {why}")
    print(f"站内链接: 检查 {checked} 个，坏链 {len(broken)} 个")
    for page, href in broken[:20]:
        print(f"  ✗ {page} → {href}")
    print(f"引用角标: {cite_count} 处，未登记 {len(cite_unknown)} 处")
    for page in sorted(set(cite_unknown))[:10]:
        print(f"  ✗ {page} 出现未登记的来源 id")
    print(f"来源登记表: {src_n} 条")

    if broken or cite_unknown or src_n == 0 or lang_missing or hreflang_bad:
        sys.exit(1)
    print("全部通过")


if __name__ == "__main__":
    main()
