---
title: "NIP-17: Private Direct Messages"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17 defines private direct messages using NIP-59 gift wrapping for sender privacy. Unlike NIP-04 DMs, which expose the sender in the outer event, NIP-17 hides the sender from relays and casual observers.

## How It Works

Messages are wrapped in multiple encryption layers:
1. The actual message content lives in a rumor event of kind 14.
2. A seal encrypts that content to the recipient.
3. A gift wrap encrypts the seal again and publishes it from a disposable keypair.

The outer gift wrap uses a random, disposable keypair so relays and observers cannot determine who sent the message.

## Message Structure

- **Kind 14** - The actual DM content inside the wrapped layers
- **Kind 1059** - The outer gift wrap event published to relays
- Uses NIP-44 encryption for the payloads inside the wrapping flow
- The spec has been refined to better support interactive DM features such as reactions

## Security and Trust Model

- Relays cannot see the sender (hidden by gift wrap's disposable keypair)
- Recipient is visible (in the `p` tag of the gift wrap)
- Message timestamps are randomized within a window
- No visible threading or conversation grouping on the relay

The recipient still learns who sent the message after unwrapping it. NIP-17 hides sender identity from the network, not from the other participant. That is an important distinction when people describe it as "private DMs."

## Why It Matters

NIP-04 DMs encrypt content but leave metadata visible:
- Sender pubkey is public
- Recipient pubkey is in the `p` tag
- Timestamps are exact

NIP-17 hides the sender at the cost of more complex implementation.

That complexity buys a real privacy improvement. A relay can still see that a wrapped message is addressed to a recipient, but it cannot directly build a sender-recipient graph from outer event metadata the way it can with kind 4 messages.

## Interop Notes

NIP-17 also defines inbox relay lists for private messaging. Clients can publish a kind 10050 event so senders know which relays to target for DM delivery. Keeping DM relay routing separate from public content routing helps avoid publishing private traffic to the wrong places.

---

**Primary sources:**
- [NIP-17 Specification](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - wording cleanup and reaction support update

**Mentioned in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#shopstr-marketplace)
- [Newsletter #5: News](/en/newsletters/2026-01-13-newsletter/#news)
- [Newsletter #13: Vector](/en/newsletters/2026-03-11-newsletter/#vector-v032-ships-nip-77-negentropy-sync-and-mls-improvements)
- [Newsletter #19: NipLock password manager](/en/newsletters/2026-04-22-newsletter/#niplock-ships-a-nip-17-based-password-manager)

**See also:**
- [NIP-04: Encrypted Direct Messages (Deprecated)](/en/topics/nip-04/)
- [NIP-44: Encrypted Payloads](/en/topics/nip-44/)
- [NIP-59: Gift Wrap](/en/topics/nip-59/)
