import { describe, expect, test } from "bun:test";
import { extractMentions } from "../scripts/publish";
import type { NpubMap } from "../scripts/lib/npub-database";

function project(npub: string) {
  return {
    npub,
    identity_type: "project" as const,
    evidence: [],
    outreach: true,
    mention_only: false,
    legacy: false,
  };
}

const npubs: NpubMap = {
  mosaico: project("npub1mosaico"),
  amethyst: project("npub1amethyst"),
  gitworkshop: project("npub1gitworkshop"),
  fips: project("npub1fips"),
  nostur: project("npub1nostur"),
  "swift-nostr": project("npub1swiftnostr"),
  "lawallet-nwc": project("npub1lawalletnwc"),
  mill: project("npub1mill"),
  nail: project("npub1nail"),
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

  test("includes projects introduced under Newly Discovered", () => {
    const body = `## Newly Discovered

### Nail bridges Nostr and email

Text.

## Protocol and Spec Work

### Protocol update
`;

    const result = extractMentions(body, npubs);

    expect(result.found.map((entry) => entry.name)).toEqual(["Nail"]);
    expect(result.missing).toEqual([]);
  });

  test("includes an exact curated project heading from protocol work", () => {
    const body = `## Protocol Work

### Mill implements a draft for cloud-account key backup

Text.

### BUDs: Blossom servers may identify unknown uploads

Text.
`;

    const result = extractMentions(body, npubs);

    expect(result.found.map((entry) => entry.name)).toEqual(["Mill"]);
    expect(result.missing).toEqual([]);
  });

  test("separates researched unresolved identities from unknown missing names", () => {
    const body = `## Tagged Releases

### Granary v11.0 adds NIP-71 support

Text.
`;
    const result = extractMentions(body, npubs, {
      granary: {
        checked_at: "2026-08-02",
        reason: "No verified identity.",
        sources: ["https://github.com/snarfed/granary"],
      },
    });

    expect(result.unresolved.map((entry) => entry.name)).toEqual(["Granary"]);
    expect(result.missing).toEqual([]);
  });

  test("alias order cannot downgrade a project representative to an unlabeled individual", () => {
    const shared = "npub1shared";
    const identities: NpubMap = {
      keep: {
        ...project(shared),
        identity_type: "maintainer",
        person: "wksantiago",
        mention_only: true,
      },
      wksantiago: {
        ...project(shared),
        identity_type: "individual",
      },
    };
    const body = `## In Development

### wksantiago updates signing

Text.

### Keep updates signing

Text.
`;
    const result = extractMentions(body, identities);
    expect(result.found).toHaveLength(1);
    expect(result.found[0].name).toBe("Keep");
    expect(result.found[0].identity_type).toBe("maintainer");
  });

  test("publishing exposes only outreach-eligible resolved recipients", () => {
    const marmot = project("npub1marmot");
    const sirius = { ...project("npub1sirius"), outreach: false };
    const identities: NpubMap = { marmot, sirius };
    const body = `## In Development

### Marmot updates messaging

Text.

### Sirius updates signing

Text.
`;
    const result = extractMentions(body, identities, {}, new Set(["npub1marmot"]));
    expect(result.found.map((entry) => entry.name)).toEqual(["Marmot", "Sirius"]);
    expect(result.outreachRecipients).toEqual([]);
  });
});
