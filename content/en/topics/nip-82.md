---
title: "Proposed NIP-82 (Unassigned): Software Application Catalog"
date: 2026-06-17
lastmod: 2026-10-28
draft: false
categories:
  - Proposals
  - Apps
---

The software application catalog described on this page is a proposal under review. It is not an accepted NIP. It lives in [nostr-protocol/nips pull request #2526](https://github.com/nostr-protocol/nips/pull/2526), titled "Zapstore spec". As of this page's last update, that pull request is open and unmerged, and the official NIPs master branch contains no `82.md` file. "NIP-82" is the label the proposal uses for itself. It is not an official NIP number. Event kinds, tags and behaviour may change before any merge. The pull request says it supersedes the earlier [pull request #1336](https://github.com/nostr-protocol/nips/pull/1336).

## Proposed event kinds

The draft divides a software catalog into several kinds of event:

- **Kind 32267, application:** an addressable event that describes an app.
- **Kind 30063, release:** an addressable event for one version of that app. It references that version's assets.
- **Kind 3063, asset:** a regular event that describes one downloadable file.
- **Kind 30267, curation:** an addressable list that a curator publishes to group or recommend apps.
- **Kind 30509, signing certificate link:** an addressable event that links an X.509 certificate, such as an APK signing certificate, to the Nostr key that publishes software, so clients know which certificates that publisher controls. Its `d` tag is the SHA-256 hash of the DER-encoded certificate. It carries a signature made with the certificate's private key and an expiry as a Unix timestamp, and it can optionally mark the link as revoked.
- **Kind 10067, relay list:** a replaceable list of relays where catalog events can be found.

## Platform, integrity and validity

Asset events carry platform and runtime identifiers, so a client can show only the files that match a device. Each asset also carries a file hash. A client can use it to check that the downloaded bytes match what the publisher signed. For Android packages, the draft includes the signing certificate fingerprint. An installer can compare it with the certificate of an app that is already installed before it offers an update. Before installing an Android package, clients SHOULD fetch the kind 30509 event by certificate hash. They should verify its certificate signature against the certificate embedded in the APK and against the asset's publisher, and check that the proof has not expired or been revoked.

## Trust limits

A valid signature only shows that a particular key published an event. It does not prove that the key belongs to the real developer, that the software is safe, or that a curator's list can be trusted. The proposal gives no guarantee about arbitrary publishers. Clients and users must decide which publisher and curator keys to rely on. This page does not claim any security audit or production interoperability.

## Relation to NIP-89

[NIP-89](/en/topics/nip-89/) handler events advertise which applications can handle which event kinds. This proposal describes the software artifacts and where to get them, so the two cover separate concerns.

---

**Primary sources:**
- [nostr-protocol/nips PR #2526: Zapstore spec](https://github.com/nostr-protocol/nips/pull/2526) (open, unmerged; supersedes [PR #1336](https://github.com/nostr-protocol/nips/pull/1336))

**Mentioned in:**
- [Newsletter #27: Amethyst v1.12.0 release coverage (historical reference)](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #46: Software application catalog proposed as NIP-82](/en/newsletters/2026-10-28-newsletter/#software-application-catalog-proposed-as-nip-82)

**See also:**
- [NIP-89: Application Handlers](/en/topics/nip-89/)
