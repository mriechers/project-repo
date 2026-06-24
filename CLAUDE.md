# <!-- TODO: Project Name -->

<!-- One or two sentences: what this project IS and the single governing constraint
     that shapes every decision in it. Lead with that constraint — it's the most
     load-bearing line in this file. (destiny's example: "Bungie's API can't create
     loadout slots, so all loadout application routes through DIM and this tooling
     stays strictly read-only.") Delete this comment once written. -->

## Tech stack

<!-- TODO: language(s), runtime versions, key frameworks/libraries. One line each.
     e.g. Python 3.12, stdlib-first; pytest for tests; no web framework. -->

## Run / build / test

```bash
# TODO: the commands an agent needs to actually run this thing.
# e.g.
#   python -m venv .venv && source .venv/bin/activate && pip install -e .
#   pytest
#   ./tools/<entrypoint> --help
```

## Key paths

<!-- TODO: the 3–6 paths an agent must know to navigate. Point at the entry doc
     (e.g. knowledge/INDEX.md, docs/architecture.md) rather than re-explaining it here. -->

| Path | What lives there |
|---|---|
| `<!-- src/ -->` | <!-- application code --> |
| `<!-- tests/ -->` | <!-- test suite --> |
| `planning/` | Session continuity — read `planning/README.md` first |

## Multi-service note

One project repo MAY contain several services that ship together — a web frontend, a
worker, and a shared library under one repo with **one CI pipeline and one release
cadence**. A cohesive multi-service application is **one project repo**, not many. Reach
for a separate repo (and a coordination/metarepo layer above it) only when services have
genuinely independent remotes, CI, and release cycles. When in doubt, stay monorepo.

## Conventions

This repo follows workspace conventions — **referenced, never duplicated** (see
`~/Developer/the-lodge/conventions/`):

- **Commits** — `<type>: <subject>` + `Agent:` / `Machine:` / `Co-Authored-By: Claude`
  trailers. Enforced by `.githooks/commit-msg`. See `COMMIT_CONVENTIONS.md`.
- **Secrets** — 1Password via `get-secret.sh`, registered in `registry.yaml`. Never
  `.env`, never raw `security`/`op` in code. See `SECRETS_MANAGEMENT.md` and the
  `resolve_secret()` exemplar in `docs/secrets-example.py`.
- **Planning** — `planning/{README,progress,backlog}.md` (or `docs/superpowers/{plans,specs}/`
  if this repo uses superpowers SDD). See `PLANNING_CONVENTIONS.md`.
- **Agent rules** — the five charter rules are pointed to from `.claude/rules/README.md`.

## Agent instructions

- This file (`CLAUDE.md`) is the source of truth; `AGENTS.md` symlinks to it so non-Claude
  harnesses read the same guidance. Add a `GEMINI.md` symlink **only** if this repo invites
  Gemini/Codex work — and if you do, carry the `non-claude-agents` worktree-isolation rule.
- Keep this file lean (**≤120 lines**). Machine-ops runbooks → `docs/`. Conditional or
  specialized procedures → a skill under `.claude/skills/<category>/<name>/SKILL.md`.
  A line that restates a number (port, count) is a staleness liability — point at the
  source instead.
- This is a **project repo** targeting compliance **L2** (L3 once `planning/` is active).
  See `README.md` for the ladder.
