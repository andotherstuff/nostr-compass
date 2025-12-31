---
title: "NIP-94: File Metadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2025-12-31
draft: false
categories:
  - Multimedia
  - Protocolo
---

NIP-94 define un evento de metadatos de archivo (kind 1063) para organizar y clasificar archivos compartidos en Nostr, permitiendo a los relays filtrar y organizar contenido de manera efectiva.

## Cómo Funciona

1. El usuario sube un archivo a un servicio de alojamiento
2. Se publica un evento kind 1063 con metadatos sobre el archivo
3. El contenido del evento contiene una descripción legible por humanos
4. Tags estructurados proporcionan metadatos legibles por máquinas
5. Clientes especializados pueden organizar y mostrar archivos sistemáticamente

## Tags Requeridos y Opcionales

**Tags principales:**
- `url` - Enlace de descarga del archivo
- `m` - MIME type (formato en minúsculas requerido)
- `x` - Hash SHA-256 del archivo

**Tags opcionales:**
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

## Casos de Uso

NIP-94 está diseñado para aplicaciones de compartición de archivos en lugar de clientes de contenido social o de formato largo. Las aplicaciones sugeridas incluyen:

- Relays de indexación de torrents
- Plataformas de compartición de portafolios (similar a Pinterest)
- Distribución de configuración y actualizaciones de software
- Bibliotecas y archivos de medios

---

**Fuentes principales:**
- [Especificación NIP-94](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Mencionado en:**
- [Newsletter #3: Resumen de Diciembre](/es/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Ver también:**
- [NIP-92: Archivos Adjuntos de Medios](/es/topics/nip-92/)
- [Blossom](/es/topics/blossom/)
