# Recipe: instantiate this template for your project

From "I copied the template" to "an agent can pick this repo up cold and be productive."
Plan for a 20–40 minute first pass; defer optional slots (CI tiers, skills) until you
actually have something to wire them to. Resist over-documenting — a project repo earns L2
with a single screen of `CLAUDE.md`.

## Before you start

Have a one-sentence answer to: **what is this project, and what is the single governing
constraint that shapes it?** That sentence is the first line of `CLAUDE.md`. If you can't
write it yet, you're not ready to scaffold.

## Step 1 — Copy the template into place

```bash
cd ~/Developer
cp -R the-lodge/templates/project-repo my-project
cd my-project
rm -rf .git && git init && git branch -m main
```

## Step 2 — Fill `CLAUDE.md`

Open `CLAUDE.md` and fill every `<!-- TODO -->`:

1. **Project name + governing constraint** (the first line — the most load-bearing in the file)
2. **Tech stack** — languages, runtime versions, key frameworks
3. **Run / build / test** — the actual commands an agent runs
4. **Key paths** — the 3–6 paths to navigate; point at an entry doc rather than re-explaining
5. Keep the **multi-service note** if relevant; the **conventions** and **agent-instructions**
   sections ship correct — leave them.

Stay under ~120 lines. Machine-ops runbooks go in `docs/`; conditional procedures become a
skill. Don't restate numbers that live elsewhere.

## Step 3 — Enable the `AGENTS.md` symlink + commit-msg hook

The template ships `AGENTS.md` as a symlink to `CLAUDE.md`. Verify it survived the copy
(some flows drop symlinks):

```bash
ls -la AGENTS.md          # should show: AGENTS.md -> CLAUDE.md
ln -s CLAUDE.md AGENTS.md # recreate if missing
```

Add a **`GEMINI.md` symlink only if** this repo invites Gemini/Codex work — and if you do,
carry the `non-claude-agents` worktree-isolation rule (a non-Claude agent must work in its
own worktree, never commit to `main` directly).

Wire the commit-msg hook (it delegates to the workspace canonical hook, no-op if absent):

```bash
chmod +x .githooks/commit-msg
git config core.hooksPath .githooks
```

## Step 4 — Wire CI when (and only when) a suite exists

`.github/workflows/ci.yml` ships the **floor secret-scan** job on always — leave it on.
When you have a real test suite, uncomment the language-tier block (python / node) that
matches your stack and adjust the install/lint/test commands. Don't uncomment a stub before
the suite exists — a job that does nothing reads as green coverage that isn't there.

## Step 5 — Register secrets (if any)

Never put a secret in a file. For each API key:

1. Ask the user to add it to the right 1Password vault (`Workspace-PBSWI` = work,
   `Workspace-Personal` = personal).
2. Register it in `~/Developer/the-lodge/registry.yaml` as a `onepassword` artifact.
3. Read it via the `resolve_secret()` pattern in `docs/secrets-example.py` — copy that into
   your code. Never call `security`/`op` directly.

If your repo has no code that reads secrets, delete `docs/secrets-example.py`.

## Step 6 — Set up planning + write the first entry

`planning/{README,progress,backlog}.md` ship as minimum scaffolding (L3). Fill the
`README.md` "Current State" / "Last Session" blocks and write your first `progress.md` entry
at the end of session one.

**Superpowers alternative:** if this repo uses spec-driven development, `docs/superpowers/
{plans,specs}/` is an accepted planning home instead — reduce `planning/README.md` to a
one-line pointer to it rather than running two substrates.

## Step 7 — Skills (when you have one)

Canonical placement is `.claude/skills/<category>/<name>/SKILL.md` (the `.gitkeep` reserves
the tree). Once the marketplace lands (Phase 3), each skill carries `maturity: rnd|stable`
frontmatter. Don't put skills at root `skills/` — they won't deploy to `~/.claude/skills/`.

## Step 8 — First commit

```bash
git add -A
git commit   # the hook validates the message; include the trailers below
```

```
feat: initialize my-project

Agent: <agent-name> (Claude)
Machine: <hostname -s>

Co-Authored-By: Claude <noreply@anthropic.com>
```

Then create the remote (`gh repo create mriechers/my-project --private --source=. --push`)
when you're ready to publish.

## Delete the placeholder / example files once real

These ship as teaching artifacts. Replace them — they shouldn't live alongside real content:

| Placeholder / example | Delete or replace after | Replacement |
|---|---|---|
| `<!-- TODO -->` blocks in `CLAUDE.md` | Step 2 | Your real project content |
| `docs/secrets-example.py` | Step 5 | Your own `resolve_secret()` call site (or delete if no secrets) |
| `.claude/skills/.gitkeep` | Step 7 | Your first real skill under `.claude/skills/<category>/` |
| `.claude/rules/README.md` | Post-Phase-3 | The installed charter-package dependency |
| Commented CI tier stubs | Step 4 | Uncommented language job(s) for your stack |
| `planning/` TODO blocks | Step 6 | Your real current-state + first progress entry |

---

*A project repo targets L2 by default, L3 once `planning/` is active. See
[`README.md`](./README.md) for the ladder and `~/Developer/the-lodge/conventions/
REPO_SETUP_AND_STANDARDS.md` for the full standard.*
