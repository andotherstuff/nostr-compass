---
title: "NIP-57: Zaps"
date: 2025-12-17
translationOf: /en/topics/nip-57.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 define zaps, una forma de adjuntar pagos Lightning a identidades y contenido de Nostr. Estandariza tanto la solicitud de una invoice habilitada para zap como el evento de recibo que las carteras publican después del pago.

## Cómo funciona

1. El cliente descubre el endpoint LNURL del destinatario a partir de los metadatos del perfil o de una etiqueta `zap` en el evento objetivo.
2. El cliente envía una solicitud de zap kind `9734` firmada al callback LNURL del destinatario, no a los relays.
3. El usuario paga la invoice.
4. El servidor de la cartera del destinatario publica un recibo de zap kind `9735` en los relays listados en la solicitud de zap.
5. Los clientes validan y muestran el zap.

## Solicitud de zap (kind 9734)

La solicitud de zap es un evento firmado que identifica al pagador y al objetivo previsto. Suele incluir:

- Etiqueta `p` con la pubkey del destinatario
- Etiqueta `e` con el evento que recibe el zap (opcional)
- Etiqueta `amount` en millisatoshis
- Etiqueta `relays` que lista dónde publicar el recibo

El contenido direccionable puede usar una etiqueta `a` en lugar de, o junto con, una etiqueta `e`. La etiqueta opcional `k` registra el kind del objetivo.

## Recibo de zap (kind 9735)

Lo publica el servidor de la cartera del destinatario después de la confirmación del pago. Contiene:

- La solicitud de zap original en una etiqueta `description`
- Etiqueta `bolt11` con la invoice pagada
- Etiqueta `preimage` que prueba el pago

Los clientes deberían validar el recibo frente a la `nostrPubkey` LNURL del destinatario, el monto de la invoice y la solicitud de zap original. Un recibo sin esa validación es solo una afirmación.

## Confianza y tradeoffs

Los zaps son útiles porque hacen visibles los pagos dentro del grafo social, pero el recibo sigue siendo creado por la infraestructura de cartera del destinatario. La propia especificación señala que un recibo de zap no es una prueba universal de pago. Se entiende mejor como una declaración firmada por la cartera de que se pagó una invoice vinculada a una solicitud de zap.

Un cliente que valida debe comprobar cuatro cosas antes de mostrar un recibo como zap: que la firma del recibo coincide con la `nostrPubkey` anunciada en la respuesta LNURL del destinatario, que el monto de la invoice `bolt11` coincide con la etiqueta `amount` de la solicitud de zap embebida, que el hash de descripción de la invoice compromete la solicitud de zap serializada y que el `preimage` hashea al `payment_hash` de la invoice. Los clientes que renderizan conteos agregados de zaps sin realizar estas comprobaciones son trivialmente falseables por un atacante que publique eventos kind `9735` forjados.

## Zaps privados y anónimos

Los zaps privados añaden una capa de confidencialidad encima. Un remitente puede cifrar el `content` de la solicitud de zap para el destinatario e incluir una etiqueta `anon` en la solicitud externa, de modo que la red de relays vea el objetivo del pago pero no pueda leer la nota adjunta. Un zap anónimo va un paso más allá: el cliente genera un keypair efímero nuevo para la propia solicitud de zap, así que el recibo sigue probando que hubo un pago, pero el destinatario no puede vincular el zap con la pubkey de largo plazo del remitente.

## Objetivos de zap y splits

NIP-57 sustenta el sistema de objetivos de zap especificado en [NIP-75](/es/topics/nip-75/). Un objetivo es un evento kind `9041` que declara una cantidad objetivo y un conjunto de relays donde cuentan los recibos, y los clientes calculan el progreso sumando montos validados `bolt11` de eventos kind `9735` coincidentes.

Los zap splits, definidos en un apéndice del NIP, permiten que un destinatario publique un perfil kind `0` con múltiples etiquetas `zap` ponderadas para que un único pago de zap se divida atómicamente entre varias pubkeys. [Amethyst](https://github.com/vitorpamplona/amethyst), [Damus](https://github.com/damus-io/damus) y [noStrudel](https://github.com/hzrd149/nostrudel) implementan el pago dividido de extremo a extremo.

---

**Fuentes primarias:**
- [Especificación NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/)
- [Boletín #2: Noticias](/es/newsletters/2025-12-24-newsletter/)
- [Boletín #3: Cambios notables de código](/es/newsletters/2025-12-31-newsletter/)
- [Boletín #9: Actualizaciones de NIP](/es/newsletters/2026-02-11-newsletter/)
- [Boletín #19: Análisis de NIP](/en/newsletters/2026-04-22-newsletter/)

**Ver también:**
- [NIP-47: Nostr Wallet Connect](/es/topics/nip-47/)
- [NIP-75: Objetivos de zap](/es/topics/nip-75/)
- [NIP-53: Actividades en vivo](/es/topics/nip-53/)
