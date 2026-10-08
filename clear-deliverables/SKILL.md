---
name: clear-deliverables
description: Structure and verify technical deliverables around reader needs. Use when producing or revising structured technical explanations, operational procedures, specifications, handoffs or HTML explanation pages. Not for everyday chat or informal replies.
license: MIT
metadata:
  author: "Hogan Tong"
  version: "1.0.1"
---

# Clear deliverables

By [Hogan Tong](https://github.com/Tonguso).

The core method has no software dependencies. The optional HTML checker requires Python 3.9+, Playwright 1.48+ and its Chromium browser. Rendering other formats requires appropriate local tools.

## Scope and prerequisites
Apply to the requested artifact, not the agent's everyday voice. Preserve the user's language, technical meaning, scope and approvals. Maintenance-manual/STE techniques are optional for technical instructions, not a global English lexicon or a restriction on Chinese punctuation. Do not claim ASD-STE100 compliance without the applicable standard and an actual compliance review.

Before drafting, identify the reader, their decision or task, prior knowledge, output medium and intended viewing sizes. Use supplied requirements; ask only for missing facts that change correctness or consequential scope. Inspect sources and relevant tools before promising verification. Do not infer current access from old results.

## Steps
1. Define the reader's question and the successful outcome. Put the answer, action or governing rule first. Select only the structure needed: explanation, procedure, specification or handoff. See [patterns and checks](references/method.md) for compact templates.
2. Map the content before styling. Each section should answer one reader question. Separate essentials from supporting detail. Give definitions before unfamiliar notation and link prerequisites rather than repeat whole documents.
3. Make statements executable or testable: name the actor, action, object, condition, timing, units and exceptions where relevant. Keep one term for one concept. For procedures include expected results, stop conditions, failure response and safe restart. For specifications distinguish requirements from examples and assumptions. Do not simplify away safety warnings or domain precision.
4. Separate evidence, inference, proposal and unknowns. Keep sources, dates, observation periods and calculation assumptions with the claims they support. Trace material numbers to inputs; qualify causal interpretations. Missing evidence remains missing, not a plausible completion.
5. Add a diagram only when relationships or sequence are clearer visually. Select flow, sequence, state or architecture according to the question. Label arrows with their meaning, payload or condition; name nodes, directions, units and boundaries. Match identifiers to the text. Include failure branches and a text equivalent. Styling is contextual, not a mandated engineering-sheet aesthetic.
6. Review substantive correctness against sources/requirements, then readability in the actual rendered medium. These are separate checks, not a requirement for separate agents or paid reviewers. Fix ambiguous actors, missing units, contradictions, unsupported conclusions and unusable failure paths. Inspect every relevant page/slide/view, including diagram labels at intended size. Re-render changed artifacts and retain exact evidence.

## Medium-specific QA
Use any relevant document, research or design skills already available in the host. No companion skill or named agent tool is required.

- Research: check material claims against opened sources and their context; an excerpt match is not truth verification.
- Slides: preserve requested editability, render with an available compatible application, check overflow and inspect every slide. State renderer limitations; HTML checks do not validate a slide deck.
- Spreadsheets: check formulas, errors, totals and units, and recalculate with a compatible spreadsheet engine when calculations are part of the deliverable. Reading cached values does not prove recalculation. Explanatory clarity does not establish financial correctness.
- Frontend: retain applicable design, accessibility and interaction checks. This skill adds explanatory structure, not arbitrary visual bans.
- HTML: optionally use [HTML checker guide](references/html-checker.md) and `scripts/check_html.py` on trusted self-contained local pages. Inspect screenshots using the host's image-viewing capability. If printing is requested, separately render and inspect print output; the checker does not validate print pagination.

## Acceptance and failure behavior
Before calling a deliverable final, review requirements and sources, inspect relevant rendered views, fix material defects, and confirm the actual output files exist and can be opened with the available file tools or target application. Report the files, actual tests and limitations, not a generic quality certification.

If evidence, rendering or dependencies are unavailable, preserve and label the draft, name the blocked check and next useful step. Follow the host's permissions and the user's existing authorization for dependency setup. Do not silently substitute a format or claim an unperformed test. If the checker flags an intentional layout, inspect it and document a narrowly scoped exception; do not ignore all errors. A checker pass proves only its measured rules, never semantic correctness, full accessibility or production readiness.
