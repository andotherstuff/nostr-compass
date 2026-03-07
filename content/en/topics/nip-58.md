---
title: "NIP-58: Badges"
date: 2026-01-28
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58 defines a badge system for Nostr. One event defines the badge, another awards it, and a third lets the recipient choose whether to display it on their profile.

## How It Works

### Badge Definition (Kind 30009)

Issuers create badge definitions as addressable events:

```json
{
  "id": "4f4a4b3d9b6f0f7e3d0b0c6f6e4e4a26b5c0d4c92b9f4c07b2d8e6b36d50a111",
  "pubkey": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
  "created_at": 1706054400,
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Early Adopter"],
    ["description", "Joined before 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ],
  "content": "",
  "sig": "abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789"
}
```

### Badge Award (Kind 8)

Issuers award badges to one or more users:

```json
{
  "id": "d9f96f2d8a0b2fbe54d7ff4c36278c5ddf2b8f0f10f3f99c0d9e8a7b6c5d4321",
  "pubkey": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210",
  "created_at": 1706058000,
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ],
  "content": "",
  "sig": "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
}
```

### Badge Display (Kind 30008)

Users choose which badges to display on their profile:

```json
{
  "id": "8c2f0d17f4c9b93d6f31a2d45ef6f0a2b3c4d5e6f708192a3b4c5d6e7f8090ab",
  "pubkey": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "created_at": 1706061600,
  "kind": 30008,
  "tags": [
    ["d", "profile_badges"],
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["e", "award-event-id"]
  ],
  "content": "",
  "sig": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
}
```

In a profile badges event, clients should read `a` and `e` tags as ordered pairs. An `a` tag without its matching award event, or an `e` tag without its matching badge definition, should be ignored.

## Use Cases

- **Community membership**: Show membership in groups or communities
- **Achievements**: Recognize contributions or milestones
- **Attestations**: Let a third party vouch for a role or status
- **Access control**: Gate features or spaces using issuer-backed badges

## Trust Model

Badge value depends entirely on the issuer's reputation. Anyone can create badges, so clients should:

- Display issuer information prominently
- Allow users to filter by trusted issuers
- Not treat badges as authoritative without context

Badge awards are immutable and non-transferable. That makes badges suitable for attestations and acknowledgments, but not for portable credentials in the tokenized sense.

## Implementation Notes

Badge definitions are addressable events, so issuers can update badge artwork or descriptions over time without changing the badge identifier. The award event is the durable record that ties a recipient to that definition at a point in time.

Clients also have latitude in presentation. The spec explicitly allows them to show fewer badges than a user lists and to pick the thumbnail size that fits the available space.

---

**Primary sources:**
- [NIP-58 Specification](https://github.com/nostr-protocol/nips/blob/master/58.md)

**Mentioned in:**
- [Newsletter #7: Five Years of Nostr Januarys](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #12: Five Years of Nostr Februaries](/en/newsletters/2026-03-04-newsletter/)

**See also:**
- [NIP-51: Lists](/en/topics/nip-51/)
- [Web of Trust](/en/topics/web-of-trust/)
