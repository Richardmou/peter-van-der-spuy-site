#!/usr/bin/env node
/**
 * Quick visual-review screenshots for this project.
 *
 * node screenshot.mjs <http://localhost:PORT/path> [label] [--width=1440] [--height=900] [--viewport-only]
 *
 * - Refuses non-localhost URLs (this is for reviewing our own dev server, not
 *   fetching arbitrary pages).
 * - Saves to ./temporary screenshots/screenshot-N.png (or -N-label.png),
 *   auto-incremented, never overwritten.
 * - Full-page by default (the whole scrollable page in one image); pass
 *   --viewport-only to capture just the first screenful instead.
 * - Uses puppeteer-core against the system Chrome install, so `npm install`
 *   does not also pull down a bundled Chromium.
 */
import puppeteer from "puppeteer-core";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const OUT_DIR = path.join(__dirname, "temporary screenshots");

const CHROME_CANDIDATES = [
  "C:/Program Files/Google/Chrome/Application/chrome.exe",
  "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
  process.env.LOCALAPPDATA ? path.join(process.env.LOCALAPPDATA, "Google/Chrome/Application/chrome.exe") : null,
].filter(Boolean);

function findChrome() {
  for (const p of CHROME_CANDIDATES) if (fs.existsSync(p)) return p;
  throw new Error(
    "Could not find a system Chrome install. Checked:\n" + CHROME_CANDIDATES.map((p) => "  " + p).join("\n")
  );
}

function parseArgs(argv) {
  const flags = {};
  const positional = [];
  for (const arg of argv) {
    const m = arg.match(/^--([\w-]+)(?:=(.*))?$/);
    if (m) flags[m[1]] = m[2] ?? true;
    else positional.push(arg);
  }
  return { flags, positional };
}

function nextIndex() {
  fs.mkdirSync(OUT_DIR, { recursive: true });
  const existing = fs.readdirSync(OUT_DIR).filter((f) => /^screenshot-(\d+)/.test(f));
  const nums = existing.map((f) => Number(f.match(/^screenshot-(\d+)/)[1]));
  return nums.length ? Math.max(...nums) + 1 : 1;
}

async function main() {
  const { flags, positional } = parseArgs(process.argv.slice(2));
  const [url, label] = positional;

  if (!url) {
    console.error("usage: node screenshot.mjs <http://localhost:PORT/path> [label] [--width=1440] [--height=900] [--viewport-only]");
    process.exit(1);
  }

  let parsed;
  try {
    parsed = new URL(url);
  } catch {
    console.error(`Not a valid URL: ${url}`);
    process.exit(1);
  }
  if (!/^(localhost|127\.0\.0\.1)$/.test(parsed.hostname)) {
    console.error(`Refusing non-localhost URL: ${url}\nThis tool is for reviewing our own dev server, not fetching third-party pages.`);
    process.exit(1);
  }

  const width = Number(flags.width || 1440);
  const height = Number(flags.height || 900);
  const fullPage = !flags["viewport-only"];

  const executablePath = findChrome();
  const browser = await puppeteer.launch({ executablePath, headless: true });
  try {
    const page = await browser.newPage();
    await page.setViewport({ width, height, deviceScaleFactor: 1 });
    await page.goto(url, { waitUntil: "networkidle0", timeout: 30000 });
    // let webfonts/late layout settle
    await new Promise((r) => setTimeout(r, 400));

    if (fullPage) {
      // A full-page screenshot resizes the viewport to content height right
      // before capturing, with no scroll in between. Anything with
      // loading="lazy" below the original fold never enters the viewport
      // under that path, so its fetch never fires (not a failed load, an
      // unsent one) and it paints as a blank box. Jumping straight to the
      // bottom puts everything in range at once; then poll until every
      // image actually finishes decoding rather than guessing a fixed
      // delay; a bundled step-scroll with a short per-step wait timed out
      // some images without a fixed relationship to page depth, so don't
      // reintroduce that.
      await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight));
      await page.waitForFunction(
        () => Array.from(document.images).every((img) => img.complete),
        { timeout: 8000 }
      ).catch(() => {}); // best-effort: proceed with whatever loaded in time
      await page.evaluate(() => window.scrollTo(0, 0));
      await new Promise((r) => setTimeout(r, 200));
    }

    const n = nextIndex();
    const suffix = label ? `-${label}` : "";
    const filename = `screenshot-${n}${suffix}.png`;
    const outPath = path.join(OUT_DIR, filename);
    await page.screenshot({ path: outPath, fullPage });

    console.log(outPath);
  } finally {
    await browser.close();
  }
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
