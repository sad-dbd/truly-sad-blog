# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Static HTML/CSS/vanilla JS artist site for S.AD (Adam Duers Shepard), deployed via GitHub Pages at trulysad.com. No build system, no npm, no framework — edit files and push.

To preview locally: `python3 -m http.server 8000` from the repo root, then open `http://localhost:8000`.

## Structure

Every page is a self-contained HTML file. Shared stylesheet: `assets/sad.css`. No templating — nav and footer are copy-pasted into each page.

Pages:
- `/` — home with hero and recent releases
- `/releases/` — full discography with tab-filtered views (All / Singles / Projects / Playlists)
- `/untitled/` — notes/blog posts
- `/studios/` — SAD Studios content
- `/lyrics/{track}/` — per-track lyrics page with fixed Apple Music player bar
- `/legacy/` — archived older content
- `/404.html` — custom 404

## Conventions

**Nav active state:** On each page, the active nav link uses `class="nav-link active href="..."` — note the missing closing quote on `class`. This is a pre-existing HTML bug consistent across all pages; don't fix it unless asked, and replicate the pattern if adding new pages to match existing files.

**Lyrics pages:** Place `.player-bar` div with Apple Music embed inside `.lyrics-wrap`, after `.lyrics-dsp-section`. See `lyrics/anon/index.html` as the template.

**New release:** Add a `.rc` card to both `#tab-all` and the relevant filtered tab panel in `releases/index.html`. Cover art goes in `assets/` as `sad_{slug}_cover_400x400.webp`. Update the "Recent releases" rows on `index.html` to reflect the latest three.

## Design system

Defined in `assets/sad.css` via CSS custom properties:

```
--white / --off-white / --dim / --muted / --faint / --fainter / --bg (black)
--font-sans: DM Sans  |  --font-mono: DM Mono
```

All interactive elements (links, rows, tabs) use `transition: var(--ease)` (0.18s ease). Hover states shift color toward `--white`. The aesthetic is minimal monochrome — no color, heavy use of monospace labels at 0.6rem with letter-spacing.

## Project context

Artist site for S.AD — rapper based in Auckland, New Zealand. Released catalogue:
- ANON (30 Apr 2025) — Single
- Faded (14 Jun 2025) — Single
- & (01 Sep 2025) — Single
- Morals (01 Oct 2025) — Single
- Doomed (20 Dec 2025) — Single
- Lo, Doomed & Faded (31 Dec 2025) — Album (7 tracks, 2 album-only)

## Known issues to fix

- Nav active state has a malformed class attribute across all pages — fix it
- Apple Music embed URLs on lyrics pages need verifying (format may need track-level not album-level ID)
- Collections nav link on mobile menu may have alignment issues
- Footer copyright symbol may be missing (was © 2023–2026 SAD VENTURES LIMITED)

## Assets

All cover art in assets/ as WebP 400x400. Playlists and Studios artwork are JPG/PNG.
robots.txt blocks all major AI training crawlers while allowing Googlebot.