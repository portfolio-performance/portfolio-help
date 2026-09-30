You are reviewing a **Simplified Chinese translation** of the Portfolio Performance
manual for **financial terminology accuracy and semantic correctness**.

Repo: `/Users/yifeitao/Projects/portfolio-help`
- English source (ground truth): `docs/en/<page>.md`
- Chinese translation under review: `docs/zh/<page>.md`
- Authoritative termbase: `translation/TERMINOLOGY.zh.md`

## Your task
For **each page assigned to you**, read the English page IN FULL first, understand what
it actually means, then read the Chinese page and check:

1. **Financial concept fidelity** — does the Chinese say the same *financial* thing?
   Watch specifically for:
   - realized vs unrealized gains (已实现 / 未实现)
   - time-weighted vs money-weighted return (时间加权 / 资金加权)
   - absolute vs relative performance (绝对 / 相对)
   - cost basis / purchase value (成本 / 买价) — these are DIFFERENT numbers
   - internal rate of return (内部收益率) vs modified (修正)
   - annualized (年化) vs cumulative (累计) vs average (平均)
   - total return vs price return vs total cost return
   - stock split / dividend reinvestment / dividend adjustment
   - net asset value, market value, book value (市值 / 净值 / 账面价值)
   - currency conversion / FX rate direction
   - FIFO / LIFO / moving average / weighted average cost basis
   - deposits/withdrawals being cash flows vs the portfolio value itself
   - deposits account balance vs portfolio value distinction
   - tax on gains vs dividend withholding tax
   - Sharpe/Treynor/volatility/benchmark tracking error
   - secure trade date vs settlement date
   - accrued interest vs coupon

2. **Termbase conformance** — `translation/TERMINOLOGY.zh.md` is the agreed termbase.
   Flag any page that uses a different word for a term the termbase fixes.

3. **Numeric/formula integrity** — every number, formula, unit, date and sign must match
   the English exactly. A wrong sign or a swapped percentage is a serious defect.

4. **Omissions** — any English sentence, bullet, warning or caveat with no Chinese
   counterpart. Missing content is worse than clumsy wording.

5. **Added content** — any Chinese sentence asserting something the English does not.

## Output format
For each page return ONLY problems, as lines:

```
PAGE: <page.md>
L<n>: WRONG|<what English says>|<what Chinese says>|<correct rendering>
L<n>: OMITTED|<what is missing>
L<n>: ADDED|<what was added>
L<n>: TERMBASE|<termbase term>|<what page uses>
```

If a page is clean, output `PAGE: <page.md>` followed by `OK`.

Be strict and specific. Do not report style preferences, spacing, or wording that is
merely less elegant — only semantic or terminology defects. Quote the exact English
words so the finding can be verified. Do NOT edit any files.
