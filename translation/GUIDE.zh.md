# Portfolio Performance 手册 —— 中文翻译工作说明（子代理必读）

你的任务：把 Portfolio Performance 手册的若干英文页面翻译为简体中文，写入
`docs/zh/` 下同名路径的文件。仓库根目录为 `/Users/yifeitao/Projects/portfolio-help`。

**动手前必须先读**：`translation/TERMINOLOGY.zh.md`（术语基准表）。这是全文唯一术语来源，
不得自行造词。工作说明原文在 `translation/GUIDE.zh.md`（即本文件）。

## 绝对不能改动的部分（改了会被 CI 判失败）

翻译只改**散文**。以下内容必须与英文原文**逐字符一致**：

1. **所有图片引用**：`![](images/xxx.png)` 的路径一字不改，包括大小写与连字符。
2. **所有链接目标**：`[文本](./path/to/page.md#anchor)` —— **只改方括号内的链接文字**，
   圆括号内的路径与 `#anchor` 一字不改。
3. **所有行内代码与代码块**：反引号内 `` `View > Reports` `` 内的内容虽需译成中文，
   但**代码块**（``` 围栏）内一律保持原样，一个字符都不动。
4. **所有数学公式**：`$$ ... $$` 块与 `$ ... $` 行内公式，原样保留。
5. **分隔符 `|`、`>`、`<`**：表格、菜单路径里的原样保留。
6. **Admonition 标记**：`!!! Note`、`!!! Important`、`!!! info "标题"` 等，
   类型关键字（Note/Important/Info/Tip/Warning/Danger/Failure）保持原样，
   只译其中的文字内容。
7. **文件名前置元数据**：`---\ntitle: ...\n---` 结构保留，`title:` 必须有，
   值译为中文。`description`、`changes`、`todo` 等键按原样结构译出。

## 必须改动的部分

- 散文段落、列表、表格单元格（表头与内容）、标题文字。
- **图注标识符**：`Figure: xxx.{class=pp-figure}` → `图： xxx.{class=pp-figure}`
  （冒号后**必须有一个空格**！`{class=...}` 原样不动）。这是中文版 mkdocs 配置的标识符。
  **务必注意**：mkdocs-caption 插件的正则要求标识符与图题文字之间有空格，
  写成 `图：标题`（无空格）会导致图注**完全不渲染**且不报错。已实测验证。
- **图注里不能用反引号或内联 HTML**：mkdocs-caption 会把图注当 XML 解析，
  里面的 `` `代码` `` 或 `<a href=…>` 会被渲染成 `<code>`/`<a>` 元素导致解析失败，
  图注**同样静默消失**（构建只在日志里报一行 `Invalid XML in caption`）。
  所以菜单路径写成 `图： 视图 > 收益 > 证券概览`，不要加反引号。
  已实测：`scripts/zh_check_captions.py` 会扫描全部图注并与构建产物比对。
- **正文中引用图的地方**：英文 "see Figure 3" → 中文「见图 3」；
  "Figure 1: ..." 这类行内引用 → 「图 1：...」。
- **标题（heading）**：`## Some Heading` → `## 某些标题`。见下方锚点规则。

## 锚点规则（关键，务必照做）

手册中有 64 处形如 `xxx.md#english-anchor` 的跨页链接，它们指向**英文标题**自动生成的
锚点。如果标题直接译成中文，这些链接会全部失效。

**因此：每个 `##` 及更深级别的标题，都必须在末尾追加原英文标题生成的锚点。**

格式：`## 中文标题 {#english-anchor}`

锚点由原英文标题按 mkdocs 规则生成：转小写 → 去掉非字母数字字符（保留连字符和空格）
→ 空格替换为连字符。例如：
- `## Performance Measurement` → 锚点 `performance-measurement`
- `## Deposit & withdrawal` → 锚点 `deposit-withdrawal`
- `## 1. Historical Quotes import` → 锚点 `1-historical-quotes-import`
- `## Stock split ...` → 锚点 `stock-split-`（注意结尾的连字符要保留）

若某标题在英文原文中已显式带 `{#...}`，保留其原有锚点。
`# 一级标题`（H1）不加锚点。

## 术语要点（摘要，完整表见 translation/TERMINOLOGY.zh.md）

- **账目** = transaction（绝不用"交易"）；**证券** = security；
  **证券账户** = securities account；**现金账户** = deposit account（不是"存款账户"）；
  **关联账户** = reference account。
- 界面标签用反引号包裹并与中文界面一致：`` `报告期` ``、`` `收益` ``、`` `成本` ``、
  `` `买价` ``、`` `全部证券` ``、`` `关联账户` ``、`` `类别` ``、`` `资产明细` ``。
  行文叙述概念时不加反引号（如"选择报告期后即可看到绩效"）。
- 菜单路径整体放反引号并译成中文：`` `视图 > 报告 > 收益` ``、`` `文件 > 导入` ``。
- **收益** = 界面 performance；**收益率** = return。
  资金加权收益率 / 内部收益率 (IRR) / 时间加权收益率 (TTWROR)。
- **先进先出** = FIFO（不是"先入先出"）；**移动平均** = moving average。
  **未实现收益 / 已实现收益** = unrealized / realized gains；
  **资本利得** = capital gains。
- **报价** = quote（不是"行情"）；**市值** = market value；
  **期初市值/期末市值** = MVB/MVE；**股息** = dividend。
- **最大回撤** / **下行波动率** / **波动率**；**夏普比率**。
- 金额与货币单位（EUR/USD/GBP）不译。应用名 Portfolio Performance 不译。
- 文件名、XML/CSV 列名、类名、API 名称一律保持英文原样并用反引号。

## 文风

- 技术手册的简体中文：准确、简洁、书面语，不要翻译腔，不要口语填充词。
- 长句可适当拆分以符合中文习惯，但不得增删信息。
- 标点用全角（，。：；），但代码、行内代码、英文专有名词内部用半角。
- 不要添加原文没有的解释，也不要省略原文的限定语（如"仅""通常""在此情形下"）。

## 交付前自检

逐页确认：
- [ ] 没有改动任何图片路径、链接目标、代码块、公式
- [ ] 每个 `##`+ 标题都带 `{#english-anchor}`
- [ ] `Figure: ` 已改为 `图： `（**冒号后有空格**，`图：标题` 不渲染）
- [ ] 图注里**没有**反引号或内联 HTML（否则图注静默消失）
- [ ] 图注里引用的图号与原文一致（编号不重排）
- [ ] front matter 有 `title:`
- [ ] 没有出现 U+FFFD（乱码）或重复/丢失的段落

跑一遍机器校验（提交前必须全绿）：

```
python3 scripts/zh_check_captions.py     # 图注：反引号 + 渲染数量
python3 scripts/zh_audit_terms.py        # 禁用译法
python3 scripts/zh_verify_anchors.py     # 锚点与英文一致
python3 scripts/zh_check.py              # 结构：图片/链接/围栏/公式
mkdocs build -f config/zh/mkdocs.yml     # 最终构建，0 warning
```

完成后回报：翻译了哪些文件，以及任何你判断存疑的术语。