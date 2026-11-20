---
title: "NAP-INTENT: Napplet Intents"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

NAP-INTENT is a draft contract in the napplet specifications. These specifications describe how small apps called napplets request services from a host runtime. NAPs are napplet draft contracts, not accepted NIPs. NAP-INTENT covers intent invocation: a napplet asks for an action, and a handler carries it out.

Merged [#106](https://github.com/napplet/naps/pull/106) on `master` combines two duplicated `IntentInvokeOptions` schemas into one. It also converts a bare `naddr` recommendation fragment into a `handlerHint`, which is kept outside the convention's identity and payload. When a caller names a handler explicitly, it uses an opaque catalog identity. That identity is separate from a recommendation coordinate. The host rejects malformed or duplicate hints. The change adds no new operation or capability, and it sets no precedence rule. It brings the existing web projection into line with these rules. The text remains a draft specification.

**Primary sources:**
- [napplet/naps PR #106](https://github.com/napplet/naps/pull/106)

**Mentioned in:**
- [Newsletter #49](/en/newsletters/2026-11-18-newsletter/#origami74-myco)

**See also:**
- [NIP-89: Recommended application handlers](/en/topics/nip-89/)
- [NIP-19: bech32 entities](/en/topics/nip-19/)
- [NAP-WEBMCP](/en/topics/nap-webmcp/)
