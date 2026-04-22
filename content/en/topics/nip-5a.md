---
title: "NIP-5A: Static Websites"
date: 2026-04-01
draft: false
categories:
  - Protocol
  - Hosting
---

NIP-5A defines how to host static websites under Nostr keypairs. Site authors publish signed manifest events that map URL paths to SHA256 content hashes, and host servers resolve those manifests to serve the site's files from Blossom storage.

## How It Works

The spec uses two event kinds. Kind `15128` is a root site manifest, one per pubkey, which serves as the default website for that key. Kind `35128` is a named site manifest, identified by a `d` tag, which acts like a subdomain. Each manifest contains `path` tags mapping absolute URL paths to SHA256 hashes of the files that should be served.

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

A host server receives an HTTP request, extracts the author's pubkey from the subdomain, fetches the site manifest from the author's relay list, resolves the requested path to a content hash, and downloads the matching blob from the Blossom server(s) listed in `server` tags.

## URL Resolution

Root sites use the npub as the subdomain. Named sites use a 50-character base36 encoding of the raw pubkey followed by the `d` tag value, all in a single DNS label. Because DNS labels are limited to 63 characters and the base36 pubkey always uses 50, named site identifiers are limited to 13 characters.

## Implementations

- [nsite](https://github.com/lez/nsite) - Host server that resolves NIP-5A manifests and serves files
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - UI for building and publishing site manifests

---

**Primary sources:**
- [NIP-5A Specification](https://github.com/nostr-protocol/nips/blob/master/5A.md)
- [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) - Original proposal and merge
- [nsite](https://github.com/lez/nsite) - Reference host implementation
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - Publishing and management UI

**Mentioned in:**
- [Newsletter #16: NIP-5A merges](/en/newsletters/2026-04-01-newsletter/#nip-5a-merges-bringing-static-websites-to-nostr)
- [Newsletter #16: NIP Deep Dive](/en/newsletters/2026-04-01-newsletter/#nip-deep-dive-nip-5a-static-websites)
- [Newsletter #19: NIP-5D applets proposal](/en/newsletters/2026-04-22-newsletter/#nip-updates)

**See also:**
- [Blossom](/en/topics/blossom/)
- [NIP-65: Relay List Metadata](/en/topics/nip-65/)
- [NIP-96: HTTP File Storage](/en/topics/nip-96/)
