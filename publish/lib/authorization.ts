import { readFile } from "node:fs/promises";
import { loadJournal, mutateJournal, sha256, stableJson } from "./journal.ts";

type AuthorizationReceipt = {
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

export async function recordEditionAuthorization(outDir: string, issue: number, receiptPath: string): Promise<void> {
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
  if (now < new Date(auth.not_before) || new Date(auth.not_before).getUTCDay() !== 3 || new Date(auth.not_before).getUTCHours() < 16) throw new Error("merge is not admitted before Wednesday 16:00 UTC");
  if (auth.issue !== issue || auth.head_sha !== pr.head_sha || auth.base_sha !== pr.base_sha || auth.prospective_tree_sha !== prospectiveTree || auth.source_sha256 !== journal.source.sha256) throw new Error("merge authorization identity changed");
  if (sha256(await readFile(journal.source.path)) !== auth.source_sha256) throw new Error("publication source changed after authorization");
  for (const gate of ["quality", "feedback"] as const) {
    const effect = journal.effects[gate];
    if (effect?.state !== "confirmed" || effect.event_id !== pr.head_sha || !effect.payload_path || !effect.payload_sha256 || sha256(await readFile(effect.payload_path)) !== effect.payload_sha256) throw new Error(`merge requires current exact-head ${gate} evidence`);
  }
  if (new Date(auth.final_feedback_scan_at) < new Date(auth.not_before)) throw new Error("final feedback scan predates publication admission");
}

export async function assertSigningAuthorized(outDir: string, issue: number, kind: 1 | 30023, signerPubkey: string, now = new Date()): Promise<void> {
  const journal = await loadJournal(outDir, issue), auth = journal.authorization;
  const effect = journal.effects.authorization;
  if (!auth || effect?.state !== "confirmed") throw new Error("signing requires a scoped journaled edition authorization");
  if (!effect.payload_path || !effect.payload_sha256 || sha256(await readFile(effect.payload_path)) !== effect.payload_sha256 || effect.payload_sha256 !== auth.receipt_sha256) throw new Error("signing authorization receipt bytes changed");
  if (journal.effects.merge?.state !== "confirmed" || journal.effects.deploy?.state !== "confirmed") throw new Error("signing is not admitted before exact merge and deployment confirmation");
  if (auth.issue !== issue || auth.signer_pubkey !== signerPubkey || auth.purpose !== "weekly-publication" || !auth.allowed_event_kinds.includes(kind)) throw new Error("signing authorization does not cover this signer, purpose, or event kind");
  if (now < new Date(auth.not_before) || auth.edition_date !== auth.not_before.slice(0, 10) || now.toISOString().slice(0, 10) !== auth.edition_date) throw new Error("signing authorization is not for the current admitted Wednesday occurrence");
  if (!journal.pull_request || journal.pull_request.head_sha !== auth.head_sha || journal.pull_request.base_sha !== auth.base_sha || journal.pull_request.prospective_tree_sha !== auth.prospective_tree_sha || journal.source?.sha256 !== auth.source_sha256) throw new Error("signing authorization identity changed");
  if (sha256(await readFile(journal.source.path)) !== auth.source_sha256) throw new Error("publication source changed after signing authorization");
}
