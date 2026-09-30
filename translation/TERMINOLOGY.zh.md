# Portfolio Performance 中文译名对照表（译名基准）

本文件是中文版手册的**唯一术语基准**。所有页面必须以此表为准，不得自行造词。
术语来源优先级：

1. **应用程序自身的简体中文界面**（`messages_zh.properties`，PP 官方译名）——凡界面里已
   有译名的，一律照抄，**不得改写**。
2. 金融教科书 / 中国大陆证券业通用译名。
3. 上述两者冲突时，以可理解性优先，并在 `docs/zh` 页面内保持前后一致。

## 一、总原则

- **引用界面文字时**：一律用反引号包裹，且与中文界面**完全一致**，如
  `` `报告期` ``、`` `收益` ``、`` `关联账户` ``。英文手册用 `View > Reports > Performance`，
  中文版对应写成 `` `视图 > 报告 > 收益` ``（菜单层级名同样译成中文）。
- **描述概念时**（行文中叙述，不是在引用界面）：不用反引号，不要求与界面一致。
  例如"选择报告期后即可看到绩效"——这里 `报告期` 是概念，不加反引号。
- 判断法则：**能自然接上"……字段／……菜单／……列"的，是界面标签，加反引号并照抄界面译名。**

## 二、核心账户与账目（Transaction / Account）

| 英文 | 中文 | 说明 |
| :--- | :--- | :--- |
| transaction | 账目 | PP 官方译名。**不是**"交易"。全文统一 |
| security | 证券 | PP 官方译名 |
| securities account (depot) | 证券账户 | PP 官方译名（内部代码 depot） |
| deposit account | 现金账户 | PP 官方译名 `现金账户`。**注意**：不是"存款账户" |
| reference account | 关联账户 | PP 官方译名 |
| offset account | 目标账户 | PP 官方 `目标账户`。**不是**"对手账户" |
| account | 现金账户 | PP 官方译名。裸 account 指现金账户 |
| portfolio | 投资组合 | |
| buy | 买入 | 界面用「买入」，名词形式「买」仅在描述配对时出现 |
| sell | 卖出 | |
| dividend | 股息 | 界面用「股息」，非「红利」 |
| delivery inbound / outbound | 证券转入 / 证券转出 | 官方 `证券转入` / `证券转出`。delivery 一律译"证券转入/转出"，不译"交割" |
| transfer | 转账 | 账户间转账 |
| security transfer | 证券转移 | 官方 `LabelSecurityTransfer` = **证券转移**。**注意**：与 delivery（证券转入/转出）是不同的账目类型，全文不可混用「证券转账」 |
| stock split ratio N-for-M | N 拆 M | 例如 2-for-1 = `2 拆 1`，20-for-1 = `20 拆 1`，反向分股 1-for-5 = `1 拆 5`。比例方向不可颠倒 |
| symbol | 证券代码 | 官方 `ColumnSymbol` = `证券代码` |
| deposit (transaction) | 存款 | 官方 `存款`。入金动作用"入金" |
| withdrawal | 取款 | 官方 `取款`。名词形式亦作"转出"（官方 `转出`），全文择一：用「取款」 |
| interest | 利息 | |
| interest charge | 利息支出 | 官方 `利息支出`。不是"利息费用" |
| fees | 费用 | |
| fees refund | 费用退款 | 界面无此独立标签，按构词法处理 |
| tax / taxes | 税款 | 官方 `税款` |
| tax refund | 退税款 | |
| stock split | 分股 / 拆股 | 官方 `分股`。行文中拆股亦可，正文统一用「分股」 |
| inbound delivery | 证券转入 | |
| outbound delivery | 证券转出 | |

## 三、绩效指标（Performance）

本节是全文最易出错处，务必逐条对照。

| 英文 | 中文 | 说明 |
| :--- | :--- | :--- |
| performance | 绩效 / 收益 | **界面用 `收益`**（官方 `收益`）。行文叙述概念时用「绩效」，界面标签一律「收益」 |
| return / rate of return | 收益率 | 官方 `收益率` |
| total return | 总收益率 | 手册中 Absolute Performance 的同义词 |
| absolute performance | 总收益 | 官方 `总收益`（绝对值，非百分比） |
| absolute performance % | 总收益率 % | 官方 `总收益率 %` |
| money-weighted rate of return | 资金加权收益率 | 亦称 IRR。**不是**"金额加权" |
| internal rate of return (IRR) | 内部收益率 (IRR) | 官方 `内部收益率 (IRR)` |
| time-weighted rate of return | 时间加权收益率 | |
| true time-weighted rate of return (TTWROR) | 时间加权收益率 (TTWROR) | 官方 `时间加权收益率 (TTWROR)`。日常简写 TTWROR |
| TWROR p.a. / per annum | 年化时间加权收益率 | `TTWROR p.a.` 保留原标识并加注"年化" |
| simple rate of return | 简单收益率 | |
| annualized | 年化 | |
| cumulative | 累计 | |
| periodic | 期间收益率 | 对应 TTWROR 的非年化值 |
| total rate of return | 总收益率 | |
| realized gains | 已实现收益（资本利得） | 官方 `实现资本利得`。行文可用「已实现收益」 |
| unrealized gains | 未实现收益（浮动盈亏） | 官方 `未实现资本利得` |
| capital gains | 资本利得 | 官方 `资本利得` |
| profit / loss | 盈 / 亏 | 官方 `盈 / 亏` |
| gross profit / loss | 毛利 / 亏 | 官方 `毛利 / 亏` |
| earnings | 收入 | 官方 `收入`（= 股息 + 利息） |
| gross | 总额 | 官方 `总额` |
| net | 净 | 官方 `净` |
| net transaction value | 净额 | 官方 `净额` |

## 四、成本与买价（关键概念，易错）

| 英文 | 中文 | 说明 |
| :--- | :--- | :--- |
| purchase value | 成本 | 官方 `成本`（= 买价 × 份额，含费用） |
| purchase price | 买价 | 官方 `买价`（每股平均买入成本） |
| acquisition cost | 买入成本 | 概念叙述时用 |
| acquisition cost method / cost method | 买价计算方式 | 官方 `买价计算方式` |
| FIFO (First-In, First-Out) | 先进先出 (FIFO) | 官方 `先进先出`。**不是**"先入先出" |
| moving average | 移动平均 | 官方 `移动平均` |
| Adjusted Cost Base (ACB) | 调整后成本基础 (ACB) | 加拿大/法语区术语，作括注 |
| gross purchase price | 买价 (总额) | 官方 `买价 (总额)`，含费用与税款 |
| charge | 买入总成本 | 一次买入的总支出（含费用税款） |
| proceeds | 卖出净收入 | 卖出实得（扣费税后） |
| entry value | 入场价格 | 官方 `入场价格` |
| exit value | 离场价格 | 官方 `离场价格` |
| debits | 借记 | 官方 `借记` |
| credits | 贷记 | 官方 `贷记` |

## 五、风险指标

| 英文 | 中文 | 说明 |
| :--- | :--- | :--- |
| volatility | 波动率 | 官方 `波动率` |
| semivolatility / semideviation | 下行波动率 | 官方 `下行波动率` |
| maximum drawdown (MDD) | 最大回撤 | 官方 `最大回撤` |
| drawdown duration | 最长回撤期 | 官方 `最长回撤期` |
| current drawdown | 当前回撤 | 官方 `当前回撤` |
| Sharpe ratio | 夏普比率 | 官方 `夏普比率` |
| risk-free rate of return | 无风险收益率 | 官方 `无风险收益率` |
| high watermark | 历史最高水位 | |
| all-time high (ATH) | 历史最高 | 官方 `历史最高` |
| distance to SMA | 距 SMA | 官方 `距 SMA` |
| SMA (simple moving average) | 简单移动平均 (SMA) | 官方 `简单移动平均 (SMA)` |

## 六、行情与价格

| 英文 | 中文 | 说明 |
| :--- | :--- | :--- |
| quote | 报价 | 官方 `报价`。**不是**"行情" |
| historical quote | 历史报价 | 官方 `历史报价` |
| historical price | 历史价格 | 行文常用，与 historical quote 同指 |
| price | 价格 | |
| market value (MV) | 市值 | 官方 `市值` |
| market value at beginning (MVB) | 期初市值 | |
| market value at end (MVE) | 期末市值 | |
| closing price | 收盘价 | 官方 `收盘价` |
| ex-date | 除权日 | 官方 `除权日` |
| actual # quotes | 实际 # 报价 | 官方 |
| expected # quotes | 预期 # 报价 | 官方 |
| missing # quotes | 缺少 # 报价 | 官方 |
| completeness | 完整性 | |
| price provider / quote feed | 提供方 | 官方 `提供方`。**注意区分**：官方 `LabelQuoteFeed` = **报价馈送**（指数据源本身），`GroupLabelQuoteFeed` = **报价提供方**（指该分组）。行文用「报价馈送提供方」指具体 JSON 馈送，用「提供方」泛指 |
| base currency | 基准货币 | 官方 `基准货币` |
| target currency | 目标货币 | 官方 `目标货币` |
| currency gains | 汇兑损益 | 官方 `汇兑损益` |
| exchange rate | 汇率 | 官方 `汇率` |
| completeness of historical quotes | 历史报价完整性 | |

## 七、报告与界面结构

| 英文 | 中文 | 说明 |
| :--- | :--- | :--- |
| reporting period | 报告期 | 官方 `报告期`。英文手册的 Reporting Period 一律译「报告期」 |
| statement of assets | 资产明细 | 官方 `资产明细` |
| holdings | 持仓 | 官方 `持仓` |
| payments | 收入 | 官方 `收入`（报表名，指股息+利息明细） |
| trades | 头寸 | 官方 `头寸`。**不是**"交易"。closed/open trade = 已结/未结头寸 |
| trade | 头寸 | 一次完整的买卖配对 |
| calculation | 计算 | 官方 `计算` |
| dashboard | 仪表板 | 界面 `报表`。行文用「仪表板」 |
| chart | 图表 | 官方 `图表` |
| taxonomies | 类别 | 官方 `类别`。taxonomy = 分类体系，全文译「类别」 |
| allocation | 配置 | 官方 `配置` |
| weight | 权重 | 官方 `权重` |
| rebalancing | 再平衡（界面 `调整`） | 行文用「再平衡」，界面标签用 `调整` |
| widget | 组件 | |
| watchlist | 关注列表 | 官方 `关注列表` |
| general data | 常规数据 | 官方 `常规数据` |
| security account | 证券账户 | |
| all transactions | 全部账目 | 官方 `全部账目` |
| all securities | 全部证券 | 官方 `全部证券` |
| only inactive instruments | 仅已停用证券 | 官方 `仅已停用证券`。**不是**"仅已停用投资品" |
| only active instruments | 仅已启用投资品 | 官方译名 |
| holdings ≠ 0 / = 0 | 持仓 ≠ 0 / = 0 | 官方筛选项 |
| markings | 标记 | 官方 `标记` |
| remove entries | 移除所有过滤器 | 官方 `移除所有过滤器` |
| grouped accounts | 账户分组 | 官方 `账户分组` |
| investment plans | 投资计划 | 官方 `投资计划` |
| savings plans | 储蓄计划 | |
| stock split | 分股 | |
| spin-off | 分拆 | |
| merger | 合并 | |
| insolvency | 破产 | |
| CSV import / export | CSV 导入 / 导出 | |
| PDF import | PDF 导入 | |
| XML file | XML 文件 | |
| performance neutral transfers | 绩效中性转账 | |
| cash flow | 现金流 | |
| inflow / outflow | 流入 / 流出 | |
| external flow | 外部现金流 | |

## 八、图中与正文交叉引用

- 图注前缀 `Figure:` → **`图：`**（`config/zh/mkdocs.yml` 已配置 `markdown_identifier: '图：'`）。
- 正文中引用图的地方，英文写作 "see Figure 3"，中文写作**「见图 3」**。
- 章节标题 `Figure 1: ...` 这类行内引用也译为「图 1」。
- 表格标题统一 `表 1：`。

## 九、书写规范

- 标点用全角中文标点；括号内含英文/代码时用全角括号，如 `报告期（Report Period）`。
- 金额单位沿用原文 EUR / USD / GBP 等，不翻译。
- 菜单路径用 `>` 连接且整体包在反引号内：`` `文件 > 导入 > CSV 文件` ``。
- 应用名 **Portfolio Performance** 保留英文原样，两词之间空格。
- 文件名、代码标识符、XML/CSV 列名保持英文原样并用反引号。