# Agent Skills

Reusable instructions and resources for AI agents. Each skill explains what it does, when to use it, and how to carry out the task.

## Skills

- [Clear deliverables](clear-deliverables/SKILL.md): structure technical explanations, procedures, specifications and handoffs around reader needs; verify evidence and rendered readability. Includes an optional offline HTML layout checker.
- [Basket reverse engineering](basket-reverse-engineering/SKILL.md): infer a stock basket’s themes, selection logic, filters, and thesis.
- [Quant literature research](quant-literature-research/SKILL.md): verify quantitative finance sources, assess replication and implementation evidence, and prepare a backtest handoff. Requires web search and source access.

- [Daily US market recap](daily-us-market-recap/SKILL.md): write verified, client-ready US closing notes in English or Chinese, covering market moves, industry divergence and upcoming catalysts.

- [Talk like a human being](talk-like-a-human-being/SKILL.md): guide everyday agent communication in English or Chinese with natural wording and factual precision.

- [Excel workbooks](xlsx/SKILL.md): build, edit and audit Excel workbooks and financial models with live formulas, safe edits to other people's files, and recalculation checks before delivery. Needs Excel on Windows for files with charts, pivots or macros.

## Adding a skill

Create a directory named for the skill and add a `SKILL.md` file. Use YAML frontmatter for the skill’s `name` and `description`, followed by Markdown instructions. Add supporting files only when needed. See the [Agent Skills specification](https://agentskills.io/specification).

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
