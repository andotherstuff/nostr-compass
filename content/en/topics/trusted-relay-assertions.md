---
title: "Trusted Relay Assertions"
date: 2026-01-21
draft: false
categories:
  - Protocol
  - Relays
---

Trusted Relay Assertions is the idea of publishing signed third-party evaluations of relays on Nostr so clients can choose relays with more context than self-reported metadata alone. The current standardized building block is [NIP-85: Trusted Assertions](/en/topics/nip-85/), which defines how users trust providers and how providers publish signed computed results.

## How It Works

Relay selection has three layers. [NIP-11: Relay Information Document](/en/topics/nip-11/) covers what a relay says about itself. [NIP-66: Relay Discovery and Liveness Monitoring](/en/topics/nip-66/) covers what observers can measure, such as availability and latency. Trusted relay assertions try to fill the remaining gap: what a third party concludes from that data, and whether a client decides to trust that conclusion.

In the broader NIP-85 model, users name trusted providers with kind `10040` events, and providers publish signed addressable assertion events. A relay-scoring application would then need two more pieces that clients agree on: how a relay is identified as the subject, and which result tags represent the score and its supporting evidence.

That distinction is important because the transport and trust delegation are standardized, but the relay-specific scoring model is still an application pattern. Different providers can legitimately disagree about what makes a relay trustworthy.

## Trust Model

Relay trust scores are not objective facts. One provider may prioritize uptime and write throughput, another may prioritize legal jurisdiction, moderation policy, or operator identity, and a third may care most about resistance to surveillance. A useful client should show who produced the score, not just the score itself.

This is also where [Web of Trust](/en/topics/web-of-trust/) enters the picture. If a client already trusts certain people or services, it can prefer relay evaluations coming from that same social neighborhood instead of pretending a single global ranking exists.

## Why It Matters

For [NIP-46](/en/topics/nip-46/) remote signers, wallet connections, or any app that suggests unfamiliar relays, third-party relay evaluations can reduce blind trust in defaults. Combined with [NIP-65](/en/topics/nip-65/) relay lists, clients can separate "which relays do I use" from "which relays do I trust for this task."

The main correctness caveat is scope. January 2026 newsletter coverage described relay trust scoring as a dedicated proposal, but the merged standard in the NIPs repository is the broader [NIP-85: Trusted Assertions](/en/topics/nip-85/) format. Relay scoring remains a use case built on top of that model, not a separate finalized relay-trust wire format.

---

**Primary sources:**
- [NIP-85 Specification](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #1534: Trusted Assertions](https://github.com/nostr-protocol/nips/pull/1534)

**Mentioned in:**
- [Newsletter #6: News](/en/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Newsletter #6: NIP Updates](/en/newsletters/2026-01-21-newsletter/#nip-updates)
- [Newsletter #7: NIP Updates](/en/newsletters/2026-01-28-newsletter/#nip-updates)

**See also:**
- [NIP-11: Relay Information Document](/en/topics/nip-11/)
- [NIP-66: Relay Discovery and Liveness Monitoring](/en/topics/nip-66/)
- [NIP-85: Trusted Assertions](/en/topics/nip-85/)
- [Web of Trust](/en/topics/web-of-trust/)
