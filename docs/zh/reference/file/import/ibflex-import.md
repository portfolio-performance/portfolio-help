---
title: 导入 Interactive Brokers Flex Query
---

Interactive Brokers 允许客户将账户活动导出为 XML 文件。

## 创建 Activity Flex Query {#creating-an-activity-flex-query}

在首次导出数据之前，你需要先为 Portfolio Performance 创建一个 Flex Query。关于如何新建查询，请参见 Interactive Brokers 的[创建 Activity Flex Query](https://www.ibkrguides.com/clientportal/performanceandstatements/activityflex.htm)。

以下是所需的参数：

- 至少选择下列各个*部分*（除非另有说明，均为 "Select All" 行）。
  - Account Information（勾选 Account ID、Account Alias 与 Currency）
  - Cash Transactions
  - Corporate Actions
  - Sales Tax Details
  - Trades
- 在 "General Configuration" 下将 "Include Currency Rates?" 改为 "Yes"。

## 从 Activity Flex Query 导入 {#importing-from-an-activity-flex-query}

运行此前创建的 Flex Query。关于操作方法，请参见 Interactive Brokers 的[运行 Flex Query](https://www.ibkrguides.com/clientportal/performanceandstatements/runflex.htm)。

在 Portfolio Performance 中，使用 `文件 > 导入 > Interactive Brokers: Activity Flex Query`，并选择你刚刚下载的 XML。

请注意，你可以通过 "Delivery Options" 中的 "Accounts" 修改 Flex Query 使其包含多个账户，从而一次性导入多个 Interactive Brokers 账户的账目。

### 自动将 Interactive Brokers 账户与证券账户匹配 {#automatically-matching-interactive-brokers-accounts-to-securities-accounts}

Interactive Brokers 账户的 ID 形如 U1234567，并不容易记住。因此，导入器在尝试把某笔账目匹配到证券账户时，也会考虑账户别名。

例如，ID 为 U4242424、别名为 "Hotblack Desiato" 的 Interactive Brokers 账户，将与名为 "U4242424" 或 "Hotblack Desiato" 的证券账户匹配。

### 处理多货币账目 {#handling-transactions-in-multiple-currencies}

单个 Interactive Brokers 账户拥有多个外币余额，但 Portfolio Performance 每个证券账户只支持一个关联账户。因此，导入器采用一条经验规则，把外币账目匹配到正确的现金账户。

该规则是：凡是以关联账户名称开头的现金账户都视为候选。例如，若关联现金账户名为 "IB"，则名为 "IB EUR"、"IB CHF" 的账户都符合这条经验规则。