# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single-page scroll-driven website for Peter van der Spuy (Gulfstream captain, Porsche racer, Camel Safari 911 builder, podcast host), built with the `nateherk-design:scroll-craft` plugin skill. It is a client mock-up being iterated from Peter's feedback. Not a git repo.

**Always invoke the `frontend-design` skill before writing any frontend code.** Then work inside the scroll-craft skill's rules (`SKILL.md` and `references/` in the plugin cache) — they govern devices, cues, grammar, verification and the taste floor.

Skill path: `C:\Users\richa\.claude\plugins\cache\nateherk\nateherk-design\0.3.0\skills\scroll-craft`

## The site lives in one file

`scrollcraft/builds/peter-van-der-spuy/index.html` — all custom CSS in its `<style>`, all markup, and the signature-move JS inline. `scrollcraft.css` / `scrollcraft.js` beside it are the engine, copied verbatim: **never edit them**. Theme through `--sc-*` tokens and drive behaviour through `data-sc-*` attributes only.

`BRIEF.md` in the same folder is the design brief (journey, feeling curve, peak, signature move). `scrollcraft/FINGERPRINTS.md` is the build registry — append, never rewrite rows.

## Commands

Run from `scrollcraft/builds/peter-van-der-spuy/`. `SKILL` below = the skill path above.

```bash
node $SKILL/scripts/doctor.mjs                                   # preflight (ffmpeg/playwright/key/workspace)
node $SKILL/scripts/serve.mjs --root . --port 4500 &             # dev server → http://localhost:4500
node $SKILL/scripts/shoot.mjs --url http://localhost:4500 --out lab/<name>                         # desktop verify
node $SKILL/scripts/shoot.mjs --url http://localhost:4500 --out lab/<name> --width 390 --height 844 # mobile
node $SKILL/scripts/shoot.mjs --url http://localhost:4500 --out lab/<name> --reduced-motion
```

- Never screenshot a `file:///` URL; always serve. Check `curl -s -o /dev/null -w "%{http_code}" http://localhost:4500/` before starting a second server.
- `shoot.mjs` writes `lab/<name>/NN.png` + `report.json`. Read the PNGs with the Read tool; query `report.json` (per-frame `cues`, `contrast`, `act`) with Python to find a frame by its text.
- **Always run desktop + mobile after any layout/cue change, and fix before reporting.** Do at least two look-and-fix rounds; do not stop after one pass.

**Python:** `python` resolves to the Windows Store stub. Use `C:/Users/richa/AppData/Local/Programs/Python/Python312/python.exe` from Bash, or `py -3` from PowerShell. PIL, numpy, onnxruntime are installed.

**Environment limits (don't work around silently — say so):** no full ffmpeg build (contact sheets and video encoding unavailable); no `KIE_AI_API_KEY` (no generated imagery — the build is real-photo only); `rembg` is installed but crashes on import because Application Control blocks `llvmlite.dll` — use `.models/cutout.py` (standalone U2Net via onnxruntime) instead.

## Screenshot workflow (visual self-review)

`shoot.mjs` (above) is the automated device/cue/contrast verifier — it lives in the scroll-craft skill and only understands `data-sc-*` behaviour. `screenshot.mjs` is a separate, simpler tool for the human-eye pass: does this actually look professional. It lives at the **project root**, not in the build folder.

- Puppeteer is a project devDependency (`npm install`, done once at the project root — `puppeteer-core`, not `puppeteer`, so `npm install` does not also pull down a bundled Chromium; the script points at the existing system Chrome install instead).
- **Always screenshot from localhost, from the project root:**
  ```bash
  node screenshot.mjs http://localhost:4500 label
  node screenshot.mjs http://localhost:4500 label --width=390 --height=844   # mobile
  node screenshot.mjs http://localhost:4500 label --viewport-only            # first screen only, default is full-page
  ```
- Refuses any non-localhost URL. Saves to `./temporary screenshots/screenshot-N[-label].png`, auto-incremented, never overwritten.
- After screenshotting, read the PNG with the Read tool — full-page shots of this site are tall; expect one long image per pass, not one per section.
- When reviewing, be specific rather than just "looks good": name the section, the property, and the fix — "the Porsche fact-strip dividers are heavier than the section rule above them", "endurance stat numbers and the video card don't share a baseline". Check spacing/padding, type scale and weight, exact hex against `brand_guidelines.md` §3, alignment, border-radius, shadow consistency (`--pv-shadow` everywhere, nothing flat), image sizing against the quality tiers below.
- Run this after any visual change, alongside `shoot.mjs`, not instead of it. `shoot.mjs` catches contrast and dead-scroll defects; `screenshot.mjs` is for craft.
- **Full-page mode misrepresents `pin`/`pan` sections.** Chrome's full-page capture renders the whole document in one oversized viewport with scroll frozen at 0, so `.sc-stage { position: sticky; top: 0 }` (every pinned or pan act) never actually "sticks" — it just sits at its natural top offset inside its tall spacer, leaving what looks like a dead cream gap below it. This is a screenshot artifact, not a real defect; a real visitor scrolling never sees it, and `shoot.mjs` (which drives real scroll positions) won't report it either. Don't "fix" it. For the hero and the Safari rail specifically, judge them with `shoot.mjs` or `lab/walk.mjs` (interactive `scrollTo`-based, in the build folder) instead of `screenshot.mjs --fullPage`; use `screenshot.mjs` full-page for the static flow sections, where it's accurate.
- **`page.evaluate(() => window.scrollTo(...))` + `setTimeout` is not a reliable way to test scroll-driven behaviour.** Under automation it can leave the engine's rAF-driven state stuck (reads back as if nothing moved, or as leftover state from a previous jump) even though the CSS/JS is correct. This cost real time chasing a phantom "pan rail is broken" bug that didn't exist. For any real scroll-mechanics diagnosis, use Playwright's `browser_run_code_unsafe` with `page.mouse.wheel(0, delta)` in a loop — that's genuine trusted input through the browser's real scroll pipeline, and it's what actually confirmed the pan rail works correctly.

## Reading the verifier

- `CONTRAST FAIL` (<3:1) must be fixed. `CONTRAST THIN` (3–4.5:1) is acceptable **only** for large display headings; on body-size text fix it. Note the harness samples mid-fade frames, so a cue ramping in can read THIN without being a real defect.
- `CUES THAT NEVER PEAK` almost always means the cue window is too narrow for the six-position walk — widen it, don't move it.
- `no dead scroll detected` does not mean no visual gap. Read the frames.

## How the page is put together

- **Grammar (v2):** a filmic hero on an editorial body — a client-directed hybrid, not a scroll-craft grammar. Eight `main > section`s: `pin` (hero), `flow` ×3 (captain, Porsche, endurance), `flow` + `reveal` (Safari photo), `pan` (Safari rail), `flow` (podcast), `flow` close at `min-height: 100svh`. Adjacent flows are deliberate. **Only the hero and the rail are scroll-driven.**
- **Text is static, everywhere.** Peter rejected scroll-gated copy as "faffy" and "jumpy" but wants the site story-heavy. So: no `data-sc-cue`, `data-sc-kinetic` or `data-sc-in` on text, ever; prose is fully present on arrival, one column at 62ch, line-height 1.6. Reveals are for photos only. Don't trim prose to make a section tidy; add a sourced detail if it reads thin.
- **Theme:** cream ground with two dark highlight blocks (`.pv-dark-block` on Endurance and the close). The dark block re-declares the `--sc-*` tokens on its own subtree, so children re-theme automatically. Sections are **painted** with `.pv-cream-block` / `.pv-cream-deep` / `.pv-dark-block` — there is deliberately no `data-sc-drift`, because the skill forbids interpolating cream↔black.
- **Stripe band** (`.pv-band`): the Safari car's graduated livery stripes rendered olive/gold/rust. It is the only section divider (after captain, Porsche, and the rail) and the hero's bottom edge. Never put it inside a section or behind text.
- **Hero:** one whole photo (`assets/hero/edit_v4_preview.jpg`), `data-sc-parallax` on the wrapper, greet-and-hold copy over a bottom scrim. Peter's direction: do not split it into layers. `assets/hero/rider_cutout.png` and `background_plate.jpg` are the abandoned layered version — leave them, don't use them.
- **Flow sections after the pin and the pan** (captain, podcast) carry `.pv-tight-top`; the act's slide-off already costs a viewport, so full section padding on top reads as a dead screen.
- **Signature move:** `#pv-flightlog` stamps a verified fact per section via an IntersectionObserver over `main > section`. The `stamps[]` array in the inline script is **index-aligned with section order** (8 entries; the rail is its own section) — update it whenever a section is added, removed or moved.
- **Never `scroll-behavior: smooth` on `html`.** It queues an animated scroll on top of the engine's own internal lerp (see `scrollcraft.js` — pin/pan progress is already eased), so the two fight each other. This was a real, shipped bug in an earlier pass and was the actual cause of "the gallery scroll isn't working well" — not the pan mechanics themselves, which are correct. If anchor-nav needs a smooth jump, scope it to a click handler on just those links (`el.scrollIntoView({behavior:'smooth'})`), never blanket CSS.
- **Line-art motifs** (`.pv-motif--*`) are hand-authored SVG, sized to actually read at a glance (`.pv-motif` opacity 0.2 cream / 0.3 dark — earlier, lower values were reported as "hardly visible"), one primary motif per section plus supporting detail, none in the podcast-grid or close. Two are geography/place-specific and styled after an old expedition chart (tinted landmass, political borders, a rhumb-line compass rose radiating from one focal point) rather than generic: `--map` is a Southern Africa regional outline with Zimbabwe, Botswana and South Africa labelled (Namibia and Mozambique are shaped but unlabelled; a small closed loop stands in for Lesotho) and the Camelthorn Pathfinders' dashed Zimbabwe-into-Botswana route, per the expedition jacket patch; `--circuit` keeps its original Kyalami-flow shape (long straight, sweeping esses, tight infield) and adds the same rhumb-line device for visual family, labelled KYALAMI / 9HR. Explicitly **not** a surveyed trace of either the borders or the real circuit — decoration that earns its place by being specific rather than generic. Livery *shapes* (stripe band, twin rally lamps, roof-rack lattice, spare-tyre circle) stay in brand colours only. **No teal, no Porsche crest, no Camel Trophy mark** — the marks are third-party trademarks; confirmed with the client.
- **Motifs behind a photo card get hidden, not faded.** `.pv-frame` has an opaque background, so a `.pv-motif` positioned to overlap one is fully covered, not just dimmed — check with `getBoundingClientRect()` on both, don't eyeball it. This bit the Safari map's "ZIMBABWE" label (and, earlier, the whole peak photo's motif) before being caught and repositioned.
- **Eyebrows** only on the captain and Safari sections (skill rule: at most one per three). No em dashes or middle-dot strings in visible copy; `lab/walk.mjs` plus `grep -c '—' index.html` catches regressions.
- `.pv-prose p { margin: 0 }` outranks single-class rules on its children; scope overrides as `.pv-prose .foo`.

## Content rules (from the client)

- Facts only, no hype. Everything on the page is sourced (Porsche Newsroom/Christophorus feature, motorsport.co.za, YouTube descriptions, Peter's own captions). Don't invent numbers, places or dates; a `count` device with an unverified figure is a liability.
- Porsche section is about a *lifetime* in the marque and its community — the dismantled-car-rebuild story was explicitly cut.
- Aviation section leads with "one of the most experienced Gulfstream captains in the world" and global range; Mandela is the payoff, not the premise.
- Endurance (SAES 2023, Dolphin Engineering Juno SS3, co-drivers Byron Mitchell & Nian du Toit, P3 Class A, Nine-Hours of Kyalami) is the section Peter is proudest of — keep it.
- Porsche section has a real photo now (`race-18-crop.jpg`, cropped from a letterboxed source — check `assets/safari/race-18.jpg`'s black bars before reusing it elsewhere). Client asked for a car photo here specifically; swap for a better one if Peter supplies one.
- Close section is content-hugging (no forced `min-height: 100svh`) and the footer is a single slim line — client called both "too thick" and asked them sized to just fit their content. Don't reintroduce full-viewport padding or a stacked multi-line footer.
- Podcast gallery at the bottom uses real YouTube video IDs and `https://i.ytimg.com/vi/<id>/hqdefault.jpg` thumbnails, linking out; check the channel for current episodes before editing the list.

## Images

- `brand_guidelines.md` is the brand source of truth (colors §3, adventure identity §4, voice §5.1). Use those hex values; don't invent brand colors.
- **Quality tiers:** `assets/images/` (client-supplied, ~1130px, proper photography) is the only tier fit for large display. Instagram-sourced material (`assets/safari_raw/`, `assets/inlays/`) is capped at 360×640 — Instagram serves reels at `s640x640` to logged-out viewers and rejects larger variants — so keep those to contained frames, never full-bleed.
- To get Instagram images, pull the `<img src>` from the DOM (Playwright MCP `browser_evaluate`) and download the file; don't screenshot-crop the grid. `assets/safari_raw/_contact.jpg` is a contact sheet of the 24 personal-grid posts.
- Porsche Newsroom press photos are Porsche AG copyright: research only, never site assets.

## Design guardrails

Only animate `transform` and `opacity`; never `transition: all`. Every clickable needs hover, focus-visible and active states. Layered, colour-tinted shadows (`--pv-shadow`), not flat ones. One type family, Archivo: 900 uppercase for display, 400/500/600 for text; never 900 on body copy. Don't add sections or features Peter hasn't asked for; his feedback drives scope.
