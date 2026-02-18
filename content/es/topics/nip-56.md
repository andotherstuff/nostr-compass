---
title: "NIP-56: Reporting"
date: 2026-02-18
translationOf: /en/topics/nip-56.md
translationDate: 2026-02-18
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-56 define un mecanismo de reporte usando eventos kind 1984, permitiendo a usuarios y aplicaciones señalar contenido objetable a través de la red Nostr.

## Cómo Funciona

Un usuario publica un evento kind 1984 con una etiqueta `p` que referencia la pubkey que se está reportando. Al reportar una nota específica, una etiqueta `e` referencia el ID de la nota. Ambas etiquetas aceptan un tercer parámetro que especifica la categoría de la infracción.

## Categorías de Reporte

- **nudity**: contenido para adultos
- **malware**: virus, troyanos, ransomware
- **profanity**: lenguaje ofensivo y discurso de odio
- **illegal**: contenido que podría violar leyes
- **spam**: mensajes repetitivos no deseados
- **impersonation**: suplantación de identidad fraudulenta
- **other**: infracciones que no encajan en las categorías anteriores

## Comportamiento de Clientes y Relays

Los clientes pueden usar los reportes de usuarios seguidos para decisiones de moderación, como difuminar contenido cuando múltiples contactos de confianza lo señalan. Los relays deben evitar la moderación automática via reportes debido al riesgo de manipulación; los reportes de moderadores de confianza pueden informar la aplicación manual en su lugar. Se soporta clasificación adicional a través de etiquetas `l` y `L` de NIP-32.

---

**Fuentes primarias:**
- [Especificación NIP-56](https://github.com/nostr-protocol/nips/blob/master/56.md)

**Mencionado en:**
- [Boletín #10: Actualizaciones de Proyectos](/es/newsletters/2026-02-18-newsletter/#notedeck-preparación-para-android-app-store)

**Ver también:**
- [NIP-22: Comment](/es/topics/nip-22/)
