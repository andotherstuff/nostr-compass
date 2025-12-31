---
title: "Web of Trust"
date: 2025-12-31
draft: false
categories:
  - Trust
  - Social Graph
---

Web of Trust (WoT) is a decentralized trust model where reputation and trustworthiness are derived from social graph relationships rather than central authorities.

## How It Works

In Nostr, Web of Trust leverages the follow graph (NIP-02 contact lists) and report events to calculate trust scores:

1. **Graph Construction**: A directed graph is built from pubkeys, events, and their relationships (follows, mutes, reports)
2. **Weight Assignment**: Initial weights are assigned to known-trustworthy pubkeys (e.g., those with verified NIP-05 identifiers)
3. **Iterative Propagation**: Trust scores flow through the network using algorithms similar to PageRank
4. **Sybil Resistance**: If an attacker creates many fake accounts, the trust passed to them is divided by the number of fakes

## Key Properties

- **Decentralized**: No central authority determines reputation
- **Personalized**: Trust can be calculated from each user's perspective based on who they follow
- **Sybil-Resistant**: Bot farms cannot easily game the system due to trust dilution
- **Composable**: Can be applied to spam filtering, content moderation, relay admission, and payment directories

## Applications in Nostr

- **Spam Filtering**: Relays can use WoT to filter low-trust content
- **Content Discovery**: Surface content from accounts trusted by your network
- **Payment Directories**: Lightning address lookup with impersonation prevention
- **Relay Policies**: WoT relays accept only notes from trusted pubkeys
- **Decentralized Moderation**: Communities can curate based on trust scores

## Implementations

Several projects implement Web of Trust for Nostr:
- **Nostr.Band Trust Rank**: PageRank-style scoring for the network
- **WoT Relays**: Relays filtering by social distance
- **DCoSL**: Protocol for decentralized reputation systems
- **Noswot**: Trust scoring based on follows and reports

---

**Primary sources:**
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [DCoSL Protocol](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [NIP-02: Follow List](/en/topics/nip-02/)
