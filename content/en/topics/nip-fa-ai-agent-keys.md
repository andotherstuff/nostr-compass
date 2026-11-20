---
title: "NIP-FA (proposed): AI Agent Keys"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

AI Agent Keys is open proposal [#2545](https://github.com/nostr-protocol/nips/pull/2545) in the official NIPs repository, with the draft identifier NIP-FA. It has no connection to the Buzz attestation specification, which also uses the FA label. The proposal lets users carry AI provider configuration from one client to another. A replaceable kind 12000 event holds an ordered list of provider keys and endpoints, encrypted with NIP-44 to the author's own key. Clients ignore public key tags on this event. Each key may be used only with its own URL. Endpoints must use HTTPS unless they are loopback or keyless.

This design has a direct cost. Anyone who holds the account key, or who can perform NIP-44 decryption for it, can spend against the stored provider credentials. Only provider-side limits restrict that spending. The proposal covers portable configuration and does not define an agent framework. No deployment has been verified, and interoperability between providers has not been shown.

**Primary sources:**
- [NIPs PR #2545: AI Agent Keys](https://github.com/nostr-protocol/nips/pull/2545)

**Mentioned in:**
- [Newsletter #49](/en/newsletters/2026-11-18-newsletter/#nostr-protocol-nips-2545)

**See also:**
- [NIP-44: Encrypted payloads](/en/topics/nip-44/)
- [NIP-01: Basic protocol](/en/topics/nip-01/)
- [NAP-LLM](/en/topics/nap-llm/)
