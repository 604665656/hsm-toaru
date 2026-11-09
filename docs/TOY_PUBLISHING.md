# 哈士喵禁书目录 v0.81 · TOY 上架说明（2026-11-09）

## 交付包
- `哈士喵禁书目录_v081_发布包.zip`：8 条目 / 12,083,545 B，Windows 打包未写 UTF-8 flag，
  8 个中文名按 `cp437 -> utf-8/gbk` 还原（见 `_unpack_new.py`）。
- 主入口 `index.html` 14,653,515 B，单文件离线可玩；另有 README.md 与 3 张截图。
- 页面 `<title>` 仍写 `v0.65`，是上游归档遗留；按「不动源文件」原则保留，README 如实注明。

## 分包策略
`_build_all.py` 统一纯分包，零内容改动：
- 1 个内联 `<script>`（14,368,381 字符）→ `app1.js`
- 1 个内联 `<style>`（100,512 字符）**保持内联**：全文有 44 处 `url(#...)` SVG fragment 引用，
  外置成 CSS 会解析失效（与 11-08 哈士喵 v0.38 结论一致）。
- 入口 `index.html` 127,305 B（原 14.65 MB），远低于 Toy 1 MB 硬限制。
- 0 根绝对路径引用、0 `assets/` 外部依赖，406 处 `data:image` 全部内嵌。

## 校验
- `node --check app1.js` 通过
- `toy_doctor.py --require-root-index`：0 warning 通过
- 复用命令：`toy update 52938462465024 toy --yes --json`

## 与旧版差异
旧版 v0.38 全部内容移入 `legacy/2026-11-09/`，主目录为 v0.81 新交付；
GitHub 保留完整单文件源码，Toy 产物只做分包，不做内容裁剪。
