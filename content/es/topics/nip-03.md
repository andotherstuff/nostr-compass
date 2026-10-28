---
title: "NIP-03: atestaciones de OpenTimestamps para events"
date: 2026-10-28
translationOf: /en/topics/nip-03.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-03 describe cómo publicar una prueba de [OpenTimestamps](https://opentimestamps.org/) para un event de Nostr. La prueba demuestra que el event ya existía en el momento de un bloque concreto de Bitcoin.

**Advertencia:** la especificación actual lleva las etiquetas `draft`, `optional` y `unrecommended`. Según su encabezado, es vulnerable a un ataque específico y necesita una actualización. El texto no describe el ataque. Trata el formato como una referencia histórica y no lo adoptes en trabajos nuevos hasta que se revise la especificación.

## Cómo funciona

Cada prueba se publica como un event independiente de kind 1040. Su tag `e` indica el id del event objetivo, junto con una URL de relay, y su tag `k` registra el kind de ese event. La prueba de OpenTimestamps debe demostrar como digest el propio id del event objetivo. El id no se vuelve a hashear.

El `content` contiene el archivo `.ots` completo, codificado en base64, con al menos una atestación de Bitcoin. La especificación recomienda exactamente una atestación y ninguna atestación pendiente, ya que estas añaden bytes sin ayudar a la verificación.

Para verificarla, se obtiene el event de kind 1040, se decodifica su contenido y se comprueba la prueba contra Bitcoin. Una prueba válida muestra que el id del event quedó consignado a más tardar en el bloque atestiguado. Así se fija un momento máximo posible de creación del event que no depende del propio valor `created_at` del autor. Lo que no demuestra es que el contenido del event sea verdadero.

## Historia

Un [commit del 11 de octubre de 2023](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e) cambió el lugar donde residen las pruebas. Antes de él, una prueba era un campo `ots` adjunto al propio event. Desde entonces, cada prueba es un event independiente de kind 1040 que apunta a su objetivo.

## Fuentes primarias

- [Especificación actual de NIP-03](https://github.com/nostr-protocol/nips/blob/master/03.md)
- [Commit del 11 de octubre de 2023 que traslada las pruebas a events de kind 1040](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e)

## Mencionado en los boletines

- [Boletín n.º 46 (2026-10-28): octubre de 2023, los events aportan pruebas y solicitudes de trabajo](/es/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)

## Véase también

- [NIP-01: protocolo básico](/es/topics/nip-01/)
