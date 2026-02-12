---
title: "NIP-96: Almacenamiento de Archivos HTTP"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Media
---

NIP-96 definió cómo subir, descargar y gestionar archivos en servidores de medios HTTP desde clientes Nostr. Ahora marcado como "no recomendado" en favor de Blossom, NIP-96 sigue siendo relevante mientras proyectos transitan entre ambos estándares de medios.

## Cómo Funciona

El cliente descubre las capacidades de un servidor de archivos consultando `/.well-known/nostr/nip96.json`, que retorna la URL de API, tipos de contenido soportados, límites de tamaño y transformaciones de medios disponibles.

Para subir, el cliente envía un POST `multipart/form-data` a la URL de API con cabecera de autorización NIP-98 (un evento Nostr firmado que prueba la identidad del uploader). El servidor retorna metadatos de archivo NIP-94 conteniendo la URL del archivo, hashes SHA-256, tipo MIME y dimensiones.

Las descargas usan solicitudes GET a `<api_url>/<sha256-hash>`, con parámetros de consulta opcionales para transformaciones del lado del servidor como redimensionamiento de imágenes. La eliminación usa DELETE con auth NIP-98. Mediante eventos kind 10096, cada usuario declara sus servidores de subida preferidos.

## Por Qué Fue Obsoletado

NIP-96 ataba las URLs de archivos a servidores específicos. Si un servidor dejaba de funcionar, cada nota Nostr que referenciaba sus URLs perdía los medios. Blossom invierte esto haciendo del hash SHA-256 del contenido el identificador canónico. Cualquier servidor Blossom que aloje el mismo archivo lo sirve en la misma ruta de hash, haciendo el contenido portable entre servidores por defecto.

Blossom también simplifica la API con PUT simple para subidas, GET para descargas, y eventos Nostr firmados (no cabeceras HTTP) para autorización. La obsolescencia ocurrió en septiembre 2025 vía [PR #2047](https://github.com/nostr-protocol/nips/pull/2047).

## La Transición

Servidores como nostr.build y void.cat soportaban NIP-96 y han añadido o migrado a endpoints Blossom. Cada cliente está en distinta etapa de adopción. Angor v0.2.5 añadió configuración de servidor NIP-96 mientras ZSP v0.3.1 sube exclusivamente a servidores Blossom. La coexistencia continuará hasta que las implementaciones restantes de NIP-96 completen la migración.

Los eventos kind 10096 de preferencia de servidor siguen siendo útiles para la selección de servidor Blossom. Los metadatos de archivo NIP-94 (eventos kind 1063) describen propiedades de archivos con independencia de qué protocolo de subida los creó.

---

**Fuentes principales:**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**Mencionado en:**
- [Newsletter #9: Análisis Profundo de NIP](/es/newsletters/2026-02-11-newsletter/#análisis-profundo-de-nip-nip-96-almacenamiento-de-archivos-http-y-la-transición-a-blossom)

**Ver también:**
- [Protocolo Blossom](/es/topics/blossom/)
- [NIP-94: Metadatos de Archivo](/es/topics/nip-94/)
