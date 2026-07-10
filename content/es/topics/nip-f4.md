---
title: "NIP-F4: Podcasts"
date: 2026-06-03
draft: false
translationOf: /en/topics/nip-f4.md
translationDate: 2026-07-01
categories:
  - NIPs
  - Protocol
  - Media
---

NIP-F4 define cómo los clientes de Nostr referencian, muestran e interactúan socialmente con episodios de podcast. Fusionado el 2026-05-28 tras dos años y tres meses en borrador, la especificación usa eventos de kind 54 para episodios y se diseña en torno a la pila existente de podcasting RSS como una capa complementaria.

## Cómo funciona

Un evento de episodio de podcast kind 54 transporta un tag `title`, un tag `image` opcional, un tag `description`, uno o más tags `imeta` para el archivo de audio (URL, tipo mime, hash, duración, bitrate, código de idioma, URLs de respaldo, indicador de servicio NIP-96), tags de tópico `t` y un tag `alt` NIP-31 para visualización de respaldo.

La decisión de diseño clave es el tag `i`, que transporta el GUID RSS del episodio usando el formato `podcast:item:guid:<guid>`. Esto permite:

- Que un cliente de Nostr muestre un evento kind 54 y lo enlace de vuelta al mismo episodio en cualquier aplicación de podcast compatible con RSS
- Que un cliente de Nostr compatible con RSS muestre los episodios de un podcast existente como eventos kind 54 sin obligar al podcaster a migrar el hospedaje
- Encadenamiento de comentarios entre protocolos vía los tags `<podcast:socialInteract>` y `<podcast:chat>` de Podcasting 2.0

## Coexistencia con RSS

El debate de dos años en el hilo del PR (con el co-autor de Podcasting 2.0 Dave Jones, Alex Gleason, fiatjaf, Mike Terenzio, Pablo F7z y Jeff Gardner) se resolvió en coexistencia. Nostr proporciona la capa social y de descubrimiento mientras que RSS mantiene la fuente de verdad para el archivo de audio y los metadatos del feed. Nostr no duplica la capa de distribución de RSS.

Esto contrasta con intentos anteriores de reemplazar RSS (JSONFeed, RSS 3.0, APIs propietarias de podcast). El namespace de Podcasting 2.0 ya soporta `<podcast:socialInteract>` referenciando eventos de Nostr por ID de nota, por lo que un feed RSS puede declarar su hilo de discusión de Nostr complementario sin requerir que Nostr replique el propio feed.

## Ejemplo de evento

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["imeta", "url https://podcast.example.com/audio/ep42.mp3", "m audio/mpeg", "x b2e0a7a82ac9f3f3a71f1d9a78c381d5be9d1cf19dce258765c17c8a76287c93", "duration 4523", "bitrate 192000", "l en ISO-639-1"],
    ["i", "podcast:item:guid:9b2a4c7d-1e3f-4a5b-8c9d-0e1f2a3b4c5d"],
    ["t", "podcasting"],
    ["alt", "Podcast episode: Why RSS Won (43 min)"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

## Implementaciones

- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - Pantalla dedicada de podcast con lista de episodios y reproductor integrado (primera implementación importante en un cliente, mayo 2026)
- [Wavlake](https://wavlake.com) - La mayor plataforma nativa de Nostr de música y podcasting, se espera que se alinee con kind 54 para contenido de podcast
- [Fountain](https://fountain.fm) - Aplicación de podcast de Bitcoin, se espera que puentee RSS y NIP-F4

## Cuestiones abiertas

La especificación fusionada deja varias cuestiones de diseño para que las implementaciones converjan:

- Se recomiendan pubkeys por creador pero no son obligatorias, por lo que plataformas como Wavlake que publican muchos creadores bajo una sola pubkey siguen siendo válidas
- Los comentarios y discusión por episodio usan el hilado genérico NIP-22 y notas de línea de tiempo kind 1 en lugar de un kind dedicado de comentario de episodio
- Los metadatos por podcast (anfitrión, red, idioma, licencia) viven o bien en los metadatos kind 0 del publicador o en un registro separado a nivel de podcast kind 54

---

**Fuentes primarias:**
- [Especificación NIP-F4](https://github.com/nostr-protocol/nips/blob/master/F4.md)
- [PR #1093](https://github.com/nostr-protocol/nips/pull/1093) - Propuesta original, fusionada el 2026-05-28 tras dos años de discusión
- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - Primera implementación importante en un cliente

**Mencionado en:**
- [Boletín #25: Actualizaciones NIP y análisis en profundidad](/es/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-f4-podcasts)
- [Boletín #27: Amethyst v1.12.0 incorpora wallets Cashu, nutzaps, un driver CLINK y auto-reparación de Tor](/es/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Véase también:**
- [NIP-22 (Comentarios)](https://github.com/nostr-protocol/nips/blob/master/22.md)
- [NIP-31 (Tags alt)](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [NIP-94 (Metadatos de archivo)](/es/topics/nip-94/)
- [NIP-96 (Almacenamiento de archivos HTTP)](/es/topics/nip-96/)
- [Podcasting 2.0](https://podcasting2.org)
