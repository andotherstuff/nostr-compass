import { describe, expect, test } from "bun:test";
import { extractMentions } from "../scripts/publish";

const npubs = {
  mosaico: { npub: "npub1mosaico", mention_only: false },
  amethyst: { npub: "npub1amethyst", mention_only: false },
  gitworkshop: { npub: "npub1gitworkshop", mention_only: false },
  fips: { npub: "npub1fips", mention_only: false },
  nostur: { npub: "npub1nostur", mention_only: false },
  "swift-nostr": { npub: "npub1swiftnostr", mention_only: false },
  "lawallet-nwc": { npub: "npub1lawalletnwc", mention_only: false },
};

describe("publish mention extraction", () => {
  test("treats only application-section H3 headings as projects", () => {
    const body = `## Top Stories

### Mosaico 0.1.2 gives agents a shared fabric

Text.

## In Development

### Amethyst recovers stalled syncs

Text.

## Protocol and Spec Work

### Merged

### Mutual key-set declarations

### [BOLT12 zaps](/en/topics/nip-57/)

## NIP Deep Dive: Six Nostr Julys, 2021 to 2026

### July 2021

### July 2026
`;

    const result = extractMentions(body, npubs);

    expect(result.found.map((entry) => entry.name)).toEqual(["Amethyst", "Mosaico"]);
    expect(result.missing).toEqual([]);
  });

  test("uses exact project headings and ignores protocol repositories and footer links", () => {
    const body = `## Top Stories

### GitWorkshop coordinates maintainers and keeps repository sync independent

Text.

## Tagged Releases

### Nostur 1.30.1 tightens sharing and duplicate-post protection

Text.

## In Development

### FIPS opens an OpenWrt access layer and starts a FreeBSD port

Text.

## Protocol and Spec Work

### Gamma Markets: no public specification changes landed

The [Gamma Markets specification repository](https://github.com/GammaMarkets/market-spec) had no changes.

Send a note through the [Nostr Compass project](https://github.com/andotherstuff/nostr-compass).
`;

    const result = extractMentions(body, npubs);

    expect(result.found.map((entry) => entry.name)).toEqual(["FIPS", "GitWorkshop", "Nostur"]);
    expect(result.missing).toEqual([]);
  });

  test("keeps lowercase hyphenated project names from application headings", () => {
    const body = `## Tagged Releases

### swift-nostr 0.7.0

Text.

### lawallet-nwc 2.0.0

Text.

## Protocol and Spec Work

### nostr-protocol repository activity
`;

    const result = extractMentions(body, npubs);

    expect(result.found.map((entry) => entry.name)).toEqual(["lawallet-nwc", "swift-nostr"]);
    expect(result.missing).toEqual([]);
  });
});
