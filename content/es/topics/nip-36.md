---
title: "NIP-36: Contenido sensible"
date: 2026-10-14
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-36.md
translationDate: 2026-10-15
---

NIP-36 define un tag opcional `content-warning` con un motivo opcional. Los clientes pueden usarlo para ocultar un event hasta que el lector decida mostrarlo. El event sigue siendo público.

## Implementaciones

[Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) analiza el tag y su motivo. [Coracle](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) utiliza la configuración de contenido sensible del lector y ofrece una acción para mostrarlo. [noStrudel](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) comprueba las preferencias de advertencia y el estado de expansión antes de presentar la advertencia.

---

**Fuentes primarias:**
- [Especificación de NIP-36](https://github.com/nostr-protocol/nips/blob/master/36.md)

**Mencionado en:**
- [Boletín #44: Advertencias de contenido antes de mostrarlo](/es/newsletters/2026-10-14-newsletter/#content-warnings-before-display)

**Véase también:**
- [NIP-32: Etiquetado](/es/topics/nip-32/)
