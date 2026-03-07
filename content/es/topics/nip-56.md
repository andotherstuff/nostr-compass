---
title: "NIP-56: Reportes"
date: 2026-02-18
translationOf: /en/topics/nip-56.md
translationDate: 2026-03-07
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-56 define eventos de reporte kind `1984`. Permiten a usuarios y aplicaciones publicar señales de moderación sobre cuentas, notas y blobs sin requerir una única autoridad de moderación compartida.

## Cómo funciona

Un reporte debe incluir una etiqueta `p` para la pubkey reportada. Si el reporte es sobre un evento específico, también debe incluir una etiqueta `e` para ese evento. El tipo de reporte aparece como el tercer valor en la etiqueta `p`, `e` o `x` relevante.

## Categorías de reporte

- **nudity**: contenido para adultos
- **malware**: virus, troyanos, ransomware y payloads similares
- **profanity**: lenguaje ofensivo y discurso de odio
- **illegal**: contenido que podría violar leyes
- **spam**: mensajes repetitivos no deseados
- **impersonation**: suplantación de identidad fraudulenta
- **other**: infracciones que no encajan en las categorías anteriores

Los reportes de blobs usan etiquetas `x` con el hash del blob y pueden incluir una etiqueta `server` que apunta al endpoint de alojamiento. Eso hace que NIP-56 sea utilizable para moderación de medios, no solo notas y perfiles.

## Seguridad y modelo de confianza

Los reportes son señales, no veredictos. Los clientes pueden ponderarlos usando confianza social, listas de moderación o roles explícitos de moderador. Los relays también pueden leerlos, pero la especificación advierte contra la moderación totalmente automática porque los reportes son fáciles de manipular.

Se puede agregar clasificación adicional con etiquetas `l` y `L` de NIP-32, lo cual es útil cuando un cliente quiere un vocabulario de moderación más fino que los siete tipos de reporte base.

---

**Fuentes primarias:**
- [Especificación NIP-56](https://github.com/nostr-protocol/nips/blob/master/56.md)

**Mencionado en:**
- [Boletín #10: Actualizaciones de proyectos](/en/newsletters/2026-02-18-newsletter/#notedeck-android-app-store-prep)

**Ver también:**
- [NIP-22: Comment](/es/topics/nip-22/)
