---
title: "NIP-57: Zaps"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 define zaps, una forma de enviar pagos Lightning a usuarios y contenido de Nostr con prueba criptográfica de que el pago ocurrió.

## Cómo Funciona

1. El cliente obtiene la dirección Lightning del destinatario desde su perfil kind 0
2. El cliente solicita una factura del servidor LNURL del destinatario, incluyendo un evento de solicitud de zap
3. El usuario paga la factura
4. El servidor LNURL publica un recibo de zap kind 9735 a los relays Nostr
5. Los clientes muestran el zap en el contenido del destinatario

## Solicitud de Zap (kind 9734)

La solicitud de zap es un evento firmado que demuestra quién envió el zap y a qué contenido. Incluye:
- Etiqueta `p` con la pubkey del destinatario
- Etiqueta `e` con el evento siendo zappeado (opcional)
- Etiqueta `amount` en millisatoshis
- Etiqueta `relays` listando dónde publicar el recibo

## Recibo de Zap (kind 9735)

Publicado por el servidor LNURL después de la confirmación del pago. Contiene:
- La solicitud de zap original en una etiqueta `description`
- Etiqueta `bolt11` con la factura pagada
- Etiqueta `preimage` demostrando el pago

---

**Fuentes primarias:**
- [Especificación NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)
- [Boletín #2: Noticias](/es/newsletters/2025-12-24-newsletter/#news)

**Ver también:**
- [NIP-47: Nostr Wallet Connect](/es/topics/nip-47/)
