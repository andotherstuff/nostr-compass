---
title: "NIP-17: Mensajes Directos Privados"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17 define mensajes directos privados usando el envoltorio de regalo (gift wrapping) de NIP-59 para la privacidad del remitente. A diferencia de los DMs de NIP-04 que exponen al remitente, los mensajes NIP-17 ocultan quién envió el mensaje. El destinatario permanece visible en el envoltorio de regalo exterior.

## Cómo Funciona

Los mensajes se envuelven en múltiples capas de encriptación:
1. El contenido real del mensaje (kind 14)
2. Un sello que encripta el contenido para el destinatario
3. Un envoltorio de regalo que oculta la identidad del remitente

El envoltorio de regalo exterior usa un par de claves aleatorio y desechable para que los relays y observadores no puedan determinar quién envió el mensaje.

## Estructura del Mensaje

- **Kind 14** - El contenido real del DM (dentro del sello)
- Usa encriptación NIP-44 para el contenido
- Soporta reacciones (kind 7) dentro de conversaciones DM

## Garantías de Privacidad

- Los relays no pueden ver al remitente (oculto por el par de claves desechable del envoltorio de regalo)
- El destinatario es visible (en la etiqueta `p` del envoltorio de regalo)
- Las marcas de tiempo de los mensajes se aleatorizan dentro de una ventana
- No hay hilos visibles ni agrupación de conversaciones en el relay

## Comparación con NIP-04

Los DMs de NIP-04 encriptan el contenido pero dejan los metadatos visibles:
- La pubkey del remitente es pública
- La pubkey del destinatario está en la etiqueta `p`
- Las marcas de tiempo son exactas

NIP-17 oculta al remitente a costa de una implementación más compleja.

---

**Fuentes primarias:**
- [Especificación NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md)

**Mencionado en:**
- [Boletín #1: Actualizaciones de NIP](/es/newsletters/2025-12-17-newsletter/#nip-updates)
- [Boletín #2: Noticias](/es/newsletters/2025-12-24-newsletter/#news)

**Ver también:**
- [NIP-59: Gift Wrap](/es/topics/nip-59/)
