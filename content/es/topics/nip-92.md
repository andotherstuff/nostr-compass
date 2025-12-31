---
title: "NIP-92: Media Attachments"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2025-12-31
draft: false
categories:
  - Medios
  - Protocolo
---

NIP-92 permite a los usuarios adjuntar archivos de medios a eventos de Nostr incluyendo URLs junto con etiquetas de metadatos en línea que describen esos recursos.

## Cómo Funciona

1. El usuario coloca URLs de medios directamente en el contenido del evento (por ejemplo, en una nota de texto kind 1)
2. Una etiqueta `imeta` (metadatos en línea) correspondiente proporciona detalles sobre cada URL
3. Los clientes pueden reemplazar las URLs imeta con vistas previas enriquecidas basadas en los metadatos
4. Los metadatos generalmente se generan automáticamente cuando los archivos se suben durante la composición

## La Etiqueta imeta

Cada etiqueta `imeta` debe tener una `url` y al menos otro campo. Los campos soportados incluyen:

- `url` - La URL del medio (requerido)
- `m` - Tipo MIME del archivo
- `dim` - Dimensiones de la imagen (ancho x alto)
- `blurhash` - Blurhash para generación de vista previa
- `alt` - Texto alternativo para accesibilidad
- `x` - Hash SHA-256 (de NIP-94)
- `fallback` - URLs alternativas si la principal falla

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

**Mencionado en:**
- [Boletín #3: Resumen de Diciembre](/es/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Ver también:**
- [NIP-94: Metadatos de Archivo](/es/topics/nip-94/)
