"""Reference secrets resolver — the workspace exemplar.

Copy this `resolve_secret()` pattern into your project (adapt the module location to taste).
It is the canonical implementation of the workspace secrets convention
(~/Developer/the-lodge/conventions/SECRETS_MANAGEMENT.md):

    Secrets live in 1Password, are registered in registry.yaml, and are read ONLY through
    get-secret.sh. Never .env, never a raw `security` (Keychain) or `op` (1Password) call
    in project code.

The resolution order mirrors get-secret.sh itself:
    1. Environment variable  → CI / Docker friendly; short-circuits before any 1Password call
    2. get-secret.sh         → registry-driven 1Password lookup (the primary local path)
    3. Clear error / "" fallback → portable for anyone outside this workspace

Adapted from the `destiny` repo (tools/resolve_build.py), the secrets reference impl.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

# The single resolution entry point. Code never talks to 1Password (`op`) or Keychain
# (`security`) directly — only through this shim, so the whole workspace has one place
# to change when the secrets layer evolves.
GET_SECRET_SH = Path.home() / "Developer" / "the-lodge" / "scripts" / "get-secret.sh"


def resolve_secret(key: str) -> str:
    """Resolve a secret by name: env var first, else the-lodge get-secret.sh (1Password).

    get-secret.sh itself checks the env var before 1Password, so this mirrors the workspace
    convention exactly. Degrades to env-var-only (returns "") when get-secret.sh isn't
    present, keeping the tool portable for anyone outside this workspace.
    """
    val = os.environ.get(key, "").strip()
    if val:
        return val
    if GET_SECRET_SH.exists():
        try:
            out = subprocess.run(
                [str(GET_SECRET_SH), key], capture_output=True, text=True, timeout=30
            )
            if out.returncode == 0:
                return out.stdout.strip()
        except (OSError, subprocess.SubprocessError):
            pass
    return ""


# --- Usage -------------------------------------------------------------------------------
# At the call site, treat a missing secret as a hard, actionable error — don't fail silently:
#
#     api_key = resolve_secret("MYAPP_API_KEY")
#     if not api_key:
#         raise SystemExit(
#             "MYAPP_API_KEY is not set. Add it to 1Password and register it in "
#             "registry.yaml so get-secret.sh can resolve it, or export it as an env var "
#             "for a one-off / CI run."
#         )
#
# Then register the key in ~/Developer/the-lodge/registry.yaml as a `onepassword` artifact
# (vault / item / field / consuming repo) — that's what makes get-secret.sh and lodge-doctor
# aware of it. Ask the user to add the actual secret to the right vault
# (Workspace-PBSWI = work, Workspace-Personal = personal); never store a secret from
# conversation yourself.
