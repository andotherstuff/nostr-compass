import { describe, expect, test } from "bun:test";
import { mkdtemp, readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { loadJournal, loadOrCreateJournal, mutateJournal, reuseOrSign, saveJournal } from "./journal.ts";
import type { SignedEvent } from "./bunker.ts";

describe("publication journal", () => {
  test("creates a schema-versioned per-edition journal and fails closed on malformed state", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-journal-"));
    const journal = await loadOrCreateJournal(out, 42);
    expect(journal.schema_version).toBe(1);
    await writeFile(join(out, "42", "state.json"), "{bad");
    expect(loadJournal(out, 42)).rejects.toThrow("Refusing publication with unreadable state.json");
  });

  test("reuses exact signed bytes and refuses changed intent after an attempt", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-sign-"));
    const payload = join(out, "8", "event.json");
    let calls = 0;
    const signer = async (event: any) => {
      calls++;
      return { ...event, id: "a".repeat(64), pubkey: "b".repeat(64), sig: "c".repeat(128) } as SignedEvent;
    };
    const unsigned = { kind: 1, content: "same", tags: [], created_at: 1 };
    await reuseOrSign({ outDir: out, issue: 8, effectName: "article", unsigned, payloadFile: payload, signer });
    const bytes = await readFile(payload, "utf8");
    await reuseOrSign({ outDir: out, issue: 8, effectName: "article", unsigned, payloadFile: payload, signer });
    expect(calls).toBe(1);
    expect(await readFile(payload, "utf8")).toBe(bytes);
    const statePath = join(out, "8", "state.json");
    const state = JSON.parse(await readFile(statePath, "utf8"));
    state.effects.article.state = "attempted";
    await writeFile(statePath, JSON.stringify(state));
    expect(reuseOrSign({ outDir: out, issue: 8, effectName: "article", unsigned: { ...unsigned, content: "changed" }, payloadFile: payload, signer })).rejects.toThrow("intent changed");
  });

  test("serializes concurrent receipt mutations without losing updates", async () => {
    const outDir = await mkdtemp(join(tmpdir(), "compass-journal-race-"));
    const journal = await loadOrCreateJournal(outDir, 1);
    journal.effects.article = { state: "attempted", intent_sha256: "intent", receipts: {} };
    await saveJournal(outDir, journal);
    await Promise.all(["one", "two", "three"].map((relay) => mutateJournal(outDir, 1, (current) => {
      current.effects.article.receipts![relay] = { ok: true, ms: 1, recorded_at: "2026-09-09T00:00:00Z" };
    })));
    expect(Object.keys((await loadJournal(outDir, 1)).effects.article.receipts ?? {}).sort()).toEqual(["one", "three", "two"]);
  });
});
