import { describe, expect, test } from "bun:test";
import { buildAnnouncementContent } from "./announcement.ts";

describe("buildAnnouncementContent", () => {
  test("turns the newsletter opening section into a dense kind 1 note", () => {
    const body = [
      "Welcome back to Nostr Compass, your weekly guide to Nostr.",
      "",
      "**This week:** [IndieSats](#indiesats) nostr:npub1indie opens publishing, while [Nostrord](#nostrord) ships group moderation.",
      "",
      "Tagged releases bring [Amber](#amber) with grouped signing approvals and [nak](https://github.com/fiatjaf/nak) with NIP-34 workflows.",
      "",
      "---",
      "",
      "## Lead stories",
      "",
      "This must not appear in the announcement.",
    ].join("\n");

    expect(buildAnnouncementContent("Nostr Compass #33", body, "naddr1article")).toBe(
      [
        "Nostr Compass #33 is out. Here is what changed across Nostr this week:",
        "",
        "IndieSats nostr:npub1indie opens publishing, while Nostrord ships group moderation.",
        "",
        "Tagged releases bring Amber with grouped signing approvals and nak with NIP-34 workflows.",
        "",
        "Read the full issue: nostr:naddr1article",
      ].join("\n"),
    );
  });

  test("stops at the first H2 when the opening has no horizontal rule", () => {
    const body = "**This week:** Dense opening.\n\n## Shipping This Week\n\nNot part of the opening.";

    expect(buildAnnouncementContent("Nostr Compass #34", body, "naddr1next")).toContain(
      "Dense opening.\n\nRead the full issue: nostr:naddr1next",
    );
    expect(buildAnnouncementContent("Nostr Compass #34", body, "naddr1next")).not.toContain(
      "Shipping This Week",
    );
  });
});
