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

## Sources and deliberate exclusions
Agent Skills format: https://agentskills.io/specification (read 2026-10-07).
Method inspiration: https://github.com/FutureAtoms/karpathy-ladder, inspected commit 07c7089; MIT, copyright (c) 2026 FutureAtoms.
Borrowed concepts: labelled diagrams, sources versus interpretations, browser-based layout checks. Text and checker are newly authored, not copied or adapted code. If future edits copy substantial upstream material, include the upstream MIT notice and license with those files.
Excluded: video/audio pipelines, automatic font downloads, paid reviewers, global lexicons, punctuation bans and a fixed visual style.
