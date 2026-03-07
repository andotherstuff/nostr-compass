---
title: "NIP-92: Media Attachments"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

NIP-92 permite a los usuarios adjuntar archivos de medios a eventos de Nostr incluyendo URLs junto con etiquetas de metadatos en línea que describen esos recursos.

## Cómo funciona

Los usuarios colocan URLs de medios directamente en el contenido del evento, por ejemplo en una nota de texto kind `1`. Una etiqueta `imeta` correspondiente añade detalles legibles por máquina para esa URL exacta. Los clientes pueden usar los metadatos para renderizar vistas previas, reservar espacio de diseño y evitar adivinar las propiedades del archivo después de que la nota ya esté en pantalla.

Cada etiqueta `imeta` debería coincidir con una URL en el contenido del evento. Los clientes pueden ignorar etiquetas que no coincidan, lo que da a las implementaciones una regla simple para rechazar metadatos obsoletos o malformados.

## La etiqueta imeta

Cada etiqueta `imeta` debe tener una `url` y al menos otro campo. Los campos soportados incluyen:

- `url` - La URL del medio (requerido)
- `m` - Tipo MIME del archivo
- `dim` - Dimensiones de la imagen (ancho x alto)
- `blurhash` - Blurhash para generación de vista previa
- `alt` - Texto alternativo para accesibilidad
- `x` - Hash SHA-256 (de NIP-94)
- `fallback` - URLs alternativas si la principal falla

Dado que `imeta` puede contener campos de [NIP-94: File Metadata](/es/topics/nip-94/), los clientes pueden reusar el mismo tipo MIME, dimensiones, hash y texto de accesibilidad que ya entenderían para eventos de metadatos de archivo independientes.

## Por qué importa

El beneficio más inmediato es mejor renderizado antes de la descarga. Si `dim` está presente, los clientes pueden reservar la cantidad correcta de espacio para una imagen o video en lugar de reajustar la línea de tiempo después de que el archivo cargue. Si `blurhash` está presente, pueden mostrar una vista previa de bajo costo primero. Si `alt` está presente, el adjunto sigue siendo usable para usuarios con lectores de pantalla y baja visión.

NIP-92 también permite que los clientes mantengan la publicación misma como fuente de verdad. La URL permanece en `content`, así que clientes más antiguos siguen mostrando un enlace simple, mientras que clientes más nuevos pueden transformar la misma nota en una tarjeta de medios más rica.

## Notas de interoperabilidad

NIP-92 es metadatos en línea, no un formato de objeto de medios separado. Si un cliente necesita un registro de archivo reutilizable con su propio evento, [NIP-94: File Metadata](/es/topics/nip-94/) es la mejor opción.

## Ejemplo

```json
["imeta",
  "url https://example.com/image.jpg",
  "m image/jpeg",
  "dim 1920x1080",
  "blurhash LKO2?U%2Tw=w]~RBVZRi}^Xu%LRj"
]
```

---

**Fuentes primarias:**
- [Especificación NIP-92](https://github.com/nostr-protocol/nips/blob/master/92.md)
- [Primal Android PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) - Una implementación concreta de cliente para manejo de dimensiones y relación de aspecto

**Mencionado en:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #6: News](/en/newsletters/2026-01-21-newsletter/#news)

**Ver también:**
- [NIP-94: File Metadata](/es/topics/nip-94/)
