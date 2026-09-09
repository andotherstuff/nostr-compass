// Stage 5: gated, resumable broadcast of exact signed payloads.
import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { nip19 } from "nostr-tools";
import { broadcastToRelays, relayHasEvent, type RelayReceipt } from "../lib/relays.ts";
import { loadJournal, mutateJournal, sha256 } from "../lib/journal.ts";
import { writeAtomic } from "../lib/safety.ts";
import type { SignedEvent } from "../lib/bunker.ts";

const DEFAULT_OUT_DIR = join(import.meta.dir, "..", "out");
const DEFAULT_RELAYS_PATH = join(import.meta.dir, "..", "config/relays.json");
const DEFAULT_LEDGER = join(import.meta.dir, "..", "published.json");
type PublishedEntry = { issue: number; event_id: string; announcement_id: string; first_published_at: number; last_edited_at: number; banner_url: string; relays_ok: string[]; relays_fail: string[] };
type Broadcaster = (event: SignedEvent, relays: string[], onReceipt?: (receipt: RelayReceipt) => Promise<void> | void) => Promise<RelayReceipt[]>;
type Reader = (relay: string, eventId: string) => Promise<boolean>;

async function readLedger(path: string): Promise<PublishedEntry[]> {
  try { const value = JSON.parse(await readFile(path, "utf8")); if (!Array.isArray(value)) throw new Error("not an array"); return value; }
  catch (e) { if ((e as NodeJS.ErrnoException).code === "ENOENT") return []; throw new Error(`Refusing to overwrite malformed published.json: ${(e as Error).message}`); }
}

export function relayFloor(configured: number, requested?: number): number {
  if (configured < 5) throw new Error("At least five relays must be configured for publication");
  const floor = requested ?? 5;
  if (!Number.isInteger(floor) || floor < 5 || floor > configured) throw new Error("relay_floor must be an integer between five and the configured relay count");
  return floor;
}

export async function broadcastIssue(issue: number, reallyBroadcast: boolean, options: { outDir?: string; relaysPath?: string; ledgerPath?: string; broadcaster?: Broadcaster; reader?: Reader; encodeLinks?: boolean } = {}): Promise<{ article_ok: number; announcement_ok: number }> {
  if (!reallyBroadcast) throw new Error("Broadcast is gated. Pass --really-broadcast to enable.");
  const outDir = options.outDir ?? DEFAULT_OUT_DIR;
  const relaysPath = options.relaysPath ?? DEFAULT_RELAYS_PATH;
  const ledgerPath = options.ledgerPath ?? DEFAULT_LEDGER;
  const broadcaster = options.broadcaster ?? broadcastToRelays;
  const reader = options.reader ?? relayHasEvent;
  const issueDir = join(outDir, String(issue));
  const article = JSON.parse(await readFile(join(issueDir, "event.json"), "utf8")) as SignedEvent;
  const announcement = JSON.parse(await readFile(join(issueDir, "announcement.json"), "utf8")) as SignedEvent;
  const cfg = JSON.parse(await readFile(relaysPath, "utf8")) as { relays: string[]; relay_floor?: number; readback_exempt_relays?: string[] };
  const exempt = new Set(cfg.readback_exempt_relays ?? []);
  const durableRelays = cfg.relays.filter((relay) => !exempt.has(relay));
  const floor = relayFloor(durableRelays.length, cfg.relay_floor);
  const journal = await loadJournal(outDir, issue);
  for (const gate of ["quality", "feedback"] as const) {
    const evidence = journal.effects[gate];
    if (evidence?.state !== "confirmed" || !evidence.payload_path || !evidence.payload_sha256 || sha256(await readFile(evidence.payload_path)) !== evidence.payload_sha256) throw new Error(`Refusing broadcast before ${gate} exact-head artifact evidence is confirmed`);
  }
  if (journal.effects.buttondown?.state !== "confirmed" || !journal.effects.buttondown.event_id) throw new Error("Refusing broadcast before explicit Buttondown sent/skipped disposition is confirmed");
  if (journal.effects.merge?.state !== "confirmed" || !journal.pull_request?.merge_sha) {
    throw new Error("Refusing to broadcast before the exact pull request merge is confirmed");
  }
  if (journal.effects.deploy?.state !== "confirmed" || !journal.deployment || journal.deployment.head_sha !== journal.pull_request.merge_sha || journal.deployment.tree_sha !== journal.pull_request.merge_tree_sha || journal.effects.deploy.payload_sha256 !== journal.deployment.content_sha256) {
    throw new Error("Refusing to broadcast before deployment of the exact merge commit is externally confirmed");
  }
  for (const [name, event] of [["article", article], ["announcement", announcement]] as const) {
    const effect = journal.effects[name];
    if (!effect || effect.event_id !== event.id || !effect.payload_sha256) throw new Error(`Journal does not pin signed ${name} payload ${event.id}`);
    const payloadPath = join(issueDir, name === "article" ? "event.json" : "announcement.json");
    const bytes = await readFile(payloadPath);
    if (effect.payload_path !== payloadPath || sha256(bytes) !== effect.payload_sha256) {
      throw new Error(`Signed payload hash mismatch for ${name}`);
    }
  }

  const send = async (name: "article" | "announcement", event: SignedEvent): Promise<RelayReceipt[]> => {
    let current = await loadJournal(outDir, issue);
    const existing = current.effects[name].receipts ?? {};
    const remaining = cfg.relays.filter((relay) => !existing[relay]?.ok);
    await mutateJournal(outDir, issue, (j) => { j.effects[name].state = "attempted"; });
    try {
      await broadcaster(event, remaining, async (receipt) => {
        await mutateJournal(outDir, issue, (j) => {
          j.effects[name].receipts ??= {};
          j.effects[name].receipts![receipt.relay] = { ...receipt, recorded_at: new Date().toISOString() };
        });
      });
    } catch (error) {
      await mutateJournal(outDir, issue, (j) => { j.effects[name].state = "ambiguous"; j.effects[name].error = (error as Error).message; });
      throw error;
    }
    for (const relay of durableRelays) {
      const found = await reader(relay, event.id);
      await mutateJournal(outDir, issue, (journal) => { journal.effects[name].readbacks ??= {}; journal.effects[name].readbacks![relay] = { found, recorded_at: new Date().toISOString() }; });
    }
    current = await loadJournal(outDir, issue);
    const receipts = Object.entries(current.effects[name].receipts ?? {}).map(([relay, r]) => ({ relay, ok: r.ok, reason: r.reason, ms: r.ms }));
    const ok = Object.values(current.effects[name].readbacks ?? {}).filter((receipt) => receipt.found).length;
    await mutateJournal(outDir, issue, (j) => { j.effects[name].state = ok >= floor ? "confirmed" : "failed"; j.effects[name].error = ok >= floor ? undefined : `relay floor not met: ${ok}/${floor}`; });
    if (ok < floor) throw new Error(`${name} relay floor not met: ${ok}/${floor}`);
    return receipts;
  };

  const articleReceipts = await send("article", article);
  const announcementReceipts = await send("announcement", announcement);
  const finalState = await loadJournal(outDir, issue);
  const articleReadback = Object.entries(finalState.effects.article.readbacks ?? {}).filter(([, receipt]) => receipt.found).map(([relay]) => relay);
  const announcementReadback = Object.entries(finalState.effects.announcement.readbacks ?? {}).filter(([, receipt]) => receipt.found).map(([relay]) => relay);
  await writeAtomic(join(issueDir, "receipts.json"), JSON.stringify({ schema_version: 1, relay_floor: floor, acceptance: { article: articleReceipts, announcement: announcementReceipts }, readback: { article: finalState.effects.article.readbacks, announcement: finalState.effects.announcement.readbacks } }, null, 2));
  const first_published_at = Number(article.tags.find((t) => t[0] === "published_at")?.[1] ?? article.created_at);
  const entry: PublishedEntry = { issue, event_id: article.id, announcement_id: announcement.id, first_published_at, last_edited_at: article.created_at, banner_url: article.tags.find((t) => t[0] === "image")?.[1] ?? "", relays_ok: articleReadback, relays_fail: durableRelays.filter((relay) => !articleReadback.includes(relay)) };
  const ledger = await readLedger(ledgerPath); const idx = ledger.findIndex((e) => e.issue === issue); if (idx >= 0) ledger[idx] = entry; else ledger.push(entry);
  await writeAtomic(ledgerPath, JSON.stringify(ledger, null, 2));

  const relayHints = [...new Set([...entry.relays_ok, ...announcementReadback])].slice(0, 4);
  const dTag = article.tags.find((t) => t[0] === "d")?.[1]; if (!dTag) throw new Error("article event is missing its d-tag");
  console.log(`              article njump: https://njump.me/${nip19.naddrEncode({ kind: article.kind, pubkey: article.pubkey, identifier: dTag, relays: relayHints })}`);
  console.log(`              announce njump: https://njump.me/${nip19.neventEncode({ id: announcement.id, author: announcement.pubkey, kind: announcement.kind, relays: relayHints })}`);
  return { article_ok: entry.relays_ok.length, announcement_ok: announcementReadback.length };
}
