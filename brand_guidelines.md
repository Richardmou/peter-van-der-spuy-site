[text](<../Peter W2/CLAUDE.md>)# Peter van der Spuy — Brand Identity Guide

Master reference for Peter's brand identity — channel positioning, the logo,
the visual/color system, brand voice, and an expanded adventure/outdoor
identity — for use across the website and any future brand work. Originally
built from the podcast channel's own production guide; thumbnail-specific
production mechanics have been removed here since they don't apply to the
site, and the adventure/outdoor identity (§4) has been built out to anchor the
broader brand beyond the podcast alone.

Built by scraping the channel's `/videos` tab and individual watch pages with
firecrawl, then parsing the embedded YouTube data with
`tools/parse_youtube_channel_videos.py` and
`tools/parse_youtube_video_details.py`, cross-referenced with the Porsche
Newsroom feature on Peter (Christophorus magazine, 2018) and the public
Instagram profiles for both @peter_vd_spuy and @petervanderspuypodcast.

---

## 1. Identity & Positioning

| | |
|---|---|
| Name | Peter van der Spuy |
| Podcast handle | [@PetervanderSpuyPodcast](https://www.youtube.com/@PetervanderSpuyPodcast) |
| Website | [petervanderspuy.com](https://petervanderspuy.com/) |
| Category | Motorsport / Aviation / Supercars / High-performance mindset |
| Instagram (podcast) | [@petervanderspuypodcast](https://www.instagram.com/petervanderspuypodcast/) |
| Instagram (personal) | [@peter_vd_spuy](https://www.instagram.com/peter_vd_spuy/) |
| Audio | Also distributed on Spotify |

**Channel bio (as published):**

> Motorsport • Aviation • Supercars • High-Performance Mindset
>
> The podcast explores motorsport, aviation, supercars, Endurance racing, sim
> racing & high-performance mindset through conversations with elite
> performers operating at the edge of precision and risk.
>
> Hosted by Peter van der Spuy — South African intercontinental Gulfstream
> business jet captain and motorsport race driver, trusted to fly global
> leaders including Nobel Laureate Nelson Mandela.
>
> Featuring conversations with professional racing drivers, jet pilots,
> supercar builders, endurance athletes, entrepreneurs, adventurers & cultural
> creators.
>
> Topics include:
> • Motorsport & racing drivers
> • Aviation & business jet flying
> • Supercars, Porsche culture & performance engineering
> • Sim racing vs real racing
> • Extreme sports & adrenaline culture
> • Leadership, conservation & performance psychology

**Personal Instagram bio (as published):** "Adventurist. Animal and nature
conservationist, motorsport and aviation junkie, generalist, podcaster."

**Podcast Instagram bio (as published):** "Motorsport, aviation &
adrenaline-driven adventurists, conservation & thrill-seeking stories."

**Host credential taglines** (rotate across copy — pull from this set, or
write a new one in the same register, rather than inventing an unrelated bio
each time):
- "Gulfstream Captain, Race Driver & High-Performance Speaker."
- "South African intercontinental Gulfstream business jet captain and
  motorsport race driver, trusted to fly global leaders including Nobel
  Laureate Nelson Mandela."

**Brand positioning, in one line:** conversations with elite performers
operating at the edge of precision and risk — told through Peter's own
credibility as a pilot and racer, not as a neutral interviewer.

---

## 2. Logo & Visual Mark

Saved locally at `workflows/assets/logo.jpg` (channel avatar, ~900×900).

**Description:** A circular vintage aviation-badge / crest emblem, rendered
in gold-on-black line art — evokes an old military aviator wings badge or a
classic car dashboard medallion. Background illustration is a stylized retro
aircraft instrument panel / control yoke in gold, amber and cream tones on
black. A large pair of ornate gold "wings" spans horizontally behind the
center, reinforcing the aviation theme. Centered on top of the illustrated
badge is a real cutout photo of Peter — smiling, wearing glasses and an olive
cap reading "Aeronautica Militare" (the Italian air force's heritage apparel
line — a small but genuine signal of the aviator-streetwear register the
brand already lives in). Curved white bold caps text follows the top of the
circle ("PETER VAN DER SPUY") and the bottom ("PODCAST"), in a heavy
condensed sans-serif.

**Why this matters for brand work:** the logo's gold/amber-on-black palette is
the *original source* of the brand's orange-on-black color system (§3) —
treat gold/amber and black as the two non-negotiable brand colors for any new
asset, with olive/khaki and rust-orange as supporting neutrals.

---

## 3. Brand Color System

Sampled directly from the logo and existing channel assets.

| Role | Hex | Notes |
|---|---|---|
| Black (primary background / text panels) | `#000000` | Dominant backdrop; also the logo's background |
| Off-white / white (headline, body text) | `#FEFEFE` | Never pure design-tool white — looks slightly warm on screen |
| Brand bright orange (accent) | `#F87840` | Thin accent lines, badges, fill bands — used sparingly |
| Olive / khaki (secondary neutral) | `#7D754E` | Mid-tone band color, the bridge into the outdoor palette in §4.6 |
| Burnt rust orange (alternate solid bg) | `#AA3007` | Full-bleed warm background option |
| Gold/amber (logo) | `#E8A03E`–`#F0B24A` (approx.) | The badge illustration's gold tone — same family as the brand orange, slightly more yellow |

**Pattern: black base + one warm orange/gold accent + olive/khaki as a
tertiary neutral. Never more than 3–4 colors in a single composition.** This
rule carries forward unchanged into the site build.

---

## 4. Adventure & Outdoor Identity

Peter's brand is bigger than the podcast alone: pilot, racer, conservationist,
and now storyteller. This section builds out that fuller identity so the
website reads as "a man who has lived several full lives at the edge," not
just "a podcast host."

### 4.1 Brand pillars

1. **Aviation Command** — two decades as an intercontinental Gulfstream
   captain, flying heads of state and Nobel laureates (Nelson Mandela chief
   among them). Precision, discretion, altitude. The aviator-badge logo and
   the "Aeronautica Militare" cap are real, lived-in signals of this, not
   costume.
2. **Motorsport Precision** — a lifelong Porsche obsessive who built his first
   car from a dismantled wreck before he ever flew commercially. GT-series and
   hill-climb race driver; a six-time Concours-champion 911 (964) cabriolet
   and a 911 GT3 RS in his history. Technical, exacting, "engineer's genes."
3. **Wild Africa** — self-described animal and nature conservationist. The
   Camel Safari Porsche Project — a 911 rebuilt in Camel Trophy-inspired rally
   trim (lifted, roof-racked, Falken Motorsport-shod) for African expedition
   rallying — is the pillar where motorsport and the African bush collide.
   Instagram content backs this up directly: wildlife (a cheetah in the bush),
   desert dune driving, bush/conservation highlight reels.
4. **Adventure Storytelling** — the podcast is the newest pillar, the vehicle
   for finally telling the first three out loud, in conversation with other
   elite performers who operate at the same edge.

### 4.2 Narrative throughline

Peter didn't start as a storyteller — he spent thirty years being the story:
the pilot in the room when history was being negotiated, the driver who built
his own race car by hand before it was his job, the guy who took a Porsche
into the African bush and came back with a rally build nobody else has. The
podcast, and now the site, exist to finally put that in his own words —
against the same standard of precision he's held himself to in a cockpit and
on a track.

### 4.3 Mood & tone descriptors

Rugged, exacting, weathered-but-cared-for, expedition-ready, quietly
world-class, dry humor, understated confidence, "earned, not performed."
Avoid: loud, flashy, try-hard extreme-sports energy, influencer gloss,
generic "adventure brand" stock-photo cheerfulness.

### 4.4 Materials, textures & motifs to draw on

Weathered leather and canvas, brushed/scratched aircraft aluminum, cockpit
instrument dials and toggle switches, roof-rack webbing and jerry cans, race
suit Nomex and helmet foam, khaki and drill cotton, dust and sun-bleached
paint rather than showroom gloss. These are textures to reference in
photography direction and generated-asset prompts (see scroll-craft's
`references/assets.md` style preamble) — not literal graphic patterns to
stamp on the page.

### 4.5 Photography direction

Real, in-situ, unglamorized: the actual cockpit, the actual rally car with
real dust on it, real bush light — not a studio backdrop or a stock adventurer.
This matches the scroll-craft skill's own "photographic unless genuinely
illustrated" default (see `references/worlds.md`) and is reinforced, not
contradicted, by everything sampled from his own Instagram content: handheld,
sun-flared, real-location shots, never posed-studio. Golden hour and hard
desert daylight both appear in his own content — treat both as on-brand rather
than forcing one lighting mood.

### 4.6 Extended outdoor palette

The core system in §3 (black + orange/gold + olive/khaki) already contains the
seed of an outdoor palette in its olive/khaki neutral — this extends it for
uses where the site needs to feel like bush and dust rather than a
podcast-studio badge:

| Role | Hex | Notes |
|---|---|---|
| Sand / dust | `#C9B27F` (approx.) | Desert and rally-dust surfaces; use as a light neutral, not a headline color |
| Deep olive drab | `#4A4934` (approx.) | Darker relative of the existing `#7D754E` khaki, for shadow/depth in bush scenes |
| Weathered gunmetal | `#3A3A38` (approx.) | Aircraft/instrument metal, an alternative dark neutral to pure black for texture-heavy scenes |

**These three are proposed extensions, not sampled from a real photo of the
Camel Safari Porsche** — confirm/adjust against the car's actual livery once
real photos are in hand (see the project plan's asset-sourcing step). Don't
lock them as final brand colors until then.

### 4.7 Iconography & motifs

Aviator wings (already in the logo), a waypoint/compass mark, a thin
topographic contour line, a rally roof-rack silhouette. Use at most one as a
recurring small mark (favicon, section divider, signature-move seed) —
per the skill's own hard rules, this is restraint, not a badge stamped on
every section.

---

## 5. Video Description System

Full descriptions were analyzed from 3 episodes (~6mo, ~9mo, and the
channel's very first episode) via `tools/parse_youtube_video_details.py`,
which extracts `videoDetails.shortDescription` from the page's embedded
`ytInitialPlayerResponse`.

### 5.1 Voice & tone — applies to site copy too

- **Specificity over hype.** The single strongest pattern across every
  sample: concrete facts (numbers, place names, dollar amounts, ages, dates)
  replace generic praise. "20 teenagers," "45.0 hours," "40°C heat" — not "an
  amazing journey." Write from real facts, not filler adjectives. This is the
  single most important voice rule to carry into the website's copy.
- **Curiosity-gap opening.** The first line is always a hook — a rhetorical
  question or a surprising claim — never "In this episode..." Apply the same
  discipline to hero copy and section openers on the site.
- **Third-person narrative voice** for descriptive copy, occasionally breaking
  into direct address for engagement prompts.
- **Warm and respectful register**, even when the subject is a rivalry or a
  debate — never sarcastic, never clickbait-negative.
- **Em dashes used for aside/emphasis** rather than parentheses, consistent
  with the host bio style ("Hosted by Peter van der Spuy — Gulfstream
  Captain...").

### 5.2 Structural template (for episode descriptions, not the site)

```
[1. HOOK — 1–2 punchy questions or a bold claim, no guest name yet.]
[2. SETUP — "In this episode, Peter van der Spuy sits down with [Guest Name]
    (@instagram_handle) to unpack/discuss [topic]..."]
[3. GUEST CONTEXT — 1–2 paragraphs of background, concrete details.]
[4. "Together, Peter [+ guest names] discuss:" — emoji-bulleted list, 5–8 items.]
[5. Optional "Key takeaways:" — 3–5 plain bullets.]
[6. Chapter timestamps — "MM:SS Description", one per line.]
[7. Optional bonus engagement question.]
[8. "🔗 LINKS & RESOURCES" — Instagram handles for guest(s), host, podcast.]
[9. "Featured Guests:" — name + one-line title, per guest.]
["Hosted by Peter van der Spuy — [rotating tagline, see §1]"]
[10. CTA — Like, Subscribe and Share.]
[11. Hashtag block — 10–20 tags, always the last line.]
```

### 5.3 Notes

- Guest Instagram handles are always linked as full URLs, both inline (`@handle`)
  and again in the links section.
- Timestamps format is `MM:SS Description`.
- The channel's very first episode is noticeably shorter and skips several
  sections — treat §5.2 as the matured, current standard, not every episode's
  floor.

---

## 6. Title Patterns

Observed formats (mix and match):
- `[Intriguing hook/outcome] with [Guest Name]` — e.g. "From Simulator to the
  Snake Pit: Inside Formula 1, LeMans & Racing Longevity with Jan Lammers."
- `[Guest Name]'s [notable thing] Story.` / `[Topic]: [Guest tagline]` — e.g.
  "From Teen Author to Cape-to-Cairo Pilot: Megan Werner's Wild Aviation Story."
- `Inside [World/Topic]: [Angle] | [Guest Name]` — pipe-separated variant.
- Multi-part episodes append `Part 1` / `Part 2`.
- Titles almost always end with a period or the guest's full name — rarely a
  question mark.

Useful as the naming convention for any episode links/cards on the site.

---

## 7. Source Data & Tools

- `tools/parse_youtube_channel_videos.py` — extracts the video list (title,
  URL, view count, upload age, thumbnail) from a channel's `/videos` page.
- `tools/parse_youtube_video_details.py` — extracts full description,
  keywords/tags, duration, category, and thumbnail URLs from a single video's
  watch page.
- `workflows/assets/logo.jpg` — the channel's logo/avatar, kept as a
  persistent brand asset.
