# CLAUDE.md

Bhuvaneswaran P's B2B portfolio: a static one-page site (`index.html`, `styles.css`, `main.js`), on GitHub, auto-deployed by Vercel.

## Start of every session
1. Read `PROJECT.md`. It holds every project detail, decision, link and open TODO.
2. Read the last ~40 lines of `PROMPTS.md` to see what was asked most recently.
3. Never lose session data. Before ending a task, write anything new into `PROJECT.md`: the session log, decisions, facts and TODOs.

## Prompt log
- A `UserPromptSubmit` hook (`.claude/hooks/log-prompt.py`, configured in `.claude/settings.json`) appends every prompt, verbatim and timestamped, to `PROMPTS.md`.
- If the hook isn't active (no new entry appears after a prompt), add the prompt to `PROMPTS.md` by hand in the same format.
- Never edit or delete past entries. The hook redacts obvious tokens, but don't commit secrets: **the GitHub repo is public.**

## How Bhuvanesh prompts (and what he expects)
- Short, lowercase, sometimes typo'd prompts. Read for intent ("componends" = components, "also a local" = also run it locally).
- Often sends follow-ups mid-task. Fold them into the running work rather than restarting.
- Design direction comes as reference screenshots plus "I want in that layout". Match the references closely; don't invent a different style.
- "push" means commit, push to GitHub, confirm the Vercel production deploy is live, and report the URL.
- Wants things done end to end: git, deploy, local server. Report outcomes plainly; flag anything unverified.
- Wants everything recorded in the repo so a new session can pick up without re-asking.

## Workflow
- **Local:** `python3 -m http.server 3000` from the repo root, then open http://127.0.0.1:3000.
- **Deploy:** push to `main`. Vercel (team `bhuvan-s-project`, project `bhuvanesh-portfolio`) builds production automatically. Check it with `vercel ls bhuvanesh-portfolio` and `curl` the live URL in `PROJECT.md`.
- **Manual deploy fallback:** `vercel deploy --prod --yes`. The repo is already linked; add `--scope bhuvan-s-project` if asked.
- **Git:** remote is SSH (`git@github.com:pbhuvaneswaran/bhuvaneshportfolio.git`). HTTPS push has no credentials on this Mac.
- `.vercelignore` keeps `CLAUDE.md`, `PROJECT.md`, `PROMPTS.md`, `docs/` and `.claude/` off the live site. Keep it that way.

## Content rules
- Never invent metrics, testimonials, clients or dates. Use only facts in `PROJECT.md` → "Owner profile", and mark anything unverified.
- LinkedIn blocks automated fetches (HTTP 999). Ask Bhuvanesh to paste profile text instead.

## Design rules
- Every colour and font is a token in `:root` in `styles.css`. Reuse tokens; don't hard-code new colours.
- Keep the bento-board layout and component vocabulary described in `PROJECT.md` → "Design system".
- After visual changes, screenshot with Playwright (Chrome is installed) at 1440×900 and 390×844. Check there's no horizontal scroll and the console has no errors besides the missing `assets/portrait.jpg`.
