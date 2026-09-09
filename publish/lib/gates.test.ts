import { expect, test } from "bun:test";
import { mkdtemp, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { loadJournal, loadOrCreateJournal, saveJournal, sha256 } from "./journal.ts";
import { QUALITY_ROLES, recordButtondownDisposition, recordCompositeQuality, recordFeedbackSnapshot } from "./gates.ts";

async function fixture() { const out = await mkdtemp(join(tmpdir(), "compass-gates-")); const source = join(out, "source.md"); await writeFile(source, "content"); const journal = await loadOrCreateJournal(out, 1); journal.source = { path: source, sha256: sha256("content") }; journal.pull_request = { number: 1, head_sha: "a".repeat(40), base_sha: "b".repeat(40) }; await saveJournal(out, journal); return { out, source }; }
const common = { schema_version: 1, verdict: "PASS", revision: "a".repeat(40), content_sha256: sha256("content"), input_sha256: "c".repeat(64), output_sha256: "d".repeat(64), checker_version: "checker-v1", provider: "provider", model: "model", checks: [{ command_sha256: "e".repeat(64), exit_code: 0, input_sha256: "c".repeat(64), output_sha256: "d".repeat(64) }], findings: [], unresolved_count: 0 };
async function makeEditorialApproval(out: string) {
  const source_freshness = [];
  const manifestFamilies: Record<string, any> = {};
  const since = "2026-09-01T16:00:00Z";
  const until = "2026-09-08T16:00:00Z";
  for (const family of ["projects", "nip-discussions", "nostr-recap", "shakespeare-apps", "nip34", "zapstore", "app-discovery", "heartbeats", "monthly-history", "specs"]) {
    const status = family === "monthly-history" ? "not_applicable" : family === "projects" ? "complete" : "empty_verified";
    const candidate_ids = family === "projects" ? ["repo:noise"] : [];
    const dispositions = family === "projects" ? { "repo:noise": { decision: "skip", reason: "outside exact source window" } } : {};
    const skip_evidence = family === "projects" ? [{ candidate_id: "repo:noise", reason: "outside exact source window" }] : [];
    const collectorPath = join(out, `collector-source-${family}.ts`); const collectorRaw = `collector:${family}`; await writeFile(collectorPath, collectorRaw);
    const artifactPath = status === "not_applicable" ? null : join(out, `artifact-${family}.json`);
    const artifactRaw = status === "not_applicable" ? null : JSON.stringify({ family, candidates: candidate_ids });
    if (artifactPath && artifactRaw !== null) await writeFile(artifactPath, artifactRaw);
    const canonical_query = { family, pass_id: "pass-1", since, until };
    const pagination_complete = status !== "not_applicable";
    const receipt = {
      pass_id: "pass-1", family, status,
      artifact_path: artifactPath, artifact_sha256: artifactRaw === null ? null : sha256(artifactRaw),
      collector_path: collectorPath, canonical_query, pagination_complete,
      item_count: candidate_ids.length, page_count: status === "not_applicable" ? 0 : 1,
      include_count: 0, skip_count: skip_evidence.length, skip_evidence, candidate_ids, dispositions,
    };
    const receipt_path = join(out, `collector-${family}.json`); const raw = JSON.stringify(receipt); await writeFile(receipt_path, raw);
    source_freshness.push({ family, pass_id: "pass-1", effective_since: since, effective_until: until, status, receipt_path, receipt_sha256: sha256(raw) });
    manifestFamilies[family] = {
      pass_id: "pass-1", status, window: { since, until }, canonical_query, pagination_complete,
      item_count: receipt.item_count, page_count: receipt.page_count, include_count: 0,
      skip_count: receipt.skip_count, skip_evidence, candidate_ids, dispositions,
      collector: collectorPath, collector_sha256: sha256(collectorRaw),
      artifact_path: artifactPath, artifact_sha256: receipt.artifact_sha256,
    };
  }
  const families = Object.keys(manifestFamilies);
  const sourceManifestPath = join(out, "source-manifest.json"); const sourceManifestRaw = JSON.stringify({ schema_version: 2, pass_id: "pass-1", expected_families: families, families: manifestFamilies, finalized: true }); await writeFile(sourceManifestPath, sourceManifestRaw);
  const ledgerPath = join(out, "selection-ledger.json"); const ledgerRaw = JSON.stringify({ schema_version: 1, source_pass_id: "pass-1", source_manifest_sha256: sha256(sourceManifestRaw), draft_sha256: sha256("content"), selection_policy: { minimum_score: 8, maximum_score: 10, require_no_zero_axis: true, fixed_item_cap: null, qualified_items_must_publish: true }, hard_gate_fields: ["primary_evidence", "in_window_progress", "nostr_surface", "continuity_delta"], score_axes: ["nostr_significance", "user_operator_impact", "novelty", "evidence_maturity", "explanatory_value"], source_expansion: [], candidates: [], final: true }); await writeFile(ledgerPath, ledgerRaw);
  const draftPath = join(out, "source.md"); const draftRaw = await Bun.file(draftPath).text();
  const coverage = { schema_version: 1, receipt_type: "selection-coverage", verdict: "PASS", checker_version: "selection-coverage-v1", source_pass_id: "pass-1", source_manifest_path: sourceManifestPath, source_manifest_sha256: sha256(sourceManifestRaw), ledger_path: ledgerPath, ledger_sha256: sha256(ledgerRaw), draft_path: draftPath, draft_sha256: sha256(draftRaw), retained_source_candidate_count: 0, editorial_candidate_count: 0, qualified_candidate_count: 0, selected_candidate_count: 0, skipped_candidate_count: 0, unresolved_count: 0, final: true };
  const coveragePath = join(out, "selection-coverage-receipt.json"); const coverageRaw = JSON.stringify(coverage); await writeFile(coveragePath, coverageRaw);
  return {
  source_freshness,
  selection_coverage: { receipt_path: coveragePath, receipt_sha256: sha256(coverageRaw) },
  practical_assessment: { question: "Which implementation path best fits Compass readers?", alternatives: [{ id: "a", evidence_url: "https://example.com/a" }, { id: "b", evidence_url: "https://example.com/b" }], selected: "a", rationale: "Primary evidence supports the selected interoperable path.", supporting_evidence_urls: ["https://example.com/evidence"], confidence: "high" },
  deep_dive: { mode: "regular", nips: [{ nip: "NIP-57", merged: true, spec_url: "https://github.com/nostr-protocol/nips/blob/master/57.md", current_activity_url: "https://github.com/nostr-protocol/nips/commits/master/57.md" }, { nip: "NIP-61", merged: true, spec_url: "https://github.com/nostr-protocol/nips/blob/master/61.md", current_activity_url: "https://github.com/nostr-protocol/nips/commits/master/61.md" }], implementations: [{ name: "A", evidence_url: "https://example.com/impl-a" }, { name: "B", evidence_url: "https://example.com/impl-b" }, { name: "C", evidence_url: "https://example.com/impl-c" }] },
  approved_by: "selection-review", approved_at: "2026-09-08T17:00:00Z",
  } as const;
}

test("five structured role receipts produce a revision/content-bound composite", async () => {
  const { out, source } = await fixture(); const paths: any = {}; const editorialApproval = await makeEditorialApproval(out);
  for (const role of QUALITY_ROLES) { paths[role] = join(out, `${role}.json`); await writeFile(paths[role], JSON.stringify({ ...common, receipt_type: "quality-role", role, ...(role === "continuity_value" ? { editorial_approval: editorialApproval } : {}), final: true }, null, 2)); }
  const composite = await recordCompositeQuality(out, 1, source, paths); expect((await loadJournal(out, 1)).effects.quality.payload_path).toBe(composite);
  await writeFile(source, "changed"); await expect(recordCompositeQuality(out, 1, source, paths)).rejects.toThrow("content");
});

test("old PASS followed by FAIL cannot satisfy final-position enforcement", async () => {
  const { out, source } = await fixture(); const paths: any = {}; const editorialApproval = await makeEditorialApproval(out);
  for (const role of QUALITY_ROLES) { paths[role] = join(out, `${role}.json`); await writeFile(paths[role], JSON.stringify({ ...common, receipt_type: "quality-role", role, ...(role === "continuity_value" ? { editorial_approval: editorialApproval } : {}), final: true }, null, 2)); }
  await writeFile(paths.links, `${JSON.stringify({ ...common, receipt_type: "quality-role", role: "links", final: true })}\n${JSON.stringify({ ...common, receipt_type: "quality-role", role: "links", verdict: "FAIL", final: true })}`);
  await expect(recordCompositeQuality(out, 1, source, paths)).rejects.toThrow("one structured JSON object");
});

test("rejects shallow practical selection and a deep dive without three implementations", async () => {
  const { out, source } = await fixture(); const paths: any = {}; const editorialApproval = await makeEditorialApproval(out);
  for (const role of QUALITY_ROLES) {
    const bad = role === "continuity_value" ? { ...editorialApproval, practical_assessment: { ...editorialApproval.practical_assessment, alternatives: [editorialApproval.practical_assessment.alternatives[0]] }, deep_dive: { ...editorialApproval.deep_dive, implementations: editorialApproval.deep_dive.implementations.slice(0, 2) } } : undefined;
    paths[role] = join(out, `${role}.json`);
    await writeFile(paths[role], JSON.stringify({ ...common, receipt_type: "quality-role", role, ...(bad ? { editorial_approval: bad } : {}), final: true }, null, 2));
  }
  await expect(recordCompositeQuality(out, 1, source, paths)).rejects.toThrow("continuity_value");
});

test("feedback snapshot binds material feedback and rejects holds", async () => {
  const { out, source } = await fixture(); const path = join(out, "feedback.json");
  await writeFile(path, JSON.stringify({ ...common, receipt_type: "feedback", holds: ["owner"], material_feedback_sha256: "d".repeat(64), final: true }, null, 2)); await expect(recordFeedbackSnapshot(out, 1, source, path)).rejects.toThrow("hold");
  await writeFile(path, JSON.stringify({ ...common, receipt_type: "feedback", holds: [], material_feedback_sha256: "d".repeat(64), final: true }, null, 2)); await recordFeedbackSnapshot(out, 1, source, path); expect((await loadJournal(out, 1)).effects.feedback.state).toBe("confirmed");
});

test("coverage receipt is exact-draft bound and cannot declare an item cap", async () => {
  const { out, source } = await fixture(); const paths: any = {}; const editorialApproval: any = await makeEditorialApproval(out);
  const coveragePath = editorialApproval.selection_coverage.receipt_path; const coverage = JSON.parse(await Bun.file(coveragePath).text()); const ledger = JSON.parse(await Bun.file(coverage.ledger_path).text()); ledger.selection_policy.fixed_item_cap = 12; const ledgerRaw = JSON.stringify(ledger); await writeFile(coverage.ledger_path, ledgerRaw); coverage.ledger_sha256 = sha256(ledgerRaw); const coverageRaw = JSON.stringify(coverage); await writeFile(coveragePath, coverageRaw); editorialApproval.selection_coverage.receipt_sha256 = sha256(coverageRaw);
  for (const role of QUALITY_ROLES) { paths[role] = join(out, `${role}.json`); await writeFile(paths[role], JSON.stringify({ ...common, receipt_type: "quality-role", role, ...(role === "continuity_value" ? { editorial_approval: editorialApproval } : {}), final: true }, null, 2)); }
  await expect(recordCompositeQuality(out, 1, source, paths)).rejects.toThrow("continuity_value");
});

test("coverage receipt cannot bless an unfinished source manifest", async () => {
  const { out, source } = await fixture(); const paths: any = {}; const editorialApproval: any = await makeEditorialApproval(out);
  const coveragePath = editorialApproval.selection_coverage.receipt_path; const coverage = JSON.parse(await Bun.file(coveragePath).text());
  const manifest = JSON.parse(await Bun.file(coverage.source_manifest_path).text()); manifest.finalized = false; const manifestRaw = JSON.stringify(manifest); await writeFile(coverage.source_manifest_path, manifestRaw);
  coverage.source_manifest_sha256 = sha256(manifestRaw); const coverageRaw = JSON.stringify(coverage); await writeFile(coveragePath, coverageRaw); editorialApproval.selection_coverage.receipt_sha256 = sha256(coverageRaw);
  const ledger = JSON.parse(await Bun.file(coverage.ledger_path).text()); ledger.source_manifest_sha256 = coverage.source_manifest_sha256; const ledgerRaw = JSON.stringify(ledger); await writeFile(coverage.ledger_path, ledgerRaw);
  coverage.ledger_sha256 = sha256(ledgerRaw); const finalCoverageRaw = JSON.stringify(coverage); await writeFile(coveragePath, finalCoverageRaw); editorialApproval.selection_coverage.receipt_sha256 = sha256(finalCoverageRaw);
  for (const role of QUALITY_ROLES) { paths[role] = join(out, `${role}.json`); await writeFile(paths[role], JSON.stringify({ ...common, receipt_type: "quality-role", role, ...(role === "continuity_value" ? { editorial_approval: editorialApproval } : {}), final: true }, null, 2)); }
  await expect(recordCompositeQuality(out, 1, source, paths)).rejects.toThrow("continuity_value");
});

test("coverage receipt counts must match the exact manifest and ledger", async () => {
  const { out, source } = await fixture(); const paths: any = {}; const editorialApproval: any = await makeEditorialApproval(out);
  const coveragePath = editorialApproval.selection_coverage.receipt_path; const coverage = JSON.parse(await Bun.file(coveragePath).text()); coverage.retained_source_candidate_count = 4;
  const coverageRaw = JSON.stringify(coverage); await writeFile(coveragePath, coverageRaw); editorialApproval.selection_coverage.receipt_sha256 = sha256(coverageRaw);
  for (const role of QUALITY_ROLES) { paths[role] = join(out, `${role}.json`); await writeFile(paths[role], JSON.stringify({ ...common, receipt_type: "quality-role", role, ...(role === "continuity_value" ? { editorial_approval: editorialApproval } : {}), final: true }, null, 2)); }
  await expect(recordCompositeQuality(out, 1, source, paths)).rejects.toThrow("continuity_value");
});

test("manifest cannot remove a maintained source family", async () => {
  const { out, source } = await fixture(); const paths: any = {}; const editorialApproval: any = await makeEditorialApproval(out);
  const coveragePath = editorialApproval.selection_coverage.receipt_path; const coverage = JSON.parse(await Bun.file(coveragePath).text());
  const manifest = JSON.parse(await Bun.file(coverage.source_manifest_path).text());
  manifest.expected_families = manifest.expected_families.filter((family: string) => family !== "specs");
  delete manifest.families.specs;
  const manifestRaw = JSON.stringify(manifest); await writeFile(coverage.source_manifest_path, manifestRaw);
  coverage.source_manifest_sha256 = sha256(manifestRaw);
  const ledger = JSON.parse(await Bun.file(coverage.ledger_path).text()); ledger.source_manifest_sha256 = coverage.source_manifest_sha256;
  const ledgerRaw = JSON.stringify(ledger); await writeFile(coverage.ledger_path, ledgerRaw); coverage.ledger_sha256 = sha256(ledgerRaw);
  const coverageRaw = JSON.stringify(coverage); await writeFile(coveragePath, coverageRaw); editorialApproval.selection_coverage.receipt_sha256 = sha256(coverageRaw);
  for (const role of QUALITY_ROLES) { paths[role] = join(out, `${role}.json`); await writeFile(paths[role], JSON.stringify({ ...common, receipt_type: "quality-role", role, ...(role === "continuity_value" ? { editorial_approval: editorialApproval } : {}), final: true }, null, 2)); }
  await expect(recordCompositeQuality(out, 1, source, paths)).rejects.toThrow("continuity_value");
});

test("required source family cannot be declared not applicable", async () => {
  const { out, source } = await fixture(); const paths: any = {}; const editorialApproval: any = await makeEditorialApproval(out);
  const freshness = editorialApproval.source_freshness.find((entry: any) => entry.family === "projects");
  const sourceReceipt = JSON.parse(await Bun.file(freshness.receipt_path).text());
  Object.assign(sourceReceipt, { status: "not_applicable", artifact_path: null, artifact_sha256: null, pagination_complete: false, item_count: 0, page_count: 0, include_count: 0, skip_count: 0, skip_evidence: [], candidate_ids: [], dispositions: {} });
  const sourceReceiptRaw = JSON.stringify(sourceReceipt); await writeFile(freshness.receipt_path, sourceReceiptRaw);
  freshness.status = "not_applicable"; freshness.receipt_sha256 = sha256(sourceReceiptRaw);
  const coveragePath = editorialApproval.selection_coverage.receipt_path; const coverage = JSON.parse(await Bun.file(coveragePath).text());
  const manifest = JSON.parse(await Bun.file(coverage.source_manifest_path).text());
  Object.assign(manifest.families.projects, { status: "not_applicable", artifact_path: null, artifact_sha256: null, pagination_complete: false, item_count: 0, page_count: 0, include_count: 0, skip_count: 0, skip_evidence: [], candidate_ids: [], dispositions: {} });
  const manifestRaw = JSON.stringify(manifest); await writeFile(coverage.source_manifest_path, manifestRaw); coverage.source_manifest_sha256 = sha256(manifestRaw);
  const ledger = JSON.parse(await Bun.file(coverage.ledger_path).text()); ledger.source_manifest_sha256 = coverage.source_manifest_sha256;
  const ledgerRaw = JSON.stringify(ledger); await writeFile(coverage.ledger_path, ledgerRaw); coverage.ledger_sha256 = sha256(ledgerRaw);
  const coverageRaw = JSON.stringify(coverage); await writeFile(coveragePath, coverageRaw); editorialApproval.selection_coverage.receipt_sha256 = sha256(coverageRaw);
  for (const role of QUALITY_ROLES) { paths[role] = join(out, `${role}.json`); await writeFile(paths[role], JSON.stringify({ ...common, receipt_type: "quality-role", role, ...(role === "continuity_value" ? { editorial_approval: editorialApproval } : {}), final: true }, null, 2)); }
  await expect(recordCompositeQuality(out, 1, source, paths)).rejects.toThrow("continuity_value");
});

test("manifest cannot remove a candidate retained by its exact freshness receipt", async () => {
  const { out, source } = await fixture(); const paths: any = {}; const editorialApproval: any = await makeEditorialApproval(out);
  const coveragePath = editorialApproval.selection_coverage.receipt_path; const coverage = JSON.parse(await Bun.file(coveragePath).text());
  const manifest = JSON.parse(await Bun.file(coverage.source_manifest_path).text());
  manifest.families.projects.candidate_ids = [];
  manifest.families.projects.dispositions = {};
  manifest.families.projects.item_count = 0;
  manifest.families.projects.skip_count = 0;
  manifest.families.projects.skip_evidence = [];
  const manifestRaw = JSON.stringify(manifest); await writeFile(coverage.source_manifest_path, manifestRaw);
  coverage.source_manifest_sha256 = sha256(manifestRaw);
  const ledger = JSON.parse(await Bun.file(coverage.ledger_path).text()); ledger.source_manifest_sha256 = coverage.source_manifest_sha256;
  const ledgerRaw = JSON.stringify(ledger); await writeFile(coverage.ledger_path, ledgerRaw); coverage.ledger_sha256 = sha256(ledgerRaw);
  const coverageRaw = JSON.stringify(coverage); await writeFile(coveragePath, coverageRaw); editorialApproval.selection_coverage.receipt_sha256 = sha256(coverageRaw);
  for (const role of QUALITY_ROLES) { paths[role] = join(out, `${role}.json`); await writeFile(paths[role], JSON.stringify({ ...common, receipt_type: "quality-role", role, ...(role === "continuity_value" ? { editorial_approval: editorialApproval } : {}), final: true }, null, 2)); }
  await expect(recordCompositeQuality(out, 1, source, paths)).rejects.toThrow("continuity_value");
});

test("coverage receipt cannot bless a candidate that fails deterministic selection policy", async () => {
  const { out, source } = await fixture(); const paths: any = {}; const editorialApproval: any = await makeEditorialApproval(out);
  const coveragePath = editorialApproval.selection_coverage.receipt_path; const coverage = JSON.parse(await Bun.file(coveragePath).text());
  const ledger = JSON.parse(await Bun.file(coverage.ledger_path).text());
  ledger.candidates = [{
    candidate_id: "bad", name: "Bad", reason: "included despite failing every gate",
    hard_gate: { primary_evidence: false, in_window_progress: false, nostr_surface: false, continuity_delta: false },
    scores: { nostr_significance: 0, user_operator_impact: 0, novelty: 0, evidence_maturity: 0, explanatory_value: 0 },
    triage: "GREEN", final_disposition: "include", primary_sources: [], draft_sources: [],
  }];
  const ledgerRaw = JSON.stringify(ledger); await writeFile(coverage.ledger_path, ledgerRaw); coverage.ledger_sha256 = sha256(ledgerRaw);
  Object.assign(coverage, { editorial_candidate_count: 1, qualified_candidate_count: 1, selected_candidate_count: 1, skipped_candidate_count: 0 });
  const coverageRaw = JSON.stringify(coverage); await writeFile(coveragePath, coverageRaw); editorialApproval.selection_coverage.receipt_sha256 = sha256(coverageRaw);
  for (const role of QUALITY_ROLES) { paths[role] = join(out, `${role}.json`); await writeFile(paths[role], JSON.stringify({ ...common, receipt_type: "quality-role", role, ...(role === "continuity_value" ? { editorial_approval: editorialApproval } : {}), final: true }, null, 2)); }
  await expect(recordCompositeQuality(out, 1, source, paths)).rejects.toThrow("continuity_value");
});

test("Buttondown is never implicit", async () => { const { out } = await fixture(); await expect(recordButtondownDisposition(out, 1, { status: "skipped", reason: "" })).rejects.toThrow("reason"); await recordButtondownDisposition(out, 1, { status: "skipped", reason: "operator did not authorize email" }); expect((await loadJournal(out, 1)).effects.buttondown.event_id).toBe("skipped"); });
