---
name: daily-us-market-recap
metadata:
  author: Hogan Tong
  version: "1.0.0"
description: Write a concise, client-ready daily US market recap in English or Chinese using verified closing prices, market-moving news, industry performance and upcoming catalysts. Use for daily market recaps, US closing wraps, what happened in the market today, 美股收盘 and 每日市场回顾. Not for weekly reviews or intraday updates.
compatibility: Requires web access to Yahoo Finance and news or primary sources, including timestamped intraday data for the London 20:00 dollar-index observation.
---

# Daily US Market Recap

Produce a short note that a sales trader can forward directly to clients. Keep research notes and verification details separate from the finished copy. Do not distribute the note on the user's behalf without explicit approval.

## Workflow

### 1. Establish the session and verify prices

Determine the requested trading date in America/New_York. Account for holidays and early closes. Article publication dates do not establish the trading session.

Use Yahoo Finance for market prices and daily changes. Inspect quote timestamps, session dates and regular-session status, not just retrieval time. Use equity regular-session closes, never after-hours or intraday quotes.

Do not publish before the required same-day closing data have refreshed. If they have not refreshed, return only:

- English: Today's closing data haven't refreshed yet. Please try again later.
- Chinese: 当日收盘数据尚未刷新，请稍后再试。

A retrieval failure does not prove that data have not refreshed. If quotes cannot be verified, report the specific blocker separately and withhold the recap. Never substitute stale values or insert verification disclaimers into client copy. Do not promise a background retry unless one has actually been arranged.

### 2. Collect the relevant market data

Start with Yahoo quote pages, historical data, Sectors and Industries. Use available browsing and retrieval tools; custom scripts are not required by default.

Required coverage:

- S&P 500, Nasdaq Composite and Dow: closing levels and daily percentage changes. Include VIX when useful.
- Meaningful industry leaders, laggards or divergences: verified daily changes and selected stock examples.
- Gold, WTI, Brent and US Dollar Index: prices and daily percentage changes under the conventions below.
- Treasury yields when material: yield levels and daily changes in basis points, particularly 2Y and 10Y. A yield's percentage return is not a basis-point change.

Cross-assets have different closing conventions. Verify each instrument's published close or settlement and date; do not assume a US equity 16:00 close applies to all instruments. Retain timestamps and conventions internally.

#### Instrument conventions

- Gold: prefer verified spot XAU/USD if a usable Yahoo quote is available. If using GC=F, call it gold futures, never spot gold.
- Oil: use CL=F for WTI and BZ=F for Brent. Verify contracts and exchanges, including front-contract rolls. BZ=F may represent NYMEX Brent financial futures; do not label it ICE Brent without verification.
- DXY: use the DX-Y.NYB index observation at 20:00 Europe/London, respecting daylight saving time. Calculate the change against the previous trading day's observation at the same London time. Verify timestamped intraday observations for both dates. Do not substitute the current quote, daily historical Close, default daily change or DX=F futures. Keep this convention internal; client copy reports only the dollar index price and change. This fixed-time observation is an explicit exception to the close/settlement requirement. Market Open status alone does not invalidate it.
- Price and change must refer to the same instrument, contract and reference convention. Never mix spot with futures or settlements with later quotes.

#### Industry integrity

Verify the session, classification and calculation basis internally. Yahoo industry data must not be described as GICS level 3 without confirmation. ETFs are proxies, not industry indexes. Selected stocks do not establish a full-market ranking.

Focus on the day's meaningful concentration or divergence, not a sector-return laundry list. Use specific industries and stocks that explain the move. Claim top/bottom rankings only when the relevant universe has been checked. If required industry data cannot be verified, report the blocker outside the client note rather than inventing a ranking.

### 3. Identify news and catalysts

Read the day's material news across the market, not just energy or macro. Yahoo is the market-price source; use credible named news sources and primary releases for news verification.

Consider:

- Economic releases and central-bank decisions.
- Earnings, guidance, transactions and company announcements.
- Geopolitics, policy and regulatory developments.
- Industry-wide technology events, supply disruptions and demand changes.

For material economic releases, report actual versus consensus. Include prior values or revisions only when they change the interpretation. Verify actuals against official releases where possible and use one identifiable consensus survey.

Distinguish events from explanations. Attribute a move to an event only when contemporaneous evidence supports the link. Otherwise report the event and price action separately. Do not invent flows, force every move into a Fed narrative or supply a plausible explanation for an unexplained move.

Include relevant upcoming catalysts, not only today's drivers. Verify event dates and details. If an exact date is unavailable, do not invent one. Explain what the event could resolve without presenting a forecast as fact.

### 4. Compose the client note

Use the language explicitly requested by the user, English or Chinese. Otherwise mirror the current request. Neither language is a fixed default.

Normally use 5-7 short bullets, about 180-250 English words or 400-700 Chinese characters. Prioritize significance over a fixed template. Combine overlapping points and omit filler.

A useful order is:

1. Equity closes and the session's main evidenced driver.
2. Important economic data and implications.
3. Meaningful industry divergence and stock reactions.
4. Major market-moving news and verified upcoming catalysts.
5. Compact cross-asset prices and changes.

No headings, tables, attachments, introductory commentary or closing pleasantries in the recap. Keep source URLs, quote timestamps, classification caveats and troubleshooting in internal research notes, not client copy. Do not use phrases such as "under Yahoo's industry classification" or "these are latest quotes, not verified settlements" to patch missing verification.

#### Formatting

- Use ASCII hyphen bullets: `- `. Do not use decorative bullet symbols.
- Use natural punctuation in both languages. Avoid em dashes, en dashes, ornamental separators and unnecessary quotation marks.
- English uses standard ASCII punctuation and normal word spacing.
- Chinese uses ordinary Chinese punctuation. Do not insert spaces between Chinese and numbers or English terms: `9月`, `标普500`, `AMD涨2.95%`, `12亿美元`. Preserve normal spaces within English phrases.
- Use ASCII `/` for unit separators, never full-width `／`: `美元/桶`, `美元/盎司`.
- Report DXY without its source or London observation time. State instruments and units only where needed for accuracy.

## Final check

Before returning the note, confirm:

- All prices belong to the intended session and satisfy the applicable observation convention.
- Every change has the correct sign, instrument, units and reference.
- Industry claims are supported; stock examples are not disguised as rankings.
- News is relevant to the requested day, not recycled from a prior session.
- Causal claims have evidence and upcoming catalysts are verified.
- The note uses the requested language and client-copy formatting.
- No private user details, source chatter, verification disclaimers or unsupported specifics appear in the note.
