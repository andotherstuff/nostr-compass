// Formatting helpers retained for structured Compass milestone records.
//
// Repository code never delivers milestone messages. The host-owned durable
// outbox/reconciler is the sole notification producer and owns retries,
// idempotency, routing, and delivery readback.

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

/** Render a PR number as a full Markdown link. */
export function prLink(pr: number): string {
  return `[#${pr}](${REPO_URL}/pull/${pr})`;
}

export function runLink(runId: number | string): string {
  return `[run ${runId}](${REPO_URL}/actions/runs/${runId})`;
}

/** Compact bullets, not a table, for host-owned milestone records. */
export function renderMessage(
  issue: number,
  milestone: Milestone,
  lines: string[],
  suffix?: string,
): string {
  const head =
    `Nostr Compass issue ${issue} — ${SUBJECTS[milestone]}` + (suffix ? ` (${suffix})` : "");
  const body = lines.filter((line) => line.trim().length > 0).map((line) => `- ${line.trim()}`);
  return body.length > 0 ? `**${head}**\n${body.join("\n")}` : `**${head}**`;
}

/**
 * Compatibility hook for repository stages that still record milestone-shaped
 * data. It deliberately performs no I/O. The host durable outbox/reconciler
 * observes committed state and is the only component allowed to deliver.
 */
export async function notifyMilestone(
  _issue: number,
  _milestone: Milestone,
  _lines: string[],
  _opts: { key?: string; suffix?: string } = {},
): Promise<boolean> {
  return false;
}
