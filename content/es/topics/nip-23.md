---
title: "NIP-23: Contenido long-form"
date: 2026-04-08
translationOf: /en/topics/nip-23.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Publicación
---

NIP-23 define kind `30023` para contenido de texto long-form en Nostr. A diferencia de las notas cortas kind `1`, los eventos long-form son eventos reemplazables parametrizados (indexados por una etiqueta `d`), soportan formato Markdown e incluyen etiquetas de metadatos para títulos, resúmenes, imágenes y fechas de publicación.

## Cómo funciona

Un evento long-form usa kind `30023` con una etiqueta `d` como identificador único, lo que permite al autor actualizar el contenido publicando un nuevo evento con la misma etiqueta `d`. El campo `content` contiene texto Markdown. Las etiquetas estándar incluyen `title`, `summary`, `image` (URL de la imagen de cabecera), `published_at` (timestamp unix de publicación original) y `t` (hashtags). Como el evento es reemplazable parametrizado, los relays almacenan solo la versión más reciente por etiqueta `d` y por autor.

## Etiquetas clave

- `d` - identificador único del artículo (slug)
- `title` - título del artículo
- `summary` - descripción breve
- `image` - URL de la imagen de cabecera
- `published_at` - timestamp unix de publicación original (distinto de `created_at`, que se actualiza en cada edición)
- `t` - etiquetas de hashtag/tema

## Implementaciones

- [Habla](https://habla.news) - lector y publicador de contenido long-form
- [YakiHonne](https://yakihonne.com) - plataforma de contenido long-form
- [Highlighter](https://highlighter.com) - herramienta de lectura y anotación

---

**Fuentes primarias:**
- [Especificación NIP-23](https://github.com/nostr-protocol/nips/blob/master/23.md)

**Ver también:**
- [NIP-01 (Protocolo básico)](/es/topics/nip-01/)
