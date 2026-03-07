---
title: "NIP-17: Mensajes Directos Privados"
date: 2025-12-17
translationOf: /en/topics/nip-17.md
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17 define mensajes directos privados usando gift wrapping de NIP-59 para proteger la identidad del remitente. A diferencia de los DMs de NIP-04, que exponen al remitente en el evento exterior, NIP-17 oculta al remitente de los relays y observadores casuales.

## Cómo Funciona

Los mensajes se envuelven en múltiples capas de cifrado:
1. El contenido real del mensaje vive en un evento rumor de kind 14.
2. Un sello cifra ese contenido para el destinatario.
3. Un gift wrap cifra el sello de nuevo y lo publica desde un par de claves desechable.

El gift wrap exterior usa un par de claves aleatorio y desechable, de modo que los relays y observadores no pueden determinar quién envió el mensaje.

## Estructura del Mensaje

- **Kind 14** - El contenido real del DM dentro de las capas envueltas
- **Kind 1059** - El evento gift wrap exterior publicado en relays
- Usa cifrado NIP-44 para los payloads dentro del flujo de envoltorio
- La especificación se ha refinado para soportar mejor funciones interactivas de DM como reacciones

## Modelo de Seguridad y Confianza

- Los relays no pueden ver al remitente (oculto por el par de claves desechable del gift wrap)
- El destinatario es visible (en el tag `p` del gift wrap)
- Las marcas de tiempo de los mensajes se aleatorizan dentro de una ventana
- No hay agrupación visible de hilos ni conversaciones en el relay

El destinatario sí descubre quién envió el mensaje al desenvolverlo. NIP-17 oculta la identidad del remitente de la red, no del otro participante. Esa es una distinción importante cuando se describe como "DMs privados".

## Por Qué Importa

Los DMs de NIP-04 cifran el contenido pero dejan los metadatos visibles:
- La pubkey del remitente es pública
- La pubkey del destinatario está en el tag `p`
- Las marcas de tiempo son exactas

NIP-17 oculta al remitente a costa de una implementación más compleja.

Esa complejidad compra una mejora real de privacidad. Un relay aún puede ver que un mensaje envuelto está dirigido a un destinatario, pero no puede construir directamente un grafo remitente-destinatario a partir de los metadatos del evento exterior como sí puede con mensajes kind 4.

## Notas de Interoperabilidad

NIP-17 también define listas de relays de bandeja de entrada para mensajería privada. Los clientes pueden publicar un evento kind 10050 para que los remitentes sepan a qué relays dirigir los DMs. Mantener el enrutamiento de relays de DM separado del enrutamiento de contenido público ayuda a evitar publicar tráfico privado en los lugares incorrectos.

---

**Fuentes primarias:**
- [Especificación NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - Limpieza de redacción y actualización de soporte de reacciones

**Mencionado en:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#shopstr-marketplace)
- [Newsletter #5: News](/en/newsletters/2026-01-13-newsletter/#news)

**Ver también:**
- [NIP-04: Encrypted Direct Messages (Deprecated)](/es/topics/nip-04/)
- [NIP-44: Encrypted Payloads](/es/topics/nip-44/)
- [NIP-59: Gift Wrap](/es/topics/nip-59/)
