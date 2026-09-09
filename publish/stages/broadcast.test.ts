import { describe, expect, setDefaultTimeout, test } from "bun:test";
setDefaultTimeout(20_000);
import { mkdtemp, readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { loadOrCreateJournal, saveJournal, sha256 } from "../lib/journal.ts";
import { broadcastIssue, relayFloor } from "./broadcast.ts";

const event = (id: string, kind: number) => ({ id, kind, pubkey: "b".repeat(64), sig: "c".repeat(128), created_at: 1, tags: kind === 30023 ? [["d", "newsletter-1"], ["published_at", "1"]] : [], content: "x" });
async function fixture() {
  const root = await mkdtemp(join(tmpdir(), "compass-broadcast-")); const out = join(root, "out"); const dir = join(out, "1");
  const articlePath = join(dir, "event.json");
  const announcementPath = join(dir, "announcement.json");
  const articleBytes = JSON.stringify(event("a".repeat(64), 30023));
  const announcementBytes = JSON.stringify(event("d".repeat(64), 1));
  await Bun.write(articlePath, articleBytes);
  await Bun.write(announcementPath, announcementBytes);
  await writeFile(join(root, "relays.json"), JSON.stringify({ relays: ["wss://one", "wss://two", "wss://three", "wss://four", "wss://five"] }));
  const state = await loadOrCreateJournal(out, 1);
  state.effects.article = { state: "prepared", intent_sha256: "i", payload_path: articlePath, payload_sha256: sha256(articleBytes), event_id: "a".repeat(64), receipts: {} };
  state.effects.announcement = { state: "prepared", intent_sha256: "i", payload_path: announcementPath, payload_sha256: sha256(announcementBytes), event_id: "d".repeat(64), receipts: {} };
  const mergeSha = "e".repeat(40), treeSha = "f".repeat(40), contentHash = "1".repeat(64);
  state.pull_request = { number: 1, head_sha: "a".repeat(40), base_sha: "b".repeat(40), merge_sha: mergeSha, merge_tree_sha: treeSha };
  state.effects.merge = { state: "confirmed", intent_sha256: "merge", event_id: mergeSha };
  state.deployment = { workflow_run_id: 7, workflow_url: "https://github.test/run/7", head_sha: mergeSha, tree_sha: treeSha, page_url: "https://example.test/newsletter", content_sha256: contentHash, verified_at: "2026-09-09T00:00:00Z" };
  state.effects.deploy = { state: "confirmed", intent_sha256: "deploy", event_id: "7", payload_sha256: contentHash };
  for (const gate of ["quality", "feedback"]) { const path = join(root, `${gate}.txt`); await writeFile(path, "GATE: PASS\n"); state.effects[gate] = { state: "confirmed", intent_sha256: gate, payload_path: path, payload_sha256: sha256("GATE: PASS\n") }; }
  state.effects.buttondown = { state: "confirmed", intent_sha256: "buttondown", event_id: "skipped" };
  await saveJournal(out, state); return { root, out };
}

describe("broadcast journal", () => {
  test("fails closed unless at least five relays can meet the floor", () => { expect(() => relayFloor(4)).toThrow("five"); expect(relayFloor(12)).toBe(5); expect(() => relayFloor(12, 4)).toThrow("between five"); });

  test("refuses broadcast without exact deployment evidence", async () => {
    const { root, out } = await fixture(); const statePath = join(out, "1", "state.json"); const state = JSON.parse(await readFile(statePath, "utf8")); delete state.deployment; await writeFile(statePath, JSON.stringify(state));
    await expect(broadcastIssue(1, true, { outDir: out, relaysPath: join(root, "relays.json"), ledgerPath: join(root, "published.json"), reader: async () => true, broadcaster: async () => [] })).rejects.toThrow("deployment");
  });
  test("persists receipt progress before a crash and resumes only missing receipts", async () => {
    const { root, out } = await fixture(); let first = true;
    const crashing = async (_event: any, relays: string[], onReceipt?: any) => { expect(relays).toEqual(["wss://one", "wss://two", "wss://three", "wss://four", "wss://five"]); await onReceipt({ relay: relays[0], ok: true, ms: 1 }); throw new Error("crash"); };
    await expect(broadcastIssue(1, true, { outDir: out, relaysPath: join(root, "relays.json"), ledgerPath: join(root, "published.json"), reader: async () => true, broadcaster: crashing })).rejects.toThrow("crash");
    const after = JSON.parse(await readFile(join(out, "1", "state.json"), "utf8")); expect(after.effects.article.receipts["wss://one"].ok).toBe(true); expect(after.effects.article.state).toBe("ambiguous");
    const seen: string[][] = [];
    const success = async (_event: any, relays: string[], onReceipt?: any) => { seen.push(relays); const receipts = relays.map((relay) => ({ relay, ok: true, ms: 1 })); for (const r of receipts) await onReceipt(r); return receipts; };
    await broadcastIssue(1, true, { outDir: out, relaysPath: join(root, "relays.json"), ledgerPath: join(root, "published.json"), reader: async () => true, broadcaster: success });
    expect(seen[0]).toEqual(["wss://two", "wss://three", "wss://four", "wss://five"]); expect(first).toBe(true);
  });
  test("acceptance without five independent readbacks never publishes", async () => {
    const { root, out } = await fixture();
    const accept = async (_event: any, relays: string[], onReceipt?: any) => { const receipts = relays.map((relay) => ({ relay, ok: true, ms: 1 })); for (const receipt of receipts) await onReceipt(receipt); return receipts; };
    await expect(broadcastIssue(1, true, { outDir: out, relaysPath: join(root, "relays.json"), ledgerPath: join(root, "published.json"), reader: async (relay) => relay !== "wss://five", broadcaster: accept })).rejects.toThrow("relay floor not met");
    expect(readFile(join(root, "published.json"), "utf8")).rejects.toThrow();
  });
  test("both exact event ids must independently meet the readback floor", async () => {
    const { root, out } = await fixture(); const articleId = "a".repeat(64);
    const accept = async (_event: any, relays: string[], onReceipt?: any) => { const receipts = relays.map((relay) => ({ relay, ok: true, ms: 1 })); for (const receipt of receipts) await onReceipt(receipt); return receipts; };
    await expect(broadcastIssue(1, true, { outDir: out, relaysPath: join(root, "relays.json"), ledgerPath: join(root, "published.json"), reader: async (_relay, eventId) => eventId === articleId, broadcaster: accept })).rejects.toThrow("announcement relay floor not met");
    expect(readFile(join(root, "published.json"), "utf8")).rejects.toThrow();
  });
  test("refuses a payload whose bytes no longer match the journal", async () => {
    const { root, out } = await fixture();
    await Bun.write(join(out, "1", "event.json"), JSON.stringify(event("a".repeat(64), 30023)) + "\n");
    const broadcaster = async () => { throw new Error("must not broadcast"); };
    await expect(broadcastIssue(1, true, { outDir: out, relaysPath: join(root, "relays.json"), ledgerPath: join(root, "published.json"), reader: async () => true, broadcaster })).rejects.toThrow("payload hash mismatch");
  });
});
