# Prompt log

Every prompt Bhuvanesh gives, verbatim (typos included), so no session context is lost.
Since session 1, a hook (`.claude/hooks/log-prompt.py`) appends new prompts automatically at the bottom of this file.
Outcomes and decisions are recorded in `PROJECT.md` → "Session log".

> Note: the GitHub repo is public, so this file is public too. The hook redacts obvious tokens; don't paste secrets.

---

## Session 1, 2026-11-09 (logged by hand)

### 1
> these are my details- https://www.linkedin.com/in/pbhuvaneswaran/
>
> create a b2b portfolio for myself,
>
> take ui componends and buttons from here
>
> take these as example, I want in that layout
> [Image 1] [Image 2]

Attached images are saved as `docs/references/ref-1-numbered-portfolio-grid.png` and `docs/references/ref-2-social-media-manager-bento.png`. No "here" link was included.
→ Researched the profile and built `index.html`, `styles.css` and `main.js` in the bento layout.

### 2
> i need it to be in git and vercel

→ `git init`, committed, deployed to Vercel production.

### 3 (sent mid-task)
> also a local

→ Local server started: `python3 -m http.server 3000`.

### 4 (sent mid-task)
> git link: https://github.com/pbhuvaneswaran/bhuvaneshportfolio

→ Added the remote, switched to SSH, pushed `main`.

### 5
> i connected

→ Verified that Vercel ↔ GitHub is connected.

### 6
> push

→ Nothing new to push yet; offered to run a test deploy.

### 7
> push, commit and vercel prod push
>
> also create a project md file  and prompts of claude md file, like whatever i give,
> all these project details and prompt details , how i prompt should be stored here, so that a session data never gets lost

→ Created `PROJECT.md`, `CLAUDE.md`, this file, the auto-logging hook and `.vercelignore`. Committed, pushed, and verified the production deploy.

---

## Auto-logged prompts
