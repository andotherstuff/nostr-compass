import { describe, expect, test } from "bun:test";
import { mkdtemp, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { loadOrCreateJournal, mutateJournal, prepareDeployment, saveJournal, sha256 } from "../lib/journal.ts";
import { mergeIssue, pinPullRequest } from "./merge.ts";

async function setup() { const out = await mkdtemp(join(tmpdir(), "compass-merge-")); const source = join(out, "source.md"), gate = join(out, "gate.json"); await writeFile(source, "source"); await writeFile(gate, "gate"); const journal = await loadOrCreateJournal(out, 1); journal.source = { path: source, sha256: sha256("source") }; journal.pull_request = { number: 7, head_sha: head, base_sha: base, prospective_tree_sha: tree }; journal.effects.merge = { state: "prepared", intent_sha256: `7:${head}:${base}:${tree}` }; for (const name of ["quality", "feedback"]) journal.effects[name] = { state: "confirmed", intent_sha256: name, event_id: head, payload_path: gate, payload_sha256: sha256("gate") }; journal.authorization = { issue: 1, phase_id: "phase", head_sha: head, base_sha: base, prospective_tree_sha: tree, source_sha256: sha256("source"), hold_version: "hold-v1", not_before: "2020-01-01T16:00:00Z", final_feedback_scan_at: "2020-01-01T16:01:00Z", receipt_sha256: "f".repeat(64) }; journal.effects.authorization = { state: "confirmed", intent_sha256: "auth" }; await saveJournal(out, journal); await prepareDeployment(out, 1, "https://nostrcompass.org/en/newsletters/test"); return out; }
const head = "a".repeat(40), base = "b".repeat(40), merge = "c".repeat(40), potential = "d".repeat(40), tree = "e".repeat(40);
const view = (state = "OPEN", actualHead = head) => JSON.stringify({ number: 7, state, mergeable: "MERGEABLE", mergeStateStatus: "CLEAN", headRefOid: actualHead, baseRefOid: base, baseRefName: "main", potentialMergeCommit: state === "OPEN" ? { oid: potential } : null, mergeCommit: state === "MERGED" ? { oid: merge } : null });
function runner(options: { mergedAfter?: boolean; loseReadback?: boolean; strict?: boolean } = {}) {
  let views = 0; const calls: string[][] = [];
  const run = async (_cmd: string, args: string[]) => {
    calls.push(args);
    if (args[0] === "pr" && args[1] === "view") {
      views++;
      if (options.loseReadback && views > 1) return { code: 1, stdout: "", stderr: "offline" };
      return { code: 0, stdout: view(options.mergedAfter && views > 1 ? "MERGED" : "OPEN"), stderr: "" };
    }
    if (args[0] === "api" && args[1].includes("/git/commits/")) return { code: 0, stdout: tree + "\n", stderr: "" };
    if (args[0] === "api" && args[1].includes("/protection")) return { code: options.strict === false ? 1 : 0, stdout: options.strict === false ? "" : "true\n", stderr: options.strict === false ? "not found" : "" };
    if (args[0] === "pr" && args[1] === "merge") return { code: 1, stdout: "", stderr: "connection lost" };
    return { code: 1, stdout: "", stderr: "unexpected" };
  };
  return { run, calls };
}

describe("exact PR merge", () => {
  test("passes expected head SHA and reconciles a lost success response by exact tree", async () => {
    const out = await setup(); await pinPullRequest(out, 1, { number: 7, head_sha: head, base_sha: base }); const { run, calls } = runner({ mergedAfter: true });
    expect(await mergeIssue(1, { reallyMerge: true, outDir: out, run })).toBe("confirmed");
    expect(calls.find((args) => args[1] === "merge")).toContain("--match-head-commit");
    expect(calls.find((args) => args[1] === "merge")).toContain(head);
  });
  test("refuses a changed head", async () => {
    const out = await setup(); await pinPullRequest(out, 1, { number: 7, head_sha: head, base_sha: base });
    await expect(mergeIssue(1, { reallyMerge: true, outDir: out, run: async () => ({ code: 0, stdout: view("OPEN", "f".repeat(40)), stderr: "" }) })).rejects.toThrow("head no longer matches");
  });
  test("fails closed when the server does not enforce base currentness", async () => {
    const out = await setup(); await pinPullRequest(out, 1, { number: 7, head_sha: head, base_sha: base }); const { run, calls } = runner({ strict: false });
    await expect(mergeIssue(1, { reallyMerge: true, outDir: out, run })).rejects.toThrow("server does not enforce");
    expect(calls.some((args) => args[1] === "merge")).toBe(false);
  });
  test("returns prepared without claiming a merge", async () => {
    const out = await setup(); await pinPullRequest(out, 1, { number: 7, head_sha: head, base_sha: base }); const { run, calls } = runner();
    expect(await mergeIssue(1, { reallyMerge: false, outDir: out, run })).toBe("prepared");
    expect(calls.some((args) => args[1] === "merge")).toBe(false);
  });
  test("persists ambiguity when authoritative post-merge readback fails", async () => {
    const out = await setup(); await pinPullRequest(out, 1, { number: 7, head_sha: head, base_sha: base }); const { run } = runner({ loseReadback: true });
    await expect(mergeIssue(1, { reallyMerge: true, outDir: out, run })).rejects.toThrow("gh pr view failed");
    expect((await loadOrCreateJournal(out, 1)).effects.merge.state).toBe("ambiguous");
  });
  test("reconciles an already-merged PR only with prior prospective tree evidence", async () => {
    const out = await setup(); await pinPullRequest(out, 1, { number: 7, head_sha: head, base_sha: base });
    await mutateJournal(out, 1, (journal) => { journal.pull_request!.prospective_tree_sha = tree; journal.effects.merge.state = "ambiguous"; });
    const run = async (_cmd: string, args: string[]) => args[0] === "pr" ? { code: 0, stdout: view("MERGED"), stderr: "" } : { code: 0, stdout: tree, stderr: "" };
    expect(await mergeIssue(1, { reallyMerge: true, outDir: out, run })).toBe("confirmed");
  });
});
