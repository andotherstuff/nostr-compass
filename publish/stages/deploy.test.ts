import { describe, expect, setDefaultTimeout, test } from "bun:test";
setDefaultTimeout(20_000);
import { mkdtemp, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { confirmDeployment, loadJournal, loadOrCreateJournal, prepareDeployment, saveJournal, sha256 } from "../lib/journal.ts";
import { verifyAndRecordDeployment } from "./deploy.ts";

const mergeSha = "a".repeat(40), treeSha = "b".repeat(40);
async function fixture() {
  const out = await mkdtemp(join(tmpdir(), "compass-deploy-")); const source = join(out, "source.md"); const sourceBytes = "Nostr Compass #42\n\nbody"; await writeFile(source, sourceBytes);
  const journal = await loadOrCreateJournal(out, 42); journal.source = { path: source, sha256: sha256(sourceBytes) }; journal.pull_request = { number: 7, head_sha: "c".repeat(40), base_sha: "d".repeat(40), prospective_tree_sha: treeSha, merge_sha: mergeSha, merge_tree_sha: treeSha }; journal.effects.merge = { state: "confirmed", intent_sha256: "merge", event_id: mergeSha }; await saveJournal(out, journal); await prepareDeployment(out, 42, "https://nostrcompass.org/en/newsletters/2026-09-09"); return out;
}

describe("deployment receipt", () => {
  test("records authenticated workflow, exact tree, and served content digest", async () => {
    const out = await fixture(); const page = "<html>Nostr Compass #42</html>";
    const run = async (_cmd: string, args: string[]) => args[0] === "run" ? { code: 0, stdout: JSON.stringify([{ databaseId: 99, url: "https://github.test/run/99", headSha: mergeSha, status: "completed", conclusion: "success", event: "push" }]), stderr: "" } : { code: 0, stdout: treeSha, stderr: "" };
    await verifyAndRecordDeployment(42, { outDir: out, pageUrl: "https://nostrcompass.org/en/newsletters/2026-09-09", run, fetcher: async () => new Response(page, { status: 200 }) });
    const journal = await loadJournal(out, 42); expect(journal.deployment?.workflow_run_id).toBe(99); expect(journal.deployment?.content_sha256).toBe(sha256(page)); expect(journal.effects.deploy.state).toBe("confirmed");
  });
  test("rejects forged or mismatched deployment evidence", async () => {
    const out = await fixture();
    await expect(confirmDeployment(out, 42, { workflow_run_id: 1, workflow_url: "https://github.test/run/1", head_sha: "f".repeat(40), tree_sha: treeSha, page_url: "https://nostrcompass.org/x", content_sha256: "0".repeat(64), verified_at: "2026-09-09T00:00:00Z" })).rejects.toThrow("does not match");
    const run = async (_cmd: string, args: string[]) => args[0] === "run" ? { code: 0, stdout: JSON.stringify([{ databaseId: 2, url: "https://github.test/run/2", headSha: mergeSha, status: "completed", conclusion: "success", event: "push" }]), stderr: "" } : { code: 0, stdout: "f".repeat(40), stderr: "" };
    await expect(verifyAndRecordDeployment(42, { outDir: out, pageUrl: "https://nostrcompass.org/en/newsletters/2026-09-09", run, fetcher: async () => new Response("Nostr Compass #42") })).rejects.toThrow("tree does not match");
  });
});
