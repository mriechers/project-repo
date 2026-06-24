# project-repo template

The canonical template for a **single-application / service repo** in the `~/Developer`
workspace. Every repo that ships runnable code — a tool, a service, a library, or a cohesive
multi-service app under one CI — instantiates this.

It is deliberately **lean**. A project repo carries the mechanical scaffolding that makes
agents productive and conventions enforceable, and nothing more. Architecture, runbooks, and
specialized procedures live a layer down (in `docs/`, in skills, or in the code itself).

## What you get

| File | Purpose |
|---|---|
| `CLAUDE.md` | Agent entry point — purpose, governing constraint, stack, run commands, conventions (lean, ≤120 lines) |
| `AGENTS.md` → `CLAUDE.md` | Symlink so non-Claude harnesses read the same guidance |
| `.gitignore` | Secrets + OS + Python/Node baseline; TODO for language-specific additions |
| `.githooks/commit-msg` | Clone-portable delegate to the workspace canonical commit hook |
| `.claude/rules/README.md` | Pointer to the five charter rules (installed as a package in Phase 3) |
| `.claude/skills/.gitkeep` | Reserves the canonical skill placement: `.claude/skills/<category>/<name>/SKILL.md` |
| `planning/` | `README` / `progress` / `backlog` — session continuity (L3 substrate) |
| `.github/workflows/ci.yml` | Floor secret-scan (always on) + commented language-tier stubs |
| `docs/secrets-example.py` | The `resolve_secret()` exemplar — env → `get-secret.sh` → clear error |
| `RECIPE.md` | Step-by-step instantiation guide |

## Compliance ladder target

Project repos are graded against the L1–L4 ladder in
`~/Developer/the-lodge/conventions/REPO_SETUP_AND_STANDARDS.md`:

- **L2 (Standard) — the default target.** `CLAUDE.md` + `AGENTS.md` symlink + `.gitignore`
  + `.githooks/commit-msg` with `core.hooksPath` set. This template ships everything for L2.
- **L3 (Active) — add `planning/`.** Once the repo has active development, the `planning/`
  substrate (shipped here) graduates it to L3.

L4 (cross-cutting binding contract) is for risky multi-step domain ops and is out of scope
for a normal project repo.

## Getting started

Follow [`RECIPE.md`](./RECIPE.md). The short version: clone → fill `CLAUDE.md` → enable the
`AGENTS.md` symlink + commit-msg hook → wire CI when tests exist → register secrets → write
your first `planning/progress.md` entry. Delete the placeholder/example files once you have
real ones (see the table in RECIPE).
