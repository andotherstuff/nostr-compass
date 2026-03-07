---
title: "NIP-94: File Metadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

NIP-94 define un evento de metadatos de archivo (kind 1063) para organizar y clasificar archivos compartidos en Nostr, permitiendo a los relays filtrar y organizar contenido de manera efectiva.

## Cómo funciona

NIP-94 usa kind `1063` como un evento de metadatos independiente para un archivo. El `content` del evento contiene una descripción legible por humanos, mientras que las etiquetas llevan campos legibles por máquina como URL de descarga, tipo MIME, hashes, dimensiones e indicaciones de vista previa.

Esa separación importa porque el evento de metadatos puede ser indexado, filtrado y reutilizado independientemente de cualquier nota que enlace al archivo. Un cliente puede tratar un evento kind `1063` como la descripción canónica de un recurso en lugar de extraer metadatos del texto libre de una publicación.

## Etiquetas requeridas y opcionales

**Etiquetas principales:**
- `url` - Enlace de descarga del archivo
- `m` - Tipo MIME (formato en minúsculas requerido)
- `x` - Hash SHA-256 del archivo

**Etiquetas opcionales:**
- `ox` - Hash SHA-256 del archivo original antes de transformaciones del servidor
- `size` - Tamaño del archivo en bytes
- `dim` - Dimensiones (ancho x alto) para imágenes/video
- `magnet` - Magnet URI para distribución torrent
- `i` - Infohash del torrent
- `blurhash` - Imagen de marcador de posición para vistas previas
- `thumb` - URL de miniatura
- `image` - URL de imagen de vista previa
- `summary` - Extracto de texto
- `alt` - Descripción de accesibilidad
- `fallback` - Fuentes de descarga alternativas
- `service` - Protocolo o tipo de servicio de almacenamiento, como NIP-96

Las etiquetas `ox` y `x` son fáciles de pasar por alto pero útiles en la práctica. `ox` identifica el archivo original subido, mientras que `x` puede identificar la versión transformada que un servidor realmente sirve. Cuando un servidor de medios comprime o redimensiona las subidas, los clientes pueden preservar la identidad del archivo original sin pretender que el blob transformado es idéntico byte por byte.

## Cuándo usarlo

NIP-94 está diseñado para aplicaciones de compartición de archivos en lugar de clientes de contenido social o de formato largo. Las aplicaciones sugeridas incluyen:

- Relays de indexación de torrents
- Plataformas de compartición de portafolios (similar a Pinterest)
- Distribución de configuración y actualizaciones de software
- Bibliotecas y archivos de medios

Si los metadatos del archivo solo necesitan decorar una URL incrustada dentro de otro evento, [NIP-92: Media Attachments](/es/topics/nip-92/) es más ligero. NIP-94 es la mejor opción cuando el archivo mismo debería ser consultable como un objeto de primera clase.

## Notas de interoperabilidad

NIP-94 funciona entre backends de almacenamiento. Un archivo puede subirse a través de [NIP-96: HTTP File Storage](/es/topics/nip-96/), Blossom u otro servicio, y aún así describirse con la misma forma de evento kind `1063`. Por eso el formato de metadatos sobrevive a cualquier protocolo de subida individual.

---

**Fuentes primarias:**
- [Especificación NIP-94](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Mencionado en:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Ver también:**
- [NIP-92: Media Attachments](/es/topics/nip-92/)
- [Blossom](/es/topics/blossom/)
