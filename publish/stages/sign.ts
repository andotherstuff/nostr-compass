// Stages 2 + 3: PREPARE + SIGN.
// PREPARE composes the kind 30023 event template (no signing). SIGN requests
// a bunker signature for it. They run together because PREPARE is fast and
// has no external side effects; the operator only sees the Amber prompt at
// SIGN.
//
// Article structure for Compass kind 30023:
//   - kind: 30023
//   - tags: d=newsletter-N, title, summary (TL;DR), published_at, image
//           (pinned banner URL), alt, plus 0-6 t tags from the Tags block
//   - content: newsletter body and only the body. No banner attribution. No
//     announcement prefix. The TL;DR lives in the summary tag, the banner
//     in the image tag, the announcement in the separate kind:1.

import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { signWithBunker, type SignedEvent, type UnsignedEvent } from "../lib/bunker.ts";
import { writeAtomic } from "../lib/safety.ts";

const OUT_DIR = join(import.meta.dir, "..", "out");
const AUTHOR_PATH = join(import.meta.dir, "..", "config/author.json");

type Metadata = {
  issue: number;
  title: string;
  tldr: string;
  banner_url: string;
  body: string;
  tags: string[];
};

type PublishedEntry = {
  issue: number;
  event_id: string;
  first_published_at: number;
};

const PUBLISHED_LEDGER = join(import.meta.dir, "..", "published.json");

async function readLedger(): Promise<PublishedEntry[]> {
  try {
    return JSON.parse(await readFile(PUBLISHED_LEDGER, "utf8")) as PublishedEntry[];
  } catch {
    return [];
  }
}

export function buildArticleEvent(args: {
  metadata: Metadata;
  pubkey: string;
  firstPublishedAt: number;
}): UnsignedEvent {
  const { metadata, pubkey, firstPublishedAt } = args;
  void pubkey;
  const now = Math.floor(Date.now() / 1000);

  const dTagValue = `newsletter-${metadata.issue}`;
  const tags: string[][] = [
    ["d", dTagValue],
    ["title", metadata.title],
    ["summary", metadata.tldr],
    ["published_at", String(firstPublishedAt)],
    ["image", metadata.banner_url],
    ["alt", `Long-form article: ${metadata.title}`],
  ];
  for (const t of metadata.tags) {
    tags.push(["t", t]);
  }

  return {
    kind: 30023,
    content: metadata.body,
    tags,
    created_at: now,
  };
}

export async function signArticle(issue: number): Promise<SignedEvent> {
  const issueDir = join(OUT_DIR, String(issue));
  const metadataPath = join(issueDir, "metadata.json");

  const metadata = JSON.parse(await readFile(metadataPath, "utf8")) as Metadata;
  const author = JSON.parse(await readFile(AUTHOR_PATH, "utf8")) as {
    pubkey_hex: string;
    npub: string;
  };
  if (author.pubkey_hex === "PENDING_PREFLIGHT") {
    throw new Error(
      `config/author.json still says PENDING_PREFLIGHT. Run preflight first to discover and lock in the signing pubkey.`,
    );
  }

  const ledger = await readLedger();
  const prior = ledger.find((e) => e.issue === issue);
  const firstPublishedAt = prior?.first_published_at ?? Math.floor(Date.now() / 1000);

  const unsigned = buildArticleEvent({
    metadata,
    pubkey: author.pubkey_hex,
    firstPublishedAt,
  });

  // Persist the unsigned template before requesting a signature, so we can
  // inspect what we're about to sign and replay if anything goes wrong.
  await writeAtomic(
    join(issueDir, "article.unsigned.json"),
    JSON.stringify(unsigned, null, 2),
  );

  console.log(`              requesting bunker signature for kind 30023 article (Amber prompt incoming)...`);
  const signed = await signWithBunker(unsigned, author.pubkey_hex);

  await writeAtomic(
    join(issueDir, "event.json"),
    JSON.stringify(signed, null, 2),
  );

  console.log(`              ✓ signed`);
  console.log(`              event_id: ${signed.id}`);
  console.log(`              published_at: ${firstPublishedAt}${prior ? " (preserved)" : " (new)"}`);
  console.log(`              tags: ${metadata.tags.length === 0 ? "none" : metadata.tags.join(", ")}`);
  return signed;
}
