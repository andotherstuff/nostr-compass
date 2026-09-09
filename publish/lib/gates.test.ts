import { expect, test } from "bun:test";
import { mkdtemp, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { loadJournal, loadOrCreateJournal, saveJournal, sha256 } from "./journal.ts";
import { QUALITY_ROLES, recordButtondownDisposition, recordCompositeQuality, recordFeedbackSnapshot } from "./gates.ts";

async function fixture() { const out = await mkdtemp(join(tmpdir(), "compass-gates-")); const source = join(out, "source.md"); await writeFile(source, "content"); const journal = await loadOrCreateJournal(out, 1); journal.source = { path: source, sha256: sha256("content") }; journal.pull_request = { number: 1, head_sha: "a".repeat(40), base_sha: "b".repeat(40) }; await saveJournal(out, journal); return { out, source }; }
const common = { schema_version: 1, verdict: "PASS", revision: "a".repeat(40), content_sha256: sha256("content"), input_sha256: "c".repeat(64), output_sha256: "d".repeat(64), checker_version: "checker-v1", provider: "provider", model: "model", checks: [{ command_sha256: "e".repeat(64), exit_code: 0, input_sha256: "c".repeat(64), output_sha256: "d".repeat(64) }], findings: [], unresolved_count: 0 };

test("five structured role receipts produce a revision/content-bound composite", async () => {
  const { out, source } = await fixture(); const paths: any = {};
  for (const role of QUALITY_ROLES) { paths[role] = join(out, `${role}.json`); await writeFile(paths[role], JSON.stringify({ ...common, receipt_type: "quality-role", role, final: true }, null, 2)); }
  const composite = await recordCompositeQuality(out, 1, source, paths); expect((await loadJournal(out, 1)).effects.quality.payload_path).toBe(composite);
  await writeFile(source, "changed"); await expect(recordCompositeQuality(out, 1, source, paths)).rejects.toThrow("content");
});

test("old PASS followed by FAIL cannot satisfy final-position enforcement", async () => {
  const { out, source } = await fixture(); const paths: any = {};
  for (const role of QUALITY_ROLES) { paths[role] = join(out, `${role}.json`); await writeFile(paths[role], JSON.stringify({ ...common, receipt_type: "quality-role", role, final: true }, null, 2)); }
  await writeFile(paths.links, `${JSON.stringify({ ...common, receipt_type: "quality-role", role: "links", final: true })}\n${JSON.stringify({ ...common, receipt_type: "quality-role", role: "links", verdict: "FAIL", final: true })}`);
  await expect(recordCompositeQuality(out, 1, source, paths)).rejects.toThrow("one structured JSON object");
});

test("feedback snapshot binds material feedback and rejects holds", async () => {
  const { out, source } = await fixture(); const path = join(out, "feedback.json");
  await writeFile(path, JSON.stringify({ ...common, receipt_type: "feedback", holds: ["owner"], material_feedback_sha256: "d".repeat(64), final: true }, null, 2)); await expect(recordFeedbackSnapshot(out, 1, source, path)).rejects.toThrow("hold");
  await writeFile(path, JSON.stringify({ ...common, receipt_type: "feedback", holds: [], material_feedback_sha256: "d".repeat(64), final: true }, null, 2)); await recordFeedbackSnapshot(out, 1, source, path); expect((await loadJournal(out, 1)).effects.feedback.state).toBe("confirmed");
});

test("Buttondown is never implicit", async () => { const { out } = await fixture(); await expect(recordButtondownDisposition(out, 1, { status: "skipped", reason: "" })).rejects.toThrow("reason"); await recordButtondownDisposition(out, 1, { status: "skipped", reason: "operator did not authorize email" }); expect((await loadJournal(out, 1)).effects.buttondown.event_id).toBe("skipped"); });
