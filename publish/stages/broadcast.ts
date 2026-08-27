// Stage 5: BROADCAST.
// Disabled by default: the stage refuses to run unless the operator passes
// the explicit --really-broadcast flag. The first real broadcast is reserved
// for the next scheduled publish day; until then, sign-without-broadcast is
// the safe default.
//
// When enabled, broadcasts BOTH the kind 30023 article and the kind:1
// announcement to every configured relay. Records receipts and updates
// published.json.

import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { nip19 } from "nostr-tools";
import { broadcastToRelays, type RelayReceipt } from "../lib/relays.ts";
import { writeAtomic } from "../lib/safety.ts";
import type { SignedEvent } from "../lib/bunker.ts";

const OUT_DIR = join(import.meta.dir, "..", "out");
const RELAYS_PATH = join(import.meta.dir, "..", "config/relays.json");
const PUBLISHED_LEDGER = join(import.meta.dir, "..", "published.json");

type RelaysConfig = { relays: string[] };

type PublishedEntry = {
  issue: number;
  event_id: string;
  announcement_id: string;
  first_published_at: number;
  last_edited_at: number;
  banner_url: string;
  relays_ok: string[];
  relays_fail: string[];
};

async function readLedger(): Promise<PublishedEntry[]> {
  try {
    return JSON.parse(await readFile(PUBLISHED_LEDGER, "utf8")) as PublishedEntry[];
  } catch {
    return [];
  }
}

export async function broadcastIssue(
  issue: number,
  reallyBroadcast: boolean,
): Promise<{ article_ok: number; announcement_ok: number }> {
  if (!reallyBroadcast) {
    throw new Error(
      `Broadcast is gated. Pass --really-broadcast to enable.\n` +
        `This is intentional: the first real broadcast is reserved for the next\n` +
        `scheduled publication. Until then, the pipeline stops at sign.`,
    );
  }

  const issueDir = join(OUT_DIR, String(issue));
  const article = JSON.parse(
    await readFile(join(issueDir, "event.json"), "utf8"),
  ) as SignedEvent;
  const announcement = JSON.parse(
    await readFile(join(issueDir, "announcement.json"), "utf8"),
  ) as SignedEvent;
  const cfg = JSON.parse(await readFile(RELAYS_PATH, "utf8")) as RelaysConfig;

  console.log(`              broadcasting article ${article.id.slice(0, 12)}... to ${cfg.relays.length} relays`);
  const articleReceipts = await broadcastToRelays(article, cfg.relays);
  printReceipts(articleReceipts);

  console.log(`              broadcasting announcement ${announcement.id.slice(0, 12)}... to ${cfg.relays.length} relays`);
  const announcementReceipts = await broadcastToRelays(announcement, cfg.relays);
  printReceipts(announcementReceipts);

  await writeAtomic(
    join(issueDir, "receipts.json"),
    JSON.stringify({ article: articleReceipts, announcement: announcementReceipts }, null, 2),
  );

  // Update ledger.
  const publishedAtTag = article.tags.find((t) => t[0] === "published_at");
  const first_published_at = publishedAtTag
    ? parseInt(publishedAtTag[1], 10)
    : article.created_at;
  const imageTag = article.tags.find((t) => t[0] === "image");
  const banner_url = imageTag ? imageTag[1] : "";

  const entry: PublishedEntry = {
    issue,
    event_id: article.id,
    announcement_id: announcement.id,
    first_published_at,
    last_edited_at: article.created_at,
    banner_url,
    relays_ok: articleReceipts.filter((r) => r.ok).map((r) => r.relay),
    relays_fail: articleReceipts.filter((r) => !r.ok).map((r) => r.relay),
  };
  const ledger = await readLedger();
  const idx = ledger.findIndex((e) => e.issue === issue);
  if (idx >= 0) ledger[idx] = entry;
  else ledger.push(entry);
  await writeAtomic(PUBLISHED_LEDGER, JSON.stringify(ledger, null, 2));

  const article_ok = articleReceipts.filter((r) => r.ok).length;
  const announcement_ok = announcementReceipts.filter((r) => r.ok).length;
  console.log(`              ✓ article  ${article_ok}/${cfg.relays.length} relays`);
  console.log(`              ✓ announce ${announcement_ok}/${cfg.relays.length} relays`);

  // Kind 30023 is addressable: a raw hex id or note1 will NOT resolve on
  // njump/primal/etc. It must be encoded as naddr (kind + pubkey + d-tag).
  // Kind 1 needs at least nevent (raw hex also fails on njump).
  const relayHints = [
    ...new Set([
      ...articleReceipts.filter((r) => r.ok).map((r) => r.relay),
      ...announcementReceipts.filter((r) => r.ok).map((r) => r.relay),
    ]),
  ].slice(0, 4);
  const dTag = article.tags.find((t) => t[0] === "d")?.[1];
  if (!dTag) throw new Error("article event is missing its d-tag; cannot build naddr link");
  const naddr = nip19.naddrEncode({
    kind: article.kind,
    pubkey: article.pubkey,
    identifier: dTag,
    relays: relayHints,
  });
  const nevent = nip19.neventEncode({
    id: announcement.id,
    author: announcement.pubkey,
    kind: announcement.kind,
    relays: relayHints,
  });
  console.log(`              article njump:  https://njump.me/${naddr}`);
  console.log(`              announce njump: https://njump.me/${nevent}`);
  return { article_ok, announcement_ok };
}

function printReceipts(receipts: RelayReceipt[]): void {
  for (const r of receipts) {
    const status = r.ok ? "ok" : "FAIL";
    const reason = r.ok ? "" : `  ${r.reason}`;
    console.log(`              ${status.padEnd(4)}  ${r.relay.padEnd(36)}  ${r.ms}ms${reason}`);
  }
}
