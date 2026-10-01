---
title: "NIP-26: Firma delegada de events"
date: 2026-09-30
draft: false
categories:
  - NIPs
  - Identity
translationOf: /en/topics/nip-26.md
translationDate: 2026-10-01
---

NIP-26 documenta una forma de que una clave de Nostr autorice a otra clave a firmar un conjunto limitado de events. Su especificación actual está marcada como **borrador** y **no recomendada**, por lo que recoge un diseño anterior en lugar de ofrecer orientación para una nueva integración.

## Cómo funciona

La clave de la cuenta firma un token de delegación que identifica la clave delegada y las condiciones. Las condiciones pueden restringir los valores de kind de los events y sus tiempos de `created_at`. La clave delegada firma el event con su propia clave y adjunta el token en una tag `delegation`. Un lector debe verificar tanto la firma del event como el token de delegación conforme a esas condiciones. Los relays que admiten este esquema también pueden buscar por delegante.

El modelo permite que una aplicación publique sin disponer de la clave de firma principal de la cuenta. Sus requisitos adicionales de validación y búsqueda en relays explican por qué las implementaciones no pueden considerar una firma ordinaria de event como prueba suficiente de una identidad delegada. La [especificación actual](https://github.com/nostr-protocol/nips/blob/master/26.md) señala explícitamente que este enfoque no se recomienda.

---

**Fuentes primarias:**
- [Especificación de NIP-26 y estado actual](https://github.com/nostr-protocol/nips/blob/master/26.md)
- [Texto sobre firma delegada de septiembre de 2022](https://github.com/nostr-protocol/nips/commit/b62aa418d)

**Mencionado en:**
- [Boletín #42: Septiembre de 2022](/es/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)
