import { expect, test } from "bun:test";
import { mkdtemp, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { loadOrCreateJournal, prepareDeployment, saveJournal, sha256 } from "../lib/journal.ts";
import { mergeIssue, pinPullRequest } from "./merge.ts";
import { verifyAndRecordDeployment } from "./deploy.ts";
import { broadcastIssue } from "./broadcast.ts";

const head = "a".repeat(40), base = "b".repeat(40), merge = "c".repeat(40), potential = "d".repeat(40), tree = "e".repeat(40);
const event = (id: string, kind: number) => ({ id, kind, pubkey: "f".repeat(64), sig: "0".repeat(128), created_at: 1, tags: kind === 30023 ? [["d", "newsletter-42"], ["published_at", "1"]] : [], content: "x" });

test("delayed Pages success resumes retained merge state and only then broadcasts", async () => {
  const root = await mkdtemp(join(tmpdir(), "compass-order-")); const out = join(root, "out"); const issueDir = join(out, "42"); const source = join(root, "42publish.md"); const pageUrl = "https://nostrcompass.org/en/newsletters/test";
  await writeFile(source, "Nostr Compass #42\n"); const article = JSON.stringify(event("1".repeat(64), 30023)); const announcement = JSON.stringify(event("2".repeat(64), 1)); await Bun.write(join(issueDir, "event.json"), article); await Bun.write(join(issueDir, "announcement.json"), announcement);
  const journal = await loadOrCreateJournal(out, 42); journal.source = { path: source, sha256: sha256("Nostr Compass #42\n") }; journal.effects.article = { state: "prepared", intent_sha256: "article", payload_path: join(issueDir, "event.json"), payload_sha256: sha256(article), event_id: "1".repeat(64), receipts: {} }; journal.effects.announcement = { state: "prepared", intent_sha256: "announcement", payload_path: join(issueDir, "announcement.json"), payload_sha256: sha256(announcement), event_id: "2".repeat(64), receipts: {} }; for (const gate of ["quality", "feedback"]) { const path = join(root, `${gate}.txt`); await writeFile(path, "GATE: PASS\n"); journal.effects[gate] = { state: "confirmed", intent_sha256: gate, event_id: head, payload_path: path, payload_sha256: sha256("GATE: PASS\n") }; } journal.effects.buttondown = { state: "confirmed", intent_sha256: "buttondown", event_id: "skipped" }; journal.effects.merge = { state: "prepared", intent_sha256: `7:${head}:${base}:${tree}` }; journal.pull_request = { number: 7, head_sha: head, base_sha: base, prospective_tree_sha: tree }; journal.authorization = { issue: 42, phase_id: "phase", head_sha: head, base_sha: base, prospective_tree_sha: tree, source_sha256: sha256("Nostr Compass #42\n"), hold_version: "hold-v1", not_before: "2020-01-01T16:00:00Z", final_feedback_scan_at: "2020-01-01T16:01:00Z", receipt_sha256: "f".repeat(64) }; journal.effects.authorization = { state: "confirmed", intent_sha256: "auth" }; await saveJournal(out, journal); await prepareDeployment(out, 42, pageUrl); await pinPullRequest(out, 42, { number: 7, head_sha: head, base_sha: base });
  let views = 0; const mergeRun = async (_cmd: string, args: string[]) => {
    if (args[0] === "pr" && args[1] === "view") return { code: 0, stdout: JSON.stringify({ number: 7, state: ++views > 1 ? "MERGED" : "OPEN", mergeable: "MERGEABLE", mergeStateStatus: "CLEAN", headRefOid: head, baseRefOid: base, baseRefName: "main", potentialMergeCommit: views === 1 ? { oid: potential } : null, mergeCommit: views > 1 ? { oid: merge } : null }), stderr: "" };
    if (args[0] === "api" && args[1].includes("branches/main/protection")) return { code: 0, stdout: "true", stderr: "" };
    if (args[0] === "api") return { code: 0, stdout: tree, stderr: "" };
    return { code: 0, stdout: "merged", stderr: "" };
  };
  await mergeIssue(42, { reallyMerge: true, outDir: out, run: mergeRun });
  const noRun = async (_cmd: string, args: string[]) => args[0] === "run" ? { code: 0, stdout: "[]", stderr: "" } : { code: 0, stdout: tree, stderr: "" };
  await expect(verifyAndRecordDeployment(42, { outDir: out, run: noRun, fetcher: async () => new Response("Nostr Compass #42") })).rejects.toThrow("No successful push deployment");
  await writeFile(join(root, "relays.json"), JSON.stringify({ relays: ["wss://1", "wss://2", "wss://3", "wss://4", "wss://5"], relay_floor: 5 })); let sends = 0;
  const broadcaster = async (_event: any, relays: string[], onReceipt?: any) => { sends++; const receipts = relays.map((relay) => ({ relay, ok: true, ms: 1 })); for (const receipt of receipts) await onReceipt(receipt); return receipts; };
  await expect(broadcastIssue(42, true, { outDir: out, relaysPath: join(root, "relays.json"), ledgerPath: join(root, "published.json"), reader: async () => true, broadcaster })).rejects.toThrow("deployment"); expect(sends).toBe(0);
  const successRun = async (_cmd: string, args: string[]) => args[0] === "run" ? { code: 0, stdout: JSON.stringify([{ databaseId: 9, url: "https://github.test/run/9", headSha: merge, status: "completed", conclusion: "success", event: "push" }]), stderr: "" } : { code: 0, stdout: tree, stderr: "" };
  await verifyAndRecordDeployment(42, { outDir: out, run: successRun, fetcher: async () => new Response("<h1>Nostr Compass #42</h1>") });
  await broadcastIssue(42, true, { outDir: out, relaysPath: join(root, "relays.json"), ledgerPath: join(root, "published.json"), reader: async () => true, broadcaster }); expect(sends).toBe(2);
});
