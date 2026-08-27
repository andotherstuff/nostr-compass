// Milestone notifications for the publish pipeline.
//
// WHY THIS EXISTS
// ---------------
// Publishing #37 reached Nostr and the website with nobody watching, and the
// two failures that followed (no publish log for #36, wrong relay facts in the
// first #37 log) were only found by hand afterwards. A milestone line per stage
// makes each transition observable at the time it happens.
//
// The configured notification target already owns this project's outcomes, so
// the pipeline posts into that one channel. AGENTS.md § "One producer owns each
// recurring report" forbids standing up a second cron producer for the same
// outcome, and this respects that: same owner, same channel, no new job.
//
// A notification is never allowed to fail a publish. Every error is swallowed
// and reported on stderr. Each (issue, milestone) pair sends at most once, so
// re-running a stage after a fix does not re-announce it.

import { readFile, mkdir, writeFile, access } from "node:fs/promises";
import { join } from "node:path";
import { spawn } from "node:child_process";

const RUNTIME_ROOT = join(import.meta.dir, "..");
const NOTIFY_CONFIG = join(RUNTIME_ROOT, "config/notify.json");
const OUT_DIR = join(RUNTIME_ROOT, "out");
const REPO_URL = "https://github.com/andotherstuff/nostr-compass";

export type Milestone =
  | "parsed"
  | "signed"
  | "announced"
  | "broadcast"
  | "merged"
  | "deployed"
  | "logged"
  | "log-pr-opened"
  | "outreach-sent"
  | "translated-language"
  | "translation-pr-opened"
  | "translated"
  | "backlog"
  | "failed";

type NotifyConfig = { enabled: boolean; target: string; command?: string[] };

/**
 * The delivery command, as argv with {target} and {body} placeholders.
 *
 * The transport is host wiring, not part of the publication logic, so it is
 * configured rather than compiled in. config/notify.json is gitignored; see
 * config/notify.example.json for the shape and skills/_COMPASS/LOCAL_OPS.md for
 * this install's values. Without a configured command there is nothing to send
 * to, and notification is skipped rather than guessed at.
 */
type Notifier = { target: string; command: string[] };

const SUBJECTS: Record<Milestone, string> = {
  parsed: "Draft parsed",
  signed: "Article signed",
  announced: "Announcement signed",
  broadcast: "Broadcast to relays",
  merged: "Newsletter PR merged",
  deployed: "Website deployed",
  logged: "Publication log recorded",
  "log-pr-opened": "Publication log PR opened",
  "outreach-sent": "Outreach DMs sent",
  "translated-language": "Language translated",
  "translation-pr-opened": "Translation PR opened",
  translated: "Translations merged",
  backlog: "Translation backlog",
  failed: "Publish halted",
};

function parseCommand(raw: string | undefined): string[] | null {
  if (!raw) return null;
  try {
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) && parsed.every((a) => typeof a === "string") ? parsed : null;
  } catch {
    return null;
  }
}

async function loadConfig(): Promise<Notifier | null> {
  if (process.env.COMPASS_NOTIFY === "0") return null;
  let cfg: NotifyConfig | null = null;
  try {
    cfg = JSON.parse(await readFile(NOTIFY_CONFIG, "utf8")) as NotifyConfig;
  } catch {
    // An absent config is the normal state for a fresh clone, not an error.
  }
  const target = process.env.COMPASS_NOTIFY_TARGET || cfg?.target;
  if (!cfg?.enabled && !process.env.COMPASS_NOTIFY_TARGET) return null;
  if (!target) {
    console.error("notify: no target configured; skipping");
    return null;
  }
  const command = parseCommand(process.env.COMPASS_NOTIFY_COMMAND) || cfg?.command;
  if (!command || command.length === 0) {
    console.error(
      "notify: no delivery command configured; set command in config/notify.json " +
        "or COMPASS_NOTIFY_COMMAND (JSON argv). Skipping.",
    );
    return null;
  }
  return { target, command };
}

/**
 * Render a PR number as a full Markdown link. MARMOT_MESSAGE_MARKDOWN.md
 * requires every forge reference in user-facing text to be a link, never a
 * bare `PR #N`.
 */
export function prLink(pr: number): string {
  return `[#${pr}](${REPO_URL}/pull/${pr})`;
}

export function runLink(runId: number | string): string {
  return `[run ${runId}](${REPO_URL}/actions/runs/${runId})`;
}

/**
 * Compact bullets, not a table: Marmot truncates long bodies and pipe tables
 * fail silently when the delimiter row does not match the header.
 */
export function renderMessage(
  issue: number,
  milestone: Milestone,
  lines: string[],
  suffix?: string,
): string {
  // "issue 37", not "#37": MARMOT_MESSAGE_MARKDOWN.md forbids a bare `#N`
  // because a reader cannot tell a newsletter number from a PR number, and a
  // heading like "#37 — Publication log PR [#144]" is exactly that ambiguity.
  const head =
    `Nostr Compass issue ${issue} — ${SUBJECTS[milestone]}` + (suffix ? ` (${suffix})` : "");
  const body = lines.filter((l) => l.trim().length > 0).map((l) => `- ${l.trim()}`);
  return body.length > 0 ? `**${head}**\n${body.join("\n")}` : `**${head}**`;
}

/**
 * Some steps repeat legitimately within one issue — one per language, for
 * instance — so the caller can pass a key to scope the once-only guard. Without
 * a key the milestone name is the key.
 */
function markerName(milestone: Milestone, key?: string): string {
  return key ? `${milestone}.${key.replace(/[^a-zA-Z0-9._-]/g, "_")}` : milestone;
}

async function alreadySent(issue: number, milestone: Milestone, key?: string): Promise<boolean> {
  try {
    await access(join(OUT_DIR, String(issue), "notified", markerName(milestone, key)));
    return true;
  } catch {
    return false;
  }
}

async function markSent(issue: number, milestone: Milestone, key?: string): Promise<void> {
  const dir = join(OUT_DIR, String(issue), "notified");
  await mkdir(dir, { recursive: true });
  await writeFile(join(dir, markerName(milestone, key)), `${new Date().toISOString()}\n`, "utf8");
}

export function renderCommand(command: string[], target: string, body: string): string[] {
  return command.map((arg) => arg.replace("{target}", target).replace("{body}", body));
}

export function runDeliveryCommand(
  command: string[],
  target: string,
  body: string,
  timeoutMs = 15_000,
): Promise<number> {
  return new Promise((resolve) => {
    const [cmd, ...args] = renderCommand(command, target, body);
    const child = spawn(cmd, args, { stdio: ["ignore", "ignore", "pipe"] });
    let stderr = "";
    let settled = false;
    const finish = (code: number): void => {
      if (settled) return;
      settled = true;
      clearTimeout(timeout);
      resolve(code);
    };
    const timeout = setTimeout(() => {
      console.error(`notify: ${cmd} timed out after ${timeoutMs}ms`);
      child.kill("SIGTERM");
      const forceKill = setTimeout(() => child.kill("SIGKILL"), 1_000);
      forceKill.unref();
      finish(124);
    }, timeoutMs);
    timeout.unref();
    child.stderr.on("data", (d) => (stderr += d.toString()));
    child.on("error", (e) => {
      console.error(`notify: ${cmd} failed to start: ${e.message}`);
      finish(1);
    });
    child.on("close", (code) => {
      if (code !== 0 && !settled) console.error(`notify: ${cmd} exit ${code}: ${stderr.trim()}`);
      finish(code ?? 1);
    });
  });
}

function send(notifier: Notifier, body: string): Promise<number> {
  return runDeliveryCommand(notifier.command, notifier.target, body);
}

/**
 * Announce one milestone. Returns true when a message was delivered.
 * Never throws: publishing must not depend on the messaging gateway.
 */
export async function notifyMilestone(
  issue: number,
  milestone: Milestone,
  lines: string[],
  opts: { key?: string; suffix?: string } = {},
): Promise<boolean> {
  try {
    const cfg = await loadConfig();
    if (!cfg) return false;
    if (milestone !== "failed" && (await alreadySent(issue, milestone, opts.key))) return false;
    const code = await send(cfg, renderMessage(issue, milestone, lines, opts.suffix));
    if (code !== 0) return false;
    if (milestone !== "failed") await markSent(issue, milestone, opts.key);
    return true;
  } catch (e) {
    console.error(`notify: ${(e as Error).message}`);
    return false;
  }
}
