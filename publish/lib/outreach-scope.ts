export type OutreachRecipient = {
  npub: string;
  names: string[];
  primaryName: string;
};

export const OUTREACH_REPORT_SCHEMA_VERSION = 1;

export function resolveOutreachRoots(runtimeRoot: string, workspaceOverride?: string): {
  workspaceRoot: string;
  runtimeRoot: string;
} {
  return {
    workspaceRoot: workspaceOverride || runtimeRoot,
    runtimeRoot,
  };
}

function normalizeName(value: string): string {
  return value.trim().toLocaleLowerCase();
}

export function filterRecipients<T extends OutreachRecipient>(recipients: T[], onlyNames: string[]): T[] {
  if (onlyNames.length === 0) return recipients;

  const targets = [...new Set(onlyNames.map(normalizeName).filter(Boolean))];
  const matchedTargets = new Set<string>();
  const selected = recipients.filter((recipient) => {
    const aliases = [recipient.primaryName, ...recipient.names].map(normalizeName);
    const matches = targets.filter((target) => aliases.includes(target));
    matches.forEach((target) => matchedTargets.add(target));
    return matches.length > 0;
  });

  const missing = targets.filter((target) => !matchedTargets.has(target));
  if (missing.length > 0) {
    throw new Error(`No outreach recipient matched: ${missing.join(", ")}`);
  }

  return [...new Map(selected.map((recipient) => [recipient.npub, recipient])).values()];
}

export type OutreachMessageArgs = {
  reminder: boolean;
  rerecord?: boolean;
  issue?: number;
  reviewUrl: string;
  newsletterUrl: string;
  podcastUrl: string;
  podcastTime: string;
};

export function buildOutreachMessage(args: OutreachMessageArgs): string {
  if (args.reminder || args.rerecord) {
    throw new Error("Podcast outreach is paused pending the new post-publication setup.");
  }
  if (!args.reviewUrl) {
    throw new Error("Newsletter review outreach requires a GitHub PR URL.");
  }
  return `Hey, your project is mentioned in the draft for this week's Nostr Compass newsletter. Could you review the coverage on GitHub before publication? ${args.reviewUrl}`;
}

export function outreachReportSuffix(onlyNames: string[], reminder = false, rerecord = false): string {
  const reminderSuffix = rerecord ? "-rerecord" : reminder ? "-reminder" : "";
  if (onlyNames.length === 0) return reminderSuffix;
  const slug = [...new Set(onlyNames.map(normalizeName).filter(Boolean))]
    .map((name) => name.replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, ""))
    .filter(Boolean)
    .join("-");
  return slug ? `-${slug}${reminderSuffix}` : reminderSuffix;
}
