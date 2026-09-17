# Fingerprints

Every site you build with **scroll-craft** gets one row here, appended after it
ships. The registry exists so your next build can prove it is a different page
rather than a re-skin of one you already made.

This file is **yours**. It starts empty on purpose: the gate is about not
repeating *yourself*, so it has nothing to say until you have built something.

The rules and the gate live in the skill's
`references/uniqueness.md`. Short version:

**A new build must differ from EVERY row below on at least 4 of the 6
dimensions.** Four against each row individually, not four on average across the
table. If a planned build fails, change the plan. Never edit a row to make room
for it.

The six dimensions are: **grammar**, **nav treatment**, **hero device**,
**act-sequence shape**, **close pattern**, **signature move**.

Dimension 6 is free, because a signature move is unique by definition. So the
gate really asks for three more out of the remaining five, and a build that
changes only grammar and world will fail it.

---

## The registry

| Build | Grammar | Nav treatment | Hero device | Act-sequence shape | Close pattern | Signature move | World | Port |
|---|---|---|---|---|---|---|---|---|
| peter-van-der-spuy | Filmic one-shot | Fixed minimal bar: wordmark + one CTA ("Follow the Journey") | Pinned full-bleed single real photo (whole image, single-plane parallax, no video, no cutout layers) with greet-cue kinetic headline | 9 sections: pin, flow, pin, flow, pin(framed reveal), pan, pin(+count), flow(grid), pin(+pointer) — ~19vh total | Pinned spotlight stage, two CTAs (primary accent + ghost), footer inside the stage | Flight-log placard: fixed bottom-left badge that stamps a real, verified fact (date/place/number) per act via IntersectionObserver, reading `--sc-p`-independent scroll position rather than engine events | Cream editorial ground with two dark highlight blocks (endurance, close) and burnt-rust accent throughout; adventure/motorsport biography — aviation, Porsche, African rally, endurance racing, podcast | localhost:4500 (dev only) |
| peter-van-der-spuy v2 | Editorial body with a filmic hero (client-directed hybrid: Peter rejected scroll-gated text as "faffy" but wanted the story kept whole) | Fixed cream bar: wordmark, five section anchors, one rust CTA | Pinned full-bleed photo, greet-and-hold copy, livery stripe band as its bottom edge | 8 sections `pin, flow, flow, flow(dark), flow+reveal, pan, flow, flow-hold`; adjacent flows are deliberate; ~15vh | Dark flow block at `min-height: 100svh`, centred, two CTAs, two-line footer inside; no magnet, no spotlight | Flight-log placard stamping a verified fact per chapter (carried over from v1); the livery stripe band as the only section divider | Same world as v1, long-form magazine read; single family Archivo | localhost:4500 (dev only) |

---

## What is taken

Add a bullet here whenever a build claims something a later build should avoid
reusing: a grammar, a nav treatment, a close pattern, a signature move, an
act-count-and-length band. The shared columns are what the next build inherits
as a constraint, so writing them down is the whole point.

- **peter-van-der-spuy** takes: filmic one-shot as a photo-parallax hero (no video/scrub anywhere on the page); the "flight log" stamped-placard signature move; a fixed-bar-plus-spotlight-close pairing. A later build should reach for a different grammar, a different signature-move category (not another persistent stamped rail), and a different close pattern before it can pass the gate against this row.
- **peter-van-der-spuy v2** takes: the "filmic hero on an editorial body" hybrid; a three-stripe graduated band (derived from a client's own vehicle livery) as the sole section divider; a five-anchor cream bar; a dark `100svh` flow close. Shares the flight-log move and the world with v1 (superseded, row kept). Note for future builds: this hybrid was a client redirect, not a chosen grammar; don't reach for it by default.

---

## Appending a row

After shipping, add one line to the table and one bullet to **What is taken** if
the build claimed something new. Fill every column. Say what the build shares
with existing rows.

Rows are append-only. A build that has been superseded stays in the table,
because the space it occupies is still occupied.

---

## Worked example

The skill's author kept a registry of twelve builds across eight page grammars.
If you want to see what a filled-in table looks like, and which shapes tend to
collide, read `EXAMPLES.md` in the scroll-craft repository. Treat it as
illustration only: those rows are somebody else's builds and they do **not**
constrain yours.
