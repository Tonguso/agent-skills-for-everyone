---
name: quant-literature-research
description: Searches, gathers and synthesises academic and industry literature on quantitative finance topics (factors, anomalies, strategies, market microstructure, risk models, ML for trading), judges how credible each piece is, and writes a replication brief for a backtest. Use when the user asks to look into the literature on a topic, find papers on a factor or strategy, check whether a claimed effect is real or replicates, judge whether a paper or research report is reliable, or wants a synthesis before modelling or backtesting. Covers research and judgment only, not coding or backtesting.
compatibility: Needs web search and the ability to fetch web pages (journal, preprint and working-paper sites, factor databases).
metadata:
  author: Hogan Tong
  version: "1.2.1"
---

# Quant Literature Research

## Requirements and evidence access
Requires web search and access to source pages; full-text pages or PDFs are needed to verify methods and numerical results. Use the host agent's available tools. If access is unavailable, disclose the limitation rather than pretending to have reviewed the evidence.
For each source, state whether you read metadata, an abstract, selected sections, or full text. Track the version and access date where practical. An abstract-only review cannot support a complete replication brief. Mark unavailable inputs as unknown; never infer formulas, lags, costs, or reported statistics.

## Purpose
This skill covers the layer before modelling and backtesting: find the relevant
literature, work out what it actually says, and — the part that matters most — judge
whether it's trustworthy enough to act on or feed into a backtest. The coding and
backtesting happen separately, and this skill ends with a brief for that step. A
well-organised summary of a bad paper is worse than useless; it launders weak evidence
into something that looks authoritative.

Typical requests: survey what's known on a quant finance topic before building or testing
it; find papers on a factor or strategy; check whether a claimed anomaly, factor or effect
replicates and still holds up; judge whether a specific paper or research report is
reliable.

## Citation integrity (non-negotiable)

A made-up citation is the worst failure this skill can produce: it looks authoritative and
gets passed on to the backtesting step as if it were real.
- **Cite only papers you have actually found in this session.** Open the paper's page
  (journal, preprint server, working-paper series, author site) and check the title,
  authors, year and venue against that page before citing it. Give the link.
- **Never fill in details from memory.** That includes the journal, year, sample period,
  t-stats or Sharpe ratios. If a number isn't on a page you read, don't state it.
- If you remember a paper but can't find it, either leave it out or mark it plainly as
  "recalled, not verified". Never present it as a checked source.
- Quote key numbers (alphas, t-stats, sample periods) from the paper itself, not from a
  secondary summary, which may have garbled them.

## Source tiers

Label each source using these publication categories, separately from evidence quality.
Publication status is useful context, not a mechanical credibility ranking: a transparent,
independently replicated working paper may provide stronger evidence than a weak published
study. Judge methods, identification, transparency and replication before venue or reputation.

1. **Published, peer-reviewed journals** — record the journal and review status; peer
   review does not establish that a result replicates. The top general finance journals first (Journal of Finance,
   Journal of Financial Economics, Review of Financial Studies), then other strong
   finance, econometrics and management-science journals, then applied and practitioner
   journals. For a non-US market, the leading local journals (including local-language
   ones) also belong here for local evidence. Markets often behave differently, so a
   result from one market does not carry over to another by default.
2. **Established working-paper series** (e.g. NBER) — not journal peer review;
   affiliation and circulation do not replace a methodological assessment.
3. **Open working-paper repositories** (e.g. SSRN) — huge volume, no peer review, quality
   varies enormously. This is where most quant factor research surfaces first. Useful for
   finding things early, but flag explicitly as unreviewed.
4. **Preprint servers** (e.g. arXiv q-fin) — same caveat, skews more technical and
   mathematical. Use the relevant sub-categories (statistical finance, trading and
   microstructure, portfolio management, risk management, computational finance).
5. **Institutional research** — asset managers' and banks' quant research and white
   papers. Credible on data and technique, but read knowing the author may have a
   commercial incentive to make an effect look robust (they may be selling a product
   built on it).
6. **Sell-side research, research newsletters and paid research communities** — useful
   for context and leads. Assess any empirical evidence on its methods and transparency;
   commentary or inaccessible supporting analysis cannot validate a strategy.

## Search method

1. **Clarify the question first** if it's ambiguous — a factor name alone isn't enough;
   confirm the asset class, region, and horizon the user cares about, since most effects
   are asset-class- or region-specific and don't automatically generalise.
2. **For equity anomalies and factors, check large-scale replication studies and open
   factor databases first.** Several academic projects have re-run hundreds of published
   anomalies under common, stricter rules, and some publish code and regularly updated
   factor returns, including across many countries. Search for them by topic ("anomaly
   replication", "factor replication database", "open source asset pricing"). They answer
   "is it real, and does it still work?" faster than reading papers one by one:
   - If the factor has been re-tested there, start from that result, not the original
     paper's.
   - Expect shrinkage. Re-tests that handle microcaps properly typically find a large
     share of published anomalies don't hold up, and studies of post-publication returns
     find published effects lose a substantial part of their return after publication.
     Discount any published effect accordingly unless there is evidence it held up.
   - Where updated factor returns exist, examine returns after the original sample and
     after publication separately. Check when the signal and implementation choices were
     fixed, whether database construction changed, and whether later data informed those
     choices. A database extension is not automatically an independent replication or a
     clean out-of-sample test. Label fresh fixed-rule observations, revised backfills and
     independent replications separately.
   - If the factor isn't covered by any of these, say so: that is information too.
3. **Search broadly, across tiers**, using web search against each source (e.g.
   `site:arxiv.org q-fin [topic]`, `site:ssrn.com [topic]`, `"[topic]" journal of finance`).
   Don't stop at the first hit — pull enough results to see the shape of the literature:
   is this one paper, a small cluster, or a well-established area with dozens of
   follow-ups and rebuttals?
4. **Screen by title/abstract** before reading full text — same logic as a PRISMA-style
   systematic review, just not formally documented as one unless the user wants that level
   of rigour. Discard obviously irrelevant or low-quality hits before spending time on
   full text.
5. **Pull full text** for anything that clears the screen. For paywalled journal articles,
   look for an ungated working-paper or preprint version of the same paper before giving
   up — many published papers have a public preprint.
   For a working paper, check whether it was later published, and where. Publication moves
   it up a tier. Also check whether the results changed between versions: effects that
   shrink from the first draft to the published version are a warning sign.
6. **Chase citations both ways** where it matters: what did this paper build on, and —
   more importantly — has anything since tried to replicate, extend, or debunk it? A
   factor that nobody has revisited for years is a different risk profile from one that's
   been stress-tested by a decade of follow-up work. Use citation indexes (e.g. Google
   Scholar's "Cited by", Semantic Scholar) to find later papers, and search the paper's
   title together with words like "replication", "revisited", "fails" or "does not
   survive".

## Credibility assessment — the actual judgment

This is the part generic literature-review tools don't do. Apply these checks to every
paper/claim before reporting it, and give the user an explicit verdict (High / Medium / Low
confidence, or Insufficient evidence), not just a summary. Separate confidence in the
paper's stated finding from evidence of incremental alpha and implementability.

1. **Peer-reviewed vs working paper.** State which, and check the version, corrections,
   retractions and subsequent publication. Peer review is not a substitute for checking
   the evidence, and an unpublished result is not automatically weak.
2. **Out-of-sample testing.** Does the paper test on data outside the period/sample used
   to find the effect? In-sample fit alone is weak evidence of predictive performance;
   assess it against the actual claim rather than dismissing all in-sample analysis. This is the single most important check for anything
   factor/strategy-related.
3. **Multiple testing / data snooping.** Quant finance has a well-documented file-drawer
   problem: researchers (and firms) test hundreds of factors and publish the handful that
   come back significant. A single significant result with no adjustment for how many
   things were tried should be discounted. Look for whether the paper addresses this
   (multiple-testing-adjusted t-stat thresholds, deflated Sharpe ratios) or ignores it
   entirely.
4. **Economic rationale.** Is there a story for *why* the effect should exist — a risk
   premium, a behavioural bias, a structural/liquidity constraint — or is it pure
   statistical pattern-matching with no mechanism? Treat the proposed mechanism as a
   hypothesis to test, not evidence that the effect will persist. A convincing story
   cannot rescue failed out-of-sample results.
5. **Sample length and robustness across markets/periods.** An effect shown in one
   market over a short window is weak evidence. The same effect holding across multiple
   markets, multiple decades, or surviving regime changes is much stronger.
6. **Track record of the authors/institution.** Not an appeal to authority for its own
   sake, but repeated, later-validated work from the same group is a real signal;
   a first paper from an unknown source with no follow-up is not automatically wrong,
   just unproven.
7. **Has it been replicated or debunked since?** Actively search for later papers that
   tried to reproduce the result. Many well-known "anomalies" have been shown to weaken
   or disappear post-publication (a documented pattern in this literature — publication
   itself can cause an effect to be arbitraged away, or reveal it was p-hacked in the
   first place). Flag explicitly if you find a later paper that contradicts or fails to
   replicate the original.
8. **Is it new, or a known factor under a new name?** Use controls appropriate to the
   asset class, market and claimed mechanism. For equities, Fama-French factors plus
   momentum may be relevant; other asset classes need different benchmarks. A signal
   explained by existing factors has weak evidence of incremental alpha, but may still
   be useful as an implementation or exposure choice. That does not by itself make the
   paper low credibility. State when controls are inadequate for the claim.
9. **Is it driven by microcaps or the short side?** Check whether the result holds
   value-weighted and with size breakpoints based on large-cap stocks, not only
   equal-weighted across all stocks. Check whether the profits come mostly from the short
   leg. Shorts in small, illiquid names are often expensive or impossible to borrow.
10. **Does it survive trading costs and capacity?** Look for turnover, cost assumptions
    and capacity estimates. Many high-turnover anomalies disappear after realistic costs.
    Also ask whether it can be implemented with the instruments available (cash equities,
    swaps, futures) and what borrow it needs.

### Confidence rubric
Combine the checks into the verdict like this, then adjust with judgment and say why:
- **High:** effect survives out of sample (including after publication where data
  exists), holds in more than one market or period, has a plausible mechanism, survives
  standard factor controls, and has been independently replicated.
- **Medium:** survives out of sample and has a mechanism, but evidence is limited to one
  market, it hasn't been independently replicated, or it weakens materially after costs
  or value weighting.
- **Low:** weak evidence for the specific claim, such as a predictive effect supported
  only in sample, material leakage, uncontrolled specification search, or credible failed
  replications. Microcap dependence and equal weighting restrict relevance and trading
  feasibility; they are not automatic proof that the measured effect is false.
- **Insufficient evidence:** access or reporting is too limited to assess the claim.
  Missing out-of-sample, cost or replication evidence is not the same as a failed test.
  State what would be needed to make a judgment.

No universal t-stat cutoff establishes multiple-testing validity. A threshold near 3
appears in some equity-factor research, but the appropriate correction depends on the
hypothesis family, dependence structure, search process and inferential method. Check
what adjustment the study actually uses. Apply this predictive-strategy rubric only
where relevant; descriptive, theoretical and causal studies need assessments suited
to their claims.

**Credibility and relevance are separate verdicts.** A credible result from one market,
size segment or horizon may say little about another. Give both: how much to trust the
paper, and how much it applies to the market, region and horizon the user asked about.

### Extra warning signs for machine-learning papers
ML papers fail in their own ways. Check for:
- **Leakage:** information from the test period reaching training, through feature
  scaling fitted on the full sample, look-ahead in features, or random train/test splits
  on time-series data.
- **Overlapping labels:** check whether training-label information intervals overlap
  validation/test intervals. Purge affected training observations where they do. Consider
  an embargo when the split design and remaining information dependence justify one;
  it is not universally required and is not a substitute for chronological validation.
  Explain the split, information intervals and chosen safeguards.
- **Hyperparameters tuned on the test period,** or many model variants tried with only
  the best one reported. Treat that as a multiple-testing problem and look for a deflated
  Sharpe ratio or similar.
- **No simple baseline.** If a linear model or a known factor gets most of the result,
  the ML adds little.
- **Gross returns only,** with high turnover and no cost analysis.

## Output format

For a single paper/claim, give the user:
- **What it claims** (one or two sentences, plain language)
- **Data and method** (market, period, technique — enough for whoever runs the backtest
  to know what it would take to reproduce)
- **Publication category and credibility verdict** (High / Medium / Low / Insufficient
  evidence per the rubric, with the specific reason and checks that drove it)
- **Access coverage** (metadata, abstract, selected sections or full text; version and
  access date where practical), plus missing evidence and its consequences
- **Relevance verdict**, separately: how far it applies to the market, region and horizon
  in question
- **Replication status**: whether the effect has been re-tested in replication studies or
  factor databases, what they show (including performance after the paper's sample
  ended), and any later paper that confirmed or contradicted it
- **Source link(s)**, verified as per Citation integrity
- **Handoff brief for the backtest**, in a fixed shape so the replication can be checked:
  - Signal definition, exactly as the paper builds it (formula, inputs, any ranking or
    standardisation)
  - Data needed, and from where (prices, accounting data, analyst data, etc.)
  - Universe and filters (exchanges, size filter, price filter, exclusions such as
    financials or microcaps)
  - Portfolio construction (sorts or regressions, number of portfolios, value or equal
    weighting, long-short or long-only) and rebalance frequency
  - Lags on accounting data to avoid look-ahead (e.g. the paper's assumed reporting lag)
  - Benchmarks the signal must beat (which factor model)
  - The paper's reported numbers to reproduce (mean return, t-stat, alpha, Sharpe, sample
    period), quoted from the paper with page or table reference
  - Known pitfalls to watch (survivorship, transaction costs, regime dependency, borrow)

For a literature survey across a topic, group by tier and give a short synthesis:
what's well-established, what's contested, what's a single unreplicated claim. Don't
flatten disagreement in the literature into a false consensus — if authors disagree,
say so and say why. Every paper mentioned carries its verified link and tier.

Keep it honest about gaps: if the search turns up thin or contradictory literature, say
that plainly rather than padding the answer with tangential results dressed up as
relevant.

## Language

Reply in the language the user writes in, but keep paper titles, author names, and
technical terms (Sharpe ratio, look-ahead bias, p-hacking, etc.) in their original form,
since that's how they will be cited and searched.
