---
title: "NIP-68: Feeds centrados en imágenes"
date: 2026-07-29
translationOf: /en/topics/nip-68.md
translationDate: 2026-07-29
draft: false
categories:
  - Media
  - Protocol
---

NIP-68 define events direccionables de imágenes. Ofrece a los clientes una forma portátil de publicar metadatos de imágenes, pies de foto, etiquetas y referencias a archivos de imagen, al tiempo que mantiene el propio event separado del almacenamiento de blobs.

## Cómo funciona

Una imagen usa kind `20` e incluye un tag `title`, mientras la descripción va en `content`. El tag `imeta` describe cada imagen con campos como `url`, `m` para el tipo MIME, `dim` para las dimensiones, texto `alt` y un hash SHA-256 opcional. Varios tags `imeta` permiten que un event represente un conjunto de imágenes.

El event puede incluir tags `p` para las personas representadas o acreditadas, tags `t` para los temas y referencias Nostr habituales. También puede incluir tags de tipo de medio, hash, ubicación y advertencia de contenido para que los clientes puedan filtrar y mostrar las publicaciones de imágenes de forma coherente.

NIP-68 no prescribe un backend de almacenamiento. Los clientes pueden hacer referencia a URL HTTPS corrientes o a un sistema direccionado por contenido como Blossom, siempre que publiquen suficientes metadatos `imeta` para que otro cliente muestre y verifique la imagen.

## Implementaciones

[NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0) añadió etiquetado de imágenes NIP-68 junto con sus funciones de cliente orientadas a imágenes.

---

**Fuentes principales:**
- [Especificación NIP-68](https://github.com/nostr-protocol/nips/blob/master/68.md)
- [NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0)

**Mencionado en:**
- [Newsletter #33: Lanzamientos etiquetados](/es/newsletters/2026-07-29-newsletter/#tagged-releases)

**Véase también:**
- [Protocolo Blossom](/es/topics/blossom/)
- [NIP-94: Metadatos de archivos](/es/topics/nip-94/)
