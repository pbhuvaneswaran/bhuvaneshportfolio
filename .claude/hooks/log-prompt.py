#!/usr/bin/env python3
"""UserPromptSubmit hook: append every prompt, verbatim, to PROMPTS.md.

- Prints nothing: stdout from a UserPromptSubmit hook is injected into Claude's context.
- Never blocks the prompt: any failure exits 0 silently.
- Redacts obvious secrets (GitHub/OpenAI/Slack/Vercel-style tokens) before writing,
  because this repo is public.
"""
import json
import os
import re
import sys
import time
from pathlib import Path

SECRET = re.compile(r"(ghp_|gho_|ghs_|github_pat_|sk-|xox[abprs]-|vercel_)[A-Za-z0-9_\-]{12,}")


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    prompt = (data.get("prompt") or "").rstrip()
    if not prompt.strip():
        return
    root = (
        os.environ.get("CLAUDE_PROJECT_DIR")
        or data.get("cwd")
        or str(Path(__file__).resolve().parents[2])
    )
    log = Path(root) / "PROMPTS.md"
    prompt = SECRET.sub("[REDACTED-SECRET]", prompt)
    stamp = time.strftime("%Y-%m-%d %H:%M %Z")
    sid = (data.get("session_id") or "")[:8]
    quoted = "\n".join(("> " + line) if line else ">" for line in prompt.splitlines())
    with log.open("a", encoding="utf-8") as f:
        f.write(f"\n### {stamp} · session `{sid}`\n{quoted}\n")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
