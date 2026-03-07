---
title: "NIP-57: Zaps"
date: 2025-12-17
translationOf: /en/topics/nip-57.md
translationDate: 2026-03-07
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 define zaps, una forma de vincular pagos Lightning a identidades y contenido de Nostr. Estandariza tanto la solicitud de una factura habilitada para zaps como el evento de recibo que las carteras publican después del pago.

## Cómo funciona

1. El cliente descubre el endpoint LNURL del destinatario desde los metadatos del perfil o una etiqueta `zap` en el evento objetivo.
2. El cliente envía una solicitud de zap kind `9734` firmada al callback LNURL del destinatario, no a los relays.
3. El usuario paga la factura.
4. El servidor de cartera del destinatario publica un recibo de zap kind `9735` en los relays listados en la solicitud de zap.
5. Los clientes validan y muestran el zap.

## Solicitud de zap (kind 9734)

La solicitud de zap es un evento firmado que identifica al pagador y al objetivo. Generalmente incluye:

- Etiqueta `p` con la pubkey del destinatario
- Etiqueta `e` con el evento siendo zappeado (opcional)
- Etiqueta `amount` en millisatoshis
- Etiqueta `relays` listando dónde publicar el recibo

El contenido direccionable puede usar una etiqueta `a` en lugar de, o junto a, una etiqueta `e`. La etiqueta opcional `k` registra el kind del objetivo.

## Recibo de zap (kind 9735)

Publicado por el servidor de cartera del destinatario después de la confirmación del pago. Contiene:

- La solicitud de zap original en una etiqueta `description`
- Etiqueta `bolt11` con la factura pagada
- Etiqueta `preimage` que demuestra el pago

Los clientes deben validar el recibo contra la `nostrPubkey` del LNURL del destinatario, el monto de la factura y la solicitud de zap original. Un recibo sin esa validación es solo una afirmación.

## Confianza y compensaciones

Los zaps son útiles porque hacen los pagos visibles dentro del grafo social, pero el recibo aún es creado por la infraestructura de cartera del destinatario. La propia especificación señala que un recibo de zap no es una prueba universal de pago. Se entiende mejor como una declaración firmada por la cartera de que una factura vinculada a una solicitud de zap fue pagada.

---

**Fuentes primarias:**
- [Especificación NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Mencionado en:**
- [Boletín #1: Noticias](/en/newsletters/2025-12-17-newsletter/#news)
- [Boletín #2: Noticias](/en/newsletters/2025-12-24-newsletter/#news)
- [Boletín #3: Cambios notables de código](/en/newsletters/2025-12-31-newsletter/#amethyst-android)
- [Boletín #9: Actualizaciones de NIP](/en/newsletters/2026-02-11-newsletter/#nip-updates)

**Ver también:**
- [NIP-47: Nostr Wallet Connect](/es/topics/nip-47/)
