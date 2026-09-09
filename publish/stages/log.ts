// Stage 7: LOG.
//
// WHY THIS EXISTS
// ---------------
// The publication log was a hand-written artifact, and both failure modes
// showed up within two issues. #36 shipped with no log at all. #37's first log
// cited `data/compass_relays.txt` as the broadcast configuration and reported
// readback from an ad-hoc relay probe, when the pipeline actually reads
// `publish/config/relays.json` and `publish/out/<n>/receipts.json` is the
// authoritative ledger. Both were wrong in the direction of looking finished.
//
// This stage derives the log from the artifacts the run already produced:
// receipts.json for per-relay acceptance, published.json for event ids, the
// GitHub deploy run for the website, and a fresh exact-id readback for
// durability. Nothing here is typed from memory.
//
// The log is written into the workspace under the compass repo, committed on a
// branch, and pushed as a PR. It is deliberately not committed straight to
// main: the log is prose about a publication and stays reviewable.

import { readFile, mkdir, readdir } from "node:fs/promises";
import { join } from "node:path";
import { spawn } from "node:child_process";
import WebSocket from "ws";
import { writeAtomic } from "../lib/safety.ts";
import { loadJournal, mutateJournal, sha256, stableJson } from "../lib/journal.ts";
import { notifyMilestone, prLink, runLink } from "../lib/notify.ts";

const RUNTIME_ROOT = join(import.meta.dir, "..", "..");
const PUBLISH_ROOT = join(RUNTIME_ROOT, "publish");
const OUT_DIR = join(PUBLISH_ROOT, "out");
const RELAYS_PATH = join(PUBLISH_ROOT, "config/relays.json");
const AUTHOR_PATH = join(PUBLISH_ROOT, "config/author.json");

const REPO = "andotherstuff/nostr-compass";

const READBACK_TIMEOUT_MS = 20_000;

type RelaysConfig = { relays: string[] };
type Receipt = { relay: string; ok: boolean; reason?: string; ms: number };
type Receipts = { article: Receipt[]; announcement: Receipt[] };
type StoredReceipts = {
  schema_version: 1;
  relay_floor: number;
  acceptance: Receipts;
  readback: {
    article: Record<string, { found: boolean; recorded_at: string }>;
    announcement: Record<string, { found: boolean; recorded_at: string }>;
  };
};

export function assertCurrentReceiptSchema(value: unknown): asserts value is StoredReceipts {
  const stored = value as Partial<StoredReceipts>;
  if (stored.schema_version !== 1 || !Number.isInteger(stored.relay_floor) || (stored.relay_floor ?? 0) < 5 ||
      !stored.acceptance || !Array.isArray(stored.acceptance.article) || !Array.isArray(stored.acceptance.announcement) ||
      !stored.readback || typeof stored.readback.article !== "object" || stored.readback.article === null ||
      typeof stored.readback.announcement !== "object" || stored.readback.announcement === null) {
    throw new Error("Unsupported or malformed publication receipt schema");
  }
}
type LedgerEntry = {
  issue: number;
  event_id: string;
  announcement_id: string;
  first_published_at: number;
  last_edited_at?: number;
  banner_url: string;
  relays_ok: string[];
  relays_fail: string[];
};
type Metadata = { issue: number; title: string; source_path: string };

export type ReadbackRow = { relay: string; article: boolean; announcement: boolean };

function run(cmd: string, args: string[]): Promise<{ code: number; stdout: string; stderr: string }> {
  return new Promise((resolve) => {
    const child = spawn(cmd, args, {
      stdio: ["ignore", "pipe", "pipe"],
      env: { ...process.env, GH_CACHE_TTL: "0", HERMES_GH_NO_CACHE: "1" },
    });
    let stdout = "";
    let stderr = "";
    child.stdout.on("data", (d) => (stdout += d.toString()));
    child.stderr.on("data", (d) => (stderr += d.toString()));
    child.on("error", (e) => resolve({ code: 1, stdout: "", stderr: e.message }));
    child.on("close", (code) => resolve({ code: code ?? 1, stdout, stderr }));
  });
}

/**
 * A write-only NIP-66 blaster accepts an event but does not serve it back.
 * Counting it as readback evidence would overstate durability, so it is
 * excluded from the readback set while still counting toward fan-out.
 */
export function isBlaster(relay: string): boolean {
  return relay.includes("sendit.nosflare.com");
}

/**
 * metadata.json records the parse input (`/tmp/<n>publish.md`), not the issue
 * date, so the date is resolved from the repo: the newsletter whose frontmatter
 * title is exactly this issue. Guessing from the run date would silently
 * mislabel a recovery run that publishes yesterday's issue.
 */
export function matchesIssueTitle(frontmatter: string, issue: number): boolean {
  return new RegExp(`^title:\\s*"?Nostr Compass #${issue}"?\\s*$`, "m").test(frontmatter);
}

/**
 * Newsletter dates as seen on a git ref, for when the working tree is stale.
 *
 * The log stage runs right after the merge stage put the issue on origin/main,
 * so origin/main always has it even when the local checkout does not.
 */
async function issueDatesOnRef(compassDir: string, issue: number, ref: string): Promise<string[]> {
  const git = (...args: string[]) => run("git", ["-C", compassDir, ...args]);
  if ((await git("rev-parse", "--verify", "--quiet", `${ref}^{commit}`)).code !== 0) return [];
  const listed = await git("ls-tree", "--name-only", "-r", ref, "--", "content/en/newsletters");
  if (listed.code !== 0) return [];
  const hits: string[] = [];
  for (const path of listed.stdout.split("\n").map((l) => l.trim()).filter(Boolean).sort()) {
    const name = path.split("/").pop() ?? "";
    if (!/^\d{4}-\d{2}-\d{2}-newsletter\.md$/.test(name)) continue;
    const shown = await git("show", `${ref}:${path}`);
    if (shown.code === 0 && matchesIssueTitle(shown.stdout.slice(0, 400), issue)) {
      hits.push(name.replace("-newsletter.md", ""));
    }
  }
  return hits;
}

export async function resolveIssueDate(compassDir: string, issue: number): Promise<string> {
  const dir = join(compassDir, "content/en/newsletters");
  const files = (await readdir(dir)).filter((f) => /^\d{4}-\d{2}-\d{2}-newsletter\.md$/.test(f));
  let hits: string[] = [];
  for (const f of files.sort()) {
    const head = (await readFile(join(dir, f), "utf8")).slice(0, 400);
    if (matchesIssueTitle(head, issue)) hits.push(f.replace("-newsletter.md", ""));
  }

  // The default compassDir is the shared checkout, which nothing in the weekly
  // automation keeps current — it was 27 commits behind on 2026-08-27, missing
  // both #36 and #37. Falling back to origin/main means a stale checkout cannot
  // fail the log stage of an issue that is already merged and live.
  let source = dir;
  if (hits.length === 0) {
    await run("git", ["-C", compassDir, "fetch", "origin", "--quiet"]);
    hits = await issueDatesOnRef(compassDir, issue, "origin/main");
    source = `${dir} or origin/main`;
    if (hits.length > 0) {
      console.log(`              resolved issue date from origin/main (${compassDir} is behind)`);
    }
  }

  if (hits.length === 0) throw new Error(`No newsletter in ${source} has title "Nostr Compass #${issue}".`);
  if (hits.length > 1) {
    throw new Error(`Ambiguous issue date for #${issue}: ${hits.join(", ")}. Resolve the duplicate title.`);
  }
  return hits[0];
}

/**
 * Ask one relay for both events by exact id. Returns which of the two it
 * served. A relay that accepted the broadcast but cannot serve the event back
 * is a real durability gap and must show up in the log as such.
 */
function readbackFromRelay(
  relay: string,
  articleId: string,
  announcementId: string,
): Promise<ReadbackRow> {
  return new Promise((resolve) => {
    const found = { article: false, announcement: false };
    let settled = false;
    const finish = () => {
      if (settled) return;
      settled = true;
      try {
        ws.terminate();
      } catch {
        /* ignore */
      }
      resolve({ relay, ...found });
    };

    let ws: WebSocket;
    try {
      ws = new WebSocket(relay, { handshakeTimeout: READBACK_TIMEOUT_MS });
    } catch {
      resolve({ relay, article: false, announcement: false });
      return;
    }
    const timer = setTimeout(finish, READBACK_TIMEOUT_MS);
    let closed = 0;

    ws.on("open", () => {
      ws.send(JSON.stringify(["REQ", "art", { ids: [articleId] }]));
      ws.send(JSON.stringify(["REQ", "ann", { ids: [announcementId] }]));
    });
    ws.on("message", (raw) => {
      let msg: unknown;
      try {
        msg = JSON.parse(raw.toString());
      } catch {
        return;
      }
      if (!Array.isArray(msg)) return;
      if (msg[0] === "EVENT") {
        const id = (msg[2] as { id?: string } | undefined)?.id;
        if (id === articleId) found.article = true;
        if (id === announcementId) found.announcement = true;
      } else if (msg[0] === "EOSE" || msg[0] === "CLOSED") {
        if (++closed >= 2) {
          clearTimeout(timer);
          finish();
        }
      }
    });
    ws.on("error", () => {
      clearTimeout(timer);
      finish();
    });
    ws.on("close", () => {
      clearTimeout(timer);
      finish();
    });
  });
}

export async function readbackAll(
  relays: string[],
  articleId: string,
  announcementId: string,
): Promise<ReadbackRow[]> {
  return Promise.all(relays.map((r) => readbackFromRelay(r, articleId, announcementId)));
}

export type DeployRunRow = { databaseId: number; conclusion: string; name: string; event: string };

/**
 * A merge commit can carry several runs: the push-triggered deploy plus any
 * manual workflow_dispatch reruns. The push run is the one the merge caused, so
 * prefer it; a rerun that happens to sort first must not be credited instead.
 */
export function selectDeployRun(rows: DeployRunRow[]): DeployRunRow | null {
  const pages = rows.filter((r) => /pages/i.test(r.name));
  const candidates = pages.length > 0 ? pages : rows;
  return candidates.find((r) => r.event === "push") ?? candidates[0] ?? null;
}

/**
 * The deploy that published THIS issue, matched by the merge commit. Taking the
 * most recent run on main instead would attribute a later unrelated deploy to
 * this publication, which is exactly the kind of plausible-looking wrong fact
 * the log exists to prevent.
 */
async function deployRunForCommit(sha: string | null): Promise<{ id: string; conclusion: string } | null> {
  if (!sha) return null;
  const { code, stdout } = await run("gh", [
    "run",
    "list",
    "--repo",
    REPO,
    "--commit",
    sha,
    "--limit",
    "20",
    "--json",
    "databaseId,conclusion,name,event",
  ]);
  if (code !== 0) return null;
  try {
    const deploy = selectDeployRun(JSON.parse(stdout) as DeployRunRow[]);
    if (!deploy) return null;
    return { id: String(deploy.databaseId), conclusion: deploy.conclusion || "in progress" };
  } catch {
    return null;
  }
}

async function mergedPr(
  date: string,
): Promise<{ number: number; mergeCommit: string | null; mergedAt: string | null } | null> {
  const { code, stdout } = await run("gh", [
    "pr",
    "list",
    "--repo",
    REPO,
    "--head",
    `newsletter/${date}`,
    "--state",
    "merged",
    "--json",
    "number,mergeCommit,mergedAt",
  ]);
  if (code !== 0) return null;
  try {
    const rows = JSON.parse(stdout) as {
      number: number;
      mergeCommit: { oid?: string } | null;
      mergedAt: string | null;
    }[];
    if (rows.length === 0) return null;
    return {
      number: rows[0].number,
      mergeCommit: rows[0].mergeCommit?.oid ?? null,
      mergedAt: rows[0].mergedAt ?? null,
    };
  } catch {
    return null;
  }
}

/**
 * Cite the pre-publication gates by reading them, not by asserting them. A
 * refresh file that does not end in an evidence-bearing GATE: PASS is reported
 * as such rather than quietly omitted.
 */
/**
 * Roots that may hold this issue's gate artifacts, in order of preference.
 *
 * `data/newsletter_workspace` is gitignored, so the gate files exist only in
 * the worktree the weekly run used, never in the shared checkout. Reading just
 * compassDir made the log report every gate "missing" for an issue whose gates
 * all passed — a false negative in the direction of looking unverified.
 */
export function gateRoots(compassDir: string, date: string): string[] {
  const roots = [compassDir];
  const explicit = process.env.COMPASS_WORKSPACE_DIR;
  if (explicit) roots.push(explicit);
  roots.push(join(compassDir, "..", "compass-worktrees", date));
  return roots.filter((root, i) => roots.indexOf(root) === i);
}

export async function gateStatus(compassDir: string, date: string): Promise<string[]> {
  const files = [
    [`prepublish_refresh_${date}.md`, "Pre-publication refresh"],
    [`final_delta_refresh_${date}.md`, "Final delta refresh"],
    [`handoff_${date}.md`, "Stage 8 review handoff"],
  ];
  const roots = gateRoots(compassDir, date);
  const out: string[] = [];
  for (const [name, label] of files) {
    let line = `- ${label} (\`${name}\`): missing`;
    for (const root of roots) {
      let body: string;
      try {
        body = await readFile(join(root, "data/newsletter_workspace", name), "utf8");
      } catch {
        continue;
      }
      const pass = /GATE:\s*PASS/.test(body);
      const where = root === compassDir ? "" : ` in \`${root}\``;
      line = `- ${label} (\`${name}\`)${where}: ${pass ? "ends in GATE: PASS" : "present but does NOT end in GATE: PASS"}`;
      break;
    }
    out.push(line);
  }
  return out;
}

async function pageStatus(date: string, title: string): Promise<string> {
  const url = `https://nostrcompass.org/en/newsletters/${date}-newsletter/`;
  const { code, stdout } = await run("curl", ["-s", "-w", "\\n%{http_code}", url]);
  if (code !== 0) return "could not be fetched";
  const lines = stdout.split("\n");
  const status = lines[lines.length - 1].trim();
  const hasTitle = stdout.includes(title);
  return `HTTP ${status}${hasTitle ? ` and contained \`${title}\`` : " but did NOT contain the issue title"}`;
}

export function renderLog(args: {
  issue: number;
  date: string;
  title: string;
  pr: { number: number; mergeCommit: string | null; mergedAt: string | null } | null;
  prerequisites: string[];
  deploy: { id: string; conclusion: string } | null;
  page: string;
  ledger: LedgerEntry;
  configured: string[];
  receipts: Receipts;
  readback: ReadbackRow[];
  naddr: string;
  nevent: string;
  announcementCreatedAt: number | null;
  relayFloor?: number;
}): string {
  const {
    issue, date, title, pr, prerequisites, deploy, page, ledger,
    configured, receipts, readback, naddr, nevent, announcementCreatedAt,
  } = args;
  const artFail = receipts.article.filter((r) => !r.ok);
  const annFail = receipts.announcement.filter((r) => !r.ok);
  const artOk = receipts.article.length - artFail.length;
  const annOk = receipts.announcement.length - annFail.length;
  const durable = readback.filter((r) => !isBlaster(r.relay));
  const bothBack = durable.filter((r) => r.article && r.announcement);
  const partial = durable.filter((r) => (r.article ? 1 : 0) + (r.announcement ? 1 : 0) === 1);
  const neither = durable.filter((r) => !r.article && !r.announcement);
  const iso = (s: number) => new Date(s * 1000).toISOString().replace(".000Z", "Z");

  const out: string[] = [];
  out.push(`# Compass publication log — ${date}`, "");
  out.push(`Issue: ${title}`);
  out.push(
    `Draft PR: ${pr === null ? "not found" : `https://github.com/${REPO}/pull/${pr.number}`}`,
  );
  out.push(`Deployed page: https://nostrcompass.org/en/newsletters/${date}-newsletter/`, "");
  out.push("## Publication prerequisites", "");
  out.push(...prerequisites, "");
  out.push("## Merge and deployment", "");
  out.push(
    pr === null
      ? "- No merged PR was found for this issue's newsletter branch."
      : `- PR #${pr.number} squash-merged into \`main\`${pr.mergedAt ? ` at \`${pr.mergedAt}\`` : ""}` +
        `${pr.mergeCommit ? ` as commit \`${pr.mergeCommit.slice(0, 7)}\`` : ""}.`,
  );
  out.push(
    deploy === null
      ? "- GitHub Pages deploy status could not be read."
      : `- GitHub Pages workflow https://github.com/${REPO}/actions/runs/${deploy.id} concluded \`${deploy.conclusion}\`.`,
  );
  out.push(`- The canonical URL returned ${page}.`, "");
  out.push("## Nostr publication", "");
  // A NIP-23 replacement keeps the d tag and published_at but gets a new event
  // id, so without this line a reader cannot explain why the id differs from an
  // earlier copy of this log.
  const edited =
    typeof ledger.last_edited_at === "number" &&
    ledger.last_edited_at !== ledger.first_published_at;
  if (edited) {
    out.push(
      `- **Replaced after first publication.** The addressable event was re-signed and ` +
        `rebroadcast at ${iso(ledger.last_edited_at as number)} on the same \`d\` tag, so the ` +
        `event id below differs from the one recorded at first publication. \`published_at\` ` +
        `is preserved.`,
      "",
    );
  }
  out.push(`- Kind 30023 event ID: \`${ledger.event_id}\``);
  out.push(
    `  - \`d\` tag \`newsletter-${issue}\`, \`published_at\` \`${ledger.first_published_at}\` (${iso(ledger.first_published_at)})`,
  );
  out.push(`  - Banner image ${ledger.banner_url}`);
  out.push(`- Kind 1 event ID: \`${ledger.announcement_id}\``);
  if (announcementCreatedAt !== null) {
    out.push(`  - Created at \`${announcementCreatedAt}\` (${iso(announcementCreatedAt)})`);
  }
  out.push(`- Article: https://njump.me/${naddr}`);
  out.push(`- Announcement: https://njump.me/${nevent}`);
  out.push(
    `- Signed events and receipts: \`publish/out/${issue}/\`; ledger entry in \`publish/published.json\`.`,
    "",
  );
  out.push("### Broadcast fan-out", "");
  out.push(
    `\`publish/config/relays.json\` configures ${configured.length} targets. ` +
      `The article was accepted by ${artOk} and the announcement by ${annOk}.`,
    "",
  );
  if (artFail.length === 0 && annFail.length === 0) {
    out.push("Every configured target accepted both events.", "");
  } else {
    out.push("Rejections and failures:", "");
    for (const r of artFail) out.push(`- article, \`${r.relay}\`: ${r.reason ?? "no reason given"}`);
    for (const r of annFail) out.push(`- announcement, \`${r.relay}\`: ${r.reason ?? "no reason given"}`);
    out.push("");
  }
  // An naddr hint relay that rejected the broadcast will not resolve the hint
  // until a rebroadcast. Readers following the naddr are the ones affected, so
  // the log names it rather than leaving it implied by the rejection list.
  const hintRelays = configured.filter((r) => !isBlaster(r)).slice(0, 4);
  const failedHints = [...new Set(artFail.concat(annFail).map((r) => r.relay))].filter((r) =>
    hintRelays.includes(r),
  );
  if (failedHints.length > 0) {
    out.push(
      `${failedHints.map((r) => `\`${r}\``).join(", ")} ${failedHints.length === 1 ? "is" : "are"} ` +
        `also ${failedHints.length === 1 ? "an" : ""} \`naddr\` hint ${failedHints.length === 1 ? "relay" : "relays"}, ` +
        `so ${failedHints.length === 1 ? "that hint" : "those hints"} will not resolve there until the event is rebroadcast.`,
      "",
    );
  }
  const blaster = configured.filter(isBlaster);
  if (blaster.length > 0) {
    out.push(
      `${blaster.map((b) => `\`${b}\``).join(", ")} ${blaster.length === 1 ? "is a" : "are"} ` +
        `write-only NIP-66 ${blaster.length === 1 ? "blaster" : "blasters"}; ` +
        `acceptance counts as fan-out and is excluded from readback evidence.`,
      "",
    );
  }
  out.push("### Independent readback", "");
  out.push(
    `Exact-id queries against the ${durable.length} durable configured relays after broadcast:`,
    "",
  );
  out.push(`- both events returned by ${bothBack.length}: ${bothBack.map((r) => `\`${r.relay}\``).join(", ") || "none"}`);
  if (partial.length > 0) {
    for (const r of partial) {
      out.push(
        `- only the ${r.article ? "article" : "announcement"} returned by \`${r.relay}\``,
      );
    }
  }
  if (neither.length > 0) {
    out.push(`- neither event returned by: ${neither.map((r) => `\`${r.relay}\``).join(", ")}`);
  }
  out.push("");
  const articleBack = durable.filter((row) => row.article).length;
  const announcementBack = durable.filter((row) => row.announcement).length;
  const relayFloor = args.relayFloor ?? 1;
  const gate =
    artOk > 0 && annOk > 0 && articleBack >= relayFloor && announcementBack >= relayFloor
      ? `GATE: PASS (merge and deploy verified; article accepted by ${artOk}/${configured.length} and announcement by ${annOk}/${configured.length} configured relays; exact-id readback article=${articleBack}, announcement=${announcementBack}, floor=${relayFloor})`
      : `GATE: FAIL (article ok=${artOk}, announcement ok=${annOk}, exact-id readback article=${articleBack}, announcement=${announcementBack}, floor=${relayFloor}; investigate before treating this issue as published)`;
  out.push(
    `The signed events are archived to the untracked local store at ` +
      `\`data/newsletter_workspace/published/${date}_30023.json\` and ` +
      `\`data/newsletter_workspace/published/${date}_1.json\`, byte-identical to ` +
      `\`publish/out/${issue}/event.json\` and \`publish/out/${issue}/announcement.json\`.`,
    "",
  );
  out.push(gate, "");
  return out.join("\n");
}

/**
 * Build the publication log, commit it on a branch and open a PR.
 * Returns the PR number, or null when there was nothing to push.
 */
export async function logIssue(
  issue: number,
  opts: { compassDir: string; openPr: boolean; outDir?: string; relaysPath?: string; authorPath?: string; pageEvidence?: string; notify?: boolean; commandRunner?: typeof run; logWorktreeRoot?: string },
): Promise<number | null> {
  const outDir = opts.outDir ?? OUT_DIR;
  const command = opts.commandRunner ?? run;
  const issueDir = join(outDir, String(issue));
  const metadata = JSON.parse(await readFile(join(issueDir, "metadata.json"), "utf8")) as Metadata;
  const stored: unknown = JSON.parse(await readFile(join(issueDir, "receipts.json"), "utf8"));
  assertCurrentReceiptSchema(stored);
  const receipts = stored.acceptance;
  const journal = await loadJournal(outDir, issue);
  const articleEffect = journal.effects.article, announcementEffect = journal.effects.announcement;
  if (articleEffect?.state !== "confirmed" || announcementEffect?.state !== "confirmed" || journal.effects.merge?.state !== "confirmed" || journal.effects.deploy?.state !== "confirmed" || !journal.pull_request?.merge_sha || !journal.deployment) throw new Error("Canonical journal does not confirm merge, deployment, and both Nostr events");
  for (const [name, effect, filename] of [["article", articleEffect, "event.json"], ["announcement", announcementEffect, "announcement.json"]] as const) {
    const bytes = await readFile(join(issueDir, filename));
    if (!effect.payload_path || !effect.payload_sha256 || sha256(bytes) !== effect.payload_sha256 || effect.payload_path !== join(issueDir, filename)) throw new Error(`Canonical ${name} payload bytes do not match the journal`);
  }
  const article = JSON.parse(await readFile(join(issueDir, "event.json"), "utf8")) as { id: string; created_at: number; tags: string[][] };
  const announcement = JSON.parse(await readFile(join(issueDir, "announcement.json"), "utf8")) as { id: string; created_at: number };
  if (article.id !== articleEffect.event_id || announcement.id !== announcementEffect.event_id) throw new Error("Signed event IDs do not match the canonical journal");
  const ledger: LedgerEntry = {
    issue, event_id: article.id, announcement_id: announcement.id,
    first_published_at: Number(article.tags.find((tag) => tag[0] === "published_at")?.[1] ?? article.created_at),
    last_edited_at: article.created_at,
    banner_url: article.tags.find((tag) => tag[0] === "image")?.[1] ?? "",
    relays_ok: Object.entries(stored.readback.article).filter(([, row]) => row.found).map(([relay]) => relay),
    relays_fail: Object.entries(stored.readback.article).filter(([, row]) => !row.found).map(([relay]) => relay),
  };
  const { relays: configured } = JSON.parse(await readFile(opts.relaysPath ?? RELAYS_PATH, "utf8")) as RelaysConfig;
  const author = JSON.parse(await readFile(opts.authorPath ?? AUTHOR_PATH, "utf8")) as { pubkey_hex: string };

  const date = await resolveIssueDate(opts.compassDir, issue);
  const readback: ReadbackRow[] = configured.filter((relay) => !isBlaster(relay)).map((relay) => ({
    relay,
    article: stored.readback.article[relay]?.found === true,
    announcement: stored.readback.announcement[relay]?.found === true,
  }));
  const articleRecovered = readback.filter((row) => row.article).length;
  const announcementRecovered = readback.filter((row) => row.announcement).length;
  if (articleRecovered < stored.relay_floor || announcementRecovered < stored.relay_floor) throw new Error(`Retained readback floor is not met for both events: article=${articleRecovered}, announcement=${announcementRecovered}, floor=${stored.relay_floor}`);

  const { nip19 } = await import("nostr-tools");
  const hintRelays = configured.filter((r) => !isBlaster(r)).slice(0, 4);
  const naddr = nip19.naddrEncode({
    identifier: `newsletter-${issue}`,
    pubkey: author.pubkey_hex,
    kind: 30023,
    relays: hintRelays,
  });
  const nevent = nip19.neventEncode({
    id: ledger.announcement_id,
    author: author.pubkey_hex,
    relays: hintRelays.slice(0, 2),
  });
  let announcementCreatedAt: number | null = null;
  try {
    const ann = JSON.parse(await readFile(join(issueDir, "announcement.json"), "utf8")) as {
      created_at?: number;
    };
    announcementCreatedAt = ann.created_at ?? null;
  } catch {
    /* the announcement file is optional evidence, not a blocker */
  }

  const page = opts.pageEvidence ?? await pageStatus(date, metadata.title);
  const pr = {
    number: journal.pull_request.number,
    mergeCommit: journal.pull_request.merge_sha,
    mergedAt: null,
  };
  const deploy = {
    id: String(journal.deployment.workflow_run_id),
    conclusion: "success",
  };
  const prerequisites = [
    `- Quality composite: \`${journal.effects.quality?.payload_path ?? "missing"}\` (${journal.effects.quality?.payload_sha256 ?? "missing"})`,
    `- Feedback snapshot: \`${journal.effects.feedback?.payload_path ?? "missing"}\` (${journal.effects.feedback?.payload_sha256 ?? "missing"})`,
    `- Edition authorization: \`${journal.effects.authorization?.payload_path ?? "missing"}\` (${journal.effects.authorization?.payload_sha256 ?? "missing"})`,
  ];
  for (const gate of ["quality", "feedback", "authorization"] as const) {
    const effect = journal.effects[gate];
    if (effect?.state !== "confirmed" || !effect.payload_path || !effect.payload_sha256 || sha256(await readFile(effect.payload_path)) !== effect.payload_sha256) throw new Error(`Canonical ${gate} receipt is missing or changed`);
  }

  const body = renderLog({
    issue,
    date,
    title: metadata.title,
    pr,
    prerequisites,
    deploy,
    page,
    ledger,
    configured,
    receipts,
    readback,
    naddr,
    nevent,
    announcementCreatedAt,
    relayFloor: stored.relay_floor,
  });

  const relPath = `data/newsletter_workspace/publish_log_${date}.md`;
  const branch = `chore/publish-log-${date}`;
  const projectionIntent = sha256(stableJson({
    issue, date, branch, body_sha256: sha256(body),
    receipts_sha256: sha256(await readFile(join(issueDir, "receipts.json"))),
    article_sha256: articleEffect.payload_sha256,
    announcement_sha256: announcementEffect.payload_sha256,
  }));
  const priorProjection = journal.effects.log_projection;
  if (priorProjection && priorProjection.intent_sha256 !== projectionIntent) throw new Error("Canonical log projection intent changed after projection started");
  const logRoot = opts.logWorktreeRoot ?? process.env.COMPASS_LOG_WORKTREE_ROOT ?? join(opts.compassDir, "..", ".compass-log-worktrees");
  const logDir = join(logRoot, `issue-${issue}`);
  await mkdir(logRoot, { recursive: true });
  if (opts.openPr) {
    const present = await command("git", ["-C", logDir, "rev-parse", "--is-inside-work-tree"]);
    if (present.code !== 0) {
      const fetch = await command("git", ["-C", opts.compassDir, "fetch", "origin", "--quiet"]);
      if (fetch.code !== 0) throw new Error(`git fetch failed: ${fetch.stderr.trim()}`);
      const addWorktree = await command("git", ["-C", opts.compassDir, "worktree", "add", "--force", "-B", branch, logDir, "origin/main"]);
      if (addWorktree.code !== 0) throw new Error(`isolated log worktree creation failed: ${addWorktree.stderr.trim()}`);
    } else {
      const fetch = await command("git", ["-C", logDir, "fetch", "origin", "--quiet"]);
      if (fetch.code !== 0) throw new Error(`isolated log worktree fetch failed: ${fetch.stderr.trim()}`);
      const checkout = await command("git", ["-C", logDir, "checkout", "-B", branch, "origin/main"]);
      if (checkout.code !== 0) throw new Error(`isolated log worktree reset failed: ${checkout.stderr.trim()}`);
    }
  }
  const projectionRoot = opts.openPr ? logDir : opts.compassDir;
  const absPath = join(projectionRoot, relPath);
  const git = (...args: string[]) => command("git", ["-C", projectionRoot, ...args]);
  await mkdir(join(projectionRoot, "data/newsletter_workspace"), { recursive: true });
  await writeAtomic(absPath, body);
  await mutateJournal(outDir, issue, (current) => {
    current.effects.log_projection = {
      state: opts.openPr ? "attempted" : "prepared",
      intent_sha256: projectionIntent,
      payload_path: absPath,
      payload_sha256: sha256(body),
    };
  });
  console.log(`              wrote ${relPath} in ${projectionRoot}`);

  // Archive the signed events beside the other publication artifacts. This
  // directory is untracked by repo convention; the copy exists so the exact
  // signed bytes survive independently of publish/out/.
  const archiveDir = join(projectionRoot, "data/newsletter_workspace/published");
  await mkdir(archiveDir, { recursive: true });
  for (const [src, dst] of [
    ["event.json", `${date}_30023.json`],
    ["announcement.json", `${date}_1.json`],
  ]) {
    try {
      await writeAtomic(join(archiveDir, dst), await readFile(join(issueDir, src), "utf8"));
    } catch (e) {
      console.error(`              warning: could not archive ${src}: ${(e as Error).message}`);
    }
  }

  if (!opts.openPr) {
    console.log("              --no-log-pr: leaving the log uncommitted");
    return null;
  }

  const add = await git("add", "--", relPath);
  if (add.code !== 0) throw new Error(`git add failed: ${add.stderr.trim()}`);
  const diff = await git("diff", "--cached", "--quiet");
  if (diff.code === 0) {
    console.log("              log already matches main; nothing to push");
    await mutateJournal(outDir, issue, (current) => {
      current.effects.log_projection.state = "confirmed";
      current.effects.log_projection.event_id = "already-on-main";
    });
    return null;
  }

  const markAmbiguous = async (error: Error) => mutateJournal(outDir, issue, (current) => {
    current.effects.log_projection.state = "ambiguous";
    current.effects.log_projection.error = error.message;
  });
  const findOpenPr = async (): Promise<number | null> => {
    const result = await command("gh", ["pr", "list", "--repo", REPO, "--head", branch, "--state", "open", "--json", "number,headRefName,url"]);
    if (result.code !== 0) throw new Error(`exact log PR readback failed: ${result.stderr.trim()}`);
    let rows: { number: number; headRefName: string; url: string }[];
    try { rows = JSON.parse(result.stdout); } catch { throw new Error("exact log PR readback returned malformed JSON"); }
    if (!Array.isArray(rows) || rows.length > 1) throw new Error("exact log PR readback returned an ambiguous result set");
    if (rows.length === 0) return null;
    const row = rows[0];
    if (!Number.isInteger(row.number) || row.headRefName !== branch || row.url !== `https://github.com/${REPO}/pull/${row.number}`) throw new Error("exact log PR readback did not match the projected branch and canonical URL");
    return row.number;
  };

  let prNumber: number | null = null;
  try {
    const commit = await git("commit", "-q", "-m", `Add Newsletter #${issue} publication log`);
    if (commit.code !== 0) throw new Error(`git commit failed: ${commit.stderr.trim()}`);
    const push = await git("push", "-q", "--force-with-lease", "-u", "origin", branch);
    if (push.code !== 0) throw new Error(`git push failed: ${push.stderr.trim()}`);

    prNumber = await findOpenPr();
    if (prNumber === null) {
      await command("gh", [
        "pr", "create", "--repo", REPO, "--head", branch,
        "--title", `Add Newsletter #${issue} publication log`,
        "--body", `Publication evidence for ${metadata.title}, projected by the publish pipeline's log stage from the schema-versioned per-edition journal, retained receipt bytes, and exact external readbacks.`,
      ]);
      // The create response is not evidence: success can lose its response and
      // failure can happen after GitHub committed the PR. Reconcile by exact
      // branch readback in either case.
      prNumber = await findOpenPr();
    }
    if (prNumber === null) throw new Error("log projection push completed but exact pull-request identity could not be reconciled");
  } catch (error) {
    await markAmbiguous(error as Error);
    throw error;
  }

  await mutateJournal(outDir, issue, (current) => {
    current.effects.log_projection.state = "confirmed";
    current.effects.log_projection.event_id = String(prNumber);
    current.effects.log_projection.error = undefined;
  });

  // Two distinct steps finished here, so both are announced: the deploy landed
  // and the log PR exists.
  if (opts.notify !== false && deploy !== null) {
    await notifyMilestone(issue, "deployed", [
      `Deploy ${runLink(deploy.id)} concluded \`${deploy.conclusion}\`.`,
      `Canonical page returned ${page}.`,
    ]);
  }
  if (opts.notify !== false) await notifyMilestone(issue, "log-pr-opened", [
    prNumber === null
      ? `Publication log written to \`${relPath}\`.`
      : `Publication log PR ${prLink(prNumber)} opened for \`${relPath}\`.`,
    `Verdict: ${body.trimEnd().split("\n").filter((l) => l.startsWith("GATE:")).at(-1) ?? "no gate line"}`,
  ]);

  return prNumber;
}
