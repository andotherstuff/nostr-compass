---
title: "NIP-1B: Network Abuse Reports"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

NIP-1B is a proposed NIP for network abuse reports. It is open and unmerged as nostr-protocol/nips#2548 and is not an accepted NIP. Under the proposal, service operators would publish reports of attacks and probes against their infrastructure as Nostr events. The proposal covers attacks on services in general. It gives operators a way to publish and query reports and does not say how anyone should respond to one.

Each report is an addressable kind 31984 event. An operator corrects a report by publishing a replacement at the same address. Single-letter tags let relay filters search reports by source network, given as a /24 IPv4 or /64 IPv6 prefix. Other tags record the ASN, the targeted application, the user agent and the attempted operation. NIP-32 labels can classify a report further.

The draft sets out several limits. A Tor or VPN exit address in a report does not identify the attacker. Report authors are asked to leave out details that could cause harm. A reporter's signature shows who published a report and does not prove that the allegation is true. The PR author describes a read-only relay that already holds reports. Independent verification of that data is not established in the reviewed evidence, and the data should not be used as a trusted automatic blocklist.

**Primary sources:**
- [nostr-protocol/nips#2548](https://github.com/nostr-protocol/nips/pull/2548)

**Mentioned in:**
- [Newsletter #49 (2026-11-18)](/en/newsletters/2026-11-18-newsletter/#nostr-protocol-nips-2548)

**See also:**
- [NIP-32: Labeling](/en/topics/nip-32/)
- [NIP-56: Reporting](/en/topics/nip-56/)
