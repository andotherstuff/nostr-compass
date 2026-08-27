#!/usr/bin/env bun
// Compass DM outreach — weekly, reproducible mechanism.
//
// MANUAL INVOCATION ONLY (same gate as publish.ts). Run:
//   COMPASS_PUBLISH_INVOCATION=manual bun dm-outreach.ts <issue> --pr-url <url> \
//     --podcast-url <url> --podcast-time "Thursday at 16:00 UTC" [--reminder] [--really-send]
//
// What it does, every week, without hand-curating a recipient list:
//
// 1. Runs `bun scripts/publish.ts <newsletter file>` to get the exact set of
//    projects/people this issue actually mentions (name + npub), matched
//    against data/npubs.yml. This is the same resolution the newsletter's
//    own nostr: mentions use, so the DM list can never drift from what was
//    actually published.
// 2. Augments that list with each project's "main dev" by reading ONLY the
//    "# Newsletter #<issue> additions" section of data/npubs.yml (the
//    freshly-curated, one-blank-line-per-group section for this week) and
//    pulling in any other npub grouped with a found project in that section.
//    This is deliberately scoped to that section only — older parts of
//    npubs.yml were assembled over many months without a consistent
//    blank-line-per-group convention, and pairing across those loosely
//    risks DMing someone who was never actually mentioned (verified this
//    the hard way while building this script: an unscoped pass wrongly
//    pulled in "HAVEN"'s dev via incidental blank-line adjacency to the
//    unrelated Marmot alias block).
// 3. For each unique recipient pubkey: checks for a published NIP-65 relay
//    list (kind 10002). If found, sends a NIP-17 gift-wrapped DM to their
//    listed relays (plus the compass default set). If not found, falls back
//    to a legacy NIP-04 DM to the compass default relay set only, since we
//    have no way to know where else to deliver it and can't assume their
//    client supports gift wraps yet.
// 4. Reports exactly who was sent to, via which protocol, and who was
//    skipped and why.
//
// Never-DM list: any npub listed under the top-level `no_dm:` key in
// data/npubs.yml is always excluded from outreach, even if
// scripts/publish.ts genuinely finds it mentioned in the issue (e.g. Marmot
// itself, since this whole outreach mechanism, this chat, and the bunker
// a project whose software this pipeline depends on to publish should never
// receive a solicitation DM sent over that same software).
// Add more entries there rather than hardcoding exclusions in this file.

if (process.env.COMPASS_PUBLISH_INVOCATION !== "manual") {
  console.error("Refusing to run. Set COMPASS_PUBLISH_INVOCATION=manual.");
  process.exit(2);
}

import { access, readFile } from "node:fs/promises";
import { join } from "node:path";
import { spawn } from "node:child_process";
import { decode } from "nostr-tools/nip19";
import { generateSecretKey, finalizeEvent, getPublicKey } from "nostr-tools/pure";
import { encrypt as nip44EncryptLocal, getConversationKey } from "nostr-tools/nip44";
import {
  signWithBunker,
  nip44EncryptWithBunker,
  nip04EncryptWithBunker,
  closeBunker,
  type SignedEvent,
} from "./lib/bunker.ts";
import { broadcastToRelays, queryNewest } from "./lib/relays.ts";
import { writeAtomic } from "./lib/safety.ts";
import { countSentRows } from "./lib/outreach-report.ts";
import {
  buildOutreachMessage,
  filterRecipients,
  OUTREACH_REPORT_SCHEMA_VERSION,
  outreachReportSuffix,
  resolveOutreachRoots,
} from "./lib/outreach-scope.ts";
import { notifyMilestone } from "./lib/notify.ts";

const RUNTIME_ROOT = join(import.meta.dir, "..");
const { workspaceRoot: COMPASS_ROOT } = resolveOutreachRoots(RUNTIME_ROOT, process.env.COMPASS_DIR);
const NPUBS_FILE = join(COMPASS_ROOT, "data/npubs.yml");
const NEWSLETTERS_DIR = join(COMPASS_ROOT, "content/en/newsletters");
const AUTHOR_PATH = join(RUNTIME_ROOT, "publish/config/author.json");
const RELAYS_PATH = join(RUNTIME_ROOT, "publish/config/relays.json");
const OUT_DIR = join(RUNTIME_ROOT, "publish/out");

// Well-known relays likely to hold a recipient's kind 10002 relay list, even
// if we don't yet know their actual inbox relays.
const INDEXER_RELAYS = [
  "wss://relay.damus.io",
  "wss://nos.lol",
  "wss://relay.nostr.band",
  "wss://purplepag.es",
  "wss://relay.primal.net",
];

const now = () => Math.round(Date.now() / 1000);
const TWO_DAYS = 2 * 24 * 60 * 60;
const randomNow = () => Math.round(now() - Math.random() * TWO_DAYS);

// ---------------------------------------------------------------------------
// Args
// ---------------------------------------------------------------------------

type Args = {
  issue: number;
  reviewUrl: string;
  newsletterUrl: string;
  podcastUrl: string;
  podcastTime: string;
  reminder: boolean;
  rerecord: boolean;
  reallySend: boolean;
  onlyNames: string[];
};

function parseArgs(argv: string[]): Args {
  const positional: string[] = [];
  let reviewUrl = "";
  let newsletterUrl = "";
  let podcastUrl = "";
  let podcastTime = "";
  let reminder = false;
  let rerecord = false;
  let reallySend = false;
  const onlyNames: string[] = [];
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--pr-url") reviewUrl = argv[++i];
    else if (a === "--newsletter-url") newsletterUrl = argv[++i];
    else if (a === "--podcast-url") podcastUrl = argv[++i];
    else if (a === "--podcast-time") podcastTime = argv[++i];
    else if (a === "--reminder") reminder = true;
    else if (a === "--rerecord") rerecord = true;
    else if (a === "--only") onlyNames.push(argv[++i]);
    else if (a === "--really-send") reallySend = true;
    else if (a.startsWith("--")) throw new Error(`Unknown flag: ${a}`);
    else positional.push(a);
  }
  if (positional.length !== 1) throw new Error("Expected exactly one positional argument: the newsletter issue number.");
  if (!reviewUrl && !newsletterUrl) throw new Error("Either --pr-url or --newsletter-url is required.");
  if (reviewUrl && newsletterUrl) throw new Error("Use either --pr-url or --newsletter-url, not both.");
  if (!podcastUrl) throw new Error("--podcast-url is required.");
  if (!podcastTime) throw new Error("--podcast-time is required so outreach never sends a stale hardcoded date.");
  if (reminder && rerecord) throw new Error("Use either --reminder or --rerecord, not both.");
  return { issue: parseInt(positional[0], 10), reviewUrl, newsletterUrl, podcastUrl, podcastTime, reminder, rerecord, reallySend, onlyNames };
}

// ---------------------------------------------------------------------------
// Step 1: real mentions this issue, via scripts/publish.ts
// ---------------------------------------------------------------------------

type FoundMention = { name: string; npub: string; mention_only: boolean };
type UnresolvedMention = {
  name: string;
  record: { checked_at?: string; reason: string; sources?: string[] };
};

function findNewsletterFile(issue: number): Promise<string> {
  return readFile(join(NEWSLETTERS_DIR, "_index.md"), "utf8")
    .then(() => "")
    .catch(() => "")
    .then(async () => {
      const { readdir } = await import("node:fs/promises");
      const files = await readdir(NEWSLETTERS_DIR);
      for (const f of files) {
        if (!f.endsWith("-newsletter.md")) continue;
        const content = await readFile(join(NEWSLETTERS_DIR, f), "utf8");
        if (new RegExp(`Nostr Compass #${issue}\\b`).test(content) || new RegExp(`newsletter_number:\\s*${issue}\\b`).test(content)) {
          return join(NEWSLETTERS_DIR, f);
        }
      }
      throw new Error(`Could not find a newsletter file for issue #${issue} in ${NEWSLETTERS_DIR}`);
    });
}

function runPublishScript(newsletterPath: string): Promise<{
  found: FoundMention[];
  unresolved: UnresolvedMention[];
  missing: string[];
}> {
  return new Promise((resolve, reject) => {
    const child = spawn("bun", [join(COMPASS_ROOT, "scripts/publish.ts"), newsletterPath, "--force"], {
      cwd: COMPASS_ROOT,
      stdio: ["ignore", "pipe", "pipe"],
    });
    const out: Buffer[] = [];
    const err: Buffer[] = [];
    child.stdout.on("data", (c: Buffer) => out.push(c));
    child.stderr.on("data", (c: Buffer) => err.push(c));
    child.on("close", () => {
      try {
        const parsed = JSON.parse(Buffer.concat(out).toString("utf8"));
        resolve({
          found: parsed.mentions.found as FoundMention[],
          unresolved: (parsed.mentions.unresolved || []) as UnresolvedMention[],
          missing: (parsed.mentions.missing || []).map((entry: unknown) =>
            typeof entry === "string" ? entry : String((entry as { name?: string }).name || entry),
          ),
        });
      } catch (e) {
        reject(new Error(`scripts/publish.ts did not return parseable JSON: ${(e as Error).message}\nstderr: ${Buffer.concat(err).toString("utf8")}`));
      }
    });
    child.on("error", reject);
  });
}

// ---------------------------------------------------------------------------
// Step 2: dev-pairing augmentation, scoped strictly to this issue's own
// "# Newsletter #<issue> additions" section of npubs.yml.
// ---------------------------------------------------------------------------

type Entry = { name: string; npub: string; mention_only: boolean };

function parseBlock(block: string[]): Entry[] {
  const entries: Entry[] = [];
  let i = 0;
  while (i < block.length) {
    const line = block[i];
    if (line.trim().startsWith("#") || line.trim() === "") {
      i++;
      continue;
    }
    const simple = line.match(/^([^:#][^:]*):\s*(npub1[a-z0-9]{58})\s*$/);
    if (simple) {
      entries.push({ name: simple[1].trim(), npub: simple[2], mention_only: false });
      i++;
      continue;
    }
    const objHead = line.match(/^([^:#][^:]*):\s*$/);
    if (objHead) {
      const name = objHead[1].trim();
      let npub: string | undefined;
      let mentionOnly = false;
      let j = i + 1;
      while (j < block.length && block[j].startsWith("  ")) {
        const sub = block[j].trim();
        const npubMatch = sub.match(/^npub:\s*(npub1[a-z0-9]{58})/);
        if (npubMatch) npub = npubMatch[1];
        if (sub.includes("mention_only")) mentionOnly = true;
        j++;
      }
      if (npub) entries.push({ name, npub, mention_only: mentionOnly });
      i = j;
      continue;
    }
    i++;
  }
  return entries;
}

async function loadDevPairings(issue: number): Promise<Map<string, Entry[]>> {
  const raw = await readFile(NPUBS_FILE, "utf8");
  const lines = raw.split("\n");

  let startIdx = -1;
  const headerRe = new RegExp(`^# Newsletter #${issue} additions`);
  for (let i = 0; i < lines.length; i++) {
    if (headerRe.test(lines[i])) startIdx = i;
  }
  if (startIdx === -1) {
    console.log(`              no "# Newsletter #${issue} additions" section found in npubs.yml; skipping dev-pairing augmentation.`);
    return new Map();
  }

  let endIdx = lines.length;
  // Skip the header's own closing banner line before scanning for the end.
  for (let i = startIdx + 2; i < lines.length; i++) {
    if (/^# Newsletter #\d+ additions/.test(lines[i]) || /^# =+$/.test(lines[i])) {
      endIdx = i;
      break;
    }
  }

  const zone = lines.slice(startIdx, endIdx);
  const blocks: string[][] = [];
  let cur: string[] = [];
  for (const line of zone) {
    if (line.trim() === "") {
      if (cur.length) blocks.push(cur);
      cur = [];
    } else {
      cur.push(line);
    }
  }
  if (cur.length) blocks.push(cur);

  const groupOf = new Map<string, Entry[]>();
  for (const block of blocks) {
    const entries = parseBlock(block);
    if (!entries.length) continue;
    for (const e of entries) groupOf.set(e.npub, entries);
  }
  return groupOf;
}

// ---------------------------------------------------------------------------
// Step 3: build final recipient list
// ---------------------------------------------------------------------------

type Recipient = { npub: string; hex: string; names: string[]; primaryName: string };

function decodeNpub(npub: string): string {
  const d = decode(npub);
  if (d.type !== "npub") throw new Error(`${npub} is not an npub`);
  return d.data as string;
}

// Top-level `no_dm:` list in npubs.yml — a flat YAML list of npubs, e.g.:
//   no_dm:
//     - npub1...  # comment
// Parsed independently of the per-issue dev-pairing section above.
async function loadNoDmSet(): Promise<Set<string>> {
  const raw = await readFile(NPUBS_FILE, "utf8");
  const lines = raw.split("\n");
  const startIdx = lines.findIndex((l) => /^no_dm:\s*$/.test(l.trim()));
  if (startIdx === -1) return new Set();
  const hexes = new Set<string>();
  for (let i = startIdx + 1; i < lines.length; i++) {
    const line = lines[i];
    if (/^\s*-\s*npub1[a-z0-9]{58}/.test(line)) {
      const m = line.match(/npub1[a-z0-9]{58}/);
      if (m) hexes.add(decodeNpub(m[0]));
      continue;
    }
    if (line.trim() === "" || line.trim().startsWith("#")) continue;
    break; // end of the list
  }
  return hexes;
}

async function buildRecipients(
  issue: number,
  found: FoundMention[],
): Promise<{ recipients: Recipient[]; excludedNoDm: Recipient[] }> {
  const devPairings = await loadDevPairings(issue);
  const noDmHexes = await loadNoDmSet();
  const byNpub = new Map<string, { names: Set<string>; fromFound: boolean }>();

  for (const f of found) {
    const group = devPairings.get(f.npub) ?? [{ name: f.name, npub: f.npub, mention_only: f.mention_only }];
    for (const g of group) {
      if (!byNpub.has(g.npub)) byNpub.set(g.npub, { names: new Set(), fromFound: g.npub === f.npub });
      byNpub.get(g.npub)!.names.add(g.name);
    }
  }

  const recipients: Recipient[] = [];
  const excludedNoDm: Recipient[] = [];
  for (const [npub, info] of byNpub) {
    const hex = decodeNpub(npub);
    const names = [...info.names];
    const entry = {
      npub,
      hex,
      names,
      primaryName: names.sort((a, b) => a.length - b.length)[0], // shortest name = usually the clean project/handle name
    };
    if (noDmHexes.has(hex)) {
      excludedNoDm.push(entry); // never-DM list, e.g. Marmot itself
      continue;
    }
    recipients.push(entry);
  }
  return {
    recipients: recipients.sort((a, b) => a.primaryName.localeCompare(b.primaryName)),
    excludedNoDm: excludedNoDm.sort((a, b) => a.primaryName.localeCompare(b.primaryName)),
  };
}

// ---------------------------------------------------------------------------
// Step 5: NIP-17 gift wrap (seal signed via bunker, wrap signed locally with
// a fresh ephemeral key, per NIP-59) and NIP-04 fallback.
// ---------------------------------------------------------------------------

async function buildGiftWrap(
  senderHex: string,
  recipientHex: string,
  message: string,
): Promise<SignedEvent> {
  // Rumor (kind 14, unsigned, never broadcast on its own).
  const rumor = {
    kind: 14,
    pubkey: senderHex,
    created_at: now(),
    tags: [["p", recipientHex]],
    content: message,
  };

  // Seal (kind 13): content = nip44(rumor) encrypted to the recipient, using
  // the SENDER's real identity key. That encryption happens inside Amber via
  // the bunker's nip44_encrypt RPC; we never touch the real secret key.
  const sealContent = await nip44EncryptWithBunker(recipientHex, JSON.stringify(rumor));
  const seal = await signWithBunker(
    { kind: 13, content: sealContent, tags: [], created_at: randomNow() },
    senderHex,
  );

  // Gift wrap (kind 1059): signed by a throwaway local key, never the real
  // identity. No bunker approval needed, this key never signs anything else.
  const wrapKey = generateSecretKey();
  const wrapContent = nip44EncryptLocal(
    JSON.stringify(seal),
    getConversationKey(wrapKey, recipientHex),
  );
  const wrap = finalizeEvent(
    { kind: 1059, content: wrapContent, tags: [["p", recipientHex]], created_at: randomNow() },
    wrapKey,
  );
  return wrap as SignedEvent;
}

async function buildNip04Dm(senderHex: string, recipientHex: string, message: string): Promise<SignedEvent> {
  const content = await nip04EncryptWithBunker(recipientHex, message);
  return signWithBunker({ kind: 4, content, tags: [["p", recipientHex]], created_at: now() }, senderHex);
}

// ---------------------------------------------------------------------------
// Step 6: protocol decision (NIP-65 presence check)
// ---------------------------------------------------------------------------

async function resolveTargetRelays(recipientHex: string, defaultRelays: string[]): Promise<{ protocol: "nip17" | "nip04"; relays: string[] }> {
  const relayList = await queryNewest(INDEXER_RELAYS, { kinds: [10002], authors: [recipientHex], limit: 1 });
  if (!relayList) {
    return { protocol: "nip04", relays: defaultRelays };
  }
  const inboxRelays = relayList.tags
    .filter((t) => t[0] === "r" && (t.length === 2 || t[2] === "write"))
    .map((t) => t[1])
    .filter((r) => r.startsWith("wss://") || r.startsWith("ws://"));
  const relays = [...new Set([...defaultRelays, ...inboxRelays])].slice(0, 12);
  return { protocol: "nip17", relays };
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

type ReportRow = {
  primaryName: string;
  names: string[];
  npub: string;
  protocol: "nip17" | "nip04" | "skipped";
  status: "sent" | "failed" | "planned" | "skipped";
  relaysOk?: number;
  relaysTotal?: number;
  eventId?: string;
  reason?: string;
};

async function main() {
  const args = parseArgs(process.argv);
  const suffix = outreachReportSuffix(args.onlyNames, args.reminder, args.rerecord);
  const outPath = join(
    OUT_DIR,
    args.reallySend
      ? `dm-outreach-${args.issue}${suffix}.json`
      : `dm-outreach-${args.issue}${suffix}-plan.json`,
  );
  if (args.reallySend) {
    try {
      await access(outPath);
      throw new Error(`Refusing to duplicate a completed campaign: ${outPath.replace(RUNTIME_ROOT + "/", "")}`);
    } catch (error) {
      if ((error as NodeJS.ErrnoException).code !== "ENOENT") throw error;
    }
  }
  const author = JSON.parse(await readFile(AUTHOR_PATH, "utf8")) as { npub: string; pubkey_hex: string };
  const relaysCfg = JSON.parse(await readFile(RELAYS_PATH, "utf8")) as { relays: string[] };

  console.log(`DM OUTREACH  issue=${args.issue}  reminder=${args.reminder}  rerecord=${args.rerecord}  really_send=${args.reallySend}`);
  console.log(`             sender=${author.npub}`);

  const newsletterPath = await findNewsletterFile(args.issue);
  console.log(`             newsletter=${newsletterPath}`);

  const { found, unresolved, missing } = await runPublishScript(newsletterPath);
  console.log(`             found ${found.length} mentioned projects/people via scripts/publish.ts`);
  if (unresolved.length || missing.length) {
    console.log(
      `             identity gate: ${unresolved.length} researched unresolved, ${missing.length} missing`,
    );
  }

  let { recipients, excludedNoDm } = await buildRecipients(args.issue, found);
  if (args.onlyNames.length > 0) {
    const scoped = filterRecipients([...recipients, ...excludedNoDm], args.onlyNames);
    const scopedNpubs = new Set(scoped.map((recipient) => recipient.npub));
    recipients = recipients.filter((recipient) => scopedNpubs.has(recipient.npub));
    excludedNoDm = excludedNoDm.filter((recipient) => scopedNpubs.has(recipient.npub));
    console.log(`             targeted follow-up: ${args.onlyNames.join(", ")}`);
  }
  console.log(`             ${recipients.length} unique recipients after dev-pairing augmentation`);
  if (excludedNoDm.length) {
    console.log(
      `             excluded ${excludedNoDm.length} via no_dm list: ${excludedNoDm.map((r) => r.primaryName).join(", ")}`,
    );
  }
  console.log("");

  const report: ReportRow[] = excludedNoDm.map((r) => ({
    primaryName: r.primaryName,
    names: r.names,
    npub: r.npub,
    protocol: "skipped",
    status: "skipped",
    reason: "on the no_dm list in data/npubs.yml (never solicited)",
  }));

  for (const r of recipients) {
    const message = buildOutreachMessage(args);
    try {
      const { protocol, relays } = await resolveTargetRelays(r.hex, relaysCfg.relays);

      if (!args.reallySend) {
        report.push({ primaryName: r.primaryName, names: r.names, npub: r.npub, protocol, status: "planned" });
        console.log(`  [plan]  ${protocol.padEnd(5)}  ${r.primaryName.padEnd(20)}  ${r.npub}`);
        continue;
      }

      const event =
        protocol === "nip17"
          ? await buildGiftWrap(author.pubkey_hex, r.hex, message)
          : await buildNip04Dm(author.pubkey_hex, r.hex, message);

      const receipts = await broadcastToRelays(event, relays);
      const ok = receipts.filter((x) => x.ok).length;

      report.push({
        primaryName: r.primaryName,
        names: r.names,
        npub: r.npub,
        protocol,
        status: ok > 0 ? "sent" : "failed",
        relaysOk: ok,
        relaysTotal: relays.length,
        eventId: event.id,
        reason: ok === 0 ? "no relay accepted the event" : undefined,
      });
      console.log(
        `  [${ok > 0 ? "sent" : "FAIL"}]  ${protocol.padEnd(5)}  ${r.primaryName.padEnd(20)}  ${ok}/${relays.length} relays  ${event.id.slice(0, 12)}`,
      );
    } catch (e) {
      report.push({
        primaryName: r.primaryName,
        names: r.names,
        npub: r.npub,
        protocol: "skipped",
        status: "failed",
        reason: (e as Error).message,
      });
      console.log(`  [FAIL]  ${"error".padEnd(5)}  ${r.primaryName.padEnd(20)}  ${(e as Error).message}`);
    }
  }

  // A dry run (no --really-send) writes to a separate `-plan` file, never to
  // the real `dm-outreach-<issue>.json`. That file is the permanent audit
  // trail of an actual send (event IDs, relay receipt counts) and must never
  // be clobbered by a later dry-run test.
  //
  // History note (corrected 2026-07-16): an earlier version of this comment
  // claimed a dry run had clobbered a real issue-31 receipt on 2026-07-21 and
  // that "the underlying DMs themselves had already been delivered fine".
  // Both claims were false. 2026-07-21 was in the future when the comment was
  // written, and the file said to have been destroyed
  // (publish/out/dm-outreach-31.json, mtime 21:29) itself records
  // really_send:false with all 24 recipients at status:"planned" and zero
  // event IDs — it was a dry run's own output, written before this guard
  // existed (dm-outreach.ts mtime 21:31), not a real receipt. No issue-31
  // outreach DM had been sent at that point. The guard below is still correct;
  // only its stated history was wrong.
  await writeAtomic(
    outPath,
    JSON.stringify(
      {
        schema_version: OUTREACH_REPORT_SCHEMA_VERSION,
        issue: args.issue,
        reminder: args.reminder,
        rerecord: args.rerecord,
        really_send: args.reallySend,
        only: args.onlyNames,
        generated_at: now(),
        unresolved,
        missing,
        report,
      },
      null,
      2,
    ),
  );

  console.log("");
  console.log(`✓ wrote ${outPath.replace(RUNTIME_ROOT + "/", "")}`);

  // A dry run is not a finished step, so only a real send is announced.
  if (args.reallySend) {
    const sent = countSentRows(report);
    await notifyMilestone(
      args.issue,
      "outreach-sent",
      [
        `${sent} of ${report.length} recipients received a review invitation.`,
        missing.length > 0 ? `${missing.length} identity/identities unresolved and skipped.` : "",
        `Receipt: \`${outPath.replace(RUNTIME_ROOT + "/", "")}\`.`,
      ],
      { key: args.reminder ? "reminder" : args.rerecord ? "rerecord" : "campaign" },
    );
  }
}

main()
  .catch((e) => {
    console.error(`error: ${(e as Error).message}`);
    process.exitCode = 1;
  })
  .finally(async () => {
    await closeBunker();
  });
