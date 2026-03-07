---
title: "NIP-56: Reporting"
date: 2026-02-18
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-56 defines kind `1984` report events. They let users and apps publish moderation signals about accounts, notes, and blobs without requiring a single shared moderation authority.

## How It Works

A report must include a `p` tag for the reported pubkey. If the report is about a specific event, it must also include an `e` tag for that event. The report type appears as the third value in the relevant `p`, `e`, or `x` tag.

## Report Categories

- **nudity**: adult content
- **malware**: viruses, trojans, ransomware, and similar payloads
- **profanity**: offensive language and hate speech
- **illegal**: content potentially violating laws
- **spam**: unwanted repetitive messages
- **impersonation**: fraudulent identity claims
- **other**: violations not fitting above categories

Blob reports use `x` tags with the blob hash and may include a `server` tag pointing at the hosting endpoint. That makes NIP-56 usable for media moderation, not just notes and profiles.

## Security and Trust Model

Reports are signals, not verdicts. Clients can weight them using social trust, moderation lists, or explicit moderator roles. Relays can read them too, but the spec warns against fully automatic moderation because reports are easy to game.

Additional classification can be added with NIP-32 `l` and `L` tags, which is useful when a client wants a finer moderation vocabulary than the base seven report types.

---

**Primary sources:**
- [NIP-56 Specification](https://github.com/nostr-protocol/nips/blob/master/56.md)

**Mentioned in:**
- [Newsletter #10: Project Updates](/en/newsletters/2026-02-18-newsletter/#notedeck-android-app-store-prep)

**See also:**
- [NIP-22: Comment](/en/topics/nip-22/)
