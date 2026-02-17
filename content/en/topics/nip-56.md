---
title: "NIP-56: Reporting"
date: 2026-02-18
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-56 defines a reporting mechanism using kind 1984 events, allowing users and applications to flag objectionable content across the Nostr network.

## How It Works

A user publishes a kind 1984 event with a `p` tag referencing the pubkey being reported. When reporting a specific note, an `e` tag references the note ID. Both tags accept a third parameter specifying the violation category.

## Report Categories

- **nudity**: adult content
- **malware**: viruses, trojans, ransomware
- **profanity**: offensive language and hate speech
- **illegal**: content potentially violating laws
- **spam**: unwanted repetitive messages
- **impersonation**: fraudulent identity claims
- **other**: violations not fitting above categories

## Client and Relay Behavior

Clients can use reports from followed users for moderation decisions, such as blurring content when multiple trusted contacts flag it. Relays should avoid automatic moderation via reports due to gaming risks; trusted moderators' reports may inform manual enforcement instead. Additional classification is supported through NIP-32 `l` and `L` tags.

---

**Primary sources:**
- [NIP-56 Specification](https://github.com/nostr-protocol/nips/blob/master/56.md)

**Mentioned in:**
- [Newsletter #10: Project Updates](/en/newsletters/2026-02-18-newsletter/#notedeck-android-app-store-prep)

**See also:**
- [NIP-22: Comment](/en/topics/nip-22/)
