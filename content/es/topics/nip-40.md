---
title: "NIP-40: Marca de Tiempo de Expiración"
date: 2025-12-17
translationOf: /en/topics/nip-40.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
---

NIP-40 define un tag de expiración que indica a los relays cuándo un evento debe ser eliminado.

## Cómo Funciona

Los eventos incluyen un tag `expiration` con una marca de tiempo Unix:

```json
["expiration", "1734567890"]
```

Después de este tiempo, los relays deben eliminar el evento y negarse a servirlo.

## Por Qué Importa

- Contenido efímero que debe desaparecer después de un tiempo establecido
- Ofertas o anuncios de tiempo limitado
- Expiración de listados en marketplaces (ej., Shopstr)
- Reducción de requisitos de almacenamiento de relays

La expiración es una indicación de retención, no un sistema de revocación. Ayuda a alinear el comportamiento de los relays con contenido obsoleto, pero no garantiza el borrado una vez que otro relay, cliente o archivo ya copió el evento.

## Notas de Confianza y Seguridad

- Los relays no están obligados a respetar la expiración (pero la mayoría lo hace)
- Los clientes no deben confiar en la expiración para eliminación de contenido crítico para la seguridad
- Una vez que el contenido es obtenido por otro cliente, puede ser cacheado o re-publicado
- La expiración no oculta que un evento existió. Los IDs de evento, citas o copias fuera de relay pueden seguir existiendo después de que pase la marca de tiempo

---

**Fuentes primarias:**
- [Especificación NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md)

**Mencionado en:**
- [Newsletter #1: Noticias](/en/newsletters/2025-12-17-newsletter/)
- [Newsletter #3: Cambios Notables de Código](/en/newsletters/2025-12-31-newsletter/)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
