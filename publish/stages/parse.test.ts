import { describe, expect, test } from "bun:test";
import { parsePublishSource } from "./parse.ts";

const bannerUrl = "https://example.com/cover.png";

describe("parsePublishSource", () => {
  test("parses the four-block format without a separate announcement block", () => {
    const tldr = "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twenty-one";
    const raw = [
      "Nostr Compass #33",
      "",
      tldr,
      "",
      bannerUrl,
      "",
      "Welcome back to Nostr Compass.",
      "",
      "**This week:** Dense opening section.",
      "",
      "## Lead stories",
      "",
      "Full body prose.",
      "",
      "Tags: nostr, clients",
    ].join("\n");

    const metadata = parsePublishSource(raw, 33, bannerUrl, "/tmp/33publish.md");

    expect(metadata.body).toStartWith("Welcome back to Nostr Compass.");
    expect(metadata.body).toContain("## Lead stories");
    expect(metadata.tags).toEqual(["nostr", "clients"]);
    expect("announcement" in metadata).toBe(false);
  });

  test("discards the separate announcement block from legacy five-block sources", () => {
    const tldr = "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twenty-one";
    const raw = [
      "Nostr Compass #32",
      "",
      tldr,
      "",
      bannerUrl,
      "",
      "Nostr Compass #32 is out. This legacy announcement must not become article prose.",
      "",
      "Welcome back to Nostr Compass.",
      "",
      "**This week:** Dense opening section.",
    ].join("\n");

    const metadata = parsePublishSource(raw, 32, bannerUrl, "/tmp/32publish.md");

    expect(metadata.body).toStartWith("Welcome back to Nostr Compass.");
    expect(metadata.body).not.toContain("legacy announcement");
  });
});
