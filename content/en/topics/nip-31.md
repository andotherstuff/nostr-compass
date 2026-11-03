---
title: "NIP-31: Dealing with unknown event kinds"
date: 2026-11-04
draft: false
categories:
  - NIPs
  - Protocol
---

> **Status warning:** The current [NIP-31 specification](https://github.com/nostr-protocol/nips/blob/master/31.md) marks itself `unrecommended` as "unnecessarily bloated," and its status line reads draft, unrecommended and optional. Relays already hold events that use this convention, so this page explains how clients read them. It does not recommend NIP-31 for new protocols.

NIP-31 defines a top-level `alt` tag. The tag holds a short plaintext summary for custom event kinds that are not meant to be read as ordinary text notes.

## How It Works

The author of a custom-kind event adds an `alt` tag with a label a person can read. Clients built around kind 1 do not have to subscribe to every kind they do not recognize. Their users can still come across such an event when a note references it, and the label gives some context even though the client does not implement that kind.

Tag fragment, not a complete event:

```
["alt", "<short plaintext summary>"]
```

A readable label only covers display. It cannot cast a vote, act on a wallet request or perform any other native action of the kind. For richer interaction, the spec points to [NIP-89: Recommended Application Handlers](/en/topics/nip-89/).

## Implementations

In noStrudel's [unknown-event card at commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx), the first `alt` tag is trimmed and becomes the main label, with an optional `Using <client>` line. A missing or blank value yields `Unknown event (kind ...)`, and up to three lines of content appear on their own. The same component resolves the `client` tag through NIP-89 handler templates. It shows an Open button when a shareable address exists and `Open in <client>` when a valid handler link resolves. The explanation and the app dispatch are separate controls.

Amethyst's [UnknownEventDigest.kt at commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) prefers content it classifies as prose and falls back to `alt`. Its parser trims values and takes the first nonblank `alt`. As a result, an event whose first `alt` is blank can get a different label here than in noStrudel. Both descriptions reflect the source code at those commits. Neither confirms how a released version behaves.

## Limits

- `alt` is a tag, so the event ID and signature defined in [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) cover it. A valid signature shows that the author published the label. It does not show that the label is accurate, so a summary can mislead.
- Tags are public. An `alt` on an event with encrypted content exposes its summary and can reveal what the content hides.
- Both properties above come from the NIP-01 event envelope. NIP-31's own text does not state them as requirements.
- A top-level `alt` tag is different from the image-description `alt` field inside `imeta`, and renderers parse them separately.

---

**Primary sources:**
- [NIP-31 Specification](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [noStrudel embedded-unknown.tsx at commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)
- [Amethyst UnknownEventDigest.kt at commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt)

**Mentioned in:**
- [Newsletter #47: NIP Deep Dive](/en/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)

**See also:**
- [NIP-89: Recommended Application Handlers](/en/topics/nip-89/)
- [NIP-73: External Content IDs](/en/topics/nip-73/)
- [NIP-01: Basic protocol flow description](/en/topics/nip-01/)
