#!/usr/bin/env bun
/**
 * publish.ts - Prepare newsletter content for Nostr publishing
 *
 * Handles mechanical transformations:
 * - Strips YAML frontmatter, extracts title/number
 * - Converts internal links to absolute URLs
 * - Simplifies footer (removes HTML anchor with nostr URI)
 * - Extracts mentioned projects/people from content
 * - Matches mentions against data/npubs.yml
 * - For project npubs: replaces first standalone mention with nostr:npub tag
 * - For dev npubs (mention_only): appends (nostr:npub) after project name
 * - Deduplicates by npub value
 *
 * Usage: bun scripts/publish.ts [path/to/newsletter.md]
 *        If no path given, auto-detects the most recent newsletter.
 *
 * Output: JSON to stdout
 * Warnings: Missing npubs to stderr
 */

import { readFileSync, readdirSync } from "fs";
import { join, resolve } from "path";
import { parse as parseYaml } from "yaml";

const BASE_URL = "https://nostrcompass.org";
const NEWSLETTERS_DIR = resolve(import.meta.dir, "../content/en/newsletters");
const NPUBS_FILE = resolve(import.meta.dir, "../data/npubs.yml");
const BANNER_IMAGE =
  "https://image.nostr.build/fbf98ad0d8f84fd6b60fd920c0364df3549ea7a2e0ca16a159202a2cd87b8baf.png";

// ---------------------------------------------------------------------------
// Load npubs database
// ---------------------------------------------------------------------------

interface NpubEntry {
  npub: string;
  mention_only: boolean; // true = dev account, keep project name + append npub
}

interface NpubMap {
  [name: string]: NpubEntry; // lowercased name -> entry
}

function loadNpubs(): NpubMap {
  const raw = readFileSync(NPUBS_FILE, "utf-8");

  // Parse the YAML file; commented-out entries are not parsed
  const parsed = parseYaml(raw);
  if (!parsed || typeof parsed !== "object") return {};

  const map: NpubMap = {};
  for (const [key, value] of Object.entries(parsed)) {
    if (typeof value === "string" && value.startsWith("npub1")) {
      // Simple string value = project account (replace name with npub)
      map[key.toLowerCase()] = { npub: value, mention_only: false };
    } else if (
      value &&
      typeof value === "object" &&
      "npub" in (value as Record<string, unknown>)
    ) {
      // Object value = may have mention_only flag
      const obj = value as { npub: string; mention_only?: boolean };
      if (typeof obj.npub === "string" && obj.npub.startsWith("npub1")) {
        map[key.toLowerCase()] = {
          npub: obj.npub,
          mention_only: obj.mention_only === true,
        };
      }
    }
  }
  return map;
}

// ---------------------------------------------------------------------------
// Find the most recent newsletter
// ---------------------------------------------------------------------------

function findLatestNewsletter(): string {
  const files = readdirSync(NEWSLETTERS_DIR)
    .filter((f) => f.match(/^\d{4}-\d{2}-\d{2}-newsletter\.md$/))
    .sort()
    .reverse();

  if (files.length === 0) {
    throw new Error("No newsletter files found in " + NEWSLETTERS_DIR);
  }
  return join(NEWSLETTERS_DIR, files[0]);
}

// ---------------------------------------------------------------------------
// Parse frontmatter
// ---------------------------------------------------------------------------

interface Frontmatter {
  title: string;
  date: string;
  [key: string]: unknown;
}

function parseFrontmatter(content: string): {
  frontmatter: Frontmatter;
  body: string;
} {
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) {
    throw new Error("Could not parse YAML frontmatter");
  }
  const frontmatter = parseYaml(match[1]) as Frontmatter;
  return { frontmatter, body: match[2] };
}

// ---------------------------------------------------------------------------
// Extract newsletter number from title
// ---------------------------------------------------------------------------

function extractNumber(title: string): number {
  const match = title.match(/#(\d+)/);
  if (!match) {
    throw new Error(`Could not extract newsletter number from title: ${title}`);
  }
  return parseInt(match[1], 10);
}

// ---------------------------------------------------------------------------
// Convert internal links to absolute URLs
// ---------------------------------------------------------------------------

function convertInternalLinks(body: string): string {
  // Match markdown links with relative paths: [text](/en/...)
  return body.replace(
    /\]\(\/en\//g,
    `](${BASE_URL}/en/`
  );
}

// ---------------------------------------------------------------------------
// Simplify footer
// ---------------------------------------------------------------------------

function simplifyFooter(body: string): string {
  // Replace the HTML anchor sign-off with plain text
  // Pattern: <a href="nostr:npub1...">Reach out via NIP-17 DM</a> or find us on Nostr.
  return body.replace(
    /<a href="nostr:npub[^"]*">Reach out via NIP-17 DM<\/a> or find us on Nostr\./g,
    "Reach out via DM or find us on Nostr."
  );
}

// ---------------------------------------------------------------------------
// Extract mentioned projects and people from newsletter body
// ---------------------------------------------------------------------------

function extractMentions(
  body: string,
  npubs: NpubMap
): {
  found: { name: string; npub: string; mention_only: boolean }[];
  missing: string[];
  mentionString: string;
} {
  const mentionedNames = new Set<string>();

  // Helper: clean a candidate name and decide whether to keep it
  function addIfValid(text: string) {
    text = text.trim();
    // Skip very short names (noise like "Mi", "Go", etc.)
    if (text.length < 3) return;
    // Skip NIP refs, PR numbers, version strings, commit hashes, kind descriptions
    if (/^NIP-|^PR #|^v?\d+\.\d+|^[a-f0-9]{7,}$/.test(text)) return;
    if (/^Kind \d/i.test(text)) return;
    // Skip bare domain names (foo.com, foo.org, etc.)
    if (/^[a-z0-9.-]+\.[a-z]{2,}$/.test(text)) return;
    // Skip all-lowercase multi-word phrases (descriptions, not project names)
    if (/^[a-z]/.test(text) && text.split(/\s+/).length > 1) return;
    // Skip hyphenated repo-style names (marmots-web-chat, etc.)
    if (/^[a-z][a-z0-9]*-[a-z]/.test(text)) return;
    // Skip parenthetical descriptions: "MDK (Marmot Development Kit)"
    // Strip the parenthetical and keep the base name
    const stripped = text.replace(/\s*\([^)]+\)/, "").trim();
    if (!stripped) return;
    // Skip names that are just "polyfill library", "NIPs repository", etc.
    if (/^(polyfill|reference|spec|open|draft)\b/i.test(stripped)) return;
    if (/\b(library|repository|integration|schemata)\b/i.test(stripped) && stripped.split(/\s+/).length > 1) {
      // For compound names like "Nostrability schemata", extract first word only
      // But keep actual project names like "Alby Hub"
      // Heuristic: if the last word is a generic noun, skip it
      const genericSuffixes = /\b(library|repository|integration|schemata|implementation|protocol|SDK|backend|frontend|releases?)\b/i;
      if (genericSuffixes.test(stripped)) {
        // Try to match just the project name from the first capitalized word(s)
        const firstWord = stripped.split(/\s+/)[0];
        if (firstWord && /^[A-Z]/.test(firstWord)) {
          mentionedNames.add(firstWord);
        }
        return;
      }
    }
    mentionedNames.add(stripped);
  }

  // 1. Extract project names from GitHub repo links (not PRs, commits, releases)
  const repoLinkPattern = /\[([^\]]+)\]\(https:\/\/github\.com\/[^/]+\/[^/)]+\)/g;
  let match;
  while ((match = repoLinkPattern.exec(body)) !== null) {
    addIfValid(match[1]);
  }

  // 2. Extract from project website links (top-level domain only, no paths)
  const siteLinkPattern = /\[([^\]]+)\]\(https:\/\/(?:www\.)?([a-z0-9.-]+\.[a-z]{2,})\/?(?:\))/g;
  while ((match = siteLinkPattern.exec(body)) !== null) {
    const domain = match[2];
    if (["github.com", "nostrcompass.org", "testflight.apple.com"].includes(domain)) continue;
    addIfValid(match[1]);
  }

  // 3. Extract project names from H3 section headers
  const headerPattern = /^###\s+(.+)$/gm;
  while ((match = headerPattern.exec(body)) !== null) {
    const fullHeader = match[1].trim();
    if (/^NIP-/.test(fullHeader)) continue;
    // Extract name before action verb, version, or colon
    const nameMatch = fullHeader.match(
      /^(.+?)(?:\s+(?:Ships?|Adds?|Implements?|Releases?|Merges?|Launches?|Fixes?|Receives?|Enables?|Expands?|Extracts?|Gets?|Updates?|Introduces?|Reaches?|Begins?|Gains?|Supports?|Drops?|Brings?|Rolls?|Publishes?|Integrates?|Migrates?|Moves?)\b|\s+v\d|\s+\d+\.\d|:|$)/i
    );
    if (nameMatch) {
      let name = nameMatch[1].trim();
      if (name && !/^NIP-/.test(name)) {
        // If extracted name is still very long (>4 words), it's likely a
        // descriptive header without a verb match. Try first 1-2 words.
        const words = name.split(/\s+/);
        if (words.length > 4 && /^[A-Z]/.test(words[0])) {
          // Take capitalized prefix (e.g. "OpenSats" from "OpenSats Sixteenth Wave...")
          name = words[0];
        }
        addIfValid(name);
      }
    }
  }

  // 4. Deduplicate: merge case variants, prefer the form that appears in npubs.yml
  //    Also normalize: "Igloo for iOS" -> skip, "Frostr Igloo iOS TestFlight" -> "Frostr"
  const normalized = new Set<string>();
  const seenLower = new Set<string>();
  for (const name of mentionedNames) {
    const lower = name.toLowerCase();
    if (seenLower.has(lower)) continue;
    seenLower.add(lower);
    normalized.add(name);
  }

  // 5. Match against npubs database
  const found: { name: string; npub: string; mention_only: boolean }[] = [];
  const missing: string[] = [];
  const seenNpubs = new Set<string>();

  for (const name of normalized) {
    const lower = name.toLowerCase();
    const entry = npubs[lower];

    if (entry) {
      if (!seenNpubs.has(entry.npub)) {
        seenNpubs.add(entry.npub);
        found.push({ name, npub: entry.npub, mention_only: entry.mention_only });
      }
    } else {
      missing.push(name);
    }
  }

  // Sort found by name for stable output
  found.sort((a, b) => a.name.localeCompare(b.name));
  missing.sort();

  // Build mention string: "nostr:npub1... nostr:npub2..."
  const mentionString = found.map((f) => `nostr:${f.npub}`).join(" ");

  return { found, missing, mentionString };
}

// ---------------------------------------------------------------------------
// Inject nostr:npub tags into body text
// ---------------------------------------------------------------------------

/**
 * Inject nostr:npub tags into body text for each mentioned project.
 *
 * Two modes based on npub type:
 * - Project account (mention_only=false): Replace project name with nostr:npub
 *   e.g. "Damus ships..." -> "nostr:npub1... ships..." (renders as "Damus ships...")
 * - Dev account (mention_only=true): Keep project name, append dev npub
 *   e.g. "Coracle 0.6.29..." -> "Coracle (nostr:npub1...) 0.6.29..." (renders as "Coracle (hodlbod) 0.6.29...")
 *
 * Rules:
 * - Only injects the FIRST standalone occurrence per npub
 * - Skips occurrences inside markdown link text [Name](url)
 * - Longer names are replaced first to avoid partial matches
 */
function injectNpubMentions(
  body: string,
  found: { name: string; npub: string; mention_only: boolean }[]
): string {
  // Sort by name length descending to avoid partial matches
  const sorted = [...found].sort((a, b) => b.name.length - a.name.length);
  const injected = new Set<string>();

  for (const { name, npub, mention_only } of sorted) {
    // Skip if we already injected this npub (deduplicate aliases)
    if (injected.has(npub)) continue;

    const escaped = name.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

    // Pattern with alternation:
    //   Group 1: markdown link text containing the name -> preserve as-is
    //            Matches [... Name ...](url) to avoid injecting inside link brackets
    //   Ungroup: standalone name as whole word -> inject
    const pattern = new RegExp(
      `(\\[[^\\]]*${escaped}[^\\]]*\\]\\([^)]+\\))|\\b${escaped}\\b`,
      "g"
    );

    let replaced = false;
    body = body.replace(pattern, (match, linkGroup) => {
      // Preserve markdown links containing the name
      if (linkGroup) return match;
      // Only inject on the first standalone occurrence
      if (replaced) return match;
      replaced = true;

      if (mention_only) {
        // Dev account: keep project name, append dev npub in parens
        return `${name} (nostr:${npub})`;
      } else {
        // Project account: replace name with npub (renders as project name)
        return `nostr:${npub}`;
      }
    });

    if (replaced) {
      injected.add(npub);
    }
  }

  return body;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

function main() {
  // Parse flags
  const args = process.argv.slice(2);
  const forceMode = args.includes("--force");
  const positionalArgs = args.filter((a) => !a.startsWith("--"));

  const inputPath = positionalArgs[0]
    ? resolve(positionalArgs[0])
    : findLatestNewsletter();

  const raw = readFileSync(inputPath, "utf-8");
  const { frontmatter, body: rawBody } = parseFrontmatter(raw);

  const number = extractNumber(frontmatter.title);
  const title = frontmatter.title;

  // Apply transformations
  let body = rawBody;
  body = convertInternalLinks(body);
  body = simplifyFooter(body);

  // Trim leading/trailing whitespace from body
  body = body.trim();

  // Load npubs and extract mentions
  const npubs = loadNpubs();
  const mentions = extractMentions(body, npubs);

  // Inject nostr:npub tags into body text (replaces first standalone mention)
  body = injectNpubMentions(body, mentions.found);

  // Report found mentions on stderr
  if (mentions.found.length > 0) {
    console.error(`[publish] Found npubs for ${mentions.found.length} projects:`);
    for (const { name, npub, mention_only } of mentions.found) {
      const tag = mention_only ? "[dev]" : "[project]";
      console.error(`  + ${tag} ${name} -> ${npub.slice(0, 20)}...`);
    }
  }

  // Warn about missing npubs on stderr
  if (mentions.missing.length > 0) {
    console.error("");
    console.error(`[publish] MISSING npubs for ${mentions.missing.length} projects:`);
    for (const name of mentions.missing) {
      console.error(`  - ${name}`);
    }
    console.error("");
    console.error("[publish] Add missing npubs to data/npubs.yml and re-run.");
    console.error("[publish] Lookup: njump.me, nostr.band, or project docs.");
    console.error("[publish] Use --force to skip this check.");
  }

  // Output JSON to stdout
  const output = {
    number,
    title,
    image: BANNER_IMAGE,
    body,
    mentions: {
      found: mentions.found,
      missing: mentions.missing,
      mentionString: mentions.mentionString,
    },
  };

  console.log(JSON.stringify(output, null, 2));

  // Exit with code 1 if there are missing npubs (unless --force)
  if (mentions.missing.length > 0 && !forceMode) {
    process.exit(1);
  }
}

main();
