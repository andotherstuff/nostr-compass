import { describe, expect, test } from "bun:test";
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
  await writeFile(join(root, "relays.json"), JSON.stringify({ relays: ["wss://one", "wss://two", "wss://three"] }));
  const state = await loadOrCreateJournal(out, 1);
  state.effects.article = { state: "prepared", intent_sha256: "i", payload_path: articlePath, payload_sha256: sha256(articleBytes), event_id: "a".repeat(64), receipts: {} };
  state.effects.announcement = { state: "prepared", intent_sha256: "i", payload_path: announcementPath, payload_sha256: sha256(announcementBytes), event_id: "d".repeat(64), receipts: {} };
  await saveJournal(out, state); return { root, out };
}

describe("broadcast journal", () => {
  test("bounds the default floor by configured relay count", () => { expect(relayFloor(1)).toBe(1); expect(relayFloor(3)).toBe(2); });
  test("persists receipt progress before a crash and resumes only missing receipts", async () => {
    const { root, out } = await fixture(); let first = true;
    const crashing = async (_event: any, relays: string[], onReceipt?: any) => { expect(relays).toEqual(["wss://one", "wss://two", "wss://three"]); await onReceipt({ relay: relays[0], ok: true, ms: 1 }); throw new Error("crash"); };
    await expect(broadcastIssue(1, true, { outDir: out, relaysPath: join(root, "relays.json"), ledgerPath: join(root, "published.json"), broadcaster: crashing })).rejects.toThrow("crash");
    const after = JSON.parse(await readFile(join(out, "1", "state.json"), "utf8")); expect(after.effects.article.receipts["wss://one"].ok).toBe(true); expect(after.effects.article.state).toBe("ambiguous");
    const seen: string[][] = [];
    const success = async (_event: any, relays: string[], onReceipt?: any) => { seen.push(relays); const receipts = relays.map((relay) => ({ relay, ok: true, ms: 1 })); for (const r of receipts) await onReceipt(r); return receipts; };
    await broadcastIssue(1, true, { outDir: out, relaysPath: join(root, "relays.json"), ledgerPath: join(root, "published.json"), broadcaster: success });
    expect(seen[0]).toEqual(["wss://two", "wss://three"]); expect(first).toBe(true);
  });
  test("does not create compatibility ledger below relay floor", async () => {
    const { root, out } = await fixture();
    const fail = async (_event: any, relays: string[], onReceipt?: any) => { const receipts = relays.map((relay, i) => ({ relay, ok: i === 0, ms: 1 })); for (const r of receipts) await onReceipt(r); return receipts; };
    await expect(broadcastIssue(1, true, { outDir: out, relaysPath: join(root, "relays.json"), ledgerPath: join(root, "published.json"), broadcaster: fail })).rejects.toThrow("relay floor not met");
    expect(readFile(join(root, "published.json"), "utf8")).rejects.toThrow();
  });
  test("refuses a payload whose bytes no longer match the journal", async () => {
    const { root, out } = await fixture();
    await Bun.write(join(out, "1", "event.json"), JSON.stringify(event("a".repeat(64), 30023)) + "\n");
    const broadcaster = async () => { throw new Error("must not broadcast"); };
    await expect(broadcastIssue(1, true, { outDir: out, relaysPath: join(root, "relays.json"), ledgerPath: join(root, "published.json"), broadcaster })).rejects.toThrow("payload hash mismatch");
  });
});
