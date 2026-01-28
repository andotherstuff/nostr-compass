---
title: "NIP-58: Badges"
date: 2026-01-28
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58 defines a badge system for Nostr, allowing issuers to create badges and award them to users who can then display them on their profiles.

## How It Works

### Badge Definition (Kind 30009)

Issuers create badge definitions as addressable events:

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Early Adopter"],
    ["description", "Joined before 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### Badge Award (Kind 8)

Issuers award badges to users:

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### Badge Display (Kind 30008)

Users choose which badges to display on their profile:

```json
{
  "kind": 30008,
  "tags": [
    ["d", "profile_badges"],
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["e", "award-event-id"]
  ]
}
```

## Use Cases

- **Community Membership**: Prove membership in groups or communities
- **Achievements**: Recognize contributions or milestones
- **Verification**: Third-party attestations (employee, creator, etc.)
- **Access Control**: Gate content or features based on badge ownership

## Trust Model

Badge value depends entirely on the issuer's reputation. Anyone can create badges, so clients should:
- Display issuer information prominently
- Allow users to filter by trusted issuers
- Not treat badges as authoritative without context

## Related

- [NIP-51](/en/topics/nip-51/) - Lists
- [Web of Trust](/en/topics/web-of-trust/)
