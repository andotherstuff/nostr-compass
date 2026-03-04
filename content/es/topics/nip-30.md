---
title: "NIP-30: Emoji Personalizados"
date: 2026-03-04
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-04
draft: false
categories:
  - NIP
  - Social
---

NIP-30 define cómo los clientes muestran emoji personalizados en eventos Nostr. Los emoji personalizados se referencian en el contenido del evento usando shortcodes (`:shortcode:`) y se resuelven mediante etiquetas `emoji` que mapean cada shortcode a una URL de imagen.

## Cómo Funciona

Un evento que usa emoji personalizados incluye etiquetas `emoji` junto a las referencias de shortcode en el contenido:

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

Los clientes reemplazan `:gleam:` y `:nostrich:` en el contenido renderizado con imágenes en línea desde las URLs especificadas. Los shortcodes deben ser alfanuméricos (se permiten separadores de guion bajo), y las URLs de imagen deben apuntar a imágenes pequeñas y cuadradas adecuadas para visualización en línea.

## Conjuntos de Emoji

Los emoji personalizados pueden organizarse en conjuntos con nombre publicados como eventos reemplazables parametrizados kind 30030. Cada conjunto agrupa emoji relacionados bajo un identificador de etiqueta `d`:

```json
{
  "kind": 30030,
  "tags": [
    ["d", "nostr-animals"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"],
    ["emoji", "nostrcat", "https://example.com/nostrcat.png"]
  ]
}
```

Una actualización de marzo de 2026 ([PR #2247](https://github.com/nostr-protocol/nips/pull/2247)) añadió referencias opcionales de dirección de conjunto de emoji en las etiquetas emoji, permitiendo a los clientes abrir el conjunto de origen para navegación o marcadores cuando un usuario hace clic en un emoji.

## Reacciones

Los emoji personalizados de NIP-30 también funcionan en eventos de reacción kind 7. Una reacción con `content` establecido a un shortcode y una etiqueta `emoji` coincidente se renderiza como una reacción de emoji personalizado en el evento referenciado:

```json
{
  "kind": 7,
  "content": ":fire:",
  "tags": [
    ["emoji", "fire", "https://example.com/fire.gif"],
    ["e", "<event-id>"]
  ]
}
```

---

**Fuentes primarias:**
- [Especificación NIP-30](https://github.com/nostr-protocol/nips/blob/master/30.md)
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - Dirección de conjunto de emoji en etiquetas

**Mencionado en:**
- [Boletín #12: NoorNote v0.5.x](/es/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [Boletín #12: Actualizaciones de NIPs](/es/newsletters/2026-03-04-newsletter/#nip-updates)
