---
title: "NIP-36: Conteúdo sensível"
date: 2026-10-14
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-36.md
translationDate: 2026-10-15
---

O NIP-36 define uma tag opcional `content-warning` com um motivo também opcional. Os clientes podem usá-la para ocultar um event até que o leitor decida revelá-lo. O event permanece público.

## Implementações

[Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) interpreta a tag e seu motivo. [Coracle](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) usa a configuração de conteúdo sensível do leitor e oferece uma ação para revelar o conteúdo. [noStrudel](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) verifica as preferências de aviso e o estado de expansão antes de apresentar o aviso.

---

**Fontes primárias:**
- [Especificação do NIP-36](https://github.com/nostr-protocol/nips/blob/master/36.md)

**Mencionado em:**
- [Newsletter #44: Avisos de conteúdo antes da exibição](/pt/newsletters/2026-10-14-newsletter/#content-warnings-before-display)

**Veja também:**
- [NIP-32: Rotulagem](/pt/topics/nip-32/)
