# Bhuvanesh Portfolio: Project Record

The single source of truth for this project. Update it at the end of every session (see `CLAUDE.md`).
Prompts are logged verbatim in `PROMPTS.md`.

---

## 1. What this is
- **Goal:** a B2B portfolio site for **Bhuvaneswaran P**, a B2B SaaS SEO content writer and strategist, aimed at SaaS marketing leads who hire content and SEO help.
- **Single job of the page:** show proof of decision-stage SEO content work and get the visitor to email or connect on LinkedIn.
- **Type:** static one-page site (plain HTML/CSS/JS, no build step, no framework).

## 2. Links
| What | Where |
|---|---|
| Live site (production) | https://pbhuvanesh-portfolio.vercel.app |
| Other aliases (team-protected, 302) | https://bhuvanesh-portfolio-bhuvan-s-project.vercel.app, https://bhuvanesh-portfolio-git-main-bhuvan-s-project.vercel.app |
| GitHub repo (**public**) | https://github.com/pbhuvaneswaran/bhuvaneshportfolio |
| Vercel | team `bhuvan-s-project`, project `bhuvanesh-portfolio`, CLI user `pbhuvanesh25-5156` |
| Local preview | `python3 -m http.server 3000`, then http://127.0.0.1:3000 |
| Owner LinkedIn | https://www.linkedin.com/in/pbhuvaneswaran/ |
| Contact email used on site | pbhuvanesh25@gmail.com |

Notes:
- `https://bhuvanesh-portfolio.vercel.app` is **someone else's** project. Don't link to it.
- Per-deployment URLs (`bhuvanesh-portfolio-<hash>-bhuvan-s-project.vercel.app`) return 302 because Vercel protects deployments by default. Use the live site URL above.
- The first production URL, `bhuvanesh-portfolio-eta-taupe.vercel.app`, is **gone** (DEPLOYMENT_NOT_FOUND). Production moved to `pbhuvanesh-portfolio.vercel.app` around when GitHub was connected.

## 3. Owner profile (facts used on the site)
LinkedIn blocks automated reads (HTTP 999), so these come from public search results, gathered 2026-11-09.

**Confirmed**
- 6+ years writing SEO content and strategy for B2B SaaS brands: **Hiver, ClickUp, Plivo, HCLSoftware** (from LinkedIn profile text in search snippets).
- Building **Peach**, an AI search visibility platform.
- LinkedIn post, reshared on StartupTalky, which credits linkedin.com/in/pbhuvaneswaran: "One of my recent blogs for my client ranked #1 on Google. It stayed #1 for 5-6 consecutive weeks. … Then I checked the traffic. Anyway, ranking #1 is nice." Source: https://community.startuptalky.com/discussions/post/one-of-my-recent-blogs-for-my-client-ranked-1-on-google-GhB3tRKQAFU98fC
- Hiver blog bylines (author shown as Bhuvaneswaran P):
  - https://hiverhq.com/blog/servicenow-review
  - https://hiverhq.com/blog/tidio-reviews
  - https://hiverhq.com/blog/nextiva-review
  - https://hiverhq.com/blog/what-is-knowledge-base

**Likely, but needs Bhuvanesh to confirm** (all are on the site)
- More Hiver bylines: dynamics-365-vs-salesforce, drift-vs-intercom, servicenow-pricing, email-project-management.
- A Stackforce profile "Bhuvaneswaran P" (https://www.stackforce.co/talent/6a267a545d68ff3d9b77944c) mentions LinkedIn ghostwriting, SEO articles, landing pages, social media and webinars with sales teams, and ~9 years of experience. Used for the "LinkedIn ghostwriting" and "Landing pages" services.
- An alternate LinkedIn slug appears in search: linkedin.com/in/bhuvaneswaranp-writer (title "Bhuvaneswaran P - AI Learn Circle").

**Written by Claude as draft copy** (Bhuvanesh should edit): the "How I work" steps, the "Why me?" cards, the toolkit list (Ahrefs, Semrush, Search Console, GA4, WordPress, Webflow, ChatGPT, Claude), and the Peach description beyond "AI search visibility platform".

**Unknown, still needed:** photo, job dates, education, certifications, real traffic or pipeline numbers, testimonials or recommendations, location, Peach URL.

## 4. Design brief
- Request: "create a b2b portfolio… take ui components and buttons from here… take these as example, I want in that layout". The "here" link never arrived, so components were taken from the two reference images.
- References (saved in `docs/references/`):
  - `ref-1-numbered-portfolio-grid.png`: a cream editorial deck-style grid with numbered sections (01 About me … 13 Why me, Thank you), skill tiles with rings, a "What I do" icon row, a work-process step row, and a "Why me" card grid.
  - `ref-2-social-media-manager-bento.png`: a "Jade Tan – Social Media Manager" bento board: maroon and white panels on black, a heavy condensed headline with a script word over a circular portrait cutout, a top nav, ••• dots on panels, staggered white qualification pills, stat pills, a "My work includes" image grid and case-study boxes.
- **Borrowed from ref 2:** board layout, colour scheme, hero composition, nav style, ••• panel chrome, staggered pills, stat pills, case-study maroon boxes.
- **Borrowed from ref 1:** numbered sections, tool tiles, process step row, "Why me" 6-card grid, "Thank you" closing panel.

## 5. Design system
**Colour tokens** (`styles.css` `:root`)
| Token | Hex | Use |
|---|---|---|
| `--wine` | #5A1219 | maroon panels, headlines on white |
| `--wine-deep` | #3B0A0F | text on white, hover |
| `--frame` | #140E0F | page board behind panels |
| `--paper` | #FFFFFF | white panels |
| `--blush` | #F5E6E3 | soft fills, thumbnails |
| `--blush-line` | #EAD3CF | outlines |
| `--ink` | #2A1A1C | body text |
| `--muted` | #6F5B5D | secondary text |
| `--peach` | #F6B796 | **only** the Peach panel and its dot |

**Type**
- Anton: display headlines (uppercase, condensed).
- Mrs Saint Delafield: script accents ("Strategist", "Peach", "Thank you").
- Instrument Serif italic: section numbers (01–08), "BP" monogram, quotes.
- Montserrat 400–700: body, nav and buttons.

**Components**
- Panels: 6px radius, ••• dots top-right (`.panel::after`), variants `--paper`, `--wine` and `--peach`.
- Buttons `.btn`: pill shape, 48px tall. `--solid` and `--ghost`, plus `--sm` and `--lg`. Colours flip on wine panels. Press scale is .97; arrow icons nudge on hover.
- Chips `.chip` with `aria-pressed` (article filters), tag pills `.tags`, stat pills `.stats`, staggered brand pills `.pill`, tool tiles `.tool__mark`, the copy-email pill `.copyrow`.
- Thumbnails in "What I do" are CSS/SVG mockups (no stock images): vs-table, topic cluster, AI answer with citations, landing page, LinkedIn post, refresh chart.
- Hero: "SEO CONTENT" sized with container-query units (`cqi`). It splits onto two lines at ≤760px. The portrait circle overlaps the bottom of the headline, the script "Strategist" sits over the portrait, and a hand-drawn arrow follows it.

**Motion**: hero rise and pop, the script "writes in" via clip-path, the arrow draws in, and panels fade up on scroll. All of it is off under `prefers-reduced-motion`.

**Breakpoints**: 1100px (tiles 2-col, steps 3-col), 960px (panels stack), 760px (mobile nav, two-line hero), 420px, 340px.

## 6. Page structure (`index.html`)
| # | Section | id | Panel |
|---|---|---|---|
| – | Hero + nav | `#top` | paper |
| 01 | Who am I | `#about` | wine, span 7 |
| 02 | Written for (brands + byline card) | – | wine, span 5 |
| 03 | What I do (6 services) | `#services` | paper, span 7 |
| 04 | Selected work (8 Hiver articles + filters) | `#work` | paper, span 5, row-span 2 |
| 05 | How I work (6 steps) | `#process` | paper, span 7 |
| – | Quote strip ("Then I checked the traffic.") + rank card | – | wine |
| 06 | Skills & tools | – | paper, span 6 |
| 07 | Now building: Peach | `#peach` | peach, span 6 |
| 08 | Why me? | – | wine |
| – | Thank you / Contact | `#contact` | paper |

## 7. Files
```
index.html            page markup (content lives here)
styles.css            all styles and tokens
main.js               mobile menu, article filters, copy email, scroll reveal, footer year
assets/               put portrait.jpg here (square, face centred); monogram shows until then
docs/references/      the two design reference screenshots
CLAUDE.md             instructions for Claude sessions
PROJECT.md            this file
PROMPTS.md            verbatim prompt log (auto-appended by hook)
.claude/settings.json UserPromptSubmit hook config
.claude/hooks/log-prompt.py   the hook script
.vercelignore         keeps docs and tooling off the live site
```

## 8. Open TODOs
- [ ] Add photo at `assets/portrait.jpg`.
- [ ] Confirm the four "likely" Hiver bylines; remove any that aren't his.
- [ ] Confirm or replace the toolkit list and the ghostwriting and landing-page services.
- [ ] Paste LinkedIn About, Experience and recommendations so we can add real dates, results and testimonials.
- [ ] Optional: add a custom domain (production is currently `pbhuvanesh-portfolio.vercel.app`).
- [ ] Decide whether the GitHub repo should stay public (`PROMPTS.md` and the docs are visible there).
- [ ] The "take ui components and buttons from here" link was never sent. Ask for it if it still matters.

## 9. Decisions
- 2026-11-09: Plain static site (no framework) for zero-build Vercel hosting.
- 2026-11-09: No fabricated testimonials or metrics; only sourced facts, with unverified items flagged.
- 2026-11-09: Vercel project named `bhuvanesh-portfolio`, because the folder name has capitals Vercel rejects.
- 2026-11-09: Git remote switched to SSH, since HTTPS had no credentials.
- 2026-11-09: Project docs committed to git but excluded from deploys via `.vercelignore`.

## 10. Session log
### Session 1, 2026-11-09
- Researched the owner (LinkedIn blocked; used search, StartupTalky, the Hiver blog and Stackforce).
- Designed and built the portfolio from the two references, then reviewed it with Playwright screenshots on desktop and mobile. Fixes: hero overlap, column balance, mobile two-line hero, thumbnail overflow.
- `git init`, first commit, and local server on :3000.
- Deployed to Vercel production. Pushed to GitHub over SSH. Bhuvanesh connected the GitHub repo in the Vercel dashboard, so pushes to `main` now auto-deploy.
- Added `CLAUDE.md`, `PROJECT.md`, `PROMPTS.md`, the prompt-logging hook, `.vercelignore` and the reference images.
- First Git-triggered production deploy succeeded (commit 4a873a5). Verified that docs and tooling return 404 on the live site.
