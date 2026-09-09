import { readFile } from "node:fs/promises";
import { join } from "node:path";
import type { SignedEvent } from "./bunker.ts";
import type { RelayReceipt } from "./relays.ts";
import { mutateJournal, mutateJournalAsync, sha256, stableJson, type OutreachCampaign } from "./journal.ts";
import { writeAtomic } from "./safety.ts";

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
