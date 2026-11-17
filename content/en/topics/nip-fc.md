---
title: "NIP-FC: Maven Repositories"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

NIP-FC is a proposed NIP for distributing JVM artifacts, including Kotlin and Android libraries, through Nostr and Blossom. It is open and unmerged as nostr-protocol/nips#2547 and is not an accepted NIP.

Artifact files are stored on Blossom servers. A canonical manifest lists each file by its SHA-256 hash. The publisher signs the manifest as a kind 3071 event for a release or as an addressable kind 33071 event for a snapshot. A bridge reads these events and serves the files at standard Maven repository paths.

Releases use NIP-05 for publisher identity, which lets a consumer pin the publisher's key. Clients find the events and blobs through NIP-65 relay lists and server discovery. Consumers are expected to keep their own record of publisher keys and manifest hashes.

The proposal states its limits. If a publisher key is compromised, preferring the earliest timestamped release does not make a version immutable. Continuity between releases depends on the pins each consumer stores locally. The draft is not a replacement for Maven Central. An implemented Gradle integration path is not established in the reviewed evidence.

**Primary sources:**
- [nostr-protocol/nips#2547](https://github.com/nostr-protocol/nips/pull/2547)

**Mentioned in:**
- [Newsletter #49 (2026-11-18)](/en/newsletters/2026-11-18-newsletter/#nostr-protocol-nips-2547)

**See also:**
- [NIP-05: Mapping Nostr Keys to DNS-based Internet Identifiers](/en/topics/nip-05/)
- [NIP-65: Relay List Metadata](/en/topics/nip-65/)
- [Blossom](/en/topics/blossom/)
