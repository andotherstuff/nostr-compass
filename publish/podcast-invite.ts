#!/usr/bin/env bun

import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { decode } from "nostr-tools/nip19";
import { closeBunker, signWithBunker, type UnsignedEvent } from "./lib/bunker.ts";
import { loadJournal, mutateJournal, reuseOrSign, sha256, stableJson } from "./lib/journal.ts";
import { broadcastToRelays, relayHasEvent } from "./lib/relays.ts";
import { IssueLock, validateNumber, writeAtomic } from "./lib/safety.ts";

const ROOT = join(import.meta.dir, "..");
const OUT_DIR = join(ROOT, "publish/out");

export function buildPodcastInvitation(issue: number, newsletterUrl: string, podcastUrl: string, npubs: string[], createdAt: number): UnsignedEvent {
  const unique = [...new Set(npubs)].sort();
  const tags = unique.map((npub) => {
    const value = decode(npub);
    if (value.type !== "npub") throw new Error(`${npub} is not an npub`);
    return ["p", value.data as string];
  });
  const content = [
    `Help record the Nostr Compass #${issue} podcast. Pick the intro or any section from this week's issue and leave a short voice note in Logbook whenever it suits you.`,
    "",
    `Issue: ${newsletterUrl}`,
    `Record: ${podcastUrl}`,
    "",
    `Participants: ${unique.map((npub) => `nostr:${npub}`).join(" ")}`,
  ].join("\n");
  return { kind: 1, created_at: createdAt, tags, content };
}

async function execute(issue: number, newsletterUrl: string, podcastUrl: string, reallyBroadcast: boolean): Promise<void> {
  const journal = await loadJournal(OUT_DIR, issue);
  if (journal.effects.podcast_access?.state !== "confirmed") throw new Error("Public invitation requires confirmed Logbook access");
  const campaign = journal.outreach["podcast-invitation"];
  if (!campaign) throw new Error("Public invitation requires the journaled podcast DM campaign");
  const npubs = Object.values(campaign.recipients).flatMap((recipient) => recipient.npub ? [recipient.npub] : []);
  if (npubs.length === 0) throw new Error("Podcast campaign has no verified participants to tag");
  const prior = journal.effects.podcast_public_invitation;
  let createdAt = Math.round(Date.now() / 1000);
  if (prior?.payload_path) {
    const retained = JSON.parse(await readFile(prior.payload_path, "utf8")) as { created_at?: number };
    if (Number.isInteger(retained.created_at)) createdAt = retained.created_at!;
  }
  const unsigned = buildPodcastInvitation(issue, newsletterUrl, podcastUrl, npubs, createdAt);
  console.log(`Public Logbook invitation: issue=${issue}, tagged_participants=${new Set(npubs).size}`);
  if (!reallyBroadcast) {
    console.log(unsigned.content);
    console.log("Preview complete: no signing, relay, journal, or file mutation.");
    return;
  }
  if (journal.deployment?.page_url !== newsletterUrl || journal.effects.article?.state !== "confirmed" || journal.effects.announcement?.state !== "confirmed") throw new Error("Public invitation does not match the confirmed newsletter publication");
  const author = JSON.parse(await readFile(join(ROOT, "publish/config/author.json"), "utf8")) as { pubkey_hex: string };
  const relayConfig = JSON.parse(await readFile(join(ROOT, "publish/config/relays.json"), "utf8")) as { relays: string[]; relay_floor: number; readback_exempt_relays?: string[] };
  const eventPath = join(OUT_DIR, String(issue), "podcast-invitation.json");
  const event = await reuseOrSign({
    outDir: OUT_DIR, issue, effectName: "podcast_public_invitation", unsigned, payloadFile: eventPath,
    intent: { issue, newsletterUrl, podcastUrl, participants: [...new Set(npubs)].sort() },
    signer: (candidate) => signWithBunker(candidate, author.pubkey_hex),
  });
  await mutateJournal(OUT_DIR, issue, (state) => { state.effects.podcast_public_invitation.state = "attempted"; });
  const receipts = await broadcastToRelays(event, relayConfig.relays);
  const durable = relayConfig.relays.filter((relay) => !(relayConfig.readback_exempt_relays ?? []).includes(relay));
  const readbacks = Object.fromEntries(await Promise.all(durable.map(async (relay) => [relay, await relayHasEvent(relay, event.id)])));
  const recovered = Object.values(readbacks).filter(Boolean).length;
  await mutateJournal(OUT_DIR, issue, (state) => {
    const effect = state.effects.podcast_public_invitation;
    effect.receipts = Object.fromEntries(receipts.map((receipt) => [receipt.relay, { ...receipt, recorded_at: new Date().toISOString() }]));
    effect.readbacks = Object.fromEntries(Object.entries(readbacks).map(([relay, found]) => [relay, { found, recorded_at: new Date().toISOString() }]));
    effect.state = recovered >= relayConfig.relay_floor ? "confirmed" : "ambiguous";
    effect.error = recovered >= relayConfig.relay_floor ? undefined : `only ${recovered}/${relayConfig.relay_floor} durable relay readbacks`;
  });
  const receiptPath = join(OUT_DIR, `podcast-invitation-${issue}.json`);
  await writeAtomic(receiptPath, JSON.stringify({ schema_version: 1, issue, event_id: event.id, participants: [...new Set(npubs)].sort(), receipts, readbacks, relay_floor: relayConfig.relay_floor, final: recovered >= relayConfig.relay_floor }, null, 2));
  if (recovered < relayConfig.relay_floor) throw new Error(`Only ${recovered}/${relayConfig.relay_floor} durable relays recovered the public invitation`);
  console.log(`Confirmed public Logbook invitation ${event.id} on ${recovered} durable relays.`);
  console.log(`Receipt: ${receiptPath}`);
}

if (import.meta.main) {
  const positional: string[] = [];
  let newsletterUrl = "", podcastUrl = "", reallyBroadcast = false;
  for (let i = 2; i < process.argv.length; i++) {
    const value = process.argv[i];
    if (value === "--newsletter-url") newsletterUrl = process.argv[++i];
    else if (value === "--podcast-url") podcastUrl = process.argv[++i];
    else if (value === "--really-broadcast") reallyBroadcast = true;
    else if (value.startsWith("--")) throw new Error(`Unknown flag: ${value}`);
    else positional.push(value);
  }
  if (positional.length !== 1 || !newsletterUrl || !podcastUrl) throw new Error("Usage: podcast-invite.ts <issue> --newsletter-url <url> --podcast-url <url> [--really-broadcast]");
  const issue = validateNumber(positional[0]);
  const run = async () => {
    if (!reallyBroadcast) return execute(issue, newsletterUrl, podcastUrl, false);
    const lock = await IssueLock.acquire(issue, OUT_DIR);
    try { await execute(issue, newsletterUrl, podcastUrl, true); } finally { await lock.release(); }
  };
  run().catch((error) => { console.error(`error: ${(error as Error).message}`); process.exitCode = 1; }).finally(closeBunker);
}
