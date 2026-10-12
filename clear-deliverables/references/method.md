# Reader-first patterns

Use the smallest fitting structure. Do not force every field into every artifact.

- Explanation: answer; definitions and assumptions; mechanism; worked example with units; boundaries and exceptions; evidence and remaining uncertainty.
- Procedure: purpose; owner; prerequisites and inputs; ordered actor/action steps; expected result; decision conditions; stop/recovery; completion check and handoff.
- Specification: objective and non-goals; terms; inputs/outputs and units; MUST requirements with conditions; interfaces; failure behavior; acceptance criteria; unresolved decisions.
- Handoff: verified state; artifacts and versions; decisions with reasons; blockers; next owner/action; acceptance condition; recovery point. Distinguish completed work from plans.

## Precision example
Vague: “If it fails, retry and notify operations.”
Precise: “If the import rejects a row, the operator stops publication and saves the rejected-row log. The operator corrects the source row and reruns validation on the same batch ID. Publish only after validation reports zero rejected rows. If the prior publication outcome is unknown, check the publication receipt before retrying.”
This is an illustrative procedure, not a description of a particular production system.

Maintenance-manual techniques can help here: imperative steps, explicit conditions, one action per step when ordering matters, warnings before hazardous actions, expected outcomes after actions. They are optional tools. Do not replace technical terms with imprecise synonyms, force an English dictionary on Chinese, or advertise untested STE compliance.

## Substantive review
Can the reader act without guessing who does what? Are required inputs available? Are units, signs, dates/timezones and naming consistent? Do numeric examples recompute? Does the evidence support the specific conclusion? What happens on partial success, timeout, missing data or unknown external-action outcome? Is the restart safe? Are assumptions distinct from requirements?

## Diagrams and rendered review
Choose sequence for ordered exchanges; flow for branching tasks; state for allowed transitions; architecture for ownership/interfaces. Label relationships (“sends batch ID”, “if rejected rows > 0”), not just unlabeled arrows. Show direction and boundary. Use the same step/node identifiers in prose. Include a text description so the diagram is not the sole carrier of instructions.

At actual viewing sizes check label overlap, clipping, contrast, line/arrow meaning, hierarchy, units and readable text. For long pages inspect the entire page, not only the top. Local diagram scrolling is acceptable when discoverable and usable; page-wide unintended overflow is not. Check applicable keyboard interactions separately. Style choices such as max-width, colored borders, balanced headings and Chinese “——” are not defects by themselves.

## Arrow geometry

Arrows run horizontal or vertical. Where a route must turn, use a 90-degree elbow and the fewest bends that work; re-place boxes before adding elbows. No curves or diagonals unless no orthogonal route exists, and then list each exception with its reason when delivering.

1. Boxes sit on a grid: equal widths within a row, aligned centres, consistent gaps. Most arrows should then be one straight line; widen a gap rather than bend.
2. An arrow leaves from the middle of a box edge; several arrows sharing an edge are evenly spaced. The arrowhead tip lands on the target border (within 1px), set by placing the marker tip at the path end (refX at the tip).
3. Opposite arrows between the same pair of boxes are parallel and evenly offset.
4. A self-loop is a small symmetric rectangle: both ends on the same edge, equally spaced about its centre, label right beside it.
5. A label sits beside the middle of its own segment with a small, consistent gap: never on a line, never on a box.
6. No line passes through a box or a label. Minimise crossings. Everything stays inside the viewBox with a margin.
7. Decision diamonds: branches leave from the left/right (or bottom) vertex, run horizontally, then turn 90 degrees down into the top-middle of the target box. Yes/no labels sit beside the start of each branch.
8. The shaft is at least 20px long beyond the arrowhead; a head with no visible shaft is a defect.

Check: run scripts/check_html.py (see html-checker.md); arrow rules must report zero issues or each remaining one is a listed exception. Then render every figure and look at it, because the script does not judge symmetry, spacing or whether boxes could be placed better.


## References

- [Agent Skills specification](https://agentskills.io/specification): the package format.
- [FutureAtoms / karpathy-ladder](https://github.com/FutureAtoms/karpathy-ladder): inspiration for labelled diagrams, distinguishing sources from interpretations, and browser-based layout checks.
