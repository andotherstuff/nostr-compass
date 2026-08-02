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
 * - NIP-27 npub injection: places nostr:npub after first markdown link per project
 *   - Project accounts: [Name](url) nostr:npub1...
 *   - Dev accounts: [Name](url) (nostr:npub1...)
 * - Deduplicates by npub value (one injection per npub)
 *
 * Usage: bun scripts/publish.ts [path/to/newsletter.md] [--force]
 *        If no path given, auto-detects the most recent newsletter.
 *
 * Output: JSON to stdout
 * Warnings: Missing npubs to stderr
 */

import { readFileSync, readdirSync } from "fs";
import { join, resolve, dirname } from "path";
import { fileURLToPath } from "url";
import { parse as parseYaml } from "yaml";
import {
  formatNpubMention,
  isOutreachAllowed,
  loadNoDmFromText,
  loadValidatedNpubMapFromText,
  loadUnresolvedFromText,
  type NpubEntry,
  type NpubMap,
  type UnresolvedIdentity,
  type UnresolvedIdentityMap,
} from "./lib/npub-database";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const BASE_URL = "https://nostrcompass.org";
const NEWSLETTERS_DIR = resolve(__dirname, "../content/en/newsletters");
const NPUBS_FILE = resolve(__dirname, "../data/npubs.yml");
const BANNER_IMAGE =
  "https://image.nostr.build/fbf98ad0d8f84fd6b60fd920c0364df3549ea7a2e0ca16a159202a2cd87b8baf.png";

// ---------------------------------------------------------------------------
// Load npubs database
// ---------------------------------------------------------------------------

function loadNpubs(): NpubMap {
  return loadValidatedNpubMapFromText(readFileSync(NPUBS_FILE, "utf-8"));
}

function loadUnresolvedIdentities(): UnresolvedIdentityMap {
  return loadUnresolvedFromText(readFileSync(NPUBS_FILE, "utf-8"));
}

function loadNoDmNpubs(): Set<string> {
  return loadNoDmFromText(readFileSync(NPUBS_FILE, "utf-8"));
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

export function extractMentions(
  body: string,
  npubs: NpubMap,
  unresolvedIdentities: UnresolvedIdentityMap = {},
  noDm: Set<string> = new Set(),
): {
  found: Array<{ name: string } & NpubEntry>;
  outreachRecipients: Array<{ name: string } & NpubEntry>;
  unresolved: Array<{ name: string; record: UnresolvedIdentity }>;
  missing: string[];
  mentionString: string;
} {
  const mentionedNames = new Set<string>();

  const projectSections = new Set([
    "top stories",
    "lead stories",
    "tagged releases",
    "shipping this week",
    "in development",
    "unreleased changes",
    "new projects",
  ]);
  const protocolProjectSections = new Set([
    "protocol work",
    "protocol and spec work",
    "protocol work and nip updates",
  ]);

  let linkSection = "";
  const applicationLines: string[] = [];
  for (const line of body.split("\n")) {
    const h2 = line.match(/^##\s+(.+)$/);
    if (h2) linkSection = h2[1].trim().toLocaleLowerCase();
    if (projectSections.has(linkSection)) applicationLines.push(line);
  }
  const applicationBody = applicationLines.join("\n");

  // Helper: clean a candidate name and decide whether to keep it
  function addIfValid(text: string, fromApplicationHeading = false) {
    text = text.trim();
    // GitHub link labels often use owner/repository; identity records are keyed
    // by the project/repository name rather than the owner prefix.
    if (/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(text)) {
      const parts = text.split("/");
      text = parts[parts.length - 1] || text;
    }
    // Skip very short names (noise like "Mi", "Go", etc.)
    if (text.length < 3) return;
    // Skip NIP refs, PR numbers, version strings, commit hashes, kind descriptions
    if (/^NIP-|^PR #|^v?\d+\.\d+|^[a-f0-9]{7,}$/.test(text)) return;
    if (/^Kind \d/i.test(text)) return;
    // Skip bare domain names (foo.com, foo.org, etc.)
    if (/^[a-z0-9.-]+\.[a-z]{2,}$/.test(text)) return;
    // Skip all-lowercase multi-word phrases (descriptions, not project names)
    if (!fromApplicationHeading && /^[a-z]/.test(text) && text.split(/\s+/).length > 1) return;
    // Skip hyphenated repo-style names (marmots-web-chat, etc.)
    if (!fromApplicationHeading && /^[a-z][a-z0-9]*-[a-z]/.test(text)) return;
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
  while ((match = repoLinkPattern.exec(applicationBody)) !== null) {
    addIfValid(match[1]);
  }

  // 2. Extract from project website links (top-level domain only, no paths)
  const siteLinkPattern = /\[([^\]]+)\]\(https:\/\/(?:www\.)?([a-z0-9.-]+\.[a-z]{2,})\/?(?:\))/g;
  while ((match = siteLinkPattern.exec(applicationBody)) !== null) {
    const domain = match[2];
    if (["github.com", "nostrcompass.org", "testflight.apple.com"].includes(domain)) continue;
    addIfValid(match[1]);
  }

  // 3. Extract project names from H3 section headers, but only inside
  // application sections. Protocol/deep-dive H3s are subjects or chronology
  // labels (for example "Merged" and "July 2026"), not project mentions.
  let currentSection = "";
  for (const line of body.split("\n")) {
    const h2 = line.match(/^##\s+(.+)$/);
    if (h2) {
      currentSection = h2[1].trim().toLocaleLowerCase();
      continue;
    }
    const h3 = line.match(/^###\s+(.+)$/);
    if (!h3 || (!projectSections.has(currentSection) && !protocolProjectSections.has(currentSection))) continue;
    const fullHeader = h3[1].trim();
    if (/^NIP-/.test(fullHeader)) continue;
    // Extract name before action verb, version, or colon
    const nameMatch = fullHeader.match(
      /^(.+?)(?:\s+(?:Ships?|Adds?|Implements?|Releases?|Merges?|Launches?|Fixes?|Receives?|Recovers?|Remembers?|Keeps?|Tightens?|Pairs?|Gives?|Lets?|Clarifies?|Schedules?|Binds?|Turns?|Enables?|Expands?|Extracts?|Gets?|Updates?|Introduces?|Reaches?|Begins?|Gains?|Supports?|Drops?|Brings?|Rolls?|Publishes?|Integrates?|Migrates?|Moves?|Coordinates?|Opens?|Polishes?|Extends?)\b|\s+v\d|\s+\d+\.\d|:|$)/i
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
        // Protocol sections mostly contain spec subjects. Keep only headings
        // that resolve exactly to a curated project identity so a concrete
        // implementation such as Mill receives outreach without treating
        // generic NIP/BUD/NAP headings as projects.
        if (protocolProjectSections.has(currentSection) && !npubs[name.toLowerCase()]) {
          continue;
        }
        addIfValid(name, true);
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

  // 5. Match against npubs database. When aliases share a pubkey, choose the
  // strongest explicit semantic record rather than whichever alias appeared first.
  const foundByNpub = new Map<string, { name: string } & NpubEntry>();
  const unresolved: Array<{ name: string; record: UnresolvedIdentity }> = [];
  const missing: string[] = [];
  const identityPriority = (entry: NpubEntry): number => {
    if (entry.legacy) return entry.mention_only ? 20 : 10;
    switch (entry.identity_type) {
      case "project": return 150;
      case "organization": return 140;
      case "lead-developer": return 130;
      case "maintainer": return 120;
      case "individual": return 110;
    }
  };
  const identityAliases: Record<string, string> = {
    "21meetup 1.1.0": "21meetup",
    "applesauce signers": "applesauce",
    "bitcredit core": "bitcredit",
    "mdk workspace": "mdk",
    "nymchat 1.0.1": "nymchat",
    "primal-android": "primal android",
    "swift-nostr": "swift-nostr-client",
    "zap cooking's frontend": "zap cooking",
  };

  for (const name of normalized) {
    const lower = name.toLowerCase();
    const lookupName = npubs[lower] ? lower : (identityAliases[lower] ?? lower);
    const entry = npubs[lookupName];

    if (entry) {
      const candidate = { name, ...entry };
      const existing = foundByNpub.get(entry.npub);
      if (!existing || identityPriority(candidate) > identityPriority(existing)) {
        foundByNpub.set(entry.npub, candidate);
      }
    } else if (unresolvedIdentities[lookupName]) {
      unresolved.push({ name, record: unresolvedIdentities[lookupName] });
    } else {
      missing.push(name);
    }
  }

  const found = [...foundByNpub.values()];

  // Sort found by name for stable output
  found.sort((a, b) => a.name.localeCompare(b.name));
  unresolved.sort((a, b) => a.name.localeCompare(b.name));
  missing.sort();

  // Build mention string: "nostr:npub1... nostr:npub2..."
  const mentionString = found.map((f) => `nostr:${f.npub}`).join(" ");
  const outreachRecipients = found.filter((entry) => isOutreachAllowed(entry, noDm));

  return { found, outreachRecipients, unresolved, missing, mentionString };
}

// ---------------------------------------------------------------------------
// Inject nostr:npub tags into body text (NIP-27 compliant)
// ---------------------------------------------------------------------------

/**
 * Inject nostr:npub tags into body text for each mentioned project.
 *
 * Per NIP-27, `nostr:npub1...` in content is for rendering (clients show
 * the display name). Placing it next to a markdown link keeps the human-
 * readable name visible while notifying the project/dev.
 *
 * Identity-aware rendering:
 * - Dedicated project or individual account:
 *     `[ProjectName](url) nostr:npub1...`
 * - Personal maintainer/lead-developer account:
 *     `[ProjectName](url) (maintainer Person: nostr:npub1...)`
 *
 * Algorithm:
 * 1. For each project with a known npub, find the FIRST markdown link
 *    whose text contains the project name: `[...Name...](url)`
 * 2. Insert the npub RIGHT AFTER the link's closing `)`
 * 3. If no markdown link found, find the first bare-text mention
 *    (NOT in a `### ` header line, NOT inside `[...]()`) and inject after it
 * 4. Never inject in header lines
 * 5. Never inject inside link brackets
 * 6. Only inject once per npub (first occurrence wins)
 */
function injectNpubMentions(
  body: string,
  found: Array<{ name: string } & NpubEntry>
): string {
  // Sort by name length descending to avoid partial matches
  // (e.g. "Primal Android" before "Primal")
  const sorted = [...found].sort((a, b) => b.name.length - a.name.length);
  const injected = new Set<string>();

  // Split body into lines for line-level analysis
  let lines = body.split("\n");

  for (const entry of sorted) {
    const { name, npub } = entry;
    // Skip if we already injected this npub (deduplicate aliases)
    if (injected.has(npub)) continue;

    const escaped = name.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const npubTag = formatNpubMention(entry);

    // --- Strategy 1: Find first markdown link containing the name ---
    // Match: [text containing Name](url)
    // The name must appear in the link text portion (between [ and ])
    const linkPattern = new RegExp(
      `(\\[[^\\]]*${escaped}[^\\]]*\\]\\([^)]+\\))`,
      "i"
    );

    let didInject = false;

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];

      // Never inject in header lines
      if (/^#{1,6}\s/.test(line)) continue;

      const linkMatch = linkPattern.exec(line);
      if (linkMatch && linkMatch.index !== undefined) {
        // Insert npub tag right after the matched link's closing )
        const insertPos = linkMatch.index + linkMatch[0].length;
        lines[i] =
          line.slice(0, insertPos) + npubTag + line.slice(insertPos);
        injected.add(npub);
        didInject = true;
        break;
      }
    }

    if (didInject) continue;

    // --- Strategy 2: Find first bare-text mention (not in header, not in link brackets) ---
    // We look for the project name as a word boundary match in body text,
    // ensuring it's not inside [...] of a markdown link.
    const barePattern = new RegExp(`\\b${escaped}\\b`, "i");

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];

      // Never inject in header lines
      if (/^#{1,6}\s/.test(line)) continue;

      // Skip lines that are only horizontal rules, blank, etc.
      if (/^\s*$/.test(line) || /^---/.test(line)) continue;

      const bareMatch = barePattern.exec(line);
      if (!bareMatch) continue;

      // Check if this match is inside markdown link brackets [...]
      // Find all [...](url) spans in the line and see if our match overlaps
      const matchStart = bareMatch.index;
      const matchEnd = matchStart + bareMatch[0].length;

      let insideLink = false;
      const linkSpans = /\[([^\]]*)\]\([^)]*\)/g;
      let span;
      while ((span = linkSpans.exec(line)) !== null) {
        // The bracket content starts at span.index + 1 and ends at span.index + 1 + span[1].length
        const bracketStart = span.index + 1;
        const bracketEnd = bracketStart + span[1].length;
        if (matchStart >= bracketStart && matchEnd <= bracketEnd) {
          insideLink = true;
          break;
        }
      }

      if (insideLink) {
        // The bare name is inside a link's bracket text. This means there IS
        // a link containing the name but our Strategy 1 should have caught it.
        // This can happen if the link pattern didn't match (e.g. case).
        // Inject after the link containing it.
        const linkSpans2 = /\[[^\]]*\]\([^)]*\)/g;
        let span2;
        while ((span2 = linkSpans2.exec(line)) !== null) {
          const bracketStart = span2.index + 1;
          const bracketEnd = bracketStart + (span2[0].indexOf("](") - 1);
          if (matchStart >= bracketStart && matchEnd <= bracketStart + span2[0].indexOf("](")) {
            const insertPos = span2.index + span2[0].length;
            lines[i] =
              line.slice(0, insertPos) + npubTag + line.slice(insertPos);
            injected.add(npub);
            didInject = true;
            break;
          }
        }
        if (didInject) break;
        continue; // try next line
      }

      // Not inside a link - inject right after the bare mention
      const insertPos = matchEnd;
      lines[i] =
        line.slice(0, insertPos) + npubTag + line.slice(insertPos);
      injected.add(npub);
      didInject = true;
      break;
    }
  }

  return lines.join("\n");
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

function main() {
  // Parse flags
  const args = process.argv.slice(2);
  const forceMode = args.includes("--force");
  const noInject = args.includes("--no-inject");
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
  const unresolvedIdentities = loadUnresolvedIdentities();
  const noDm = loadNoDmNpubs();
  const mentions = extractMentions(body, npubs, unresolvedIdentities, noDm);

  // Inject nostr:npub tags into body text (NIP-27: after first link per project)
  if (!noInject) {
    body = injectNpubMentions(body, mentions.found);
  }

  // Report found mentions on stderr
  if (mentions.found.length > 0) {
    console.error(`[publish] Found npubs for ${mentions.found.length} projects:`);
    for (const { name, npub, identity_type } of mentions.found) {
      const tag = `[${identity_type}]`;
      console.error(`  + ${tag} ${name} -> ${npub.slice(0, 20)}...`);
    }
  }

  if (mentions.unresolved.length > 0) {
    console.error("");
    console.error(`[publish] RESEARCHED UNRESOLVED identities for ${mentions.unresolved.length} projects:`);
    for (const { name, record } of mentions.unresolved) {
      console.error(`  - ${name} (checked ${record.checked_at}): ${record.reason}`);
    }
    console.error("[publish] Leave these projects untagged and out of outreach unless new primary evidence is found.");
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
    console.error("[publish] Research: primary project site/repository, npub.world, then exact NAK relay queries.");
    console.error("[publish] If ownership or role remains unclear, add an unresolved record and ask the editor.");
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
      outreachRecipients: mentions.outreachRecipients,
      unresolved: mentions.unresolved,
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

if (import.meta.main) {
  main();
}
