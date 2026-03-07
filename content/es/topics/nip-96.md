---
title: "NIP-96: HTTP File Storage"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Media
---

NIP-96 define cómo los clientes Nostr suben, descargan y gestionan archivos en servidores de medios HTTP. Ahora está marcado como "no recomendado" en favor de Blossom, pero sigue siendo relevante porque servidores y clientes existentes continúan soportándolo durante la transición.

## Cómo funciona

Un cliente descubre las capacidades de un servidor de archivos obteniendo `/.well-known/nostr/nip96.json`. Ese documento publica la URL de la API de subida, URL de descarga opcional, tipos de contenido soportados, límites de tamaño y si el servidor soporta transformaciones de medios o alojamiento delegado.

Para subir, el cliente envía un POST `multipart/form-data` a la URL de la API con una cabecera de autorización [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md). El servidor responde con un objeto de metadatos con forma NIP-94 que incluye la URL del archivo más etiquetas como `ox` para el hash original y, cuando aplique, `x` para el archivo transformado que realmente se servirá.

Las descargas usan `GET <api_url>/<sha256-hash>` con parámetros de consulta opcionales como ancho de imagen. La eliminación usa `DELETE` con auth NIP-98. Los usuarios publican eventos kind `10096` para declarar sus servidores de subida preferidos.

## Detalles del modelo de datos

Un detalle útil es que NIP-96 identifica archivos por el hash del archivo original, incluso cuando el servidor transforma la subida. Eso permite a un cliente eliminar o volver a descargar el recurso por el mismo identificador estable, mientras sigue obteniendo miniaturas generadas por el servidor o variantes recomprimidas cuando estén disponibles.

El documento well-known también soporta `delegated_to_url`, que permite a un relay apuntar clientes a un servidor de almacenamiento HTTP separado. Eso evitó que el software de relay tuviera que implementar la API de medios completa por sí mismo.

## Por qué fue deprecado

NIP-96 ataba las URLs de archivos a servidores específicos. Si un servidor dejaba de funcionar, cada nota Nostr que referenciaba las URLs de ese servidor perdía sus medios. Blossom invierte esto haciendo del hash SHA-256 del contenido del archivo el identificador canónico. Cualquier servidor Blossom que aloje el mismo archivo lo sirve en la misma ruta de hash, haciendo el contenido portable entre servidores por defecto.

Blossom también simplifica la API: PUT simple para subidas, GET para descargas, y eventos Nostr firmados (no cabeceras HTTP) para autorización. La deprecación ocurrió en septiembre 2025 vía [PR #2047](https://github.com/nostr-protocol/nips/pull/2047).

## Notas de interoperabilidad

Servidores como nostr.build y void.cat soportaban NIP-96 y han añadido o migrado a endpoints Blossom. Los clientes están en diversas etapas: Angor v0.2.5 añadió configuración de servidor NIP-96 mientras ZSP v0.3.1 sube exclusivamente a servidores Blossom. La coexistencia continuará hasta que las implementaciones restantes de NIP-96 completen la migración.

Los eventos kind 10096 de preferencia de servidor siguen siendo útiles para la selección de servidor Blossom. Los metadatos de archivo NIP-94 (eventos kind 1063) describen propiedades de archivos independientemente de qué protocolo de subida los creó.

---

**Fuentes primarias:**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**Mencionado en:**
- [Newsletter #9: NIP Deep Dive](/en/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-96-http-file-storage-and-the-transition-to-blossom)

**Ver también:**
- [Blossom Protocol](/es/topics/blossom/)
- [NIP-94: File Metadata](/es/topics/nip-94/)
