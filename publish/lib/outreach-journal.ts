import { readFile } from "node:fs/promises";
import { join } from "node:path";
import type { SignedEvent } from "./bunker.ts";
import type { RelayReceipt } from "./relays.ts";
import { loadJournal, mutateJournal, mutateJournalAsync, sha256, stableJson, type OutreachCampaign } from "./journal.ts";
import { writeAtomic } from "./safety.ts";

type OutreachObligation = {
  schema_version: 1;
  issue: number;
  campaign: "review" | "podcast-invitation";
  pr_url: string;
  pr_number: number;
  head_sha: string;
  recipient_manifest_sha256: string;
  newsletter_url?: string;
  podcast_url?: string;
  merge_sha?: string;
  edition_date?: string;
  section_target?: string;
  access_manifest_sha256?: string;
  access_signature?: string;
  readiness_receipt_path?: string;
  readiness_receipt_sha256?: string;
  final: true;
};

export async function assertOutreachObligation(args: { outDir: string; issue: number; campaign: "review" | "podcast-invitation"; prUrl?: string; newsletterUrl?: string; podcastUrl?: string; recipients: { npub: string; names: string[] }[] }): Promise<void> {
  const journal = await loadJournal(args.outDir, args.issue);
  const effect = journal.effects[`outreach:${args.campaign}`];
  if (effect?.state !== "confirmed" || !effect.payload_path || !effect.payload_sha256) throw new Error(`Missing journaled ${args.campaign} outreach obligation`);
  const raw = await readFile(effect.payload_path, "utf8");
  if (sha256(raw) !== effect.payload_sha256) throw new Error("Outreach obligation bytes changed");
  let obligation: OutreachObligation;
  try { obligation = JSON.parse(raw); } catch { throw new Error("Outreach obligation is not valid JSON"); }
  const manifest = args.recipients
    .map((recipient) => ({ npub: recipient.npub, names: [...recipient.names].sort() }))
    .sort((a, b) => a.npub.localeCompare(b.npub));
  if (obligation.schema_version !== 1 || obligation.final !== true || obligation.issue !== args.issue || obligation.campaign !== args.campaign || obligation.recipient_manifest_sha256 !== sha256(stableJson(manifest)) || obligation.pr_number !== journal.pull_request?.number || obligation.head_sha !== journal.pull_request?.head_sha || obligation.pr_url !== `https://github.com/andotherstuff/nostr-compass/pull/${obligation.pr_number}`) throw new Error("Outreach obligation does not match the exact PR/head/recipient manifest");
  if (args.campaign === "review") {
    if (!args.prUrl || obligation.pr_url !== args.prUrl) throw new Error("Review outreach obligation does not match the requested PR URL");
    return;
  }
  if (journal.effects.podcast_access?.state !== "confirmed" || !journal.pull_request?.merge_sha || obligation.merge_sha !== journal.pull_request.merge_sha || obligation.newsletter_url !== args.newsletterUrl || obligation.podcast_url !== args.podcastUrl || !obligation.edition_date || !obligation.section_target || !/^[0-9a-f]{64}$/.test(obligation.access_manifest_sha256 ?? "") || !obligation.access_signature || !obligation.readiness_receipt_path || !/^[0-9a-f]{64}$/.test(obligation.readiness_receipt_sha256 ?? "")) throw new Error("Podcast outreach obligation is not bound to exact publication and Logbook access readiness");
  const readiness = await readFile(obligation.readiness_receipt_path);
  if (sha256(readiness) !== obligation.readiness_receipt_sha256 || journal.effects.podcast_access.payload_path !== obligation.readiness_receipt_path || journal.effects.podcast_access.payload_sha256 !== obligation.readiness_receipt_sha256) throw new Error("Podcast access readiness receipt bytes changed");
}

export async function prepareCampaign(args: { outDir: string; issue: number; identity: string; message: string; recipients: { npub: string; names: string[] }[] }): Promise<OutreachCampaign> {
  const intent = sha256(stableJson({ identity: args.identity, message: args.message }));
  return mutateJournalAsync(args.outDir, args.issue, (journal) => {
    const prior = journal.outreach[args.identity];
    if (prior) {
      if (prior.intent_sha256 !== intent) throw new Error("Canonical outreach campaign intent changed");
      for (const recipient of args.recipients) if (!prior.recipients[recipient.npub]) prior.recipients[recipient.npub] = { npub: recipient.npub, names: recipient.names, effect: { state: "prepared", intent_sha256: "unprepared", receipts: {} } };
      return prior;
    }
    const recipients: OutreachCampaign["recipients"] = {};
    for (const recipient of args.recipients) recipients[recipient.npub] = { npub: recipient.npub, names: recipient.names, effect: { state: "prepared", intent_sha256: "unprepared", receipts: {} } };
    const campaign = { identity: args.identity, intent_sha256: intent, message: args.message, recipients }; journal.outreach[args.identity] = campaign; return campaign;
  });
}

export async function reuseOrBuildRecipient(args: { outDir: string; issue: number; campaign: string; npub: string; intent: unknown; build: () => Promise<SignedEvent> }): Promise<SignedEvent> {
  const intentHash = sha256(stableJson(args.intent));
  return mutateJournalAsync(args.outDir, args.issue, async (journal) => {
    const recipient = journal.outreach[args.campaign]?.recipients[args.npub]; if (!recipient) throw new Error("Recipient is not in canonical campaign"); const effect = recipient.effect;
    if (effect.intent_sha256 !== "unprepared" && effect.intent_sha256 !== intentHash && ["attempted", "ambiguous", "confirmed"].includes(effect.state)) throw new Error("Recipient intent changed after send started");
    if (effect.intent_sha256 === intentHash && effect.payload_path && effect.payload_sha256) { const bytes = await readFile(effect.payload_path); if (sha256(bytes) !== effect.payload_sha256) throw new Error("Outreach signed payload hash mismatch"); return JSON.parse(bytes.toString()) as SignedEvent; }
    const event = await args.build(); const path = join(args.outDir, String(args.issue), "outreach", args.campaign, `${args.npub}.json`); const bytes = JSON.stringify(event, null, 2); await writeAtomic(path, bytes);
    recipient.effect = { state: "prepared", intent_sha256: intentHash, payload_path: path, payload_sha256: sha256(bytes), event_id: event.id, receipts: {} }; return event;
  });
}

export async function markRecipientAttempt(outDir: string, issue: number, campaign: string, npub: string): Promise<void> {
  await mutateJournal(outDir, issue, (j) => { j.outreach[campaign].recipients[npub].effect.state = "attempted"; });
}
export async function recordRecipientReceipt(outDir: string, issue: number, campaign: string, npub: string, receipt: RelayReceipt): Promise<void> {
  await mutateJournal(outDir, issue, (j) => {
    const effect = j.outreach[campaign].recipients[npub].effect;
    effect.receipts ??= {};
    effect.receipts[receipt.relay] = { ...receipt, recorded_at: new Date().toISOString() };
  });
}
export async function recordRecipientReadback(outDir: string, issue: number, campaign: string, npub: string, relay: string, found: boolean): Promise<void> {
  await mutateJournal(outDir, issue, (journal) => {
    const effect = journal.outreach[campaign].recipients[npub].effect; effect.readbacks ??= {}; effect.readbacks[relay] = { found, recorded_at: new Date().toISOString() };
  });
}
export async function finishRecipient(outDir: string, issue: number, campaign: string, npub: string, state: "confirmed" | "failed" | "ambiguous", error?: string): Promise<void> {
  await mutateJournal(outDir, issue, (j) => {
    const effect = j.outreach[campaign].recipients[npub].effect;
    effect.state = state;
    effect.error = error;
  });
}
