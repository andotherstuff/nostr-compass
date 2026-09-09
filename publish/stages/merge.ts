// Stage 6: exact-identity merge with response-loss reconciliation.
import { spawn } from "node:child_process";
import { loadJournal, mutateJournal } from "../lib/journal.ts";

const OUT_DIR = new URL("../out", import.meta.url).pathname;
const REPO = "andotherstuff/nostr-compass";
export type PullRequestIdentity = { number: number; head_sha: string; base_sha: string };
type PRView = { number: number; state: string; mergeable: string; mergeStateStatus: string; headRefOid: string; baseRefOid: string; mergeCommit?: { oid: string } | null };
type Runner = (cmd: string, args: string[]) => Promise<{ code: number; stdout: string; stderr: string }>;

const defaultRun: Runner = (cmd, args) => new Promise((resolve) => {
  const child = spawn(cmd, args, { stdio: ["ignore", "pipe", "pipe"] }); let stdout = "", stderr = "";
  child.stdout.on("data", (d) => stdout += d); child.stderr.on("data", (d) => stderr += d);
  child.on("close", (code) => resolve({ code: code ?? 1, stdout, stderr }));
});

export async function pinPullRequest(outDir: string, issue: number, identity: PullRequestIdentity): Promise<void> {
  if (!Number.isInteger(identity.number) || identity.number < 1 || !/^[0-9a-f]{40}$/.test(identity.head_sha) || !/^[0-9a-f]{40}$/.test(identity.base_sha)) throw new Error("Invalid pinned PR identity");
  await mutateJournal(outDir, issue, (j) => {
    if (j.pull_request && (j.pull_request.number !== identity.number || j.pull_request.head_sha !== identity.head_sha || j.pull_request.base_sha !== identity.base_sha)) throw new Error("Conflicting pinned PR identity");
    j.pull_request = identity;
  });
}

async function viewPR(number: number, run: Runner): Promise<PRView> {
  const r = await run("gh", ["pr", "view", String(number), "--repo", REPO, "--json", "number,state,mergeable,mergeStateStatus,headRefOid,baseRefOid,mergeCommit"]);
  if (r.code !== 0) throw new Error(`gh pr view failed: ${r.stderr.trim()}`);
  return JSON.parse(r.stdout) as PRView;
}

export async function mergeIssue(issue: number, opts: { reallyMerge: boolean; outDir?: string; run?: Runner; identity?: PullRequestIdentity }): Promise<void> {
  const outDir = opts.outDir ?? OUT_DIR; const run = opts.run ?? defaultRun;
  if (opts.identity) await pinPullRequest(outDir, issue, opts.identity);
  let journal = await loadJournal(outDir, issue);
  const pinned = journal.pull_request; if (!pinned) throw new Error("No pinned PR number/head/base identity in state.json");
  if (journal.effects.article?.state !== "confirmed" || journal.effects.announcement?.state !== "confirmed") throw new Error("Refusing to merge before both broadcast effects meet their relay floor");
  let pr = await viewPR(pinned.number, run);
  if (pr.number !== pinned.number || pr.headRefOid !== pinned.head_sha) throw new Error("PR head no longer matches pinned identity");
  if (pr.state === "MERGED") {
    const mergeSha = pr.mergeCommit?.oid; if (!mergeSha) throw new Error("Merged PR has no mergeCommit identity");
    await mutateJournal(outDir, issue, (j) => { j.pull_request!.merge_sha = mergeSha; }); return;
  }
  if (pr.baseRefOid !== pinned.base_sha) throw new Error("PR base no longer matches reviewed base SHA");
  if (pr.mergeable !== "MERGEABLE" || pr.mergeStateStatus !== "CLEAN") throw new Error(`PR #${pr.number} is not clean and mergeable`);
  if (!opts.reallyMerge) return;
  await mutateJournal(outDir, issue, (j) => { j.effects.merge = { state: "attempted", intent_sha256: `${pinned.number}:${pinned.head_sha}:${pinned.base_sha}` }; });
  const merged = await run("gh", ["pr", "merge", String(pinned.number), "--repo", REPO, "--squash", "--delete-branch", "--match-head-commit", pinned.head_sha]);
  pr = await viewPR(pinned.number, run); // authoritative reconciliation, including response loss
  if (pr.state !== "MERGED" || pr.headRefOid !== pinned.head_sha || !pr.mergeCommit?.oid) {
    await mutateJournal(outDir, issue, (j) => { j.effects.merge.state = merged.code === 0 ? "ambiguous" : "failed"; j.effects.merge.error = merged.stderr.trim() || merged.stdout.trim(); });
    throw new Error(`Merge not confirmed for exact PR/head: ${merged.stderr.trim() || merged.stdout.trim()}`);
  }
  await mutateJournal(outDir, issue, (j) => { j.pull_request!.merge_sha = pr.mergeCommit!.oid; j.effects.merge.state = "confirmed"; });
}
