import { describe, expect, test } from "bun:test";
import { mkdtemp } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { loadOrCreateJournal, saveJournal } from "../lib/journal.ts";
import { mergeIssue, pinPullRequest } from "./merge.ts";

async function setup() { const out = await mkdtemp(join(tmpdir(), "compass-merge-")); const j = await loadOrCreateJournal(out, 1); j.effects.article = { state: "confirmed", intent_sha256: "a" }; j.effects.announcement = { state: "confirmed", intent_sha256: "b" }; await saveJournal(out, j); return out; }
const head = "a".repeat(40), base = "b".repeat(40), merge = "c".repeat(40);
const view = (state = "OPEN", actualHead = head) => JSON.stringify({ number: 7, state, mergeable: "MERGEABLE", mergeStateStatus: "CLEAN", headRefOid: actualHead, baseRefOid: base, mergeCommit: state === "MERGED" ? { oid: merge } : null });

describe("exact PR merge", () => {
  test("passes expected head SHA and reconciles a lost success response", async () => {
    const out = await setup(); await pinPullRequest(out, 1, { number: 7, head_sha: head, base_sha: base }); let views = 0; const calls: string[][] = [];
    const run = async (_cmd: string, args: string[]) => { calls.push(args); if (args[1] === "view") return { code: 0, stdout: view(++views > 1 ? "MERGED" : "OPEN"), stderr: "" }; return { code: 1, stdout: "", stderr: "connection lost" }; };
    await mergeIssue(1, { reallyMerge: true, outDir: out, run });
    expect(calls.find((x) => x[1] === "merge")).toContain("--match-head-commit"); expect(calls.find((x) => x[1] === "merge")).toContain(head);
  });
  test("refuses a changed head and reads an already-merged PR by number", async () => {
    const out = await setup(); await pinPullRequest(out, 1, { number: 7, head_sha: head, base_sha: base });
    const mismatch = async () => ({ code: 0, stdout: view("OPEN", "d".repeat(40)), stderr: "" });
    await expect(mergeIssue(1, { reallyMerge: true, outDir: out, run: mismatch })).rejects.toThrow("head no longer matches");
    const mergedRun = async () => ({ code: 0, stdout: view("MERGED"), stderr: "" });
    await mergeIssue(1, { reallyMerge: true, outDir: out, run: mergedRun });
  });
});
