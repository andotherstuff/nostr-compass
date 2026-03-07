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

Kind `24` is a signed plaintext message to one or more recipients. The message body lives in `content`, and `p` tags identify the intended receivers. The spec says clients should send these events to the recipients' [NIP-65](/en/topics/nip-65/) inbox relays and to the sender's outbox relay.

Unlike threaded conversations, these messages have no concept of chat history, room state, or thread roots. They are meant to appear in a notification surface and be understandable on their own.

## Protocol Rules

- Uses `p` tags to identify recipients
- Must not use `e` tags for threading
- May use `q` tags to quote another event
- Works best with [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md) expiration tags so stale notification-style messages disappear over time

## Why It Exists

NIP-A4 gives clients a simpler public-message primitive than a full threaded note. That is useful for mention-style messages, lightweight shoutouts, or one-off notifications where building a permanent conversation tree would add more complexity than value.

The tradeoff is that these messages are public. They are easy to show in a notification UI precisely because they do not create private session state. Anyone can read and reply to them if they see them.

## Interop Notes

NIP-A4 is easy to confuse with direct-message protocols because it targets named recipients, but it is still a public event kind. Clients should not present kind `24` as private messaging or assume any confidentiality beyond relay placement.

---

**Primary sources:**
- [NIP-A4 Specification](https://github.com/nostr-protocol/nips/blob/master/A4.md)
- [NIP-A4 PR](https://github.com/nostr-protocol/nips/pull/1988)

**Mentioned in:**
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
- [NIP-10: Text Note Threading](/en/topics/nip-10/)
