---
title: "NIP-28: Chat público"
date: 2026-09-30
draft: false
categories:
  - NIPs
  - Social
translationOf: /en/topics/nip-28.md
translationDate: 2026-10-01
---

NIP-28 describe los canales de chat públicos, los mensajes de los canales y la moderación del lado del cliente como events de Nostr. La especificación actual está marcada como **borrador** y **no recomendada**, y orienta a quienes la implementan hacia NIP-29 para los grupos actuales basados en relays.

## Modelo de events

El kind `40` crea un canal; el kind `41` actualiza sus metadatos; el kind `42` contiene un mensaje. Los kind `43` y `44` permiten a un usuario ocultar un mensaje o silenciar a otro usuario en su cliente. Los tags de los mensajes hacen referencia al event de creación del canal y pueden identificar el mensaje al que se responde. Los relays no están obligados a aplicar esas decisiones de ocultación y silenciamiento del lado del cliente.

El [cambio de la especificación de septiembre de 2022](https://github.com/nostr-protocol/nips/commit/3423a6dfb) convirtió una sala de chat pública en un objeto compartido del protocolo. Comprender ese papel histórico sigue siendo útil, aunque la [especificación actual](https://github.com/nostr-protocol/nips/blob/master/28.md) recomienda una vía diferente para las nuevas implementaciones.

---

**Fuentes primarias:**
- [Especificación de NIP-28 y estado actual](https://github.com/nostr-protocol/nips/blob/master/28.md)
- [Cambio del chat público de septiembre de 2022](https://github.com/nostr-protocol/nips/commit/3423a6dfb)

**Mencionado en:**
- [Boletín #42: Septiembre de 2022](/es/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)

**Véase también:**
- [NIP-29: Grupos basados en relays](/es/topics/nip-29/)
