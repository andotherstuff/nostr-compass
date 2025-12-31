---
title: "NIP-A4: Public Messages"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-A4 defines public messages (kind 24) designed for notification screens, with broad client support as a goal.

## How It Works

Unlike threaded conversations, these messages have no concept of chat history or message chains. They're simple one-off messages intended to appear in a recipient's notification feed.

## Structure

- Uses `q` tags (quotations) rather than `e` tags to avoid threading complications
- No conversation state or history
- Designed for simple public notifications

## Use Cases

- Public acknowledgments or shoutouts
- Broadcast messages to a user
- Notifications that don't need reply threading

---

**Primary sources:**
- [NIP-A4 PR](https://github.com/nostr-protocol/nips/pull/1988)

**Mentioned in:**
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
- [NIP-10: Text Note Threading](/en/topics/nip-10/)
