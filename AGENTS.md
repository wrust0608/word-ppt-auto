# Repository instructions for agents

## Start here

1. Read `HANDOFF.md`.
2. Read the target project's `PROJECT_STATE.md` and artifacts it links.
3. Read `.agents/skills/thesis-research-and-writing/SKILL.md` and only the references routed for the current task.
4. For academic report writing, editing, delegation prompts or review, read `WRITING_POLICY.md` and the project's confirmed `AUTHOR_VOICE.md`. Apply the policy on argument logic, author decisions and accessibility; do not rely only on style lint or claim counts. Pass the policy path to any executor handoff.

## Precedence

Current user request > official institutional rules/templates > locked project decisions > verified evidence/data > research and argument workflow > author voice > linter suggestions.

Never let a style rule alter evidence, numbers, citations, claim boundaries, approved terminology or institutional formatting.

## Writing workflow

- Keep Markdown canonical; generate DOCX only from approved Markdown.
- Do not draft a chapter before its chapter contract and claim matrix are ready.
- Review evidence and logic before editing style.
- Apply `AUTHOR_VOICE.md` only from confirmed samples and author choices.
- Run the Vietnamese style linter after substantive review, not before:

  `uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py <file.md>`

- Treat linter findings as review prompts, not an AI score. Record `FIX`, `KEEP_WITH_REASON` or `FALSE_POSITIVE` in the review report.
- Before publication, run with `--publication --fail-on-error` and complete `PUBLICATION_CHECKLIST.md`.

## Integrity

- Never invent sources, DOI values, pages, data, logs, experiments, quotations, personal experience or author opinions.
- Preserve unresolved labels and record them in `PROJECT_STATE.md`.
- NotebookLM answers are navigation aids; cite the original source.
- Do not use random sentence variation, deliberate errors or detector-targeting tricks.

## Completion

Run:

```powershell
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
```

Update `PROJECT_STATE.md` after a meaningful project change. Do not change a `LOCKED` decision without direct user authorization.
