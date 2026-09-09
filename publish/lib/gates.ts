import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { loadJournal, mutateJournal, sha256, stableJson } from "./journal.ts";
import { writeAtomic } from "./safety.ts";

export const QUALITY_ROLES = ["links", "claims", "prose", "topic_audit", "continuity_value"] as const;
type QualityRole = typeof QUALITY_ROLES[number];
type Check = { command_sha256: string; exit_code: number; input_sha256: string; output_sha256: string };
type Finding = { id: string; anchor: string; resolution: string; unresolved: boolean };
const SOURCE_FAMILIES = ["projects", "nip-discussions", "nostr-recap", "shakespeare-apps", "nip34", "zapstore", "app-discovery", "heartbeats", "monthly-history", "specs"] as const;
type SelectionCoveragePointer = { receipt_path: string; receipt_sha256: string };
type EditorialApproval = {
  source_freshness: { family: string; pass_id: string; effective_since: string; effective_until: string; status: "complete" | "empty_verified" | "not_applicable"; receipt_path: string; receipt_sha256: string }[];
  selection_coverage: SelectionCoveragePointer;
  practical_assessment: { question: string; alternatives: { id: string; evidence_url: string }[]; selected: string; rationale: string; supporting_evidence_urls: string[]; confidence: "low" | "medium" | "high" };
  deep_dive: { mode: "regular"; nips: { nip: string; merged: true; spec_url: string; current_activity_url: string }[]; implementations: { name: string; evidence_url: string }[] } | { mode: "monthly-history"; reason: string; evidence_url: string };
  approved_by: string;
  approved_at: string;
};
type RoleReceipt = { schema_version: 1; receipt_type: "quality-role"; role: QualityRole; verdict: "PASS" | "FAIL"; revision: string; content_sha256: string; input_sha256: string; output_sha256: string; checker_version: string; provider: string; model: string; checks: Check[]; findings: Finding[]; unresolved_count: number; editorial_approval?: EditorialApproval; final: true };
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
async function roleEvidenceValid(value: RoleReceipt): Promise<boolean> {
  if (!(hash(value.output_sha256) && Array.isArray(value.checks) && value.checks.length > 0 && value.checks.every((check) => hash(check.command_sha256) && check.exit_code === 0 && hash(check.input_sha256) && hash(check.output_sha256)) && Array.isArray(value.findings) && value.findings.every((finding) => finding.id && finding.anchor && finding.resolution && finding.unresolved === false) && value.unresolved_count === 0)) return false;
  if (value.role !== "continuity_value") return value.editorial_approval === undefined;
  const approval = value.editorial_approval;
  if (!approval || !approval.approved_by?.trim() || Number.isNaN(+new Date(approval.approved_at))) return false;
  const monthlyHistoryMode = approval.deep_dive?.mode === "monthly-history";
  const freshness = new Map(approval.source_freshness?.map((entry) => [entry.family, entry]));
  if (freshness.size !== SOURCE_FAMILIES.length || !SOURCE_FAMILIES.every((family) => {
    const entry = freshness.get(family);
    const applicable = family === "monthly-history"
      ? (monthlyHistoryMode ? /^(complete|empty_verified)$/.test(entry?.status ?? "") : entry?.status === "not_applicable")
      : /^(complete|empty_verified)$/.test(entry?.status ?? "");
    return entry && applicable && entry.pass_id && entry.receipt_path && hash(entry.receipt_sha256) && !Number.isNaN(+new Date(entry.effective_since)) && !Number.isNaN(+new Date(entry.effective_until)) && new Date(entry.effective_since) < new Date(entry.effective_until);
  })) return false;
  if (new Set([...freshness.values()].map((entry) => entry.pass_id)).size !== 1 || new Set([...freshness.values()].map((entry) => `${entry.effective_since}/${entry.effective_until}`)).size !== 1) return false;
  const freshnessReceipts = new Map<string, { raw: string; receipt: any }>();
  for (const [family, entry] of freshness) {
    let raw: string, receipt: any;
    try { raw = await readFile(entry.receipt_path, "utf8"); receipt = JSON.parse(raw); } catch { return false; }
    const paginationValid = receipt.status === "not_applicable" ? receipt.pagination_complete === false : receipt.pagination_complete === true;
    if (sha256(raw) !== entry.receipt_sha256 || receipt.family !== family || receipt.pass_id !== entry.pass_id || receipt.status !== entry.status || receipt.canonical_query?.family !== family || receipt.canonical_query?.pass_id !== entry.pass_id || receipt.canonical_query?.since !== entry.effective_since || receipt.canonical_query?.until !== entry.effective_until || !paginationValid || !Array.isArray(receipt.candidate_ids) || new Set(receipt.candidate_ids).size !== receipt.candidate_ids.length || typeof receipt.dispositions !== "object" || receipt.dispositions === null || Array.isArray(receipt.dispositions) || Object.keys(receipt.dispositions).length !== receipt.candidate_ids.length) return false;
    if (receipt.candidate_ids.some((candidateId: unknown) => typeof candidateId !== "string" || !candidateId || !receipt.dispositions[candidateId as string] || !/^(include|skip)$/.test(receipt.dispositions[candidateId as string].decision) || typeof receipt.dispositions[candidateId as string].reason !== "string" || !receipt.dispositions[candidateId as string].reason.trim())) return false;
    const includeCount = receipt.candidate_ids.filter((candidateId: string) => receipt.dispositions[candidateId].decision === "include").length;
    const skipCount = receipt.candidate_ids.length - includeCount;
    if (receipt.item_count !== receipt.candidate_ids.length || receipt.include_count !== includeCount || receipt.skip_count !== skipCount || !Array.isArray(receipt.skip_evidence) || receipt.skip_evidence.length !== skipCount) return false;
    freshnessReceipts.set(family, { raw, receipt });
  }
  const coveragePointer = approval.selection_coverage;
  if (!coveragePointer?.receipt_path || !hash(coveragePointer.receipt_sha256)) return false;
  let coverageRaw: string, coverage: any, manifestRaw: string, manifest: any, ledgerRaw: string, ledger: any, draftRaw: string;
  try {
    coverageRaw = await readFile(coveragePointer.receipt_path, "utf8"); coverage = JSON.parse(coverageRaw);
    manifestRaw = await readFile(coverage.source_manifest_path, "utf8"); manifest = JSON.parse(manifestRaw);
    ledgerRaw = await readFile(coverage.ledger_path, "utf8"); ledger = JSON.parse(ledgerRaw);
    draftRaw = await readFile(coverage.draft_path, "utf8");
  } catch { return false; }
  const passId = [...freshness.values()][0]?.pass_id;
  if (sha256(coverageRaw) !== coveragePointer.receipt_sha256 || coverage?.schema_version !== 1 || coverage.receipt_type !== "selection-coverage" || coverage.verdict !== "PASS" || coverage.checker_version !== "selection-coverage-v1" || coverage.source_pass_id !== passId || coverage.unresolved_count !== 0 || coverage.final !== true || sha256(manifestRaw) !== coverage.source_manifest_sha256 || sha256(ledgerRaw) !== coverage.ledger_sha256 || sha256(draftRaw) !== coverage.draft_sha256 || coverage.draft_sha256 !== value.content_sha256) return false;
  if (manifest?.schema_version !== 2 || manifest.pass_id !== passId || manifest.finalized !== true || !Array.isArray(manifest.expected_families) || new Set(manifest.expected_families).size !== SOURCE_FAMILIES.length || !SOURCE_FAMILIES.every((family) => manifest.expected_families.includes(family)) || typeof manifest.families !== "object" || manifest.families === null || Array.isArray(manifest.families) || new Set(Object.keys(manifest.families)).size !== SOURCE_FAMILIES.length || !SOURCE_FAMILIES.every((family) => Object.hasOwn(manifest.families, family))) return false;
  let retainedSourceCount = 0;
  for (const family of SOURCE_FAMILIES) {
    const entry = manifest.families[family]; const freshnessEntry = freshness.get(family); const freshnessReceipt = freshnessReceipts.get(family)?.receipt;
    if (!entry || !freshnessEntry || !freshnessReceipt || entry.pass_id !== passId || entry.status !== freshnessEntry.status || entry.window?.since !== freshnessEntry.effective_since || entry.window?.until !== freshnessEntry.effective_until || !Array.isArray(entry.candidate_ids) || new Set(entry.candidate_ids).size !== entry.candidate_ids.length || typeof entry.dispositions !== "object" || entry.dispositions === null || Array.isArray(entry.dispositions) || Object.keys(entry.dispositions).length !== entry.candidate_ids.length) return false;
    if (stableJson(entry.canonical_query) !== stableJson(freshnessReceipt.canonical_query) || entry.pagination_complete !== freshnessReceipt.pagination_complete || entry.item_count !== freshnessReceipt.item_count || entry.page_count !== freshnessReceipt.page_count || entry.include_count !== freshnessReceipt.include_count || entry.skip_count !== freshnessReceipt.skip_count || stableJson(entry.skip_evidence) !== stableJson(freshnessReceipt.skip_evidence) || stableJson(entry.candidate_ids) !== stableJson(freshnessReceipt.candidate_ids) || stableJson(entry.dispositions) !== stableJson(freshnessReceipt.dispositions)) return false;
    if (entry.collector !== freshnessReceipt.collector_path || !hash(entry.collector_sha256)) return false;
    try { if (sha256(await readFile(entry.collector)) !== entry.collector_sha256) return false; } catch { return false; }
    if (entry.status === "not_applicable") {
      if (entry.artifact_path !== null || entry.artifact_sha256 !== null || freshnessReceipt.artifact_path !== null || freshnessReceipt.artifact_sha256 !== null) return false;
    } else {
      if (entry.artifact_path !== freshnessReceipt.artifact_path || entry.artifact_sha256 !== freshnessReceipt.artifact_sha256 || !hash(entry.artifact_sha256)) return false;
      try { if (sha256(await readFile(entry.artifact_path)) !== entry.artifact_sha256) return false; } catch { return false; }
    }
    for (const candidateId of entry.candidate_ids) {
      const disposition = entry.dispositions[candidateId];
      if (typeof candidateId !== "string" || !candidateId || !disposition || !/^(include|skip)$/.test(disposition.decision) || typeof disposition.reason !== "string" || !disposition.reason.trim()) return false;
      if (disposition.decision === "include") retainedSourceCount += 1;
    }
  }
  const hardGateFields = ["primary_evidence", "in_window_progress", "nostr_surface", "continuity_delta"];
  const scoreAxes = ["nostr_significance", "user_operator_impact", "novelty", "evidence_maturity", "explanatory_value"];
  if (ledger?.schema_version !== 1 || ledger.source_pass_id !== passId || ledger.source_manifest_sha256 !== coverage.source_manifest_sha256 || ledger.draft_sha256 !== coverage.draft_sha256 || ledger.selection_policy?.minimum_score !== 8 || ledger.selection_policy?.maximum_score !== 10 || ledger.selection_policy?.require_no_zero_axis !== true || ledger.selection_policy?.fixed_item_cap !== null || ledger.selection_policy?.qualified_items_must_publish !== true || JSON.stringify(ledger.hard_gate_fields) !== JSON.stringify(hardGateFields) || JSON.stringify(ledger.score_axes) !== JSON.stringify(scoreAxes) || !Array.isArray(ledger.source_expansion) || !Array.isArray(ledger.candidates) || ledger.final !== true) return false;
  const selectedCount = ledger.candidates.filter((candidate: any) => /^(include|fold)$/.test(candidate?.final_disposition)).length;
  const skippedCount = ledger.candidates.filter((candidate: any) => candidate?.final_disposition === "skip").length;
  if (![coverage.retained_source_candidate_count, coverage.editorial_candidate_count, coverage.qualified_candidate_count, coverage.selected_candidate_count, coverage.skipped_candidate_count].every((count) => Number.isInteger(count) && count >= 0) || coverage.retained_source_candidate_count !== retainedSourceCount || coverage.editorial_candidate_count !== ledger.candidates.length || coverage.qualified_candidate_count !== selectedCount || coverage.selected_candidate_count !== selectedCount || coverage.skipped_candidate_count !== skippedCount || selectedCount + skippedCount !== ledger.candidates.length) return false;
  const practical = approval.practical_assessment;
  if (!practical?.question?.trim() || !practical.rationale?.trim() || !/^(low|medium|high)$/.test(practical.confidence) || !Array.isArray(practical.alternatives) || practical.alternatives.length < 2 || new Set(practical.alternatives.map((option) => option.id)).size !== practical.alternatives.length || !practical.alternatives.some((option) => option.id === practical.selected) || practical.alternatives.some((option) => !option.id || !/^https:\/\//.test(option.evidence_url)) || !Array.isArray(practical.supporting_evidence_urls) || practical.supporting_evidence_urls.length === 0 || practical.supporting_evidence_urls.some((url) => !/^https:\/\//.test(url))) return false;
  const dive = approval.deep_dive;
  if (dive?.mode === "monthly-history") return Boolean(dive.reason?.trim() && /^https:\/\//.test(dive.evidence_url));
  return Boolean(dive?.mode === "regular" && Array.isArray(dive.nips) && dive.nips.length === 2 && new Set(dive.nips.map((item) => item.nip)).size === 2 && dive.nips.every((item) => /^NIP-\d+$/.test(item.nip) && item.merged === true && /^https:\/\//.test(item.spec_url) && /^https:\/\//.test(item.current_activity_url)) && Array.isArray(dive.implementations) && dive.implementations.length >= 3 && new Set(dive.implementations.map((item) => item.name)).size >= 3 && dive.implementations.every((item) => item.name?.trim() && /^https:\/\//.test(item.evidence_url)));
}

export async function recordCompositeQuality(outDir: string, issue: number, sourcePath: string, receiptPaths: Record<QualityRole, string>): Promise<string> {
  const journal = await loadJournal(outDir, issue); const head = journal.pull_request?.head_sha; if (!head) throw new Error("quality receipts require a pinned PR head");
  const content = await readFile(sourcePath); const contentHash = sha256(content); const roleHashes: Record<string, string> = {};
  for (const role of QUALITY_ROLES) {
    const parsed = await parseFinal<RoleReceipt>(receiptPaths[role]); const value = parsed.value;
    if (!commonValid(value) || !(await roleEvidenceValid(value)) || value.receipt_type !== "quality-role" || value.role !== role || value.verdict !== "PASS") throw new Error(`invalid final ${role} quality receipt`);
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
