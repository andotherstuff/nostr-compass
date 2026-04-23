---
title: "NIP-53: Actividades en vivo"
date: 2026-04-15
translationOf: /en/topics/nip-53.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Live Streaming
---

NIP-53 define el formato estándar de evento para metadatos de live streaming en Nostr. Un stream se anuncia como un evento direccionable kind `30311`, para que los clientes puedan descubrirlo, mostrar su estado actual y vincular el chat de vuelta al contexto del stream.

## Cómo funciona

Cada stream usa un evento kind `30311` con una etiqueta `d` como identificador estable. El evento suele incluir título y texto de resumen, una etiqueta `streaming` con la URL de reproducción y una etiqueta `status` (`planned`, `live` o `ended`). Como este es un evento direccionable, las actualizaciones reemplazan los metadatos anteriores para el mismo valor `d` en lugar de crear un rastro ilimitado de eventos.

El evento puede incluir etiquetas de tema (`t`), referencias a participantes (`p`) y campos opcionales de cantidad de participantes. El chat en vivo se transporta en eventos kind `1311` que referencian el stream con una etiqueta `a`, lo que mantiene los mensajes de chat vinculados a un registro específico de actividad en vivo.

## Implementaciones

- [Shosho](https://github.com/r0d8lsh0p/shosho-releases) publica metadatos y chat de live stream alrededor de transmisiones nativas de Nostr.
- [Zap.stream](https://zap.stream/) usa eventos Nostr para descubrimiento de streams e interacción.
- [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) usa eventos de chat en vivo kind `1311` en su contexto de radio por internet.
- [Amethyst](https://github.com/vitorpamplona/amethyst) conectó objetivos de zap de [NIP-75](/es/topics/nip-75/) en la pantalla de Live Activities mediante [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469): cada live stream lleva una cabecera de objetivo de recaudación con barra de progreso, botón de zap de un toque y un leaderboard de top zappers calculado a partir de recibos de zap kind `9735` vinculados al evento kind `30311` del stream. El siguiente [PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) añade proof-of-agreement y constructores de eventos NIP-53, y [PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486) lanza una pantalla dedicada de feed de Live Streams con filtrado y descubrimiento.
- [NoorNote v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) añade zaps de un toque desde tarjetas de live stream donde los sats aparecen en la superposición de chat del stream vía NIP-53.

---

**Fuentes primarias:**
- [Especificación NIP-53](https://github.com/nostr-protocol/nips/blob/master/53.md)
- [Amethyst PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) - cabecera del objetivo del live stream y leaderboard de top zappers
- [Amethyst PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) - proof of agreement y constructores de eventos NIP-53

**Mencionado en:**
- [Boletín #18: lanzamiento de WaveFunc](/en/newsletters/2026-04-15-newsletter/)
- [Boletín #19: objetivos de zap de live stream en Amethyst](/en/newsletters/2026-04-22-newsletter/)
- [Boletín #19: NoorNote v0.8.4](/en/newsletters/2026-04-22-newsletter/)

**Ver también:**
- [NIP-29: Grupos basados en relay](/es/topics/nip-29/)
- [NIP-75: Objetivos de zap](/es/topics/nip-75/)
- [NIP-57: Zaps](/es/topics/nip-57/)
- [NIP-C7: Mensajes de chat](/es/topics/nip-c7/)
