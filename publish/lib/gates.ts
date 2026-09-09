import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { loadJournal, mutateJournal, sha256, stableJson } from "./journal.ts";
import { writeAtomic } from "./safety.ts";

export const QUALITY_ROLES = ["links", "claims", "prose", "topic_audit", "continuity_value"] as const;
type QualityRole = typeof QUALITY_ROLES[number];
type Check = { command_sha256: string; exit_code: number; input_sha256: string; output_sha256: string };
type Finding = { id: string; anchor: string; resolution: string; unresolved: boolean };
type RoleReceipt = { schema_version: 1; receipt_type: "quality-role"; role: QualityRole; verdict: "PASS" | "FAIL"; revision: string; content_sha256: string; input_sha256: string; output_sha256: string; checker_version: string; provider: string; model: string; checks: Check[]; findings: Finding[]; unresolved_count: number; final: true };
type FeedbackReceipt = { schema_version: 1; receipt_type: "feedback"; verdict: "PASS" | "FAIL"; revision: string; content_sha256: string; input_sha256: string; checker_version: string; provider: string; model: string; holds: string[]; material_feedback_sha256: string; final: true };

async function parseFinal<T>(path: string): Promise<{ value: T; raw: string }> {
  const raw = await readFile(path, "utf8");
  if (!/"final"\s*:\s*true\s*}\s*$/.test(raw)) throw new Error("receipt must end with final:true as its final field");
  let value: unknown; try { value = JSON.parse(raw); } catch { throw new Error("receipt must be one structured JSON object"); }
  return { value: value as T, raw };
}
function hash(value: unknown): boolean { return typeof value === "string" && /^[0-9a-f]{64}$/.test(value); }
function commonValid(value: any): boolean {
  return value?.schema_version === 1 && /^(PASS|FAIL)$/.test(value.verdict) && /^[0-9a-f]{40}$/.test(value.revision) && hash(value.content_sha256) && hash(value.input_sha256) && typeof value.checker_version === "string" && value.checker_version.length > 0 && typeof value.provider === "string" && value.provider.length > 0 && typeof value.model === "string" && value.model.length > 0 && value.final === true;
}
function roleEvidenceValid(value: RoleReceipt): boolean {
  return hash(value.output_sha256) && Array.isArray(value.checks) && value.checks.length > 0 && value.checks.every((check) => hash(check.command_sha256) && check.exit_code === 0 && hash(check.input_sha256) && hash(check.output_sha256)) && Array.isArray(value.findings) && value.findings.every((finding) => finding.id && finding.anchor && finding.resolution && finding.unresolved === false) && value.unresolved_count === 0;
}

export async function recordCompositeQuality(outDir: string, issue: number, sourcePath: string, receiptPaths: Record<QualityRole, string>): Promise<string> {
  const journal = await loadJournal(outDir, issue); const head = journal.pull_request?.head_sha; if (!head) throw new Error("quality receipts require a pinned PR head");
  const content = await readFile(sourcePath); const contentHash = sha256(content); const roleHashes: Record<string, string> = {};
  for (const role of QUALITY_ROLES) {
    const parsed = await parseFinal<RoleReceipt>(receiptPaths[role]); const value = parsed.value;
    if (!commonValid(value) || !roleEvidenceValid(value) || value.receipt_type !== "quality-role" || value.role !== role || value.verdict !== "PASS") throw new Error(`invalid final ${role} quality receipt`);
    if (value.revision !== head || value.content_sha256 !== contentHash) throw new Error(`${role} quality receipt does not match exact head/content`);
    roleHashes[role] = sha256(parsed.raw);
  }
  const composite = { schema_version: 1, receipt_type: "quality-composite", issue, revision: head, content_sha256: contentHash, roles: roleHashes, verdict: "PASS", final: true };
  const path = join(outDir, String(issue), "quality-composite.json"); const raw = JSON.stringify(composite, null, 2); await writeAtomic(path, raw);
  await mutateJournal(outDir, issue, (current) => { if (current.pull_request?.head_sha !== head || current.source?.sha256 !== contentHash) throw new Error("quality inputs changed before commit"); current.effects.quality = { state: "confirmed", intent_sha256: sha256(stableJson(composite)), payload_path: path, payload_sha256: sha256(raw), event_id: head }; });
  return path;
}

export async function recordFeedbackSnapshot(outDir: string, issue: number, sourcePath: string, receiptPath: string): Promise<void> {
  const journal = await loadJournal(outDir, issue); const head = journal.pull_request?.head_sha; if (!head) throw new Error("feedback receipt requires a pinned PR head"); const contentHash = sha256(await readFile(sourcePath));
  const parsed = await parseFinal<FeedbackReceipt>(receiptPath); const value = parsed.value;
  if (!commonValid(value) || value.receipt_type !== "feedback" || value.verdict !== "PASS" || !Array.isArray(value.holds) || value.holds.length !== 0 || !/^[0-9a-f]{64}$/.test(value.material_feedback_sha256)) throw new Error("invalid final feedback receipt or unresolved hold");
  if (value.revision !== head || value.content_sha256 !== contentHash) throw new Error("feedback receipt does not match exact head/content");
  await mutateJournal(outDir, issue, (current) => { if (current.pull_request?.head_sha !== head || current.source?.sha256 !== contentHash) throw new Error("feedback inputs changed before commit"); current.effects.feedback = { state: "confirmed", intent_sha256: sha256(stableJson(value)), payload_path: receiptPath, payload_sha256: sha256(parsed.raw), event_id: head }; });
}

export async function recordButtondownDisposition(outDir: string, issue: number, disposition: { status: "sent"; external_id: string } | { status: "skipped"; reason: string }): Promise<void> {
  if (disposition.status === "sent" && !disposition.external_id.trim()) throw new Error("Buttondown sent disposition requires an external id");
  if (disposition.status === "skipped" && !disposition.reason.trim()) throw new Error("Buttondown skipped disposition requires a reason");
  await mutateJournal(outDir, issue, (journal) => { journal.effects.buttondown = { state: "confirmed", intent_sha256: sha256(stableJson(disposition)), event_id: disposition.status === "sent" ? disposition.external_id : "skipped" }; });
}
