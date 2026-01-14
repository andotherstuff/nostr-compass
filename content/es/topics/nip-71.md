---
title: "NIP-71: Eventos de Video"
date: 2026-01-13
draft: false
categories:
  - Media
  - Protocol
---

NIP-71 define kinds de eventos para contenido de video en Nostr, habilitando el compartir videos con soporte adecuado de metadatos. La especificación cubre tanto eventos de video regulares como eventos de video direccionables, con estos últimos añadidos en enero de 2026 para permitir a los creadores actualizar los metadatos del video sin republicar.

## Kinds de Eventos

NIP-71 define cuatro kinds de eventos divididos en dos categorías basadas en la relación de aspecto y direccionabilidad.

Los eventos de video regulares usan kind 21 para videos horizontales (paisaje) y kind 22 para videos verticales (retrato/shorts). Estos son eventos estándar de Nostr con contenido inmutable una vez publicados.

Los eventos de video direccionables usan kind 34235 para videos horizontales y kind 34236 para videos verticales. Estos son eventos reemplazables parametrizados identificados por la combinación de pubkey, kind y etiqueta `d`. Publicar un nuevo evento con los mismos identificadores reemplaza la versión anterior, permitiendo actualizaciones de metadatos.

## Estructura

Un evento de video direccionable completo incluye campos de identificación, etiquetas de metadatos y la referencia al contenido de video.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 34235,
  "tags": [
    ["d", "my-video-2026-01"],
    ["title", "Introduction to Nostr Video"],
    ["summary", "A walkthrough of NIP-71 video events"],
    ["url", "https://example.com/video.mp4"],
    ["thumb", "https://example.com/thumbnail.jpg"],
    ["duration", "300"],
    ["dim", "1920x1080"],
    ["origin", "youtube:dQw4w9WgXcQ"]
  ],
  "content": "Extended description, transcript, or additional notes about the video.",
  "sig": "sig1234..."
}
```

La etiqueta `d` proporciona un identificador único dentro de tus videos de ese kind, para que puedas tener múltiples videos direccionables usando diferentes valores de `d`. Las etiquetas `title` y `summary` proporcionan el título del video y una descripción corta para mostrar en los clientes. La etiqueta `url` apunta al archivo de video real, mientras que `thumb` proporciona una imagen de vista previa. La etiqueta `duration` especifica la duración en segundos, y `dim` opcionalmente especifica las dimensiones del video.

La etiqueta `origin` rastrea la plataforma de origen cuando se importa contenido de otros servicios. Esto preserva la procedencia al migrar videos de YouTube, Vimeo u otras plataformas al alojamiento de Nostr.

El campo `content` puede contener una descripción extendida, transcripción completa o cualquier texto adicional asociado con el video.

## Por Qué Importan los Eventos Direccionables

Los eventos de video regulares (kinds 21 y 22) son inmutables una vez publicados. Si publicas un video y luego notas un error tipográfico en el título, quieres actualizar la miniatura, o necesitas cambiar la URL de alojamiento porque migraste a un servicio de video diferente, no puedes modificar el evento original. Tu única opción es publicar un nuevo evento con un nuevo ID, lo que rompe cualquier referencia existente y pierde métricas de engagement.

Los eventos de video direccionables resuelven este problema haciendo el evento reemplazable. La combinación de tu pubkey, el kind del evento y la etiqueta `d` identifica únicamente tu video. Cuando publicas un nuevo evento con los mismos identificadores, los relays reemplazan la versión antigua con la nueva. Los clientes que obtienen tu video siempre obtienen los metadatos más recientes.

Esto es particularmente valioso para corregir errores de metadatos después de publicar, actualizar miniaturas a medida que mejoras tu marca, migrar URLs de alojamiento de video al cambiar de proveedores, e importar contenido de plataformas descontinuadas como Vine mientras se preserva la procedencia a través de la etiqueta `origin`.

## Implementaciones

Los eventos de video direccionables (kinds 34235 y 34236) están actualmente implementados en Amethyst y nostrvine. Ambos clientes pueden crear, mostrar y actualizar eventos de video direccionables.

---

**Fuentes primarias:**
- [Especificación NIP-71](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - Actualización de eventos de video direccionables

**Mencionado en:**
- [Newsletter #5: Actualizaciones de NIPs](/es/newsletters/2026-01-13-newsletter/#actualizaciones-de-nips)

**Ver también:**
- [NIP-94: Metadatos de Archivos](/es/topics/nip-94/)
