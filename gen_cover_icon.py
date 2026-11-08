#!/usr/bin/env python3
"""程序化生成 Toy 封面与图标（不使用游戏截图，避免 IP 角色与截屏文字带来的审核噪音）。"""
import math
import pathlib
import random
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "deliver"
OUT.mkdir(exist_ok=True)


def font(size, bold=True):
    p = "C:/Windows/Fonts/msyhbd.ttc" if bold else "C:/Windows/Fonts/msyh.ttc"
    return ImageFont.truetype(p, size)


def night_bg(w, h, seed=11):
    """深蓝紫夜空 + 极淡星点。"""
    rnd = random.Random(seed)
    im = Image.new("RGB", (w, h))
    px = im.load()
    cx, cy = 0.5, 0.38
    for y in range(h):
        t = y / h
        for x in range(w):
            r = x / w
            glow = max(0.0, 1 - math.hypot((r - cx) * 1.4, (t - cy) * 1.5))
            base = 14 + int(14 * t) + int(20 * glow)
            px[x, y] = (base, base + 8, base + 22)
    d = ImageDraw.Draw(im, "RGBA")
    for _ in range(240):
        x, y = rnd.randint(0, w), rnd.randint(0, h)
        a = rnd.randint(20, 90)
        d.ellipse([x, y, x + 2, y + 2], fill=(180, 215, 245, a))
    return im


CREAM = (240, 232, 214)
GOLD = (200, 164, 92)
CYAN = (124, 192, 245)

# ---------- 封面 1200 x 900 (4:3) ----------
W, H = 1200, 900
im = night_bg(W, H)
d = ImageDraw.Draw(im, "RGBA")

# 魔法阵同心环
for rad, alpha, width in [(330, 46, 2), (292, 30, 2), (238, 70, 3), (232, 26, 2)]:
    d.ellipse([W / 2 - rad, 400 - rad, W / 2 + rad, 400 + rad],
              outline=CYAN + (alpha,), width=width)
for k in range(12):
    a = 2 * math.pi * k / 12
    x1, y1 = W / 2 + 238 * math.cos(a), 400 + 238 * math.sin(a)
    x2, y2 = W / 2 + 292 * math.cos(a), 400 + 292 * math.sin(a)
    d.line([(x1, y1), (x2, y2)], fill=CYAN + (48,), width=2)

d.rectangle([34, 34, W - 34, H - 34], outline=GOLD + (230,), width=3)
d.rectangle([46, 46, W - 46, H - 46], outline=GOLD + (80,), width=1)

d.text((W / 2, 286), "哈 士 喵 勇 闯", font=font(74), fill=CREAM, anchor="mm")
d.text((W / 2, 410), "魔法禁书目录", font=font(124), fill=(232, 226, 208), anchor="mm")
d.line([(350, 520), (850, 520)], fill=GOLD + (200,), width=2)
d.text((W / 2, 588), "互动文字冒险 · 三十关 · 原创美术", font=font(38, False),
       fill=(206, 202, 190), anchor="mm")
d.text((W / 2, 662), "离线可玩 · 分层立绘 · 场景演出", font=font(30, False),
       fill=(170, 178, 192), anchor="mm")
d.text((W / 2, 742), "v0.38", font=font(26, False), fill=(150, 162, 182), anchor="mm")

# 金色印章
d.rounded_rectangle([(W - 186, H - 186), (W - 96, H - 96)], radius=8, fill=(168, 92, 58))
d.text((W - 141, H - 141), "喵", font=font(62), fill=(248, 240, 222), anchor="mm")

cover = OUT / "cover.png"
im.save(cover, optimize=True)
print("封面", cover, im.size, cover.stat().st_size, "B")

# ---------- 图标 512 x 512 ----------
S = 512
ic = night_bg(S, S, seed=23)
di = ImageDraw.Draw(ic, "RGBA")
di.rounded_rectangle([14, 14, S - 14, S - 14], radius=28, outline=GOLD + (255,), width=6)
di.rounded_rectangle([28, 28, S - 28, S - 28], radius=20, outline=GOLD + (90,), width=2)
for rad, alpha in [(168, 70), (146, 30)]:
    di.ellipse([S / 2 - rad, 210 - rad, S / 2 + rad, 210 + rad],
               outline=CYAN + (alpha,), width=2)
di.text((S / 2, 208), "喵", font=font(186), fill=CREAM, anchor="mm")
di.line([(128, 352), (384, 352)], fill=GOLD + (220,), width=3)
di.text((S / 2, 414), "哈 士 喵", font=font(52), fill=(214, 208, 192), anchor="mm")

icon = OUT / "icon.png"
ic.save(icon, optimize=True)
print("图标", icon, ic.size, icon.stat().st_size, "B")
