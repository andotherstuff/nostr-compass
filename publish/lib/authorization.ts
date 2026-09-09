import { readFile } from "node:fs/promises";
import { loadJournal, mutateJournal, sha256, stableJson, type PublicationJournal } from "./journal.ts";

export type AuthorizationReceipt = {
  schema_version: 1;
  receipt_type: "edition-authorization";
  issue: number;
  phase_id: string;
  head_sha: string;
  base_sha: string;
  prospective_tree_sha: string;
  source_sha256: string;
  hold_version: string;
  not_before: string;
  final_feedback_scan_at: string;
  authorized_by: string;
  signer_pubkey: string;
  purpose: "weekly-publication";
  allowed_event_kinds: number[];
  edition_date: string;
  final: true;
};

async function assertCurrentGateEvidence(journal: Awaited<ReturnType<typeof loadJournal>>, headSha: string, operation: "merge" | "signing"): Promise<void> {
  for (const gate of ["quality", "feedback"] as const) {
    const effect = journal.effects[gate];
    if (effect?.state !== "confirmed" || effect.event_id !== headSha || !effect.payload_path || !effect.payload_sha256 || sha256(await readFile(effect.payload_path)) !== effect.payload_sha256) throw new Error(`${operation} requires current exact-head ${gate} evidence`);
  }
}

async function validateEditionAuthorizationReceipt(
  outDir: string,
  issue: number,
  receiptPath: string,
  journal?: PublicationJournal,
): Promise<{ receipt: AuthorizationReceipt; raw: string; kinds: number[] }> {
  const raw = await readFile(receiptPath, "utf8");
  if (!/"final"\s*:\s*true\s*}\s*$/.test(raw)) throw new Error("authorization receipt must end with final:true");
  let receipt: AuthorizationReceipt;
  try { receipt = JSON.parse(raw); } catch { throw new Error("authorization receipt must be one JSON object"); }
  const notBefore = new Date(receipt.not_before), scan = new Date(receipt.final_feedback_scan_at);
  const kinds = Array.isArray(receipt.allowed_event_kinds)
    ? [...new Set(receipt.allowed_event_kinds)].sort((a, b) => a - b)
    : [];
  if (
    receipt.schema_version !== 1 || receipt.receipt_type !== "edition-authorization" || receipt.issue !== issue ||
    !receipt.phase_id || !receipt.hold_version || !receipt.authorized_by || receipt.final !== true ||
    !/^[0-9a-f]{40}$/.test(receipt.head_sha) || !/^[0-9a-f]{40}$/.test(receipt.base_sha) ||
    !/^[0-9a-f]{40}$/.test(receipt.prospective_tree_sha) || !/^[0-9a-f]{64}$/.test(receipt.source_sha256) ||
    !/^[0-9a-f]{64}$/.test(receipt.signer_pubkey) || receipt.purpose !== "weekly-publication" ||
    JSON.stringify(kinds) !== "[1,30023]" || !/^\d{4}-\d{2}-\d{2}$/.test(receipt.edition_date) ||
    receipt.edition_date !== receipt.not_before.slice(0, 10) || Number.isNaN(+notBefore) ||
    notBefore.getUTCDay() !== 3 || notBefore.getUTCHours() < 16 || Number.isNaN(+scan) || scan < notBefore
  ) throw new Error("invalid scoped Wednesday edition authorization");
  const current = journal ?? await loadJournal(outDir, issue);
  if (current.pull_request?.head_sha !== receipt.head_sha || current.pull_request.base_sha !== receipt.base_sha || current.source?.sha256 !== receipt.source_sha256) throw new Error("authorization does not match pinned PR/source identity");
  if (current.pull_request.prospective_tree_sha && current.pull_request.prospective_tree_sha !== receipt.prospective_tree_sha) throw new Error("authorization does not match the pinned prospective merge tree");
  return { receipt, raw, kinds };
}

function receiptMatchesJournal(receipt: AuthorizationReceipt, kinds: number[], auth: NonNullable<PublicationJournal["authorization"]>): boolean {
  return receipt.issue === auth.issue && receipt.phase_id === auth.phase_id && receipt.head_sha === auth.head_sha && receipt.base_sha === auth.base_sha && receipt.prospective_tree_sha === auth.prospective_tree_sha && receipt.source_sha256 === auth.source_sha256 && receipt.hold_version === auth.hold_version && receipt.not_before === auth.not_before && receipt.final_feedback_scan_at === auth.final_feedback_scan_at && receipt.signer_pubkey === auth.signer_pubkey && receipt.purpose === auth.purpose && receipt.edition_date === auth.edition_date && stableJson(kinds) === stableJson(auth.allowed_event_kinds);
}

async function validateJournaledAuthorization(
  outDir: string,
  issue: number,
  journal: PublicationJournal,
  operation: "merge" | "signing" | "preview",
): Promise<AuthorizationReceipt> {
  const auth = journal.authorization; const effect = journal.effects.authorization;
  const prefix = `${operation} authorization receipt bytes changed or no longer match the current hold and edition identity`;
  if (!auth || effect?.state !== "confirmed" || !effect.payload_path || !effect.payload_sha256) throw new Error(prefix);
  let validated: Awaited<ReturnType<typeof validateEditionAuthorizationReceipt>>;
  try { validated = await validateEditionAuthorizationReceipt(outDir, issue, effect.payload_path, journal); }
  catch (error) { throw new Error(`${prefix}: ${(error as Error).message}`); }
  const { receipt, raw, kinds } = validated;
  if (sha256(raw) !== effect.payload_sha256 || effect.payload_sha256 !== auth.receipt_sha256 || effect.intent_sha256 !== sha256(stableJson(receipt)) || !receiptMatchesJournal(receipt, kinds, auth)) throw new Error(prefix);
  return receipt;
}

export async function previewEditionAuthorization(outDir: string, issue: number, receiptPath: string): Promise<AuthorizationReceipt> {
  return (await validateEditionAuthorizationReceipt(outDir, issue, receiptPath)).receipt;
}

export async function previewJournaledEditionAuthorization(outDir: string, issue: number): Promise<AuthorizationReceipt> {
  const journal = await loadJournal(outDir, issue);
  return validateJournaledAuthorization(outDir, issue, journal, "preview");
}

export async function recordEditionAuthorization(outDir: string, issue: number, receiptPath: string): Promise<void> {
  const { receipt, raw, kinds } = await validateEditionAuthorizationReceipt(outDir, issue, receiptPath);
  await mutateJournal(outDir, issue, (journal) => {
    if (journal.pull_request?.head_sha !== receipt.head_sha || journal.pull_request.base_sha !== receipt.base_sha || journal.source?.sha256 !== receipt.source_sha256) throw new Error("authorization does not match pinned PR/source identity");
    journal.authorization = {
      issue, phase_id: receipt.phase_id, head_sha: receipt.head_sha, base_sha: receipt.base_sha,
      prospective_tree_sha: receipt.prospective_tree_sha, source_sha256: receipt.source_sha256,
      hold_version: receipt.hold_version, not_before: receipt.not_before,
      final_feedback_scan_at: receipt.final_feedback_scan_at, receipt_sha256: sha256(raw),
      signer_pubkey: receipt.signer_pubkey, purpose: receipt.purpose,
      allowed_event_kinds: kinds, edition_date: receipt.edition_date,
    };
    journal.effects.authorization = {
      state: "confirmed", intent_sha256: sha256(stableJson(receipt)), payload_path: receiptPath,
      payload_sha256: sha256(raw), event_id: receipt.phase_id,
    };
  });
}

export async function assertMergeAuthorized(outDir: string, issue: number, prospectiveTree: string, now = new Date()): Promise<void> {
  const journal = await loadJournal(outDir, issue), auth = journal.authorization, pr = journal.pull_request;
  if (!auth || journal.effects.authorization?.state !== "confirmed" || !pr || !journal.source) throw new Error("merge requires scoped journaled edition authorization");
  await validateJournaledAuthorization(outDir, issue, journal, "merge");
  if (now < new Date(auth.not_before) || new Date(auth.not_before).getUTCDay() !== 3 || new Date(auth.not_before).getUTCHours() < 16) throw new Error("merge is not admitted before Wednesday 16:00 UTC");
  if (auth.issue !== issue || auth.head_sha !== pr.head_sha || auth.base_sha !== pr.base_sha || auth.prospective_tree_sha !== prospectiveTree || auth.source_sha256 !== journal.source.sha256) throw new Error("merge authorization identity changed");
  if (sha256(await readFile(journal.source.path)) !== auth.source_sha256) throw new Error("publication source changed after authorization");
  await assertCurrentGateEvidence(journal, pr.head_sha, "merge");
  if (new Date(auth.final_feedback_scan_at) < new Date(auth.not_before)) throw new Error("final feedback scan predates publication admission");
}

export async function assertSigningAuthorized(outDir: string, issue: number, kind: 1 | 30023, signerPubkey: string, now = new Date()): Promise<void> {
  const journal = await loadJournal(outDir, issue), auth = journal.authorization;
  if (!auth || journal.effects.authorization?.state !== "confirmed") throw new Error("signing requires a scoped journaled edition authorization");
  await validateJournaledAuthorization(outDir, issue, journal, "signing");
  if (journal.effects.merge?.state !== "confirmed" || journal.effects.deploy?.state !== "confirmed") throw new Error("signing is not admitted before exact merge and deployment confirmation");
  if (auth.issue !== issue || auth.signer_pubkey !== signerPubkey || auth.purpose !== "weekly-publication" || !auth.allowed_event_kinds.includes(kind)) throw new Error("signing authorization does not cover this signer, purpose, or event kind");
  if (now < new Date(auth.not_before) || auth.edition_date !== auth.not_before.slice(0, 10)) throw new Error("signing authorization is not for the current admitted Wednesday occurrence");
  if (!journal.pull_request || journal.pull_request.head_sha !== auth.head_sha || journal.pull_request.base_sha !== auth.base_sha || journal.pull_request.prospective_tree_sha !== auth.prospective_tree_sha || journal.source?.sha256 !== auth.source_sha256) throw new Error("signing authorization identity changed");
  if (sha256(await readFile(journal.source.path)) !== auth.source_sha256) throw new Error("publication source changed after signing authorization");
  await assertCurrentGateEvidence(journal, auth.head_sha, "signing");
}
