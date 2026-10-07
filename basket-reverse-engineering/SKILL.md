---
name: basket-reverse-engineering
description: Reverse-engineer an existing stock basket's investment idea, selection criteria and weights, including muddled or inconsistent construction. Use for basket interpretation or 反推篮子、拆解篮子, not requests to build a new basket.
metadata:
  author: Hogan Tong
  version: "1.1.4"
---

# Basket Reverse-Engineering

Follow explicit user instructions over this skill's workflow and presentation defaults.
Use the relevant steps with the tools available; do not expand the requested task.

## Purpose and scope
Work backwards from the names and positions: what common drivers explain them, how
strongly each name is exposed, what made a name eligible, what selected it over eligible
peers, and what determined its weight. The result is an inference about construction,
not proof of the author's intent. Several rules can produce the same basket.

Do not assume the provider had a coherent investment idea or applied consistent selection
criteria. Recover the idea as far as the evidence permits, and identify where the basket
fails to express it. A coherent core with inconsistent additions is a useful conclusion;
do not polish a muddled basket into a strategy its holdings do not support. Diagnose the
construction, not the provider's intelligence, intentions or mental state.

Do not rebuild the basket, assess whether the theme is priced in, or add unsolicited
investment advice. Do report contradictory evidence, data limitations and unexplained
names. Do not assume the user created the basket. Missing peers matter only when they
help distinguish explanations.

Use web research to verify identities and claims. Fundamentals and price data are needed
only for relevant tests; vision is needed for screenshots. If a source or capability is
unavailable, narrow the claim and say which test could not be run.

## Input and research depth
Accept text, screenshots or tables. Transcribe names, identifiers, titles, labels,
weights and position signs first; briefly state what was read. Resolve listing venue,
share class and likely ticker typos. Ask before choosing between materially different
identities when the input cannot resolve them; continue work on the unambiguous names.
Titles and descriptions are leads, not conclusions.

Look for the creation date, observation date, last rebalance, source methodology, other
baskets from the author, and any stated reference universe. Ask for missing context only
when it would materially change the interpretation and cannot reasonably be inferred.
Otherwise proceed with explicit assumptions. Do not make optional context a prerequisite.

Start with identity, business mix, relevant dates and the supplied positions. Form
plausible explanations before pulling detailed metrics. Collect data that can distinguish
those explanations, expanding the peer set only when another comparison could change the
conclusion. Lists below are examples, not mandatory data collection checklists.

## Evidence and dates
- Match the source to the claim: filings and official disclosures for business mix;
  official methodology for construction rules; dated research, earnings calls and news
  for market narratives; documented market data for prices and positioning. Company
  disclosures can establish facts, while promotional claims need corroboration.
- Keep a compact working record of decisive claims, source links, publication dates,
  observation periods and whether each value is disclosed, calculated, estimated or
  inferred. Link the decisive evidence beside the corresponding output claim.
- For historical reconstruction, use information available at the construction or
  rebalance date. A later publication about an earlier financial period is not information
  the author necessarily had. Apply this to fundamentals, estimates, ETF holdings,
  classifications and corporate actions as well as prices.
- Mark current-data substitutions or later evidence explicitly. They can describe today's
  exposure but cannot establish the historical selection rule. Missing data is unknown,
  not zero, a failed threshold, or proof that a name was ineligible.

## Step 1. Identify the names and establish the baseline
Verify every company's business, listing and share class rather than relying on memory.
Record business mix and enough size, geography and listing-history information to frame
the basket. Flag unresolved identities, recent IPOs, renamings and spin-offs.

Then collect only metrics needed by a candidate explanation. Examples include free float,
average daily traded value (ADV), index membership, revenue or EPS growth, estimate
revisions, margins, ROIC, cash flow, leverage, cash runway, valuation, analyst views,
momentum, volatility, short interest and ownership. Use business-appropriate valuation
measures; compare several only when they help discriminate a valuation hypothesis.
Keep units, currencies, measurement windows and definitions comparable across names.

## Step 2. Identify the organising idea
Consider thematic, factor/style, event-driven and trade-structure explanations. A basket
may express quality or momentum directly; those need not be overlays on a sector theme.
Mixed objectives are possible. Develop a small set of plausible candidates from evidence:

- Segment, product and end-market disclosures.
- Dated research and earnings-call language describing the names' market narratives.
- Shared catalysts such as policy, spending, supply shocks or corporate actions. Use
  real excess returns over a stated window if price reactions are part of the argument;
  a single event is confounded and does not establish causation.
- Published baskets and ETFs as leads, not proof of a common construction rule.
- Residual co-movement and factor loadings when they can distinguish candidates.
- The supplied title, group labels and accompanying explanation.

For sector-based ideas, identify the shared economic driver below broad classifications
where appropriate: a product, component, technology, drug class, customer or value-chain
link. Other drivers include geography, rates, FX, commodities, ownership, shareholder
returns, positioning and index events. Do not force these into a sector explanation.

Compare one broad explanation with narrower alternatives. Prefer a simpler account when
it explains the evidence about as well, without inventing several themes for isolated
names. One theme may suffice. Keep overlapping exposures; flag exceptions without
inventing a hedge, diversifier or marketing role. If no coherent account emerges, say so.
Use a provisional organising idea to guide Steps 3-6, and revise it if the comparisons
contradict it. Do not force a defensible theme list when the evidence favours a factor or
trade-structure basket.

Keep three questions distinct: what the provider says the idea is, what the holdings
actually express, and what selection criteria can explain membership. They may disagree.
Test coherence as well as thematic coverage: sharing a fashionable label is weaker than
sharing an economic mechanism. A multi-theme basket can be coherent, while a single-theme
label can conceal inconsistent bets. Do not create a new sub-theme for every exception
or call an opposing exposure a hedge merely to rescue the explanation.

## Step 3. Separate business exposure from market sensitivity
For each relevant name and theme, grade current business exposure independently:
- High: roughly more than half of the stated revenue or profit measure.
- Medium: roughly 20-50% of that measure.
- Low: present but below roughly 20%.
- None: evidence supports no relevant exposure.
- Unknown: evidence is insufficient to establish the exposure or its degree.

State the denominator, period and whether the figure is disclosed or estimated. Do not
mix revenue and profit shares without identifying the basis. These bands are a guide,
not precision the disclosures necessarily support. Overlapping themes can each be High;
their shares need not sum to 100%.

Describe share-price or narrative sensitivity separately where relevant, using High,
Medium, Low or Unknown with its evidence and an inferred label when judgment-based.
For example: current business exposure Low; narrative sensitivity High, inferred.
Future opportunities do not become current revenue exposure. For factor baskets, assess
the relevant factor measures instead of imposing revenue-share bands.

Record positive, negative, mixed or unknown sensitivity when direction matters. For
hedges and long/short baskets, distinguish the company's sensitivity from the position's
contribution after accounting for its sign. Do not treat two highly sensitive names as
equivalent if their exposures offset.

## Step 4. Distinguish eligibility from selection
Ask separately: what could enter the universe, and what selected these names within it?
Eligibility might depend on listing, geography, tradability or an explicit mandate.
Selection might favour thematic purity, leaders, a spread across chain links, factor
ranks, catalyst exposure or a combination.

For thematic candidates, compare chain position, current business exposure, disclosed
customer/supplier links, evidence of future exposure and inferred price sensitivity.
Distinguish contracts and committed investment from guidance and speculation. For a
factor or hedge objective, compare the relevant factor ranks or offsetting exposures.
Only infer a tiered core/satellite structure when the evidence supports it.

## Step 5. Interpret and test weights
When weights or position amounts are supplied, read [Weight interpretation and testing](references/weighting.md).
Establish what the numbers represent before comparing weighting rules; distinguish target
weights from drift, caps and rounding. If no amounts were supplied, skip this step.

## Step 6. Test the construction explanations
6a. Choose informative comparisons before inspecting the proposed filter values.
Start with credible absent peers, close substitutes, relevant ETF constituents or names
used by the same author. Explain why each is comparable without assuming it should have
been included. Include present names least consistent with the proposed explanation.
Expand when a further comparison could distinguish surviving hypotheses; do not enumerate
every conceivable peer or pad a small universe.

6b. Compare included and absent names in one working table using only discriminating
metrics. Test eligibility and selection separately. An eligibility condition can be
necessary without being sufficient: an absent name passing a liquidity threshold does
not disprove that threshold, but shows that it cannot explain selection alone. A present
name failing a proposed necessary condition contradicts it unless an evidenced exception
applies. Check dates and definitions before interpreting apparent violations.

A gap between included and absent samples supports a candidate separator, not proof of
the author's threshold. Report a feasible threshold range when that is all the data
identify. Do not invent an exact cutoff inside it. A claimed top-N rule requires an
adequate eligible-universe comparison; a few selected peers cannot establish the rank.

6c. Use near-twin comparisons when companies are genuinely similar on the proposed
exposure and business. Differences suggest candidate rules, but unobserved differences
may also explain selection. One pair is a clue; seek corroboration from other independent
comparisons or the broader sample. Skip this step when no real near-twin exists.

6d. Leave unexplained names unexplained. Multiple unusual attributes do not establish a
subjective choice. Call an addition discretionary or client-driven only with evidence.
Qualitative attributes such as sole-source status, management or installed-base revenue
also need evidence; never invent a reason for an absence.

Distinguish an unexplained name from positive evidence of inconsistency. Examples of the
latter include a stated purity rule contradicted by included businesses, comparable peers
treated differently without an evidenced criterion, or weights that work against the
claimed objective. Check date, mandate, position sign and plausible constraints before
calling these contradictions. An absent explanation alone is not proof of incoherence.

6e. Compare plausible threshold, ranking and qualitative explanations, including simple
combinations where justified. Do not stop at the first fit. Compare the strongest account
with a credible alternative and identify evidence that would separate them. Searching
many metrics makes accidental fits easier. Prefer fewer unsupported assumptions and,
when available, test the rule on additional peers or a dated basket not used to invent it.
If rules remain indistinguishable, report that rather than choosing one by confidence.

6f. Check both included and absent names at the relevant date using the Evidence and dates
rules. Listing history, past liquidity, corporate actions and information release dates
can change the conclusion. State where historical evidence is unavailable.

6g. Use sibling baskets to test partition rules and author-wide conventions when available.
Align dates and mandates before treating differences as contradictions. Overlap or
non-overlap is evidence to explain, not proof of intentional partitioning.

6h. Apply these evidence grades to construction claims, including weighting claims:
- Confirmed: explicit methodology or author confirmation supports this specific rule and
  its applicable version/date. Distinguish a documented rule from verified implementation;
  disclose any mismatch with the observed basket.
- Strongly supported: informative included/absent comparisons or weight tests support it,
  credible alternatives have been tested, and no material contradiction is unexplained.
  This remains an inference about intent.
- Consistent with: the observed data fit, but comparisons, historical data or tests of
  alternatives are insufficient to distinguish it from other explanations.
- Unresolved: missing or contradictory evidence prevents a defensible conclusion.

Assess confidence in the organising idea separately from confidence in the exact
membership rule. Strong evidence of a shared theme or driver does not establish why these
names were selected over eligible peers. State both findings explicitly in the output;
apply the construction evidence grades to the membership rule, not as a substitute for
assessing the organising idea.

Keep the conclusion's strength proportional to comparison quality, independence, universe
coverage and date alignment. There is no universal minimum peer count that establishes
confidence. State the decisive missing evidence, not a generic disclaimer. Preserve a
material counterexample even if it weakens the preferred explanation.

## Step 7. Use co-movement only where informative
When price relationships could distinguish explanations, read [Co-movement evidence](references/co-movement.md).
Use real data and distinguish common market exposure from evidence of a specific idea.
Use soft cluster discovery to generate and challenge explanations, not to impose themes
or membership thresholds. Compare within- and between-group relationships, check another
window where feasible, and try an inexpensive random-basket cohesion baseline when useful.
Interpret price clusters against business exposure and catalysts before naming them.
If the check is skipped or unavailable, state that briefly and why.

## Step 8. Form the thesis and strategy
Describe the mechanism: what changes, how it reaches these companies or factor exposures,
and what the basket appears designed to express. Separate observed characteristics from
inferred intent. Retain a credible alternative when the evidence cannot distinguish it.
These findings feed the Verdict, not an extra output section.

Make coherence judgments sensitive to position size. When weights or usable position
amounts are absent, assess consistency of membership, not portfolio-level economic
coherence. A discordant name may be a small peripheral holding or a dominant position;
do not assume either, infer equal weights, or treat its presence alone as sufficient to
invalidate the portfolio. When weights are available, distinguish a membership exception
from a material contribution that undermines the claimed objective.

Explicitly assess whether the evidence supports a coherent idea, a coherent combination
of ideas, a recognisable core with inconsistent execution, a loose collection without a
defensible common selection logic, or insufficient information to tell. These are useful
distinctions, not a forced scoring system. If the basket is muddled, identify the strongest
recoverable idea and the specific names, exposures or criteria that break it. Explain
whether the weakness lies in the investment idea, its implementation, or both. Evidence
of construction inconsistency is within scope; it is not unsolicited investment advice.

## Step 9. Check whether the brief reproduces the construction logic
Mentally hand the Verdict to a builder pursuing the inferred objective. Do not run a
builder. For a thematic basket, check the driver, sub-themes and chain links; for a factor
basket, the factor definitions and selection approach; for an event or hedge basket, the
catalyst, position signs and intended offsets. Quality can be the objective itself or an
overlay, depending on the evidence. Do not impose thematic elasticity as a universal rank.

Check that the brief distinguishes universe constraints, selection preferences and weight
rules, including target versus observed weights. Which names might the builder add or
drop, and why? Which weights would differ? A mismatch can reveal a missing rule, an
unexplained pick or several valid reconstructions. Do not fabricate constraints to recover
exact membership. State in one or two lines whether the construction logic is reproducible
and what remains underdetermined.
If the basket is inconsistent, reproducing its contradictions is not a success criterion.
Say which coherent portion can be reconstructed and which additions require arbitrary
exceptions. Do not repair those choices or propose a replacement basket unless asked.

## Output
Keep the answer phone-friendly and normally readable in a minute or two. Use short prose
and lists, no tables in the default response; working tables stay in the analysis. Keep
the four sections below, omitting IV when no weights or position amounts were supplied.
Compress repetition before removing material uncertainty or decisive evidence. Follow a
user-requested format or level of detail instead of forcing this default.

Write in the user's language. For English, use plain punctuation and straight quotes;
avoid em/en dashes, decorative characters and emoji. For Chinese, use normal full-width
Chinese punctuation, including Chinese quotation marks. Avoid special spaces. Use section
numbers I-IV in English and 一、二、三、四、 in Chinese; use 1., 2. or 1、2、 for items and
(a), (b) or （1）（2） only when sub-points help. Use bold section titles if supported.

I. Verdict / 结论（Verdict）
One forwardable paragraph describing the organising idea, economic logic, selected kinds
of company or factor exposure, and weight pattern if interpretable. Do not assume an index
is the goal. Avoid a full ticker list here, but name decisive exceptions when explaining
inconsistency. Preserve uncertainty with concise language such
as "appears designed to" when intent is inferred. Include only supported claims and any
limitation that materially changes the reading. Add at most one line on a surviving
alternative and the evidence that would distinguish it. No unsolicited investment advice.
State the coherence finding plainly when material. For example: "The core idea appears
to be X, but A and B express Y, and the proposed selection rule does not explain C."
Do not bury demonstrated inconsistency under a polished theme description. If information
is merely insufficient, say that rather than declaring the provider's idea confused.

II. Theme Identification / 主题识别（Theme Identification）
Identify each organising theme, factor, event or hedge objective with its main supporting
evidence. Separate secondary overlays where appropriate without relegating a primary
factor objective to an overlay. State the exposure legend once. For a small basket,
give a compact line per name; for a larger one, group by exposure grade and repeat names
where exposures overlap. Keep business exposure distinct from narrative/price sensitivity
and show direction where relevant. Unknown must remain visible; omit None entries only
when doing so does not conceal an unexplained name. Label disclosed figures, estimates
and inferences. Close with the co-movement result or why it was not run.

III. Selection Method Inference / 选股方法推测（Selection Method Inference）
Describe selection style, then supported eligibility and selection rules separately.
Open each rule with its Step 6h grade: Confirmed / Strongly supported / Consistent with /
Unresolved; Chinese: 已确认 / 有较强证据支持 / 与数据一致 / 尚无法判断.
State the decisive comparison and any material counterexample or missing evidence.
Include sibling-basket partitioning only when supported. Avoid cataloguing rejected
hypotheses unless a rejection explains the conclusion or corrects a likely misreading.
State the reconstruction date and any current-data substitutions. Cite decisive claims
where they appear; one generic source statement cannot support unrelated assertions.

IV. Weighting Inference / 加权方法推测（Weighting Inference）
State what the supplied numbers represent and the relevant dates, then the supported
pattern and evidence grade. Explain material deviations, supported caps/rounding/drift,
and alternatives that cannot be separated. Say when the rule or input semantics remain
unresolved. Do not infer weights when none were supplied.

Close the last section with the Step 9 usability result: whether the brief reproduces the
construction logic, and any unresolved membership or weighting choices. Keep limitations
and verification findings inside the relevant sections rather than adding boilerplate.
