---
title: "NIP-30: Emoji Personalizados"
date: 2026-03-04
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-30 define cómo los clientes muestran emoji personalizados en eventos Nostr. Los emoji personalizados se referencian en el contenido del evento usando shortcodes (`:shortcode:`) y se resuelven mediante tags `emoji` que mapean cada shortcode a una URL de imagen.

## Cómo Funciona

Un evento que usa emoji personalizados incluye tags `emoji` junto a las referencias de shortcode en el contenido:

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

Los emoji personalizados pueden organizarse en conjuntos con nombre publicados como eventos reemplazables parametrizados kind 30030. Cada conjunto agrupa emoji relacionados bajo un identificador de tag `d`:

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

Una actualización de marzo de 2026 ([PR #2247](https://github.com/nostr-protocol/nips/pull/2247)) añadió referencias opcionales de dirección de conjunto de emoji en los tags emoji, permitiendo a los clientes abrir el conjunto de origen para navegación o marcadores cuando un usuario hace clic en un emoji.

## Notas de Interoperabilidad

Los emoji personalizados son una función de presentación, no una garantía de transporte. Si un cliente no entiende NIP-30 o no puede obtener la URL de la imagen, debería mostrar el texto `:shortcode:` sin procesar. Ese fallback es la razón por la que los shortcodes legibles importan.

El tag es local al evento a menos que referencie un conjunto. Reusar `:fire:` en dos eventos diferentes no implica un significado global compartido a menos que ambos apunten a la misma imagen o conjunto. Los clientes deben resolver la definición del emoji desde el evento actual primero.

## Reacciones

Los emoji personalizados de NIP-30 también funcionan en eventos de reacción kind 7. Una reacción con `content` establecido a un shortcode y un tag `emoji` coincidente se renderiza como una reacción de emoji personalizado en el evento referenciado:

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
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - Dirección de conjunto de emoji en tags

**Mencionado en:**
- [Newsletter #12: NoorNote v0.5.x](/en/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [Newsletter #12: NIP Updates](/en/newsletters/2026-03-04-newsletter/#nip-updates)
