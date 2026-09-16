#!/usr/bin/env bun

import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { resolveIssueParticipants } from "./dm-outreach.ts";
import { closeBunker, signWithBunker } from "./lib/bunker.ts";
import { loadJournal, mutateJournal, reuseOrSign, sha256, stableJson } from "./lib/journal.ts";
import { broadcastToRelays, relayHasEvent } from "./lib/relays.ts";
import { IssueLock, validateNumber, writeAtomic } from "./lib/safety.ts";

const ROOT = join(import.meta.dir, "..");
const OUT_DIR = join(ROOT, "publish/out");
const AUTHOR_PATH = join(ROOT, "publish/config/author.json");
const LOGBOOK_RELAYS = ["wss://nos.lol", "wss://relay.damus.io", "wss://relay.primal.net"];

type Args = { issue: number; newsletterUrl: string; podcastUrl: string; reallyPublish: boolean };

function parseArgs(argv: string[]): Args {
  const positional: string[] = [];
  let newsletterUrl = "";
  let podcastUrl = "";
  let reallyPublish = false;
  for (let i = 2; i < argv.length; i++) {
    const value = argv[i];
    if (value === "--newsletter-url") newsletterUrl = argv[++i];
    else if (value === "--podcast-url") podcastUrl = argv[++i];
    else if (value === "--really-publish") reallyPublish = true;
    else if (value.startsWith("--")) throw new Error(`Unknown flag: ${value}`);
    else positional.push(value);
  }
  if (positional.length !== 1 || !newsletterUrl || !podcastUrl) {
    throw new Error("Usage: podcast-access.ts <issue> --newsletter-url <url> --podcast-url <url> [--really-publish]");
  }
  return { issue: validateNumber(positional[0]), newsletterUrl, podcastUrl, reallyPublish };
}

function newsletterHeadings(markdown: string): string[] {
  return markdown.split("\n").filter((line) => /^#{2,3}\s+\S/.test(line)).map((line) => line.replace(/^#{2,3}\s+/, "").trim());
}

async function requireHttpOk(url: string, label: string): Promise<{ url: string; status: number }> {
  const response = await fetch(url.split("#")[0], { redirect: "follow" });
  if (!response.ok) throw new Error(`${label} returned HTTP ${response.status}`);
  return { url: response.url, status: response.status };
}

async function execute(args: Args): Promise<void> {
  const journal = await loadJournal(OUT_DIR, args.issue);
  if (journal.effects.merge?.state !== "confirmed" || !journal.pull_request?.merge_sha) throw new Error("Podcast access requires an exact confirmed merge");
  if (journal.effects.deploy?.state !== "confirmed" || !journal.deployment) throw new Error("Podcast access requires an attributable confirmed deployment");
  if (journal.effects.article?.state !== "confirmed" || journal.effects.announcement?.state !== "confirmed") throw new Error("Podcast access requires both newsletter events to pass relay readback");
  if (journal.deployment.page_url !== args.newsletterUrl) throw new Error("Newsletter URL does not match the confirmed deployment route");

  const resolved = await resolveIssueParticipants(args.issue);
  const participants = [...resolved.recipients, ...resolved.excludedNoDm]
    .sort((a, b) => a.npub.localeCompare(b.npub));
  if (participants.length === 0) throw new Error("No verified issue participants were resolved");
  const markdown = await readFile(resolved.newsletterPath, "utf8");
  const headings = newsletterHeadings(markdown);
  if (headings.length === 0) throw new Error("Published issue has no Logbook section targets");
  const access = {
    contributors: participants.map((participant) => ({ pubkey: participant.hex, name: participant.primaryName })),
  };
  const unsigned = {
    kind: 34201,
    created_at: Math.round(Date.now() / 1000),
    tags: [["d", `logbook-wl-${args.issue}`], ["alt", `Logbook whitelist: logbook-wl-${args.issue}`]],
    content: JSON.stringify(access),
  };
  console.log(`Logbook access plan: issue=${args.issue}, participants=${participants.length}, sections=${headings.length}`);
  if (!args.reallyPublish) {
    for (const participant of participants) console.log(`  ${participant.primaryName}: ${participant.npub}`);
    console.log("Preview complete: no signing, relay, journal, or file mutation.");
    return;
  }

  const author = JSON.parse(await readFile(AUTHOR_PATH, "utf8")) as { pubkey_hex: string };
  const issueDir = join(OUT_DIR, String(args.issue));
  const eventPath = join(issueDir, "podcast-access-event.json");
  const event = await reuseOrSign({
    outDir: OUT_DIR,
    issue: args.issue,
    effectName: "podcast_access_event",
    unsigned,
    payloadFile: eventPath,
    intent: { issue: args.issue, access, relays: LOGBOOK_RELAYS },
    signer: (candidate) => signWithBunker(candidate, author.pubkey_hex),
  });
  await mutateJournal(OUT_DIR, args.issue, (state) => { state.effects.podcast_access_event.state = "attempted"; });
  const receipts = await broadcastToRelays(event, LOGBOOK_RELAYS);
  const readbacks = Object.fromEntries(await Promise.all(LOGBOOK_RELAYS.map(async (relay) => [relay, await relayHasEvent(relay, event.id)])));
  const recovered = Object.values(readbacks).filter(Boolean).length;
  if (recovered < 2) {
    await mutateJournal(OUT_DIR, args.issue, (state) => {
      state.effects.podcast_access_event.state = "ambiguous";
      state.effects.podcast_access_event.error = `only ${recovered}/3 Logbook relays recovered the exact contributor event`;
    });
    throw new Error(`Only ${recovered}/3 Logbook relays recovered the exact contributor event`);
  }
  const [newsletterHttp, podcastHttp] = await Promise.all([
    requireHttpOk(args.newsletterUrl, "Newsletter"),
    requireHttpOk(args.podcastUrl, "Logbook"),
  ]);
  const editionDate = resolved.newsletterPath.match(/(\d{4}-\d{2}-\d{2})-newsletter\.md$/)?.[1];
  if (!editionDate) throw new Error("Could not derive edition date from the newsletter path");
  const manifest = {
    schema_version: 1,
    issue: args.issue,
    edition_date: editionDate,
    merge_sha: journal.pull_request.merge_sha,
    newsletter_url: args.newsletterUrl,
    podcast_url: args.podcastUrl,
    section_targets: ["Intro", ...headings],
    participants: participants.map(({ npub, hex, names }) => ({ npub, pubkey: hex, names: [...names].sort() })),
    unresolved: resolved.unresolved,
    missing: resolved.missing,
    whitelist_event_id: event.id,
    whitelist_event_signature: event.sig,
    relay_receipts: receipts,
    relay_readbacks: readbacks,
    http_readbacks: { newsletter: newsletterHttp, logbook: podcastHttp },
  };
  const accessManifestSha = sha256(stableJson(manifest));
  const readiness = { ...manifest, access_manifest_sha256: accessManifestSha, final: true };
  const readinessPath = join(issueDir, "podcast-access-readiness.json");
  const readinessBytes = JSON.stringify(readiness, null, 2);
  await writeAtomic(readinessPath, readinessBytes);
  const readinessSha = sha256(readinessBytes);
  const recipientManifest = resolved.recipients.map((recipient) => ({ npub: recipient.npub, names: [...recipient.names].sort() })).sort((a, b) => a.npub.localeCompare(b.npub));
  const obligation = {
    schema_version: 1,
    issue: args.issue,
    campaign: "podcast-invitation",
    pr_url: `https://github.com/andotherstuff/nostr-compass/pull/${journal.pull_request.number}`,
    pr_number: journal.pull_request.number,
    head_sha: journal.pull_request.head_sha,
    recipient_manifest_sha256: sha256(stableJson(recipientManifest)),
    newsletter_url: args.newsletterUrl,
    podcast_url: args.podcastUrl,
    merge_sha: journal.pull_request.merge_sha,
    edition_date: editionDate,
    section_target: "intro and every published H2/H3 section",
    access_manifest_sha256: accessManifestSha,
    access_signature: event.sig,
    readiness_receipt_path: readinessPath,
    readiness_receipt_sha256: readinessSha,
    final: true,
  } as const;
  const obligationPath = join(issueDir, "outreach", "podcast-invitation-obligation.json");
  const obligationBytes = JSON.stringify(obligation, null, 2);
  await writeAtomic(obligationPath, obligationBytes);
  await mutateJournal(OUT_DIR, args.issue, (state) => {
    state.effects.podcast_access_event.state = "confirmed";
    state.effects.podcast_access_event.receipts = Object.fromEntries(receipts.map((receipt) => [receipt.relay, { ...receipt, recorded_at: new Date().toISOString() }]));
    state.effects.podcast_access_event.readbacks = Object.fromEntries(Object.entries(readbacks).map(([relay, found]) => [relay, { found, recorded_at: new Date().toISOString() }]));
    state.effects.podcast_access = { state: "confirmed", intent_sha256: accessManifestSha, payload_path: readinessPath, payload_sha256: readinessSha, event_id: event.id };
    state.effects["outreach:podcast-invitation"] = { state: "confirmed", intent_sha256: sha256(stableJson(obligation)), payload_path: obligationPath, payload_sha256: sha256(obligationBytes) };
  });
  console.log(`Confirmed Logbook access for ${participants.length} verified participants on ${recovered}/3 relays.`);
  console.log(`Readiness: ${readinessPath}`);
}

if (import.meta.main) {
  const args = parseArgs(process.argv);
  const run = async () => {
    if (!args.reallyPublish) return execute(args);
    const lock = await IssueLock.acquire(args.issue, OUT_DIR);
    try { await execute(args); } finally { await lock.release(); }
  };
  run().catch((error) => { console.error(`error: ${(error as Error).message}`); process.exitCode = 1; }).finally(closeBunker);
}
