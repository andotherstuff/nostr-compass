// Stage 6: MERGE.
// Squash-merges the newsletter PR on GitHub after a successful broadcast.
// The previous workflow broadcast to Nostr but left the PR open, so the
// Hugo deploy never ran and the newsletter never appeared on the website.
//
// Safety: refuses to merge unless the broadcast ledger shows >=1 ok relay
// for the article event. The PR branch is discovered by reading the current
// git branch (publish always runs on the newsletter branch).

import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { spawn } from "node:child_process";

const OUT_DIR = join(import.meta.dir, "..", "out");
const PUBLISHED_LEDGER = join(import.meta.dir, "..", "published.json");
const COMPASS_DIR = process.env.COMPASS_DIR || join(import.meta.dir, "..", "..");
const REPO = "andotherstuff/nostr-compass";

type LedgerEntry = {
  issue: number;
  event_id: string;
  relays_ok: string[];
  relays_fail: string[];
};

type PRView = {
  number: number;
  state: string;
  mergeable: string;
  mergeStateStatus: string;
  headRefName: string;
};

function run(cmd: string, args: string[]): Promise<{ code: number; stdout: string; stderr: string }> {
  return new Promise((resolve) => {
    const child = spawn(cmd, args, { stdio: ["ignore", "pipe", "pipe"] });
    let stdout = "";
    let stderr = "";
    child.stdout.on("data", (d) => (stdout += d.toString()));
    child.stderr.on("data", (d) => (stderr += d.toString()));
    child.on("close", (code) => resolve({ code: code ?? 1, stdout, stderr }));
  });
}

async function currentBranch(): Promise<string> {
  const { code, stdout, stderr } = await run("git", ["-C", COMPASS_DIR, "branch", "--show-current"]);
  if (code !== 0) throw new Error(`git branch failed: ${stderr.trim()}`);
  return stdout.trim();
}

async function ledgerEntry(issue: number): Promise<LedgerEntry> {
  const ledger = JSON.parse(await readFile(PUBLISHED_LEDGER, "utf8")) as LedgerEntry[];
  const entry = ledger.find((e) => e.issue === issue);
  if (!entry) {
    throw new Error(
      `No ledger entry for issue ${issue} in published.json. ` +
        `Broadcast must complete successfully before merge.`,
    );
  }
  return entry;
}

async function findPR(branch: string): Promise<PRView> {
  const { code, stdout, stderr } = await run("gh", [
    "pr",
    "list",
    "--repo",
    REPO,
    "--head",
    branch,
    "--state",
    "open",
    "--json",
    "number,state,mergeable,mergeStateStatus,headRefName",
  ]);
  if (code !== 0) throw new Error(`gh pr list failed: ${stderr.trim()}`);
  const prs = JSON.parse(stdout) as PRView[];
  if (prs.length === 0) {
    throw new Error(`No open PR found for branch "${branch}" in ${REPO}.`);
  }
  if (prs.length > 1) {
    throw new Error(
      `Multiple open PRs found for branch "${branch}": ${prs.map((p) => `#${p.number}`).join(", ")}. ` +
        `Resolve manually.`,
    );
  }
  return prs[0];
}

async function mergePR(number: number): Promise<string> {
  const { code, stdout, stderr } = await run("gh", [
    "pr",
    "merge",
    String(number),
    "--repo",
    REPO,
    "--squash",
    "--delete-branch",
  ]);
  if (code !== 0) throw new Error(`gh pr merge failed: ${stderr.trim() || stdout.trim()}`);
  return stdout.trim();
}

export async function mergeIssue(
  issue: number,
  opts: { reallyMerge: boolean },
): Promise<void> {
  // Reuse the broadcast ledger as proof the broadcast actually happened.
  const entry = await ledgerEntry(issue);
  if (entry.relays_ok.length === 0) {
    throw new Error(
      `Refusing to merge: broadcast for issue ${issue} reached 0 relays. ` +
        `Re-run --stage broadcast first.`,
    );
  }

  const branch = await currentBranch();
  if (!branch.startsWith("newsletter/")) {
    throw new Error(
      `Refusing to merge: current branch "${branch}" is not a newsletter branch. ` +
        `Checkout the newsletter/* branch before merging.`,
    );
  }

  const pr = await findPR(branch);
  console.log(`              PR #${pr.number}  branch=${pr.headRefName}`);
  console.log(`              mergeable=${pr.mergeable}  mergeState=${pr.mergeStateStatus}`);

  if (pr.mergeable !== "MERGEABLE" || pr.mergeStateStatus !== "CLEAN") {
    throw new Error(
      `PR #${pr.number} is not in a clean mergeable state ` +
        `(mergeable=${pr.mergeable}, mergeState=${pr.mergeStateStatus}). Resolve on GitHub.`,
    );
  }

  if (!opts.reallyMerge) {
    console.log(`              [dry-merge] would squash-merge PR #${pr.number} and delete branch`);
    return;
  }

  const out = await mergePR(pr.number);
  console.log(`              ✓ merged PR #${pr.number}`);
  if (out) console.log(`              ${out.split("\n").join("\n              ")}`);
  console.log(`              Hugo deploy will run from main`);

  // Touch OUT_DIR/issue/merged.flag so re-runs are idempotent and auditable.
  const flagPath = join(OUT_DIR, String(issue), "merged.flag");
  await Bun.write(flagPath, `pr=${pr.number}\nmerged_at=${new Date().toISOString()}\n`);
}
