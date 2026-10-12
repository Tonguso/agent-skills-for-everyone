# Weight interpretation and testing

First establish what the numbers represent: target weights, observed portfolio weights,
share quantities or notionals. Check observation and rebalance dates, currency, shorts,
cash, leverage, gross/net totals and rounding. Do not silently normalise partial holdings
to 100% or treat quantities as weights. Use context to establish position signs; if it
does not resolve unsigned figures, state the assumption rather than silently assigning it.
If conversion inputs are unavailable, describe the supplied numbers and limit inference.

Portfolio allocation percentages describe positions, not company revenue or profit shares.
Label any chain-link totals as portfolio allocations. Do not multiply them by mixed-period,
mixed-definition business shares to imply a precise thematic revenue exposure. Such an
aggregate needs comparable denominators, dates and coverage, with unknowns retained.

Compare plausible simple models: equal weights, capitalisation/free-float weights,
inverse volatility, factor-score tilts, explicit bucket budgets or tiers. Consider caps,
floors and rounding when supported. Do not sum overlapping thematic exposures as if they
were disjoint budget buckets. Round-number tiers are clues, not proof of hand-setting.

Separate rebalance targets from subsequent price drift. If dates and returns are available,
test whether observed weights can arise from a simple starting allocation. For a fully
invested long-only basket with no flows or trades, this is proportional to starting weight
times one plus the intervening return. Account for FX and the portfolio's return convention.
Do not apply that shortcut unchanged to portfolios with shorts, cash flows or trading.
If the history is missing, retain drift as an unresolved alternative.

Compute candidate model weights on a comparable basis and inspect deviations against the
reported precision. A correlation with one metric alone does not establish the rule.
Explain relevant over/underweights relative to a stated baseline. Different metric values
among equally weighted names weaken an uncapped continuous model, but do not rule out a
capped, rounded or tiered version. Avoid inventing constraints merely to fit the sample.

Report the best-supported model, material exceptions and any models the data cannot
separate. If no model explains the deviations, say the weighting rule is unresolved;
do not default to equal weighting unless observed weights support that description.
Infer product type only when evidence extends beyond a suggestive weight pattern.
