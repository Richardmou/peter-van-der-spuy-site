# Blog: adding a new post

This blog is hand-authored static HTML. No build step, no CMS. Every post is
one `.html` file that shares `blog.css` with the listing page.

## Process, episode to post

1. **Fetch the transcript.** Use the `youtube-transcript` skill on the
   episode's YouTube URL. Not every episode has captions available; if the
   fetch fails, try another episode or ask for a transcript/notes directly.
2. **Read the transcript and pull the real story.** Podcast conversation is
   loose and repetitive; the post is not a transcription, it's an edited
   retelling. Keep only what's sourced and factual (numbers, names, places,
   direct quotes), cut filler, profanity, tangents, and anything about a
   third party that wasn't meant to be public (guests sometimes ask to keep
   details anonymous, e.g. an unnamed client, and that should stay unnamed
   in the post too).
3. **Copy `camel-safari-porsche-build.html` as a starting template.** Keep
   the `<head>` structure (title, description, canonical, OG, Twitter card,
   JSON-LD `BlogPosting`) and swap every value for the new post. Use
   `mainEntityOfPage` / `canonical` as `https://petervanderspuy.com/blog/<slug>.html`.
4. **Use real photos already in `../assets/`** (captain, porsche, safari,
   endurance, inlays) rather than anything generated or scraped, per the
   site's real-photo-only rule. Check `../CLAUDE.md` for the asset quality
   tiers before using an Instagram-sourced image full-bleed.
5. **datePublished is the date the post goes live on the site**, not
   necessarily the date the episode aired (we don't always know that from
   the transcript alone, and the site's content rule is never invent a
   date). Update both `datePublished` and `dateModified` in the JSON-LD.
6. **Add the post to `index.html`** (the blog listing) as a new `.db-row`
   under "More episodes" (`.db-entry` is only for the two featured stories at
   the top), and to `../sitemap.xml`. Then relink the chain: every post's
   `.db-post-foot` has Previous / More from the podcast / Next pills in
   blog-index order, so update the new post's neighbours too.
6a. **Give every `<img>` `width`/`height`** (the real file dimensions) and,
   below the post hero, `loading="lazy" decoding="async"`. Spell in
   British/SA English (colour, tyre, metre, licence, organise).
7. **No em dashes, no middle-dot strings, one type family (Archivo).**
   Same rules as the rest of the site (`../CLAUDE.md`). Check with
   `grep -c '—' <file>` before shipping.
8. **Serve and screenshot** before calling it done: `node
   $SKILL/scripts/serve.mjs --root . --port 4500 &` from the build folder,
   then `node screenshot.mjs http://localhost:4500/blog/<slug>.html <label>`
   from the project root, desktop and mobile.
