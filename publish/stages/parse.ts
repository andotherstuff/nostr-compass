// Stage 1: PARSE.
// Reads /tmp/{N}publish.md, splits into the 4 canonical blocks, validates
// the 21-word TL;DR, validates the banner image URL against the pinned
// config, parses an optional 5th "Tags:" block. Writes out/{N}/metadata.json.
//
// The /tmp/{N}publish.md format is the output of scripts/publish.ts:
//
//   Nostr Compass #N
//   <blank>
//   [21-word TL;DR]
//   <blank>
//   [pinned banner image URL]
//   <blank>
//   [newsletter body]
//   <blank>                  optional from here
//   Tags: foo, bar, baz       optional 6th block

import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { writeAtomic } from "../lib/safety.ts";

const COVER_PATH = join(import.meta.dir, "..", "config/cover.json");
const OUT_DIR = join(import.meta.dir, "..", "out");

export type CompassMetadata = {
  issue: number;
  title: string;
  tldr: string;
  tldr_word_count: number;
  banner_url: string;
  body: string;
  tags: string[];
  source_path: string;
};

const MAX_TAGS = 6;

function splitParagraphs(content: string): string[] {
  return content
    .split(/\n\s*\n/)
    .map((p) => p.trim())
    .filter((p) => p.length > 0);
}

function countWords(s: string): number {
  return s.trim().split(/\s+/).filter(Boolean).length;
}

function parseTagsBlock(block: string): string[] {
  const m = block.match(/^Tags:\s*(.+)$/i);
  if (!m) return [];
  const raw = m[1]
    .split(",")
    .map((t) => t.trim().toLowerCase())
    .filter((t) => t.length > 0)
    .map((t) => t.replace(/^#/, "")); // strip leading # if present
  if (raw.length > MAX_TAGS) {
    throw new Error(
      `Tags line lists ${raw.length} tags; cap is ${MAX_TAGS}. Trim before publishing.`,
    );
  }
  // Deduplicate while preserving first-seen order.
  return [...new Set(raw)];
}

export function parsePublishSource(
  raw: string,
  issue: number,
  expectedBannerUrl: string,
  sourcePath: string,
): CompassMetadata {
  const paragraphs = splitParagraphs(raw);
  if (paragraphs.length < 4) {
    throw new Error(
      `${sourcePath} has ${paragraphs.length} blocks, need at least 4: title, tldr, banner, body.`,
    );
  }

  const title = paragraphs[0];
  const tldr = paragraphs[1];
  const bannerLine = paragraphs[2];

  // Detect optional Tags: block at the end. Otherwise the body is everything
  // from paragraph index 3 onward joined with blank lines. Sources generated
  // before the four-block format may still carry a separate "#N is out"
  // announcement at index 3; discard that legacy block when re-publishing.
  let tags: string[] = [];
  let bodyEndIndex = paragraphs.length;
  const last = paragraphs[paragraphs.length - 1];
  if (/^Tags:\s*/i.test(last)) {
    tags = parseTagsBlock(last);
    bodyEndIndex = paragraphs.length - 1;
  }
  const escapedTitle = title.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const bodyStartIndex = new RegExp(`^${escapedTitle} is out\\.`, "i").test(paragraphs[3])
    ? 4
    : 3;
  const body = paragraphs.slice(bodyStartIndex, bodyEndIndex).join("\n\n");

  // Validate title shape: "Nostr Compass #N"
  const titleMatch = title.match(/^Nostr Compass #([0-9]+)$/);
  if (!titleMatch) {
    throw new Error(`Title block must be "Nostr Compass #<N>". Got: "${title}"`);
  }
  const issueFromTitle = parseInt(titleMatch[1], 10);
  if (issueFromTitle !== issue) {
    throw new Error(
      `Title says issue ${issueFromTitle} but you asked to publish issue ${issue}. Aborting.`,
    );
  }

  // Validate TL;DR word count.
  const tldrWordCount = countWords(tldr);
  if (tldrWordCount !== 21) {
    throw new Error(
      `TL;DR has ${tldrWordCount} words. Cardinal rule: exactly 21. TL;DR was: "${tldr}"`,
    );
  }

  // Validate banner URL against the pinned config.
  if (bannerLine !== expectedBannerUrl) {
    throw new Error(
      `Banner URL block does not match config/cover.json.\n` +
        `  in publish.md: ${bannerLine}\n` +
        `  in cover.json: ${expectedBannerUrl}\n` +
        `If the brand image legitimately changed, update config/cover.json.`,
    );
  }

  const metadata: CompassMetadata = {
    issue,
    title,
    tldr,
    tldr_word_count: tldrWordCount,
    banner_url: bannerLine,
    body,
    tags,
    source_path: sourcePath,
  };

  return metadata;
}

export async function parseIssue(issue: number): Promise<CompassMetadata> {
  const sourcePath = `/tmp/${issue}publish.md`;
  let raw: string;
  try {
    raw = await readFile(sourcePath, "utf8");
  } catch {
    throw new Error(
      `Could not read ${sourcePath}. Generate it first with: bun scripts/publish.ts`,
    );
  }
  const cover = JSON.parse(await readFile(COVER_PATH, "utf8")) as { banner_url: string };
  const metadata = parsePublishSource(raw, issue, cover.banner_url, sourcePath);

  await writeAtomic(
    join(OUT_DIR, String(issue), "metadata.json"),
    JSON.stringify(metadata, null, 2),
  );

  return metadata;
}
