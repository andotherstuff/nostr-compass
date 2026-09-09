// Stage 6: exact-identity merge with server-enforced base currentness.
import { spawn } from "node:child_process";
import { loadJournal, mutateJournal } from "../lib/journal.ts";
import { assertMergeAuthorized } from "../lib/authorization.ts";

const OUT_DIR = new URL("../out", import.meta.url).pathname;
const REPO = "andotherstuff/nostr-compass";
export type PullRequestIdentity = { number: number; head_sha: string; base_sha: string };
type PRView = { number: number; state: string; mergeable: string; mergeStateStatus: string; headRefOid: string; baseRefOid: string; baseRefName: string; mergeCommit?: { oid: string } | null; potentialMergeCommit?: { oid: string } | null };
type Runner = (cmd: string, args: string[]) => Promise<{ code: number; stdout: string; stderr: string }>;
const defaultRun: Runner = (cmd, args) => new Promise((resolve) => {
  const child = spawn(cmd, args, { stdio: ["ignore", "pipe", "pipe"], env: { ...process.env, GH_CACHE_TTL: "0", HERMES_GH_NO_CACHE: "1" } }); let stdout = "", stderr = "";
  child.stdout.on("data", (data) => stdout += data); child.stderr.on("data", (data) => stderr += data);
  child.on("close", (code) => resolve({ code: code ?? 1, stdout, stderr }));
});

export async function pinPullRequest(outDir: string, issue: number, identity: PullRequestIdentity): Promise<void> {
  if (!Number.isInteger(identity.number) || identity.number < 1 || !/^[0-9a-f]{40}$/.test(identity.head_sha) || !/^[0-9a-f]{40}$/.test(identity.base_sha)) throw new Error("Invalid pinned PR identity");
  await mutateJournal(outDir, issue, (journal) => {
    if (journal.pull_request && (journal.pull_request.number !== identity.number || journal.pull_request.head_sha !== identity.head_sha || journal.pull_request.base_sha !== identity.base_sha)) throw new Error("Conflicting pinned PR identity");
    journal.pull_request = { ...journal.pull_request, ...identity };
  });
}
async function viewPR(number: number, run: Runner): Promise<PRView> {
  const result = await run("gh", ["pr", "view", String(number), "--repo", REPO, "--json", "number,state,mergeable,mergeStateStatus,headRefOid,baseRefOid,baseRefName,mergeCommit,potentialMergeCommit"]);
  if (result.code !== 0) throw new Error(`gh pr view failed: ${result.stderr.trim()}`);
  return JSON.parse(result.stdout) as PRView;
}
async function commitTree(commit: string, run: Runner): Promise<string> {
  const result = await run("gh", ["api", `repos/${REPO}/git/commits/${commit}`, "--jq", ".tree.sha"]);
  const tree = result.stdout.trim();
  if (result.code !== 0 || !/^[0-9a-f]{40}$/.test(tree)) throw new Error(`Cannot verify commit tree for ${commit}: ${result.stderr.trim()}`);
  return tree;
}
async function requireServerBaseGuard(baseRef: string, run: Runner): Promise<void> {
  const result = await run("gh", ["api", `repos/${REPO}/branches/${baseRef}/protection`, "--jq", ".required_status_checks.strict"]);
  if (result.code !== 0 || result.stdout.trim() !== "true") throw new Error("Refusing merge: server does not enforce strict current-base status checks, so base identity can race the merge");
}

export async function previewMergeIssue(
  issue: number,
  opts: { outDir?: string; run?: Runner; identity?: PullRequestIdentity } = {},
): Promise<{ state: "open" | "merged"; number: number; head_sha: string; base_sha: string; prospective_tree_sha: string; merge_sha?: string }> {
  const outDir = opts.outDir ?? OUT_DIR; const run = opts.run ?? defaultRun;
  const journal = await loadJournal(outDir, issue); const pinned = journal.pull_request;
  if (!pinned) throw new Error("No pinned PR number/head/base identity in state.json");
  if (opts.identity && (opts.identity.number !== pinned.number || opts.identity.head_sha !== pinned.head_sha || opts.identity.base_sha !== pinned.base_sha)) throw new Error("Preview PR identity does not match the journal-pinned identity");
  const pr = await viewPR(pinned.number, run);
  if (pr.number !== pinned.number || pr.headRefOid !== pinned.head_sha) throw new Error("PR head no longer matches pinned identity");
  if (pr.state === "MERGED") {
    if (!pinned.prospective_tree_sha || !pr.mergeCommit?.oid) throw new Error("Merged PR lacks prospective-tree or merge-commit evidence");
    const mergeTree = await commitTree(pr.mergeCommit.oid, run);
    if (mergeTree !== pinned.prospective_tree_sha) throw new Error("Merged tree does not match the pinned prospective tree");
    return { state: "merged", number: pinned.number, head_sha: pinned.head_sha, base_sha: pinned.base_sha, prospective_tree_sha: mergeTree, merge_sha: pr.mergeCommit.oid };
  }
  if (pr.baseRefOid !== pinned.base_sha) throw new Error("PR base no longer matches reviewed base SHA");
  if (pr.mergeable !== "MERGEABLE" || pr.mergeStateStatus !== "CLEAN") throw new Error(`PR #${pr.number} is not clean and mergeable`);
  if (!pr.potentialMergeCommit?.oid) throw new Error("GitHub did not provide a prospective merge identity");
  const prospectiveTree = await commitTree(pr.potentialMergeCommit.oid, run);
  await requireServerBaseGuard(pr.baseRefName, run);
  if (pinned.prospective_tree_sha && pinned.prospective_tree_sha !== prospectiveTree) throw new Error("Current prospective merge tree differs from the journal-pinned review candidate");
  return { state: "open", number: pinned.number, head_sha: pinned.head_sha, base_sha: pinned.base_sha, prospective_tree_sha: prospectiveTree };
}

export async function mergeIssue(issue: number, opts: { reallyMerge: boolean; outDir?: string; run?: Runner; identity?: PullRequestIdentity }): Promise<"prepared" | "confirmed"> {
  const outDir = opts.outDir ?? OUT_DIR; const run = opts.run ?? defaultRun;
  if (opts.identity) await pinPullRequest(outDir, issue, opts.identity);
  let journal = await loadJournal(outDir, issue); const pinned = journal.pull_request;
  if (!pinned) throw new Error("No pinned PR number/head/base identity in state.json");
  if (opts.reallyMerge && !journal.deployment_intent) throw new Error("Refusing merge without a journal-pinned canonical deployment route");
  let pr = await viewPR(pinned.number, run);
  if (pr.number !== pinned.number || pr.headRefOid !== pinned.head_sha) throw new Error("PR head no longer matches pinned identity");
  if (pr.state === "MERGED") {
    if (!pinned.prospective_tree_sha) throw new Error("Merged PR lacks pre-mutation prospective tree evidence");
    if (!["attempted", "ambiguous"].includes(journal.effects.merge?.state ?? "")) throw new Error("Merged PR lacks a previously authorized mutation attempt");
    await assertMergeAuthorized(outDir, issue, pinned.prospective_tree_sha);
    const mergeSha = pr.mergeCommit?.oid; if (!mergeSha) throw new Error("Merged PR has no mergeCommit identity");
    const mergeTree = await commitTree(mergeSha, run);
    if (mergeTree !== pinned.prospective_tree_sha) throw new Error("Merged tree does not match the pinned prospective tree");
    await mutateJournal(outDir, issue, (j) => { j.pull_request!.merge_sha = mergeSha; j.pull_request!.merge_tree_sha = mergeTree; j.effects.merge = { state: "confirmed", intent_sha256: `${pinned.number}:${pinned.head_sha}:${pinned.base_sha}:${mergeTree}`, event_id: mergeSha }; });
    return "confirmed";
  }
  if (pr.baseRefOid !== pinned.base_sha) throw new Error("PR base no longer matches reviewed base SHA");
  if (pr.mergeable !== "MERGEABLE" || pr.mergeStateStatus !== "CLEAN") throw new Error(`PR #${pr.number} is not clean and mergeable`);
  if (!pr.potentialMergeCommit?.oid) throw new Error("GitHub did not provide a prospective merge identity");
  const prospectiveTree = await commitTree(pr.potentialMergeCommit.oid, run);
  await requireServerBaseGuard(pr.baseRefName, run);
  if (!opts.reallyMerge) {
    await mutateJournal(outDir, issue, (j) => {
      j.pull_request!.prospective_tree_sha = prospectiveTree;
      j.pull_request!.base_guard = { method: "branch-protection-strict", base_ref: pr.baseRefName, verified_at: new Date().toISOString() };
      j.effects.merge = { state: "prepared", intent_sha256: `${pinned.number}:${pinned.head_sha}:${pinned.base_sha}:${prospectiveTree}` };
    });
    return "prepared";
  }
  if (pinned.prospective_tree_sha !== prospectiveTree || journal.effects.merge?.state !== "prepared") throw new Error("merge mutation requires a previously prepared identical prospective tree");
  await assertMergeAuthorized(outDir, issue, prospectiveTree);
  await mutateJournal(outDir, issue, (j) => {
    j.pull_request!.base_guard = { method: "branch-protection-strict", base_ref: pr.baseRefName, verified_at: new Date().toISOString() };
  });
  await mutateJournal(outDir, issue, (j) => { j.effects.merge.state = "attempted"; });
  const merged = await run("gh", ["pr", "merge", String(pinned.number), "--repo", REPO, "--squash", "--delete-branch", "--match-head-commit", pinned.head_sha]);
  try { pr = await viewPR(pinned.number, run); }
  catch (error) {
    await mutateJournal(outDir, issue, (j) => { j.effects.merge.state = "ambiguous"; j.effects.merge.error = `authoritative readback failed: ${(error as Error).message}`; });
    throw error;
  }
  if (pr.state !== "MERGED" || pr.headRefOid !== pinned.head_sha || !pr.mergeCommit?.oid) {
    await mutateJournal(outDir, issue, (j) => { j.effects.merge.state = merged.code === 0 ? "ambiguous" : "failed"; j.effects.merge.error = merged.stderr.trim() || merged.stdout.trim(); });
    throw new Error(`Merge not confirmed for exact PR/head: ${merged.stderr.trim() || merged.stdout.trim()}`);
  }
  const mergeTree = await commitTree(pr.mergeCommit.oid, run);
  if (mergeTree !== prospectiveTree) {
    await mutateJournal(outDir, issue, (j) => { j.effects.merge.state = "failed"; j.effects.merge.error = "resulting merge tree differs from prospective tree"; });
    throw new Error("Resulting merge tree differs from the pre-mutation prospective tree");
  }
  await mutateJournal(outDir, issue, (j) => { j.pull_request!.merge_sha = pr.mergeCommit!.oid; j.pull_request!.merge_tree_sha = mergeTree; j.effects.merge.state = "confirmed"; j.effects.merge.event_id = pr.mergeCommit!.oid; j.effects.merge.error = undefined; });
  return "confirmed";
}
