import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { writeAtomic } from "./safety.ts";
import type { SignedEvent, UnsignedEvent } from "./bunker.ts";

export const JOURNAL_SCHEMA_VERSION = 1;
const mutationQueues = new Map<string, Promise<void>>();
export type EffectState = "prepared" | "attempted" | "confirmed" | "ambiguous" | "failed";
export type Effect = {
  state: EffectState;
  intent_sha256: string;
  payload_path?: string;
  payload_sha256?: string;
  event_id?: string;
  receipts?: Record<string, { ok: boolean; reason?: string; ms: number; recorded_at: string }>;
  error?: string;
};
export type PublicationJournal = {
  schema_version: 1;
  issue: number;
  created_at: string;
  updated_at: string;
  source?: { path: string; sha256: string };
  pull_request?: { number: number; head_sha: string; base_sha: string; merge_sha?: string };
  effects: Record<string, Effect>;
  outreach: Record<string, OutreachCampaign>;
};
export type OutreachCampaign = {
  identity: string;
  intent_sha256: string;
  message: string;
  recipients: Record<string, { npub: string; names: string[]; effect: Effect }>;
};

export function sha256(value: string | Uint8Array): string {
  const h = new Bun.CryptoHasher("sha256");
  h.update(value);
  return h.digest("hex");
}

export function stableJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(stableJson).join(",")}]`;
  if (value && typeof value === "object") {
    return `{${Object.entries(value as Record<string, unknown>).sort(([a], [b]) => a.localeCompare(b)).map(([k, v]) => `${JSON.stringify(k)}:${stableJson(v)}`).join(",")}}`;
  }
  return JSON.stringify(value);
}

export function journalPath(outDir: string, issue: number): string {
  return join(outDir, String(issue), "state.json");
}

function validateEffect(value: unknown, name: string): asserts value is Effect {
  if (!value || typeof value !== "object") throw new Error(`Malformed publication journal: effect ${name} is not an object`);
  const e = value as Partial<Effect>;
  if (!["prepared", "attempted", "confirmed", "ambiguous", "failed"].includes(e.state ?? "") || typeof e.intent_sha256 !== "string") {
    throw new Error(`Malformed publication journal: invalid effect ${name}`);
  }
}

export function validateJournal(value: unknown, issue: number): PublicationJournal {
  if (!value || typeof value !== "object") throw new Error("Malformed publication journal: root is not an object");
  const j = value as Partial<PublicationJournal>;
  if (j.schema_version !== JOURNAL_SCHEMA_VERSION) throw new Error(`Unsupported publication journal schema_version: ${String(j.schema_version)}`);
  if (j.issue !== issue || !j.effects || typeof j.effects !== "object" || !j.outreach || typeof j.outreach !== "object") {
    throw new Error("Malformed publication journal: required fields are missing or conflict with issue");
  }
  for (const [name, effect] of Object.entries(j.effects)) validateEffect(effect, name);
  for (const [campaignName, campaign] of Object.entries(j.outreach)) {
    if (!campaign || typeof campaign !== "object" || typeof campaign.identity !== "string" || typeof campaign.intent_sha256 !== "string" || !campaign.recipients || typeof campaign.recipients !== "object") {
      throw new Error(`Malformed publication journal: invalid outreach campaign ${campaignName}`);
    }
    for (const [recipient, value] of Object.entries(campaign.recipients)) validateEffect(value?.effect, `outreach.${campaignName}.${recipient}`);
  }
  return j as PublicationJournal;
}

export async function loadJournal(outDir: string, issue: number): Promise<PublicationJournal> {
  let raw: string;
  try { raw = await readFile(journalPath(outDir, issue), "utf8"); }
  catch (e) { throw new Error(`Publication journal missing for issue ${issue}: ${(e as Error).message}`); }
  try { return validateJournal(JSON.parse(raw), issue); }
  catch (e) { throw new Error(`Refusing publication with unreadable state.json: ${(e as Error).message}`); }
}

export async function loadOrCreateJournal(outDir: string, issue: number): Promise<PublicationJournal> {
  try { return await loadJournal(outDir, issue); }
  catch (e) {
    if (!(e as Error).message.includes("journal missing")) throw e;
    const now = new Date().toISOString();
    const journal: PublicationJournal = { schema_version: 1, issue, created_at: now, updated_at: now, effects: {}, outreach: {} };
    await saveJournal(outDir, journal);
    return journal;
  }
}

export async function saveJournal(outDir: string, journal: PublicationJournal): Promise<void> {
  validateJournal(journal, journal.issue);
  journal.updated_at = new Date().toISOString();
  await writeAtomic(journalPath(outDir, journal.issue), JSON.stringify(journal, null, 2));
}

export async function mutateJournal(outDir: string, issue: number, mutate: (j: PublicationJournal) => void): Promise<PublicationJournal> {
  const key = journalPath(outDir, issue);
  const previous = mutationQueues.get(key) ?? Promise.resolve();
  let result!: PublicationJournal;
  const run = previous.catch(() => undefined).then(async () => {
    const journal = await loadOrCreateJournal(outDir, issue);
    mutate(journal);
    await saveJournal(outDir, journal);
    result = journal;
  });
  const tail = run.then(() => undefined, () => undefined);
  mutationQueues.set(key, tail);
  try {
    await run;
    return result;
  } finally {
    if (mutationQueues.get(key) === tail) mutationQueues.delete(key);
  }
}

export async function reuseOrSign(args: {
  outDir: string; issue: number; effectName: string; unsigned: UnsignedEvent; payloadFile: string; intent?: unknown;
  signer: (event: UnsignedEvent) => Promise<SignedEvent>;
}): Promise<SignedEvent> {
  const intent = sha256(stableJson(args.intent ?? args.unsigned));
  const journal = await loadOrCreateJournal(args.outDir, args.issue);
  const prior = journal.effects[args.effectName];
  if (prior) {
    if (prior.intent_sha256 !== intent) {
      if (["attempted", "ambiguous", "confirmed"].includes(prior.state)) throw new Error(`Refusing to regenerate ${args.effectName}: intent changed after downstream effects started`);
    } else if (prior.payload_path && prior.payload_sha256) {
      const bytes = await readFile(prior.payload_path);
      if (sha256(bytes) !== prior.payload_sha256) throw new Error(`Signed payload hash mismatch for ${args.effectName}`);
      return JSON.parse(bytes.toString()) as SignedEvent;
    }
  }
  const signed = await args.signer(args.unsigned);
  const bytes = JSON.stringify(signed, null, 2);
  await writeAtomic(args.payloadFile, bytes);
  journal.effects[args.effectName] = { state: "prepared", intent_sha256: intent, payload_path: args.payloadFile, payload_sha256: sha256(bytes), event_id: signed.id, receipts: {} };
  await saveJournal(args.outDir, journal);
  return signed;
}
