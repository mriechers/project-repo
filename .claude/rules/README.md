# Agent rules — charter payload (pending)

This directory holds the small, auto-loaded rule fragments that brief every agent working
in this repo. They are **not authored here** — they ship as a versioned **charter package**
(Phase 3 of the workspace standardization, not yet published). Until then this README is a
placeholder pointing at the canonical set.

The charter package will install five rules, each a few lines that *reference* the full
convention in `~/Developer/the-lodge/conventions/` rather than duplicating it:

| Rule | Enforces |
|---|---|
| `agent-rules` | The core behavioral rules for AI agents |
| `commit-standards` | `<type>: <subject>` + `Agent:`/`Machine:`/`Co-Authored-By:` trailers |
| `secrets-management` | 1Password via `get-secret.sh`; never `.env`, never raw `security`/`op` |
| `non-claude-agents` | Worktree isolation for non-Claude harnesses (carry only if this repo ships `GEMINI.md`) |
| `python-standards` | venv-always, type hints (carry only for Python repos) |

## Until the charter package lands

Don't copy the full rule bodies in here — that recreates the duplication the package exists
to prevent. Reference the source of truth: `~/Developer/the-lodge/.claude/rules/` and
`~/Developer/the-lodge/conventions/`. When the package is published, replace this README
with the installed, version-pinned dependency.

<!-- TODO (post-Phase-3): install the charter package as a dependency and delete this note. -->
