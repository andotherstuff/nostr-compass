---
title: "NIP-73: IDs de Contenido Externo"
date: 2026-02-04
translationOf: /en/topics/nip-73.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
---

NIP-73 define una forma estándar de referenciar contenido externo dentro de eventos Nostr. Usa etiquetas `i` para el identificador en sí y etiquetas `k` para el tipo de identificador, de modo que los clientes puedan agrupar la discusión alrededor del mismo libro, sitio web, episodio de podcast, ubicación, hashtag u objeto de blockchain.

## Cómo Funciona

Un evento que usa NIP-73 incluye una etiqueta `i` que contiene un identificador externo normalizado y una etiqueta `k` que describe qué tipo de identificador es. Los clientes pueden entonces consultar todos los eventos que referencian el mismo tema.

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

La especificación cubre varias familias de identificadores, incluyendo:

- URLs web normalizadas sin fragmento
- ISBNs para libros
- ISANs para películas
- geohashes y códigos ISO 3166 de país o subdivisión
- GUIDs de feed, episodio y editor de podcasts
- hashtags
- identificadores de transacciones y direcciones de blockchain

## Reglas de Normalización

El detalle principal orientado al lector en NIP-73 es la normalización. El mismo sujeto debe mapearse a una única cadena canónica; de lo contrario, los clientes dividen la discusión entre múltiples identificadores que significan lo mismo.

Ejemplos de la especificación:

- los geohashes usan `geo:<valor>` y deben ser en minúsculas
- los códigos de país y subdivisión usan `iso3166:<código>` y deben ser en mayúsculas
- los ISBNs omiten guiones
- las URLs web eliminan fragmentos
- los hashes de transacciones de blockchain usan hexadecimal en minúsculas

Eso suena menor, pero es la diferencia entre una conversación compartida y varios índices incompatibles.

## Patrones Útiles

NIP-73 es una capa de referencia general, no un formato de contenido. Una nota de formato largo puede apuntar a un ISBN de libro, una reseña puede apuntar a un ISAN de película, y una publicación local puede apuntar a un geohash o código de país sin inventar una etiqueta personalizada cada vez.

La especificación también permite una pista de URL opcional como segundo valor de una etiqueta `i`. Eso da a los clientes un enlace de respaldo cuando no tienen un renderizador personalizado para el tipo de identificador.

## Por Qué Importa

Nostr ya tiene referencias internas fuertes para eventos y perfiles. NIP-73 extiende esa idea a cosas fuera de Nostr. Una vez que los identificadores están normalizados, los comentarios, calificaciones, highlights y aserciones de confianza pueden todos adjuntarse al mismo sujeto externo a través de diferentes clientes.

Por esto NIP-85 se construye sobre NIP-73. Las Trusted Assertions pueden calificar no solo usuarios y eventos, sino también identificadores NIP-73 como libros, sitios web, hashtags y ubicaciones.

---

**Fuentes primarias:**
- [Especificación NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Agrega códigos de país y subdivisión ISO 3166

**Mencionado en:**
- [Newsletter #8: Actualizaciones de NIP](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Newsletter #10: Análisis Profundo NIP-85](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)

**Ver también:**
- [NIP-85: Trusted Assertions](/es/topics/nip-85/)
