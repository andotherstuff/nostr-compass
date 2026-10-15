---
title: "NIP-36: Contenuti sensibili"
date: 2026-10-14
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-36.md
translationDate: 2026-10-15
---

NIP-36 definisce un tag `content-warning` facoltativo con una motivazione facoltativa. I client possono usarlo per nascondere un event finché il lettore non sceglie di visualizzarlo. L'event rimane pubblico.

## Implementazioni

[Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) analizza il tag e la relativa motivazione. [Coracle](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) usa l'impostazione del lettore per i contenuti sensibili e offre un'azione per visualizzarli. [noStrudel](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) controlla le preferenze relative agli avvisi e lo stato di espansione prima di mostrare l'avviso.

---

**Fonti primarie:**
- [Specifica NIP-36](https://github.com/nostr-protocol/nips/blob/master/36.md)

**Menzionato in:**
- [Newsletter #44: Avvisi sui contenuti prima della visualizzazione](/it/newsletters/2026-10-14-newsletter/#content-warnings-before-display)

**Vedi anche:**
- [NIP-32: Etichettatura](/it/topics/nip-32/)
