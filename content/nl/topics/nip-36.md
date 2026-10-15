---
title: "NIP-36: Gevoelige inhoud"
date: 2026-10-14
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-36.md
translationDate: 2026-10-15
---

NIP-36 definieert een optionele `content-warning` tag met een optionele reden. Clients kunnen deze gebruiken om een event te verbergen totdat de lezer het zichtbaar maakt. Het event blijft openbaar.

## Implementaties

[Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) verwerkt de tag en de bijbehorende reden. [Coracle](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) gebruikt de instelling van de lezer voor gevoelige inhoud en biedt een optie om de inhoud zichtbaar te maken. [noStrudel](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) controleert de waarschuwingsvoorkeuren en of de inhoud is uitgeklapt voordat de waarschuwing wordt getoond.

---

**Primaire bronnen:**
- [NIP-36-specificatie](https://github.com/nostr-protocol/nips/blob/master/36.md)

**Vermeld in:**
- [Nieuwsbrief #44: Inhoudswaarschuwingen vóór weergave](/nl/newsletters/2026-10-14-newsletter/#content-warnings-before-display)

**Zie ook:**
- [NIP-32: Labelen](/nl/topics/nip-32/)
