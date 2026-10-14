---
title: "NIP-36: Sensitive Content"
date: 2026-10-14
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-36 defines an optional `content-warning` tag with an optional reason. Clients can use it to hide an event until the reader reveals it. The event remains public.

## Implementations

[Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) parses the tag and its reason. [Coracle](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) uses the reader's sensitive-content setting and provides a reveal action. [noStrudel](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) checks warning preferences and expanded state before presenting the warning.

---

**Primary sources:**
- [NIP-36 specification](https://github.com/nostr-protocol/nips/blob/master/36.md)

**Mentioned in:**
- [Newsletter #44: Content warnings before display](/en/newsletters/2026-10-14-newsletter/#content-warnings-before-display)

**See also:**
- [NIP-32: Labeling](/en/topics/nip-32/)
