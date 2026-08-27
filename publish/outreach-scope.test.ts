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

  test("builds a one-hour podcast reminder without repeating review copy", () => {
    expect(
      buildOutreachMessage({
        reminder: true,
        reviewUrl: "",
        newsletterUrl: "https://nostrcompass.org/en/newsletters/2026-07-29-newsletter/",
        podcastUrl: "https://riverside.example/studio",
        podcastTime: "today at 16:00 UTC",
      }),
    ).toBe(
      "Reminder: the Nostr Compass podcast starts today at 16:00 UTC. Your project is part of this week's discussion. Join if you are free: https://riverside.example/studio",
    );
  });

  test("builds an explicit recording-failure re-record invitation", () => {
    expect(
      buildOutreachMessage({
        reminder: false,
        rerecord: true,
        issue: 30,
        reviewUrl: "",
        newsletterUrl: "https://nostrcompass.org/en/newsletters/2026-07-08-newsletter/",
        podcastUrl: "https://riverside.example/studio",
        podcastTime: "today at 15:00 UTC",
      }),
    ).toBe(
      "Recording update: we need to re-record Nostr Compass #30 after a recording failure. We start today at 15:00 UTC. Your project was part of that episode's discussion. Join if you are free: https://riverside.example/studio",
    );
  });
});
