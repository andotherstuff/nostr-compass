import { readFile } from "node:fs/promises";
import { loadJournal, confirmDeployment, sha256 } from "../lib/journal.ts";

const REPO = "andotherstuff/nostr-compass";
type Runner = (cmd: string, args: string[]) => Promise<{ code: number; stdout: string; stderr: string }>;
type Fetcher = (url: string, init: RequestInit) => Promise<Response>;
type RunEvidence = { databaseId: number; url: string; headSha: string; status: string; conclusion: string; event: string };

async function defaultRun(cmd: string, args: string[]) {
  const proc = Bun.spawn([cmd, ...args], { stdout: "pipe", stderr: "pipe", env: { ...process.env, GH_CACHE_TTL: "0", HERMES_GH_NO_CACHE: "1" } });
  const [stdout, stderr, code] = await Promise.all([new Response(proc.stdout).text(), new Response(proc.stderr).text(), proc.exited]);
  return { code, stdout, stderr };
}

export async function verifyAndRecordDeployment(issue: number, options: { pageUrl?: string; outDir: string; workflow?: string; run?: Runner; fetcher?: Fetcher }): Promise<void> {
  const run = options.run ?? defaultRun; const fetcher = options.fetcher ?? fetch;
  const journal = await loadJournal(options.outDir, issue); const pr = journal.pull_request;
  const pageUrl = options.pageUrl ?? journal.deployment_intent?.page_url;
  if (!pageUrl || journal.deployment_intent?.page_url !== pageUrl || !/^https:\/\/nostrcompass\.org\//.test(pageUrl)) throw new Error("Deployment page URL is not the journal-pinned canonical route");
  if (journal.effects.merge?.state !== "confirmed" || !pr?.merge_sha || !pr.merge_tree_sha) throw new Error("Cannot verify deployment before exact merge confirmation");
  if (!journal.source) throw new Error("Cannot verify deployment without the journal-pinned source artifact");
  const source = await readFile(journal.source.path);
  if (sha256(source) !== journal.source.sha256) throw new Error("Journal-pinned source artifact hash changed");
  const marker = `Nostr Compass #${issue}`;
  if (!source.toString().includes(marker)) throw new Error("Journal-pinned source does not identify this edition");

  const runsResult = await run("gh", ["run", "list", "--repo", REPO, "--workflow", options.workflow ?? "Deploy Hugo site to Pages", "--commit", pr.merge_sha, "--event", "push", "--json", "databaseId,url,headSha,status,conclusion,event", "--limit", "20"]);
  if (runsResult.code !== 0) throw new Error(`Authenticated deployment lookup failed: ${runsResult.stderr.trim()}`);
  const runs = JSON.parse(runsResult.stdout) as RunEvidence[];
  const matches = runs.filter((candidate) => candidate.headSha === pr.merge_sha && candidate.event === "push" && candidate.status === "completed" && candidate.conclusion === "success").sort((a, b) => b.databaseId - a.databaseId);
  if (matches.length === 0) throw new Error("No successful push deployment exists for the exact merge commit");

  const treeResult = await run("gh", ["api", `repos/${REPO}/git/commits/${pr.merge_sha}`, "--jq", ".tree.sha"]);
  if (treeResult.code !== 0 || treeResult.stdout.trim() !== pr.merge_tree_sha) throw new Error("Live merge commit tree does not match the journal-pinned resulting tree");
  const separator = pageUrl.includes("?") ? "&" : "?";
  const response = await fetcher(`${pageUrl}${separator}compass_verify=${matches[0].databaseId}`, { cache: "no-store", redirect: "error", headers: { "Cache-Control": "no-cache", Pragma: "no-cache" } });
  if (!response.ok) throw new Error(`Served page readback failed with HTTP ${response.status}`);
  const bytes = new Uint8Array(await response.arrayBuffer());
  if (!new TextDecoder().decode(bytes).includes(marker)) throw new Error("Served page does not contain the exact edition marker");
  await confirmDeployment(options.outDir, issue, { workflow_run_id: matches[0].databaseId, workflow_url: matches[0].url, head_sha: pr.merge_sha, tree_sha: pr.merge_tree_sha, page_url: pageUrl, content_sha256: sha256(bytes), verified_at: new Date().toISOString() });
}
