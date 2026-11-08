#!/usr/bin/env python3
"""把单文件《哈士喵勇闯魔法禁书目录 v0.38》构建为 B站 Toy 上架包。

平台硬规则：入口 index.html 解压后 <= 1MB，资源必须相对路径。
本作与《杯雪》的结构不同，构建策略也不同：

  * 226 个 data:image/webp;base64 全在 <script> 的 ART 对象里 → 解码成真实
    图片文件，按内容 SHA1 去重，引用改为 ./assets/<hash>.webp。
  * 唯一的 <script>（8.08MB）外置为 ./app1.js。
  * **<style> 保持内联**：它含 44 处 url(#runes) / url(#glow) 等 SVG fragment
    引用，外置成 CSS 后这些引用会相对 CSS 文件解析而失效，导致滤镜/渐变丢失。
    内联 104KB 远低于 1MB 上限，保留最稳妥。

只写 toy/ 产物，源文件与历史版本一个字不改。
用法： python build_toy.py
"""
import base64
import hashlib
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "最新版_v0.38" / "哈士喵勇闯魔法禁书目录_v0.38.html"
OUT = ROOT / "toy"
ASSETS = OUT / "assets"

if not SRC.exists():
    raise SystemExit("找不到主游戏文件：%s" % SRC)

s = SRC.read_text(encoding="utf-8")
print("源文件：%s / %d B" % (SRC.name, SRC.stat().st_size))

if OUT.exists():
    shutil.rmtree(OUT)
ASSETS.mkdir(parents=True)

# ---------- 1. base64 图片外置 ----------
written = {}
seen = {}


def img_repl(m):
    b64 = m.group(1)
    key = hashlib.sha1(b64.encode("ascii")).hexdigest()[:16]
    if key not in written:
        fn = key + ".webp"
        (ASSETS / fn).write_bytes(base64.b64decode(b64))
        written[key] = fn
    seen[key] = seen.get(key, 0) + 1
    return "./assets/" + written[key]


PAT = re.compile(r"data:image/webp;base64,([A-Za-z0-9+/=]+)")
s, n = PAT.subn(img_repl, s)
print("外置图片：%d 处引用 / %d 个唯一文件" % (n, len(written)))
if n < 200:
    raise SystemExit("图片外置数量异常，构建中止")

# ---------- 2. 主脚本外置（style 保持内联，理由见文件头） ----------
script_no = [0]


def script_repl(m):
    # 只处理无 src 属性的内联脚本
    script_no[0] += 1
    fn = "app%d.js" % script_no[0]
    (OUT / fn).write_text(m.group(2), encoding="utf-8")
    return '<script src="./%s"></script>' % fn


s, nj = re.subn(
    r"<script(?![^>]*\ssrc=)([^>]*)>(.*?)</script>", script_repl, s, flags=re.S | re.I
)
print("外置脚本块：%d" % nj)
if nj != 1:
    raise SystemExit("预期 1 个内联脚本，实得 %d 个，构建中止" % nj)

# ---------- 3. 写入口 ----------
(OUT / "index.html").write_text(s, encoding="utf-8")
size = (OUT / "index.html").stat().st_size
print("入口 index.html：%d B（上限 1,048,576 B）" % size)
if size > 1048576:
    raise SystemExit("入口超过 1MB，构建中止")

# ---------- 4. 自检 ----------
bad_abs = re.findall(r'(?:src|href)\s*=\s*["\']/(?!/)', s)
bad_url = re.findall(r"url\(\s*[\"']?/", s)
leftover = len(PAT.findall(s))
ext_links = len(re.findall(r"https?://", s))
svg_frag = len(re.findall(r"url\(#", s))
print("根绝对路径 src/href: %d / url(/): %d / 残留 base64: %d / 外链: %d / SVG fragment 引用: %d"
      % (len(bad_abs), len(bad_url), leftover, ext_links, svg_frag))
for f in sorted(OUT.rglob("*")):
    if f.is_file() and f.suffix.lower() in (".js", ".css", ".html"):
        t = f.read_text(encoding="utf-8")
        if re.search(r'(?:src|href)\s*=\s*["\']/(?!/)', t):
            print("  ! 绝对路径:", f.relative_to(OUT))
        if PAT.search(t):
            print("  ! 残留 base64:", f.relative_to(OUT))
print("产物：%d 个文件 / %d B"
      % (sum(1 for f in OUT.rglob("*") if f.is_file()),
         sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file())))
