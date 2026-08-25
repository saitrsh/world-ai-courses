#!/usr/bin/env python3
"""Render cambridge-question-index.md into a clean, comparison-oriented web page.

The raw markdown tables read as a cramped wall of text on Pages. This emits a
responsive page: color-coded paper cards, frequency bars, and a Cambridge↔NYCU
comparison grid. Deterministic; re-run after editing the .md.
"""
import re
from pathlib import Path

MD = Path("cambridge-question-index.md")
OUT = Path("cambridge-question-index.html")

# 主題大類 keyword -> (css class, label color)
TOPIC_COLORS = [
    ("神經網路", "nn"), ("規劃", "plan"), ("CSP", "csp"),
    ("搜尋", "search"), ("ML", "ml"), ("邏輯斯", "ml"), ("迴歸", "ml"),
]


def topic_class(topic: str) -> str:
    for kw, cls in TOPIC_COLORS:
        if kw in topic:
            return cls
    return "misc"


def rows(md: str, header_startswith: str):
    """Yield cell-lists for a markdown table identified by its header row."""
    lines = md.splitlines()
    out, in_tbl = [], False
    for ln in lines:
        if ln.startswith("|") and header_startswith in ln:
            in_tbl = True
            continue
        if in_tbl:
            if not ln.startswith("|"):
                break
            if set(ln.replace("|", "").strip()) <= set("-: "):
                continue
            safe = ln.strip().strip("|").replace(r"\|", "\x00")  # protect escaped pipes
            cells = [c.strip().replace("\x00", "|") for c in safe.split("|")]
            out.append(cells)
    return out


def inline(s: str) -> str:
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    return s


def main():
    md = MD.read_text(encoding="utf-8")

    # --- per-paper cards ---
    papers = rows(md, "檔案")
    cards = []
    for file, ys, topic, subs, form in papers:
        cls = topic_class(topic)
        subs_html = " ".join(
            f"<span class='sub'>{inline(x.strip())}</span>"
            for x in subs.split("·") if x.strip())
        cards.append(f"""<div class="card {cls}">
  <div class="card-h"><span class="yr">{inline(ys)}</span><span class="tag {cls}">{inline(topic)}</span></div>
  <div class="subs">{subs_html}</div>
  <div class="form">{inline(form)}</div>
</div>""")

    # --- frequency bars ---
    freq = rows(md, "出現份數")
    bars = []
    for topic, n, pct, _rep in freq:
        p = int(re.search(r"\d+", pct).group())
        cls = topic_class(topic)
        bars.append(f"""<div class="bar-row">
  <div class="bar-label">{inline(topic)}</div>
  <div class="bar-track"><div class="bar-fill {cls}" style="width:{p}%"></div></div>
  <div class="bar-val">{inline(n)} 份 · {pct}</div>
</div>""")

    # --- Cambridge ↔ NYCU comparison ---
    comp = rows(md, "是否落在")
    comp_rows = []
    for axis, hit, value in comp:
        hitcls = "yes" if "✅" in hit else "warn" if "⚠️" in hit else ""
        comp_rows.append(
            f"<tr><td>{inline(axis)}</td><td class='{hitcls}'>{inline(hit)}</td><td>{inline(value)}</td></tr>")

    # --- axes + one-liner (pull the prose blocks) ---
    axes_html = ""
    if "### 三條穩定命題主軸" in md:
        block = md.split("### 三條穩定命題主軸", 1)[1].split("\n## ", 1)[0]
        for m in re.finditer(r"^\d+\.\s+(.*)$", block, re.M):
            axes_html += f"<li>{inline(m.group(1))}</li>"
    oneliner = re.search(r"\*\*一句話:\*\*\s*(.*)", md)
    one_html = inline(oneliner.group(1)) if oneliner else ""

    html = TEMPLATE.format(
        cards="\n".join(cards), bars="\n".join(bars),
        comp="\n".join(comp_rows), axes=axes_html, oneliner=one_html)
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT} ({len(html)} bytes; {len(papers)} papers, {len(freq)} topics)")


TEMPLATE = """<!doctype html><html lang="zh-Hant"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Cambridge AI 真卷 · 題型對照</title>
<style>
:root{{--bg:#fbfaff;--fg:#1a1a2e;--mut:#5f5f78;--line:#e6e4f2;--acc:#6b46c1;--card:#fff}}
@media(prefers-color-scheme:dark){{:root{{--bg:#13131e;--fg:#e9e9f4;--mut:#a2a2ba;--line:#2a2a3d;--acc:#b794f6;--card:#1b1b29}}}}
.nn{{--c:#8b5cf6}}.plan{{--c:#3b82f6}}.csp{{--c:#10b981}}.search{{--c:#f59e0b}}.ml{{--c:#ec4899}}.misc{{--c:#64748b}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,"Segoe UI",Roboto,"Noto Sans TC",sans-serif}}
.wrap{{max-width:1100px;margin:0 auto;padding:28px 18px 72px}}
a{{color:var(--acc)}}.back{{display:inline-block;margin-bottom:14px;font-weight:600;text-decoration:none}}
h1{{font-size:1.6rem;margin:.1em 0 .3em;color:var(--acc)}}
h2{{font-size:1.25rem;margin:2em 0 .7em;padding-bottom:.3em;border-bottom:2px solid var(--line)}}
.lead{{color:var(--mut);font-size:.95rem;background:var(--card);border:1px solid var(--line);border-left:4px solid var(--acc);border-radius:8px;padding:12px 16px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}}
.card{{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--c);border-radius:10px;padding:14px 16px}}
.card-h{{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:8px}}
.yr{{font-weight:700;font-size:.95rem}}
.tag{{font-size:.72rem;font-weight:700;color:#fff;background:var(--c);padding:3px 9px;border-radius:20px;white-space:nowrap}}
.subs{{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:10px}}
.sub{{font-size:.78rem;background:color-mix(in srgb,var(--c) 12%,transparent);color:var(--fg);padding:3px 8px;border-radius:6px}}
.form{{font-size:.75rem;color:var(--mut);font-style:italic}}
.bar-row{{display:grid;grid-template-columns:170px 1fr 130px;align-items:center;gap:12px;margin:9px 0;font-size:.88rem}}
.bar-track{{background:var(--line);border-radius:20px;height:14px;overflow:hidden}}
.bar-fill{{height:100%;background:var(--c);border-radius:20px}}
.bar-val{{color:var(--mut);font-size:.82rem}}
table{{border-collapse:collapse;width:100%;margin:.5em 0;font-size:.9rem}}
th,td{{border:1px solid var(--line);padding:9px 12px;text-align:left;vertical-align:top}}
th{{background:color-mix(in srgb,var(--acc) 12%,transparent);font-weight:700}}
td.yes{{color:#10b981;font-weight:700}}td.warn{{color:#f59e0b;font-weight:700}}
ol{{padding-left:1.2em}}ol li{{margin:.5em 0}}
.one{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 18px;font-size:.95rem}}
code{{background:color-mix(in srgb,var(--acc) 10%,transparent);padding:.1em .4em;border-radius:4px;font-size:.86em}}
.legend{{display:flex;flex-wrap:wrap;gap:10px;margin:10px 0 4px;font-size:.8rem}}
.legend span{{display:inline-flex;align-items:center;gap:5px}}
.dot{{width:11px;height:11px;border-radius:50%;display:inline-block}}
@media(max-width:560px){{.bar-row{{grid-template-columns:1fr;gap:3px}}.bar-val{{text-align:right}}}}
</style></head><body><div class="wrap">
<a class="back" href="index.html">← 回課程總表</a>
<h1>Cambridge AI (Tripos Part IB) 真卷 · 題型對照</h1>
<p class="lead">21 份 past papers 逐份分類 · 出題者 <b>Sean Holden (sbh11)</b> 近十年題風高度一致、可預測 · 來源 <a href="https://www.cl.cam.ac.uk/teaching/exams/pastpapers/t-ArtificialIntelligence.html">Cambridge CST past papers</a>(1993 起全公開)</p>
<div class="legend">
<span><i class="dot" style="background:#8b5cf6"></i>神經網路</span>
<span><i class="dot" style="background:#3b82f6"></i>規劃</span>
<span><i class="dot" style="background:#10b981"></i>CSP</span>
<span><i class="dot" style="background:#f59e0b"></i>搜尋</span>
<span><i class="dot" style="background:#ec4899"></i>ML</span></div>
<h2>逐份索引（21 份）</h2>
<div class="grid">
{cards}
</div>
<h2>題型頻率統計</h2>
{bars}
<p class="lead" style="border-left-color:var(--mut)">一份卷常橫跨 2 大類（規劃常接 CSP、搜尋常接 ML），故佔比加總 &gt;100%。</p>
<h2>三條穩定命題主軸（近十年 sbh11）</h2>
<ol>{axes}</ol>
<h2>對 NYCU 資格考 AI 卷的對照</h2>
<table><thead><tr><th>Cambridge 主軸</th><th>落在 NYCU 範圍？</th><th>練這批的價值</th></tr></thead>
<tbody>{comp}</tbody></table>
<h2>一句話</h2>
<p class="one">{oneliner}</p>
<p style="color:var(--mut);font-size:.8rem;margin-top:2em">生成 2026-08-25 · 資料來源公開（Cambridge CST past papers）· 僅供個人備考</p>
</div></body></html>"""


if __name__ == "__main__":
    main()
