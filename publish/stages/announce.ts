// Stage 4: ANNOUNCE-SIGN.
// Composes a kind:1 announcement and requests a bunker signature.
// Same shape as ~/blog/publish/stages/announce.ts:
//   - top-level note (no e/a tags, otherwise clients render it as a reply)
//   - no t tags (no hashtags on the announcement)
//   - inline NIP-21 nostr:nevent reference to the article in content
// Compass-specific differences:
//   - the note reuses the newsletter's full opening digest so kind:1-only
//     readers receive the same dense update as article readers
//   - inline nostr:npub mentions injected into the article opening are kept

import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { nip19 } from "nostr-tools";
import { signWithBunker, type SignedEvent, type UnsignedEvent } from "../lib/bunker.ts";
import { buildAnnouncementContent } from "../lib/announcement.ts";
import { writeAtomic } from "../lib/safety.ts";

const OUT_DIR = join(import.meta.dir, "..", "out");
const RELAYS_PATH = join(import.meta.dir, "..", "config/relays.json");
const AUTHOR_PATH = join(import.meta.dir, "..", "config/author.json");

type Metadata = { issue: number; title: string; body: string };

export async function signAnnouncement(issue: number): Promise<SignedEvent> {
  const issueDir = join(OUT_DIR, String(issue));

  const metadata = JSON.parse(
    await readFile(join(issueDir, "metadata.json"), "utf8"),
  ) as Metadata;
  const article = JSON.parse(
    await readFile(join(issueDir, "event.json"), "utf8"),
  ) as SignedEvent;
  const author = JSON.parse(await readFile(AUTHOR_PATH, "utf8")) as {
    pubkey_hex: string;
  };
  const relayCfg = JSON.parse(await readFile(RELAYS_PATH, "utf8")) as {
    relays: string[];
  };

  // The article is kind 30023 (addressable), so it must be referenced via
  // naddr (kind + pubkey + d-tag), not nevent-by-id. nevent pins this exact
  // revision; naddr resolves to whatever the current/latest edit is, which
  // is the correct behavior for parameterized-replaceable events. See the
  // same fix in stages/broadcast.ts.
  const dTag = article.tags.find((t) => t[0] === "d")?.[1];
  if (!dTag) throw new Error("article event is missing its d-tag; cannot build naddr reference");
  const naddr = nip19.naddrEncode({
    kind: article.kind,
    pubkey: author.pubkey_hex,
    identifier: dTag,
    relays: relayCfg.relays.slice(0, 4),
  });

  // Top-level kind:1: editorial intro + the article's opening digest + naddr.
  const content = buildAnnouncementContent(metadata.title, metadata.body, naddr);

  // No 'e', no 'a', no 't'. Top-level root note.
  const tags: string[][] = [
    ["alt", `Announcement for: ${metadata.title}`],
  ];

  const unsigned: UnsignedEvent = {
    kind: 1,
    content,
    tags,
    created_at: Math.floor(Date.now() / 1000),
  };

  await writeAtomic(
    join(issueDir, "announcement.unsigned.json"),
    JSON.stringify(unsigned, null, 2),
  );

  console.log(`              composing announcement for "${metadata.title}"`);
  console.log(`              embedding nostr:${naddr.slice(0, 24)}... in content`);
  console.log(`              requesting bunker signature for kind:1 (Amber prompt incoming)...`);
  const signed = await signWithBunker(unsigned, author.pubkey_hex);

  await writeAtomic(
    join(issueDir, "announcement.json"),
    JSON.stringify(signed, null, 2),
  );

  console.log(`              ✓ signed kind:1 (id ${signed.id.slice(0, 12)}...)`);
  return signed;
}
