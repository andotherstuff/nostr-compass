import { describe, expect, test } from "bun:test";
import {
  buildOutreachMessage,
  filterRecipients,
  OUTREACH_REPORT_SCHEMA_VERSION,
  outreachReportSuffix,
  resolveOutreachRoots,
} from "./lib/outreach-scope.ts";

type Recipient = { npub: string; names: string[]; primaryName: string };

const recipients: Recipient[] = [
  {
    npub: "npub1nostrology",
    names: ["Nostrology", "WhisperHash maintainer"],
    primaryName: "Nostrology",
  },
  {
    npub: "npub1other",
    names: ["Other Project"],
    primaryName: "Other Project",
  },
];

describe("targeted pre-publication outreach", () => {
  test("keeps runtime secrets and receipts canonical while reading a weekly worktree", () => {
    expect(resolveOutreachRoots("/srv/compass", "/srv/compass-worktrees/2026-08-26")).toEqual({
      workspaceRoot: "/srv/compass-worktrees/2026-08-26",
      runtimeRoot: "/srv/compass",
    });
    expect(OUTREACH_REPORT_SCHEMA_VERSION).toBe(1);
  });

  test("filters by any project or maintainer alias without duplicating a shared npub", () => {
    expect(filterRecipients(recipients, ["whisperhash maintainer"])).toEqual([recipients[0]]);
    expect(filterRecipients(recipients, ["NOSTROLOGY", "whisperhash maintainer"])).toEqual([recipients[0]]);
  });

  test("throws when a requested target does not resolve", () => {
    expect(() => filterRecipients(recipients, ["missing project"])).toThrow(
      "No outreach recipient matched: missing project",
    );
  });

  test("creates separate receipt suffixes for follow-up and reminder outreach", () => {
    expect(outreachReportSuffix(["Nostrology", "WhisperHash maintainer"])).toBe(
      "-nostrology-whisperhash-maintainer",
    );
    expect(outreachReportSuffix([], true)).toBe("-reminder");
    expect(outreachReportSuffix(["Nostrology"], true)).toBe("-nostrology-reminder");
    expect(outreachReportSuffix([], false, true)).toBe("-rerecord");
    expect(outreachReportSuffix([])).toBe("");
  });

  test("builds review-only copy with the GitHub PR link", () => {
    expect(
      buildOutreachMessage({
        reminder: false,
        reviewUrl: "https://github.com/andotherstuff/nostr-compass/pull/147",
        newsletterUrl: "",
        podcastUrl: "",
        podcastTime: "",
      }),
    ).toBe(
      "Hey, your project is mentioned in the draft for this week's Nostr Compass newsletter. Could you review the coverage on GitHub before publication? https://github.com/andotherstuff/nostr-compass/pull/147",
    );
  });

  test("rejects legacy podcast and re-record outreach", () => {
    const base = {
      issue: 38,
      reviewUrl: "",
      newsletterUrl: "https://nostrcompass.org/en/newsletters/2026-09-02-newsletter/",
      podcastUrl: "https://riverside.example/studio",
      podcastTime: "Thursday at 16:00 UTC",
    };
    expect(() => buildOutreachMessage({ ...base, reminder: true })).toThrow(
      "Podcast outreach is paused pending the new post-publication setup.",
    );
    expect(() => buildOutreachMessage({ ...base, reminder: false, rerecord: true })).toThrow(
      "Podcast outreach is paused pending the new post-publication setup.",
    );
  });
});
