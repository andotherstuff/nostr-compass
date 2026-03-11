---
title: "NIP-59: Gift Wrap"
date: 2025-12-17
translationOf: /en/topics/nip-59.md
translationDate: 2026-03-11
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59 define gift wrap, una forma de encapsular un evento para que los relays y observadores externos no identifiquen al remitente real a partir del evento exterior que reciben.

## Estructura

Un evento gift-wrapped tiene tres capas:

1. **Rumor** - El evento objetivo sin firma.
2. **Seal** (kind `13`) - El rumor cifrado para el destinatario y firmado por el remitente real.
3. **Gift Wrap** (kind `1059`) - El seal cifrado de nuevo y firmado por una clave aleatoria de un solo uso.

El seal debe tener etiquetas vacías. El gift wrap exterior generalmente lleva la etiqueta `p` del destinatario para que los relays puedan enrutarlo.

## Qué oculta

Gift wrap oculta al remitente de los relays y observadores de la red porque el evento exterior está firmado por una clave desechable. El destinatario, sin embargo, puede descifrar el seal interior e identificar qué clave de largo plazo lo firmó. Así que la ganancia de privacidad es protección de metadatos en la capa de transporte, no anonimato frente al destinatario.

La especificación también recomienda aleatorizar los timestamps del wrapper y, cuando sea posible, usar relays que requieran autenticación y solo sirvan eventos envueltos al destinatario previsto. Sin esos comportamientos del relay, los metadatos del destinatario pueden filtrarse de todas formas.

## Notas operativas

Gift wrap no es un protocolo de mensajería por sí mismo. Otros protocolos, como sistemas de mensajería privada, lo usan como bloque de construcción.

Los relays pueden optar por no almacenar eventos envueltos durante mucho tiempo porque no son públicamente útiles. La especificación también permite proof-of-work en el wrapper exterior cuando las implementaciones quieren resistencia extra contra spam.

## Casos de uso

- Mensajes directos privados (NIP-17)
- Notas solo para amigos (propuesta NIP-FR)
- Payloads de notificaciones push (propuesta NIP-9a)
- Cualquier escenario que requiera privacidad del remitente frente a la red

---

**Fuentes primarias:**
- [Especificación NIP-59](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Mencionado en:**
- [Boletín #8: NIP Deep Dive](/es/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-59-gift-wrap)
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)
- [Boletín #1: Actualizaciones de NIP](/es/newsletters/2025-12-17-newsletter/#nip-updates)
- [Boletín #3: Resumen de diciembre](/es/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Boletín #15: PRs abiertos](/es/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**Ver también:**
- [NIP-17: Mensajes directos privados](/es/topics/nip-17/)
