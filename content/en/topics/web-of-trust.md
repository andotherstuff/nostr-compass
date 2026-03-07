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

In Nostr, Web of Trust usually starts from the follow graph in [NIP-02: Follow List](/en/topics/nip-02/) and sometimes adds mutes, reports, or verified identity signals. A client or service picks one or more seed pubkeys that it already trusts, then propagates trust outward through the graph.

1. **Graph construction**: Build a directed graph of follows and optional negative signals
2. **Seed selection**: Start from pubkeys the observer already trusts
3. **Score propagation**: Push rank through the graph with an algorithm such as PageRank or a variant
4. **Cutoffs and normalization**: Limit graph depth, damp low-signal accounts, and normalize the final score for display or filtering

The exact algorithm is not standardized. Two WoT systems can both be valid while producing different rankings because they use different seeds, graph depth, decay rules, or treatments of mutes and reports.

## Why It Matters

WoT gives Nostr a way to rank and filter without a central moderation service. A personalized trust graph is harder to game than a raw follower count because fake accounts still need trust to flow into them from the observer's existing network.

The flip side is cold start. If you follow nobody, a personalized WoT has almost no basis for ranking anything. Many products solve that by shipping starter follows, trusted-provider defaults, or precomputed scores from external services.

## Applications in Nostr

- **Spam Filtering**: Relays can use WoT to filter low-trust content
- **Content Discovery**: Surface content from accounts trusted by your network
- **Payment Directories**: Lightning address lookup with impersonation prevention
- **Relay Policies**: WoT relays accept only notes from trusted pubkeys
- **Decentralized Moderation**: Communities can curate based on trust scores

## Implementation Notes

Because WoT computations require crawling large parts of the network, many clients do not calculate them locally. [NIP-85: Trusted Assertions](/en/topics/nip-85/) exists partly for this reason: it gives clients a way to consume signed third-party WoT calculations when local computation is too expensive.

Existing implementations also answer different questions. A global trust rank is useful for discovery and spam resistance across the whole network. A personalized local score is better for "show me accounts my graph would trust." Reading a WoT number without knowing which model produced it is a common source of confusion.

---

**Primary sources:**
- [NIP-02: Follow List](https://github.com/nostr-protocol/nips/blob/master/02.md)
- [NIP-85: Trusted Assertions](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [DCoSL Protocol](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [NIP-02: Follow List](/en/topics/nip-02/)
