import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { IssueLock, writeAtomic } from "./safety.ts";
import type { SignedEvent, UnsignedEvent } from "./bunker.ts";

export const JOURNAL_SCHEMA_VERSION = 1;
export type EffectState = "prepared" | "attempted" | "confirmed" | "ambiguous" | "failed";
export type Effect = {
  state: EffectState;
  intent_sha256: string;
  payload_path?: string;
  payload_sha256?: string;
  event_id?: string;
  receipts?: Record<string, { ok: boolean; reason?: string; ms: number; recorded_at: string }>;
  readbacks?: Record<string, { found: boolean; recorded_at: string }>;
  disposition?: "no_dm" | "unknown_identity" | "missing_identity" | "no_nip17_inbox" | "failed" | "confirmed";
  error?: string;
};
export type PullRequestEvidence = {
  number: number;
  head_sha: string;
  base_sha: string;
  prospective_tree_sha?: string;
  base_guard?: { method: "branch-protection-strict" | "git-ref-cas"; base_ref: string; verified_at: string };
  merge_sha?: string;
  merge_tree_sha?: string;
};
export type DeploymentEvidence = {
  workflow_run_id: number;
  workflow_url: string;
  head_sha: string;
  tree_sha: string;
  page_url: string;
  content_sha256: string;
  verified_at: string;
};
export type PublicationJournal = {
  schema_version: 1;
  revision: number;
  issue: number;
  created_at: string;
  updated_at: string;
  source?: { path: string; sha256: string };
  pull_request?: PullRequestEvidence;
  deployment_intent?: { page_url: string; intent_sha256: string };
  deployment?: DeploymentEvidence;
  authorization?: { issue: number; phase_id: string; head_sha: string; base_sha: string; prospective_tree_sha: string; source_sha256: string; hold_version: string; not_before: string; final_feedback_scan_at: string; receipt_sha256: string; signer_pubkey: string; purpose: "weekly-publication"; allowed_event_kinds: number[]; edition_date: string };
  effects: Record<string, Effect>;
  outreach: Record<string, OutreachCampaign>;
};
export type OutreachCampaign = {
  identity: string;
  intent_sha256: string;
  message: string;
  recipients: Record<string, { npub?: string; names: string[]; effect: Effect }>;
};

export function sha256(value: string | Uint8Array): string {
  const h = new Bun.CryptoHasher("sha256"); h.update(value); return h.digest("hex");
}
export function stableJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(stableJson).join(",")}]`;
  if (value && typeof value === "object") return `{${Object.entries(value as Record<string, unknown>).sort(([a], [b]) => a.localeCompare(b)).map(([k, v]) => `${JSON.stringify(k)}:${stableJson(v)}`).join(",")}}`;
  return JSON.stringify(value);
}
export function journalPath(outDir: string, issue: number): string { return join(outDir, String(issue), "state.json"); }

function validateEffect(value: unknown, name: string): asserts value is Effect {
  if (!value || typeof value !== "object") throw new Error(`Malformed publication journal: effect ${name} is not an object`);
  const e = value as Partial<Effect>;
  if (!["prepared", "attempted", "confirmed", "ambiguous", "failed"].includes(e.state ?? "") || typeof e.intent_sha256 !== "string") throw new Error(`Malformed publication journal: invalid effect ${name}`);
}
export function validateJournal(value: unknown, issue: number): PublicationJournal {
  if (!value || typeof value !== "object") throw new Error("Malformed publication journal: root is not an object");
  const j = value as Partial<PublicationJournal>;
  if (j.schema_version !== JOURNAL_SCHEMA_VERSION) throw new Error(`Unsupported publication journal schema_version: ${String(j.schema_version)}`);
  if (!Number.isInteger(j.revision) || (j.revision ?? -1) < 0 || j.issue !== issue || !j.effects || typeof j.effects !== "object" || !j.outreach || typeof j.outreach !== "object") throw new Error("Malformed publication journal: required fields are missing or conflict with issue");
  for (const [name, effect] of Object.entries(j.effects)) validateEffect(effect, name);
  for (const [campaignName, campaign] of Object.entries(j.outreach)) {
    if (!campaign || typeof campaign !== "object" || typeof campaign.identity !== "string" || typeof campaign.intent_sha256 !== "string" || !campaign.recipients || typeof campaign.recipients !== "object") throw new Error(`Malformed publication journal: invalid outreach campaign ${campaignName}`);
    for (const [recipient, recipientValue] of Object.entries(campaign.recipients)) validateEffect(recipientValue?.effect, `outreach.${campaignName}.${recipient}`);
  }
  return j as PublicationJournal;
}

async function loadInternal(outDir: string, issue: number): Promise<PublicationJournal> {
  let raw: string;
  try { raw = await readFile(journalPath(outDir, issue), "utf8"); }
  catch (error) { throw new Error(`Publication journal missing for issue ${issue}: ${(error as Error).message}`); }
  try { return validateJournal(JSON.parse(raw), issue); }
  catch (error) { throw new Error(`Refusing publication with unreadable state.json: ${(error as Error).message}`); }
}
async function saveInternal(outDir: string, journal: PublicationJournal, expectedRevision: number): Promise<void> {
  if (journal.revision !== expectedRevision) throw new Error("Stale in-memory journal revision");
  try {
    const current = await loadInternal(outDir, journal.issue);
    if (current.revision !== expectedRevision) throw new Error(`Stale journal write: expected revision ${expectedRevision}, found ${current.revision}`);
  } catch (error) {
    if (expectedRevision !== 0 || !(error as Error).message.includes("journal missing")) throw error;
  }
  journal.revision = expectedRevision + 1;
  journal.updated_at = new Date().toISOString();
  validateJournal(journal, journal.issue);
  await writeAtomic(journalPath(outDir, journal.issue), JSON.stringify(journal, null, 2));
}
async function withJournalLock<T>(outDir: string, issue: number, operation: () => Promise<T>): Promise<T> {
  const lock = await IssueLock.acquire(issue, outDir, ".journal-lock");
  try { return await operation(); } finally { await lock.release(); }
}
export async function loadJournal(outDir: string, issue: number): Promise<PublicationJournal> { return loadInternal(outDir, issue); }
export async function loadOrCreateJournal(outDir: string, issue: number): Promise<PublicationJournal> {
  try { return await loadInternal(outDir, issue); }
  catch (error) {
    if (!(error as Error).message.includes("journal missing")) throw error;
    return withJournalLock(outDir, issue, async () => {
      try { return await loadInternal(outDir, issue); } catch (again) { if (!(again as Error).message.includes("journal missing")) throw again; }
      const now = new Date().toISOString();
      const journal: PublicationJournal = { schema_version: 1, revision: 0, issue, created_at: now, updated_at: now, effects: {}, outreach: {} };
      await saveInternal(outDir, journal, 0); return journal;
    });
  }
}
export async function saveJournal(outDir: string, journal: PublicationJournal): Promise<void> {
  await withJournalLock(outDir, journal.issue, () => saveInternal(outDir, journal, journal.revision));
}
export async function mutateJournalAsync<T>(outDir: string, issue: number, mutate: (journal: PublicationJournal) => Promise<T> | T): Promise<T> {
  return withJournalLock(outDir, issue, async () => {
    let journal: PublicationJournal;
    try { journal = await loadInternal(outDir, issue); }
    catch (error) {
      if (!(error as Error).message.includes("journal missing")) throw error;
      const now = new Date().toISOString(); journal = { schema_version: 1, revision: 0, issue, created_at: now, updated_at: now, effects: {}, outreach: {} };
    }
    const revision = journal.revision; const result = await mutate(journal); await saveInternal(outDir, journal, revision); return result;
  });
}
export async function mutateJournal(outDir: string, issue: number, mutate: (journal: PublicationJournal) => void): Promise<PublicationJournal> {
  return mutateJournalAsync(outDir, issue, (journal) => { mutate(journal); return journal; });
}

export async function confirmDeployment(outDir: string, issue: number, evidence: DeploymentEvidence): Promise<void> {
  if (!Number.isInteger(evidence.workflow_run_id) || evidence.workflow_run_id < 1 || !/^https:\/\//.test(evidence.workflow_url) || !/^[0-9a-f]{40}$/.test(evidence.head_sha) || !/^[0-9a-f]{40}$/.test(evidence.tree_sha) || !/^https:\/\//.test(evidence.page_url) || !/^[0-9a-f]{64}$/.test(evidence.content_sha256)) throw new Error("Invalid deployment confirmation evidence");
  await mutateJournal(outDir, issue, (journal) => {
    const pr = journal.pull_request;
    if (journal.effects.merge?.state !== "confirmed" || !pr?.merge_sha || evidence.head_sha !== pr.merge_sha || evidence.tree_sha !== pr.merge_tree_sha) throw new Error("Deployment evidence does not match the confirmed merge commit and resulting tree");
    journal.deployment = evidence;
    journal.effects.deploy = { state: "confirmed", intent_sha256: sha256(stableJson(evidence)), event_id: evidence.workflow_run_id.toString(), payload_sha256: evidence.content_sha256 };
  });
}

export async function prepareDeployment(outDir: string, issue: number, pageUrl: string): Promise<void> {
  if (!/^https:\/\/nostrcompass\.org\//.test(pageUrl)) throw new Error("Deployment page URL must be on canonical nostrcompass.org HTTPS origin");
  const intent = sha256(stableJson({ issue, page_url: pageUrl }));
  await mutateJournal(outDir, issue, (journal) => {
    if (journal.deployment_intent && journal.deployment_intent.intent_sha256 !== intent) throw new Error("Deployment route intent changed");
    journal.deployment_intent = { page_url: pageUrl, intent_sha256: intent };
  });
}

export async function reuseOrSign(args: { outDir: string; issue: number; effectName: string; unsigned: UnsignedEvent; payloadFile: string; intent?: unknown; signer: (event: UnsignedEvent) => Promise<SignedEvent> }): Promise<SignedEvent> {
  return withJournalLock(args.outDir, args.issue, async () => {
    let journal: PublicationJournal;
    try { journal = await loadInternal(args.outDir, args.issue); }
    catch (error) {
      if (!(error as Error).message.includes("journal missing")) throw error;
      const now = new Date().toISOString(); journal = { schema_version: 1, revision: 0, issue: args.issue, created_at: now, updated_at: now, effects: {}, outreach: {} };
    }
    const revision = journal.revision;
    const intent = sha256(stableJson(args.intent ?? args.unsigned)); const prior = journal.effects[args.effectName];
    if (prior) {
      if (prior.intent_sha256 !== intent && ["attempted", "ambiguous", "confirmed"].includes(prior.state)) throw new Error(`Refusing to regenerate ${args.effectName}: intent changed after downstream effects started`);
      if (prior.intent_sha256 === intent && prior.payload_path && prior.payload_sha256) {
        const bytes = await readFile(prior.payload_path); if (sha256(bytes) !== prior.payload_sha256) throw new Error(`Signed payload hash mismatch for ${args.effectName}`); return JSON.parse(bytes.toString()) as SignedEvent;
      }
    }
    const signed = await args.signer(args.unsigned); const bytes = JSON.stringify(signed, null, 2); await writeAtomic(args.payloadFile, bytes);
    journal.effects[args.effectName] = { state: "prepared", intent_sha256: intent, payload_path: args.payloadFile, payload_sha256: sha256(bytes), event_id: signed.id, receipts: {} };
    await saveInternal(args.outDir, journal, revision); return signed;
  });
}
